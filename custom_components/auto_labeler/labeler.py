"""Core labeling engine for the Auto Labeler integration."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import label_registry as lr

from .const import MANAGED_MARKER
from .rules import LabelSpec, LabelerOptions, compute_label_specs

_LOGGER = logging.getLogger(__name__)

__all__ = ["Labeler", "LabelerOptions", "RunResult", "compute_label_specs"]


@dataclass
class RunResult:
    """Summary of a labeling run, returned to the caller / service response."""

    scanned: int = 0
    updated: int = 0
    labels_created: int = 0
    changes: list[dict[str, list[str]]] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "scanned": self.scanned,
            "updated": self.updated,
            "labels_created": self.labels_created,
            "changes": self.changes,
        }


class Labeler:
    """Applies the ruleset to the entity registry."""

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass

    async def _resolve_label(
        self, spec: LabelSpec, result: RunResult, *, create: bool
    ) -> str:
        """Return the label_id for ``spec``.

        Creates the label when missing and ``create`` is set. During a dry run
        (``create=False``) nothing is written: existing labels resolve to their
        id, missing ones to a ``(neu) <name>`` placeholder so the preview still
        shows what would be added.
        """
        reg = lr.async_get(self.hass)
        existing = reg.async_get_label_by_name(spec["name"])
        if existing is not None:
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
        options: LabelerOptions,
        entity_filter: set[str] | None = None,
    ) -> RunResult:
        """Scan the entity registry and apply labels."""
        result = RunResult()
        ent_reg = er.async_get(self.hass)

        entries = list(ent_reg.entities.values())
        for entry in entries:
            if entity_filter is not None and entry.entity_id not in entity_filter:
                continue
            result.scanned += 1

            specs = compute_label_specs(entry, options)
            if not specs:
                continue

            target_ids = {
                await self._resolve_label(s, result, create=not options.dry_run)
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
            "Auto Labeler run: scanned=%s updated=%s created=%s dry_run=%s",
            result.scanned,
            result.updated,
            result.labels_created,
            options.dry_run,
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
            result.labels_created -= 1  # negative => removed

        return result
