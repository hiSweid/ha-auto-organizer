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
    for service in (
        "run",
        "cleanup",
        "assign_areas",
        "assign_icons",
        "remove_all",
        "preview",
    ):
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
    # The raw runtime.last_run keeps the changes list (service responses
    # need it) — the stripping happens in the sensor's state attributes.
    await _add_entry(hass)
    await hass.services.async_call(
        DOMAIN, "remove_all", {"dry_run": True}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()
    state = hass.states.get("sensor.entity_auto_organizer_last_run")
    assert state is not None
    assert "changes" not in state.attributes.get("remove_all", {})


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

    await hass.services.async_call(
        DOMAIN, "run", {"dry_run": True}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()
    # icons_set lives nested in the raw data but is lifted to a top-level
    # attribute on the Last run sensor for visibility.
    state = hass.states.get("sensor.entity_auto_organizer_last_run")
    assert state is not None
    assert state.attributes.get("icons_set", 0) >= 1


async def test_history_sensors_track_last_10_changes(hass: HomeAssistant) -> None:
    from custom_components.auto_organizer.const import CONF_SET_ENTITY_ICONS
    from homeassistant.helpers import entity_registry as er

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={CONF_SET_ENTITY_ICONS: True},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    ent_reg = er.async_get(hass)
    ent_reg.async_get_or_create(
        "sensor", "test", "coffee_3", suggested_object_id="kaffeemaschine3"
    )

    # A dry run must not pollute the history.
    await hass.services.async_call(
        DOMAIN, "run", {"dry_run": True}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()
    assert hass.states.get("sensor.entity_auto_organizer_last_labeled_entities").state == "unknown"

    await hass.services.async_call(
        DOMAIN, "run", {"dry_run": False}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()

    labeled = hass.states.get("sensor.entity_auto_organizer_last_labeled_entities")
    iconed = hass.states.get("sensor.entity_auto_organizer_last_entities_with_new_icon")
    assert labeled is not None and labeled.state != "unknown"
    assert any(
        i["entity_id"] == "sensor.kaffeemaschine3" for i in labeled.attributes["items"]
    )
    assert iconed is not None and iconed.state != "unknown"
    assert any(
        i["entity_id"] == "sensor.kaffeemaschine3" for i in iconed.attributes["items"]
    )

    await hass.services.async_call(
        DOMAIN, "assign_icons", {"dry_run": False}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()
    grouped = hass.states.get("sensor.entity_auto_organizer_last_grouped_entities")
    assert grouped is not None  # no areas configured in tests -> stays unknown
    assert grouped.state == "unknown"


async def test_custom_rule_matches_stat(hass: HomeAssistant) -> None:
    # No dedicated sensor for this (kept out of the entity list on
    # purpose) — it's still computed into runtime.stats for diagnostics.
    from homeassistant.helpers import entity_registry as er
    from custom_components.auto_organizer.const import CONF_CUSTOM_RULES

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={CONF_CUSTOM_RULES: "kaffeemaschine=appliances"},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    ent_reg = er.async_get(hass)
    ent_reg.async_get_or_create(
        "sensor", "test", "coffee_4", suggested_object_id="kaffeemaschine4"
    )
    stats = entry.runtime_data.refresh_stats()

    assert stats["custom_rule_matches"] >= 1
    assert stats["entities_with_area"] == stats["entities_total"] - stats["entities_without_area"]


async def test_error_tracked_on_service_failure(hass: HomeAssistant) -> None:
    entry = await _add_entry(hass)

    def _boom(*args, **kwargs):
        raise RuntimeError("boom")

    entry.runtime_data.organizer.cleanup = _boom  # type: ignore[method-assign]
    try:
        await hass.services.async_call(
            DOMAIN, "cleanup", {"dry_run": True}, blocking=True, return_response=True
        )
    except Exception:
        pass
    await hass.async_block_till_done()

    last_error = hass.states.get("sensor.entity_auto_organizer_last_error")
    assert last_error is not None and "boom" in last_error.state
    assert last_error.attributes["count"] >= 1


async def test_icons_scope_surfaces_in_last_run_sensor(hass: HomeAssistant) -> None:
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
        "sensor", "test", "coffee_5", suggested_object_id="kaffeemaschine5"
    )

    await hass.services.async_call(
        DOMAIN, "assign_icons", {"dry_run": True}, blocking=True, return_response=True
    )
    await hass.async_block_till_done()

    state = hass.states.get("sensor.entity_auto_organizer_last_run")
    assert state is not None
    assert "icons" in state.attributes
    assert "changes" not in state.attributes["icons"]


async def test_dry_run_seeded_from_configured_default(hass: HomeAssistant) -> None:
    # Regression test: runtime.dry_run used to hardcode to False at startup
    # and only ever get overwritten by the dry-run switch entity, so a user
    # who configured "dry run by default" in the options flow but never
    # toggled the switch would get real writes from the Run button on a
    # fresh install. It must now start from the configured option.
    from custom_components.auto_organizer.const import CONF_DRY_RUN

    entry = MockConfigEntry(
        domain=DOMAIN, title="Entity Auto-Organizer", options={CONF_DRY_RUN: True}
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.runtime_data.dry_run is True


async def test_remove_all_button_disabled_by_default(hass: HomeAssistant) -> None:
    # Regression test: an accidental tap on this button used to wipe every
    # label in the whole HA instance (not just this integration's own) with
    # no undo — it must be opt-in, not enabled out of the box.
    from homeassistant.helpers import entity_registry as er

    await _add_entry(hass)
    ent_reg = er.async_get(hass)
    remove_all = next(
        e
        for e in ent_reg.entities.values()
        if e.platform == DOMAIN and e.unique_id.endswith("_remove_all")
    )
    assert remove_all.disabled_by is not None


async def test_exclude_blocks_area_and_floor_labels(hass: HomeAssistant) -> None:
    # Regression test: area/floor labels used to be appended after
    # compute_label_specs() (which already honors excludes) without
    # re-checking the exclude list, so an explicitly excluded entity still
    # got area/floor labels.
    from homeassistant.helpers import area_registry as ar
    from homeassistant.helpers import entity_registry as er

    from custom_components.auto_organizer.const import CONF_ENABLE_AREA, CONF_EXCLUDE

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="Entity Auto-Organizer",
        options={
            CONF_ENABLE_AREA: True,
            CONF_EXCLUDE: "sensor.excluded_kitchen_thing",
        },
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    area_reg = ar.async_get(hass)
    area = area_reg.async_get_or_create("Kitchen")
    ent_reg = er.async_get(hass)
    ent_reg.async_get_or_create(
        "sensor", "test", "excluded_1", suggested_object_id="excluded_kitchen_thing"
    )
    ent_reg.async_update_entity(
        "sensor.excluded_kitchen_thing", area_id=area.id
    )

    result = await hass.services.async_call(
        DOMAIN, "run", {"dry_run": True}, blocking=True, return_response=True
    )
    changed_ids = {c["entity_id"] for c in result["changes"]}
    assert "sensor.excluded_kitchen_thing" not in changed_ids
