"""Integration tests: setup, services and the control entities."""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.auto_organizer.const import DOMAIN


async def _add_entry(hass: HomeAssistant) -> MockConfigEntry:
    entry = MockConfigEntry(domain=DOMAIN, title="Entity Auto-Organizer", options={})
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    return entry


async def test_setup_registers_services(hass: HomeAssistant) -> None:
    await _add_entry(hass)
    for service in ("run", "cleanup", "assign_areas", "remove_all"):
        assert hass.services.has_service(DOMAIN, service)


async def test_control_entities_created(hass: HomeAssistant) -> None:
    await _add_entry(hass)
    states = hass.states.async_entity_ids()
    # buttons + select + switch + sensors -> several entities created
    ours = [e for e in states if "auto_organizer" in e or "auto-organizer" in e]
    assert any(e.startswith("button.") for e in ours)
    assert any(e.startswith("select.") for e in ours)
    assert any(e.startswith("switch.") for e in ours)
    assert any(e.startswith("sensor.") for e in ours)


async def test_run_service_executes(hass: HomeAssistant) -> None:
    await _add_entry(hass)
    result = await hass.services.async_call(
        DOMAIN, "run", {"dry_run": True}, blocking=True, return_response=True
    )
    assert "scanned" in result


async def test_unload(hass: HomeAssistant) -> None:
    entry = await _add_entry(hass)
    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
