"""Shared runtime state for the Auto-Organizer control entities."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import label_registry as lr
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.util import dt as dt_util

from .const import DOMAIN, MANAGED_MARKER, NAME, SCOPE_AREAS, SCOPE_BOTH, SCOPE_LABELS
from .labeler import Labeler, LabelerOptions


@dataclass
class AutoOrganizerRuntime:
    """Holds the labeler plus the state driven by the control entities."""

    hass: HomeAssistant
    entry: ConfigEntry
    labeler: Labeler
    options_factory: Callable[[], LabelerOptions]
    scope: str = SCOPE_BOTH
    dry_run: bool = False
    last_run: dict | None = None
    stats: dict = field(default_factory=dict)
    _listeners: list[Callable[[], None]] = field(default_factory=list)

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.entry.entry_id)},
            name=NAME,
            manufacturer="Auto-Organizer",
            entry_type=DeviceEntryType.SERVICE,
        )

    @callback
    def add_listener(self, cb: Callable[[], None]) -> Callable[[], None]:
        """Register a state-changed callback; returns an unsubscribe."""
        self._listeners.append(cb)

        def _remove() -> None:
            if cb in self._listeners:
                self._listeners.remove(cb)

        return _remove

    @callback
    def _notify(self) -> None:
        for cb in list(self._listeners):
            cb()

    @callback
    def refresh_stats(self) -> dict:
        """Recompute registry statistics and notify listeners."""
        ent_reg = er.async_get(self.hass)
        label_reg = lr.async_get(self.hass)
        dev_reg = dr.async_get(self.hass)

        managed = {
            label.label_id
            for label in label_reg.async_list_labels()
            if label.description == MANAGED_MARKER
        }

        names = {label.label_id: label.name for label in label_reg.async_list_labels()}
        per_label: dict[str, int] = {}

        total = labeled = unlabeled = without_area = managed_on = 0
        for entry in ent_reg.entities.values():
            total += 1
            if entry.labels:
                labeled += 1
            else:
                unlabeled += 1
            if set(entry.labels) & managed:
                managed_on += 1
            for label_id in entry.labels:
                name = names.get(label_id, label_id)
                per_label[name] = per_label.get(name, 0) + 1

            area_id = entry.area_id
            if area_id is None and entry.device_id:
                device = dev_reg.async_get(entry.device_id)
                area_id = device.area_id if device else None
            if not area_id:
                without_area += 1

        coverage = round(labeled / total * 100, 1) if total else 0.0
        self.stats = {
            "entities_total": total,
            "entities_labeled": labeled,
            "entities_unlabeled": unlabeled,
            "entities_without_area": without_area,
            "managed_labels": len(managed),
            "managed_labeled_entities": managed_on,
            "coverage_pct": coverage,
            "by_label": dict(
                sorted(per_label.items(), key=lambda kv: kv[1], reverse=True)
            ),
        }
        self._notify()
        return self.stats

    async def async_execute(self) -> dict:
        """Run labels and/or area assignment according to the selected scope."""
        summary: dict = {
            "scope": self.scope,
            "dry_run": self.dry_run,
            "timestamp": dt_util.utcnow().isoformat(),
        }
        options = self.options_factory()
        options.dry_run = self.dry_run
        if self.scope in (SCOPE_BOTH, SCOPE_LABELS):
            summary["labels"] = (await self.labeler.run(options)).as_dict()
        if self.scope in (SCOPE_BOTH, SCOPE_AREAS):
            summary["areas"] = (
                await self.labeler.assign_areas(
                    dry_run=self.dry_run, exclude=options.exclude
                )
            ).as_dict()
        self.last_run = summary
        self.refresh_stats()
        return summary

    async def async_cleanup(self) -> dict:
        """Remove labels created by this integration."""
        result = (await self.labeler.cleanup(dry_run=self.dry_run)).as_dict()
        self.last_run = {
            "scope": "cleanup",
            "dry_run": self.dry_run,
            "timestamp": dt_util.utcnow().isoformat(),
            "cleanup": result,
        }
        self.refresh_stats()
        return self.last_run

    async def async_remove_all(self) -> dict:
        """Remove every label in Home Assistant (not just managed ones)."""
        result = (
            await self.labeler.remove_all_labels(dry_run=self.dry_run)
        ).as_dict()
        self.last_run = {
            "scope": "remove_all",
            "dry_run": self.dry_run,
            "timestamp": dt_util.utcnow().isoformat(),
            "remove_all": result,
        }
        self.refresh_stats()
        return self.last_run
