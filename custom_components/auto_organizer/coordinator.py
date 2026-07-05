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

from .const import (
    DOMAIN,
    MANAGED_MARKER,
    NAME,
    SCOPE_ALL,
    SCOPE_AREAS,
    SCOPE_BOTH,
    SCOPE_ICONS,
    SCOPE_LABELS,
)
from .organizer import Organizer, OrganizerOptions
from .rules import SPECIFIC_ICONS, _normalize


@dataclass
class AutoOrganizerRuntime:
    """Holds the organizer plus the state driven by the control entities."""

    hass: HomeAssistant
    entry: ConfigEntry
    organizer: Organizer
    options_factory: Callable[[], OrganizerOptions]
    scope: str = SCOPE_BOTH
    dry_run: bool = False
    last_run: dict | None = None
    stats: dict = field(default_factory=dict)
    # Rolling history (newest first, capped at 10) of the entities most
    # recently touched by each change type, across all runs/services —
    # unlike `last_run`, this survives being overwritten by the next run.
    last_labeled: list[dict] = field(default_factory=list)
    last_grouped: list[dict] = field(default_factory=list)
    last_iconed: list[dict] = field(default_factory=list)
    # Errors raised by a run/service call since the last restart — never
    # cleared automatically, only ever appended to.
    error_count: int = 0
    last_error: str | None = None
    last_error_time: str | None = None
    _listeners: list[Callable[[], None]] = field(default_factory=list)

    HISTORY_LIMIT = 10

    @callback
    def record_history(
        self, target: list[dict], changes: list[dict], timestamp: str
    ) -> None:
        """Merge freshly changed entities into a rolling history list.

        Re-touched entities move back to the front instead of duplicating.
        Mutates ``target`` in place so callers can keep holding their
        reference to ``self.last_labeled`` etc.
        """
        if not changes:
            return
        fresh = {c["entity_id"] for c in changes}
        kept = [c for c in target if c["entity_id"] not in fresh]
        merged = [{**c, "timestamp": timestamp} for c in changes] + kept
        target[:] = merged[: self.HISTORY_LIMIT]

    @callback
    def record_error(self, message: str) -> None:
        """Track a run/service failure for the diagnostic sensors."""
        self.error_count += 1
        self.last_error = message
        self.last_error_time = dt_util.utcnow().isoformat()
        self._notify()

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
        known_icons = set(SPECIFIC_ICONS.values())
        custom_rules = self.options_factory().custom_rules

        total = labeled = unlabeled = without_area = managed_on = with_icon = 0
        custom_rule_matches = 0
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
            # entry.icon could be user-picked or set by a previous run — we
            # can't tell those apart, so this counts "has one of our known
            # specific icons", not strictly "we set this".
            if entry.icon and entry.icon in known_icons:
                with_icon += 1

            area_id = entry.area_id
            if area_id is None and entry.device_id:
                device = dev_reg.async_get(entry.device_id)
                area_id = device.area_id if device else None
            if not area_id:
                without_area += 1

            if custom_rules:
                ename = entry.name or entry.original_name
                haystack = _normalize(f"{entry.entity_id} {ename or ''}")
                if any(needle in haystack for needle in custom_rules):
                    custom_rule_matches += 1

        coverage = round(labeled / total * 100, 1) if total else 0.0
        self.stats = {
            "entities_total": total,
            "entities_labeled": labeled,
            "entities_unlabeled": unlabeled,
            "entities_without_area": without_area,
            "entities_with_area": total - without_area,
            "managed_labels": len(managed),
            "managed_labeled_entities": managed_on,
            "entities_with_specific_icon": with_icon,
            "custom_rule_matches": custom_rule_matches,
            "coverage_pct": coverage,
            "by_label": dict(
                sorted(per_label.items(), key=lambda kv: kv[1], reverse=True)
            ),
        }
        self._notify()
        return self.stats

    async def async_execute(self) -> dict:
        """Run labels and/or area assignment according to the selected scope."""
        try:
            summary: dict = {
                "scope": self.scope,
                "dry_run": self.dry_run,
                "timestamp": dt_util.utcnow().isoformat(),
            }
            options = self.options_factory()
            options.dry_run = self.dry_run
            if self.scope in (SCOPE_ALL, SCOPE_BOTH, SCOPE_LABELS):
                labels_result = await self.organizer.run(options)
                summary["labels"] = labels_result.as_dict()
                if not self.dry_run:
                    self.record_history(
                        self.last_labeled, labels_result.changes, summary["timestamp"]
                    )
                    self.record_history(
                        self.last_iconed,
                        labels_result.icon_changes,
                        summary["timestamp"],
                    )
            if self.scope in (SCOPE_ALL, SCOPE_BOTH, SCOPE_AREAS):
                areas_result = await self.organizer.assign_areas(
                    dry_run=self.dry_run, exclude=options.exclude
                )
                summary["areas"] = areas_result.as_dict()
                if not self.dry_run:
                    self.record_history(
                        self.last_grouped, areas_result.changes, summary["timestamp"]
                    )
            if self.scope in (SCOPE_ALL, SCOPE_ICONS):
                icons_result = await self.organizer.assign_icons(
                    options, dry_run=self.dry_run
                )
                summary["icons"] = icons_result.as_dict()
                if not self.dry_run:
                    self.record_history(
                        self.last_iconed, icons_result.changes, summary["timestamp"]
                    )
            self.last_run = summary
            self.refresh_stats()
            return summary
        except Exception as err:
            self.record_error(str(err))
            raise

    async def async_cleanup(self) -> dict:
        """Remove labels created by this integration."""
        try:
            result = (await self.organizer.cleanup(dry_run=self.dry_run)).as_dict()
            self.last_run = {
                "scope": "cleanup",
                "dry_run": self.dry_run,
                "timestamp": dt_util.utcnow().isoformat(),
                "cleanup": result,
            }
            self.refresh_stats()
            return self.last_run
        except Exception as err:
            self.record_error(str(err))
            raise

    async def async_remove_all(self) -> dict:
        """Remove every label in Home Assistant (not just managed ones)."""
        try:
            result = (
                await self.organizer.remove_all_labels(dry_run=self.dry_run)
            ).as_dict()
            self.last_run = {
                "scope": "remove_all",
                "dry_run": self.dry_run,
                "timestamp": dt_util.utcnow().isoformat(),
                "remove_all": result,
            }
            self.refresh_stats()
            return self.last_run
        except Exception as err:
            self.record_error(str(err))
            raise
