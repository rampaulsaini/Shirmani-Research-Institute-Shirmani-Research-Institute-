"""Deterministic signal-to-language interpretation contract.

This module translates measured/observed multimodal signal summaries into
plain-language statements without pretending that an inferred state is direct
proof of subjective experience.
"""
from __future__ import annotations

import math
from typing import Any

SCHEMA_VERSION = "1.0"

ALLOWED_MODALITIES = {
    "acoustic", "vibration", "electrical", "bioelectrical", "temperature",
    "humidity", "light", "motion", "chemical", "image", "video", "text", "speech",
}

def _finite_number(value: Any) -> float | None:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None

def normalize_observation(observation: dict[str, Any]) -> dict[str, Any]:
    modality = str(observation.get("modality", "")).strip().casefold()
    if modality not in ALLOWED_MODALITIES:
        raise ValueError(f"unsupported modality: {modality or '<empty>'}")
    features = observation.get("features") or {}
    if not isinstance(features, dict):
        raise ValueError("features must be an object")
    normalized = {}
    for key, value in sorted(features.items()):
        n = _finite_number(value)
        normalized[str(key)] = n if n is not None else str(value)
    return {
        "schema_version": SCHEMA_VERSION,
        "modality": modality,
        "timestamp": str(observation.get("timestamp", "")),
        "source_id": str(observation.get("source_id", "")),
        "features": normalized,
        "context": str(observation.get("context", "")),
    }

def interpret_observation(observation: dict[str, Any]) -> dict[str, Any]:
    obs = normalize_observation(observation)
    numeric = [v for v in obs["features"].values() if isinstance(v, (int, float))]
    quality = 1.0 if numeric else 0.5
    context = obs["context"] or "no additional context supplied"
    return {
        "schema_version": SCHEMA_VERSION,
        "modality": obs["modality"],
        "source_id": obs["source_id"],
        "observed": obs["features"],
        "interpretation": (
            f"Observed {obs['modality']} signal features were received. "
            f"Context: {context}."
        ),
        "inference": (
            "No subjective feeling is asserted. Any biological, emotional, "
            "or state interpretation requires a validated model and evidence."
        ),
        "confidence": round(quality, 6),
        "confidence_type": "signal_quality_proxy",
        "provenance": {
            "source_id": obs["source_id"],
            "timestamp": obs["timestamp"],
            "modality": obs["modality"],
            "schema_version": SCHEMA_VERSION,
        },
        "verification_status": "UNVERIFIED",
    }

def to_plain_language(result: dict[str, Any]) -> str:
    return (
        f"सरल भाषा: {result['interpretation']} "
        f"यह केवल मापे गए संकेतों का वर्णन है; प्रत्यक्ष अनुभव का प्रमाण नहीं। "
        f"Signal-quality confidence: {result['confidence']:.2f}. "
        f"Verification: {result['verification_status']}."
    )
