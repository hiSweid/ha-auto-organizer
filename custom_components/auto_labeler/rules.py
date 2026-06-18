"""Rule definitions for the Auto Labeler integration.

The ruleset is intentionally pure data so it can be extended, unit-tested and
later made configurable without touching the engine in ``labeler.py``.

Each label spec is ``(name, color, icon)``.  ``color`` must be one of Home
Assistant's named label colors and ``icon`` an ``mdi:`` icon.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Protocol, TypedDict


class LabelSpec(TypedDict):
    """A label to create / assign."""

    name: str
    color: str
    icon: str


class EntityLike(Protocol):
    """The subset of an entity registry entry the ruleset reads.

    Declared as a Protocol so the rule engine can be unit-tested with a plain
    stand-in object, without importing Home Assistant.
    """

    entity_id: str
    device_class: str | None
    original_device_class: str | None
    platform: str | None
    entity_category: str | None


@dataclass
class LabelerOptions:
    """Runtime options controlling a labeling run."""

    dry_run: bool = False
    overwrite: bool = False
    enable_domain: bool = True
    enable_device_class: bool = True
    enable_integration: bool = False
    skip_categories: bool = True
    label_prefix: str = ""


def spec(name: str, color: str, icon: str) -> LabelSpec:
    """Build a :class:`LabelSpec`."""
    return {"name": name, "color": color, "icon": icon}


# --- Domain based labels -------------------------------------------------
# Maps an entity domain to a coarse functional label.
DOMAIN_LABELS: Final[dict[str, LabelSpec]] = {
    "light": spec("Beleuchtung", "amber", "mdi:lightbulb-group"),
    "switch": spec("Schalter", "blue", "mdi:toggle-switch"),
    "fan": spec("Lüfter", "cyan", "mdi:fan"),
    "climate": spec("Klima", "teal", "mdi:thermostat"),
    "cover": spec("Rollläden", "brown", "mdi:window-shutter"),
    "lock": spec("Schlösser", "blue-grey", "mdi:lock"),
    "vacuum": spec("Staubsauger", "deep-purple", "mdi:robot-vacuum"),
    "media_player": spec("Medien", "indigo", "mdi:multimedia"),
    "camera": spec("Kameras", "grey", "mdi:cctv"),
    "binary_sensor": spec("Binärsensoren", "light-blue", "mdi:checkbox-marked-circle"),
    "sensor": spec("Sensoren", "light-green", "mdi:gauge"),
    "number": spec("Steuerung", "green", "mdi:knob"),
    "select": spec("Steuerung", "green", "mdi:knob"),
    "button": spec("Taster", "green", "mdi:gesture-tap-button"),
    "scene": spec("Szenen", "purple", "mdi:palette"),
    "automation": spec("Automationen", "pink", "mdi:robot"),
    "script": spec("Skripte", "pink", "mdi:script-text"),
    "device_tracker": spec("Anwesenheit", "orange", "mdi:account-question"),
    "person": spec("Anwesenheit", "orange", "mdi:account"),
    "weather": spec("Wetter", "light-blue", "mdi:weather-partly-cloudy"),
    "update": spec("Updates", "deep-orange", "mdi:package-up"),
    "alarm_control_panel": spec("Sicherheit", "red", "mdi:shield-home"),
    "siren": spec("Sicherheit", "red", "mdi:bullhorn"),
}

# --- Device-class based labels ------------------------------------------
# Finer-grained labels derived from a sensor/binary_sensor device_class.
DEVICE_CLASS_LABELS: Final[dict[str, LabelSpec]] = {
    "temperature": spec("Temperatur", "deep-orange", "mdi:thermometer"),
    "humidity": spec("Luftfeuchtigkeit", "blue", "mdi:water-percent"),
    "pressure": spec("Druck", "blue-grey", "mdi:gauge"),
    "atmospheric_pressure": spec("Druck", "blue-grey", "mdi:gauge"),
    "battery": spec("Batterie", "green", "mdi:battery"),
    "power": spec("Energie", "amber", "mdi:flash"),
    "energy": spec("Energie", "amber", "mdi:flash"),
    "current": spec("Energie", "amber", "mdi:flash"),
    "voltage": spec("Energie", "amber", "mdi:flash"),
    "gas": spec("Energie", "amber", "mdi:meter-gas"),
    "water": spec("Wasser", "light-blue", "mdi:water"),
    "illuminance": spec("Helligkeit", "yellow", "mdi:brightness-6"),
    "motion": spec("Bewegung", "red", "mdi:motion-sensor"),
    "occupancy": spec("Anwesenheit", "orange", "mdi:account-question"),
    "presence": spec("Anwesenheit", "orange", "mdi:account-question"),
    "door": spec("Öffnungen", "brown", "mdi:door"),
    "window": spec("Öffnungen", "brown", "mdi:window-closed-variant"),
    "garage_door": spec("Öffnungen", "brown", "mdi:garage"),
    "opening": spec("Öffnungen", "brown", "mdi:square-outline"),
    "smoke": spec("Sicherheit", "red", "mdi:smoke-detector"),
    "carbon_monoxide": spec("Sicherheit", "red", "mdi:molecule-co"),
    "gas_safety": spec("Sicherheit", "red", "mdi:gas-cylinder"),
    "moisture": spec("Leck", "light-blue", "mdi:water-alert"),
    "connectivity": spec("Verbindung", "grey", "mdi:wifi"),
    "pm25": spec("Luftqualität", "teal", "mdi:air-filter"),
    "pm10": spec("Luftqualität", "teal", "mdi:air-filter"),
    "carbon_dioxide": spec("Luftqualität", "teal", "mdi:molecule-co2"),
    "aqi": spec("Luftqualität", "teal", "mdi:air-filter"),
    "signal_strength": spec("Verbindung", "grey", "mdi:wifi"),
}

# --- entity_id keyword fallbacks ----------------------------------------
# Applied when nothing more specific matched; keyed by substring in entity_id.
KEYWORD_LABELS: Final[dict[str, LabelSpec]] = {
    "battery": spec("Batterie", "green", "mdi:battery"),
    "_power": spec("Energie", "amber", "mdi:flash"),
    "_energy": spec("Energie", "amber", "mdi:flash"),
    "temperature": spec("Temperatur", "deep-orange", "mdi:thermometer"),
    "humidity": spec("Luftfeuchtigkeit", "blue", "mdi:water-percent"),
    "motion": spec("Bewegung", "red", "mdi:motion-sensor"),
}


def compute_label_specs(
    entry: EntityLike, options: LabelerOptions
) -> list[LabelSpec]:
    """Return the list of label specs that apply to a single entity.

    Pure function (no Home Assistant state) so the ruleset can be unit-tested
    in isolation.
    """
    specs: list[LabelSpec] = []
    seen: set[str] = set()

    # Skip config/diagnostic helper entities; they only add noise.
    if options.skip_categories and getattr(entry, "entity_category", None):
        return specs

    def add(s: LabelSpec | None) -> None:
        if s and s["name"] not in seen:
            seen.add(s["name"])
            specs.append(s)

    domain = entry.entity_id.split(".", 1)[0]

    if options.enable_domain:
        add(DOMAIN_LABELS.get(domain))

    if options.enable_device_class:
        device_class = entry.device_class or entry.original_device_class
        if device_class:
            add(DEVICE_CLASS_LABELS.get(device_class))

    # Keyword fallbacks only when nothing more specific matched.
    if not specs:
        entity_id = entry.entity_id.lower()
        for needle, s in KEYWORD_LABELS.items():
            if needle in entity_id:
                add(s)

    if options.enable_integration and entry.platform:
        add({"name": entry.platform, "color": "grey", "icon": "mdi:puzzle"})

    if options.label_prefix:
        specs = [{**s, "name": f"{options.label_prefix}{s['name']}"} for s in specs]

    return specs
