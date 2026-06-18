# Entity Auto-Labeler for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Automatically assign [Labels](https://www.home-assistant.io/docs/organizing/labels/)
to your Home Assistant entities based on a rule set — by **domain** (lights,
switches, covers, …) and **device class** (temperature, motion, battery,
energy, …). No cloud, no API keys, runs entirely local.

Hundreds of entities get sensible, consistent labels in one click, ready to use
in label-based automations, dashboards and the entity filter.

## Features

- 🏷️ Rule-based labeling by domain and device class (with keyword fallback)
- 🎨 Creates labels with sensible colors and Material Design icons
- 🧪 **Dry-run** mode — preview every change before anything is written
- ➕ **Merge** (default) or **overwrite** existing labels
- ⏱️ Optional run on startup and/or on a recurring interval
- 🧹 `cleanup` service removes only the labels this integration created
- 🌍 English & German translations

## Installation

### HACS (custom repository)

1. HACS → ⋮ → *Custom repositories*
2. Add `https://github.com/henrykhanke/ha-auto-labeler`, category **Integration**
3. Install *Entity Auto-Labeler*, then restart Home Assistant
4. *Settings → Devices & Services → Add Integration → Entity Auto-Labeler*

### Manual

Copy `custom_components/auto_labeler` into your `config/custom_components/`
directory and restart.

## Usage

After setup the integration registers two services:

```yaml
# Preview what would change — writes nothing
action: auto_labeler.run
data:
  dry_run: true

# Apply labels to everything
action: auto_labeler.run

# Limit to specific entities
action: auto_labeler.run
data:
  entities:
    - light.kitchen
    - sensor.outdoor_temperature

# Remove every label this integration created
action: auto_labeler.cleanup
```

`auto_labeler.run` returns a response with `scanned`, `updated`,
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
| Label by integration | off | Adds the source integration as a label |
| Run on startup | off | Run once when Home Assistant starts |
| Re-scan interval | 0 | Minutes between automatic runs (0 = off) |
| Label prefix | — | Optional prefix for created labels |

## How it works

The rule set lives in [`rules.py`](custom_components/auto_labeler/rules.py) as
plain data and is applied by the engine in
[`labeler.py`](custom_components/auto_labeler/labeler.py). Labels created by the
integration are marked internally so `cleanup` never touches labels you made by
hand.

## Contributing

Rule contributions are very welcome — extend the maps in `rules.py` and add a
case to `tests/test_rules.py`. Run the tests with `pytest -q`.

## License

[MIT](LICENSE)
