# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2026-07-01

### Added (synonym-cluster pass across all categories)
Several categories had almost no keyword fallback at all (they relied
entirely on the HA domain matching, which misses helper/template entities
that merely *reference* a device type by name). Added German+English
synonym clusters for:
- **Lights** (was just "Lichterkette"): Lampe, Glühbirne, Leuchte,
  Deckenleuchte, Stehlampe, Tischlampe, Wandleuchte, Pendelleuchte,
  Nachtlicht, LED-Streifen, Licht, Spot, Strahler; lamp, bulb, spotlight,
  downlight, nightlight, flashlight, chandelier, sconce, floor/table/ceiling
  lamp, wall/pendant light, LED strip.
- **Switches** (was empty): Steckdose, Steckdosenleiste, Schalter, outlet,
  socket, smart plug.
- **Vacuums** (was empty): Staubsauger, Saugroboter, Wischroboter, vacuum,
  robot vacuum, Roomba, Roborock, iRobot.
- **Cameras** (was just "Reolink"): Kamera, Überwachungskamera, camera,
  webcam, CCTV, NVR, video doorbell.
- **Waste** (was integration-only): Abfall, Müll, Mülltonne, Restmüll,
  Biomüll, Gelber Sack, Altpapier, Wertstoff, Entsorgung, trash, garbage,
  recycling.
- **Shopping** (was integration-only): Einkaufsliste, Einkauf,
  Lebensmittel, grocery, shopping list.
- **Updates** (was just "firmware"): Aktualisierung, software update, new
  version.
- **Locks**: Schloss, verriegelt, Verriegelung, Türriegel.
- **Fans**: Gebläse, blower, ceiling fan, generic "fan".
- **Media**: TV / television.
- **Security**: Klingel, Türklingel, doorbell.
- Smaller top-ups for water (Durchfluss, Wasserstand, flow rate), leak
  (water overflow), temperature/humidity/motion/light-level (generic temp,
  dew/damp, movement/PIR, lux), cost (Gebühr, Abrechnung, billing, price),
  garden (Blumen, Pflanzen, garden hose), network (modem), appliances
  (Mikrowelle, microwave, toaster), and car (charging station, PHEV).
- Ambiguous/collision-prone short words (`licht`, `spot`, `strahler`,
  `socket`, `tv`, `temp`, `pir`, `lux`, `fan`, `damp`, `muell`, `nvr`,
  `phev`, `blumen`) are matched with explicit word-boundary padding to
  avoid false positives — confirmed by testing against real collisions
  such as German "Pflicht"/"Birnensaft"/"Heizstrahler"/"Blumenkohl"/
  "Müller" (common surname) and English "websocket"/"basket"/"pocket"/
  "woven"/"infant"/HVAC "damper".

### Added
- Two new curated theme labels: **Waste** (`waste_collection_schedule`
  integration) and **Shopping** (`tgtg` / Too Good To Go integration).
- New domains: `valve` (covers), `air_quality`, `assist_satellite`/`stt`/`tts`
  (media).
- New device classes: `volume` and `ph` (water).
- Much larger keyword vocabulary, in both German and English, derived from a
  real-registry gap analysis plus a broader pass over common Home Assistant
  naming conventions: energy (inverter, consumption, feed-in), water/leak
  (Shelly Flood), garden (lawn/watering, mower, sprinkler), climate (HVAC,
  heat pump, furnace, boiler, BLE temperature monitors), cost (tariff,
  savings, heating-oil price), presence (Android/tablet, kiosk, bed sensor),
  security (door-sensor phrasing, intrusion, smoke detector, additional
  German door-name compounds), covers (shutters, blinds, awning), locks
  (deadbolt), appliances (oven, fridge, freezer, dryer, kettle), air quality
  (CO2, particulate) and EV models (e-tron, Niro, Ariya, Outlander).
- Many new curated integration themes: solar/inverter brands (SolarEdge,
  Fronius, Growatt, Victron, Huawei, Solax, GoodWe, Enphase), dynamic
  electricity tariffs (Tibber, aWATTar, EnergyZero, Nordpool, Octopus),
  EV/charging brands (Ohme, myenergi, Tesla Wall Connector, Teslemetry, BMW,
  Mercedes, Kia, Hyundai, Renault, Volvo, Smartcar), HVAC brands (MELCloud,
  Tado, ecobee, Sensibo, Nibe, OpenTherm), cameras/NVR (Ring, UniFi Protect,
  Amcrest, Eufy, Arlo), alarm systems (Abode, Verisure, SimpliSafe,
  Envisalink, Konnected), locks (August, Schlage, Nuki), presence tracking
  (Life360, OwnTracks, GPSLogger, iCloud, Fully Kiosk), media platforms
  (Spotify, Cast, Apple TV, webOS, Samsung/Android TV, Denon, MusicCast,
  HEOS, Roon, Volumio, Squeezebox, BluOS), air quality (AirVisual, Airly,
  PurpleAir), weather (Pirate Weather, Tomorrow.io, Buienradar, Tempest,
  Ambient Weather), garden/irrigation (Rachio, Husqvarna Automower, Hunter
  Hydrawise), and network monitoring (ASUSWRT, Netgear, AdGuard,
  UptimeRobot, Synology DSM).

### Fixed
- Removed an unsafe generic keyword ("oven" without word-boundary
  anchoring) that collided with unrelated words like "woven"; re-added with
  whole-word matching only.

## [0.3.0] - 2026-06-20

### Added
- Much larger label vocabulary (data-driven from real registries): PV/grid,
  voltage/frequency, consumption/feed-in, UV & weather stations (Ecowitt),
  air quality (VOC), personal devices (presence), doors/windows by name,
  and integration themes (Frigate, WLED, DWD, hassio, Marstek, Reolink, …).
- Home Assistant integration tests in CI (config flow, services, entities).
- Brand icon/logo assets in the repository for the HACS listing.

### Changed
- Renamed the internal engine from "Labeler" to **Organizer** (it manages
  both labels and areas); the domain stays `auto_organizer`.

## [0.2.0] - 2026-06-18

### Added
- **Repair issues**: a warning when custom rules reference unknown labels, and
  when area/floor labeling is enabled but no areas exist.
- **Diagnostics**: download config-entry diagnostics (options + stats + last
  run summary, no secrets) from the device page.
- **Automatic language**: label language now defaults to `auto`, following
  Home Assistant's configured language (resolved to German or English).
- **Custom rules**: user-defined `keyword=label` mappings (per line/comma);
  only existing labels are accepted, applied as a prioritized keyword layer.
- **Exclude option**: skip entities from labeling and area assignment by
  domain, exact entity_id or fnmatch pattern (e.g. `sensor.test_*`).
- **Auto-label new entities**: newly added entities are labeled automatically
  (debounced) via the entity-registry event; toggle `auto_label_new`
  (default on).
- **Control entities** (a device with): *Run now* and *Cleanup labels* buttons,
  a *Run scope* select (labels+areas / only labels / only areas), a *Dry run*
  switch, and sensors: *Last run* (+ details), *Last run time*, *Labeled
  entities*, *Unlabeled entities*, *Entities without area*, *Managed labels*
  and *Label coverage* (%).
- `auto_organizer.assign_areas` service: auto-assigns entities **without** an
  area to a matching area by name/alias (longest match wins, ambiguous matches
  skipped). Supports `dry_run`; never changes existing area assignments.
- Known vehicle names (e-Golf, Tesla, Zoe, Leaf, Kona, Ioniq, …) are labeled
  **Auto** even when a device class also applies.
- `max_labels` option (default **2**) caps labels per entity.
- Much larger keyword vocabulary (German + English) for the fallback, now
  matched against the normalized entity_id **and** friendly name, so more
  entities get a sensible label (e.g. Wasser, Klima, Medien, Garten).

### Changed
- Doors/windows/openings now map to **Sicherheit** (the separate "Öffnungen"
  label was removed).
- Frost/storm warnings map to **Wetter**; heating-oil entities (oilfox,
  Ölverbrauch) map to **Klima**.

## [0.1.0] - 2026-06-18

### Added
- Rule-based entity labeling by **domain** and **device class** with an
  `entity_id` keyword fallback.
- Curated **integration theme** labels: Haushaltsgeräte (appliances), Garten
  (garden), Netzwerk & Server (network), Auto (car / charging). These apply
  even to diagnostic/config entities.
- **Kosten** (cost) label for the `monetary` device class.
- German (default) and English label names via a language-keyed catalog
  (`language` option).
- Optional **area** and **floor** labels (`enable_area` / `enable_floor`).
- Services `auto_organizer.run` (with `dry_run`, `overwrite`, `entities`) and
  `auto_organizer.cleanup`, both returning a result summary.
- Options: dry run, overwrite, per-rule toggles, skip diagnostic/config
  entities, run on startup, recurring re-scan interval, label prefix.
- Config flow (single instance) and EN/DE translations.
- hassfest + HACS validation workflow and a pure, HA-independent unit-test
  suite (40 tests).

### Notes
- Energy stays a single **Energie** label (power/energy/current/voltage/gas …);
  it is intentionally not split.
- Labels created by the integration are marked internally so `cleanup` never
  removes labels you created by hand.

[Unreleased]: https://github.com/hiSweid/ha-auto-organizer/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/hiSweid/ha-auto-organizer/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/hiSweid/ha-auto-organizer/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/hiSweid/ha-auto-organizer/releases/tag/v0.1.0
