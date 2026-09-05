"""Unit tests for the pure rule engine (no Home Assistant required)."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

# Make the integration importable as a bare module without installing HA.
COMPONENT = Path(__file__).resolve().parents[1] / "custom_components" / "auto_organizer"
sys.path.insert(0, str(COMPONENT))

import rules  # noqa: E402
from rules import (  # noqa: E402
    OrganizerOptions,
    affected_count,
    area_floor_specs,
    compute_label_specs,
    is_excluded,
    label_differs,
    invalid_custom_rule_labels,
    label_spec,
    match_area,
    parse_custom_rules,
)

AREAS = [
    {"area_id": "wohnzimmer", "name": "Wohnzimmer", "aliases": []},
    {"area_id": "kueche", "name": "Küche", "aliases": ["Kitchen"]},
    {"area_id": "bad", "name": "Bad", "aliases": []},
    {"area_id": "schlafzimmer", "name": "Schlafzimmer", "aliases": []},
]


@dataclass
class FakeEntry:
    entity_id: str
    device_class: str | None = None
    original_device_class: str | None = None
    platform: str | None = None
    entity_category: str | None = None


def names(entry, options=None):
    return [s["name"] for s in compute_label_specs(entry, options or OrganizerOptions())]


def test_domain_label_applied():
    assert names(FakeEntry("light.kitchen")) == ["Beleuchtung"]


def test_device_class_label():
    entry = FakeEntry("sensor.outdoor", original_device_class="temperature")
    assert names(entry) == ["Temperatur"]


def test_user_device_class_overrides_original():
    entry = FakeEntry(
        "sensor.x", device_class="humidity", original_device_class="temperature"
    )
    assert "Luftfeuchtigkeit" in names(entry)
    assert "Temperatur" not in names(entry)


def test_keyword_fallback_only_when_no_match():
    # unknown domain, but entity_id mentions battery
    assert names(FakeEntry("foo.bar_battery")) == ["Batterie"]


def test_keyword_can_add_alongside_domain_match():
    # Since v0.10 only a *curated* match gates the keyword pass — a plain
    # domain match is not "more specific" the way a curated integration
    # theme is, so a light in a room whose name mentions "battery" also
    # gets that theme instead of being capped at "Beleuchtung".
    entry = FakeEntry("light.battery_room")
    result = names(entry)
    assert "Beleuchtung" in result
    assert "Batterie" in result


def test_disable_domain():
    opts = OrganizerOptions(enable_domain=False)
    entry = FakeEntry("sensor.x", original_device_class="motion")
    assert names(entry, opts) == ["Bewegung"]


def test_integration_label_opt_in():
    opts = OrganizerOptions(enable_integration=True)
    entry = FakeEntry("light.k", platform="hue")
    assert names(entry, opts) == ["Beleuchtung", "hue"]


def test_prefix_applied():
    opts = OrganizerOptions(label_prefix="auto:")
    assert names(FakeEntry("light.k"), opts) == ["auto:Beleuchtung"]


def test_no_duplicate_label_names():
    # power + voltage both map to "Energie"; ensure dedupe by name
    entry = FakeEntry("sensor.x", original_device_class="power")
    result = names(entry)
    assert len(result) == len(set(result))


def test_diagnostic_entities_get_generic_label():
    # Since v0.10, skip_categories still keeps the domain/keyword engine off
    # a diagnostic/config helper, but no longer leaves it with *no* label at
    # all — that silently dropped ~1000 entities on a real installation out
    # of every label-based filter. It gets a generic marker instead, unless
    # a curated integration already gave it something more specific (see
    # test_curated_applies_even_to_diagnostic).
    entry = FakeEntry("sensor.uptime", entity_category="diagnostic")
    assert names(entry) == ["Diagnose"]


def test_config_entities_get_generic_label():
    entry = FakeEntry("switch.led_config", entity_category="config")
    assert names(entry) == ["Konfiguration"]


def test_categories_labeled_when_skip_disabled():
    opts = OrganizerOptions(skip_categories=False)
    entry = FakeEntry("light.led_config", entity_category="config")
    assert names(entry, opts) == ["Beleuchtung"]


def test_all_labels_have_valid_color_icon_and_names():
    valid_colors = {
        "primary", "accent", "red", "pink", "purple", "deep-purple", "indigo",
        "blue", "light-blue", "cyan", "teal", "green", "light-green", "lime",
        "yellow", "amber", "orange", "deep-orange", "brown", "grey", "blue-grey",
    }
    for key, ld in rules.LABELS.items():
        assert ld["color"] in valid_colors, key
        assert ld["icon"].startswith("mdi:"), key
        for lang in rules.SUPPORTED_LANGUAGES:
            assert ld["names"].get(lang), f"{key} missing {lang}"


def test_every_mapped_key_exists_in_catalog():
    for mapping in (rules.DOMAIN_LABELS, rules.DEVICE_CLASS_LABELS, rules.KEYWORD_LABELS):
        for key in mapping.values():
            assert key in rules.LABELS, key


def test_english_language():
    opts = OrganizerOptions(language="en")
    entry = FakeEntry("sensor.outdoor", original_device_class="temperature")
    assert names(entry, opts) == ["Temperature"]


def test_unsupported_language_falls_back_to_german():
    opts = OrganizerOptions(language="fr")
    assert names(FakeEntry("light.k"), opts) == ["Beleuchtung"]


def test_language_region_code_normalized():
    opts = OrganizerOptions(language="en-US")
    assert names(FakeEntry("light.k"), opts) == ["Lights"]


def test_curated_integration_label():
    entry = FakeEntry("lawn_mower.vorgarten", platform="navimow")
    # curated key comes first, then the domain label (both mower -> deduped)
    assert names(entry) == ["Mähroboter"]


def test_curated_applies_even_to_diagnostic():
    entry = FakeEntry(
        "sensor.pve_cpu", platform="proxmoxve", entity_category="diagnostic"
    )
    # diagnostic => domain label skipped, but curated theme still applied
    assert names(entry) == ["Netzwerk & Server"]


def test_curated_can_be_disabled():
    opts = OrganizerOptions(enable_curated=False)
    # plain sensor with no device_class -> no label once "Sensoren" is gone
    entry = FakeEntry("sensor.something", platform="navimow")
    assert names(entry, opts) == []


def test_car_label_from_integration():
    # evcc_intg is deliberately NOT curated (see rules.py) — it's a
    # whole-house energy controller, not a car-only integration. "Auto"
    # still applies here, just via the " evcc " keyword instead of a
    # blanket platform label, which lets other evcc entities (a pool pump
    # loadpoint, the home battery) get their own theme instead.
    entry = FakeEntry("sensor.evcc_ladestand", platform="evcc_intg")
    assert "Auto" in names(entry)


def test_car_label_from_keyword():
    # "wallbox" -> car and "leistung" -> energy (capped at 2)
    assert "Auto" in names(FakeEntry("sensor.wallbox_ladung"))


def test_keyword_pv_grid_energy():
    assert names(FakeEntry("sensor.pv_grid_share")) == ["Energie"]
    assert names(FakeEntry("sensor.spannung_l1")) == ["Energie"]


def test_keyword_uv_weather():
    assert names(FakeEntry("sensor.uv_hoch")) == ["Wetter"]


def test_keyword_personal_device_presence():
    # sensor domain has no label; "iphone" keyword -> presence
    assert names(FakeEntry("sensor.iphone_von_johanna")) == ["Anwesenheit"]


def test_marstek_integration_energy():
    assert names(FakeEntry("sensor.venus_x", platform="marstek_modbus")) == ["Energie"]


def test_reolink_integration_cameras():
    assert names(FakeEntry("sensor.reolink_x", platform="reolink")) == ["Kameras"]


def test_integration_themes_extra():
    cases = {
        "frigate": "Kameras",
        "dwd_weather": "Wetter",
        "hassio": "Netzwerk & Server",
        "backup": "Netzwerk & Server",
    }
    for platform, label in cases.items():
        assert names(FakeEntry("sensor.x", platform=platform)) == [label], platform


def test_reolink_keyword_via_name():
    assert names(FakeEntry("sensor.reolink_x906b_status")) == ["Kameras"]
    # with "motion" in the name, both Bewegung and Kameras apply
    assert "Kameras" in names(FakeEntry("sensor.reolink_x906b_motion"))


def test_keyword_consumption_energy():
    assert names(FakeEntry("sensor.plug1_summe_verbraucht")) == ["Energie"]
    assert names(FakeEntry("sensor.shelly_em_summe_eingespeist")) == ["Energie"]


def test_keyword_doors_windows_by_name():
    assert names(FakeEntry("binary_sensor.eingangstuer")) == ["Sicherheit"]
    assert names(FakeEntry("binary_sensor.garagentor")) == ["Sicherheit"]


def test_keyword_weather_station():
    assert names(FakeEntry("sensor.shelly_ecowitt_ws90_boengeschwindigkeit")) == ["Wetter"]


def test_keyword_lichterkette_lights():
    assert names(FakeEntry("sensor.flur_lichterkette")) == ["Beleuchtung"]


def test_keyword_voc_air_quality():
    assert names(FakeEntry("sensor.wohnzimmer_tvoc_voc")) == ["Luftqualität"]


def test_keyword_fanfreq_climate():
    assert names(FakeEntry("sensor.wohnzimmer_ac_fanfreq")) == ["Klima"]


def test_keyword_water_group():
    assert names(FakeEntry("sensor.wasserzaehler_stand")) == ["Wasser"]


def test_keyword_climate_group():
    assert names(FakeEntry("sensor.heizung_vorlauf")) == ["Klima"]


def test_keyword_matches_friendly_name():
    entry = FakeEntry("sensor.xyz_123")
    entry.name = "Waschmaschine Restzeit"
    assert "Haushaltsgeräte" in names(entry)


def test_keyword_umlaut_in_name():
    entry = FakeEntry("sensor.abc")
    entry.name = "Lüfter Bad"
    assert names(entry) == ["Lüfter"]


def test_keyword_runs_alongside_device_class():
    # Since v0.10 a device_class match no longer blocks the keyword pass —
    # only a curated integration match does. A water-temperature sensor
    # gets both themes instead of being capped at "Temperatur".
    entry = FakeEntry("sensor.wasser_temp", original_device_class="temperature")
    result = names(entry)
    assert "Temperatur" in result
    assert "Wasser" in result


def test_curated_appliance_label():
    entry = FakeEntry("binary_sensor.waschmaschine", platform="ha_washdata")
    assert "Haushaltsgeräte" in names(entry)


def test_monetary_maps_to_cost():
    entry = FakeEntry("sensor.strompreis", original_device_class="monetary")
    assert "Kosten" in names(entry)


def test_lawn_mower_domain_maps_to_mower():
    # A robotic mower is its own theme, not "Auto" (issue #4). "Garten"
    # legitimately also applies here via the "vorgarten" keyword — the
    # mower really is garden equipment, just not filed under the generic
    # theme alone any more.
    result = names(FakeEntry("lawn_mower.vorgarten"))
    assert "Mähroboter" in result
    assert "Auto" not in result


def test_weather_device_classes_map_to_weather():
    for dc in ("wind_speed", "precipitation", "uv_index", "irradiance"):
        entry = FakeEntry("sensor.x", original_device_class=dc)
        assert "Wetter" in names(entry), dc


def test_apparent_power_groups_into_energy():
    entry = FakeEntry("sensor.x", original_device_class="apparent_power")
    assert "Energie" in names(entry)


def test_vibration_maps_to_motion():
    entry = FakeEntry("binary_sensor.x", original_device_class="vibration")
    assert "Bewegung" in names(entry)


def test_voc_maps_to_air_quality():
    entry = FakeEntry(
        "sensor.x", original_device_class="volatile_organic_compounds"
    )
    assert "Luftqualität" in names(entry)


def test_area_floor_specs_disabled_by_default():
    assert area_floor_specs("Wohnzimmer", "Erdgeschoss", OrganizerOptions()) == []


def test_area_floor_specs_area_only():
    opts = OrganizerOptions(enable_area=True)
    specs = area_floor_specs("Wohnzimmer", "Erdgeschoss", opts)
    assert [s["name"] for s in specs] == ["Wohnzimmer"]


def test_area_floor_specs_both():
    opts = OrganizerOptions(enable_area=True, enable_floor=True)
    specs = area_floor_specs("Küche", "Erdgeschoss", opts)
    assert [s["name"] for s in specs] == ["Küche", "Erdgeschoss"]


def test_area_floor_specs_missing_names_skipped():
    opts = OrganizerOptions(enable_area=True, enable_floor=True)
    assert area_floor_specs(None, None, opts) == []


# --- Regression guards for user label preferences -----------------------

REMOVED_LABEL_NAMES = {
    "Sensoren",
    "Binärsensoren",
    "Steuerung",
    "Taster",
    "Druck",
    "Verbindung",
}


def test_removed_label_names_not_in_catalog():
    present = {ld["names"]["de"] for ld in rules.LABELS.values()}
    assert present.isdisjoint(REMOVED_LABEL_NAMES), present & REMOVED_LABEL_NAMES


def test_removed_domains_produce_no_label():
    for domain in ("sensor", "binary_sensor", "number", "select", "button"):
        entry = FakeEntry(f"{domain}.plain_no_dc")
        assert names(entry) == [], domain


def test_removed_device_classes_produce_no_label():
    for dc in ("pressure", "atmospheric_pressure", "connectivity", "signal_strength"):
        entry = FakeEntry("sensor.x", original_device_class=dc)
        assert names(entry) == [], dc


def test_energy_is_a_single_label_not_split():
    energy_dcs = (
        "power", "energy", "current", "voltage", "gas",
        "apparent_power", "reactive_power", "power_factor", "frequency",
    )
    produced = set()
    for dc in energy_dcs:
        produced.update(names(FakeEntry("sensor.x", original_device_class=dc)))
    assert produced == {"Energie"}, produced


def test_heating_domains_go_into_klima():
    for domain in ("climate", "water_heater", "humidifier"):
        entry = FakeEntry(f"{domain}.thermostat")
        assert "Klima" in names(entry), domain


def test_energy_and_lights_have_distinct_colors():
    assert rules.LABELS["energy"]["color"] != rules.LABELS["lights"]["color"]


def test_is_excluded_empty():
    assert is_excluded("light.k", ()) is False


def test_is_excluded_by_domain():
    assert is_excluded("sensor.x", ("sensor",)) is True
    assert is_excluded("light.x", ("sensor",)) is False


def test_is_excluded_by_exact_id_and_glob():
    assert is_excluded("light.kitchen", ("light.kitchen",)) is True
    assert is_excluded("sensor.test_foo", ("sensor.test_*",)) is True
    assert is_excluded("sensor.other", ("sensor.test_*",)) is False


def test_excluded_entity_gets_no_label():
    opts = OrganizerOptions(exclude=("light",))
    assert names(FakeEntry("light.kitchen"), opts) == []
    # other domains unaffected
    assert names(FakeEntry("switch.k"), opts) == ["Schalter"]


def test_parse_custom_rules_valid_and_invalid():
    rules_map = parse_custom_rules("pool=water\nspielzimmer=media, bogus=doesnotexist")
    assert rules_map == {"pool": "water", "spielzimmer": "media"}


def test_parse_custom_rules_empty():
    assert parse_custom_rules("") == {}
    assert parse_custom_rules(None) == {}


def test_custom_rule_applied_as_fallback():
    opts = OrganizerOptions(custom_rules={"pool": "water"})
    assert names(FakeEntry("sensor.pool_ph"), opts) == ["Wasser"]


def test_invalid_custom_rule_labels():
    assert invalid_custom_rule_labels("pool=water\nx=nope, y=media") == ["nope"]
    assert invalid_custom_rule_labels("pool=water") == []
    assert invalid_custom_rule_labels("") == []


def test_custom_rule_runs_alongside_domain_match():
    # Since v0.10 a domain match no longer blocks custom rules either —
    # only a curated integration match does.
    opts = OrganizerOptions(custom_rules={"kitchen": "water"})
    result = names(FakeEntry("light.kitchen"), opts)
    assert "Beleuchtung" in result
    assert "Wasser" in result


def test_affected_count_none_and_empty():
    assert affected_count(None) == 0
    assert affected_count({}) == 0


def test_affected_count_sums_labels_and_areas():
    last = {"labels": {"updated": 10}, "areas": {"assigned": 5}}
    assert affected_count(last) == 15


def test_affected_count_cleanup_and_remove_all():
    assert affected_count({"cleanup": {"updated": 7}}) == 7
    assert affected_count({"remove_all": {"updated": 42}}) == 42


def test_affected_count_ignores_non_dict_sections():
    # robustness: missing/garbage sections must not raise
    assert affected_count({"labels": None, "scope": "labels"}) == 0


def test_label_differs_detects_color_and_icon_drift():
    spec = label_spec("energy")  # lime / mdi:flash
    assert label_differs("amber", spec["icon"], spec) is True
    assert label_differs(spec["color"], "mdi:other", spec) is True
    assert label_differs(spec["color"], spec["icon"], spec) is False


def test_label_names_are_unique_per_language():
    for lang in rules.SUPPORTED_LANGUAGES:
        seen = [ld["names"][lang] for ld in rules.LABELS.values()]
        assert len(seen) == len(set(seen)), f"duplicate name in {lang}"


def test_binary_climate_device_classes_map_to_klima():
    for dc in ("cold", "heat"):
        entry = FakeEntry("binary_sensor.x", original_device_class=dc)
        assert names(entry) == ["Klima"], dc


def test_binary_light_maps_to_light_level():
    entry = FakeEntry("binary_sensor.x", original_device_class="light")
    assert names(entry) == ["Helligkeit"]


def test_plug_and_energy_distance_map_to_energy():
    for dc in ("plug", "energy_distance"):
        entry = FakeEntry("sensor.x", original_device_class=dc)
        assert names(entry) == ["Energie"], dc


def test_update_device_class_maps_to_updates():
    entry = FakeEntry("binary_sensor.x", original_device_class="update")
    assert names(entry) == ["Updates"]


def test_raw_integration_label_skipped_for_diagnostic():
    # The raw platform label (enable_integration) is still correctly kept
    # off a diagnostic entity — it just no longer means the entity ends up
    # with *no* label at all, see test_diagnostic_entities_get_generic_label.
    opts = OrganizerOptions(enable_integration=True, enable_curated=False)
    entry = FakeEntry("sensor.x", platform="foo", entity_category="diagnostic")
    assert names(entry, opts) == ["Diagnose"]


# --- area matching -------------------------------------------------------

def test_match_area_from_entity_id():
    assert match_area("light.wohnzimmer_decke", None, AREAS) == "wohnzimmer"


def test_match_area_handles_umlaut():
    assert match_area("sensor.kueche_temperatur", "Küche Temperatur", AREAS) == "kueche"


def test_match_area_via_alias():
    assert match_area("switch.kitchen_coffee", None, AREAS) == "kueche"


def test_match_area_from_friendly_name():
    assert match_area("sensor.xyz_123", "Schlafzimmer Fenster", AREAS) == "schlafzimmer"


def test_match_area_none_when_no_match():
    assert match_area("sensor.cpu_load", "CPU Load", AREAS) is None


def test_match_area_longest_wins():
    areas = [
        {"area_id": "bad", "name": "Bad", "aliases": []},
        {"area_id": "gaeste_bad", "name": "Gäste Bad", "aliases": []},
    ]
    # "gaeste bad" is longer/more specific than "bad"
    assert match_area("light.gaeste_bad_spiegel", None, areas) == "gaeste_bad"


def test_doors_and_windows_map_to_security():
    for dc in ("door", "window", "garage_door", "opening"):
        entry = FakeEntry("binary_sensor.x", original_device_class=dc)
        assert names(entry) == ["Sicherheit"], dc


def test_openings_label_removed():
    assert "openings" not in rules.LABELS
    present = {ld["names"]["de"] for ld in rules.LABELS.values()}
    assert "Öffnungen" not in present


def test_car_name_labeled_as_auto():
    assert names(FakeEntry("sensor.egolf_reichweite")) == ["Auto"]


def test_car_name_via_friendly_name():
    entry = FakeEntry("sensor.xyz", original_device_class=None)
    entry.name = "Tesla Ladestand"
    assert "Auto" in names(entry)


def test_car_name_plus_device_class_within_cap():
    entry = FakeEntry("sensor.egolf_batterie", original_device_class="battery")
    assert names(entry) == ["Auto", "Batterie"]


def test_frost_keyword_maps_to_weather():
    # "frost" itself is now whole-word padded (was an unpadded 5-char root
    # silently matching inside any glued compound containing it — the same
    # bug class as "pv" matching inside "pve"). The specific compound
    # "frostwarnung" already has its own dedicated, more precise entry.
    assert "Temperatur" in names(FakeEntry("binary_sensor.frostwarnung"))
    assert "Wetter" in names(FakeEntry("sensor.frost_heute_nacht"))


def test_oil_consumption_maps_to_klima():
    assert names(FakeEntry("sensor.taglicher_olverbrauch")) == ["Klima"]


def test_oilfox_integration_maps_to_klima():
    assert names(FakeEntry("sensor.oilfox_fuellstand", platform="oilfox")) == ["Klima"]


def test_max_labels_cap():
    opts = OrganizerOptions(max_labels=1)
    entry = FakeEntry("sensor.maeher", platform="navimow",
                      original_device_class="temperature")
    # curated Mähroboter + Temperatur would be 2, capped to 1
    assert names(entry, opts) == ["Mähroboter"]


def test_max_labels_default_is_three():
    # mower (curated) + car (CAR_NAME_KEYWORDS) + battery (device_class)
    # all fit under the v0.10 default cap of 3.
    entry = FakeEntry("sensor.egolf_batterie", platform="navimow",
                      original_device_class="battery")
    result = names(entry)
    assert len(result) == 3
    assert set(result) == {"Mähroboter", "Auto", "Batterie"}


def test_max_labels_cap_still_truncates():
    opts = OrganizerOptions(max_labels=2)
    entry = FakeEntry("sensor.egolf_batterie", platform="navimow",
                      original_device_class="battery")
    assert len(names(entry, opts)) == 2


def test_match_area_first_token_wins_over_later_one():
    areas = [
        {"area_id": "a1", "name": "Nord", "aliases": []},
        {"area_id": "a2", "name": "Süd", "aliases": []},
    ]
    # Two equally long candidates: the one at the head of the name is the
    # entity's own room, the later one is what it refers to.
    assert match_area("sensor.nord_sued_klima", None, areas) == "a1"


def test_match_area_ambiguous_returns_none():
    areas = [
        {"area_id": "a1", "name": "Nord", "aliases": []},
        {"area_id": "a2", "name": "Nord", "aliases": []},
    ]
    # Same position, same length, different areas -> genuinely undecidable.
    assert match_area("sensor.nord_klima", None, areas) is None


def test_match_area_matches_ha_slug_of_umlaut_area():
    # HA slugifies "Büro" to "buro", not "buero" — the area has to match its
    # own entity ids.
    areas = [{"area_id": "buro", "name": "Büro", "aliases": []}]
    assert match_area("binary_sensor.thread_presence_buro", None, areas) == "buro"
    assert match_area("sensor.kuche_fp300_temperatur", None, [
        {"area_id": "kuche", "name": "Küche", "aliases": []}
    ]) == "kuche"


def test_match_area_own_room_beats_measurement_target():
    areas = [
        {"area_id": "wohnzimmer", "name": "Wohnzimmer", "aliases": []},
        {"area_id": "sittingpit", "name": "Sittingpit", "aliases": []},
    ]
    entity = "sensor.thread_presence_wohnzimmer_rssi_sittingpit_rechts"
    assert match_area(entity, None, areas) == "wohnzimmer"


def test_match_area_longer_wins_at_same_position():
    areas = [
        {"area_id": "bad", "name": "Bad", "aliases": []},
        {"area_id": "bad_klo", "name": "Bad Klo", "aliases": []},
    ]
    assert match_area("light.bad_klo_spiegel", None, areas) == "bad_klo"


def test_match_area_device_name_is_fallback_only():
    areas = [
        {"area_id": "kueche", "name": "Küche", "aliases": []},
        {"area_id": "wohnzimmer", "name": "Wohnzimmer", "aliases": []},
    ]
    # Entity carries no room -> device name decides.
    assert (
        match_area("light.hue_color_lamp_3", None, areas, device_name="Hue Küche")
        == "kueche"
    )
    # Entity carries a room -> the device must not override it.
    assert (
        match_area(
            "light.wohnzimmer_stehlampe", None, areas, device_name="Hue Bridge Küche"
        )
        == "wohnzimmer"
    )


def test_waste_collection_schedule_curated():
    entry = FakeEntry("calendar.waste_collection_schedule_abfallkalender",
                      platform="waste_collection_schedule")
    assert names(entry) == ["Abfall"]


def test_tgtg_curated():
    entry = FakeEntry("sensor.tgtg_oh_mother", platform="tgtg")
    assert names(entry) == ["Einkauf"]


def test_grocy_curated_not_waste():
    # A Grocy product entity can be named after anything in the pantry
    # (e.g. "Frittierfett" - frying fat), which collides with the
    # unrelated "waste" keyword vocabulary (used cooking-oil disposal).
    # The curated integration label wins so every Grocy entity is
    # "Einkauf" regardless of the product name. See GH issue #2.
    entry = FakeEntry(
        "sensor.shopping_list_with_grocy_product_frittierfett_202",
        platform="grocy",
    )
    assert names(entry) == ["Einkauf"]


def test_ac_verbrauch_keyword():
    assert names(FakeEntry("sensor.buero_ac_verbrauch")) == ["Energie"]


def test_shelly_flood_keyword():
    assert names(FakeEntry("binary_sensor.shelly_flood")) == ["Leck"]


def test_kiosk_and_screensaver_keywords():
    assert names(FakeEntry("binary_sensor.sm_x906b_kiosk_mode")) == ["Anwesenheit"]
    assert names(FakeEntry("binary_sensor.sm_x906b_screensaver")) == ["Anwesenheit"]


def test_door_compound_keywords():
    assert names(FakeEntry("binary_sensor.eingangstur")) == ["Sicherheit"]
    assert names(FakeEntry("binary_sensor.haustuer_kontakt")) == ["Sicherheit"]


def test_garden_watering_keywords():
    assert names(FakeEntry("input_boolean.heute_rasen_giessen")) == ["Garten"]


def test_oil_price_keyword():
    assert names(FakeEntry("input_number.olpreis_pro_liter")) == ["Kosten"]


def test_ble_temp_keyword():
    # "ble temp" (climate) and the generic " temp " (temperature) both apply;
    # the longer, more specific "ble temp" now takes priority (see
    # KEYWORD_LABELS_BY_LENGTH in rules.py).
    assert names(FakeEntry("sensor.buero_ac_ble_temp")) == ["Klima", "Temperatur"]


def test_new_domains():
    # "garden hose" also legitimately matches the garden keyword now that a
    # domain match no longer blocks the keyword pass.
    assert "Rollläden" in names(FakeEntry("valve.garden_hose"))
    assert names(FakeEntry("tts.piper")) == ["Medien"]
    assert names(FakeEntry("stt.whisper")) == ["Medien"]


def test_new_device_classes():
    assert names(FakeEntry("sensor.tank", original_device_class="volume")) == ["Wasser"]
    assert names(FakeEntry("sensor.pool", original_device_class="ph")) == ["Wasser"]


def test_new_integrations():
    assert names(FakeEntry("sensor.x", platform="tibber")) == ["Kosten"]
    assert names(FakeEntry("device_tracker.x", platform="life360")) == ["Anwesenheit"]
    assert names(FakeEntry("camera.x", platform="ring")) == ["Kameras"]
    assert names(FakeEntry("lock.x", platform="nuki")) == ["Schlösser"]
    assert names(FakeEntry("sensor.x", platform="solaredge")) == ["Energie"]


def test_no_false_positive_oven_substring():
    assert names(FakeEntry("sensor.woven_fabric_display")) == []
    assert names(FakeEntry("sensor.provencal_recipe")) == []


def test_english_appliance_words():
    assert "Haushaltsgeräte" in names(FakeEntry("sensor.kitchen_oven_temp"))
    assert names(FakeEntry("sensor.wine_fridge")) == ["Haushaltsgeräte"]


def test_car_brand_e_tron():
    assert names(FakeEntry("sensor.audi_e_tron_range")) == ["Auto"]


def test_light_synonyms_de_en():
    assert names(FakeEntry("sensor.wohnzimmer_lampe")) == ["Beleuchtung"]
    assert names(FakeEntry("sensor.flur_licht")) == ["Beleuchtung"]
    assert names(FakeEntry("sensor.spot_kueche")) == ["Beleuchtung"]
    assert names(FakeEntry("sensor.strahler_wohnzimmer")) == ["Beleuchtung"]
    assert names(FakeEntry("sensor.hallway_nightlight")) == ["Beleuchtung"]
    assert names(FakeEntry("sensor.living_room_lamp")) == ["Beleuchtung"]


def test_light_synonym_word_boundary_no_false_positive():
    assert names(FakeEntry("input_boolean.wartungspflicht")) == []
    assert names(FakeEntry("sensor.birnensaft_menge")) == []
    # "strahler" (lights) must not match inside "heizstrahler" — the entity
    # correctly picks up the (separately added) "heizstrahler"->climate
    # keyword instead, so just confirm no incorrect Lights label.
    assert "Beleuchtung" not in names(FakeEntry("sensor.heizstrahler_terrasse"))


def test_switch_and_outlet_synonyms():
    assert names(FakeEntry("sensor.wohnzimmer_steckdose")) == ["Schalter"]
    assert names(FakeEntry("sensor.kueche_outlet")) == ["Schalter"]
    assert names(FakeEntry("sensor.buero_smart_plug")) == ["Schalter"]


def test_tv_synonym_no_socket_false_positive():
    assert names(FakeEntry("sensor.tv_wohnzimmer")) == ["Medien"]
    assert names(FakeEntry("sensor.websocket_status")) == []
    assert names(FakeEntry("sensor.basket_count")) == []


def test_vacuum_synonyms():
    assert names(FakeEntry("sensor.wohnzimmer_staubsauger")) == ["Staubsauger"]
    assert names(FakeEntry("sensor.roomba_status")) == ["Staubsauger"]
    assert names(FakeEntry("binary_sensor.robot_vacuum_error")) == ["Staubsauger"]


def test_camera_synonyms():
    assert "Kameras" in names(FakeEntry("sensor.eingang_kamera"))
    assert names(FakeEntry("sensor.garage_webcam")) == ["Kameras"]
    assert "Kameras" in names(FakeEntry("sensor.haustuer_video_doorbell"))


def test_waste_generic_keywords():
    assert names(FakeEntry("sensor.restmuell_naechste_abholung")) == ["Abfall"]
    assert names(FakeEntry("sensor.recycling_pickup")) == ["Abfall"]


def test_updates_keywords():
    assert names(FakeEntry("sensor.aktualisierung_verfuegbar")) == ["Updates"]
    assert names(FakeEntry("sensor.software_update_check")) == ["Updates"]


def test_lock_synonyms():
    assert "Schlösser" in names(FakeEntry("binary_sensor.haustuer_schloss"))
    assert "Schlösser" in names(FakeEntry("binary_sensor.tuerriegel_status"))


def test_fan_synonyms_no_infant_false_positive():
    assert names(FakeEntry("sensor.buero_geblaese")) == ["Lüfter"]
    assert names(FakeEntry("sensor.infant_temperature")) == ["Temperatur"]


def test_doorbell_and_klingel():
    assert names(FakeEntry("binary_sensor.haustuer_klingel")) == ["Sicherheit"]


def test_no_false_positive_blumenkohl_and_overflow():
    # "blumen" (garden) must not match inside "blumenkohl" (cauliflower) —
    # the entity separately matches "vorrat" (shopping), which is correct.
    assert "Garten" not in names(FakeEntry("sensor.blumenkohl_vorrat"))
    assert names(FakeEntry("binary_sensor.buffer_overflow")) == []


def test_no_false_positive_snack_riegel():
    # "riegel" alone must not map to locks (only "tuerriegel" does) — the
    # entity separately matches "vorrat" (shopping), which is correct.
    assert "Schlösser" not in names(FakeEntry("sensor.riegel_snack_vorrat"))


def test_shopping_generic_keywords():
    assert names(FakeEntry("sensor.einkaufsliste")) == ["Einkauf"]
    # "reminder" also (correctly) matches the automations vocab since the
    # 2026-07-16 batch, so check membership instead of exact equality.
    assert "Einkauf" in names(FakeEntry("sensor.grocery_reminder"))


def test_enabled_labels_restricts_to_allowlist():
    opts = OrganizerOptions(enabled_labels=frozenset({"lights"}))
    assert names(FakeEntry("light.k"), opts) == ["Beleuchtung"]
    assert names(FakeEntry("switch.k"), opts) == []


def test_enabled_labels_empty_means_unrestricted():
    opts = OrganizerOptions(enabled_labels=frozenset())
    assert names(FakeEntry("light.k"), opts) == ["Beleuchtung"]
    assert names(FakeEntry("switch.k"), opts) == ["Schalter"]


def test_enabled_labels_filters_curated_and_keyword_matches():
    opts = OrganizerOptions(enabled_labels=frozenset({"car"}))
    # "wallbox" keyword -> car (allowed) and "leistung" -> energy (blocked)
    assert names(FakeEntry("sensor.wallbox_ladung"), opts) == ["Auto"]


def test_suggest_entity_icon_keyword_beats_domain():
    from rules import suggest_entity_icon
    # domain "media_player" -> Medien (generic), but "tv" keyword is more specific
    entry = FakeEntry("media_player.wohnzimmer_tv")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:television"


def test_suggest_entity_icon_appliance_keyword():
    from rules import suggest_entity_icon
    entry = FakeEntry("sensor.kaffeemaschine_kueche")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:coffee-maker"


def test_suggest_entity_icon_integration_platform():
    from rules import suggest_entity_icon
    entry = FakeEntry("media_player.x", platform="spotify")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:spotify"


def test_suggest_entity_icon_none_when_nothing_specific():
    from rules import suggest_entity_icon
    # "sensor" has no domain-level icon (relies on device_class instead),
    # and this entity has neither a recognizable keyword nor a device_class
    entry = FakeEntry("sensor.plain_thing_xyz")
    assert suggest_entity_icon(entry, OrganizerOptions()) is None


def test_suggest_entity_icon_domain_fallback_covers_every_domain():
    from rules import suggest_entity_icon
    for domain in rules.DOMAIN_LABELS:
        entry = FakeEntry(f"{domain}.some_generic_entity_name")
        result = suggest_entity_icon(entry, OrganizerOptions())
        if domain in rules.STATEFUL_ICON_DOMAINS:
            # These always keep HA's own per-state icon (locked/unlocked,
            # open/closed, armed, cleaning/docked...) — a registry override
            # would freeze it to one shape, so no suggestion is correct.
            assert result is None, domain
        else:
            assert result is not None, domain


def test_suggest_entity_icon_never_overrides_stateful_domains():
    from rules import suggest_entity_icon
    for domain in rules.STATEFUL_ICON_DOMAINS:
        # Even a specific keyword match must not win here.
        entry = FakeEntry(f"{domain}.eingangstuer")
        assert suggest_entity_icon(entry, OrganizerOptions()) is None, domain


def test_suggest_entity_icon_binary_sensor_only_stateful_with_device_class():
    from rules import suggest_entity_icon

    # No device_class -> HA shows one static icon regardless of state, so a
    # keyword-based suggestion is safe and useful.
    entry = FakeEntry("binary_sensor.feuermelder_flur")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:smoke-detector"

    # With a device_class -> HA already swaps the icon per state, so no
    # suggestion must be made even though the same keyword matches.
    entry = FakeEntry("binary_sensor.feuermelder_flur", device_class="smoke")
    assert suggest_entity_icon(entry, OrganizerOptions()) is None


def test_suggest_entity_icon_platform_beats_domain():
    from rules import suggest_entity_icon
    # Spotify (a specific service) should win over the generic media_player
    # domain icon, since it names the actual product, not just the category
    entry = FakeEntry("media_player.x", platform="spotify")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:spotify"


def test_suggest_entity_icon_respects_exclude():
    from rules import suggest_entity_icon
    opts = OrganizerOptions(exclude=("sensor.kaffeemaschine_kueche",))
    entry = FakeEntry("sensor.kaffeemaschine_kueche")
    assert suggest_entity_icon(entry, opts) is None


def test_specific_icons_keys_are_reachable():
    # Every SPECIFIC_ICONS key must match a real keyword/domain/device_class/
    # platform/car-name — otherwise it's dead code from a typo and can never
    # be suggested.
    known = (
        set(rules.KEYWORD_LABELS)
        | set(rules.DOMAIN_LABELS)
        | set(rules.DEVICE_CLASS_LABELS)
        | set(rules.INTEGRATION_LABELS)
        | set(rules.CAR_NAME_KEYWORDS)
    )
    known_stripped = {k.strip() for k in known}
    for key in rules.SPECIFIC_ICONS:
        assert key in known_stripped, f"orphaned SPECIFIC_ICONS key: {key!r}"


def test_specific_icons_are_valid_mdi_strings():
    for key, icon in rules.SPECIFIC_ICONS.items():
        assert icon.startswith("mdi:"), key


def test_new_specific_icon_words():
    from rules import suggest_entity_icon as icon_for
    opts = OrganizerOptions()
    cases = {
        "sensor.kaffee_vorrat": "mdi:coffee-maker",
        "sensor.wasserkocher_kueche": "mdi:kettle",
        "sensor.nuki_battery_level": "mdi:lock",
        "sensor.access_point_status": "mdi:access-point",
        "binary_sensor.feuermelder_flur": "mdi:smoke-detector",
        "sensor.dunstabzugshaube_stufe": "mdi:air-filter",
        "sensor.iphone_von_johanna": "mdi:cellphone",
        "sensor.heizkoerper_wohnzimmer": "mdi:radiator",
        "sensor.rasenroboter_status": "mdi:robot-mower",
        "sensor.tiefkuehltruhe_temp": "mdi:fridge-outline",
        "sensor.aquarium_ph": "mdi:fishbowl",
        "sensor.drucker_tinte": "mdi:printer",
        "sensor.luftreiniger_pm25": "mdi:air-purifier",
        "sensor.luftbefeuchter_status": "mdi:air-humidifier",
        "sensor.deckenventilator_speed": "mdi:ceiling-fan",
        "sensor.stromspeicher_soc": "mdi:home-battery",
        "sensor.co2_buero": "mdi:molecule-co2",
        "binary_sensor.haustuer_kontakt": "mdi:door",
        "binary_sensor.terrassentuer_kontakt": "mdi:door-sliding",
        "sensor.gelbersack_naechste_abholung": "mdi:recycle",
        "sensor.vorhang_wohnzimmer": "mdi:curtains",
        "sensor.futterautomat_katze": "mdi:paw",
        "sensor.whirlpool_temp": "mdi:hot-tub",
        "sensor.kuechenwaage_gewicht": "mdi:scale-balance",
        "sensor.swimming_pool_ph": "mdi:pool",
        "sensor.synology_status": "mdi:nas",
        "sensor.windrichtung_grad": "mdi:compass",
        "sensor.family_location": "mdi:account-group",
        "binary_sensor.ring_video_doorbell": "mdi:doorbell-video",
        "binary_sensor.wohnung_klingel": "mdi:doorbell",
        "binary_sensor.kohlenmonoxid_melder": "mdi:molecule-co",
    }
    for eid, expected in cases.items():
        assert icon_for(FakeEntry(eid), opts) == expected, eid


def test_suggest_entity_icon_longer_keyword_beats_shorter_substring():
    from rules import suggest_entity_icon
    # Regression test for the "first match in dict order wins" bug: a
    # generic keyword ("power" -> mdi:power) must not shadow a more specific
    # compound word ("powerwall" -> mdi:home-battery) that contains it as a
    # substring, no matter which one was merged into KEYWORD_LABELS first.
    entry = FakeEntry("sensor.tesla_powerwall_soc")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:home-battery"


def test_keyword_labels_by_length_is_sorted_and_complete():
    # KEYWORD_LABELS_BY_LENGTH is what makes the longest-match fix above
    # (and the equivalent priority fix in _collect_label_keys) actually
    # take effect — guard its two invariants directly so a future refactor
    # can't silently regress back to dict-insertion-order matching.
    pairs = rules.KEYWORD_LABELS_BY_LENGTH
    assert len(pairs) == len(rules.KEYWORD_LABELS)
    assert dict(pairs) == rules.KEYWORD_LABELS
    lengths = [len(needle) for needle, _key in pairs]
    assert lengths == sorted(lengths, reverse=True)


def test_no_false_positive_smartlockdown_and_ofenrohr():
    # "smartlock" (locks) must not match inside "smartlockdown" — the
    # entity separately matches "lockdown" (security), which is correct.
    assert "Schlösser" not in names(FakeEntry("binary_sensor.smartlockdown_status"))
    assert names(FakeEntry("sensor.ofenrohr_status")) == []
    assert names(FakeEntry("sensor.infektionsherd_counter")) == []


def test_specific_icons_word_coverage_per_icon():
    # Loose sanity metric: most curated icons should have multiple matching
    # words, not just a single one-off keyword.
    from collections import Counter
    counts = Counter(rules.SPECIFIC_ICONS.values())
    multi_word_icons = sum(1 for n in counts.values() if n >= 2)
    assert multi_word_icons >= 20


def test_pv_keyword_is_whole_word_not_pve_substring():
    from rules import suggest_entity_icon
    # Live bug: unpadded "pv" silently matched inside "pve" (the Proxmox
    # host's own hostname abbreviation), mislabeling/re-iconing dozens of
    # unrelated Proxmox sensors (GPU/NVMe/RAM/load) as solar/energy.
    entry = FakeEntry("sensor.proxmox_host_pve_gpu_temperatur", original_device_class="temperature")
    # "Netzwerk & Server" now legitimately also applies (the real, padded
    # "proxmox" keyword) — what this test actually guards against is "pv"
    # leaking out of "pve" into "Energie", which it must not.
    assert "Temperatur" in names(entry)
    assert "Energie" not in names(entry)
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:thermometer"
    # The legitimate whole-word case (a real PV/solar entity) must still match.
    assert "Energie" in names(FakeEntry("sensor.solcast_pv_forecast"))


def test_volume_device_class_not_shadowed_by_audio_keyword():
    from rules import suggest_entity_icon
    # Live bug: SensorDeviceClass.VOLUME (a measured litre/gallon quantity,
    # e.g. oil/water consumption) collided with the unrelated "volume"
    # keyword (audio loudness), producing an mdi:volume-high speaker icon
    # on a plain litres sensor.
    entry = FakeEntry("sensor.heizoeltank_fuellstand", original_device_class="volume")
    icon = suggest_entity_icon(entry, OrganizerOptions())
    assert icon not in (None, "mdi:volume-high")
    # A media player's actual volume control keeps its audio icon.
    assert suggest_entity_icon(FakeEntry("number.wohnzimmer_tv_volume"), OrganizerOptions()) == "mdi:volume-high"


def test_oelverbrauch_gets_oil_icon_not_device_class_fallback():
    from rules import suggest_entity_icon
    entry = FakeEntry("sensor.taglicher_olverbrauch", original_device_class="volume")
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:oil"


def test_grid_icon_is_power_grid_not_ui_layout():
    from rules import suggest_entity_icon
    assert suggest_entity_icon(FakeEntry("sensor.evcc_grid_currents_0"), OrganizerOptions()) == "mdi:transmission-tower"


def test_thread_presence_platform_labeled_presence_not_network():
    from rules import suggest_entity_icon
    # This user's own RF-sensing integration; must never fall through to
    # the (deliberately removed) generic "thread" network keyword.
    entry = FakeEntry(
        "sensor.thread_presence_bad_status", platform="thread_presence", original_device_class="enum"
    )
    assert names(entry) == ["Anwesenheit"]
    assert suggest_entity_icon(entry, OrganizerOptions()) == "mdi:radar"


def test_generic_bridge_platform_does_not_shadow_device_class_icon():
    from rules import suggest_entity_icon
    # Matter/ESPHome/Tasmota host arbitrary heterogeneous device types, so a
    # blanket per-platform icon must not override a perfectly good
    # device_class icon (this affected ~600+ live Matter entities alone).
    # No override exists for device_class "energy" — falling through to
    # None (HA's own device_class-aware default icon) is correct and far
    # better than the old blanket mdi:home-automation.
    entry = FakeEntry("sensor.essbereich_energie", platform="matter", original_device_class="energy")
    assert suggest_entity_icon(entry, OrganizerOptions()) != "mdi:home-automation"
    entry2 = FakeEntry("sensor.garage_oben_links_leistung", platform="matter", original_device_class="power")
    assert suggest_entity_icon(entry2, OrganizerOptions()) == "mdi:power"
    # A genuine product-specific platform (not a generic bridge) still wins.
    assert suggest_entity_icon(FakeEntry("sensor.x", platform="spotify"), OrganizerOptions()) == rules.SPECIFIC_ICONS.get("spotify")


# --- keyword boundary rule (v0.10: no more accidental infix matches) ------


def test_keyword_infix_does_not_match():
    # "wasserverbrauch" contains "server" — a water meter is not a server.
    assert "Netzwerk & Server" not in names(FakeEntry("sensor.wasserverbrauch"))
    assert names(FakeEntry("sensor.wasserverbrauch")) == ["Wasser"]


def test_keyword_matches_compound_prefix_and_suffix():
    # German compounds glue the needle to either end and must still match.
    assert "Wasser" in names(FakeEntry("sensor.wasserverbrauch"))
    assert "Klima" in names(FakeEntry("sensor.heizungskeller_vorlauf"))
    assert "Kosten" in names(FakeEntry("sensor.oelkosten_heute"))


def test_keyword_veto_next_alarm_is_not_security():
    # Issue #3: a phone's next alarm is not a burglar alarm.
    entry = FakeEntry("sensor.iphone_von_henryk_next_alarm")
    assert "Sicherheit" not in names(entry)


def test_keyword_veto_spot_clean_is_not_a_light():
    # Issue #5: "spot clean" on a vacuum is not a spotlight.
    assert "Beleuchtung" not in names(FakeEntry("button.roborock_spot_clean"))


def test_keyword_veto_waste_schedule_is_not_an_automation():
    entry = FakeEntry("sensor.waste_collection_schedule_bioabfall")
    assert names(entry) == ["Abfall"]


# --- curated platform label stays authoritative ---------------------------


def test_curated_platform_label_still_applies():
    entry = FakeEntry("sensor.reolink_x", platform="reolink")
    assert names(entry) == ["Kameras"]


# --- mower theme (issue #4) ----------------------------------------------


def test_mower_keyword_is_not_garden():
    assert names(FakeEntry("sensor.navimow_i105_status")) == ["Mähroboter"]


def test_mower_is_not_a_car():
    assert "Auto" not in names(FakeEntry("lawn_mower.sunseeker"))


def test_irrigation_stays_garden():
    # Only the mower keywords moved; watering hardware keeps "Garten".
    assert "Garten" in names(FakeEntry("sensor.gardena_bewaesserungsventil"))
    assert "Mähroboter" not in names(FakeEntry("sensor.gardena_bewaesserungsventil"))
    assert names(FakeEntry("sensor.rasensprenger_status")) == ["Garten"]


# --- car-name keyword exceptions (issue #4 follow-up) ---------------------


def test_leaf_wetness_is_not_a_nissan_leaf():
    # A weather station's leaf-wetness sensor is not a Nissan Leaf. Before
    # the CAR_NAME_KEYWORD_EXCEPTIONS fix, "leaf" matching first also
    # blocked the correct "humidity" keyword label (curated_hit gating).
    entry = FakeEntry("sensor.ws_leaf_wetness")
    result = names(entry)
    assert "Auto" not in result
    assert "Luftfeuchtigkeit" in result


def test_nissan_leaf_is_still_a_car():
    assert "Auto" in names(FakeEntry("sensor.nissan_leaf_battery"))


# --- affected_count counts icon-only runs --------------------------------


def test_affected_count_includes_icons():
    assert affected_count({"icons": {"icons_set": 12}}) == 12
    assert affected_count({"labels": {"updated": 3}, "icons": {"icons_set": 4}}) == 7


# --- wled: curated removed, generic keyword respects skip_categories ------


def test_wled_light_entity_still_gets_beleuchtung():
    # Real light entities keep "Beleuchtung" via the DOMAIN_LABELS "light"
    # match regardless of platform.
    entry = FakeEntry("light.wled_besta", platform="wled")
    assert "Beleuchtung" in names(entry)


def test_wled_diagnostic_wifi_entity_no_longer_mislabeled():
    # Issue found in the 2026-09-01 audit: curating "wled" -> "lights"
    # bypassed skip_categories and mislabeled the integration's own Wi-Fi/
    # uptime diagnostics as "Beleuchtung". Removing the curated entry lets
    # the generic " wled " keyword handle it instead, which correctly
    # respects skip_categories like every other keyword match.
    entry = FakeEntry(
        "sensor.wled_besta_wlan_signal", platform="wled",
        entity_category="diagnostic",
    )
    assert names(entry) == ["Diagnose"]


# --- evcc: curated removed, only the pool pump is vetoed -------------------


def test_evcc_pool_pump_is_not_a_car():
    # Issue found in the 2026-09-01 audit: curating "evcc_intg" -> "car"
    # blanket-labeled a whole-house energy controller's pool-pump loadpoint
    # as "Auto". "Garten" applies via the "poolpumpe" keyword instead, and
    # KEYWORD_VETOES cancels the generic " evcc " -> car reading for it.
    entry = FakeEntry("select.evcc_poolpumpe_mode", platform="evcc_intg")
    result = names(entry)
    assert "Garten" in result
    assert "Auto" not in result


def test_evcc_garage_charger_stays_a_car():
    entry = FakeEntry("sensor.evcc_garage_charge_power", platform="evcc_intg")
    assert "Auto" in names(entry)
