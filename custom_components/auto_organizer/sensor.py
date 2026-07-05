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

from collections.abc import Callable

from . import AutoOrganizerConfigEntry
from .const import CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
from .coordinator import AutoOrganizerRuntime
from .organizer import OrganizerOptions
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
            StatsSensor(
                runtime, "entities_with_area", "with_area", "mdi:map-marker-radius", "entities"
            ),
            StatsSensor(
                runtime, "custom_rule_matches", "custom_rule_matches",
                "mdi:filter-cog", "entities",
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
            OptionSensor(
                runtime, "language", "language", "mdi:translate", lambda o: o.language
            ),
            OptionSensor(
                runtime, "max_labels", "max_labels", "mdi:tag-multiple",
                lambda o: o.max_labels, unit="labels",
            ),
            OptionSensor(
                runtime, "scan_interval", "scan_interval", "mdi:timer-cog-outline",
                lambda o: entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
                unit="min",
            ),
            OptionSensor(
                runtime, "exclude_count", "exclude_count", "mdi:filter-remove-outline",
                lambda o: len(o.exclude), unit="patterns",
            ),
            OptionSensor(
                runtime, "custom_rules_count", "custom_rules_count",
                "mdi:script-text-outline",
                lambda o: len(o.custom_rules), unit="rules",
            ),
            ErrorCountSensor(runtime),
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
        sections = ("labels", "areas", "cleanup", "remove_all")
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
        # Surface icons_set at the top level too — it's otherwise buried
        # inside attrs["labels"], easy to miss when just glancing at state.
        icons_set = last.get("labels", {}).get("icons_set")
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


class OptionSensor(_BaseSensor):
    """Read-only reflection of one currently effective config-entry option.

    Lets you see at a glance what's configured (language, limits, exclude
    patterns, ...) without opening the options flow — resolved values like
    `language: auto` -> `de` are shown as HA actually applies them.
    """

    def __init__(
        self,
        runtime: AutoOrganizerRuntime,
        key: str,
        translation_key: str,
        icon: str,
        getter: Callable[[OrganizerOptions], Any],
        unit: str | None = None,
    ) -> None:
        super().__init__(runtime, translation_key, icon)
        self._getter = getter
        if unit:
            self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self) -> Any:
        return self._getter(self._runtime.options_factory())


class ErrorCountSensor(_BaseSensor):
    """Number of run/service failures since the last restart."""

    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _attr_native_unit_of_measurement = "errors"

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "error_count", "mdi:alert-circle-outline")

    @property
    def native_value(self) -> int:
        return self._runtime.error_count


class LastErrorSensor(_BaseSensor):
    """Message of the most recent run/service failure, if any."""

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "last_error", "mdi:alert-octagon-outline")

    @property
    def native_value(self) -> str | None:
        if not self._runtime.last_error:
            return None
        # Entity states are capped at 255 chars; the full text is still
        # available in the timestamp-paired attribute for diagnostics.
        return self._runtime.last_error[:255]

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        if not self._runtime.last_error:
            return None
        return {
            "message": self._runtime.last_error,
            "timestamp": self._runtime.last_error_time,
        }
