"""The Entity Auto-Labeler integration."""

from __future__ import annotations

import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
)
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.start import async_at_started

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
    CONF_LANGUAGE,
    CONF_SKIP_CATEGORIES,
    DEFAULT_DRY_RUN,
    DEFAULT_LANGUAGE,
    DEFAULT_ENABLE_DEVICE_CLASS,
    DEFAULT_ENABLE_DOMAIN,
    DEFAULT_ENABLE_INTEGRATION,
    DEFAULT_LABEL_PREFIX,
    DEFAULT_SKIP_CATEGORIES,
    DEFAULT_OVERWRITE,
    DEFAULT_RUN_ON_STARTUP,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    SERVICE_CLEANUP,
    SERVICE_RUN,
)
from .labeler import Labeler, LabelerOptions

_LOGGER = logging.getLogger(__name__)

type AutoLabelerConfigEntry = ConfigEntry[Labeler]


def _options_from_entry(entry: ConfigEntry) -> LabelerOptions:
    o = entry.options
    return LabelerOptions(
        dry_run=o.get(CONF_DRY_RUN, DEFAULT_DRY_RUN),
        overwrite=o.get(CONF_OVERWRITE, DEFAULT_OVERWRITE),
        enable_domain=o.get(CONF_ENABLE_DOMAIN, DEFAULT_ENABLE_DOMAIN),
        enable_device_class=o.get(
            CONF_ENABLE_DEVICE_CLASS, DEFAULT_ENABLE_DEVICE_CLASS
        ),
        enable_integration=o.get(
            CONF_ENABLE_INTEGRATION, DEFAULT_ENABLE_INTEGRATION
        ),
        skip_categories=o.get(CONF_SKIP_CATEGORIES, DEFAULT_SKIP_CATEGORIES),
        language=o.get(CONF_LANGUAGE, DEFAULT_LANGUAGE),
        label_prefix=o.get(CONF_LABEL_PREFIX, DEFAULT_LABEL_PREFIX),
    )


async def async_setup_entry(
    hass: HomeAssistant, entry: AutoLabelerConfigEntry
) -> bool:
    """Set up Auto Labeler from a config entry."""
    labeler = Labeler(hass)
    entry.runtime_data = labeler

    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    if entry.options.get(CONF_RUN_ON_STARTUP, DEFAULT_RUN_ON_STARTUP):

        async def _run_on_start(_now) -> None:
            await labeler.run(_options_from_entry(entry))

        async_at_started(hass, _run_on_start)

    interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    if interval and interval > 0:

        async def _scheduled(_now) -> None:
            await labeler.run(_options_from_entry(entry))

        entry.async_on_unload(
            async_track_time_interval(
                hass, _scheduled, timedelta(minutes=interval)
            )
        )

    _register_services(hass)
    return True


def _register_services(hass: HomeAssistant) -> None:
    """Register integration services once."""
    if hass.services.has_service(DOMAIN, SERVICE_RUN):
        return

    async def _handle_run(call: ServiceCall) -> ServiceResponse:
        entries: list[AutoLabelerConfigEntry] = hass.config_entries.async_entries(
            DOMAIN
        )
        if not entries:
            return {"error": "no config entry"}
        entry = entries[0]
        options = _options_from_entry(entry)
        if ATTR_DRY_RUN in call.data:
            options.dry_run = call.data[ATTR_DRY_RUN]
        if ATTR_OVERWRITE in call.data:
            options.overwrite = call.data[ATTR_OVERWRITE]
        entity_filter = call.data.get(ATTR_ENTITY_FILTER)
        result = await entry.runtime_data.run(
            options,
            entity_filter=set(entity_filter) if entity_filter else None,
        )
        return result.as_dict()

    async def _handle_cleanup(call: ServiceCall) -> ServiceResponse:
        entries = hass.config_entries.async_entries(DOMAIN)
        if not entries:
            return {"error": "no config entry"}
        result = await entries[0].runtime_data.cleanup(
            dry_run=call.data.get(ATTR_DRY_RUN, False)
        )
        return result.as_dict()

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


async def _async_update_listener(
    hass: HomeAssistant, entry: AutoLabelerConfigEntry
) -> None:
    """Reload the entry when options change."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(
    hass: HomeAssistant, entry: AutoLabelerConfigEntry
) -> bool:
    """Unload a config entry."""
    if not hass.config_entries.async_entries(DOMAIN):
        for service in (SERVICE_RUN, SERVICE_CLEANUP):
            hass.services.async_remove(DOMAIN, service)
    return True
