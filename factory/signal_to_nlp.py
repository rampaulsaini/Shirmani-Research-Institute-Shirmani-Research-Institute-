"""Evidence-first signal-to-NLP translation for multimodal observations.

This module translates measured observations into plain language while preserving
provenance, uncertainty, and the distinction between observation and inference.
It does not claim that a physical signal is a human-like feeling.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from math import isfinite
from typing import Any

@dataclass(frozen=True)
class Observation:
    source: str
    modality: str
    feature: str
    value: float
    unit: str = ""
    baseline: float | None = None
    baseline_tolerance: float | None = None
    evidence_ids: tuple[str, ...] = ()

def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and isfinite(float(value))

def classify_change(value: float, baseline: float | None, tolerance: float | None) -> str:
    if baseline is None or tolerance is None or tolerance < 0:
        return "observed"
    delta = value - baseline
    if abs(delta) <= tolerance:
        return "within-baseline"
    return "above-baseline" if delta > 0 else "below-baseline"

def observation_to_nlp(obs: Observation) -> dict[str, Any]:
    if not obs.source or not obs.modality or not obs.feature:
        raise ValueError("source, modality and feature are required")
    if not _finite(obs.value):
        raise ValueError("value must be a finite number")
    if obs.baseline is not None and not _finite(obs.baseline):
        raise ValueError("baseline must be finite or null")
    if obs.baseline_tolerance is not None and (
        not _finite(obs.baseline_tolerance) or obs.baseline_tolerance < 0
    ):
        raise ValueError("baseline_tolerance must be a non-negative finite number")
    state = classify_change(obs.value, obs.baseline, obs.baseline_tolerance)
    value_text = f"{obs.value:g}{(' ' + obs.unit) if obs.unit else ''}"
    text = f"Source {obs.source} reports {obs.modality} signal '{obs.feature}' at {value_text}; status: {state}."
    if state == "observed":
        interpretation = "The measurement is reported without a baseline comparison."
    elif state == "within-baseline":
        interpretation = "The measurement is within the supplied baseline tolerance."
    else:
        interpretation = "The measurement differs from the supplied baseline; this is a signal change, not proof of a subjective feeling."
    return {
        "schema_version": "1.0",
        "observation": asdict(obs),
        "status": state,
        "plain_language": text,
        "interpretation": interpretation,
        "claim_level": "measurement",
        "confidence": {
            "type": "evidence_completeness",
            "score": round(min(1.0, len(obs.evidence_ids) / 2.0), 3),
            "not_probability_of_feeling": True,
        },
        "evidence_ids": list(obs.evidence_ids),
    }

def translate_batch(rows: list[Observation]) -> list[dict[str, Any]]:
    return [observation_to_nlp(row) for row in rows]

def self_test() -> dict[str, Any]:
    row = Observation("test-sensor", "electrical", "signal_amplitude", 1.25, "mV", 1.0, 0.1, ("e1", "e2"))
    result = observation_to_nlp(row)
    assert result["status"] == "above-baseline"
    assert result["confidence"]["score"] == 1.0
    assert result["confidence"]["not_probability_of_feeling"] is True
    return {"status": "PASS", "schema_version": "1.0"}
