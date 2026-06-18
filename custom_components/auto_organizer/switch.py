"""Switch entity to toggle dry-run mode for the control buttons."""

from __future__ import annotations

from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from . import AutoOrganizerConfigEntry
from .coordinator import AutoOrganizerRuntime


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AutoOrganizerConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([DryRunSwitch(entry.runtime_data)])


class DryRunSwitch(SwitchEntity, RestoreEntity):
    """When on, the Run/Cleanup buttons only preview (write nothing)."""

    _attr_has_entity_name = True
    _attr_translation_key = "dry_run"
    _attr_icon = "mdi:test-tube"

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        self._runtime = runtime
        self._attr_unique_id = f"{runtime.entry.entry_id}_dry_run"
        self._attr_device_info = runtime.device_info

    @property
    def is_on(self) -> bool:
        return self._runtime.dry_run

    async def async_turn_on(self, **kwargs: Any) -> None:
        self._runtime.dry_run = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs: Any) -> None:
        self._runtime.dry_run = False
        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        last = await self.async_get_last_state()
        if last is not None:
            self._runtime.dry_run = last.state == "on"
