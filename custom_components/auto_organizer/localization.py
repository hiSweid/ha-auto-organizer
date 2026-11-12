"""Helpers for runtime language values sourced from translations/*.json."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Final

TRANSLATIONS_DIR: Final = Path(__file__).parent / "translations"
FALLBACK_LANGUAGE: Final = "en"
RUNTIME_NEW_LABEL_MARKER_KEY: Final = ("runtime", "new_label_marker")
DEFAULT_NEW_LABEL_MARKER: Final = "new"


@lru_cache(maxsize=1)
def available_translation_languages() -> tuple[str, ...]:
    """Return available translation language codes from /translations."""
    langs = sorted(
        path.stem for path in TRANSLATIONS_DIR.glob("*.json") if path.is_file()
    )
    return tuple(langs) if langs else (FALLBACK_LANGUAGE,)


def resolve_translation_language(language: str | None) -> str:
    """Normalize to a known translation language, falling back to English."""
    if not language:
        return FALLBACK_LANGUAGE
    base = language.split("-", 1)[0].lower()
    return base if base in available_translation_languages() else FALLBACK_LANGUAGE


@lru_cache(maxsize=64)
def _load_translation(language: str) -> dict[str, Any]:
    path = TRANSLATIONS_DIR / f"{language}.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _dig(data: dict[str, Any], path: tuple[str, ...]) -> str | None:
    cur: Any = data
    for part in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur if isinstance(cur, str) and cur else None


def runtime_new_label_marker(language: str | None) -> str:
    """Return the localized marker used in dry-run new-label placeholders."""
    lang = resolve_translation_language(language)
    text = _dig(_load_translation(lang), RUNTIME_NEW_LABEL_MARKER_KEY)
    if text:
        return text
    fallback = _dig(_load_translation(FALLBACK_LANGUAGE), RUNTIME_NEW_LABEL_MARKER_KEY)
    return fallback or DEFAULT_NEW_LABEL_MARKER
