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


def build_record(
    *,
    event_id: str,
    source_type: str,
    observations: Iterable[Dict[str, Any]],
    confidence: float,
    evidence_id: str = "measurement-batch",
    evidence_type: str = "measured_signal",
    provenance_source: str = "supreme_nlp_adapter",
    context: str | None = None,
) -> Dict[str, Any]:
    """Build a gate-compatible, evidence-linked interpretation record.

    This is the bridge between measured multimodal inputs and the Supreme NLP
    verification contract. It never upgrades a measurement into a claim about
    subjective experience.
    """
    if not isinstance(event_id, str) or not event_id.strip():
        raise ValueError("event_id must be a non-empty string")
    if not isinstance(source_type, str) or not source_type.strip():
        raise ValueError("source_type must be a non-empty string")
    confidence = _finite_number(confidence, "confidence")
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")

    normalized = [
        normalize_observation(
            modality=item.get("modality", ""),
            feature=item.get("feature", ""),
            value=item.get("value"),
            unit=item.get("unit"),
            timestamp=item.get("timestamp"),
            source_id=item.get("source_id"),
            observation_id=item.get("id"),
        )
        for item in observations
    ]
    if not normalized:
        raise ValueError("at least one observation is required")

    language = to_plain_language(normalized, context=context)
    return {
        "event_id": event_id.strip(),
        "source_type": source_type.strip(),
        "observations": normalized,
        "interpretation": language,
        "confidence": confidence,
        "evidence": [{
            "id": evidence_id,
            "type": evidence_type,
            "observation_ids": [item["id"] for item in normalized],
        }],
        "verification": {
            "independent_check": False,
            "method": "adapter_contract_pending_independent_check",
        },
        "provenance": {
            "source": provenance_source,
            "adapter": "supreme_nlp_adapter",
        },
    }
