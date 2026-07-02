"""Rule definitions for the Auto-Organizer integration.

The ruleset is intentionally pure data so it can be extended, unit-tested and
later made configurable without touching the engine in ``organizer.py``.

Labels are referenced by a stable *key* (e.g. ``"lights"``).  A key maps to a
color, an ``mdi:`` icon and a per-language display name.  Only German (``de``)
and English (``en``) are supported for now; German is the default.
"""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass, field
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
class OrganizerOptions:
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
    max_labels: int = 2
    exclude: tuple[str, ...] = field(default_factory=tuple)
    custom_rules: dict[str, str] = field(default_factory=dict)
    # Restrict which label *themes* may be assigned at all (by catalog key,
    # e.g. "lights", "waste"). Empty = no restriction, every label allowed.
    enabled_labels: frozenset[str] = field(default_factory=frozenset)
    # When set, also apply a more specific icon (see SPECIFIC_ICONS) to
    # entities that already got a label from this run. Never overwrites an
    # icon the user picked manually.
    set_entity_icons: bool = False


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
    "energy": _ld("lime", "mdi:flash", "Energie", "Energy"),
    "water": _ld("light-blue", "mdi:water", "Wasser", "Water"),
    "light_level": _ld("yellow", "mdi:brightness-6", "Helligkeit", "Light Level"),
    "motion": _ld("red", "mdi:motion-sensor", "Bewegung", "Motion"),
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
    "waste": _ld("green", "mdi:trash-can", "Abfall", "Waste"),
    "shopping": _ld("deep-purple", "mdi:cart-heart", "Einkauf", "Shopping"),
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
    "valve": "covers",
    "air_quality": "air_quality",
    "assist_satellite": "media",
    "stt": "media",
    "tts": "media",
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
    "volume": "water",
    "ph": "water",
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
    "door": "security",
    "window": "security",
    "garage_door": "security",
    "opening": "security",
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

# --- specific entity icons ------------------------------------------------
# Keyed by the same "reason" that also picked a label (a domain, device_class,
# integration platform, or keyword — after stripping the whole-word padding
# spaces some keywords use). Only entries that are meaningfully more precise
# than the label's own icon are listed here; everything else falls back to
# the label icon (or no override at all).
SPECIFIC_ICONS: Final[dict[str, str]] = {
    # appliances — coffee
    "kaffeemaschine": "mdi:coffee-maker",
    "coffee maker": "mdi:coffee-maker",
    "kaffee": "mdi:coffee-maker",
    "espressomaschine": "mdi:coffee-maker",
    "kaffeevollautomat": "mdi:coffee-maker",
    "coffee machine": "mdi:coffee-maker",
    "espresso machine": "mdi:coffee-maker",
    # appliances — dryer
    "trockner": "mdi:tumble-dryer",
    "dryer": "mdi:tumble-dryer",
    # appliances — dishwasher
    "geschirrspuel": "mdi:dishwasher",
    "spuelmaschine": "mdi:dishwasher",
    "dishwasher": "mdi:dishwasher",
    # appliances — oven / stove
    "backofen": "mdi:stove",
    "oven": "mdi:stove",
    "ofen": "mdi:stove",
    "herd": "mdi:stove",
    "cooktop": "mdi:stove",
    # appliances — fridge / freezer
    "kuehlschrank": "mdi:fridge-outline",
    "fridge": "mdi:fridge-outline",
    "refrigerator": "mdi:fridge-outline",
    "gefrier": "mdi:fridge-outline",
    "freezer": "mdi:fridge-outline",
    "tiefkuehler": "mdi:fridge-outline",
    "tiefkuehltruhe": "mdi:fridge-outline",
    # appliances — kettle
    "kettle": "mdi:kettle",
    "wasserkocher": "mdi:kettle",
    # appliances — microwave / toaster
    "mikrowelle": "mdi:microwave",
    "microwave": "mdi:microwave",
    "toaster": "mdi:toaster-oven",
    # media — TV
    "tv": "mdi:television",
    "fernseher": "mdi:television",
    "television": "mdi:television",
    # media — speakers
    "lautsprecher": "mdi:speaker",
    "sonos": "mdi:speaker",
    "speaker": "mdi:speaker",
    "soundbar": "mdi:soundbar",
    # media — misc
    "projector": "mdi:projector",
    "amplifier": "mdi:amplifier",
    "tastatur": "mdi:keyboard",
    "keyboard": "mdi:keyboard",
    "spotify": "mdi:spotify",
    # lights
    "lichterkette": "mdi:string-lights",
    "chandelier": "mdi:chandelier",
    "led strip": "mdi:led-strip-variant",
    "ceiling lamp": "mdi:ceiling-light",
    "deckenleuchte": "mdi:ceiling-light",
    "floor lamp": "mdi:floor-lamp",
    "stehlampe": "mdi:floor-lamp",
    "table lamp": "mdi:desk-lamp",
    "tischlampe": "mdi:desk-lamp",
    "wandleuchte": "mdi:wall-sconce",
    "wall light": "mdi:wall-sconce",
    # locks
    "schloss": "mdi:lock",
    "tuerschloss": "mdi:lock",
    "deadbolt": "mdi:lock",
    "vorhangschloss": "mdi:lock",
    "smartlock": "mdi:lock",
    "nuki": "mdi:lock",
    # cameras
    "video doorbell": "mdi:doorbell-video",
    "ring doorbell": "mdi:doorbell-video",
    "webcam": "mdi:webcam",
    "nvr": "mdi:cctv",
    # car / charging
    "wallbox": "mdi:ev-station",
    "ladestation": "mdi:ev-station",
    "charging station": "mdi:ev-station",
    "chargepoint": "mdi:ev-station",
    "charge point": "mdi:ev-station",
    "ladepunkt": "mdi:ev-station",
    "ev charger": "mdi:ev-station",
    # garden — mowing
    "mower": "mdi:robot-mower",
    "maehroboter": "mdi:robot-mower",
    "rasenmaeher": "mdi:robot-mower",
    "rasenroboter": "mdi:robot-mower",
    # garden — watering
    "sprinkler": "mdi:sprinkler",
    "rasensprenger": "mdi:sprinkler",
    "sprinkleranlage": "mdi:sprinkler",
    "bewaesser": "mdi:water-pump",
    "irrigation": "mdi:water-pump",
    "garden hose": "mdi:water-pump",
    "tropfbewaesserung": "mdi:water-pump",
    # network
    "router": "mdi:router-wireless",
    "fritzbox": "mdi:router-wireless",
    "access point": "mdi:access-point",
    # climate — heating
    "heizkoerper": "mdi:radiator",
    "radiator": "mdi:radiator",
    # weather
    "sunrise": "mdi:weather-sunset-up",
    "sonnenaufgang": "mdi:weather-sunset-up",
    "sunset": "mdi:weather-sunset-down",
    "sonnenuntergang": "mdi:weather-sunset-down",
    "rainfall": "mdi:weather-pouring",
    "regenmenge": "mdi:weather-pouring",
    "wind gust": "mdi:weather-windy",
    "windboe": "mdi:weather-windy",
    # security — smoke / fire
    "rauchmelder": "mdi:smoke-detector",
    "smoke detector": "mdi:smoke-detector",
    "feuermelder": "mdi:smoke-detector",
    "fire alarm": "mdi:smoke-detector",
    # security — openings
    "fenster": "mdi:window-closed-variant",
    "window sensor": "mdi:window-closed-variant",
    "window contact": "mdi:window-closed-variant",
    "garagentor": "mdi:garage",
    "garage door": "mdi:garage",
    # covers
    "jalousie": "mdi:blinds",
    "blinds": "mdi:blinds",
    "rollos": "mdi:blinds",
    "venetian blinds": "mdi:blinds",
    # fans
    "range hood": "mdi:air-filter",
    "exhaust fan": "mdi:air-filter",
    "dunstabzugshaube": "mdi:air-filter",
    # presence — mobile devices
    "iphone": "mdi:cellphone-iphone",
    "ipad": "mdi:tablet-ipad",
    "tablet": "mdi:tablet",
    "android": "mdi:cellphone-android",
    "smartphone": "mdi:cellphone",
    "handy": "mdi:cellphone",
    "kiosk": "mdi:tablet",
    "bettsensor": "mdi:bed",
    # energy — solar / storage
    "solar": "mdi:solar-power",
    "photovolt": "mdi:solar-power",
    "pv": "mdi:solar-power",
    "stromspeicher": "mdi:home-battery",
    "batteriespeicher": "mdi:home-battery",
    "marstek": "mdi:home-battery",
    # appliances — misc
    "drucker": "mdi:printer",
    "printer": "mdi:printer",
    "luftreiniger": "mdi:air-purifier",
    # climate — humidity control
    "luftbefeuchter": "mdi:air-humidifier",
    # fans — ceiling
    "deckenventilator": "mdi:ceiling-fan",
    # water — aquarium
    "aquarium": "mdi:fishbowl",
    # air quality
    "co2": "mdi:molecule-co2",
    # weather — extra
    "frost": "mdi:snowflake",
    "pollen": "mdi:flower-pollen",
    # waste — subtypes
    "gelbersack": "mdi:recycle",
    "recycling": "mdi:recycle",
    "altpapier": "mdi:recycle",
    "biomuell": "mdi:leaf",
    # security — front/balcony/patio doors
    "eingangstuer": "mdi:door",
    "eingangstur": "mdi:door",
    "haustuer": "mdi:door",
    "haustur": "mdi:door",
    "wohnungstuer": "mdi:door",
    "wohnungstur": "mdi:door",
    "balkontuer": "mdi:door-sliding",
    "balkontur": "mdi:door-sliding",
    "terrassentuer": "mdi:door-sliding",
    "terrassentur": "mdi:door-sliding",
    # security — plain (non-video) doorbell / CO detector
    "klingel": "mdi:doorbell",
    "tuerklingel": "mdi:doorbell",
    "doorbell": "mdi:doorbell",
    "kohlenmonoxid": "mdi:molecule-co",
    "carbon monoxide detector": "mdi:molecule-co",
    # covers — curtains
    "vorhang": "mdi:curtains",
    "curtain": "mdi:curtains",
    "curtains": "mdi:curtains",
    # appliances — pets / pool / misc
    "futterautomat": "mdi:paw",
    "pet feeder": "mdi:paw",
    "katzenklo": "mdi:paw",
    "litter box": "mdi:paw",
    "whirlpool": "mdi:hot-tub",
    "kuechenwaage": "mdi:scale-balance",
    # water — pool
    "swimming pool": "mdi:pool",
    # network — NAS
    "synology": "mdi:nas",
    # weather — wind direction
    "windrichtung": "mdi:compass",
    # presence — group
    "family": "mdi:account-group",
    # closing the remaining label categories that had zero icon
    # differentiation — one word each, so every label theme can produce a
    # specific icon, not just the label's own generic one.
    # automations / scenes / scripts
    "zeitgesteuert": "mdi:calendar-clock",
    "scheduled": "mdi:calendar-clock",
    "szene": "mdi:palette-swatch",
    "skript": "mdi:script-text-outline",
    # battery
    "battery_charging": "mdi:battery-charging",
    # cost
    "abrechnung": "mdi:receipt",
    "billing": "mdi:receipt",
    "ersparnis": "mdi:piggy-bank",
    "savings": "mdi:piggy-bank",
    # humidity — dew point
    "taupunkt": "mdi:thermometer-water",
    "dew point": "mdi:thermometer-water",
    # leak — sensor devices specifically
    "wassermelder": "mdi:water-alert-outline",
    "shelly flood": "mdi:water-alert-outline",
    # light level — lux unit
    "lux": "mdi:brightness-7",
    # motion — vibration sensors
    "vibration": "mdi:vibrate",
    # shopping — groceries
    "lebensmittel": "mdi:basket",
    "grocery": "mdi:basket",
    # switches — outlets / plugs
    "steckdose": "mdi:power-plug",
    "steckdosenleiste": "mdi:power-plug",
    "outlet": "mdi:power-plug",
    "smart plug": "mdi:power-plug",
    # temperature (completeness — same as the label's own icon)
    "temperature": "mdi:thermometer",
    # updates — firmware specifically
    "firmware": "mdi:chip",
    # vacuums — mop robots
    "wischroboter": "mdi:robot-vacuum-variant",
    # --- domain-level fallback -------------------------------------------
    # Keyed by the bare HA domain (exact dict lookup in suggest_entity_icon,
    # not a substring scan — zero collision risk regardless of the string).
    # Guarantees every entity gets an icon suggestion even when its name has
    # no recognizable keyword, not just entities with a "specific" name.
    # Some reuse the label's own icon; others are genuinely more precise
    # than the label icon for that exact domain.
    "air_quality": "mdi:air-filter",
    "alarm_control_panel": "mdi:shield-home",
    "assist_satellite": "mdi:account-voice",
    "automation": "mdi:robot",
    "camera": "mdi:cctv",
    "climate": "mdi:thermostat",
    "cover": "mdi:window-shutter",
    "device_tracker": "mdi:crosshairs-gps",
    "fan": "mdi:fan",
    "humidifier": "mdi:air-humidifier",
    "light": "mdi:lightbulb-group",
    "lock": "mdi:lock",
    "media_player": "mdi:cast",
    "person": "mdi:account",
    "remote": "mdi:remote",
    "scene": "mdi:palette",
    "script": "mdi:script-text",
    "siren": "mdi:alarm-light",
    "stt": "mdi:microphone-message",
    "sun": "mdi:weather-sunny",
    "switch": "mdi:toggle-switch",
    "tts": "mdi:volume-high",
    "update": "mdi:package-up",
    "vacuum": "mdi:robot-vacuum",
    "valve": "mdi:valve",
    "water_heater": "mdi:water-boiler",
    "weather": "mdi:weather-partly-cloudy",
}

# --- keyword fallbacks --------------------------------------------------
# Applied only when nothing more specific matched. Substrings are tested
# against the normalized (lowercased, de-umlauted) entity_id AND friendly
# name, so e.g. "wasser" matches "Wasserzähler". Keep substrings >= 4 chars
# and distinctive to avoid false positives. All map to EXISTING labels.
KEYWORD_LABELS: Final[dict[str, str]] = {
    # energy
    "strom": "energy",
    "leistung": "energy",
    "energie": "energy",
    "energy": "energy",
    "power": "energy",
    "watt": "energy",
    "kwh": "energy",
    "einspeis": "energy",
    "netzbezug": "energy",
    "photovolt": "energy",
    "solar": "energy",
    "wechselrichter": "energy",
    "ac verbrauch": "energy",
    "verbraucher": "energy",
    "inverter": "energy",
    "consumption": "energy",
    "self consumption": "energy",
    "feed in": "energy",
    "amperage": "energy",
    # water
    "wasser": "water",
    "water": "water",
    "fluessig": "water",
    "liquid": "water",
    "nass": "water",
    "durchfluss": "water",
    "wasserstand": "water",
    "aquarium": "water",
    "swimming pool": "water",
    "water level": "water",
    "flow rate": "water",
    # leak
    "wasserleck": "leak",
    "leckage": "leak",
    "wassermelder": "leak",
    "shelly flood": "leak",
    "water leak": "leak",
    "water overflow": "leak",
    # temperature
    "temperature": "temperature",
    "temperatur": "temperature",
    "thermometer": "temperature",
    " temp ": "temperature",
    # humidity
    "humidity": "humidity",
    "feucht": "humidity",
    "luftfeucht": "humidity",
    "taupunkt": "humidity",
    "dew point": "humidity",
    " damp ": "humidity",
    # battery
    "battery": "battery",
    "batterie": "battery",
    "akku": "battery",
    "ladestand": "battery",
    "ladezustand": "battery",
    "charge level": "battery",
    "low battery": "battery",
    # motion / presence
    "motion": "motion",
    "bewegung": "motion",
    "bewegungsmelder": "motion",
    "movement": "motion",
    " pir ": "motion",
    "praesenz": "presence",
    "bettsensor": "presence",
    "kiosk": "presence",
    "screensaver": "presence",
    "android": "presence",
    "tablet": "presence",
    "occupied": "presence",
    # light level
    "helligkeit": "light_level",
    "illuminance": "light_level",
    "beleuchtungsstaerke": "light_level",
    " lux ": "light_level",
    # weather
    "wetter": "weather",
    "weather": "weather",
    "niederschlag": "weather",
    "regenmenge": "weather",
    "windgeschw": "weather",
    "windspeed": "weather",
    "sturm": "weather",
    "unwetter": "weather",
    "frost": "weather",
    "pollen": "weather",
    "sonnenaufgang": "weather",
    "sonnenuntergang": "weather",
    "sunrise": "weather",
    "sunset": "weather",
    "rainfall": "weather",
    "wind gust": "weather",
    # security
    "rauchmelder": "security",
    "alarm": "security",
    "einbruch": "security",
    "tuerkontakt": "security",
    "fensterkontakt": "security",
    "eingangstuer": "security",
    "eingangstur": "security",
    "haustuer": "security",
    "haustur": "security",
    "wohnungstuer": "security",
    "wohnungstur": "security",
    "balkontuer": "security",
    "balkontur": "security",
    "terrassentuer": "security",
    "terrassentur": "security",
    "door sensor": "security",
    "window sensor": "security",
    "intrusion": "security",
    "smoke detector": "security",
    "glass break": "security",
    # car / charging
    "wallbox": "car",
    "ladestation": "car",
    "egolf": "car",
    "tesla": "car",
    "ioniq": "car",
    "enyaq": "car",
    "evcc": "car",
    "niro": "car",
    "ariya": "car",
    "e tron": "car",
    "outlander": "car",
    "ev charging": "car",
    "chargepoint": "car",
    "charge point": "car",
    "charging station": "car",
    " phev ": "car",
    "plug in hybrid": "car",
    "ladepunkt": "car",
    "ev charger": "car",
    # media
    "fernseher": "media",
    "lautsprecher": "media",
    "sonos": "media",
    "soundbar": "media",
    "mediaplayer": "media",
    "receiver": "media",
    "speaker": "media",
    "amplifier": "media",
    "projector": "media",
    # appliances
    "waschmaschine": "appliances",
    "trockner": "appliances",
    "geschirrspuel": "appliances",
    "spuelmaschine": "appliances",
    "kaffeemaschine": "appliances",
    "backofen": "appliances",
    "kuehlschrank": "appliances",
    "gefrier": "appliances",
    "dishwasher": "appliances",
    "washer": "appliances",
    "dryer": "appliances",
    " oven ": "appliances",
    "fridge": "appliances",
    "refrigerator": "appliances",
    "freezer": "appliances",
    "coffee maker": "appliances",
    "kettle": "appliances",
    "mikrowelle": "appliances",
    "microwave": "appliances",
    "toaster": "appliances",
    "kaffee": "appliances",
    "espressomaschine": "appliances",
    "kaffeevollautomat": "appliances",
    "coffee machine": "appliances",
    "espresso machine": "appliances",
    " ofen ": "appliances",
    " herd ": "appliances",
    "cooktop": "appliances",
    "tiefkuehler": "appliances",
    "tiefkuehltruhe": "appliances",
    "wasserkocher": "appliances",
    "drucker": "appliances",
    "printer": "appliances",
    "luftreiniger": "appliances",
    "futterautomat": "appliances",
    "pet feeder": "appliances",
    "katzenklo": "appliances",
    "litter box": "appliances",
    "whirlpool": "appliances",
    "kuechenwaage": "appliances",
    # garden
    "garten": "garden",
    "maehroboter": "garden",
    "rasenmaeher": "garden",
    "bewaesser": "garden",
    "irrigation": "garden",
    "rasen": "garden",
    "giessen": "garden",
    "mower": "garden",
    "sprinkler": "garden",
    " blumen ": "garden",
    "pflanzen": "garden",
    "garden hose": "garden",
    "rasenroboter": "garden",
    "rasensprenger": "garden",
    "sprinkleranlage": "garden",
    "tropfbewaesserung": "garden",
    # network
    "fritzbox": "network",
    "proxmox": "network",
    "router": "network",
    "netzwerk": "network",
    "speedtest": "network",
    "unifi": "network",
    "wireguard": "network",
    "pihole": "network",
    "modem": "network",
    "access point": "network",
    "synology": "network",
    # climate / heating
    "klima": "climate",
    "heizung": "climate",
    "heizkoerper": "climate",
    "radiator": "climate",
    "luftbefeuchter": "climate",
    "thermostat": "climate",
    "klimaanlage": "climate",
    "heizoel": "climate",
    "heizol": "climate",
    "olverbrauch": "climate",
    "oelverbrauch": "climate",
    "fussbodenheiz": "climate",
    "ble temp": "climate",
    "hvac": "climate",
    "heat pump": "climate",
    "furnace": "climate",
    "boiler": "climate",
    "air conditioner": "climate",
    # cost
    "kosten": "cost",
    "tarif": "cost",
    "ersparnis": "cost",
    "erloes": "cost",
    "strompreis": "cost",
    "oelpreis": "cost",
    "olpreis": "cost",
    "tariff": "cost",
    "electricity price": "cost",
    "energy price": "cost",
    "savings": "cost",
    "revenue": "cost",
    "gebuehr": "cost",
    "abrechnung": "cost",
    "billing": "cost",
    "price": "cost",
    # covers
    "rolllad": "covers",
    "rollladen": "covers",
    "jalousie": "covers",
    "markise": "covers",
    "beschattung": "covers",
    "shutters": "covers",
    "blinds": "covers",
    "awning": "covers",
    "rollos": "covers",
    "venetian blinds": "covers",
    "vorhang": "covers",
    "curtain": "covers",
    "curtains": "covers",
    # locks
    "tuerschloss": "locks",
    "schliessanlage": "locks",
    "deadbolt": "locks",
    "door lock": "locks",
    "schloss": "locks",
    "verriegelt": "locks",
    "verriegelung": "locks",
    "tuerriegel": "locks",
    "vorhangschloss": "locks",
    " smartlock ": "locks",
    "nuki": "locks",
    # switches / outlets
    "steckdose": "switches",
    "steckdosenleiste": "switches",
    "schalter": "switches",
    "outlet": "switches",
    " socket ": "switches",
    "smart plug": "switches",
    " tv ": "media",
    "television": "media",
    # fans
    "luefter": "fans",
    "ventilator": "fans",
    "abluft": "fans",
    "lueftung": "fans",
    "exhaust fan": "fans",
    "range hood": "fans",
    "dunstabzugshaube": "fans",
    "deckenventilator": "fans",
    "geblaese": "fans",
    "blower": "fans",
    "ceiling fan": "fans",
    " fan ": "fans",
    # updates
    "firmware": "updates",
    "aktualisierung": "updates",
    "software update": "updates",
    "new version": "updates",
    # energy (PV / grid / storage / electrical quantities)
    "pv": "energy",
    "grid": "energy",
    "einspeisung": "energy",
    "eigenverbrauch": "energy",
    "autarkie": "energy",
    "spannung": "energy",
    "frequenz": "energy",
    "wirkleistung": "energy",
    "blindleistung": "energy",
    "stromspeicher": "energy",
    "batteriespeicher": "energy",
    "marstek": "energy",
    # weather
    "uv": "weather",
    "windrichtung": "weather",
    "sonnenstunden": "weather",
    "luftdruck": "weather",
    # presence (personal devices / occupancy)
    "iphone": "presence",
    "ipad": "presence",
    "macbook": "presence",
    "airpods": "presence",
    "smartphone": "presence",
    "handy": "presence",
    "occupancy": "presence",
    "belegung": "presence",
    "anwesenheit": "presence",
    "location": "presence",
    "zuhause": "presence",
    # network
    "ssid": "network",
    # cameras (Reolink models often arrive via MQTT)
    "reolink": "cameras",
    "kamera": "cameras",
    "camera": "cameras",
    "ueberwachungskamera": "cameras",
    "webcam": "cameras",
    "cctv": "cameras",
    " nvr ": "cameras",
    "video doorbell": "cameras",
    "ring doorbell": "cameras",
    # vacuums
    "staubsauger": "vacuums",
    "saugroboter": "vacuums",
    "wischroboter": "vacuums",
    "vacuum": "vacuums",
    "robot vacuum": "vacuums",
    "roomba": "vacuums",
    "roborock": "vacuums",
    "irobot": "vacuums",
    # waste / recycling
    "abfall": "waste",
    " muell ": "waste",
    "muelltonne": "waste",
    "restmuell": "waste",
    "biomuell": "waste",
    "gelbersack": "waste",
    "altpapier": "waste",
    "wertstoff": "waste",
    "entsorgung": "waste",
    "trash": "waste",
    "garbage": "waste",
    "recycling": "waste",
    "waste bin": "waste",
    # shopping
    "einkaufsliste": "shopping",
    "einkauf": "shopping",
    "lebensmittel": "shopping",
    "grocery": "shopping",
    "shopping list": "shopping",
    # media
    "wiedergabeliste": "media",
    "playlist": "media",
    # light level
    "brightness": "light_level",
    # presence
    "family": "presence",
    # energy (consumption / feed-in / demand telemetry)
    "verbraucht": "energy",
    "eingespeist": "energy",
    "bedarf": "energy",
    "leistungsaufnahme": "energy",
    # weather (Ecowitt station, gusts)
    "ecowitt": "weather",
    "boen": "weather",
    "windboe": "weather",
    "regenrate": "weather",
    # security (doors / windows / openings by name)
    "fenster": "security",
    "tuer": "security",
    "garagentor": "security",
    "oeffnung": "security",
    "offnung": "security",
    "klingel": "security",
    "tuerklingel": "security",
    "doorbell": "security",
    "feuermelder": "security",
    "fire alarm": "security",
    "window contact": "security",
    "garage door": "security",
    "kohlenmonoxid": "security",
    "carbon monoxide detector": "security",
    # automations / scenes / scripts (mostly domain-matched; these extend
    # the fallback so template/helper entities describing one by name
    # still get labeled and can pick a specific icon)
    "zeitgesteuert": "automations",
    "scheduled": "automations",
    " szene ": "scenes",
    " skript ": "scripts",
    # lights
    "lichterkette": "lights",
    "lampe": "lights",
    "gluehbirne": "lights",
    "leuchte": "lights",
    "deckenleuchte": "lights",
    "stehlampe": "lights",
    "tischlampe": "lights",
    "wandleuchte": "lights",
    "pendelleuchte": "lights",
    "nachtlicht": "lights",
    "led streifen": "lights",
    " licht ": "lights",
    " spot ": "lights",
    " strahler ": "lights",
    "lamp": "lights",
    "bulb": "lights",
    "spotlight": "lights",
    "downlight": "lights",
    "nightlight": "lights",
    "flashlight": "lights",
    "chandelier": "lights",
    "sconce": "lights",
    "floor lamp": "lights",
    "table lamp": "lights",
    "ceiling lamp": "lights",
    "wall light": "lights",
    "pendant light": "lights",
    "led strip": "lights",
    # media (TV remotes / keyboards)
    "tastatur": "media",
    "keyboard": "media",
    # air quality
    "voc": "air_quality",
    "luftqualitaet": "air_quality",
    "luftguete": "air_quality",
    "feinstaub": "air_quality",
    "co2": "air_quality",
    "particulate": "air_quality",
    # climate (AC telemetry)
    "fanfreq": "climate",
    "klimaanlage": "climate",
}

# Known vehicle/model names; matched as whole words in entity_id/name and
# always labeled "car" (even when a device_class also applies).
CAR_NAME_KEYWORDS: Final[tuple[str, ...]] = (
    "egolf", "golf", "tesla", "zoe", "leaf", "kona", "ioniq",
    "enyaq", "polestar", "cupra",
)

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
    "rachio": "garden",
    "husqvarna_automower": "garden",
    "hunter_hydrawise": "garden",
    # network & servers
    "proxmoxve": "network",
    "fritz": "network",
    "fritzbox_callmonitor": "network",
    "unifi": "network",
    "openwrt": "network",
    "speedtestdotnet": "network",
    "asuswrt": "network",
    "netgear": "network",
    "adguard": "network",
    "uptimerobot": "network",
    "synology_dsm": "network",
    "nmap_tracker": "presence",
    # car / charging
    "evcc_intg": "car",
    "wallbox": "car",
    "easee": "car",
    "zaptec": "car",
    "openevse": "car",
    "ohme": "car",
    "myenergi": "car",
    "tesla_wall_connector": "car",
    "teslemetry": "car",
    "bmw_connected_drive": "car",
    "mercedesme": "car",
    "kia_uvo": "car",
    "hyundai_kia_connect": "car",
    "renault": "car",
    "volvooncall": "car",
    "smartcar": "car",
    # heating oil
    "oilfox": "climate",
    # climate / HVAC brands
    "melcloud": "climate",
    "toshiba_ac": "climate",
    "midea_ac": "climate",
    "tado": "climate",
    "ecobee": "climate",
    "sensibo": "climate",
    "nibe_heatpump": "climate",
    "opentherm_gw": "climate",
    # home battery storage (Marstek Venus via Modbus) -> energy
    "marstek_modbus": "energy",
    # solar / inverters
    "solaredge": "energy",
    "fronius": "energy",
    "growatt_server": "energy",
    "victron_remote_monitoring": "energy",
    "huawei_solar": "energy",
    "solax": "energy",
    "goodwe": "energy",
    "enphase_envoy": "energy",
    "solarlog": "energy",
    # dynamic electricity tariffs
    "tibber": "cost",
    "awattar": "cost",
    "energyzero": "cost",
    "nordpool": "cost",
    "octopus_energy": "cost",
    # cameras / NVR
    "reolink": "cameras",
    "frigate": "cameras",
    "ring": "cameras",
    "unifiprotect": "cameras",
    "amcrest": "cameras",
    "eufy_security": "cameras",
    "arlo": "cameras",
    # security / alarm systems
    "abode": "security",
    "verisure": "security",
    "simplisafe": "security",
    "envisalink": "security",
    "konnected": "security",
    # locks
    "august": "locks",
    "schlage": "locks",
    "nuki": "locks",
    # presence tracking
    "life360": "presence",
    "owntracks": "presence",
    "gpslogger": "presence",
    "icloud": "presence",
    "fully_kiosk": "presence",
    # lights
    "wled": "lights",
    # media
    "spotify": "media",
    "cast": "media",
    "apple_tv": "media",
    "webostv": "media",
    "samsungtv": "media",
    "androidtv": "media",
    "denonavr": "media",
    "yamaha_musiccast": "media",
    "heos": "media",
    "roon": "media",
    "volumio": "media",
    "squeezebox": "media",
    "bluesound": "media",
    # air quality
    "airvisual": "air_quality",
    "airly": "air_quality",
    "purpleair": "air_quality",
    # weather
    "dwd_weather": "weather",
    "met": "weather",
    "accuweather": "weather",
    "openweathermap": "weather",
    "pirateweather": "weather",
    "tomorrowio": "weather",
    "buienradar": "weather",
    "weatherflow_cloud": "weather",
    "ambient_station": "weather",
    # updates
    "hacs": "updates",
    # HA system / add-ons / infrastructure -> network & servers
    "hassio": "network",
    "backup": "network",
    "systemmonitor": "network",
    # waste / recycling collection calendars
    "waste_collection_schedule": "waste",
    # food-saving / shopping
    "tgtg": "shopping",
}


def resolve_language(language: str | None) -> str:
    """Return a supported language code, falling back to the default."""
    if language and language.split("-", 1)[0] in SUPPORTED_LANGUAGES:
        return language.split("-", 1)[0]
    return DEFAULT_LANGUAGE


def _normalize(text: str) -> str:
    """Lowercase, de-umlaut and reduce to space-separated alphanumeric tokens."""
    text = text.lower()
    for src, dst in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.replace(src, dst)
    return f" {re.sub(r'[^a-z0-9]+', ' ', text).strip()} "


def match_area(
    entity_id: str,
    name: str | None,
    areas: list[dict],
) -> str | None:
    """Guess an entity's area from its id/name by matching area names/aliases.

    ``areas`` is a list of ``{"area_id", "name", "aliases"}`` dicts. A candidate
    matches when its normalized name appears as a whole word in the entity's
    id/name. The longest match wins; ties between different areas are treated as
    ambiguous and return ``None`` (pure function, unit-testable).
    """
    hay = _normalize(f"{entity_id} {name or ''}")
    matches: list[tuple[int, str]] = []
    for area in areas:
        for cand in [area.get("name", "")] + list(area.get("aliases") or []):
            nc = _normalize(cand).strip()
            if nc and f" {nc} " in hay:
                matches.append((len(nc), area["area_id"]))
                break
    if not matches:
        return None
    longest = max(length for length, _ in matches)
    top = {area_id for length, area_id in matches if length == longest}
    return next(iter(top)) if len(top) == 1 else None


def area_floor_specs(
    area_name: str | None, floor_name: str | None, options: OrganizerOptions
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


def label_differs(color: str | None, icon: str | None, spec: LabelSpec) -> bool:
    """Return True if an existing label's color/icon no longer match the rule."""
    return color != spec["color"] or icon != spec["icon"]


def is_excluded(entity_id: str, patterns: tuple[str, ...] | list[str]) -> bool:
    """Return True if the entity matches any exclude pattern.

    A pattern matches when it equals the domain (e.g. ``sensor``), equals the
    full ``entity_id``, or matches it as an fnmatch glob (e.g. ``sensor.test_*``).
    """
    if not patterns:
        return False
    domain = entity_id.split(".", 1)[0]
    for pattern in patterns:
        pattern = pattern.strip()
        if not pattern:
            continue
        if pattern in (domain, entity_id) or fnmatch.fnmatchcase(entity_id, pattern):
            return True
    return False


def parse_custom_rules(text: str | None) -> dict[str, str]:
    """Parse user rules ``keyword=label_key`` (per line or comma separated).

    Keywords are normalized; only label keys that exist in :data:`LABELS` are
    kept (unknown ones are ignored).
    """
    result: dict[str, str] = {}
    if not text:
        return result
    for item in str(text).replace("\n", ",").split(","):
        if "=" not in item:
            continue
        raw_kw, _, label = item.partition("=")
        keyword = _normalize(raw_kw).strip()
        label = label.strip()
        if keyword and label in LABELS:
            result[keyword] = label
    return result


def invalid_custom_rule_labels(text: str | None) -> list[str]:
    """Return label keys referenced in custom rules that don't exist."""
    invalid: list[str] = []
    if not text:
        return invalid
    for item in str(text).replace("\n", ",").split(","):
        if "=" not in item:
            continue
        _, _, label = item.partition("=")
        label = label.strip()
        if label and label not in LABELS and label not in invalid:
            invalid.append(label)
    return invalid


def affected_count(last_run: dict | None) -> int:
    """Total entities changed in a run summary (labels/areas/cleanup/remove_all)."""
    if not last_run:
        return 0
    total = 0
    for section, key in (
        ("labels", "updated"),
        ("areas", "assigned"),
        ("cleanup", "updated"),
        ("remove_all", "updated"),
    ):
        section_data = last_run.get(section)
        if isinstance(section_data, dict):
            total += int(section_data.get(key, 0))
    return total


def label_spec(key: str, language: str = DEFAULT_LANGUAGE) -> LabelSpec:
    """Resolve a label key into a localized :class:`LabelSpec`."""
    ld = LABELS[key]
    lang = resolve_language(language)
    name = ld["names"].get(lang) or ld["names"][DEFAULT_LANGUAGE]
    return {"name": name, "color": ld["color"], "icon": ld["icon"]}


def _collect_label_keys(
    entry: EntityLike, options: OrganizerOptions
) -> tuple[list[str], list[str]]:
    """Return (label keys, match reasons) in priority order.

    A "reason" is the raw thing that matched (a domain name, device_class,
    integration platform, or keyword) — more specific than the label key
    it maps to, and used to look up a more specific icon in
    :data:`SPECIFIC_ICONS`. Shared by :func:`compute_label_specs` and
    :func:`suggest_entity_icon` so both stay in sync.
    """
    keys: list[str] = []
    reasons: list[str] = []
    seen: set[str] = set()

    def add(key: str | None, reason: str | None = None) -> None:
        if not key or key in seen:
            return
        if options.enabled_labels and key not in options.enabled_labels:
            return
        seen.add(key)
        keys.append(key)
        if reason:
            reasons.append(reason)

    platform = getattr(entry, "platform", None)
    is_category = bool(
        options.skip_categories and getattr(entry, "entity_category", None)
    )

    # Curated integration themes apply even to diagnostic/config entities.
    if options.enable_curated:
        if platform:
            add(INTEGRATION_LABELS.get(platform), reason=platform)
        # Known vehicle names always count as "car".
        ename = getattr(entry, "name", None) or getattr(
            entry, "original_name", None
        )
        hay = _normalize(f"{entry.entity_id} {ename or ''}")
        for kw in CAR_NAME_KEYWORDS:
            if f" {kw} " in hay:
                add("car", reason=kw)
                break

    # Domain/device_class labels are skipped for config/diagnostic helpers.
    if not is_category:
        domain = entry.entity_id.split(".", 1)[0]

        if options.enable_domain:
            add(DOMAIN_LABELS.get(domain), reason=domain)

        if options.enable_device_class:
            device_class = entry.device_class or entry.original_device_class
            if device_class:
                add(DEVICE_CLASS_LABELS.get(device_class), reason=device_class)

        # Keyword fallbacks only when nothing more specific matched. Matched
        # against the normalized entity_id and friendly name. User-defined
        # custom rules take precedence over the built-in vocabulary.
        if not keys:
            ename = getattr(entry, "name", None) or getattr(
                entry, "original_name", None
            )
            hay = _normalize(f"{entry.entity_id} {ename or ''}")
            for needle, key in options.custom_rules.items():
                if needle in hay:
                    add(key, reason=needle)
            for needle, key in KEYWORD_LABELS.items():
                if needle in hay:
                    add(key, reason=needle)

    return keys, reasons


def suggest_entity_icon(
    entry: EntityLike, options: OrganizerOptions
) -> str | None:
    """Return a more specific icon for the entity, if one is known.

    Checked in order from most to least specific: keyword/custom-rule (a
    named device like "Kaffeemaschine" or "Wohnzimmer TV") > source
    integration (e.g. "spotify", "nuki" — the actual product/service) >
    device_class > bare HA domain (the broadest fallback, e.g. every
    ``light.*`` entity). Unlike label matching, this always checks keywords
    first regardless of whether a domain/device_class already matched,
    since a keyword names the actual device while the domain only names its
    HA category. Every domain in :data:`DOMAIN_LABELS` has an entry in
    :data:`SPECIFIC_ICONS`, so this only returns ``None`` for an excluded
    entity or an unrecognized domain.
    """
    if is_excluded(entry.entity_id, options.exclude):
        return None

    ename = getattr(entry, "name", None) or getattr(entry, "original_name", None)
    hay = _normalize(f"{entry.entity_id} {ename or ''}")

    for needle in options.custom_rules:
        if needle in hay:
            icon = SPECIFIC_ICONS.get(needle.strip())
            if icon:
                return icon
    for needle in KEYWORD_LABELS:
        if needle in hay:
            icon = SPECIFIC_ICONS.get(needle.strip())
            if icon:
                return icon
    for kw in CAR_NAME_KEYWORDS:
        if f" {kw} " in hay:
            icon = SPECIFIC_ICONS.get(kw)
            if icon:
                return icon

    # The source integration (e.g. "spotify", "nuki", "ring") names the
    # actual product/service, which is more specific than the bare HA
    # domain/device_class it happens to expose — check it first.
    platform = getattr(entry, "platform", None)
    if platform:
        icon = SPECIFIC_ICONS.get(platform)
        if icon:
            return icon

    device_class = entry.device_class or entry.original_device_class
    if device_class:
        icon = SPECIFIC_ICONS.get(device_class)
        if icon:
            return icon

    domain = entry.entity_id.split(".", 1)[0]
    icon = SPECIFIC_ICONS.get(domain)
    if icon:
        return icon

    return None


def compute_label_specs(
    entry: EntityLike, options: OrganizerOptions
) -> list[LabelSpec]:
    """Return the list of label specs that apply to a single entity.

    Pure function (no Home Assistant state) so the ruleset can be unit-tested
    in isolation.
    """
    # User exclusions take priority over everything else.
    if is_excluded(entry.entity_id, options.exclude):
        return []

    keys, _ = _collect_label_keys(entry, options)
    specs = [label_spec(k, options.language) for k in keys]

    platform = getattr(entry, "platform", None)
    is_category = bool(
        options.skip_categories and getattr(entry, "entity_category", None)
    )
    if options.enable_integration and not is_category and platform:
        specs.append(
            {"name": platform, "color": "grey", "icon": "mdi:puzzle"}
        )

    if options.label_prefix:
        specs = [{**s, "name": f"{options.label_prefix}{s['name']}"} for s in specs]

    # Cap the number of labels per entity (most relevant first).
    if options.max_labels and len(specs) > options.max_labels:
        specs = specs[: options.max_labels]

    return specs
