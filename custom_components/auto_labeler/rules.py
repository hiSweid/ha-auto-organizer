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
    enable_curated: bool = True
    enable_area: bool = False
    enable_floor: bool = False
    skip_categories: bool = True
    language: str = DEFAULT_LANGUAGE
    label_prefix: str = ""


# Area/floor labels use the user-defined names verbatim (not translatable),
# with a distinct color/icon so they stand out from functional labels.
AREA_LABEL_COLOR: Final = "blue-grey"
AREA_LABEL_ICON: Final = "mdi:texture-box"
FLOOR_LABEL_COLOR: Final = "brown"
FLOOR_LABEL_ICON: Final = "mdi:stairs"


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
    "battery": _ld("green", "mdi:battery", "Batterie", "Battery"),
    "energy": _ld("amber", "mdi:flash", "Energie", "Energy"),
    "water": _ld("light-blue", "mdi:water", "Wasser", "Water"),
    "light_level": _ld("yellow", "mdi:brightness-6", "Helligkeit", "Light Level"),
    "motion": _ld("red", "mdi:motion-sensor", "Bewegung", "Motion"),
    "openings": _ld("brown", "mdi:door", "Öffnungen", "Openings"),
    "leak": _ld("light-blue", "mdi:water-alert", "Leck", "Leak"),
    "air_quality": _ld("teal", "mdi:air-filter", "Luftqualität", "Air Quality"),
    "cost": _ld("green", "mdi:cash", "Kosten", "Cost"),
    "car": _ld("blue", "mdi:car-electric", "Auto", "Car"),
    # curated, integration-derived themes
    "appliances": _ld(
        "orange", "mdi:washing-machine", "Haushaltsgeräte", "Appliances"
    ),
    "garden": _ld("light-green", "mdi:flower", "Garten", "Garden"),
    "network": _ld(
        "blue-grey", "mdi:server-network", "Netzwerk & Server", "Network & Servers"
    ),
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
    "scene": "scenes",
    "automation": "automations",
    "script": "scripts",
    "device_tracker": "presence",
    "person": "presence",
    "weather": "weather",
    "sun": "weather",
    "update": "updates",
    "alarm_control_panel": "security",
    "siren": "security",
    "humidifier": "climate",
    "water_heater": "climate",
    "lawn_mower": "garden",
    "remote": "media",
    "valve": "openings",
}

# --- device_class -> label key ------------------------------------------
DEVICE_CLASS_LABELS: Final[dict[str, str]] = {
    "temperature": "temperature",
    "humidity": "humidity",
    "battery": "battery",
    "power": "energy",
    "energy": "energy",
    "current": "energy",
    "voltage": "energy",
    "gas": "energy",
    "apparent_power": "energy",
    "reactive_power": "energy",
    "power_factor": "energy",
    "frequency": "energy",
    "energy_storage": "energy",
    "energy_distance": "energy",
    "plug": "energy",
    "monetary": "cost",
    "water": "water",
    "volume_flow_rate": "water",
    "illuminance": "light_level",
    "light": "light_level",
    "cold": "climate",
    "heat": "climate",
    "update": "updates",
    "motion": "motion",
    "moving": "motion",
    "vibration": "motion",
    "occupancy": "presence",
    "presence": "presence",
    "door": "openings",
    "window": "openings",
    "garage_door": "openings",
    "opening": "openings",
    "lock": "locks",
    "smoke": "security",
    "carbon_monoxide": "security",
    "gas_safety": "security",
    "tamper": "security",
    "moisture": "leak",
    "battery_charging": "battery",
    "pm25": "air_quality",
    "pm10": "air_quality",
    "pm1": "air_quality",
    "carbon_dioxide": "air_quality",
    "nitrogen_dioxide": "air_quality",
    "nitrogen_monoxide": "air_quality",
    "ozone": "air_quality",
    "sulphur_dioxide": "air_quality",
    "volatile_organic_compounds": "air_quality",
    "volatile_organic_compounds_parts": "air_quality",
    "aqi": "air_quality",
    "precipitation": "weather",
    "precipitation_intensity": "weather",
    "wind_speed": "weather",
    "wind_direction": "weather",
    "uv_index": "weather",
    "irradiance": "weather",
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
    "wallbox": "car",
}

# --- integration (platform) -> curated theme label ----------------------
# Thematic labels that cannot be derived from domain/device_class, mapped
# from the source integration. These apply even to diagnostic/config
# entities (they are explicitly curated, so noise is not a concern).
INTEGRATION_LABELS: Final[dict[str, str]] = {
    # household appliances
    "homeconnect": "appliances",
    "homeconnect_ws": "appliances",
    "ha_washdata": "appliances",
    "miele": "appliances",
    # garden / outdoor
    "navimow": "garden",
    "gardena": "garden",
    "gardena_bluetooth": "garden",
    "rainbird": "garden",
    "opensprinkler": "garden",
    # network & servers
    "proxmoxve": "network",
    "fritz": "network",
    "fritzbox_callmonitor": "network",
    "unifi": "network",
    "openwrt": "network",
    "speedtestdotnet": "network",
    # car / charging
    "evcc_intg": "car",
    "wallbox": "car",
    "easee": "car",
    "zaptec": "car",
    "openevse": "car",
}


def resolve_language(language: str | None) -> str:
    """Return a supported language code, falling back to the default."""
    if language and language.split("-", 1)[0] in SUPPORTED_LANGUAGES:
        return language.split("-", 1)[0]
    return DEFAULT_LANGUAGE


def area_floor_specs(
    area_name: str | None, floor_name: str | None, options: LabelerOptions
) -> list[LabelSpec]:
    """Build label specs for an entity's area and/or floor.

    Pure helper: the caller resolves the names from the registries and passes
    them in, so this stays unit-testable without Home Assistant.
    """
    specs: list[LabelSpec] = []
    if options.enable_area and area_name:
        specs.append(
            {"name": area_name, "color": AREA_LABEL_COLOR, "icon": AREA_LABEL_ICON}
        )
    if options.enable_floor and floor_name:
        specs.append(
            {
                "name": floor_name,
                "color": FLOOR_LABEL_COLOR,
                "icon": FLOOR_LABEL_ICON,
            }
        )
    return specs


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

    def add(key: str | None) -> None:
        if key and key not in seen:
            seen.add(key)
            keys.append(key)

    platform = getattr(entry, "platform", None)
    is_category = bool(
        options.skip_categories and getattr(entry, "entity_category", None)
    )

    # Curated integration themes apply even to diagnostic/config entities.
    if options.enable_curated and platform:
        add(INTEGRATION_LABELS.get(platform))

    # Domain/device_class labels are skipped for config/diagnostic helpers.
    if not is_category:
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

    if options.enable_integration and not is_category and platform:
        specs.append(
            {"name": platform, "color": "grey", "icon": "mdi:puzzle"}
        )

    if options.label_prefix:
        specs = [{**s, "name": f"{options.label_prefix}{s['name']}"} for s in specs]

    return specs
