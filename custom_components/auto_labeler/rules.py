"""Rule definitions for the Auto Labeler integration.

The ruleset is intentionally pure data so it can be extended, unit-tested and
later made configurable without touching the engine in ``labeler.py``.

Labels are referenced by a stable *key* (e.g. ``"lights"``).  A key maps to a
color, an ``mdi:`` icon and a per-language display name.  Only German (``de``)
and English (``en``) are supported for now; German is the default.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Protocol, TypedDict

# Supported UI languages. German is the default, English the fallback.
SUPPORTED_LANGUAGES: Final = ("de", "en")
DEFAULT_LANGUAGE: Final = "de"


class LabelSpec(TypedDict):
    """A resolved label to create / assign."""

    name: str
    color: str
    icon: str


class LabelDef(TypedDict):
    """Definition of a label keyed by a stable id, with localized names."""

    color: str
    icon: str
    names: dict[str, str]


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
    language: str = DEFAULT_LANGUAGE
    label_prefix: str = ""


def _ld(color: str, icon: str, de: str, en: str) -> LabelDef:
    """Build a :class:`LabelDef`."""
    return {"color": color, "icon": icon, "names": {"de": de, "en": en}}


# --- Label catalog -------------------------------------------------------
# Stable key -> color, icon, localized names.
LABELS: Final[dict[str, LabelDef]] = {
    # domains
    "lights": _ld("amber", "mdi:lightbulb-group", "Beleuchtung", "Lights"),
    "switches": _ld("blue", "mdi:toggle-switch", "Schalter", "Switches"),
    "fans": _ld("cyan", "mdi:fan", "Lüfter", "Fans"),
    "climate": _ld("teal", "mdi:thermostat", "Klima", "Climate"),
    "covers": _ld("brown", "mdi:window-shutter", "Rollläden", "Covers"),
    "locks": _ld("blue-grey", "mdi:lock", "Schlösser", "Locks"),
    "vacuums": _ld("deep-purple", "mdi:robot-vacuum", "Staubsauger", "Vacuums"),
    "media": _ld("indigo", "mdi:multimedia", "Medien", "Media"),
    "cameras": _ld("grey", "mdi:cctv", "Kameras", "Cameras"),
    "binary_sensors": _ld(
        "light-blue", "mdi:checkbox-marked-circle", "Binärsensoren", "Binary Sensors"
    ),
    "sensors": _ld("light-green", "mdi:gauge", "Sensoren", "Sensors"),
    "controls": _ld("green", "mdi:knob", "Steuerung", "Controls"),
    "buttons": _ld("green", "mdi:gesture-tap-button", "Taster", "Buttons"),
    "scenes": _ld("purple", "mdi:palette", "Szenen", "Scenes"),
    "automations": _ld("pink", "mdi:robot", "Automationen", "Automations"),
    "scripts": _ld("pink", "mdi:script-text", "Skripte", "Scripts"),
    "presence": _ld("orange", "mdi:account-question", "Anwesenheit", "Presence"),
    "weather": _ld(
        "light-blue", "mdi:weather-partly-cloudy", "Wetter", "Weather"
    ),
    "updates": _ld("deep-orange", "mdi:package-up", "Updates", "Updates"),
    "security": _ld("red", "mdi:shield-home", "Sicherheit", "Security"),
    # device classes
    "temperature": _ld(
        "deep-orange", "mdi:thermometer", "Temperatur", "Temperature"
    ),
    "humidity": _ld("blue", "mdi:water-percent", "Luftfeuchtigkeit", "Humidity"),
    "pressure": _ld("blue-grey", "mdi:gauge", "Druck", "Pressure"),
    "battery": _ld("green", "mdi:battery", "Batterie", "Battery"),
    "energy": _ld("amber", "mdi:flash", "Energie", "Energy"),
    "water": _ld("light-blue", "mdi:water", "Wasser", "Water"),
    "light_level": _ld("yellow", "mdi:brightness-6", "Helligkeit", "Light Level"),
    "motion": _ld("red", "mdi:motion-sensor", "Bewegung", "Motion"),
    "openings": _ld("brown", "mdi:door", "Öffnungen", "Openings"),
    "leak": _ld("light-blue", "mdi:water-alert", "Leck", "Leak"),
    "connectivity": _ld("grey", "mdi:wifi", "Verbindung", "Connectivity"),
    "air_quality": _ld("teal", "mdi:air-filter", "Luftqualität", "Air Quality"),
}


# --- Domain -> label key -------------------------------------------------
DOMAIN_LABELS: Final[dict[str, str]] = {
    "light": "lights",
    "switch": "switches",
    "fan": "fans",
    "climate": "climate",
    "cover": "covers",
    "lock": "locks",
    "vacuum": "vacuums",
    "media_player": "media",
    "camera": "cameras",
    "binary_sensor": "binary_sensors",
    "sensor": "sensors",
    "number": "controls",
    "select": "controls",
    "button": "buttons",
    "scene": "scenes",
    "automation": "automations",
    "script": "scripts",
    "device_tracker": "presence",
    "person": "presence",
    "weather": "weather",
    "update": "updates",
    "alarm_control_panel": "security",
    "siren": "security",
}

# --- device_class -> label key ------------------------------------------
DEVICE_CLASS_LABELS: Final[dict[str, str]] = {
    "temperature": "temperature",
    "humidity": "humidity",
    "pressure": "pressure",
    "atmospheric_pressure": "pressure",
    "battery": "battery",
    "power": "energy",
    "energy": "energy",
    "current": "energy",
    "voltage": "energy",
    "gas": "energy",
    "water": "water",
    "illuminance": "light_level",
    "motion": "motion",
    "occupancy": "presence",
    "presence": "presence",
    "door": "openings",
    "window": "openings",
    "garage_door": "openings",
    "opening": "openings",
    "smoke": "security",
    "carbon_monoxide": "security",
    "gas_safety": "security",
    "moisture": "leak",
    "connectivity": "connectivity",
    "signal_strength": "connectivity",
    "pm25": "air_quality",
    "pm10": "air_quality",
    "carbon_dioxide": "air_quality",
    "aqi": "air_quality",
}

# --- entity_id keyword fallbacks ----------------------------------------
# Applied when nothing more specific matched; keyed by substring in entity_id.
KEYWORD_LABELS: Final[dict[str, str]] = {
    "battery": "battery",
    "_power": "energy",
    "_energy": "energy",
    "temperature": "temperature",
    "humidity": "humidity",
    "motion": "motion",
}


def resolve_language(language: str | None) -> str:
    """Return a supported language code, falling back to the default."""
    if language and language.split("-", 1)[0] in SUPPORTED_LANGUAGES:
        return language.split("-", 1)[0]
    return DEFAULT_LANGUAGE


def label_spec(key: str, language: str = DEFAULT_LANGUAGE) -> LabelSpec:
    """Resolve a label key into a localized :class:`LabelSpec`."""
    ld = LABELS[key]
    lang = resolve_language(language)
    name = ld["names"].get(lang) or ld["names"][DEFAULT_LANGUAGE]
    return {"name": name, "color": ld["color"], "icon": ld["icon"]}


def compute_label_specs(
    entry: EntityLike, options: LabelerOptions
) -> list[LabelSpec]:
    """Return the list of label specs that apply to a single entity.

    Pure function (no Home Assistant state) so the ruleset can be unit-tested
    in isolation.
    """
    keys: list[str] = []
    seen: set[str] = set()

    # Skip config/diagnostic helper entities; they only add noise.
    if options.skip_categories and getattr(entry, "entity_category", None):
        return []

    def add(key: str | None) -> None:
        if key and key not in seen:
            seen.add(key)
            keys.append(key)

    domain = entry.entity_id.split(".", 1)[0]

    if options.enable_domain:
        add(DOMAIN_LABELS.get(domain))

    if options.enable_device_class:
        device_class = entry.device_class or entry.original_device_class
        if device_class:
            add(DEVICE_CLASS_LABELS.get(device_class))

    # Keyword fallbacks only when nothing more specific matched.
    if not keys:
        entity_id = entry.entity_id.lower()
        for needle, key in KEYWORD_LABELS.items():
            if needle in entity_id:
                add(key)

    specs = [label_spec(k, options.language) for k in keys]

    if options.enable_integration and entry.platform:
        specs.append(
            {"name": entry.platform, "color": "grey", "icon": "mdi:puzzle"}
        )

    if options.label_prefix:
        specs = [{**s, "name": f"{options.label_prefix}{s['name']}"} for s in specs]

    return specs
