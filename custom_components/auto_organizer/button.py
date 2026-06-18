"""Button entities to trigger Auto-Organizer runs."""

from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import AutoOrganizerConfigEntry
from .coordinator import AutoOrganizerRuntime


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AutoOrganizerConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    runtime = entry.runtime_data
    async_add_entities(
        [RunButton(runtime), CleanupButton(runtime), RemoveAllButton(runtime)]
    )


class _BaseButton(ButtonEntity):
    _attr_has_entity_name = True

    def __init__(self, runtime: AutoOrganizerRuntime, key: str, icon: str) -> None:
        self._runtime = runtime
        self._attr_translation_key = key
        self._attr_icon = icon
        self._attr_unique_id = f"{runtime.entry.entry_id}_{key}"
        self._attr_device_info = runtime.device_info


class RunButton(_BaseButton):
    """Run labels and/or area assignment per the selected scope."""

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "run", "mdi:play-circle")

    async def async_press(self) -> None:
        await self._runtime.async_execute()


class CleanupButton(_BaseButton):
    """Remove all labels created by this integration."""

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "cleanup", "mdi:broom")

    async def async_press(self) -> None:
        await self._runtime.async_cleanup()


class RemoveAllButton(_BaseButton):
    """Remove EVERY label in Home Assistant (not just managed ones)."""

    def __init__(self, runtime: AutoOrganizerRuntime) -> None:
        super().__init__(runtime, "remove_all", "mdi:label-off")

    async def async_press(self) -> None:
        await self._runtime.async_remove_all()
