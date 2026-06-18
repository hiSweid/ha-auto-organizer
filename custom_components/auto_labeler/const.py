"""Constants for the Auto Labeler integration."""

from __future__ import annotations

from typing import Final

DOMAIN: Final = "auto_labeler"
NAME: Final = "Entity Auto-Labeler"

# Config / options keys
CONF_DRY_RUN: Final = "dry_run"
CONF_OVERWRITE: Final = "overwrite"
CONF_RUN_ON_STARTUP: Final = "run_on_startup"
CONF_SCAN_INTERVAL: Final = "scan_interval"
CONF_ENABLE_DOMAIN: Final = "enable_domain"
CONF_ENABLE_DEVICE_CLASS: Final = "enable_device_class"
CONF_ENABLE_INTEGRATION: Final = "enable_integration"
CONF_ENABLE_AREA: Final = "enable_area"
CONF_ENABLE_FLOOR: Final = "enable_floor"
CONF_ENABLE_CURATED: Final = "enable_curated"
CONF_SKIP_CATEGORIES: Final = "skip_categories"
CONF_LANGUAGE: Final = "language"
CONF_MAX_LABELS: Final = "max_labels"
CONF_LABEL_PREFIX: Final = "label_prefix"

# Defaults
DEFAULT_DRY_RUN: Final = False
DEFAULT_OVERWRITE: Final = False
DEFAULT_RUN_ON_STARTUP: Final = False
DEFAULT_SCAN_INTERVAL: Final = 0  # minutes, 0 = disabled
DEFAULT_ENABLE_DOMAIN: Final = True
DEFAULT_ENABLE_DEVICE_CLASS: Final = True
DEFAULT_ENABLE_INTEGRATION: Final = False
DEFAULT_ENABLE_AREA: Final = False
DEFAULT_ENABLE_FLOOR: Final = False
DEFAULT_ENABLE_CURATED: Final = True
DEFAULT_SKIP_CATEGORIES: Final = True
DEFAULT_LANGUAGE: Final = "de"
DEFAULT_MAX_LABELS: Final = 2
DEFAULT_LABEL_PREFIX: Final = ""

# Services
SERVICE_RUN: Final = "run"
SERVICE_CLEANUP: Final = "cleanup"
SERVICE_ASSIGN_AREAS: Final = "assign_areas"

# Service call attributes
ATTR_DRY_RUN: Final = "dry_run"
ATTR_OVERWRITE: Final = "overwrite"
ATTR_ENTITY_FILTER: Final = "entities"

# Marker stored in label description so cleanup only touches our labels.
MANAGED_MARKER: Final = "auto_labeler:managed"
