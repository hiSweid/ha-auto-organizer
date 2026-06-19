"""Pytest configuration for Home Assistant integration tests.

Loaded only in CI (where pytest-homeassistant-custom-component is installed).
The pure rule-engine tests in tests/test_rules.py do not need this.
"""

pytest_plugins = "pytest_homeassistant_custom_component"
