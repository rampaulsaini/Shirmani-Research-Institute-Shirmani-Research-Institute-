"""Evidence-first multimodal signal -> plain-language NLP translator.

This is deliberately not a mind-reading system. It translates observable,
machine-readable signal features into bounded natural-language statements,
with provenance, uncertainty, and an explicit evidence boundary.

Input can represent biological, environmental, mechanical, or other sensor
streams. The same schema keeps the layer domain-neutral and testable.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Any, Mapping


SCHEMA_VERSION = "1.0"


@dataclass(frozen=True)
class SignalObservation:
    source_id: str
    domain: str
    signal_type: str
    window_seconds: float
    baseline: float
    value: float
    trend: str = "stable"
    quality: float = 1.0
    features: tuple[str, ...] = ()

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.source_id:
            errors.append("missing source_id")
        if not self.signal_type:
            errors.append("missing signal_type")
        if self.window_seconds <= 0:
            errors.append("window_seconds must be > 0")
        if not math.isfinite(self.baseline) or not math.isfinite(self.value):
            errors.append("baseline/value must be finite")
        if not 0.0 <= self.quality <= 1.0:
            errors.append("quality must be within [0,1]")
        if self.trend not in {"rising", "falling", "stable", "unknown"}:
            errors.append("invalid trend")
        return errors


def _relative_change(baseline: float, value: float) -> float:
    scale = max(abs(baseline), 1e-12)
    return (value - baseline) / scale


def classify_signal(obs: SignalObservation) -> dict[str, Any]:
    """Classify measurable change without assigning subjective experience."""
    errors = obs.validate()
    if errors:
        return {
            "status": "INVALID",
            "errors": errors,
            "claim_level": "NONE",
            "interpretation": None,
        }

    delta = _relative_change(obs.baseline, obs.value)
    magnitude = abs(delta)

    if obs.quality < 0.50:
        level = "LOW_QUALITY"
    elif magnitude >= 0.50:
        level = "STRONG_CHANGE"
    elif magnitude >= 0.10:
        level = "MODERATE_CHANGE"
    else:
        level = "SMALL_CHANGE"

    return {
        "status": "OK",
        "claim_level": level,
        "relative_change": round(delta, 6),
        "interpretation": (
            f"{obs.signal_type} shows a {level.lower().replace('_', ' ')} "
            f"relative to its supplied baseline; observed trend is {obs.trend}."
        ),
        "evidence_boundary": (
            "This describes an observable signal pattern only. It does not "
            "establish consciousness, emotion, intention, or subjective feeling."
        ),
    }


def to_plain_language(obs: SignalObservation) -> dict[str, Any]:
    """Return a simple-language rendering suitable for downstream NLP."""
    result = classify_signal(obs)
    if result["status"] != "OK":
        return result

    confidence = round(
        max(0.0, min(1.0, 0.70 * obs.quality + 0.30 * (1.0 if obs.trend != "unknown" else 0.5))),
        3,
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "source_id": obs.source_id,
        "domain": obs.domain,
        "simple_language": result["interpretation"],
        "confidence": confidence,
        "claim_level": result["claim_level"],
        "evidence_boundary": result["evidence_boundary"],
        "features": list(obs.features),
    }


def translate(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Validate a JSON-like observation and produce a deterministic NLP record."""
    obs = SignalObservation(
        source_id=str(payload.get("source_id", "")),
        domain=str(payload.get("domain", "unknown")),
        signal_type=str(payload.get("signal_type", "")),
        window_seconds=float(payload.get("window_seconds", 0)),
        baseline=float(payload.get("baseline", 0)),
        value=float(payload.get("value", 0)),
        trend=str(payload.get("trend", "unknown")),
        quality=float(payload.get("quality", 1)),
        features=tuple(str(x) for x in payload.get("features", ())),
    )
    return to_plain_language(obs)


def example_schema() -> dict[str, Any]:
    return {
        "source_id": "sensor-001",
        "domain": "plant|animal|environment|mechanical|other",
        "signal_type": "electrical|vibration|temperature|sound|motion|other",
        "window_seconds": 60,
        "baseline": 1.0,
        "value": 1.2,
        "trend": "rising",
        "quality": 0.95,
        "features": ["feature-a", "feature-b"],
    }


def as_record(obs: SignalObservation) -> dict[str, Any]:
    return asdict(obs)
