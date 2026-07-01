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
    # climate / heating
    "klima": "climate",
    "heizung": "climate",
    "heizkoerper": "climate",
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
    # locks
    "tuerschloss": "locks",
    "schliessanlage": "locks",
    "deadbolt": "locks",
    "door lock": "locks",
    "schloss": "locks",
    "verriegelt": "locks",
    "verriegelung": "locks",
    "tuerriegel": "locks",
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
    if options.enable_curated:
        if platform:
            add(INTEGRATION_LABELS.get(platform))
        # Known vehicle names always count as "car".
        ename = getattr(entry, "name", None) or getattr(
            entry, "original_name", None
        )
        hay = _normalize(f"{entry.entity_id} {ename or ''}")
        if any(f" {kw} " in hay for kw in CAR_NAME_KEYWORDS):
            add("car")

    # Domain/device_class labels are skipped for config/diagnostic helpers.
    if not is_category:
        domain = entry.entity_id.split(".", 1)[0]

        if options.enable_domain:
            add(DOMAIN_LABELS.get(domain))

        if options.enable_device_class:
            device_class = entry.device_class or entry.original_device_class
            if device_class:
                add(DEVICE_CLASS_LABELS.get(device_class))

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
                    add(key)
            for needle, key in KEYWORD_LABELS.items():
                if needle in hay:
                    add(key)

    specs = [label_spec(k, options.language) for k in keys]

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
