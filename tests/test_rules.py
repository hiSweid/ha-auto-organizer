"""Unit tests for the pure rule engine (no Home Assistant required)."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

# Make the integration importable as a bare module without installing HA.
COMPONENT = Path(__file__).resolve().parents[1] / "custom_components" / "auto_labeler"
sys.path.insert(0, str(COMPONENT))

import rules  # noqa: E402
from rules import LabelerOptions, compute_label_specs  # noqa: E402


@dataclass
class FakeEntry:
    entity_id: str
    device_class: str | None = None
    original_device_class: str | None = None
    platform: str | None = None
    entity_category: str | None = None


def names(entry, options=None):
    return [s["name"] for s in compute_label_specs(entry, options or LabelerOptions())]


def test_domain_label_applied():
    assert names(FakeEntry("light.kitchen")) == ["Beleuchtung"]


def test_device_class_adds_second_label():
    entry = FakeEntry("sensor.outdoor", original_device_class="temperature")
    assert names(entry) == ["Sensoren", "Temperatur"]


def test_user_device_class_overrides_original():
    entry = FakeEntry(
        "sensor.x", device_class="humidity", original_device_class="temperature"
    )
    assert "Luftfeuchtigkeit" in names(entry)
    assert "Temperatur" not in names(entry)


def test_keyword_fallback_only_when_no_match():
    # unknown domain, but entity_id mentions battery
    assert names(FakeEntry("foo.bar_battery")) == ["Batterie"]


def test_no_keyword_fallback_when_domain_matched():
    entry = FakeEntry("light.battery_room")
    assert names(entry) == ["Beleuchtung"]


def test_disable_domain():
    opts = LabelerOptions(enable_domain=False)
    entry = FakeEntry("sensor.x", original_device_class="motion")
    assert names(entry, opts) == ["Bewegung"]


def test_integration_label_opt_in():
    opts = LabelerOptions(enable_integration=True)
    entry = FakeEntry("light.k", platform="hue")
    assert names(entry, opts) == ["Beleuchtung", "hue"]


def test_prefix_applied():
    opts = LabelerOptions(label_prefix="auto:")
    assert names(FakeEntry("light.k"), opts) == ["auto:Beleuchtung"]


def test_no_duplicate_label_names():
    # power + voltage both map to "Energie"; ensure dedupe by name
    entry = FakeEntry("sensor.x", original_device_class="power")
    result = names(entry)
    assert len(result) == len(set(result))


def test_diagnostic_entity_skipped_by_default():
    entry = FakeEntry("sensor.uptime", entity_category="diagnostic")
    assert names(entry) == []


def test_config_entity_skipped_by_default():
    entry = FakeEntry("switch.led_config", entity_category="config")
    assert names(entry) == []


def test_categories_labeled_when_skip_disabled():
    opts = LabelerOptions(skip_categories=False)
    entry = FakeEntry("sensor.uptime", entity_category="diagnostic")
    assert names(entry, opts) == ["Sensoren"]


def test_all_specs_have_valid_color_and_icon():
    valid_colors = {
        "primary", "accent", "red", "pink", "purple", "deep-purple", "indigo",
        "blue", "light-blue", "cyan", "teal", "green", "light-green", "lime",
        "yellow", "amber", "orange", "deep-orange", "brown", "grey", "blue-grey",
    }
    for mapping in (rules.DOMAIN_LABELS, rules.DEVICE_CLASS_LABELS, rules.KEYWORD_LABELS):
        for s in mapping.values():
            assert s["color"] in valid_colors, s
            assert s["icon"].startswith("mdi:"), s
