"""Deterministic multimodal signal -> NLP interpretation contract.

This module does not claim to read subjective feelings directly. It converts
observable, timestamped signals into normalized features, hypotheses, simple
language, and explicit uncertainty/evidence fields. A learned model can later
replace individual adapters without changing the contract.
"""
from __future__ import annotations
import math
from statistics import mean, pstdev
from typing import Any

SCHEMA_VERSION = "1.0"
SUPPORTED_CHANNELS = {
    "text", "audio", "video", "vibration", "temperature",
    "electrical", "light", "chemical", "motion", "environmental",
    "generic_sensor",
}

def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))

def normalize_signal(signal: dict[str, Any]) -> dict[str, Any]:
    channel = str(signal.get("channel", "generic_sensor")).casefold()
    values = signal.get("values", [])
    if channel not in SUPPORTED_CHANNELS:
        raise ValueError(f"unsupported channel: {channel}")
    if not isinstance(values, list) or not values:
        raise ValueError("values must be a non-empty list")
    numeric = [float(v) for v in values if _finite(v)]
    if not numeric:
        raise ValueError("values contain no finite numeric samples")
    return {
        "schema_version": SCHEMA_VERSION, "channel": channel,
        "sample_count": len(numeric), "values": numeric,
        "unit": str(signal.get("unit", "unspecified")),
        "timestamp": str(signal.get("timestamp", "")),
        "source_id": str(signal.get("source_id", "unknown")),
    }

def extract_features(signal: dict[str, Any]) -> dict[str, float]:
    s = normalize_signal(signal)
    values = s["values"]
    avg = mean(values)
    deviation = pstdev(values) if len(values) > 1 else 0.0
    minimum, maximum = min(values), max(values)
    span = maximum - minimum
    return {
        "mean": round(avg, 8), "stddev": round(deviation, 8),
        "min": round(minimum, 8), "max": round(maximum, 8),
        "range": round(span, 8),
        "relative_variability": round(deviation / max(abs(avg), 1e-12), 8),
    }

def classify_pattern(features: dict[str, float]) -> dict[str, Any]:
    variability = features["relative_variability"]
    span = features["range"]
    if variability < 0.01 and span == 0:
        label = "stable"
        explanation = "The measured signal is stable within the supplied samples."
    elif variability < 0.05:
        label = "low_variation"
        explanation = "The measured signal shows small variation."
    elif variability < 0.20:
        label = "moderate_variation"
        explanation = "The measured signal shows moderate variation."
    else:
        label = "high_variation"
        explanation = "The measured signal shows high variation."
    return {"pattern": label, "explanation": explanation}

def signal_to_nlp(signal: dict[str, Any], evidence: list[str] | None = None) -> dict[str, Any]:
    normalized = normalize_signal(signal)
    features = extract_features(normalized)
    pattern = classify_pattern(features)
    evidence_ids = [str(x) for x in (evidence or []) if str(x)]
    confidence = max(0.0, min(1.0, 1.0 - min(features["relative_variability"], 1.0)))
    text = (
        f"Channel {normalized['channel']} shows {pattern['pattern']} "
        f"with mean {features['mean']} {normalized['unit']}."
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "interpretation_type": "observable-signal-to-language",
        "source_id": normalized["source_id"], "channel": normalized["channel"],
        "features": features, "pattern": pattern,
        "simple_language": text, "confidence": round(confidence, 6),
        "confidence_meaning": "heuristic classification confidence; not proof of emotion, consciousness, or subjective feeling",
        "evidence_ids": evidence_ids, "verification_status": "UNVERIFIED",
        "claim_boundary": "No subjective feeling is inferred from signal alone.",
    }
