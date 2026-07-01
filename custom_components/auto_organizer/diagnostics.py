"""Diagnostics support for Entity Auto-Organizer."""

from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant

from . import AutoOrganizerConfigEntry


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: AutoOrganizerConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry.

    Contains only configuration and aggregate counts — no secrets and no
    per-entity data.
    """
    runtime = entry.runtime_data
    last_run = runtime.last_run or {}
    return {
        "options": dict(entry.options),
        "state": {
            "scope": runtime.scope,
            "dry_run": runtime.dry_run,
        },
        "stats": runtime.stats,
        # Drop the (large) per-entity change lists from every result section
        # ("labels", "areas", "cleanup", "remove_all"); keep the summary.
        "last_run": {
            key: (
                {k: v for k, v in val.items() if k != "changes"}
                if isinstance(val, dict)
                else val
            )
            for key, val in last_run.items()
        },
    }
