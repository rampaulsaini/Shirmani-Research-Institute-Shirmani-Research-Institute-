"""Evidence-first multimodal signal -> plain-language NLP engine.

The engine describes observable patterns and preserves uncertainty. It never treats
signal interpretation as proof of subjective experience, consciousness, emotion, or intent.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from statistics import mean
from typing import Any


@dataclass(frozen=True)
class Signal:
    modality: str
    value: float
    baseline: float = 0.0
    scale: float = 1.0
    unit: str = ""
    source_id: str = ""
    timestamp: str = ""

    def normalized_deviation(self) -> float:
        if self.scale <= 0:
            raise ValueError("scale must be positive")
        return (self.value - self.baseline) / self.scale


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _fingerprint(signals: list[Signal]) -> str:
    payload = json.dumps([asdict(s) for s in signals], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def interpret(
    signals: list[Signal],
    context: dict[str, Any] | None = None,
    *,
    labelled_evaluation: bool = False,
    agreement: float | None = None,
) -> dict[str, Any]:
    """Produce a reproducible, evidence-bounded natural-language interpretation."""
    context = context or {}

    if not signals:
        return {
            "status": "insufficient_data",
            "interpretation": {
                "statement": "कोई पर्याप्त observable signal उपलब्ध नहीं है; अभी विश्वसनीय interpretation नहीं बनाई जा सकती।",
                "confidence": 0.0,
                "evidence_grade": "D",
                "limitations": ["अपर्याप्त मापनीय डेटा"],
            },
            "features": {"modalities": 0, "independent_sources": 0, "sample_count": 0},
            "provenance": {"context": context, "signal_fingerprint": _fingerprint([])},
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    modalities = len({s.modality for s in signals if s.modality})
    sources = len({s.source_id for s in signals if s.source_id})
    deviations = [abs(s.normalized_deviation()) for s in signals]

    if agreement is None:
        signs = [s.normalized_deviation() >= 0 for s in signals]
        agreement = max(sum(signs), len(signs) - sum(signs)) / len(signs)

    strength = _clamp(mean(min(d, 1.0) for d in deviations))
    sample_factor = _clamp(len(signals) / 30.0)
    source_factor = _clamp(sources / 3.0)
    modality_factor = _clamp(modalities / 3.0)
    evaluation_factor = 1.0 if labelled_evaluation else 0.55

    confidence = _clamp(
        0.25 * strength
        + 0.20 * float(agreement)
        + 0.20 * sample_factor
        + 0.20 * source_factor
        + 0.10 * modality_factor
        + 0.05 * evaluation_factor
    )

    if confidence >= 0.80:
        grade = "A"
    elif confidence >= 0.65:
        grade = "B"
    elif confidence >= 0.45:
        grade = "C"
    else:
        grade = "D"

    direction = "ऊपर" if mean(s.normalized_deviation() for s in signals) >= 0 else "नीचे"
    statement = (
        f"मापे गए संकेत baseline की तुलना में औसतन {direction} बदले हुए हैं। "
        "यह observable signal-state change का वर्णन है; इसे प्रत्यक्ष subjective "
        "experience, consciousness, emotion या intent का प्रमाण नहीं माना गया है।"
    )

    limitations = [
        "observable signal से subjective experience सीधे सिद्ध नहीं होता",
        "labelled evaluation, independent replication और calibration से confidence जाँचना आवश्यक है",
    ]

    return {
        "status": "interpreted",
        "interpretation": {
            "statement": statement,
            "confidence": round(confidence, 4),
            "evidence_grade": grade,
            "limitations": limitations,
        },
        "features": {
            "modalities": modalities,
            "independent_sources": sources,
            "sample_count": len(signals),
            "agreement": round(float(agreement), 4),
            "signal_strength": round(strength, 4),
            "labelled_evaluation": labelled_evaluation,
            "evidence_grade": grade,
        },
        "provenance": {
            "context": context,
            "signal_fingerprint": _fingerprint(signals),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    sample = [
        Signal("demo", 1.8, 1.0, 1.0, "unit", "local-demo", "2026-10-01T00:00:00Z"),
        Signal("vibration", 1.4, 1.0, 1.0, "unit", "sensor-b", "2026-10-01T00:00:01Z"),
    ]
    print(json.dumps(interpret(sample), ensure_ascii=False, indent=2))
