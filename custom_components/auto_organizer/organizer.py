"""Core labeling engine for the Auto-Organizer integration."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from homeassistant.core import HomeAssistant
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import floor_registry as fr
from homeassistant.helpers import label_registry as lr

from .const import MANAGED_MARKER
from .rules import (
    LabelSpec,
    OrganizerOptions,
    area_floor_specs,
    compute_label_specs,
    compute_label_specs_and_reasons,
    is_excluded,
    label_differs,
    match_area,
    suggest_entity_icon,
)

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "AreaAssignResult",
    "IconAssignResult",
    "Organizer",
    "OrganizerOptions",
    "RunResult",
    "compute_label_specs",
]


@dataclass
class RunResult:
    """Summary of a labeling run, returned to the caller / service response."""

    scanned: int = 0
    updated: int = 0
    labels_created: int = 0
    labels_updated: int = 0
    labels_removed: int = 0
    icons_set: int = 0
    changes: list[dict[str, list[str]]] = field(default_factory=list)
    icon_changes: list[dict[str, str]] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "scanned": self.scanned,
            "updated": self.updated,
            "labels_created": self.labels_created,
            "labels_updated": self.labels_updated,
            "labels_removed": self.labels_removed,
            "icons_set": self.icons_set,
            "changes": self.changes,
            "icon_changes": self.icon_changes,
        }


@dataclass
class IconAssignResult:
    """Summary of an icon-only assignment run."""

    scanned: int = 0
    icons_set: int = 0
    changes: list[dict[str, str]] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "scanned": self.scanned,
            "icons_set": self.icons_set,
            "changes": self.changes,
        }


@dataclass
class AreaAssignResult:
    """Summary of an area auto-assignment run."""

    scanned: int = 0
    assigned: int = 0
    changes: list[dict[str, str]] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "scanned": self.scanned,
            "assigned": self.assigned,
            "changes": self.changes,
        }


class Organizer:
    """Applies the ruleset to the entity registry."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass

    def _resolve_area_floor(
        self, entry: er.RegistryEntry
    ) -> tuple[str | None, str | None]:
        """Return (area_name, floor_name) for an entity.

        The entity's own area takes precedence; otherwise its device's area is
        used. The floor is derived from the resolved area.
        """
        area_id = entry.area_id
        if area_id is None and entry.device_id:
            device = dr.async_get(self.hass).async_get(entry.device_id)
            if device:
                area_id = device.area_id
        if not area_id:
            return None, None

        area = ar.async_get(self.hass).async_get_area(area_id)
        if area is None:
            return None, None

        floor_name: str | None = None
        if area.floor_id:
            floor = fr.async_get(self.hass).async_get_floor(area.floor_id)
            if floor:
                floor_name = floor.name
        return area.name, floor_name

    def _resolve_label(
        self,
        spec: LabelSpec,
        result: RunResult,
        *,
        create: bool,
        synced: set[str],
    ) -> str:
        """Return the label_id for ``spec``.

        Creates the label when missing and ``create`` is set. For existing
        labels managed by this integration, the color/icon is re-synced when
        the rule changed. During a dry run (``create=False``) nothing is
        written: existing labels resolve to their id, missing ones to a
        ``(neu) <name>`` placeholder so the preview still shows what would
        be added.
        """
        reg = lr.async_get(self.hass)
        existing = reg.async_get_label_by_name(spec["name"])
        if existing is not None:
            if (
                existing.description == MANAGED_MARKER
                and spec["name"] not in synced
                and label_differs(existing.color, existing.icon, spec)
            ):
                synced.add(spec["name"])
                result.labels_updated += 1
                if create:
                    reg.async_update(
                        existing.label_id,
                        color=spec["color"],
                        icon=spec["icon"],
                    )
            return existing.label_id
        if not create:
            return f"(neu) {spec['name']}"
        created = reg.async_create(
            name=spec["name"],
            color=spec["color"],
            icon=spec["icon"],
            description=MANAGED_MARKER,
        )
        result.labels_created += 1
        _LOGGER.debug("Created label %s", spec["name"])
        return created.label_id

    async def run(
        self,
        options: OrganizerOptions,
        entity_filter: set[str] | None = None,
    ) -> RunResult:
        """Scan the entity registry and apply labels."""
        result = RunResult()
        ent_reg = er.async_get(self.hass)
        synced: set[str] = set()

        if entity_filter is not None:
            # Small, targeted runs (e.g. the auto-label-new debounce) resolve
            # the handful of entity_ids directly instead of scanning the
            # whole registry (which can be several thousand entries).
            entries = [
                e
                for eid in entity_filter
                if (e := ent_reg.async_get(eid)) is not None
            ]
        else:
            entries = list(ent_reg.entities.values())

        for entry in entries:
            result.scanned += 1

            # User exclusions take priority over everything else — including
            # area/floor labels, which compute_label_specs() itself can't
            # guard since they're computed separately below and appended
            # unconditionally.
            if is_excluded(entry.entity_id, options.exclude):
                continue

            specs, reasons = compute_label_specs_and_reasons(entry, options)

            # Area/floor labels apply to any non-diagnostic entity, even when
            # no functional label matched.
            if (options.enable_area or options.enable_floor) and not (
                options.skip_categories and entry.entity_category
            ):
                area_name, floor_name = self._resolve_area_floor(entry)
                specs = specs + area_floor_specs(area_name, floor_name, options)

            if not specs:
                continue

            target_ids = {
                self._resolve_label(
                    s, result, create=not options.dry_run, synced=synced
                )
                for s in specs
            }

            if options.overwrite:
                new_labels = target_ids
            else:
                new_labels = set(entry.labels) | target_ids
            labels_changed = new_labels != set(entry.labels)

            # Only fill in an icon when the entity has none yet — never
            # overwrite one the user (or a past run) already set, since the
            # registry can't tell those two apart. Config/diagnostic
            # entities keep HA's own default icon (a slider, a clock, a
            # counter, ...) instead of inheriting the parent device's
            # keyword-matched icon — same skip_categories guard already
            # used above for area/floor labels and in assign_icons().
            icon = None
            if (
                options.set_entity_icons
                and not entry.icon
                and not (options.skip_categories and entry.entity_category)
            ):
                icon = suggest_entity_icon(entry, options)

            if not labels_changed and not icon:
                continue

            update_kwargs: dict = {}
            if labels_changed:
                added = sorted(new_labels - set(entry.labels))
                change: dict = {"entity_id": entry.entity_id, "added": added}
                if reasons:
                    # Debugging aid: which keyword/domain/device_class/
                    # platform actually matched, so a wrong or unexpected
                    # label can be traced back without reading rules.py.
                    change["reasons"] = reasons
                result.changes.append(change)
                result.updated += 1
                update_kwargs["labels"] = new_labels
            if icon:
                result.icons_set += 1
                result.icon_changes.append(
                    {"entity_id": entry.entity_id, "icon": icon}
                )
                update_kwargs["icon"] = icon

            if not options.dry_run:
                ent_reg.async_update_entity(entry.entity_id, **update_kwargs)

        _LOGGER.info(
            "Auto-Organizer run: scanned=%s updated=%s created=%s dry_run=%s",
            result.scanned,
            result.updated,
            result.labels_created,
            options.dry_run,
        )
        return result

    async def assign_areas(
        self, dry_run: bool = False, exclude: tuple[str, ...] = ()
    ) -> AreaAssignResult:
        """Auto-assign entities without an area to a matching area by name.

        A device whose entities all agree on the same room gets that area on
        the *device* itself — so it shows up as one device card in the room
        instead of the same area being scattered across every one of its
        entities as a per-entity override — while a device with disagreeing
        or only partially matched entities keeps the previous per-entity
        behaviour. This also reconciles devices that already carry that
        scattered pattern (typically from an older run of this same method):
        when every entity of an area-less device already has an explicit,
        identical area override, that area is promoted to the device and the
        now-redundant per-entity overrides are cleared back to inherited.
        Only the *storage location* of an assignment ever moves this way —
        an entity's effective area (its own override, or its device's) is
        never changed by this method. Entities matching ``exclude`` are
        skipped.
        """
        result = AreaAssignResult()
        ent_reg = er.async_get(self.hass)
        area_reg = ar.async_get(self.hass)
        dev_reg = dr.async_get(self.hass)

        areas = [
            {"area_id": a.id, "name": a.name, "aliases": list(a.aliases)}
            for a in area_reg.async_list_areas()
        ]
        if not areas:
            return result

        by_device: dict[str, list] = {}
        standalone = []
        for entry in ent_reg.entities.values():
            if is_excluded(entry.entity_id, exclude):
                continue
            device = dev_reg.async_get(entry.device_id) if entry.device_id else None
            if device is None:
                if not entry.area_id:
                    standalone.append(entry)
                continue
            by_device.setdefault(device.id, []).append(entry)

        for device_id, dev_entries in by_device.items():
            device = dev_reg.async_get(device_id)
            if device.area_id:
                # Device already has its own area — every entity inherits
                # it, nothing to guess or reconcile here.
                continue

            result.scanned += len(dev_entries)
            existing = {e.area_id for e in dev_entries if e.area_id}

            if len(existing) == 1:
                area_id = existing.pop()
                to_clear = [e for e in dev_entries if e.area_id == area_id]
                result.assigned += len(to_clear)
                result.changes.extend(
                    {
                        "entity_id": e.entity_id,
                        "area_id": area_id,
                        "device_id": device_id,
                    }
                    for e in to_clear
                )
                if not dry_run:
                    dev_reg.async_update_device(device_id, area_id=area_id)
                    for e in to_clear:
                        ent_reg.async_update_entity(e.entity_id, area_id=None)
                continue
            if existing:
                # Conflicting explicit overrides already on this device —
                # leave them exactly as they are rather than guessing which
                # one should win.
                continue

            # No entity has an area yet: guess one per entity from its own
            # id/name (falling back to the device name), same as before —
            # but only commit the guesses to the device if literally every
            # entity agrees on the same one; otherwise fall back to writing
            # per-entity, same as this method always has.
            device_name = device.name_by_user or device.name
            guesses = {
                entry.entity_id: area_id
                for entry in dev_entries
                if (
                    area_id := match_area(
                        entry.entity_id,
                        entry.name or entry.original_name,
                        areas,
                        # Fallback only — plenty of entities are named after
                        # what they measure rather than where they sit, and
                        # their device ("Hue Bridge Wohnzimmer", "Thread
                        # Presence Büro") is then the only place a room name
                        # appears at all.
                        device_name=device_name,
                    )
                )
                is not None
            }
            matched_areas = set(guesses.values())
            if len(matched_areas) == 1 and len(guesses) == len(dev_entries):
                area_id = matched_areas.pop()
                result.assigned += len(dev_entries)
                result.changes.extend(
                    {
                        "entity_id": entry.entity_id,
                        "area_id": area_id,
                        "device_id": device_id,
                    }
                    for entry in dev_entries
                )
                if not dry_run:
                    dev_reg.async_update_device(device_id, area_id=area_id)
            else:
                for entry in dev_entries:
                    area_id = guesses.get(entry.entity_id)
                    if not area_id:
                        continue
                    result.assigned += 1
                    result.changes.append(
                        {"entity_id": entry.entity_id, "area_id": area_id}
                    )
                    if not dry_run:
                        ent_reg.async_update_entity(entry.entity_id, area_id=area_id)

        for entry in standalone:
            result.scanned += 1
            area_id = match_area(
                entry.entity_id, entry.name or entry.original_name, areas
            )
            if not area_id:
                continue

            result.assigned += 1
            result.changes.append({"entity_id": entry.entity_id, "area_id": area_id})
            if not dry_run:
                ent_reg.async_update_entity(entry.entity_id, area_id=area_id)

        _LOGGER.info(
            "Auto-Organizer area assign: scanned=%s assigned=%s dry_run=%s",
            result.scanned,
            result.assigned,
            dry_run,
        )
        return result

    async def assign_icons(
        self, options: OrganizerOptions, dry_run: bool = False
    ) -> IconAssignResult:
        """Suggest and apply icons across the whole entity registry.

        Unlike the icon side-effect in :meth:`run` (which only ever touches
        entities that also matched a label this run), this scans every
        entity so it also reaches ones with no label match. Existing icons
        are only replaced when ``options.overwrite`` is set.
        """
        result = IconAssignResult()
        ent_reg = er.async_get(self.hass)

        for entry in ent_reg.entities.values():
            if is_excluded(entry.entity_id, options.exclude):
                continue
            if options.skip_categories and entry.entity_category:
                continue
            if entry.icon and not options.overwrite:
                continue

            result.scanned += 1
            icon = suggest_entity_icon(entry, options)
            if not icon or icon == entry.icon:
                continue

            result.icons_set += 1
            result.changes.append({"entity_id": entry.entity_id, "icon": icon})
            if not dry_run:
                ent_reg.async_update_entity(entry.entity_id, icon=icon)

        _LOGGER.info(
            "Auto-Organizer icon assign: scanned=%s icons_set=%s dry_run=%s",
            result.scanned,
            result.icons_set,
            dry_run,
        )
        return result

    async def cleanup(self, dry_run: bool = False) -> RunResult:
        """Remove labels that were created by this integration.

        Only labels whose description carries :data:`MANAGED_MARKER` are
        touched, so manually created labels are never deleted.
        """
        result = RunResult()
        reg = lr.async_get(self.hass)
        ent_reg = er.async_get(self.hass)

        managed = {
            label.label_id
            for label in reg.async_list_labels()
            if label.description == MANAGED_MARKER
        }
        if not managed:
            return result

        for entry in list(ent_reg.entities.values()):
            if set(entry.labels) & managed:
                result.updated += 1
                if not dry_run:
                    ent_reg.async_update_entity(
                        entry.entity_id, labels=set(entry.labels) - managed
                    )

        for label_id in managed:
            if not dry_run:
                reg.async_delete(label_id)
            result.labels_removed += 1

        return result

    async def remove_all_labels(self, dry_run: bool = False) -> RunResult:
        """Remove **every** label in Home Assistant, not just managed ones.

        Clears all label assignments from entities and deletes all labels.
        Destructive on purpose — triggered explicitly by the user.
        """
        result = RunResult()
        reg = lr.async_get(self.hass)
        ent_reg = er.async_get(self.hass)

        all_label_ids = {label.label_id for label in reg.async_list_labels()}
        if not all_label_ids:
            return result

        for entry in list(ent_reg.entities.values()):
            if entry.labels:
                result.updated += 1
                if not dry_run:
                    ent_reg.async_update_entity(entry.entity_id, labels=set())

        for label_id in all_label_ids:
            if not dry_run:
                reg.async_delete(label_id)
            result.labels_removed += 1

        return result
