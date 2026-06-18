"""Sensors exposing Auto-Organizer run results and registry statistics."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import dt as dt_util

from . import AutoOrganizerConfigEntry
from .coordinator import AutoOrganizerRuntime


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AutoOrganizerConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    runtime = entry.runtime_data
    async_add_entities(
        [
            LastRunSensor(runtime),
            LastRunTimeSensor(runtime),
            StatsSensor(runtime, "entities_labeled", "labeled", "mdi:tag-multiple", "entities"),
            StatsSensor(runtime, "entities_unlabeled", "unlabeled", "mdi:tag-off-outline", "entities"),
            StatsSensor(runtime, "entities_without_area", "without_area", "mdi:map-marker-off", "entities"),
            StatsSensor(runtime, "managed_labels", "managed_labels", "mdi:label-multiple", "labels"),
            StatsSensor(runtime, "coverage_pct", "coverage", "mdi:chart-donut", "%"),
        ]
    )


class _BaseSensor(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, runtime: AutoOrganizerRuntime, key: str, icon: str) -> None:
        self._runtime = runtime
        self._attr_translation_key = key
        self._attr_icon = icon
        self._attr_unique_id = f"{runtime.entry.entry_id}_{key}"
        self._attr_device_info = runtime.device_info

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self.async_on_remove(self._runtime.add_listener(self.async_write_ha_state))


def _affected(last: dict) -> int:
    total = 0
    if "labels" in last:
        total += int(last["labels"].get("updated", 0))
    if "areas" in last:
        total += int(last["areas"].get("assigned", 0))
    if "cleanup" in last:
        total += int(last["cleanup"].get("updated", 0))
    return total


class LastRunSensor(_BaseSensor):
    """Number of entities changed by the last run; details in attributes."""

    _attr_native_unit_of_measurement = "entities"

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "last_run", "mdi:history")

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
        attrs: dict[str, Any] = {
            k: v for k, v in last.items() if k not in ("labels", "areas", "cleanup")
        }
        for section in ("labels", "areas", "cleanup"):
            if section in last:
                attrs[section] = {
                    k: v for k, v in last[section].items() if k != "changes"
                }
        return attrs


class LastRunTimeSensor(_BaseSensor):
    """Timestamp of the last run."""

    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "last_run_time", "mdi:clock-outline")

    @property
    def native_value(self) -> datetime | None:
        last = self._runtime.last_run
        if not last or "timestamp" not in last:
            return None
        return dt_util.parse_datetime(last["timestamp"])


class StatsSensor(_BaseSensor):
    """A single registry statistic from the coordinator."""

    def __init__(
        self,
        runtime: AutoOrganizerRuntime,
        stat_key: str,
        translation_key: str,
        icon: str,
        unit: str,
    ) -> None:
        super().__init__(runtime, translation_key, icon)
        self._stat_key = stat_key
        self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self) -> float | int | None:
        return self._runtime.stats.get(self._stat_key)
