"""Deterministic multimodal observation -> plain-language NLP adapter.

This module is a dependency-free semantic adapter contract. It translates
already-measured signals into typed observations and cautious natural-language
summaries; it does not infer subjective experience from a raw signal.
"""
from __future__ import annotations

import math
from typing import Any, Dict, Iterable, List


ALLOWED_MODALITIES = {
    "signal",
    "audio",
    "image",
    "video",
    "environment",
    "bioelectric",
    "vibration",
    "chemical",
    "motion",
    "temperature",
    "light",
}


def _finite_number(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not math.isfinite(number):
        raise ValueError(f"{field} must be finite")
    return number


def normalize_observation(
    *,
    modality: str,
    feature: str,
    value: Any,
    unit: str | None = None,
    timestamp: str | None = None,
    source_id: str | None = None,
    observation_id: str | None = None,
) -> Dict[str, Any]:
    """Create a canonical, typed observation from a measured value."""
    if modality not in ALLOWED_MODALITIES:
        raise ValueError(f"unsupported modality: {modality}")
    if not isinstance(feature, str) or not feature.strip():
        raise ValueError("feature must be a non-empty string")

    if observation_id is not None and (not isinstance(observation_id, str) or not observation_id.strip()):
        raise ValueError("observation_id must be a non-empty string when provided")

    observation: Dict[str, Any] = {
        "id": observation_id or f"{modality}:{feature.strip()}",
        "modality": modality,
        "feature": feature.strip(),
        "value": _finite_number(value, "value"),
    }
    if unit is not None:
        if not isinstance(unit, str) or not unit.strip():
            raise ValueError("unit must be a non-empty string when provided")
        observation["unit"] = unit.strip()
    if timestamp is not None:
        observation["timestamp"] = timestamp
    if source_id is not None:
        observation["source_id"] = source_id
    return observation


def to_plain_language(
    observations: Iterable[Dict[str, Any]],
    *,
    context: str | None = None,
) -> Dict[str, Any]:
    """Render measured observations as cautious, human-readable language."""
    items: List[Dict[str, Any]] = list(observations)
    if not items:
        raise ValueError("at least one observation is required")

    lines = []
    for item in items:
        normalized = normalize_observation(
            modality=item.get("modality", ""),
            feature=item.get("feature", ""),
            value=item.get("value"),
            unit=item.get("unit"),
            timestamp=item.get("timestamp"),
            source_id=item.get("source_id"),
            observation_id=item.get("id"),
        )
        unit = f" {normalized['unit']}" if normalized.get("unit") else ""
        lines.append(
            f"{normalized['modality']} signal '{normalized['feature']}' "
            f"was measured at {normalized['value']}{unit}."
        )

    if context:
        if not isinstance(context, str) or not context.strip():
            raise ValueError("context must be a non-empty string when provided")
        prefix = f"Context: {context.strip()} "
    else:
        prefix = ""

    return {
        "plain_language": prefix + " ".join(lines),
        "claim_type": "data_interpretation",
        "epistemic_note": (
            "This describes measured signals only; it does not by itself "
            "establish subjective feelings, consciousness, or scientific causation."
        ),
        "observation_count": len(items),
    }
