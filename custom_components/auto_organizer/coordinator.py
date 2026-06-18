"""Shared runtime state for the Auto-Organizer control entities."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.util import dt as dt_util

from .const import DOMAIN, NAME, SCOPE_AREAS, SCOPE_BOTH, SCOPE_LABELS
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

    async def async_execute(self) -> dict:
        """Run labels and/or area assignment according to the selected scope."""
        summary: dict = {
            "scope": self.scope,
            "dry_run": self.dry_run,
            "timestamp": dt_util.utcnow().isoformat(),
        }
        if self.scope in (SCOPE_BOTH, SCOPE_LABELS):
            options = self.options_factory()
            options.dry_run = self.dry_run
            summary["labels"] = (await self.labeler.run(options)).as_dict()
        if self.scope in (SCOPE_BOTH, SCOPE_AREAS):
            summary["areas"] = (
                await self.labeler.assign_areas(dry_run=self.dry_run)
            ).as_dict()
        self.last_run = summary
        self._notify()
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
        self._notify()
        return self.last_run
