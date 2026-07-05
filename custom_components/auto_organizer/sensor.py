"""Sensors exposing Auto-Organizer run results and registry statistics."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.util import dt as dt_util

from . import AutoOrganizerConfigEntry
from .coordinator import AutoOrganizerRuntime
from .rules import affected_count


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
            StatsSensor(
                runtime, "entities_with_specific_icon", "with_icon", "mdi:palette", "entities"
            ),
            StatsSensor(
                runtime, "coverage_pct", "coverage", "mdi:chart-donut", "%",
                attrs_key="by_label",
            ),
            LastChangedSensor(
                runtime, "last_labeled", "last_labeled", "mdi:tag-check"
            ),
            LastChangedSensor(
                runtime, "last_grouped", "last_grouped", "mdi:home-group"
            ),
            LastChangedSensor(
                runtime, "last_iconed", "last_iconed", "mdi:palette-outline"
            ),
            LastErrorSensor(runtime),
        ]
    )


class _BaseSensor(SensorEntity):
    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, runtime: AutoOrganizerRuntime, key: str, icon: str) -> None:
        self._runtime = runtime
        self._attr_translation_key = key
        self._attr_icon = icon
        self._attr_unique_id = f"{runtime.entry.entry_id}_{key}"
        self._attr_device_info = runtime.device_info

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self.async_on_remove(self._runtime.add_listener(self.async_write_ha_state))


class LastRunSensor(_BaseSensor):
    """Number of entities changed by the last run; details in attributes."""

    _attr_native_unit_of_measurement = "entities"
    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "last_run", "mdi:history")

    @property
    def native_value(self) -> int | None:
        if not self._runtime.last_run:
            return None
        return affected_count(self._runtime.last_run)

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        last = self._runtime.last_run
        if not last:
            return None
        sections = ("labels", "areas", "icons", "cleanup", "remove_all")
        attrs: dict[str, Any] = {
            k: v for k, v in last.items() if k not in sections
        }
        for section in sections:
            if section in last:
                attrs[section] = {
                    k: v
                    for k, v in last[section].items()
                    if k not in ("changes", "icon_changes")
                }
        # Surface icons_set at the top level too — it's otherwise buried in
        # a section, easy to miss when just glancing at state. Icons can be
        # set either as a side effect of a labels run or by a dedicated
        # icons-scope run, so add both up.
        icons_set = last.get("labels", {}).get("icons_set", 0) + last.get(
            "icons", {}
        ).get("icons_set", 0)
        if icons_set:
            attrs["icons_set"] = icons_set
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


class LastChangedSensor(_BaseSensor, RestoreEntity):
    """Rolling history (up to 10) of the entities most recently touched by
    one change type — labeled, grouped into an area, or given an icon.

    Unlike :class:`LastRunSensor`, this accumulates across runs/services
    instead of being replaced by the next run, and survives HA restarts via
    :class:`RestoreEntity`.
    """

    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(
        self, runtime: AutoOrganizerRuntime, runtime_attr: str, key: str, icon: str
    ) -> None:
        super().__init__(runtime, key, icon)
        self._runtime_attr = runtime_attr

    @property
    def _items(self) -> list[dict]:
        return getattr(self._runtime, self._runtime_attr)

    @property
    def native_value(self) -> datetime | None:
        items = self._items
        if not items:
            return None
        return dt_util.parse_datetime(items[0]["timestamp"])

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        items = self._items
        return {"count": len(items), "items": items} if items else None

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        if self._items:
            return  # already populated by a run/service this session
        last = await self.async_get_last_state()
        if last and last.attributes.get("items"):
            setattr(
                self._runtime, self._runtime_attr, list(last.attributes["items"])
            )


class StatsSensor(_BaseSensor):
    """A single registry statistic from the coordinator."""

    _attr_state_class = SensorStateClass.MEASUREMENT

    def __init__(
        self,
        runtime: AutoOrganizerRuntime,
        stat_key: str,
        translation_key: str,
        icon: str,
        unit: str,
        attrs_key: str | None = None,
    ) -> None:
        super().__init__(runtime, translation_key, icon)
        self._stat_key = stat_key
        self._attrs_key = attrs_key
        self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self) -> float | int | None:
        return self._runtime.stats.get(self._stat_key)

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        if not self._attrs_key:
            return None
        value = self._runtime.stats.get(self._attrs_key)
        return {self._attrs_key: value} if value else None


class LastErrorSensor(_BaseSensor):
    """Message of the most recent run/service failure, if any.

    Combines what used to be two sensors (count + message) into one to
    avoid cluttering the entity list — the count is still available as an
    attribute for automations/dashboards that want to alert on it.
    """

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "last_error", "mdi:alert-octagon-outline")

    @property
    def native_value(self) -> str | None:
        if not self._runtime.last_error:
            return None
        # Entity states are capped at 255 chars; the full text is still
        # available in the "message" attribute.
        return self._runtime.last_error[:255]

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        if not self._runtime.last_error:
            return None
        return {
            "message": self._runtime.last_error,
            "timestamp": self._runtime.last_error_time,
            "count": self._runtime.error_count,
        }
