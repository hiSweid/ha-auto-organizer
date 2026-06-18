"""Config flow for the Auto Labeler integration."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import (
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.core import callback
from homeassistant.config_entries import ConfigEntry

from .const import (
    CONF_DRY_RUN,
    CONF_ENABLE_DEVICE_CLASS,
    CONF_ENABLE_DOMAIN,
    CONF_ENABLE_INTEGRATION,
    CONF_LABEL_PREFIX,
    CONF_OVERWRITE,
    CONF_RUN_ON_STARTUP,
    CONF_SCAN_INTERVAL,
    CONF_ENABLE_AREA,
    CONF_ENABLE_CURATED,
    CONF_ENABLE_FLOOR,
    CONF_LANGUAGE,
    CONF_SKIP_CATEGORIES,
    DEFAULT_DRY_RUN,
    DEFAULT_ENABLE_AREA,
    DEFAULT_ENABLE_CURATED,
    DEFAULT_ENABLE_FLOOR,
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
    NAME,
)


class AutoLabelerConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle the initial setup. Single instance only."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        if user_input is not None:
            return self.async_create_entry(title=NAME, data={}, options={})
        return self.async_show_form(step_id="user")

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        return AutoLabelerOptionsFlow()


class AutoLabelerOptionsFlow(OptionsFlow):
    """Expose the labeling options."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        o = self.config_entry.options
        schema = vol.Schema(
            {
                vol.Optional(
                    CONF_DRY_RUN,
                    default=o.get(CONF_DRY_RUN, DEFAULT_DRY_RUN),
                ): bool,
                vol.Optional(
                    CONF_OVERWRITE,
                    default=o.get(CONF_OVERWRITE, DEFAULT_OVERWRITE),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_DOMAIN,
                    default=o.get(CONF_ENABLE_DOMAIN, DEFAULT_ENABLE_DOMAIN),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_DEVICE_CLASS,
                    default=o.get(
                        CONF_ENABLE_DEVICE_CLASS, DEFAULT_ENABLE_DEVICE_CLASS
                    ),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_INTEGRATION,
                    default=o.get(
                        CONF_ENABLE_INTEGRATION, DEFAULT_ENABLE_INTEGRATION
                    ),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_CURATED,
                    default=o.get(CONF_ENABLE_CURATED, DEFAULT_ENABLE_CURATED),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_AREA,
                    default=o.get(CONF_ENABLE_AREA, DEFAULT_ENABLE_AREA),
                ): bool,
                vol.Optional(
                    CONF_ENABLE_FLOOR,
                    default=o.get(CONF_ENABLE_FLOOR, DEFAULT_ENABLE_FLOOR),
                ): bool,
                vol.Optional(
                    CONF_SKIP_CATEGORIES,
                    default=o.get(
                        CONF_SKIP_CATEGORIES, DEFAULT_SKIP_CATEGORIES
                    ),
                ): bool,
                vol.Optional(
                    CONF_LANGUAGE,
                    default=o.get(CONF_LANGUAGE, DEFAULT_LANGUAGE),
                ): vol.In(["de", "en"]),
                vol.Optional(
                    CONF_RUN_ON_STARTUP,
                    default=o.get(
                        CONF_RUN_ON_STARTUP, DEFAULT_RUN_ON_STARTUP
                    ),
                ): bool,
                vol.Optional(
                    CONF_SCAN_INTERVAL,
                    default=o.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
                ): vol.All(int, vol.Range(min=0, max=1440)),
                vol.Optional(
                    CONF_LABEL_PREFIX,
                    default=o.get(CONF_LABEL_PREFIX, DEFAULT_LABEL_PREFIX),
                ): str,
            }
        )
        return self.async_show_form(step_id="init", data_schema=schema)
