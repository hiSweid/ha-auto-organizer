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
    is_excluded,
    label_differs,
    match_area,
)

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "AreaAssignResult",
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
    changes: list[dict[str, list[str]]] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "scanned": self.scanned,
            "updated": self.updated,
            "labels_created": self.labels_created,
            "labels_updated": self.labels_updated,
            "labels_removed": self.labels_removed,
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

            specs = compute_label_specs(entry, options)

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

            if new_labels == set(entry.labels):
                continue

            added = sorted(new_labels - set(entry.labels))
            result.changes.append({"entity_id": entry.entity_id, "added": added})
            result.updated += 1

            if not options.dry_run:
                ent_reg.async_update_entity(entry.entity_id, labels=new_labels)

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

        Only entities that have no effective area (neither their own nor via
        their device) are touched, so existing assignments are never changed.
        Entities matching ``exclude`` are skipped.
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

        for entry in list(ent_reg.entities.values()):
            if entry.area_id:
                continue
            if is_excluded(entry.entity_id, exclude):
                continue
            if entry.device_id:
                device = dev_reg.async_get(entry.device_id)
                if device and device.area_id:
                    continue

            result.scanned += 1
            area_id = match_area(
                entry.entity_id, entry.name or entry.original_name, areas
            )
            if not area_id:
                continue

            result.assigned += 1
            result.changes.append(
                {"entity_id": entry.entity_id, "area_id": area_id}
            )
            if not dry_run:
                ent_reg.async_update_entity(entry.entity_id, area_id=area_id)

        _LOGGER.info(
            "Auto-Organizer area assign: scanned=%s assigned=%s dry_run=%s",
            result.scanned,
            result.assigned,
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
