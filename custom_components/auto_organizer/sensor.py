"""Sensor exposing the result of the last Auto-Organizer run."""

from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AutoOrganizerConfigEntry
from .coordinator import AutoOrganizerRuntime


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AutoOrganizerConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([LastRunSensor(entry.runtime_data)])


def _affected(last: dict) -> int:
    """Total number of entities changed in the last run."""
    total = 0
    if "labels" in last:
        total += int(last["labels"].get("updated", 0))
    if "areas" in last:
        total += int(last["areas"].get("assigned", 0))
    if "cleanup" in last:
        total += int(last["cleanup"].get("updated", 0))
    return total


class LastRunSensor(SensorEntity):
    """Number of entities changed by the last run; details in attributes."""

    _attr_has_entity_name = True
    _attr_translation_key = "last_run"
    _attr_icon = "mdi:history"
    _attr_native_unit_of_measurement = "entities"

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        self._runtime = runtime
        self._attr_unique_id = f"{runtime.entry.entry_id}_last_run"
        self._attr_device_info = runtime.device_info

    @property
    def native_value(self) -> int | None:
        if not self._runtime.last_run:
            return None
        return _affected(self._runtime.last_run)

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        last = self._runtime.last_run
        if not last:
            return None
        # Strip the (potentially huge) per-entity change lists; keep counts.
        attrs: dict[str, Any] = {
            k: v for k, v in last.items() if k not in ("labels", "areas", "cleanup")
        }
        for section in ("labels", "areas", "cleanup"):
            if section in last:
                attrs[section] = {
                    k: v for k, v in last[section].items() if k != "changes"
                }
        return attrs

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self.async_on_remove(self._runtime.add_listener(self.async_write_ha_state))
