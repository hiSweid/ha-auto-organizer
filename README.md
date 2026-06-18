# Entity Auto-Organizer for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Automatically assign [Labels](https://www.home-assistant.io/docs/organizing/labels/)
to your Home Assistant entities from a rule set — by **domain** (lights,
switches, covers, …), **device class** (temperature, motion, battery, energy, …)
and curated **integration themes** (appliances, garden, network, car). No cloud,
no API keys, runs entirely local.

Hundreds of entities get sensible, consistent labels in one click, ready to use
in label-based automations, dashboards and the entity filter. Labels default to
**German**; English is also available.

## Features

- 🏷️ Rule-based labeling by domain, device class and a keyword fallback
- 🚗 Curated integration themes — appliances, garden, network, car
- 🎨 Creates labels with sensible colors and Material Design icons
- 🌍 German (default) and English label names
- 🧹 Skips diagnostic/config entities by default to avoid noise
- 🏠 Optional **area** and **floor** labels
- 🧪 **Dry-run** mode — preview every change before anything is written
- ➕ **Merge** (default) or **overwrite** existing labels
- ⏱️ Optional run on startup and/or on a recurring interval
- ↩️ `cleanup` service removes only the labels this integration created

## Installation

### HACS (custom repository)

1. HACS → ⋮ → *Custom repositories*
2. Add `https://github.com/henrykhanke/ha-auto-organizer`, category **Integration**
3. Install *Entity Auto-Organizer*, then restart Home Assistant
4. *Settings → Devices & Services → Add Integration → Entity Auto-Organizer*

### Manual

Copy `custom_components/auto_organizer` into your `config/custom_components/`
directory and restart.

## Usage

After setup the integration registers two services:

```yaml
# Preview what would change — writes nothing
action: auto_organizer.run
data:
  dry_run: true

# Apply labels to everything
action: auto_organizer.run

# Limit to specific entities
action: auto_organizer.run
data:
  entities:
    - light.kitchen
    - sensor.aussentemperatur

# Remove every label this integration created
action: auto_organizer.cleanup
```

`auto_organizer.run` returns a response with `scanned`, `updated`,
`labels_created` and the per-entity `changes`, so you can inspect the result in
*Developer Tools → Actions*.

## Options

Configurable under the integration's *Configure* button:

| Option | Default | Description |
| --- | --- | --- |
| Dry run | off | Compute changes without writing them |
| Overwrite | off | Replace existing labels instead of merging |
| Label by domain | on | Lights, switches, covers, … |
| Label by device class | on | Temperature, motion, battery, … |
| Curated theme labels | on | Appliances, garden, network, car (by integration) |
| Label by source integration | off | Adds the raw integration name as a label |
| Area labels | off | Add a label for each entity's area |
| Floor labels | off | Add a label for each entity's floor |
| Skip diagnostic/config | on | Ignore diagnostic & config helper entities |
| Label language | `de` | `de` or `en` |
| Run on startup | off | Run once when Home Assistant starts |
| Re-scan interval | 0 | Minutes between automatic runs (0 = off) |
| Label prefix | — | Optional prefix for created labels |

Curated theme labels apply even to diagnostic/config entities (they are
explicitly mapped, so noise is not a concern).

## Control entities

The integration creates a device with everything you need to drive it from the
UI — no need to call services by hand:

- **Run now** (button) — runs according to the selected scope.
- **Run scope** (select) — *Labels + areas*, *Only labels* or *Only areas*.
- **Dry run** (switch) — when on, the buttons only preview (write nothing).
- **Cleanup labels** (button) — removes the labels this integration created.
- **Last run** (sensor) — number of entities changed, with details (counts,
  scope, dry-run, timestamp) in its attributes.

## Labels

Functional (domain / device class):
Beleuchtung, Schalter, Lüfter, Klima, Rollläden, Schlösser, Staubsauger, Medien,
Kameras, Szenen, Automationen, Skripte, Anwesenheit, Wetter, Updates,
Sicherheit, Temperatur, Luftfeuchtigkeit, Batterie, Energie, Wasser, Helligkeit,
Bewegung, Öffnungen, Leck, Luftqualität, Kosten.

Curated by integration:
Haushaltsgeräte (appliances), Garten (garden), Netzwerk & Server (network),
Auto (car / charging).

English names are used when the language option is set to `en`.

## How it works

The rule set lives in [`rules.py`](custom_components/auto_organizer/rules.py) as
plain, language-keyed data and is applied by the engine in
[`labeler.py`](custom_components/auto_organizer/labeler.py). Labels created by the
integration are marked internally so `cleanup` never touches labels you made by
hand.

## Contributing

Rule contributions are very welcome — extend the maps in `rules.py` and add a
case to `tests/test_rules.py`. The rule engine is pure and has no Home Assistant
dependency, so the tests run with plain `pytest -q`.

## License

[MIT](LICENSE)
