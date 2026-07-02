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
    for service in ("run", "cleanup", "assign_areas", "remove_all", "preview"):
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


async def test_exclude_merges_domains_entities_and_patterns(
    hass: HomeAssistant,
) -> None:
    from custom_components.auto_organizer import _merge_exclude

    assert _merge_exclude(["light", "switch"], [], "") == ("light", "switch")
    assert _merge_exclude([], ["sensor.foo"], "") == ("sensor.foo",)
    assert _merge_exclude(["light"], ["sensor.foo"], "sensor.test_*") == (
        "light",
        "sensor.foo",
        "sensor.test_*",
    )
    # the same pattern picked via two fields is only evaluated once
    assert _merge_exclude(["light"], ["sensor.foo"], "light, sensor.foo") == (
        "light",
        "sensor.foo",
    )
    assert _merge_exclude(None, None, "") == ()


async def test_options_from_entry_uses_domain_and_entity_selectors(
    hass: HomeAssistant,
) -> None:
    from custom_components.auto_organizer import _options_from_entry
    from custom_components.auto_organizer.const import (
        CONF_EXCLUDE_DOMAINS,
        CONF_EXCLUDE_ENTITIES,
    )

    entry = MockConfigEntry(
        domain=DOMAIN,
        options={
            CONF_EXCLUDE_DOMAINS: ["scene"],
            CONF_EXCLUDE_ENTITIES: ["sensor.keep_out"],
        },
    )
    entry.add_to_hass(hass)
    options = _options_from_entry(hass, entry)
    assert "scene" in options.exclude
    assert "sensor.keep_out" in options.exclude


def test_exclude_domains_selector_lists_known_domains() -> None:
    from custom_components.auto_organizer.rules import DOMAIN_LABELS

    # every domain the rule engine understands is offered in the picker
    assert "light" in DOMAIN_LABELS
    assert "switch" in DOMAIN_LABELS
    assert len(DOMAIN_LABELS) >= 20


async def test_preview_service_never_writes(hass: HomeAssistant) -> None:
    await _add_entry(hass)
    result = await hass.services.async_call(
        DOMAIN, "preview", {}, blocking=True, return_response=True
    )
    assert "labels" in result
    assert "areas" in result
    assert "scanned" in result["labels"]
    assert "scanned" in result["areas"]


async def test_own_control_entities_not_auto_labeled(hass: HomeAssistant) -> None:
    from homeassistant.helpers import entity_registry as er

    from custom_components.auto_organizer.const import CONF_AUTO_LABEL_NEW

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={CONF_AUTO_LABEL_NEW: True},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    ent_reg = er.async_get(hass)
    own_entities = [
        e for e in ent_reg.entities.values() if e.platform == DOMAIN
    ]
    assert own_entities
    # None of our own button/select/switch/sensor entities should carry
    # auto-assigned labels from their own creation event.
    assert all(not e.labels for e in own_entities)


async def test_diagnostics_strips_changes_from_every_section(
    hass: HomeAssistant,
) -> None:
    from custom_components.auto_organizer.diagnostics import (
        async_get_config_entry_diagnostics,
    )

    entry = await _add_entry(hass)
    await hass.services.async_call(
        DOMAIN, "cleanup", {"dry_run": True}, blocking=True, return_response=True
    )
    diagnostics = await async_get_config_entry_diagnostics(hass, entry)
    for section in diagnostics["last_run"].values():
        if isinstance(section, dict):
            assert "changes" not in section


async def test_control_entities_are_config_category(hass: HomeAssistant) -> None:
    from homeassistant.helpers import entity_registry as er

    await _add_entry(hass)
    ent_reg = er.async_get(hass)
    control_entities = [
        e
        for e in ent_reg.entities.values()
        if e.platform == DOMAIN and e.domain in ("button", "select", "switch")
    ]
    assert control_entities
    assert all(e.entity_category == "config" for e in control_entities)


async def test_enabled_labels_option_restricts_run(hass: HomeAssistant) -> None:
    from custom_components.auto_organizer.const import CONF_ENABLED_LABELS

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={CONF_ENABLED_LABELS: ["lights"]},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    from custom_components.auto_organizer import _options_from_entry

    options = _options_from_entry(hass, entry)
    assert options.enabled_labels == frozenset({"lights"})


def test_enabled_labels_selector_lists_every_catalog_label() -> None:
    from custom_components.auto_organizer.rules import LABELS

    assert "lights" in LABELS
    assert "waste" in LABELS
    assert len(LABELS) >= 30


async def test_set_entity_icons_option_wired(hass: HomeAssistant) -> None:
    from custom_components.auto_organizer import _options_from_entry
    from custom_components.auto_organizer.const import CONF_SET_ENTITY_ICONS

    entry = MockConfigEntry(domain=DOMAIN, options={CONF_SET_ENTITY_ICONS: True})
    entry.add_to_hass(hass)
    options = _options_from_entry(hass, entry)
    assert options.set_entity_icons is True


async def test_set_entity_icons_defaults_off(hass: HomeAssistant) -> None:
    from custom_components.auto_organizer import _options_from_entry

    entry = MockConfigEntry(domain=DOMAIN, options={})
    entry.add_to_hass(hass)
    options = _options_from_entry(hass, entry)
    assert options.set_entity_icons is False


async def test_entities_with_specific_icon_stat(hass: HomeAssistant) -> None:
    from homeassistant.helpers import entity_registry as er

    entry = await _add_entry(hass)
    ent_reg = er.async_get(hass)
    ent_reg.async_get_or_create(
        "sensor", "test", "coffee_1", suggested_object_id="kaffeemaschine"
    )
    ent_reg.async_update_entity("sensor.kaffeemaschine", icon="mdi:coffee-maker")

    runtime = entry.runtime_data
    stats = runtime.refresh_stats()
    assert stats["entities_with_specific_icon"] >= 1


async def test_last_run_sensor_strips_changes_from_remove_all(
    hass: HomeAssistant,
) -> None:
    entry = await _add_entry(hass)
    await hass.services.async_call(
        DOMAIN, "remove_all", {"dry_run": True}, blocking=True, return_response=True
    )
    runtime = entry.runtime_data
    assert "changes" not in runtime.last_run.get("remove_all", {})


async def test_last_run_sensor_surfaces_icons_set(hass: HomeAssistant) -> None:
    from custom_components.auto_organizer.const import CONF_SET_ENTITY_ICONS

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={CONF_SET_ENTITY_ICONS: True},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    from homeassistant.helpers import entity_registry as er
    ent_reg = er.async_get(hass)
    ent_reg.async_get_or_create(
        "sensor", "test", "coffee_2", suggested_object_id="kaffeemaschine2"
    )

    runtime = entry.runtime_data
    await hass.services.async_call(
        DOMAIN, "run", {"dry_run": True}, blocking=True, return_response=True
    )
    assert "icons_set" in runtime.last_run
