# Entity Auto-Organizer for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

Automatically assigns [Labels](https://www.home-assistant.io/docs/organizing/labels/),
**Areas** and **Icons** to your entities — by domain, device class, and 400+
keyword/integration rules. Local only, no cloud, no API keys.

## Features

- 🏷️ 32 label themes, 400+ keywords, 116+ curated integrations
- 🖼️ Optional icon suggestions — full coverage of every label & domain (215 mappings / 110 icons), never overwrites an existing icon
- 🏠 Optional area & floor labels, plus a standalone area-assignment service
- 🎯 Restrict to chosen label themes; exclude by domain, entity, or glob pattern
- 🧪 Dry-run mode + `preview` service — see changes before writing anything
- ⏱️ Runs on startup, on an interval, and auto-labels new entities
- 🌍 German (default) / English

## Installation

[![Open in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=hiSweid&repository=ha-auto-organizer&category=integration)

HACS → ⋮ → *Custom repositories* → add this repo (category **Integration**) →
install → restart → *Settings → Devices & Services → Add Integration →
Entity Auto-Organizer*.

Manual: copy `custom_components/auto_organizer` into `config/custom_components/`.

## Services

| Service | Does |
| --- | --- |
| `run` | Assign labels (optionally scoped to specific entities) |
| `cleanup` | Remove labels this integration created |
| `assign_areas` | Bulk-assign entities to areas |
| `remove_all` | Remove **every** label in Home Assistant |
| `preview` | Always dry-run, returns labels + areas together |

```yaml
action: auto_organizer.run
data:
  dry_run: true   # omit to actually write
```

Every write service updates the **Last run** sensor, even on dry runs. Only
`preview` never touches anything.

## Options

Under the integration's *Configure* button:

| Option | Default | What it does |
| --- | --- | --- |
| Dry run / Overwrite | off | Preview only / replace instead of merge |
| Label by domain / device class | on | Base matching rules |
| Curated theme labels | on | Integration + car-keyword matching |
| Restrict to label themes | all | Multi-select to limit which labels can be used |
| Auto-suggest entity icons | off | Fill in a specific icon where none is set |
| Area / floor labels | off | Add area/floor as labels too |
| Skip diagnostic/config | on | Ignore helper entities |
| Label language | auto | `auto` / `de` / `en` |
| Max labels per entity | 2 | 1–10 |
| Auto-label new entities | on | Debounced, on entity creation |
| Run on startup / interval | off / 0 | Automatic runs |
| Label prefix | — | Prepended to every label name |
| Exclude domains / entities / pattern | none | Three ways to skip entities |
| Custom rules | — | `keyword=label_key`, one per line |

## Control entities

**Buttons/switch:** Run now · Cleanup labels · Remove all labels · Dry run
toggle · Run scope select.

**Sensors:** Last run (incl. `icons_set` attribute) · Last run time ·
Labeled/Unlabeled entities · Entities without area · Managed labels ·
Entities with icon · Label coverage.

## Labels

32 themes — lighting, climate, security, media, appliances, garden,
network, car, waste, shopping and more — see
[`rules.py`](custom_components/auto_organizer/rules.py) for the full
catalog. *Restrict to label themes* limits assignment to a subset; *Custom
rules* add your own `keyword=label_key` mappings.

## How it works

Rules live as plain data in [`rules.py`](custom_components/auto_organizer/rules.py);
[`organizer.py`](custom_components/auto_organizer/organizer.py) applies
them per entity. Labels the integration creates are marked internally, so
`cleanup` never touches labels you made by hand.

## Contributing

Extend the maps in `rules.py`, add a case to `tests/test_rules.py`, run
`pytest -q` (no Home Assistant install needed — the rule engine is pure).

## License

[MIT](LICENSE)
