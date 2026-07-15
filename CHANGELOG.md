# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.9.120] - 2026-07-15

### Added
- Vocabulary growth: 145 new keywords (123 with icon mappings). Category batches
  for the smallest labels (motion, automations, battery) plus a batch of real
  device/platform synonyms (ZHA/Zigbee2MQTT, Matter, brands like Aqara/Eve/
  IKEA Tradfri/tado/Shelly/Tuya). Covers mmWave/PIR presence terms, automation
  trigger/condition vocabulary, cell-chemistry and BMS protection terms, and
  common device names. KEYWORD_LABELS now totals 21527.

## [0.9.119] - 2026-07-15

### Added
- Vocabulary growth: 146 new keywords (131 with icon mappings). Category batches
  for the smallest labels (energy, leak, scripts) plus an icon-driven batch
  (sport/leisure MDI icons) and a batch of real device/platform synonyms
  (ZHA/Zigbee2MQTT, Matter, brands like Avatto/Linptech/Heiman/Zanussi/Haier/
  Vorwerk/Shark/Marantec/IKEA Tradfri). KEYWORD_LABELS now totals 21382.

## [0.9.118] - 2026-07-15

### Added
- Vocabulary growth: 121 new keywords (98 with icon mappings). Category batches
  for the smallest labels (cost, waste, car) plus a batch of real
  device/platform synonyms (ZHA/Zigbee2MQTT, Matter, brands like
  Aqara/Eve/IKEA/Shelly/tado/Nuki). KEYWORD_LABELS now totals 21236.

## [0.9.117] - 2026-07-14

### Added
- Vocabulary growth: 165 new keywords (72 with icon mappings). Category batches
  for the smallest labels (updates, temperature, weather), a batch of previously
  unused Material Design Icons, and a batch of real device/platform synonyms
  (ZHA/Zigbee2MQTT, Matter, brands like Aqara/Eve/IKEA/Shelly/tado/Bosch).
  KEYWORD_LABELS now totals 21115.

## [0.9.116] - 2026-07-14

### Added
- Vocabulary growth: 154 new keywords with icon mappings. Category batches for
  the smallest labels (humidity, shopping, light_level), a batch of previously
  unused Material Design Icons, and a batch of real device/platform synonyms
  (ZHA/Zigbee2MQTT, Matter, brands like Aqara/Eve/IKEA/Shelly/tado/Bosch).
  KEYWORD_LABELS now totals 20950.

## [0.9.115] - 2026-07-14

### Added
- Vocabulary growth: 119 new keywords with icon mappings across the three
  smallest categories (security, covers, lights) plus a device-synonym batch.
  Adds security terms (biometric/iris scanners, ALPR, tamper/duress alarms,
  dome/turret/facade cameras, security shutter), shutter/awning terms
  (Gurtwickler, Roma/Warema shutters, patio awnings, conservatory roof, solar
  shade motor), lighting terms (wall washers, Nanoleaf/LIFX/Hue Signe/Livarno
  fixtures, floodlights, RGBIC/star projectors) and cross-ecosystem device
  synonyms (radiator/actuator valves, irrigation valve, dimmer button, Zigbee
  heating actuator, wallbox power). 119 regression tests added.

## [0.9.114] - 2026-07-14

### Added
- Vocabulary growth: 96 new keywords with icon mappings across the three
  smallest categories (fans, network, locks). Adds ventilation and fan-brand
  terms (Schwenkventilator, Deckenventilator, Wrasenabzug, Alpenfoehn/Sharkoon
  cooling fans, ESPHome/Sonoff/Aqara fans), network/telephony terms (VoIP/SIP
  phones, Fritzfon, Yealink, Snom, Datenvolumen, Netzwerkauslastung), and
  access-control/lock terms (Handschuhfachschloss, Zuendschloss, palm/face
  scanners, Schluesselverwaltung, Zutrittshistorie). Total keyword count now
  20677.

## [0.9.113] - 2026-07-14

### Added
- Vocabulary growth: 138 new keywords with icon mappings across the three
  smallest categories (automations, motion, scenes) plus a cross-ecosystem
  device-synonym pass. Adds switching/timing/ramp and reminder-automation
  terms (Wechselschaltung, Sanftanlauf, Dimmrampe, Boostmodus, Frostwaechter,
  Jalousie-/Garagentor-/Torautomatik) for automations; presence-radar and
  mmWave terms plus motion-sensor brands (Acconeer XM125, AWR1642, Everything
  Presence One, Innr/Ledvance/Osram/Namron/Opple/Zemismart, target/distance
  gating) for motion; light-scene and mood names (Kerzenschimmer, Milchstrasse,
  Regenwald, Backabend, Werkstatt, Journaling, Heiligabend) for scenes; and
  real device synonyms (heat pumps: Viessmann Vitocal, Daikin Altherma,
  Mitsubishi Ecodan, LG Therma; wallboxes: Alfen Eve, ABL, Webasto, Vestel;
  BYD/Delta Pro storage, Deye/Sofar inverters, Dreame vacuum, Orbit B-hyve,
  pellet boilers). Total keywords: 20581.

## [0.9.112] - 2026-07-14

### Added
- Vocabulary growth: 171 new keywords with icon mappings across the three
  smallest categories (water, cameras, scripts) plus a cross-ecosystem
  device-synonym pass and an MDI-icon-driven pass. Adds plumbing valves,
  tanks, hot-water/legionella and drainage terms for water; camera brands and
  product lines (Reolink, Arlo, Tapo, Amcrest/EmpireTech, Ctronics) plus
  NVR/PTZ/ONVIF terms for cameras; wake/bedtime/arrival/leaving script names
  and skript-prefixed phrases for scripts; and real device synonyms (Aqara,
  Eve, Shelly, Tuya lock actuators, contact/tilt sensors, floodlights, roller
  shutter motors, feed-in meters and more). Total keywords: 20456.

## [0.9.111] - 2026-07-14

### Added
- Vocabulary growth: 149 new keywords and 166 icon mappings across the three
  smallest categories (battery, vacuums, presence) plus a cross-ecosystem
  device-synonym pass. Adds tool-battery brands, cell types and charging/BMS
  terms for battery; robot-vacuum brand/model names and tank/dock/cleaning
  terms for vacuums; mmWave/radar presence sensors, BLE trackers and
  arrival/away state phrases for presence; and real device/platform synonyms
  (Nous, Paulmann, Rademacher, Busch-Jaeger, ESPHome, SMLIGHT, Fibaro, and
  more), including 18 icon-only additions for existing brand keywords that
  previously fell back to the generic domain icon. Total keywords: 20272.

## [0.9.110] - 2026-07-14

### Added
- Vocabulary growth: 146 new keywords and 136 icon mappings across the three
  smallest categories (air_quality, cost, climate) plus a cross-ecosystem
  device-synonym pass. Adds pollen species and pollutant/vapour terms for
  air quality, tax/insurance/fee and provider terms for cost, heat-pump and
  thermostat brand/model and HVAC component terms for climate, and real
  device names from ZHA/Matter ecosystems (Homematic IP, Aqara, Shelly,
  Sonoff, IKEA, doorbell/intercom stations, Zigbee coordinators). Total
  keywords: 20123.

## [0.9.109] - 2026-07-14

### Added
- Vocabulary growth: 175 new keywords and 175 icon mappings across the
  smallest categories (leak, updates, temperature) plus an MDI-icon sweep and
  a cross-ecosystem device-synonym pass. Adds fuel/oil/coolant and
  moisture-ingress leak terms, firmware/OTA update phrasings, flow/return and
  component temperature readings (CPU/GPU/disk, condenser/evaporator, dew
  point), and device synonyms (change-over/flow valves, current transformer,
  bolt drive, IR blaster, garden solenoid valve). Total keywords: 19977.

## [0.9.108] - 2026-07-14

### Added
- Vocabulary growth: 155 new keywords and 151 icon mappings across the
  smallest categories (switches, light_level, waste) plus MDI-icon and
  cross-ecosystem device-synonym passes. Adds switch/plug/relay product
  names (Shelly Pro, Sonoff, Kasa, Zooz, Inovelli, Schneider Wiser, Feller,
  MDT, Zennio) and German terms (Schiebeschalter, Pilztaster, Schlüsseltaster,
  Bistabilrelais, Brandschutzschalter), lux/illuminance sensor chips
  (OPT4048, BH175x, CM32xx, VCNL4200, APDS93xx) and brightness-sensor
  synonyms, waste/recycling terms (Mischabfall, Kompostwerk, Wertstoff bins,
  Absetzmulde, pedal/swing/sensor bins), plus household/lighting/car/food
  icon vocabulary (Wandlaterne, Roboterrasenmäher, Schallplattenspieler,
  Motorölstand, Turboaufladung).

## [0.9.107] - 2026-07-14

### Added
- Vocabulary growth: 130 new keywords and icon mappings across the smallest
  categories (scripts, humidity, scenes) plus a cross-ecosystem device-synonym
  pass. Adds named-routine/script phrases (morning/away/travel/guest/cleanup
  routines, panic button), humidity terms (dew point, mould risk, VPD,
  hygrometers, greenhouse/terrarium moisture), light-scene names (hygge, movie
  marathon, aurora, campfire, twilight), and real device synonyms (Aqara
  presence, Eve MotionBlind, VELUX roller shade, go-eCharger, DECT phone,
  fiber modem, Govee light strip, oil-tank/cistern level, particulate sensor).

## [0.9.106] - 2026-07-14

### Added
- Vocabulary growth: 121 new keywords and 93 icon mappings across the
  smallest categories (garden, locks, battery) plus a cross-ecosystem
  device-synonym pass. Includes robotic-mower and irrigation brands,
  smart-lock product lines (SimpliSafe, Level, SwitchBot, Tedee, Ultraloq,
  eufy, Yale, Schlage, ISEO, Salto, …), home-storage/inverter brands
  (Growatt, Victron, Fronius, SolarEdge, Enphase, E3DC, …), per-device
  battery sensors, and Matter/Zigbee device names (covers, presence,
  light-level, EV charging control, weather).

## [0.9.105] - 2026-07-14

### Added
- `run`/`preview` responses now include a `reasons` field per changed entity
  listing which keyword/domain/device_class/platform actually matched, so a
  wrong or unexpected label can be traced without reading rules.py.
- New `tests/test_vocab_batches.py`: the vocabulary-growth tooling now
  appends one regression test per merged word here, so a later vocabulary
  batch that shadows or breaks an earlier word's match fails a concrete,
  named test instead of silently regressing.

### Changed
- `compute_label_specs()` is now a thin wrapper around the new
  `compute_label_specs_and_reasons()`; no behavior change for existing
  callers.

## [0.9.104] - 2026-07-14

### Added
- **113 new keywords and 101 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories (scripts, fans, temperature)
  plus MDI-icon coverage and real-world device/platform synonyms. Highlights:
  fan/blower types and PC/ceiling-fan brands (Arctic, Scythe, NZXT, Atomberg,
  Crompton, Havells), flow/return/oil/engine/water/soil temperature sensors and
  probes, script/macro/command-sequence terms, plus assorted appliances,
  shopping, locks, covers and weather-sensor keywords. Icons validated against
  MDI metadata and collision-checked against the frequency word lists.

## [0.9.103] - 2026-07-14

### Added
- **173 new keywords and 140 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories (automations, weather,
  motion) plus a batch of real-world device/platform synonyms across
  ecosystems (EV charging brands go-e/Mennekes/Compleo, FRITZ!DECT models,
  Aqara/SwitchBot device types, mmWave radar modules). Automations gained
  compound trigger/schedule terms, weather gained meteorological and
  astronomical vocabulary, motion gained radar/vibration/gesture terms.

## [0.9.102] - 2026-07-14

### Added
- **133 new keywords and 131 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories (light_level, vacuums,
  air_quality) plus a batch of real-world device/platform synonyms across
  ecosystems (ZHA/Zigbee2MQTT, Matter, Aqara/Eve/Shelly/Sonoff/Homematic IP).
  Additions include ambient-light/lux sensor chips and dusk/daylight-threshold
  terms, robot vacuum & mower brands/models and cleaning-cycle vocabulary,
  air-quality sensor chips (SCD4x, SGP4x, SEN5x) plus pollen/particulate/VOC
  terms, and device synonyms such as in-wall dimmers, wallbox actuators,
  door-contact magnets and leak/water-guard sensors.

## [0.9.101] - 2026-07-14

### Added
- **162 new keywords and 119 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories (waste, updates, water)
  plus a batch of previously unused Material Design Icons mapped to smart-home
  device terms and a batch of real-world device/platform synonyms across
  ecosystems (ZHA/Zigbee2MQTT, Matter, KNX, Aqara/Eve/Shelly/Tuya). Additions
  include waste collection and recycling terms, firmware/OTA update vocabulary,
  water-supply/valve/hot-water terms, and device synonyms such as DIN-rail
  actuators, ceiling/in-wall speakers, shutter drives and pond aerators.

## [0.9.100] - 2026-07-14

### Added
- **147 new keywords and 138 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories (car, security, network)
  plus a batch of real-world device/platform synonyms across ecosystems
  (ZHA/Zigbee2MQTT, Matter, Aqara/Eve/Shelly/Tuya and alarm-panel brands).
  Additions include EV charging and model terms, alarm-panel brands and
  arming/entry-delay vocabulary, networking terms (latency, uplink/downlink,
  subnet, mesh) and device synonyms such as motorized projector screens,
  pool covers and water-damage sensors.

## [0.9.99] - 2026-07-14

### Added
- **175 new keywords and 155 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — media (orchestral and band
  instruments like cello/kontrabass/klarinette/posaune/synthesizer, vintage
  playback such as walkman/minidisc/laserdisc/grammophon, shortwave/longwave
  radio, karaoke, pre-amps and tone controls), cost (taxes and fees such as
  lohnsteuer/gewerbesteuer/maut/vignette/bussgeld, mortgage and savings terms
  like bauzins/sondertilgung/bausparvertrag/festgeld/tagesgeld, insurance and
  services like kaskoversicherung/schornsteinfeger) and presence (mmWave radar
  models LD2451/MR60FDA2, human static presence, BLE/Wi-Fi client tracking,
  occupancy states such as buero besetzt/wc besetzt/parkplatz frei) — plus real
  device/ecosystem synonyms (heat pump dryer, sauna heater, steam generator,
  gas fireplace, Eve Spirit TRV, CT clamp, Leviton switches, motion/pantry
  lights, water fountain, terrarium).

### Added
- **182 new keywords and 171 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — cameras (brand cams like
  SimpliSafe/Somfy Outdoor, Docker Wyze bridge, IR/night-vision range,
  pre/post-alarm recording), shopping (returns/refunds, pre-order, sold out,
  wholesale, price match, next-day delivery, self checkout, garden centre,
  Christmas market), and energy (inverter/meter brands such as RCT Power, SAX
  Power, Carlo Gavazzi, Powerfox, SolarFlow, direct marketing, micro/smart
  grid, ammeter) — plus real device/ecosystem synonyms (Velux Integra, Fibaro
  shutter, SwitchBot hub/bot, Tapo/LIFX/Nanoleaf lights, Osram/Theben/Eltako
  switches, SolarEdge/Sofar/Growatt/Sungrow/Enphase inverters, Pylontech,
  Tibber Pulse, Yale Doorman, Tedee, LOQED, Gardena smart, Warema) and a batch
  of untapped smart-home MDI icons (blinds-vertical, coach-lamp, power-socket,
  fuse-blade, portable generator, pool/snowflake thermometer, weather
  hurricane/tornado/sunset, industrial fridge, wireless speaker, car door lock).
  Several existing brand keywords gained their first icon. All collision-checked
  against 50k DE/EN frequency lists; tests green.

## [0.9.97] - 2026-07-13

### Added
- **153 new keywords and 134 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — scenes (named mood/routine
  scenes and ambiance phrases), humidity (thermo-hygrometer models such as
  Govee H5101/H5103, SwitchBot Meter Pro, ThermoPro TP55, sensor chips and
  per-room humidity phrases), and leak (water-leak/flood detectors and shutoff
  phrases like Moen Smart Water, Meross/Onvis/Leviton water sensors, dripping
  pipe/faucet, wet floor/wall) — plus a batch of real device/ecosystem
  synonyms across presence, lights, covers, climate, locks, energy, vacuums
  and garden (Aqara FP2/T1 presence, Ubisys S1/J1, IKEA DIRIGERA, Eve
  Energy/Aqua/Thermo, Hörmann gate drive, wischsaugroboter, and more).
  Physical scene-controller buttons, tank-level sensors and ambiguous generic
  valves/plugs were deliberately excluded to avoid mislabeling.

## [0.9.96] - 2026-07-13

### Added
- **167 new keywords and 166 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — battery (storage/BMS brands
  like Fox ESS, Enphase IQ, LG RESU, Victron SmartShunt and Orion/JBD/ANT BMS,
  plus cell codes and terms like coulombic efficiency, sulfation, capacity
  fade), motion (real mmWave/PIR/accelerometer chips such as LD2413, LD1115,
  DFRobot C4001, Apollo MSR2, ADXL345, MLX90640, plus radar gate/energy and
  wifi-sensing terms), and temperature (sensor ICs like TMP36, ADT7420,
  DS1631, grill/BBQ probes, and radiant/globe/refrigerant temperature terms) —
  plus a batch of real device/ecosystem synonyms across network, lights,
  switches, energy, water, climate, covers, cameras, presence, security and
  more (range extenders, metering sockets, load-shedding relays, bollard
  lights, pool cleaning robots, intercom modules, storm protection).

## [0.9.95] - 2026-07-13

### Added
- **135 new keywords and 124 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — air_quality (aerosols, spores,
  allergens, gas/particulate concentration terms), automations (weekly/window
  schedules, hysteresis, macro/loop/chaining flows, sunset/brightness/presence/
  motion switching triggers), and light_level (luminance sensors, lux
  range/limit/data, twilight and indoor/outdoor brightness) — plus a batch of
  smart-home icons (grills, ovens, snow removal tools, patio heater, scent
  diffusers, workshop lamps) and real device/ecosystem synonyms (scene
  controllers, clamp meters, IR blasters, Thread border routers, valve
  actuators, salt/pressure-boost water systems).

### Added
- **104 new keywords and 102 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — fans (heat/energy recovery
  ventilators, extractor/chimney hoods, tower/pedestal/bladeless fans, cross-flow
  and tangential blowers, HVAC brands like Dyson/Vornado/Meaco), garden (robotic
  mowers and brands Gardena/Husqvarna/Worx/Navimow, drip/greenhouse/raised-bed
  terms, fruit trees and plant sensors), and presence (mmWave radar modules
  LD2412/LD2413/MR60 and brands Aqara FP1/FP2/Everything Presence, geofence and
  room-occupancy logic, tracker platforms Owntracks/Overland/Traccar) — plus a
  batch of real-world device/ecosystem synonyms (IKEA Styrbar/Rodret, Nuki Go/
  Ultra, Shelly/Sonoff/Aqara/Eve/Moes device names).

## [0.9.93] - 2026-07-13

### Added
- **151 new keywords and 154 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — scripts (shell/regex/cron
  constructs, concurrency primitives like mutex/semaphore/deadlock, retry and
  watchdog/self-healing logic, scheduler and job-queue terms), locks (cylinder
  and latch internals, key variants, trailer/hasp locks, access-schedule and
  invalid-code states, Dessmann/Mijia lock naming) and vacuums (mopping and
  dock-heating features, brush types, obstacle/AI navigation, wear indicators,
  Dreame/Ecovacs model names). Plus a device-synonym pass covering real
  ZHA/Zigbee2MQTT and Homematic IP device names (IKEA RODRET/SOMRIG/PARASOLL,
  Sonoff SNZB, Ubiquiti G4 doorbell, Aqara, Homematic IP actors/sensors),
  including icon-only additions for existing keywords that previously fell back
  to the generic domain icon (rodret, somrig, parasoll, soil sensor, ir
  blaster, mmwave, lux sensor).

## [0.9.92] - 2026-07-13

### Added
- **117 new keywords and 109 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — cost (dynamic/time-of-use and
  day-ahead tariffs, EPEX/wholesale pricing, SEPA/direct-debit and payment
  terms, energy-provider billing, LCOE and return-on-capital), updates
  (firmware release/branch/flash/download flows, Tasmota/Docker/database
  migrations, security-update and rollout states, changelog and channel
  vocabulary), and climate (inverter/compressor AC, Buderus/Remeha/Namron/
  Silvercrest heating and thermostat brands, heating curve and AC remote
  terms) — plus a real device synonym (network repeater). German and English.

## [0.9.91] - 2026-07-13

### Added
- **128 new keywords and 109 new specific icons.** Incremental vocabulary
  growth across the three smallest categories — motion (mmWave/radar chips
  like HLK-LD2450, presence-sensor brands, pet-immune and multi-zone radar
  terms), lights (LED brands milight/miboxer/lohas/feit/cree, ring/studio/
  stage/blacklight fixtures, seasonal Schwibbogen/Adventsbeleuchtung), and
  shopping (grocery/drugstore delivery, staple food items, order/return and
  best-before vocabulary) — plus real device/platform synonyms (window-handle
  and gate-motor sensors, inverters, boilers, soundbars, bollard lights) and a
  batch of validated MDI-icon-backed terms.


### Added
- **104 new keywords and 61 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories — temperature (sensor chips
  like si7021/bme280, brand thermostats, culinary/industrial temperature
  terms), waste (commercial-waste ordinances, bin/collection terms,
  recycling schemes, food-waste digesters), leak (water/gas/flood detector
  brands and models such as WaterCop, FloodStop, Fibaro FGFS, Milesight
  EM300, plus pipe/pressure/gas-leak vocabulary).

## [0.9.89] - 2026-07-13

### Added
- **179 new keywords and 173 new specific icons.** Incremental vocabulary
  growth focused on the three smallest categories — humidity (condensation,
  mold, hygrometer chips and models), water (boilers, pumps, valves, tank
  levels, aquarium/pond water quality), weather (wind, cloud types,
  pressure, precipitation) — plus a batch of real device/platform synonyms
  across ecosystems (Aqara, Gardena, IKEA Tradfri, Shelly, Sonoff, Jung,
  Fronius/Kostal inverters, EV chargers, and more).

## [0.9.88] - 2026-07-13

### Fixed
- **Run/Cleanup/Remove-All now honor a configured dry-run default.**
  `runtime.dry_run` used to hardcode to `False` at startup and only ever get
  set from the dry-run switch entity's state. On a fresh install (or before
  the switch had ever been toggled), pressing "Run now" would write real
  labels/icons even if "Testlauf (keine Änderungen schreiben)" was enabled
  in the options flow. It's now seeded from the configured option at setup;
  the switch's restored state still takes over once it exists.
- **Excluded entities no longer get area/floor labels.** `exclude` patterns
  were only checked inside the functional-label matching, not before the
  area/floor labels that get appended afterwards — an explicitly excluded
  entity could still pick up its area/floor label. Exclusions are now
  checked once per entity before any labeling happens.

### Changed
- The "Remove ALL labels" button is now disabled by default. It deletes
  every label in the whole Home Assistant instance — not just ones this
  integration created — with no undo, and Home Assistant buttons have no
  confirmation dialog. Enable it explicitly if you need it; the
  `auto_organizer.remove_all` service is unaffected.

### Added
- Three regression tests covering the fixes above
  (`tests/integration/test_init.py`).

## [0.9.87] - 2026-07-13

### Fixed
- Keyword matching in `suggest_entity_icon()` and `_collect_label_keys()` now
  prefers the longest matching keyword instead of the first one found in
  dict insertion order. Previously a generic keyword (e.g. "power") could
  silently shadow a more specific compound word (e.g. "powerwall") that
  contains it as a substring, giving the entity the wrong icon or the wrong
  label priority under the `max_labels` cap — and since icons are only ever
  set once, the wrong icon stuck permanently. Fixes e.g.
  `sensor.tesla_powerwall_soc` getting `mdi:power` instead of
  `mdi:home-battery`. The fix applies regardless of the order future
  vocabulary batches get merged in.

## [0.9.86] - 2026-07-13

### Added
- Incremental vocabulary batch: 185 new keywords and 182 new icon mappings.
  Focus categories scenes, covers and security (mood/activity scenes like
  Filmabend/Guten Morgen/Neonparty/Lichtwecker; cover device types and brands
  like Raffstore/Kassettenrollo/Schnelllauftor/Somfy/Velux/Warema; security
  systems and terms like Glasbruchdetektor/Sabotage/Scharfschaltmodus and
  brands SimpliSafe/Frontpoint/Ring), plus a cross-domain icon batch and real
  device/platform synonyms from ZHA/KNX/Matter ecosystems (actuators, sensors
  and meters like Fluegelantrieb/Lueftungsaktor/Zweirichtungszaehler).

## [0.9.85] - 2026-07-13

### Added
- Incremental vocabulary batch: 107 new keywords and 96 new icon mappings.
  Focus categories water, switches and automations (irrigation and pool gear
  like Regentonne/Zisterne/Tauchpumpe/Rasensprenger/Versenkregner, water
  boilers and pumps; switch/actuator terms like Reedschalter/Halbleiterrelais/
  Zeitschaltuhr and plug/switch brands Tapo/Meross/Lutron/Third Reality/Leviton;
  automation logic like Zustandsautomat/Schrittkette/Boolean gates AND/OR/XOR,
  frost- and shading-automatics, ESPHome/Zigbee2MQTT triggers), plus device
  synonyms across lights, covers, network, media and other domains (mmWave
  presence, tubular/shade motors, EV wall connectors, mesh/network switches).

## [0.9.84] - 2026-07-13

### Added
- Incremental vocabulary batch: 140 new keywords and 140 new icon mappings.
  Focus categories vacuums, battery and light_level (robot vacuum brands like
  Coredy/Winbot/Mamibot/Neabot, ToF/AIVI/TrueDetect navigation, pet-hair and
  filter terms; home-battery brands Dyness/Pytes/Relion/Litime, BMS chips
  Daly/JK/Seplos, fuel-gauge ICs MAX17048/BQ27441, cell formats 4680/CR1632;
  ambient-light sensor ICs RPR0521/BH1780/TSL2585, lux-sensor brands and
  luminance/illuminance terms), plus device synonyms across media, climate,
  garden and other domains (incl. Alfen EV charger).

## [0.9.83] - 2026-07-13

### Added
- Incremental vocabulary batch: 209 new keywords and 206 new icon mappings.
  Focus categories fans, air_quality and network (extract/supply ventilation, cooker
  hoods and fan brands like Fantech/Hunter/Big Ass Fans; CO/CO2 sensor chips like
  CozIR/SenseAir, VOC/particulate/pollen/odour terms; VLAN, DNS, firewall, PoE, VPN
  and router brands like Tenda/EdgeRouter/SonicWall), plus an MDI icon-assignment
  pass across media, car, garden, security and locks, and a device-synonym pass adding
  common product terms (window handle, dimmer relay, presence sensor, pool pump,
  skylight motor, portable power station).

## [0.9.82] - 2026-07-13

### Added
- Incremental vocabulary batch: 136 new keywords and 124 new icon mappings.
  Focus categories automations, leak and updates (Node-RED node names, condition/
  error-handling and routine terms; gas/CO detector, damp and appliance-leak terms;
  firmware/patch/release-channel and package-signature terms), plus a device-synonym
  pass adding common product terms across covers, climate, appliances, network, car
  and switches (fancoil, sous-vide, managed switch, Type 2, OBD dongle, smart faucet).

### Added
- Incremental vocabulary batch: 145 new keywords and 146 new icon mappings.
  Focus categories motion, locks and cameras (PIR/mmWave/radar and presence-motion
  terms; smart-lock, deadbolt, cylinder and lock-brand terms like Nuki/Yale/Danalock;
  surveillance/IP/PTZ/doorbell-camera terms and brands like Reolink/Hikvision/UniFi/
  Frigate), plus 35 icon-only additions to existing device-synonym keywords
  (Aqara, IKEA Dirigera, Sonoff, Meross, Levoit and cover/lock/fan/valve terms).

## [0.9.80] - 2026-07-12

### Added
- Incremental vocabulary batch: 166 new keywords and 180 new icon mappings.
  Focus categories scripts, energy and waste (script/macro/routine and job
  scheduling terms; power-factor, meter, transformer, storage and forecast terms;
  compost, collection-day, recycling and hazardous-waste terms), plus a set of
  real device/platform synonyms and icon-only additions for existing keywords
  (fans, lights, appliances, media, garden and water devices) that previously
  fell back to their generic domain icon.

## [0.9.79] - 2026-07-12

### Added
- Incremental vocabulary batch: 167 new keywords and 165 new icon mappings.
  Focus categories temperature, cost and presence (room/sensor-IC/heating and
  beverage temperature terms; taxes, loan/interest, price and fee terms; mmWave
  radar hardware, network/BLE-tag presence and bed/seat occupancy), plus a set of
  real device/platform synonyms (Fibaro/Qubino/Danfoss/Somfy/Elero window and
  cover drives, Homematic/Nanoleaf/Govee/Innr lights, MyQ/Chamberlain garage
  doors, Danalock/ekey locks, Ubiquiti/Frigate cameras, Yamaha/WiiM media).

## [0.9.78] - 2026-07-12

### Added
- Incremental vocabulary batch: 204 new keywords and 198 new icon mappings.
  Focus categories shopping, scenes and humidity (grocery/delivery/restock and
  brand terms, light-scene/mood/routine names, humidity-sensor chips, hygrometer
  brands and room-moisture terms), a sweep of previously uncovered smart-home MDI
  icons, and real device/platform synonyms (balcony-power-plant storage, radon
  detectors, video door stations, Lutron Caseta/Pico, shunt/converter meters,
  wallbox enable, blackout blinds, gate/barrier drives, leak sensors).

## [0.9.77] - 2026-07-12

### Added
- Incremental vocabulary batch: 151 new keywords and 162 new icon mappings.
  Focus categories water, weather and light_level (rain/cistern/well/flow terms,
  hail/frost/dew-point/UV/pollen weather terms, lux/illuminance/ambient-light
  terms), a sweep of previously uncovered smart-home MDI icons, and real
  device/platform synonyms. Also added icons to 36 existing icon-less keywords
  (roller-shutter actuators, tube motors, relays, dual-tariff meters, thermal
  cameras, tamper contacts, Victron/Develco device names).

## [0.9.76] - 2026-07-12

### Added
- Incremental vocabulary batch: 148 new keywords and 114 new icon mappings.
  Focus categories media, updates and air_quality, plus real device/platform
  synonyms (Aqara/Eve/IKEA/tado/Shelly/Homematic/Eltako/Nodon switches, WLED/DALI
  lighting, window-handle brands, energy meters, home batteries, robot
  mowers/vacuums, AV/HiFi brands, air purifiers and ventilation units).

## [0.9.75] - 2026-07-12

### Added
- Incremental vocabulary batch: 173 new keywords and 149 new icon mappings.
  Focus categories fans, vacuums and battery, plus real device/platform
  synonyms (Aqara/Eve/IKEA/tado/Shelly/Homematic taster, dimmers, actuators,
  meter reading heads, radio motion/presence sensors etc.).

## [0.9.74] - 2026-07-12

### Added
- Incremental vocabulary batch: 126 new keywords and 142 new icon mappings.
  Focus categories security, waste and cost, plus device/platform synonyms
  (Ajax/Hikvision/Aqara/tado/Tradfri Dirigera/Nous/Tuya etc.) and icon-only
  mappings for 19 existing keywords that previously fell back to a generic icon.

## [0.9.73] - 2026-07-12

### Added
- Incremental vocabulary batch: 133 new keywords and 156 new icon mappings.
  Focus categories scripts, leak and climate, plus device/platform synonyms
  (ZHA/Matter/Aqara/Shelly/SIEGENIA etc.) and icon-only mappings for existing
  keywords that previously fell back to a generic icon.

## [0.9.72] - 2026-07-12

### Added
- Incremental vocabulary batch: 141 new keywords and 138 new icon mappings.
  Expanded the three smallest categories — `automations` (triggers, helpers,
  geofence/zone events, brand remotes), `locks` (smart-lock brands/models,
  cylinder and safe terms) and `temperature` (sensor ICs, degree-day and
  weather-day terms, process/junction temperatures) — plus real
  device/platform synonyms from Zigbee/Matter/brand ecosystems.



### Added
- Incremental vocabulary batch: 184 new keywords and 184 new icon mappings.
  Expanded the three smallest categories — `shopping` (groceries, payment
  methods, store types), `scenes` (mood/lighting/seasonal scenes) and
  `presence` (location, geofence, occupancy terms) — plus a batch of
  smart-home-relevant MDI icon mappings and real device/platform synonyms
  (Zigbee/Matter/brand device terms). Also filled icon gaps on existing
  keywords. Dropped the overly generic brand keyword `shelly` (ambiguous
  across relays, energy meters and dimmers).

## [0.9.70] - 2026-07-12

### Added
- Incremental vocabulary batch: 35 new keywords and 39 new icon mappings.
  Expanded the `cameras` category with brands, NVR/surveillance platforms and
  camera features (Frigate NVR, Scrypted, Nest Doorbell/Hello, Blink, Axis,
  Mobotix, Avigilon, thermal camera, object tracking, face database, etc.), and
  filled icon gaps on existing device keywords (akku, abwesenheit,
  aktualisierung, abfall, abgastemperatur, ac verbrauch).

## [0.9.69] - 2026-07-12

### Added
- Incremental vocabulary batch: 198 new keywords and 179 new icon mappings.
  Grew the three thinnest label categories (light_level, humidity, motion) with
  ambient-light/illuminance sensor chips (BH1750, TSL2591, OPT3001, VEML6031,
  APDS9007, LTR-series, etc.), humidity terms and sensor models (SHT41/45, DHT20,
  HTU31, SwitchBot/Ecowitt/Netatmo modules), and mmWave/PIR/radar motion terms
  and devices (LD2411/2461, Panasonic Grid-EYE, Aqara/Sonoff/Zooz presence).
  Added device/platform synonyms from real Zigbee/Matter ecosystems plus a batch
  of previously unused Material Design Icons for smart-home concepts.

## [0.9.68] - 2026-07-12

### Added
- Incremental vocabulary batch: 132 new keywords and 127 new icon mappings.
  Grew the three thinnest label categories: vacuums (robot-vacuum brands/models,
  accessories like brush rolls, mop pads, dust bags, suction turbines, cleaning
  and maintenance terms, navigation/cleaning modes, and error/status states such
  as stuck/tangled/tipped-over/bin-full/dock-lost), updates (firmware/software
  versioning, release channels like stable/beta/nightly, HA-specific update terms
  for core/supervisor/os/addon, and update states like installing/pending-reboot),
  and air_quality (pollutants and gases — formaldehyde, benzene, PM1/PM2.5/PM10,
  NOx/TVOC — air-purifier terms, pollen/allergens, AQI/CAQI indices, and air-quality
  sensor brands like Airthings/Awair/uHoo). Also added real device/platform synonyms
  from smart-home ecosystems (Aqara, Shelly, Eve, tado, IKEA/Tradfri, ZHA/Matter),
  and enriched 13 existing keywords with dedicated icons (e.g. giesscomputer,
  ozonsensor, wegeleuchte, einspeisezaehler, schluesseltresor).

## [0.9.67] - 2026-07-12

### Added
- Incremental vocabulary batch: 154 new keywords and 145 new icon mappings.
  Grew the three thinnest label categories: battery (cell chemistries like
  LiFePO4/NMC/LTO/sodium-ion, UPS/backup-power terms, coin-cell formats,
  kWh storage/inverter batteries, SoC/DoD/cycle-count metrics, super/ultra
  capacitors), weather (meteorological terms — dew point, fronts, pressure
  tendency, precipitation types, gusts, cloud ceiling, advisories) and media
  (streaming platforms/renderers like Bluesound/Navidrome/Music Assistant/
  DLNA renderer plus AV playback terms — subtitles, audio track, playlist,
  channel list, speaker groups). Also added real device/platform synonyms from
  ZHA/Zigbee2MQTT/Matter ecosystems (Sonoff ZBMINI, mmWave 24/60 GHz presence,
  SMA/Huawei/E3DC/SENEC/sonnen inverters and storage, universal actuators,
  tank/cistern level sensors, CO2/PM10 meters, phase switching).

## [0.9.66] - 2026-07-12

### Added
- Incremental vocabulary batch: 191 new keywords and 186 new icon mappings.
  Grew the three thinnest label categories: leak (burst-pipe / hose / siphon /
  boiler-tank / condensate-drain / sump-pump leak terms plus Gigaset/Eqiva/
  Sonoff/Dragino water sensors), cost (tariff / budget / kWh-price / billing /
  price-forecast terms) and fans (supply/exhaust dampers, room/basement/garage
  ventilation, workshop/PC/aquarium fans, fan controllers, EC/radial/axial
  blowers). Added real device/platform synonyms from ZHA/Zigbee2MQTT/Matter
  ecosystems (Aqara/Eve/Moes/Tuya roller shutters, Becker/Jarolift/Rademacher
  motors, Bosch/Danfoss/Moes radiator thermostats, Homematic/Bosch switches and
  wall transmitters, presence/smoke/contact sensors) and mapped previously
  unused MDI icons to smart-home terms (phone/call-list states, home/property
  presence, parental-control media locks, network keys).

### Added
- Incremental vocabulary batch: 180 new keywords and 172 new icon mappings.
  Grew the three thinnest label categories: waste (bin/collection/recycling
  and disposal-app terms), scripts (sequence/routine/procedure/macro names),
  and water (sprinkler/valve/pump types, pressure tank, pond/well/hydrant/
  filter terms). Added real device/platform synonyms from ZHA/Zigbee2MQTT/
  Matter ecosystems (roller-shutter motors, glass/touch wall switches,
  radiator thermostats and actuators, window-contact/shock sensors, wallbox
  controllers, Zigbee bridges/sticks) and mapped previously unused MDI icons
  to smart-home terms (cloud sync states, lock add/remove, color picker,
  battery charge/discharge, turn-signal indicators).

### Added
- Incremental vocabulary batch: 168 new keywords and 141 new icon mappings.
  Grew the three thinnest label categories (temperature, cameras, scenes) with
  temperature sensor chips and thermometer/probe types (SHT40/MCP9808/TMP117,
  brewing/3D-printing/engine/oven probes), camera types and features (speed/
  mini/eyeball dome, varifocal, WDR/HDR, AI line-crossing and people counting,
  NVR/DVR recording, RTSP/H.265 streaming, PTZ, brands like Frigate/Scrypted/
  Mobotix/Axis/Nest), and scene/mood names (drink occasions, music/audio
  evenings, themed parties, times-of-day, cooking events). Added real
  cross-ecosystem device synonyms with icons from Zigbee/Matter/Aqara/Shelly/
  Eve catalogs (dew-point sensors, mop robots, presence detectors, phase-cut
  dimmers, door/window contacts, garden heat pumps, water shutoff valves).

## [0.9.63] - 2026-07-12

### Added
- Incremental vocabulary batch: 195 new keywords and 163 new icon mappings.
  Grew the three thinnest label categories (automations, motion, light_level)
  with trigger/condition/flow-node terms, mmWave/radar presence sensors and
  chips (LD2410/LD2450, mmWave, ToF, fall-detection radar), and lux/UV/
  illuminance terms. Added cross-category smart-home devices with icons
  (tools, kitchen items, car parts, groceries) and real ecosystem device
  synonyms (shutter/blind/curtain actuators, radiator actuators, metering
  plugs, valve controllers) from Zigbee/Matter/Aqara/Shelly/Eve catalogs.

## [0.9.62] - 2026-07-12

### Added
- Incremental vocabulary batch: 198 new keywords and 169 new icon mappings.
  Grew the three thinnest label categories (air_quality, switches, humidity)
  with air-purifier/particulate/VOC/pollen terms and sensor chips, smart
  switch/relay/plug brands and models (Shelly/Sonoff/Zooz/Inovelli/Tapo/
  Meross/Aqara), and humidity/hygrometer/dehumidifier/dew-point terminology.
  Added icon-driven device concepts from previously unused smart-home MDI
  icons and further real device/platform synonyms from ZHA/Matter/Zigbee
  ecosystems (Aqara/Eve/IKEA/tado/SIEGENIA/Tuya/SELVE tubular motors,
  handles, blinds, charging stations). All icons validated against the MDI
  metadata set (no invented names).

## [0.9.61] - 2026-07-12

### Added
- Incremental vocabulary batch: 128 new keywords and 138 new icon mappings.
  Grew the three thinnest label categories (vacuums, presence, updates) with
  robot-vacuum brands/parts/mopping terms, presence-detection systems
  (mmWave/ESPresense/LD2410) and away/arrival concepts, and firmware/OTA/
  version/release-channel terminology. Added real device/platform synonyms
  from ZHA/Matter/Zigbee ecosystems (Aqara/Eve/IKEA/tado/Shelly/SIEGENIA/
  Tuya window handles, dimmers, blinds, sirens, LED strips) and icon-only
  mappings for existing keywords that still fell back to a generic icon
  (fans, blinds, locks, doorbells, smoke detectors). All icons validated
  against the MDI metadata set (no invented names).

## [0.9.60] - 2026-07-12

### Added
- Incremental vocabulary batch: 175 new keywords and 81 new icon mappings.
  Grew the three thinnest label categories (weather, scripts, shopping) with
  rare weather phenomena/cloud types, automation-platform/routine terminology
  and delivery-service/grocery/pantry terms, added a batch of smart-home MDI
  icon-to-keyword mappings, plus real device/platform synonyms from
  ZHA/Matter/Zigbee ecosystems (Aqara U200/U300 & E1 locks, IKEA Fyrtur/
  Praktlysing blinds, SwitchBot curtain/lock/plug, Reolink/Eufy doorbells,
  SkyConnect/SLZB Zigbee coordinators, etc.). All icons validated against the
  MDI metadata set (no invented names).

## [0.9.59] - 2026-07-12

### Added
- Incremental vocabulary batch: 196 new keywords and 194 new icon mappings.
  Grew the three thinnest label categories (covers, fans, battery) with
  shutter/blind/awning/gate, ventilation/exhaust/blower and
  battery-chemistry/charge-state/power-station terminology, added a batch of
  smart-home MDI icon-to-keyword mappings, plus real device/platform synonyms
  from ZHA/Matter ecosystems (fingerbot, mmwave presence, valve actuators,
  keypad locks, etc.). All icons validated against the MDI metadata set (no
  invented names).

## [0.9.58] - 2026-07-11

### Added
- Incremental vocabulary batch: 162 new keywords and 155 new icon mappings.
  Grew the three thinnest label categories (cost, locks, leak) with
  tariff/billing/payment-provider, smart-lock/access-control/keypad and
  leak/flood/damp/gas-detector terminology, plus real device/platform
  synonyms from ZHA/Matter ecosystems. All icons validated against the MDI
  metadata set (no invented names).

## [0.9.57] - 2026-07-11

### Added
- Incremental vocabulary batch: 144 new keywords and 172 new icon mappings.
  Grew the three thinnest label categories (automations, water, waste) with
  workflow/trigger/blueprint, plumbing/flow/cistern and bin/recycling/disposal
  terminology. Added new MDI icon-to-keyword mappings and real device/platform
  synonyms (ZHA/Zigbee2MQTT, Matter, Aqara/Eve/IKEA/tado/Shelly/Tuya), including
  38 icon-only additions that give existing keywords (netflix, staubsauger,
  heizung, photovoltaikanlage, schalter, …) a fitting icon instead of the
  generic domain/label fallback.

## [0.9.56] - 2026-07-11

### Added
- Incremental vocabulary batch: 163 new keywords and 164 new icon mappings.
  Grew the three thinnest label categories (air_quality, humidity, temperature)
  with additional sensor chips/models, brand sub-models and pollutant/pollen,
  dew-point/mold and probe/thermostat terminology. Added real device and
  platform synonyms across covers, energy, car, temperature, light_level, fans
  and more (Aqara, Sonoff, Shelly, tado, SIEGENIA, KEBA, go-e, Marstek, Bosch,
  Tapo), plus 12 icon-only mappings for existing keywords that previously fell
  back to the generic domain icon.

## [0.9.55] - 2026-07-11

### Added
- Incremental vocabulary batch: 150 new keywords and 164 new icon mappings.
  Grew the three thinnest label categories (media, updates, scenes) with
  speaker/AV-receiver/streaming/multiroom media terms, firmware/OTA/release
  update vocabulary, and named scene/mood terms (seasonal, activity, focus and
  ambience scenes). Added real device and platform synonyms across covers,
  switches, motion, security, leak, water, car and climate (Aqara, Shelly,
  Tuya, Eve, tado, Homematic IP), plus 14 icon-only mappings for existing
  keywords that previously fell back to the generic domain icon.

## [0.9.54] - 2026-07-11

### Added
- Incremental vocabulary batch: 171 new keywords and 140 new icon mappings.
  Grew the three thinnest label categories (scripts, light_level, motion) with
  script/sequence/macro verbs, illuminance measurement terms (lux/lumen/EV and
  sensor chips), and presence/mmWave/PIR motion vocabulary, plus real device
  and platform synonyms across many themes (Shelly Plus, Aqara/Eve/IKEA leak
  and cover devices, Nuki/tedee locks, Homematic actuators, go-e/openWB
  chargers, SwitchBot curtain/bot, ratgdo).

## [0.9.53] - 2026-07-11

### Added
- Incremental vocabulary batch: 110 new keywords and 98 new icon mappings.
  Grew the three thinnest label categories (automations, cost, fans) with
  triggers/routines, energy tariff and billing terms, and ventilation/fan
  hardware, plus real device and platform synonyms across many themes
  (Hoppe handles, reed contacts, Warema, Hunter/Orbit irrigation, Bosch
  Twinguard/Spexor, Noctua/be quiet PC fans, Eve/Gledopto/Namron devices).

## [0.9.52] - 2026-07-11

### Added
- Incremental vocabulary batch: 175 new keywords and 202 new icon mappings.
  Filled out the three thinnest label categories (weather, cameras, presence)
  with device names, synonyms and meteorological terms, added real device/
  platform synonyms across many themes (IKEA Dirigera, ConBee, Sonoff, Nuki,
  Nanoleaf, Govee, tado, Dreame, Gardena), and enriched 45 existing keywords
  that previously fell back to the generic domain icon with specific MDI icons.

## [0.9.51] - 2026-07-11

### Added
- Incremental vocabulary batch: 45 new keywords and 29 new icon mappings.
  Focused on real device/platform synonyms across many themes — IKEA controllers
  (Rodret, Somrig, Parasoll, Skydrag, Inspelning), Aqara cubes, Sonoff SNZB
  sensors, Bosch Twinguard/Spexor, Shelly RGBW, Rademacher DuoFern, Schellenberg,
  Velux Active, Lupusec, FRITZ!DECT, and German installer terms (Aufputzaktor,
  Beschattungsaktor, Zwischensteckdose, Impulszaehler, Phasenabschnitt).

## [0.9.50] - 2026-07-11

### Added
- Incremental vocabulary batch: 171 new keywords and 146 new icon mappings.
  Focused on the three thinnest label themes (battery: cell chemistries, brands
  such as Ansmann/Zendure/Pylontech, discharge and capacity terms; shopping:
  German grocery-delivery services, pantry staples, checkout and deposit-machine
  terminology; vacuums: robot/handheld vacuum models from Roborock/Dreame/Eufy/
  iRobot, nozzles, filters and mopping features) plus real device/platform
  synonyms across many themes (mmWave presence radar, mesh nodes, DIN-rail
  relays, blinds, radiators and more).

## [0.9.49] - 2026-07-11

### Added
- Incremental vocabulary batch: 193 new keywords and 171 new icon mappings.
  Focused on the three thinnest label themes (humidity: hygrometer/sensor
  models and dampness terms such as Taupunktunterschreitung, Adsorptionstrockner
  and specific-humidity vocabulary; waste: bin/collection terminology including
  Abrollcontainer, Wertstoffsack, kerbside recycling and bottle bank; leak:
  water/freeze-alarm devices and brands such as Flo by Moen, LeakBot, YoLink,
  Rueckstauventil and Rohrfrostschutz), plus a curated batch of previously
  unused Material Design Icons and real device/platform synonyms across many
  themes (Versenkregner, Rohrventilator, Nachtspeicher, Radonsensor).

## [0.9.48] - 2026-07-10

### Added
- Incremental vocabulary batch: 161 new keywords and 138 new icon mappings.
  Focused on the three thinnest label themes (locks: smart-lock brands and
  hardware such as Nuki, Tedee, Danalock, Schliesszylinder and Fingerprint-
  Schloss; water: softener, cistern, well-pump and drinking-water vocabulary
  including Wasserenthaerter, Zisterne and Osmoseanlage; air_quality: CO2,
  VOC, particulate, pollen and radon terms such as Feinstaub, Pollenflug and
  Radonmessung), plus a curated batch of Material Design Icons for
  previously icon-less entries across many themes, and real device/platform
  synonyms and icon-only additions for existing brand keywords (Zigbee2MQTT
  TRVZB, Matter smoke sensors, Ecobee/Hive/Drayton thermostats, Hekatron,
  Griesser/Tahoma covers).

## [0.9.47] - 2026-07-10

### Added
- Incremental vocabulary batch: 159 new keywords and 108 new icon mappings.
  Focused on the three thinnest label themes (scripts: script naming and
  execution/trigger vocabulary; updates: firmware/OTA, release-channel and
  HACS/add-on update terminology; temperature: appliance/CPU/floor/flow-return
  measurement points and sensor hardware such as DS18B20, PT100 and ESPHome),
  plus a curated batch of Material Design Icons for previously icon-less
  entries across many themes, and real device/platform synonyms and
  icon-only additions for existing brand keywords (Homematic IP, Philips
  Hue Go/Iris/Play, Ledvance, Fibaro, Shelly Plus/Addon, Moes, Xiaomi,
  Somfy Protect, Trust Zigbee).

## [0.9.46] - 2026-07-10

### Added
- Incremental vocabulary batch: 137 new keywords and 157 new icon mappings.
  Focused on the three thinnest label themes (automations: trigger/routine
  vocabulary such as automationsverlauf, tuerklingeltrigger, notfallautomation
  and hysterese regel; motion: PIR hardware and mounting variants like
  fresnellinse, walktest and dual technology sensor, plus location-specific
  motion sensors for haustuer, vordach and carport; scenes: mood/scene naming
  vocabulary for dinner, wellness, night-sky and holiday moments such as
  gluehweinstimmung, sternenhimmel szene and kinonacht), plus a curated batch
  of Material Design Icons for previously icon-less entries across climate,
  garden, security, network, shopping, cost, waste, weather, lights,
  air_quality, energy and car, and icon-only additions for existing brand
  and device-synonym keywords (Arlo, Bose, Eufycam, Govee, Tasmota, Yale,
  Danalock and Aqara/IKEA/SIEGENIA/Tado device terms) that previously fell
  back to a generic icon.

## [0.9.45] - 2026-07-10

### Added
- Incremental vocabulary batch: 127 new keywords and 102 new icon mappings.
  Focused on the three thinnest label themes (cost: off-peak/dynamic-tariff
  market terms such as Schwachlast, Regelenergie, Bilanzkreis, Netzausbauumlage,
  and English billing terms like time of use, peak pricing, arrears, autopay,
  plus dynamic-tariff supplier names Corrently, Ostrom, Rabot, EnBW, Yello;
  vacuums: mop hardware parts, map import/export and room-segmentation terms,
  vendor features like sonic mopping and auto water refill station, and
  budget brands Mova and Lefant; fans: KWL/MVHR ventilation-system brands
  such as Lunos, Inventer, Meltem, Wolf and Stiebel Eltron, portable-fan
  brands like Dreo, Duux and Klarstein, and heat-exchanger/filter component
  terms), plus a curated batch of Material Design Icons for previously
  icon-less entries across EV/car sensors, wireless charging, billing and
  finance, pool water chemistry, cellular/Wi-Fi security and media controls.

## [0.9.44] - 2026-07-10

### Added
- Incremental vocabulary batch: 63 new keywords and 44 new icon mappings.
  Focused on the three thinnest label themes (automations: rule-engine and
  trigger/condition terminology, IFTTT/webhook/pyscript integrations,
  presence and schedule triggers; scenes: mood and routine names such as
  reading light, work light, lounge mode, breakfast/dinner scenes; locks:
  lock/unlock states, keypad and fingerprint terms, Yale/August/Schlage/Abus/
  eQ-3 brand entries), plus real device/platform synonyms across several
  themes (EV chargers: Mennekes, ABL, go-e, EVBox; heating: Wolf; KNX-style
  switch/dimmer systems: Legrand, Hager, Busch-Jaeger; networking: Starlink,
  OpenWrt, UniFi, GL.iNet, Asus; covers: Jarolift, Griesser; appliances:
  Liebherr, V-ZUG, Siemens Home Connect, Neff; locks: eKey, Burg-Wächter;
  garden irrigation/robotic mowers: Hunter, Wolf-Garten, Orbit; and home
  battery/solar systems: Huawei FusionSolar, E3/DC, SENEC).

## [0.9.43] - 2026-07-10

### Added
- Incremental vocabulary batch: 137 new keywords and 140 new icon mappings.
  Focused on the three thinnest label themes (shopping: grocery expiry
  tracking, loyalty programs, returns/exchanges, quick-commerce apps and
  discount events; battery: battery chemistries/form factors, diagnostics
  terms like internal resistance and cell balancing, and backup power
  terms; presence: room/seat occupancy, pet tracking, NVR-based person
  detection such as Frigate/Doubletake/CompreFace, BLE beacons and
  geofencing), plus a curated batch of Material Design Icons for
  previously icon-less entries, and real device/platform synonyms from
  ZHA/Zigbee2MQTT/Matter catalogs and brands such as Aqara, Eve Systems,
  IKEA, tado, Shelly, SIEGENIA and Tuya.

## [0.9.42] - 2026-07-10

### Added
- Four missing native Home Assistant integration domains mapped to their
  category: `smlight` (Zigbee coordinator hardware) to network, `homewizard`
  (energy meters/plugs) to energy, `govee_light_local` to lights, and
  `music_assistant` to media.

## [0.9.41] - 2026-07-08

### Added
- Incremental vocabulary batch: 169 new keywords and 141 new icon mappings.
  Focused on the three thinnest label themes (air_quality: gas/odor
  terms, pollen types and air-quality sensor brands; light_level:
  illuminance/lux measurement, dusk/dawn and UV-radiation sensor terms;
  waste: waste-stream, recycling and collection-logistics terms), plus a
  curated batch of Material Design Icons for previously icon-less
  entries, and real device/platform synonyms from ZHA/Zigbee2MQTT/Matter
  catalogs and brands such as IKEA, Loxone, KNX, Gira, Sonoff, Chamberlain,
  Hörmann, Marantec, Elero, Becker, Somfy, Rademacher, WAREMA, Aeotec,
  Zooz, Inovelli, SmartThings, Wiser, bticino, Niko, ABB-Welcome and
  Xiaomi/Aqara.

## [0.9.40] - 2026-07-08

### Added
- Incremental vocabulary batch: 132 new keywords and 135 new icon mappings.
  Focused on the three thinnest label themes (updates: firmware signing,
  compatibility and support-lifecycle terms; leak: pipe/appliance/roof leak
  and smart shutoff-valve terms; humidity: hygrometer models, psychrometry
  terms and humidifier/dehumidifier brands), plus a curated batch of
  Material Design Icons for previously icon-less entries, and real device/
  platform synonyms from ZHA/Zigbee2MQTT/Matter catalogs and brands such as
  Aqara, Eve Systems, IKEA, tado, Shelly, SIEGENIA and Tuya, including
  icon-only additions for existing keywords that previously had no
  dedicated icon.

## [0.9.39] - 2026-07-08

### Added
- Incremental vocabulary batch: 171 new keywords and 122 new icon mappings.
  Focused on the three thinnest label themes (weather: weather station and
  forecast/phenomenon terms; switches: relay, actuator and smart-plug brand
  terms; scripts: routine/scenario/workflow terms), plus a curated batch of
  Material Design Icons for previously icon-less entries, and real device/
  platform synonyms from ZHA/Zigbee2MQTT/Matter catalogs and brands such as
  Aqara, Eve Systems, IKEA, tado, Shelly, SIEGENIA and Tuya (window handles,
  dimmer switches, pool pumps, EV charging stations, climate accessories).

## [0.9.38] - 2026-07-08

### Added
- Incremental vocabulary batch: 175 new keywords and 90 new icon mappings.
  Focused on the three thinnest label themes (fans: fan/ventilation brands
  and model names, speed/oscillation/tilt control terms, kitchen extractor
  hood and fault-alert terms; cameras: SD/cloud storage and privacy-zone
  terms, PTZ and zoom terms, doorbell/siren/two-way-audio terms, recording
  and resolution terms; media: podcast/audiobook/DAB+ terms, HDR/Dolby/DTS
  audio-format terms, room-correction and multiroom-audio terms, cable and
  headphone-connectivity terms), plus a curated batch of Material Design
  Icons for previously icon-less appliance/climate/car/garden/energy/
  battery/media/network/weather terms, and real device-ecosystem synonyms
  (Aqara, Eve Systems, IKEA TRADFRI, tado, Shelly, SIEGENIA, Tuya, Matter)
  including icon-only additions for existing keywords that previously had
  no dedicated icon (Gardena, Intercom, SmartThings, Nanoleaf, Somfy,
  Velux, Netatmo, Tuya).

## [0.9.37] - 2026-07-08

### Added
- Incremental vocabulary batch: 186 new keywords and 133 new icon mappings.
  Focused on the three thinnest label themes (motion: PIR/mmWave/radar
  presence-sensor terms, occupancy-vs-motion distinctions, motion-cooldown
  and clear-timeout terminology; water: water-meter/consumption/pressure
  terms, hot/cold-water and well/cistern/pool-level terms; temperature:
  indoor/outdoor, fridge/freezer, floor and water-temperature sensor terms,
  frost/heat-threshold phrasing), plus a curated batch of Material Design
  Icons for previously icon-less smart-home terms across multiple
  categories, and real device-ecosystem synonyms (Aqara, Eve Systems, IKEA
  TRADFRI, tado, Shelly, SIEGENIA, Tuya, Matter) including icon-only
  additions for existing keywords that previously had no dedicated icon.

## [0.9.36] - 2026-07-08

### Added
- Incremental vocabulary batch: 152 new keywords and 87 new icon mappings.
  Focused on the three thinnest label themes (vacuums: robotic mower brands
  and mop/lawn-robot synonyms; cost: contract types, fees/deadlines,
  dynamic/prepaid pricing terms; locks: fingerprint/keypad access terms,
  locksmith/emergency-unlock services, video doorbell), plus a curated batch
  of Material Design Icons for previously icon-less garden/energy/shopping/
  network/weather/media/car/appliance terms, and real device-ecosystem
  synonyms (Aqara, Eve Systems, IKEA, tado, Shelly, Matter, EV charging
  phase-switching terms) including icon-only additions for existing
  keywords that previously had no dedicated icon.

## [0.9.35] - 2026-07-08

### Added
- Incremental vocabulary batch: 183 new keywords and 125 new icon mappings.
  Focused on the three thinnest label themes (scenes: card-night, TV/crime-show,
  holiday and life-event mood terms, fire/outdoor and reading/lounge/bar
  ambience terms; presence: check-in/check-out and arrival/departure phrasing,
  workplace/school presence context, tracking terminology, travel-away
  context; covers: Somfy/Tahoma brand terms, garage door accessories,
  motor/drive terms, shading/awning accessories, curtain hardware and
  pleated-shade terms), plus a curated batch of Material Design Icons for
  previously icon-less garden/appliance/car/network/water/energy/media terms,
  and real device-ecosystem synonyms (Aqara, Bosch Smart Home, Homematic IP,
  IKEA TRADFRI, Tuya, Shelly, Matter) including one icon-only addition for an
  existing keyword that previously had no dedicated icon.

## [0.9.34] - 2026-07-08

### Added
- Incremental vocabulary batch: 158 new keywords and 131 new icon mappings.
  Focused on the three thinnest label themes (waste: regional bin-color and
  dialect terms, packaging-law and reusable-cup deposit terms, UK/AU
  disposal phrasing; automations: assistant-ecosystem routine terms,
  additional trigger/condition jargon, presence- and light-simulation
  terms; scripts: automation-app and platform names, batch/macro
  terminology), plus a curated batch of Material Design Icons for
  previously icon-less appliance/food/light/network terms, and real
  device-ecosystem synonyms (Shelly, IKEA TRADFRI, Matter, ZHA/Z2M,
  Homematic IP, Fibaro, Gardena, Velux, Philips Hue, Nuki) including
  icon-only additions for existing keywords (awning/blind/lock variants)
  that previously had no dedicated icon.

## [0.9.33] - 2026-07-08

### Added
- Incremental vocabulary batch: 193 new keywords and 149 new icon mappings.
  Focused on the three thinnest label themes (humidity: hygrometer/dehumidifier
  terms, condensation and mold-risk terms, greenhouse/plant humidity terms;
  battery: coin-cell/battery-type designations, low-battery warning terms in
  German and English, per-device battery terms for remotes/smoke detectors/
  door-window sensors; light_level: lux/illuminance terms, twilight and
  daylight sensor terms), plus a curated batch of Material Design Icons for
  previously icon-less smart-home terms (security, shopping, car, cost,
  media, air_quality and more), and real ecosystem device synonyms
  (Shelly/Aqara/Homematic IP/Eve/Tado/Tuya/Bosch/deCONZ/Somfy/Ring device and
  sensor names, plus icon-only completions for existing keywords that still
  fell back to generic label icons).

## [0.9.32] - 2026-07-07

### Added
- Incremental vocabulary batch: 178 new keywords and 136 new icon mappings.
  Focused on the three thinnest label themes (updates: firmware/OTA/patch and
  platform-specific update terms; leak: brand smoke/water/gas sensors and
  flooding/moisture-damage terms; shopping: delivery-service brands, pantry
  restocking and low-stock terms), plus a curated batch of Material Design
  Icons for previously icon-less smart-home terms (vehicles, garden/farm,
  network/telephony, weather, security-unlock states), and real ecosystem
  device synonyms (ZHA/Matter/Aqara/Eve/IKEA/Shelly device and sensor names).

## [0.9.31] - 2026-07-07

### Added
- Incremental vocabulary batch: 170 new keywords and 144 new icon mappings.
  Focused on the two thinnest label themes (cameras: camera-hub brands,
  detection-event terms, doorbell/intercom and recording/privacy terms;
  air_quality: gas/smoke/combustion odor terms, pollen and allergen terms,
  air-quality-index and ventilation terms) plus a fans batch (KWL/ventilation
  abbreviations, PC/laptop fan terms, directional and pressure fan terms),
  a curated batch of Material Design Icons for existing smart-home terms
  (doorbell, molecule/gas, blinds, fence, water-boiler, Z-Wave/Zigbee), and
  real ecosystem device synonyms (SwitchBot, Qubino, Heatit, ESP32, storage
  heaters, waste-bin types, air purifiers/diffusers).

## [0.9.30] - 2026-07-07

### Added
- Incremental vocabulary batch: 162 new keywords and 137 new icon mappings.
  Focused on the three thinnest label themes (cost: billing/tariff/tax/
  banking terms; vacuums: robot-vacuum brand, mopping, and mapping/no-go-zone
  terms; temperature: sensor brand names, industrial/food cold-chain and
  probe thermometer terms), plus a batch of Material Design Icons for
  existing lights/appliances/locks/security/energy/vacuums/covers terms,
  and real ecosystem device synonyms (Aqara/Shelly/Sonoff/Xiaomi/Tuya/Moes
  temperature sensors and TRVs, window/door hardware, garage lock terms).

## [0.9.29] - 2026-07-07

### Added
- Incremental vocabulary batch: 113 new keywords and 89 new icon mappings.
  Focused on the three thinnest label themes (locks, scripts, water: door/gate
  lock hardware and smart-lock brand synonyms, script/routine/condition-block
  automation terms, pool/irrigation/water-treatment device terms), plus real
  ecosystem device synonyms (Fibaro keyfob/smoke sensor, Matter fan/lock/valve,
  Nuki bridge/opener, Velux/Roto window covers, reed switch, staircase light
  switch) and a small set of curated Material Design Icons for media playback
  and network/cover states.

## [0.9.28] - 2026-07-07

### Added
- Incremental vocabulary batch: 144 new keywords and 124 new icon mappings.
  Focused on the three thinnest label themes (battery, media, automations:
  battery chemistry/charging/backup-power terms, streaming/audio-zone/
  media-player terms, automation trigger/condition/blueprint terms), plus a
  batch of Material Design Icons for existing and new smart-home terms
  (appliances, weather, security, network), and real-world device synonyms
  (water softener, dehumidifier, air fryer, anemometer, rain sensor, EV
  charging port/flap, Matter window contact/dimmer/lock, ZHA coordinator,
  sump pump, rainwater harvesting, garage door sensor).

## [0.9.27] - 2026-07-07

### Added
- Incremental vocabulary batch: 177 new keywords and 136 new icon mappings.
  Focused on the three thinnest label themes (waste, scenes, switches:
  garbage/recycling/collection-schedule terms, mood/occasion/time-of-day
  scene terms, relay/dimmer/wall-switch/power-strip terms), plus a batch of
  Material Design Icons for existing and new smart-home terms (animals,
  garden/agriculture, food, tools, solar/wind energy, weather, automotive),
  and real-world ZHA/Matter/brand device synonyms (Somfy, Rademacher, Velux,
  Danfoss, Netatmo, Sonoff, deCONZ, Hue, LIFX, innr, Paulmann, Homematic,
  Jung, Gira, SIEGENIA, Zigbee coordinator/dongle, Z-Wave stick, Thread,
  HomeKit bridge, EVSE), including 12 icon-only additions for existing
  keywords that had no specific icon yet (gateway, homebridge, hubitat,
  drehschalter, chlorpumpe, durchflussmelder, erdgasmelder,
  fehlerstromschutzschalter, bodenroboter, hacs repository,
  beschleunigungssensor, footstep sensor).
  Keyword vocabulary: 7,877 → 8,054. Icon mappings: 4,569 → 4,705.

## [0.9.26] - 2026-07-07

### Added
- Incremental vocabulary batch: 186 new keywords and 131 new icon mappings.
  Focused on the three thinnest label themes (light_level, leak, shopping:
  lux/illuminance/twilight-sensor terms, water-leak/flood/moisture-detector
  and pump/backup-water terms, shopping-list/order-tracking/delivery/
  discount terms), plus a batch of Material Design Icons for existing and
  new smart-home terms, and real-world ZHA/Matter/brand device synonyms
  (Aqara/tado/Shelly/Tuya/IKEA device names, EV charging synonyms, AC
  indoor/outdoor units, dimmer modules), including 2 icon-only additions
  for existing keywords (conbee, deconz) that had no specific icon yet.
  Keyword vocabulary: 7,691 → 7,877. Icon mappings: 4,438 → 4,569.

## [0.9.25] - 2026-07-07

### Added
- Incremental vocabulary batch: 208 new keywords and 123 new icon mappings.
  Focused on the three thinnest label themes (updates, humidity, motion:
  firmware/OTA/patch-notification terms, humidity/dehumidifier/dew-point/
  mold-warning terms, PIR/mmWave/motion-detection terms), plus a batch of
  Material Design Icons for existing and new smart-home terms, and
  real-world ZHA/Matter/brand device synonyms (window handles, pool/pump
  hardware, dimmer modules, vibration/lux sensors), including 9 icon-only
  additions for existing keywords that had no specific icon yet.
  Keyword vocabulary: 7,483 → 7,691. Icon mappings: 4,315 → 4,438.

## [0.9.24] - 2026-07-07

### Added
- Incremental vocabulary batch: 185 new keywords and 171 new icon mappings.
  Focused on the three thinnest label themes (presence, fans, cameras:
  occupancy/away-mode terms, fan speed/oscillation/exhaust terms,
  doorbell/NVR/PTZ/night-vision camera terms), plus a batch of Material
  Design Icons for existing and new smart-home terms, and real-world
  ZHA/Matter/brand device synonyms (window handles, pool/irrigation/garden
  hardware, sauna/infrared heating, pet doors, wildlife cameras).
  Keyword vocabulary: 7,298 → 7,483. Icon mappings: 4,144 → 4,315.

## [0.9.23] - 2026-07-07

### Added
- Incremental vocabulary batch: 150 new keywords and 96 new icon mappings.
  Focused on the three thinnest label themes (temperature, scripts,
  air_quality: thermometer/probe/outdoor-temp terms, script/routine/scene
  automation terms, air quality/pollen/particulate/mold/allergen terms),
  plus a batch of Material Design Icons for existing and new smart-home
  terms not yet mapped to a specific icon.
  Keyword vocabulary: 7,148 → 7,298. Icon mappings: 4,048 → 4,144.

## [0.9.22] - 2026-07-07

### Added
- Incremental vocabulary batch: 188 new keywords and 156 new icon mappings.
  Focused on the three thinnest label themes (locks, cost, vacuums:
  door/window handle and access-control hardware terms, tariff/billing/
  invoice/rebate terms, robot vacuum docking/mopping/mapping terms),
  plus a batch of Material Design Icons for existing and new smart-home
  terms, real-world ZHA/Matter/brand device synonyms, and icon-only
  additions for existing keywords that previously fell back to generic
  icons (e.g. air conditioner, wallbox plug, Aqara/repeater).
  Keyword vocabulary: 6,960 → 7,148. Icon mappings: 3,892 → 4,048.

## [0.9.21] - 2026-07-07

### Added
- Incremental vocabulary batch: 122 new keywords and 76 new icon mappings.
  Focused on the three thinnest label themes (covers, waste, battery:
  awning/shutter/blind/gate-motor brand and mechanism terms, waste
  collection/recycling/bin terms, battery health/charge-planning/backup
  terms), plus real-world ZHA/Matter/brand device synonyms (TRADFRI,
  Homematic, Bosch Spexor, tado) and icon-only additions for existing
  keywords that previously fell back to generic icons.
  Keyword vocabulary: 6,838 → 6,960. Icon mappings: 3,816 → 3,892.

## [0.9.20] - 2026-07-07

### Added
- Incremental vocabulary batch: 142 new keywords and 121 new icon mappings.
  Focused on the three thinnest label themes (leak, humidity, scenes:
  water-leak/flood/shutoff-valve sensor terms, hygrometer/dehumidifier/
  soil-moisture/dew-point terms, mood/scene naming conventions like
  movie-night, bedtime, and wake-up scenes), plus another batch of
  Material Design Icons for existing and new smart-home terms across
  multiple labels.
  Keyword vocabulary: 6,696 → 6,838. Icon mappings: 3,695 → 3,816.

## [0.9.19] - 2026-07-06

### Added
- Incremental vocabulary batch: 171 new keywords and 119 new icon mappings.
  Focused on the three thinnest label themes (light_level, shopping,
  automations: brightness/dimming/lux terms, shopping-list/grocery/receipt
  terms, automation/blueprint/routine-engine terms), another batch of
  Material Design Icons for existing and new smart-home terms across
  multiple labels, and real-world ZHA/Matter/brand device synonyms (Shelly,
  Tuya, IKEA, Aqara, Eve Systems, tado, SIEGENIA, Gardena) including icon
  additions for existing keywords that previously had none.

## [0.9.18] - 2026-07-06

### Added
- Incremental vocabulary batch: 156 new keywords and 131 new icon mappings.
  Focused on the three thinnest label themes (fans, water, scripts:
  ventilation/exhaust-fan/blower brand and speed-stage terms, water/moisture/
  flow/pool/aquarium sensor and device terms, script/scene/routine naming
  conventions), another batch of Material Design Icons for existing and new
  smart-home terms across multiple labels, and real-world ZHA/Matter/brand
  device synonyms (IKEA, Shelly, Tuya, Aqara, tado, Eve Systems, SIEGENIA,
  Hue, deCONZ/Sonoff hardware, plus generic German device terms like
  Drehdimmer and Salzwasserchlorinator).
  Keyword vocabulary: 6,369 → 6,525. Icon mappings: 3,445 → 3,576.

## [0.9.17] - 2026-07-06

### Added
- Incremental vocabulary batch: 147 new keywords and 128 new icon mappings.
  Focused on the three thinnest label themes (motion, switches, updates:
  sensor/detection/mounting-location terms, timing/contactor/relay and
  brand-specific smart-plug terms, release-channel and package/registry
  terms), another batch of Material Design Icons for existing and new
  smart-home terms across multiple labels, and real-world ZHA/Matter/brand
  device synonyms (door viewers, seatbelt retractors, dishwashers, tankless
  water heaters, irrigation computers, pool cover motors, and more) plus
  icon-only additions for existing keywords that previously fell back to
  generic label icons.

## [0.9.16] - 2026-07-06

### Added
- Incremental vocabulary batch: 172 new keywords and 140 new icon mappings.
  Focused on the three thinnest label themes (cost, temperature, cameras:
  tariffs/billing/rebate terms, core/regulator/freeze-protection temperature
  terms, location-specific and pet cameras with lens/mount/power vocabulary),
  another batch of Material Design Icons for existing and new smart-home
  terms (appliances, presence, car, garden, media, lights, energy, battery,
  weather, network), and real-world ZHA/Matter/brand device synonyms (EV
  charger brands, robot lawn mower brands, IKEA smart-home product lines,
  universal-remote/IR-hub brands, curtain motor and irrigation brands). Also
  added icon-only mappings for existing keywords that previously fell back
  to the generic domain icon (rasierer, rasierapparat, elektrorasierer,
  shaver, electric shaver).
  Keyword vocabulary: 6,024 → 6,196. Icon mappings: 3,177 → 3,317.

## [0.9.15] - 2026-07-06

### Added
- Incremental vocabulary batch: 177 new keywords and 138 new icon mappings.
  Focused on the three thinnest label themes (air_quality, waste, vacuums:
  pollen/particulate matter, waste collection apps and recycling terms,
  robot vacuum brands/models and mopping/mapping features), another batch
  of Material Design Icons for existing and new smart-home terms (garden,
  leak, security), and real-world ZHA/Matter/brand device synonyms (window
  shutters/blinds, door/glass-break sensors, pumps, extractor fans). Also
  added icon-only mappings for existing keywords that previously fell back
  to the generic domain icon (fensterladen, fensterrollo, doppelrollo,
  raffstores, riegelschloss, gasleckmelder, heizungspumpe, kondensatpumpe,
  circulator pump, door sensor, extractor fan, bathroom extractor fan,
  glasbruchsensor, garagenluefter, bewegungsmelder, poolleck).
  Keyword vocabulary: 5,847 → 6,024. Icon mappings: 3,039 → 3,177.

## [0.9.14] - 2026-07-06

### Added
- Incremental vocabulary batch: 157 new keywords and 153 new icon mappings.
  Focused on the three thinnest label themes (automations, presence, locks),
  another batch of Material Design Icons for existing and new smart-home
  terms (garden, car, network, energy, battery, presence, lights, weather,
  appliances, water, covers, security, switches, climate, media, cost,
  leak), and real-world ZHA/Matter/brand device synonyms (Shelly, IKEA
  SYMFONISK, Aqara, SIEGENIA, Nord Pool). Also added icon-only mappings for
  existing keywords that previously fell back to the generic domain icon
  (doppeltaster, drucktaster, taster, wassersensor, tuerkontakt, tuerriegel,
  lever lock, shelly blu, ikea symfonisk, aqara w100, kontaktgrill, reverse
  osmosis, nordpool, siegenia drive axxent).
  Keyword vocabulary: 5,690 → 5,847. Icon mappings: 2,886 → 3,039.

## [0.9.13] - 2026-07-06

### Added
- Incremental vocabulary batch: 191 new keywords and 113 new icon mappings.
  Focused on the three thinnest label themes (light_level, humidity, scenes),
  another batch of Material Design Icons for existing and new smart-home
  terms (garden, car, weather, energy, appliances, lights, water, security,
  air quality), and real-world ZHA/Matter/brand device synonyms (Aqara,
  Shelly, Eve Systems, IKEA, tado, Danfoss, window handle/contact sensors).
  Keyword vocabulary: 5,499 → 5,690. Icon mappings: 2,773 → 2,886.

## [0.9.12] - 2026-07-06

### Added
- Incremental vocabulary batch: 196 new keywords and 137 new icon mappings.
  Focused on the three thinnest label themes (battery, shopping, leak),
  another batch of Material Design Icons for existing and new smart-home
  terms (covers, lighting, network, produce, tools, phones), and real-world
  ZHA/Matter/brand device synonyms (Zooz, Tuya, SmartThings, LeakSmart, Eve
  Systems, irrigation and pool equipment, air quality sensors).
  Keyword vocabulary: 5,303 → 5,499. Icon mappings: 2,636 → 2,773.

## [0.9.11] - 2026-07-06

### Added
- Incremental vocabulary batch: 147 new keywords and 139 new icon mappings.
  Focused on the three thinnest label themes (updates, scripts, fans),
  another batch of Material Design Icons for vehicles/transport, tools and
  garden terms, and real-world ZHA/Matter/brand device synonyms (inverters,
  battery storage, pool equipment, cover/window controls, air quality).
  Also added icon-only mappings for existing keywords that previously fell
  back to the generic domain icon (wechselrichter, hausspeicher, feinstaub,
  griffschloss, poolabdeckung, rollladenposition, hutschienenaktor).
  Keyword vocabulary: 5,156 → 5,303. Icon mappings: 2,497 → 2,636.

## [0.9.10] - 2026-07-06

### Added
- Incremental vocabulary batch: 177 new keywords and 148 new icon mappings.
  Focused on the three thinnest label themes (water, vacuums, motion),
  another batch of Material Design Icons for existing and new smart-home
  terms, and real-world ZHA/Matter/brand device synonyms (Aqara, Eve
  Systems, IKEA, tado, Shelly, SIEGENIA, Tuya, Bosch, Fibaro, Aeotec).
  Keyword vocabulary: 4,979 → 5,156. Icon mappings: 2,349 → 2,497.

## [0.9.9] - 2026-07-06

### Added
- Incremental vocabulary batch: 143 new keywords and 47 new icon mappings.
  Focused on the three thinnest label themes (temperature, cameras, cost),
  another batch of Material Design Icons for existing and new smart-home
  terms, and real-world ZHA/Matter/brand device synonyms (Aqara, Eve
  Systems, IKEA TRADFRI, tado, Shelly, SIEGENIA, Tuya). Also added
  icon-only mappings for existing keywords that previously fell back to
  the generic domain icon (fensterkontakt, eve door, shelly uni, range
  extender, innr, risco, beko, smeg, sesame, conga).
  Keyword vocabulary: 4,836 → 4,979. Icon mappings: 2,182 → 2,349.

## [0.9.8] - 2026-07-06

### Added
- Incremental vocabulary batch: 155 new keywords and 105 new icon mappings.
  Focused on the three thinnest label themes (motion, air_quality, switches),
  another batch of Material Design Icons for existing and new smart-home
  terms, and real-world ZHA/Matter/brand device synonyms (Aqara, Hue, IKEA
  Vallhorn, Sonoff, Reolink, Wyze, Tapo). Also added icon-only mappings for
  existing keywords that previously fell back to the generic domain icon
  (wandtaster, sonoff, reolink, wyze cam, tapo cam).
  Keyword vocabulary: 4,681 → 4,836. Icon mappings: 2,077 → 2,182.

## [0.9.7] - 2026-07-06

### Added
- Incremental vocabulary batch: 172 new keywords and 135 new icon mappings.
  Focused on the three thinnest label themes (light_level, waste, locks) and
  another batch of Material Design Icons for existing and new smart-home
  terms (appliance alarms, gate/shutter/sliding-door states, network signal
  strength, moon phases, and more). Also added lock-brand synonyms (August,
  Yale Linus, Schlage, Level Lock, Abus, Assa Abloy, Ring Alarm, Friday,
  Eufy, Wyze, Aqara, Sifely, RemoteLock, Salto Systems, Somfy Protect) and
  German waste-calendar-service terms (Abfall.io, Müllmax, AWIDO, RegioIT).
  Keyword vocabulary: 4,509 → 4,681. Icon mappings: 1,942 → 2,077.

## [0.9.6] - 2026-07-06

### Added
- Incremental vocabulary batch: 175 new keywords and 91 new icon mappings.
  Focused on the three thinnest label themes (scenes, leak, humidity), another
  batch of Material Design Icons, and real-world ZHA/Matter/brand device
  synonyms (Aqara, Eve Systems, IKEA, tado, Shelly, SIEGENIA, Tuya), including
  icon-only additions for existing keywords that previously fell back to the
  generic domain icon (rollladen, nas laufwerk, gartenteich, and others).
  Keyword vocabulary: 4,334 → 4,509. Icon mappings: 1,851 → 1,942.

## [0.9.5] - 2026-07-06

### Added
- Incremental vocabulary batch: 169 new keywords and 88 new icon mappings,
  focused on the three thinnest label themes (battery, scripts, fans),
  another batch of Material Design Icons, and real-world ZHA/Matter/brand
  device synonyms (Aqara, Tuya, Homematic IP, Husqvarna, Rademacher, and
  more), including icon-only additions for existing keywords that
  previously fell back to the generic domain icon (markise, ladekabel,
  schliesszylinder, and others). Keyword vocabulary: 4,165 → 4,334. Icon
  mappings: 1,763 → 1,851.

## [0.9.4] - 2026-07-05

### Fixed
- **Icon suggestions could permanently break Home Assistant's built-in
  per-state icons.** `lock`, `cover`, `valve`, `alarm_control_panel` and
  `vacuum` entities (and any `binary_sensor` with a `device_class`) get a
  different icon per state from HA core itself (locked/unlocked,
  open/closed, armed/disarmed, cleaning/docked, ...). A registry `icon`
  override always wins over that built-in logic, freezing the icon to one
  shape forever. `suggest_entity_icon()` now skips these entirely — no
  keyword match, however specific (e.g. "Eingangstür" naming a lock), can
  override them anymore. A plain `binary_sensor` with no `device_class`
  (many generic/quirky Zigbee sensors don't expose one) still gets a
  keyword icon, since HA shows one static icon there regardless of state
  anyway.

## [0.9.3] - 2026-07-05

### Added
- Real-world ZHA/Matter device coverage gaps closed: washing machine
  (icon only, label already existed), air conditioner (icon only), EV
  charger synonyms (`autolader`/`autoladestation`), generic PC power-plug
  monitoring (`computer`/`gaming pc`/`desktop pc`), smart window handles
  (`fenstergriff`/`fensterhaltegriff`/`window handle`) and dimmer switches
  (`dimmerschalter` + an icon for the existing `dimmer switch`).

## [0.9.2] - 2026-07-05

### Added
- 47 `lights` keywords that previously fell back to the generic domain
  icon (`mdi:lightbulb-group`) now get an icon matching their actual
  fixture type: bedside/pendant/table lamps, spotlights, night lights,
  LED strip/panel/matrix, pool and stair lighting, cabinet/sconce
  lighting, grow lights, and more.

## [0.9.1] - 2026-07-05

### Changed
- Trimmed the 0.9.0 sensor additions down to the ones actually worth their
  own entity: kept the 3 rolling-history sensors, dropped the 5
  config-overview sensors and the 2 stat sensors (`entities_with_area`,
  `custom_rule_matches` — still computed into `runtime.stats` for
  diagnostics, just not surfaced as entities) and merged the 2 error
  sensors into one (`last_error`, with `count` as an attribute).

### Fixed
- The Last run sensor's `sections` list never included `"icons"`, so a
  dedicated icons-scope/service run showed no diagnostics at all on that
  sensor (worse: the raw per-entity `changes` list leaked into its
  attributes unfiltered instead of being stripped like every other
  section). `icons_set` now also adds up icons set via a `labels` run and
  a dedicated `icons` run instead of only ever reading the former.

## [0.9.0] - 2026-07-05

### Added
- New run-scope options `Everything (labels + areas + icons)` and
  `Only icons`, backed by a full-registry `Organizer.assign_icons()` pass
  (and matching `assign_icons` service) that reaches every entity, not just
  ones that also matched a label — with an overwrite option instead of the
  previous "never touch an existing icon" rule.
- Three rolling-history sensors (survive restarts): last labeled, last
  grouped (area-assigned) and last icon-assigned entities, each showing the
  10 most recent changes across all runs/services.
- Config-overview sensors: effective language, max labels per entity, scan
  interval, exclude-pattern count, custom-rule count.
- Runtime-stat sensors: entities with area, custom-rule match count.
- Error tracking: error count since restart + last error message/timestamp,
  wired into every service call and the coordinator's run/cleanup/remove-all
  paths; also surfaced in diagnostics.

## [0.8.5] - 2026-07-05

### Added
- Fifth small incremental vocabulary batch: 149 new keywords and 67 new
  icon mappings, focused on the three thinnest label themes (automations,
  updates, vacuums) plus another batch of Material Design Icons.
  Keyword vocabulary: 4,007 → 4,156. Icon mappings: 1,637 → 1,704.

## [0.8.4] - 2026-07-05

### Added
- Fourth small incremental vocabulary batch: 153 new keywords and 85 new
  icon mappings, focused on the three thinnest label themes (motion,
  temperature, shopping) plus another batch of Material Design Icons.
  Keyword vocabulary: 3,854 → 4,007. Icon mappings: 1,552 → 1,637.

## [0.8.3] - 2026-07-05

### Added
- Third small incremental vocabulary batch: 122 new keywords and 64 new
  icon mappings, focused on the three thinnest label themes (scripts,
  leak, scenes) plus another batch of Material Design Icons. Keyword
  vocabulary: 3,732 → 3,854. Icon mappings: 1,488 → 1,552.

## [0.8.2] - 2026-07-04

### Added
- Second small incremental vocabulary batch: 98 new keywords and 82 new
  icon mappings, focused on the next three thinnest label themes
  (updates, humidity, light_level) plus another batch of Material
  Design Icons. Keyword vocabulary: 3,634 → 3,732. Icon mappings:
  1,406 → 1,488.

## [0.8.1] - 2026-07-04

### Added
- First run of the new small-batch incremental vocabulary process (see
  `/home/claude/vocab_tools/` — reusable validator + merger, collision
  sweep against DE/EN frequency corpora, real MDI icon validation): 92
  new keywords and 74 new icon mappings, focused on the three
  previously thinnest label themes (scripts, scenes, automations) plus a
  small batch of additional Material Design Icons. Keyword vocabulary:
  3,541 → 3,634. Icon mappings: 1,332 → 1,406.

## [0.8.0] - 2026-07-03

### Added
- Massive vocabulary expansion: keyword vocabulary grows from ~410 to
  **3,541 entries** (German + English), generated by a themed multi-agent
  pass over all 32 label categories, then filtered through automated
  validation (format rules, duplicate removal) and two independent
  collision sweeps (against German/English 50k-word frequency corpora,
  and against the new vocabulary itself) before merging. One weak mapping
  ("gaming pc" → network) was dropped after review; a handful of
  genuinely ambiguous words (e.g. "bremse", "verstaerker", "radar",
  "tamper", "brenner", "spiegel") were word-boundary-padded after the
  sweep caught real cross-label collisions (e.g. bare "radar" would have
  wrongly matched German weather-radar terms like "Regenradar").
- Icon coverage grows from 215 to **1,332 entries across 393 distinct
  icons**, built from a full pass over all Material Design Icons tagged
  as home-automation-relevant (~1,260 base icons), so most curated
  keywords now also suggest a specific icon, not just a label.
- All new icon names were validated against the live upstream MDI icon
  list. This also caught and fixed **3 pre-existing invalid icon names**
  from an earlier release (`mdi:cellphone-iphone`, `mdi:tablet-ipad`,
  `mdi:cellphone-android` don't exist in Material Design Icons) —
  replaced with the real `mdi:cellphone` / `mdi:tablet`.

### Fixed
- Several existing tests asserted "no label at all" for entities that,
  thanks to the new vocabulary, now correctly pick up an *additional*,
  legitimate label (e.g. an entrance camera now also gets "Sicherheit"
  via the existing "eingang" keyword). Updated those assertions to check
  for the absence of the originally-tested false positive specifically,
  rather than an empty result.

## [0.7.0] - 2026-07-02

### Added
- New **"Entities with icon"** diagnostic sensor — a persistent,
  registry-wide count of entities currently carrying one of the curated
  `SPECIFIC_ICONS` values, so the icon-suggestion feature is actually
  visible somewhere in the UI instead of only in a service-call response.
- The **Last run** sensor now surfaces `icons_set` as a top-level
  attribute (it was previously buried inside the nested `labels`
  attribute, easy to miss).

### Fixed
- The **Last run** sensor's `changes` list was stripped from the
  `labels`/`areas`/`cleanup` result sections but not from `remove_all`,
  so a `remove_all` run could leave a very large `changes` list sitting
  in that sensor's state attributes. Now stripped from every section,
  consistent with the diagnostics download.

### Docs
- README/info.md trimmed from 221 to ~100 lines — same facts, less prose
  (tighter tables, one usage example instead of six, shorter feature
  bullets).

## [0.6.0] - 2026-07-02

### Added
- New option **"Also set a more specific icon per entity"** (off by
  default). When enabled, entities that get a label from a run may also
  receive a more specific icon than the label's own generic one — e.g. a
  "Kaffeemaschine"/"coffee maker" gets `mdi:coffee-maker` instead of the
  generic Appliances icon, "Wohnzimmer TV" gets `mdi:television` instead
  of the generic Media icon. **Full coverage: all 32 label themes and all
  28 entity domains are guaranteed a specific icon** — every domain in
  `DOMAIN_LABELS` has its own `SPECIFIC_ICONS` entry (checked as an exact
  dict key, not a substring, so this carries zero collision risk), so
  `set_entity_icons` never leaves an entity without a suggestion just
  because its name has no recognizable keyword. Icon priority is now
  keyword/custom-rule > source integration (e.g. "spotify", "nuki" — the
  actual product) > device_class > bare domain, so a specific integration
  match correctly wins over its generic domain icon (e.g. a Spotify
  media_player gets `mdi:spotify`, not the generic `mdi:cast` every
  media_player would otherwise get). Covers 215 curated keywords/domains/
  device-classes/platforms (DE+EN synonyms) across 110 distinct icons —
  appliances (incl. printer, air purifier/
  humidifier, aquarium, pet feeder/litter box, whirlpool, kitchen scale),
  media, lights, locks, cameras (incl. plain vs. video doorbell), covers
  (incl. curtains), car/charging, garden, network (incl. NAS), climate
  (incl. radiator), weather (incl. frost/pollen/wind direction), security
  (incl. per-door-type icons for front/balcony/patio doors, CO detector),
  waste subtypes (recycling/organic), solar/home-battery, pool, presence
  (mobile devices, family group), and every remaining label theme that
  had zero icon differentiation before (automations, battery, cost,
  humidity, leak, light level, motion, scenes, scripts, shopping,
  switches, temperature, updates, vacuums).
- Never overwrites an icon that's already set (whether picked by the user
  or a previous run) — only fills in entities that have none yet.
- `RunResult` gained an `icons_set` count, surfaced via the `run` service
  response and the diagnostics.

### Docs
- README/info.md were rewritten to match the current feature set — they
  still described the early "labels only" version (2 services, ~4 curated
  themes) even though the integration now has 5 services, 32 label themes,
  408 keyword mappings, 116 curated integrations and icon suggestion.
  Added a full Options table, a services table with YAML examples for all
  five services, and an accurate Labels/Control-entities list.
- Considered renaming the integration given the expanded scope; decided
  against it. The domain identifier `auto_organizer` can't change without
  breaking every existing install (orphaned config entry, dead service
  calls), and "Entity Auto-Organizer" still accurately describes the
  product — "organizing" is Home Assistant's own umbrella term for
  labels/areas/floors, so covering areas and icons too doesn't strain the
  name. Only the stale docs needed fixing, not the name itself.

## [0.5.0] - 2026-07-01

### Added
- The options flow's "Exclude" field was a single free-text box requiring
  domains/entity_ids/patterns to be typed by hand. Replaced with two proper
  pickers: **"Exclude entire domains/groups"** (multi-select dropdown of
  every domain the rule engine understands) and **"Exclude individual
  entities"** (native entity picker with search). The old free-text field
  stays for advanced glob patterns (e.g. `sensor.test_*`) that the pickers
  can't express. All three sources are merged and de-duplicated.
- New `preview` service: dry-run labels *and* areas together in a single
  call, without needing to call `run`/`assign_areas` separately with
  `dry_run: true`.
- New options field **"Restrict to only these label themes"**: a
  multi-select dropdown listing every label in the catalog (Lights,
  Energy, Waste, Security, …). When any are picked, only those themes may
  ever be assigned — domain/device_class/integration/keyword matches for
  anything else are silently skipped. Leave empty (the default) for no
  restriction.

### Fixed
- The `run`/`cleanup`/`assign_areas`/`remove_all` **services** called the
  organizer directly and never updated the "Last run" sensor, coverage
  stats or diagnostics — only pressing the dashboard buttons did. Since the
  services are the documented way to trigger a run from automations, this
  meant the diagnostic sensors silently went stale for that usage pattern.
  Service calls now update the same shared runtime state as the buttons.
- The auto-label-new-entities debounce could pick up this integration's
  *own* button/select/switch/sensor entities (created during its own
  setup) and try to label them. Entities belonging to this integration's
  own platform are now skipped.
- The auto-label-new-entities debouncer wasn't shut down on unload/reload,
  so a pending 15s timer could fire after reload with stale state.
- `diagnostics.py` only stripped the (large) per-entity change list from
  the `labels`/`areas` result sections; `cleanup`/`remove_all` results kept
  their full list, which can be very large. Now stripped from every section.

### Changed
- A targeted `run(entity_filter=...)` (used by the auto-label-new
  debounce) now resolves the handful of entity_ids directly from the
  registry instead of scanning every entity, which matters once the
  registry has several thousand entries.
- The button/select/switch control entities are now `EntityCategory.CONFIG`
  (matching the existing diagnostic sensors) so they show up under
  "Configuration" on the device page instead of alongside real dashboard
  entities.

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
