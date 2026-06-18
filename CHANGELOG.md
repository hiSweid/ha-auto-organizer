# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Control entities** (a device with): *Run now* and *Cleanup labels* buttons,
  a *Run scope* select (labels+areas / only labels / only areas), a *Dry run*
  switch, and a *Last run* sensor with result details.
- `auto_organizer.assign_areas` service: auto-assigns entities **without** an
  area to a matching area by name/alias (longest match wins, ambiguous matches
  skipped). Supports `dry_run`; never changes existing area assignments.
- Known vehicle names (e-Golf, Tesla, Zoe, Leaf, Kona, Ioniq, …) are labeled
  **Auto** even when a device class also applies.
- `max_labels` option (default **2**) caps labels per entity.

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

[Unreleased]: https://github.com/henrykhanke/ha-auto-organizer/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/henrykhanke/ha-auto-organizer/releases/tag/v0.1.0
