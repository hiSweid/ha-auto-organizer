"""The Entity Auto-Organizer integration."""

from __future__ import annotations

import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import (
    Event,
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
)
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers.debounce import Debouncer
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.start import async_at_started
from homeassistant.util import dt as dt_util

from .coordinator import AutoOrganizerRuntime

from .const import (
    ATTR_DRY_RUN,
    ATTR_ENTITY_FILTER,
    ATTR_OVERWRITE,
    CONF_ENABLE_DEVICE_CLASS,
    CONF_ENABLE_DOMAIN,
    CONF_ENABLE_INTEGRATION,
    CONF_DRY_RUN,
    CONF_LABEL_PREFIX,
    CONF_OVERWRITE,
    CONF_RUN_ON_STARTUP,
    CONF_SCAN_INTERVAL,
    CONF_ENABLE_AREA,
    CONF_ENABLE_CURATED,
    CONF_ENABLE_FLOOR,
    CONF_AUTO_LABEL_NEW,
    CONF_CUSTOM_RULES,
    CONF_ENABLED_LABELS,
    CONF_EXCLUDE,
    CONF_EXCLUDE_DOMAINS,
    CONF_EXCLUDE_ENTITIES,
    CONF_LANGUAGE,
    CONF_MAX_LABELS,
    CONF_SET_ENTITY_ICONS,
    CONF_SKIP_CATEGORIES,
    DEFAULT_AUTO_LABEL_NEW,
    DEFAULT_DRY_RUN,
    DEFAULT_ENABLE_AREA,
    DEFAULT_ENABLE_CURATED,
    DEFAULT_ENABLE_FLOOR,
    DEFAULT_ENABLED_LABELS,
    DEFAULT_SET_ENTITY_ICONS,
    DEFAULT_EXCLUDE_DOMAINS,
    DEFAULT_EXCLUDE_ENTITIES,
    DEFAULT_LANGUAGE,
    DEFAULT_MAX_LABELS,
    DEFAULT_ENABLE_DEVICE_CLASS,
    DEFAULT_ENABLE_DOMAIN,
    DEFAULT_ENABLE_INTEGRATION,
    DEFAULT_LABEL_PREFIX,
    DEFAULT_SKIP_CATEGORIES,
    DEFAULT_OVERWRITE,
    DEFAULT_RUN_ON_STARTUP,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    SERVICE_ASSIGN_AREAS,
    SERVICE_ASSIGN_ICONS,
    SERVICE_CLEANUP,
    SERVICE_PREVIEW,
    SERVICE_REMOVE_ALL,
    SERVICE_RUN,
)
from .organizer import Organizer, OrganizerOptions
from .rules import invalid_custom_rule_labels, parse_custom_rules

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.BUTTON,
    Platform.SELECT,
    Platform.SWITCH,
    Platform.SENSOR,
]

type AutoOrganizerConfigEntry = ConfigEntry[AutoOrganizerRuntime]


def _options_from_entry(hass: HomeAssistant, entry: ConfigEntry) -> OrganizerOptions:
    o = entry.options
    language = o.get(CONF_LANGUAGE, DEFAULT_LANGUAGE)
    if language == "auto":
        # Follow Home Assistant's configured language (resolved to de/en).
        language = hass.config.language
    return OrganizerOptions(
        dry_run=o.get(CONF_DRY_RUN, DEFAULT_DRY_RUN),
        overwrite=o.get(CONF_OVERWRITE, DEFAULT_OVERWRITE),
        enable_domain=o.get(CONF_ENABLE_DOMAIN, DEFAULT_ENABLE_DOMAIN),
        enable_device_class=o.get(
            CONF_ENABLE_DEVICE_CLASS, DEFAULT_ENABLE_DEVICE_CLASS
        ),
        enable_integration=o.get(
            CONF_ENABLE_INTEGRATION, DEFAULT_ENABLE_INTEGRATION
        ),
        enable_curated=o.get(CONF_ENABLE_CURATED, DEFAULT_ENABLE_CURATED),
        enable_area=o.get(CONF_ENABLE_AREA, DEFAULT_ENABLE_AREA),
        enable_floor=o.get(CONF_ENABLE_FLOOR, DEFAULT_ENABLE_FLOOR),
        skip_categories=o.get(CONF_SKIP_CATEGORIES, DEFAULT_SKIP_CATEGORIES),
        language=language,
        max_labels=o.get(CONF_MAX_LABELS, DEFAULT_MAX_LABELS),
        exclude=_merge_exclude(
            o.get(CONF_EXCLUDE_DOMAINS, DEFAULT_EXCLUDE_DOMAINS),
            o.get(CONF_EXCLUDE_ENTITIES, DEFAULT_EXCLUDE_ENTITIES),
            o.get(CONF_EXCLUDE, ""),
        ),
        custom_rules=parse_custom_rules(o.get(CONF_CUSTOM_RULES, "")),
        label_prefix=o.get(CONF_LABEL_PREFIX, DEFAULT_LABEL_PREFIX),
        enabled_labels=frozenset(
            o.get(CONF_ENABLED_LABELS, DEFAULT_ENABLED_LABELS)
        ),
        set_entity_icons=o.get(CONF_SET_ENTITY_ICONS, DEFAULT_SET_ENTITY_ICONS),
    )


def _parse_exclude(raw: str | list) -> tuple[str, ...]:
    """Parse the exclude option (comma/newline separated string or list)."""
    if isinstance(raw, (list, tuple)):
        items = raw
    else:
        items = str(raw).replace("\n", ",").split(",")
    return tuple(p.strip() for p in items if p.strip())


def _merge_exclude(
    domains: list | None, entities: list | None, text: str | list
) -> tuple[str, ...]:
    """Combine the domain selector, entity selector and free-text patterns.

    Preserves order and drops duplicates so the same pattern picked via two
    different UI fields doesn't get evaluated twice.
    """
    combined = list(domains or []) + list(entities or []) + list(_parse_exclude(text))
    seen: set[str] = set()
    result: list[str] = []
    for item in combined:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)


async def async_setup_entry(
    hass: HomeAssistant, entry: AutoOrganizerConfigEntry
) -> bool:
    """Set up Auto-Organizer from a config entry."""
    organizer = Organizer(hass)
    runtime = AutoOrganizerRuntime(
        hass=hass,
        entry=entry,
        organizer=organizer,
        options_factory=lambda: _options_from_entry(hass, entry),
    )
    entry.runtime_data = runtime

    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    if entry.options.get(CONF_RUN_ON_STARTUP, DEFAULT_RUN_ON_STARTUP):

        async def _run_on_start(_now) -> None:
            await organizer.run(_options_from_entry(hass, entry))

        async_at_started(hass, _run_on_start)

    interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    if interval and interval > 0:

        async def _scheduled(_now) -> None:
            await organizer.run(_options_from_entry(hass, entry))

        entry.async_on_unload(
            async_track_time_interval(
                hass, _scheduled, timedelta(minutes=interval)
            )
        )

    if entry.options.get(CONF_AUTO_LABEL_NEW, DEFAULT_AUTO_LABEL_NEW):
        pending: set[str] = set()

        async def _flush_new() -> None:
            ids = set(pending)
            pending.clear()
            if not ids:
                return
            result = await runtime.organizer.run(
                _options_from_entry(hass, entry), entity_filter=ids
            )
            if result.updated:
                # Skip the full registry walk when the new entities didn't
                # end up labeled (nothing changed for the stats to reflect).
                runtime.refresh_stats()

        debouncer = Debouncer(
            hass, _LOGGER, cooldown=15.0, immediate=False, function=_flush_new
        )
        entry.async_on_unload(debouncer.async_shutdown)

        async def _on_registry_updated(event: Event) -> None:
            if event.data.get("action") != "create":
                return
            entity_id = event.data["entity_id"]
            reg_entry = er.async_get(hass).async_get(entity_id)
            if reg_entry is not None and reg_entry.platform == DOMAIN:
                # Don't auto-label this integration's own control/diagnostic
                # entities (created during our own async_setup_entry).
                return
            pending.add(entity_id)
            await debouncer.async_call()

        entry.async_on_unload(
            hass.bus.async_listen(
                er.EVENT_ENTITY_REGISTRY_UPDATED, _on_registry_updated
            )
        )

    async def _refresh_stats(*_) -> None:
        runtime.refresh_stats()

    async_at_started(hass, _refresh_stats)
    entry.async_on_unload(
        async_track_time_interval(hass, _refresh_stats, timedelta(minutes=5))
    )

    _update_issues(hass, entry)
    _register_services(hass)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


def _update_issues(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Create/clear repair issues based on the current options."""
    o = entry.options

    invalid = invalid_custom_rule_labels(o.get(CONF_CUSTOM_RULES, ""))
    if invalid:
        ir.async_create_issue(
            hass,
            DOMAIN,
            "invalid_custom_rules",
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key="invalid_custom_rules",
            translation_placeholders={"labels": ", ".join(invalid)},
        )
    else:
        ir.async_delete_issue(hass, DOMAIN, "invalid_custom_rules")

    wants_area = o.get(CONF_ENABLE_AREA, DEFAULT_ENABLE_AREA) or o.get(
        CONF_ENABLE_FLOOR, DEFAULT_ENABLE_FLOOR
    )
    has_areas = bool(ar.async_get(hass).async_list_areas())
    if wants_area and not has_areas:
        ir.async_create_issue(
            hass,
            DOMAIN,
            "no_areas",
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key="no_areas",
        )
    else:
        ir.async_delete_issue(hass, DOMAIN, "no_areas")


def _register_services(hass: HomeAssistant) -> None:
    """Register integration services once.

    Handlers below use ``entries[0]`` — safe today because ``manifest.json``
    sets ``single_config_entry: true``. Revisit if that ever changes.
    """
    if hass.services.has_service(DOMAIN, SERVICE_RUN):
        return

    def _record_last_run(runtime, scope: str, dry_run: bool, **sections) -> None:
        """Update the shared runtime state so control-entity sensors/
        diagnostics reflect service-triggered runs, not just button presses.
        """
        runtime.last_run = {
            "scope": scope,
            "dry_run": dry_run,
            "timestamp": dt_util.utcnow().isoformat(),
            **sections,
        }
        runtime.refresh_stats()

    async def _handle_run(call: ServiceCall) -> ServiceResponse:
        entries: list[AutoOrganizerConfigEntry] = hass.config_entries.async_entries(
            DOMAIN
        )
        if not entries:
            return {"error": "no config entry"}
        entry = entries[0]
        options = _options_from_entry(hass, entry)
        if ATTR_DRY_RUN in call.data:
            options.dry_run = call.data[ATTR_DRY_RUN]
        if ATTR_OVERWRITE in call.data:
            options.overwrite = call.data[ATTR_OVERWRITE]
        entity_filter = call.data.get(ATTR_ENTITY_FILTER)
        try:
            result = await entry.runtime_data.organizer.run(
                options,
                entity_filter=set(entity_filter) if entity_filter else None,
            )
        except Exception as err:
            entry.runtime_data.record_error(str(err))
            raise
        if not options.dry_run:
            timestamp = dt_util.utcnow().isoformat()
            entry.runtime_data.record_history(
                entry.runtime_data.last_labeled, result.changes, timestamp
            )
            entry.runtime_data.record_history(
                entry.runtime_data.last_iconed, result.icon_changes, timestamp
            )
        _record_last_run(
            entry.runtime_data, "labels", options.dry_run, labels=result.as_dict()
        )
        return result.as_dict()

    async def _handle_cleanup(call: ServiceCall) -> ServiceResponse:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        dry_run = call.data.get(ATTR_DRY_RUN, False)
        try:
            result = await entries[0].runtime_data.organizer.cleanup(dry_run=dry_run)
        except Exception as err:
            entries[0].runtime_data.record_error(str(err))
            raise
        _record_last_run(
            entries[0].runtime_data, "cleanup", dry_run, cleanup=result.as_dict()
        )
        return result.as_dict()

    async def _handle_assign_areas(call: ServiceCall) -> ServiceResponse:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        dry_run = call.data.get(ATTR_DRY_RUN, False)
        try:
            result = await entries[0].runtime_data.organizer.assign_areas(
                dry_run=dry_run,
                exclude=_options_from_entry(hass, entries[0]).exclude,
            )
        except Exception as err:
            entries[0].runtime_data.record_error(str(err))
            raise
        if not dry_run:
            entries[0].runtime_data.record_history(
                entries[0].runtime_data.last_grouped,
                result.changes,
                dt_util.utcnow().isoformat(),
            )
        _record_last_run(
            entries[0].runtime_data, "areas", dry_run, areas=result.as_dict()
        )
        return result.as_dict()

    async def _handle_assign_icons(call: ServiceCall) -> ServiceResponse:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        dry_run = call.data.get(ATTR_DRY_RUN, False)
        options = _options_from_entry(hass, entries[0])
        try:
            result = await entries[0].runtime_data.organizer.assign_icons(
                options, dry_run=dry_run
            )
        except Exception as err:
            entries[0].runtime_data.record_error(str(err))
            raise
        if not dry_run:
            entries[0].runtime_data.record_history(
                entries[0].runtime_data.last_iconed,
                result.changes,
                dt_util.utcnow().isoformat(),
            )
        _record_last_run(
            entries[0].runtime_data, "icons", dry_run, icons=result.as_dict()
        )
        return result.as_dict()

    async def _handle_remove_all(call: ServiceCall) -> ServiceResponse:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        dry_run = call.data.get(ATTR_DRY_RUN, False)
        try:
            result = await entries[0].runtime_data.organizer.remove_all_labels(
                dry_run=dry_run
            )
        except Exception as err:
            entries[0].runtime_data.record_error(str(err))
            raise
        _record_last_run(
            entries[0].runtime_data, "remove_all", dry_run, remove_all=result.as_dict()
        )
        return result.as_dict()

    async def _handle_preview(call: ServiceCall) -> ServiceResponse:
        """Preview both labels and areas together; never writes anything."""
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        entry = entries[0]
        options = _options_from_entry(hass, entry)
        options.dry_run = True
        organizer = entry.runtime_data.organizer
        labels_result = await organizer.run(options)
        areas_result = await organizer.assign_areas(
            dry_run=True, exclude=options.exclude
        )
        icons_result = await organizer.assign_icons(options, dry_run=True)
        return {
            "labels": labels_result.as_dict(),
            "areas": areas_result.as_dict(),
            "icons": icons_result.as_dict(),
        }

    hass.services.async_register(
        DOMAIN,
        SERVICE_RUN,
        _handle_run,
        schema=vol.Schema(
            {
                vol.Optional(ATTR_DRY_RUN): cv.boolean,
                vol.Optional(ATTR_OVERWRITE): cv.boolean,
                vol.Optional(ATTR_ENTITY_FILTER): vol.All(
                    cv.ensure_list, [cv.entity_id]
                ),
            }
        ),
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_CLEANUP,
        _handle_cleanup,
        schema=vol.Schema({vol.Optional(ATTR_DRY_RUN): cv.boolean}),
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_ASSIGN_AREAS,
        _handle_assign_areas,
        schema=vol.Schema({vol.Optional(ATTR_DRY_RUN): cv.boolean}),
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_ASSIGN_ICONS,
        _handle_assign_icons,
        schema=vol.Schema({vol.Optional(ATTR_DRY_RUN): cv.boolean}),
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_REMOVE_ALL,
        _handle_remove_all,
        schema=vol.Schema({vol.Optional(ATTR_DRY_RUN): cv.boolean}),
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_PREVIEW,
        _handle_preview,
        schema=vol.Schema({}),
        supports_response=SupportsResponse.ONLY,
    )


async def _async_update_listener(
    hass: HomeAssistant, entry: AutoOrganizerConfigEntry
) -> None:
    """Reload the entry when options change."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(
    hass: HomeAssistant, entry: AutoOrganizerConfigEntry
) -> bool:
    """Unload a config entry."""
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    # Remove the (shared) services only once the last entry is gone.
    remaining = [
        e for e in hass.config_entries.async_entries(DOMAIN) if e.entry_id != entry.entry_id
    ]
    if not remaining:
        for service in (
            SERVICE_RUN,
            SERVICE_CLEANUP,
            SERVICE_ASSIGN_AREAS,
            SERVICE_ASSIGN_ICONS,
            SERVICE_REMOVE_ALL,
            SERVICE_PREVIEW,
        ):
            hass.services.async_remove(DOMAIN, service)
    return unloaded
