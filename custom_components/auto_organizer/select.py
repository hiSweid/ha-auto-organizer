"""Select entity to choose the run scope (labels / areas / both)."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from . import AutoOrganizerConfigEntry
from .const import SCOPES
from .coordinator import AutoOrganizerRuntime


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AutoOrganizerConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([ScopeSelect(entry.runtime_data)])


class ScopeSelect(SelectEntity, RestoreEntity):
    """Chooses what the Run button processes."""

    _attr_has_entity_name = True
    _attr_translation_key = "scope"
    _attr_options = SCOPES
    _attr_icon = "mdi:format-list-checks"
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        self._runtime = runtime
        self._attr_unique_id = f"{runtime.entry.entry_id}_scope"
        self._attr_device_info = runtime.device_info

    @property
    def current_option(self) -> str:
        return self._runtime.scope

    async def async_select_option(self, option: str) -> None:
        self._runtime.scope = option
        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        last = await self.async_get_last_state()
        if last and last.state in SCOPES:
            self._runtime.scope = last.state
