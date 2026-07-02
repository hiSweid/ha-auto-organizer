# Entity Auto-Organizer for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Automatically assign [Labels](https://www.home-assistant.io/docs/organizing/labels/),
**Areas** and entity **Icons** to your Home Assistant entities from a rule
set — by **domain** (lights, switches, covers, …), **device class**
(temperature, motion, battery, energy, …) and curated **integration themes**
(32 label themes covering appliances, garden, network, car and more). No
cloud, no API keys, runs entirely local.

Hundreds of entities get sensible, consistent labels — and now areas and
icons too — in one click, ready to use in label-based automations,
dashboards and the entity filter. Labels default to **German**; English is
also available.

## Features

- 🏷️ Rule-based labeling by domain, device class and a keyword fallback (32 label themes, 400+ keyword mappings)
- 🚗 Curated integration themes for 100+ integrations, plus a car-keyword matcher
- 🎨 Creates labels with sensible colors and Material Design icons
- 🖼️ Optional **entity icon** suggestions — full coverage of all 32 label themes and all 28 entity domains, 215 curated mappings across 110 icons (never overwrites an icon you already set)
- 🌍 German (default) and English label names
- 🧹 Skips diagnostic/config entities by default to avoid noise (curated theme labels still apply)
- 🏠 Optional **area** and **floor** labels
- 📍 Optional bulk **area assignment** (own service, separate from labeling)
- 🎯 Restrict labeling to a chosen subset of label themes
- 🚫 Three ways to exclude entities: domain picker, entity picker, and free-text glob patterns
- 🧪 **Dry-run** mode and a dedicated `preview` service — see every change before anything is written
- ➕ **Merge** (default) or **overwrite** existing labels
- ⏱️ Optional run on startup and/or on a recurring interval
- ➕ Auto-labels newly created entities (debounced)
- ↩️ `cleanup` / `remove_all` services to strip labels again

## Installation

### HACS (custom repository)

[![Open in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=hiSweid&repository=ha-auto-organizer&category=integration)

1. HACS → ⋮ → *Custom repositories*
2. Add `https://github.com/hiSweid/ha-auto-organizer`, category **Integration**
3. Install *Entity Auto-Organizer*, then restart Home Assistant
4. *Settings → Devices & Services → Add Integration → Entity Auto-Organizer*

### Manual

Copy `custom_components/auto_organizer` into your `config/custom_components/`
directory and restart.

## Usage

After setup the integration registers **five services**:

| Service | Purpose |
| --- | --- |
| `auto_organizer.run` | Assign labels (optionally scoped to specific entities) |
| `auto_organizer.cleanup` | Remove labels this integration created |
| `auto_organizer.assign_areas` | Bulk-assign entities to areas |
| `auto_organizer.remove_all` | Remove **every** label in Home Assistant, not just managed ones |
| `auto_organizer.preview` | Always dry-run — returns labels *and* areas results, writes nothing |

```yaml
# Preview what would change — writes nothing
action: auto_organizer.run
data:
  dry_run: true

# Apply labels to everything
action: auto_organizer.run

# Limit to specific entities, and replace their labels instead of merging
action: auto_organizer.run
data:
  overwrite: true
  entities:
    - light.kitchen
    - sensor.aussentemperatur

# Remove every label this integration created
action: auto_organizer.cleanup

# Bulk-assign areas (respects the exclude settings from Options)
action: auto_organizer.assign_areas

# Wipe every label in Home Assistant (destructive — use dry_run first!)
action: auto_organizer.remove_all
data:
  dry_run: true

# Combined labels+areas preview in one call — always dry-run, always returns a result
action: auto_organizer.preview
```

`auto_organizer.run` returns a response with `scanned`, `updated`,
`labels_created`, `icons_set` and the per-entity `changes`, so you can
inspect the result in *Developer Tools → Actions*. `auto_organizer.cleanup`,
`auto_organizer.assign_areas` and `auto_organizer.remove_all` return the
matching result for their own scope. `auto_organizer.preview` always
returns `{"labels": ..., "areas": ...}` and never touches the registry.

Every write service (`run`, `cleanup`, `assign_areas`, `remove_all`) —
called directly or via the control buttons — updates the **Last run** /
**Last run time** sensors, including dry runs (nothing is written, but the
sensors still reflect that a run happened). Only `preview` leaves them
untouched.

## Options

Configurable under the integration's *Configure* button:

| Option | Default | Description |
| --- | --- | --- |
| Dry run | off | Compute changes without writing them |
| Overwrite | off | Replace existing labels instead of merging |
| Label by domain | on | Lights, switches, covers, … |
| Label by device class | on | Temperature, motion, battery, … |
| Label by source integration | off | Adds the raw integration platform name as a label |
| Curated theme labels | on | Integration themes + car-keyword matcher; applied even to diagnostic/config entities |
| Restrict to label themes | none (all allowed) | Multi-select — if set, only the chosen label themes are ever assigned |
| Auto-suggest entity icons | off | Sets a more specific icon when an entity has none yet; never overwrites an existing icon |
| Area labels | off | Add a label for each entity's area (own or via its device) |
| Floor labels | off | Add a label for the floor the entity's area belongs to |
| Skip diagnostic/config | on | Excludes diagnostic & config helper entities from domain/device-class/keyword/area/floor matching |
| Label language | `auto` | `auto` (follow Home Assistant), `de` or `en` |
| Max labels per entity | 2 (1–10) | Cap on labels assigned to one entity |
| Auto-label new entities | on | Label newly added entities automatically (15s debounce) |
| Run on startup | off | Run once when Home Assistant has finished starting |
| Re-scan interval | 0 | Minutes between automatic runs (0 = off) |
| Label prefix | — | Optional text prepended to every created label's name |
| Exclude domains | none | Dropdown — entity domains to fully exclude |
| Exclude entities | none | Entity picker — specific entities to fully exclude |
| Exclude (free text) | — | Comma/newline-separated exact domains, entity_ids, or `fnmatch` globs (e.g. `sensor.test_*`) |
| Custom rules | — | `keyword=label_key` per line; takes priority over the built-in keyword fallback |

All three exclude options are merged into one list — an entity matching any
of them gets no labels and no icon suggestion. Curated theme labels ignore
*Skip diagnostic/config* on purpose, since they're explicitly mapped and not
noisy.

Example — restrict to a few themes, auto-suggest icons, and exclude some
domains/entities via YAML options (equivalent of what the UI writes):

```yaml
enable_curated: true
enable_domain: true
enable_device_class: true
enabled_labels:
  - lights
  - climate
  - security
set_entity_icons: true
exclude_domains:
  - update
  - button
exclude_entities:
  - sensor.debug_uptime
exclude: "sensor.test_*"
```

## Control entities

The integration creates a device with everything you need to drive it from
the UI — no need to call services by hand:

**Controls**

- **Run now** (button) — runs according to the selected scope.
- **Run scope** (select) — *Labels + areas*, *Only labels* or *Only areas*.
- **Dry run** (switch) — when on, the buttons only preview (write nothing).
- **Cleanup labels** (button) — removes the labels this integration created.
- **Remove all labels** (button) — deletes *every* label in Home Assistant
  (not just the managed ones). Respects the *Dry run* switch.

**Sensors**

- **Last run** — number of entities changed by the last run/service call, with a scope (`labels`/`cleanup`/`areas`/`remove_all`) and details in its attributes.
- **Last run time** — timestamp of the last run/service call.
- **Labeled entities** / **Unlabeled entities** — entities with / without labels.
- **Entities without area** — entities lacking an area (own or via device).
- **Managed labels** — number of labels created by this integration.
- **Label coverage** — percentage of entities that carry at least one label, with a per-label breakdown in its attributes.

## Labels

32 label themes, in German (default) or English:

Functional (domain / device class): Beleuchtung, Schalter, Lüfter, Klima,
Rollläden, Schlösser, Staubsauger, Medien, Kameras, Szenen, Automationen,
Skripte, Anwesenheit, Wetter, Updates, Sicherheit, Temperatur,
Luftfeuchtigkeit, Batterie, Energie, Wasser, Helligkeit, Bewegung, Leck,
Luftqualität, Kosten.

Curated by integration/keyword: Haushaltsgeräte (appliances), Garten
(garden), Netzwerk & Server (network), Auto (car / charging), Einkauf
(shopping), Abfall (waste).

English names are used when the language option is set to `en`. Use
*Restrict to label themes* to limit assignment to a subset of these, and
*Custom rules* to add your own `keyword=label_key` mappings on top of the
~400 built-in keyword fallbacks.

## How it works

The rule set lives in [`rules.py`](custom_components/auto_organizer/rules.py)
as plain, language-keyed data (label catalog, domain/device-class/keyword/
integration/icon maps) and is applied by the engine in
[`organizer.py`](custom_components/auto_organizer/organizer.py), which
computes label specs, area assignments and icon suggestions per entity.
Labels created by the integration are marked internally so `cleanup` never
touches labels you made by hand.

## Contributing

Rule contributions are very welcome — extend the maps in `rules.py` and add a
case to `tests/test_rules.py`. The rule engine is pure and has no Home
Assistant dependency, so the tests run with plain `pytest -q`.

## License

[MIT](LICENSE)
