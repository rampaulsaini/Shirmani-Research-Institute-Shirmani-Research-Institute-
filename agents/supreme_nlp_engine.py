"""Evidence-aware multimodal signal -> NLP interpretation engine.

The engine translates observable/encoded signals into human-readable language while
preserving uncertainty, provenance, limitations, and verification boundaries.
It does not claim direct access to subjective experience.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Signal:
    modality: str
    value: float
    unit: str = ""
    source_id: str = ""
    timestamp: str = ""


def _fingerprint(signals: list[Signal]) -> str:
    payload = json.dumps(
        [asdict(s) for s in signals],
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _quality(signals: list[Signal]) -> float:
    if not signals:
        return 0.0
    complete = sum(bool(s.modality and s.source_id and s.timestamp) for s in signals)
    return round(complete / len(signals), 3)


def _conservative_agreement(signals: list[Signal]) -> float:
    # This is a structural consistency proxy, not proof of semantic agreement.
    if len(signals) < 2:
        return 0.0
    units = {s.unit for s in signals if s.unit}
    if len(units) != 1:
        return 0.0
    values = [float(s.value) for s in signals]
    scale = max(abs(v) for v in values)
    if scale == 0:
        return 1.0
    spread = max(values) - min(values)
    return round(max(0.0, 1.0 - min(1.0, spread / scale)), 3)


def interpret(
    signals: list[Signal],
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = context or {}
    modalities = len({s.modality for s in signals if s.modality})
    sources = len({s.source_id for s in signals if s.source_id})
    quality = _quality(signals)
    agreement = _conservative_agreement(signals)
    complete = sum(bool(s.timestamp and s.source_id) for s in signals)

    # This is a deterministic evidence/coverage proxy. It is not calibrated
    # predictive probability and must be evaluated against labelled data.
    confidence = (
        min(
            0.99,
            0.30
            + 0.10 * min(modalities, 4)
            + 0.08 * min(sources, 4)
            + 0.03 * min(complete, 10)
            + 0.10 * agreement
            + 0.10 * quality,
        )
        if signals
        else 0.0
    )
    grade = (
        "A"
        if confidence >= 0.80 and quality >= 0.90 and agreement >= 0.70
        else "B"
        if confidence >= 0.65 and quality >= 0.70
        else "C"
    )

    status = "interpreted" if signals else "insufficient_quality"
    if not signals:
        statement = (
            "कोई पर्याप्त observable signal उपलब्ध नहीं है; "
            "अभी विश्वसनीय interpretation नहीं बनाई जा सकती।"
        )
    else:
        statement = (
            f"{modalities} प्रकार के observable signal और {sources} source मिले हैं। "
            "डेटा में एक signal pattern दर्ज हुआ है। इसे प्रत्यक्ष subjective "
            "experience का प्रमाण न मानते हुए signal-based interpretation के रूप "
            "में पढ़ना चाहिए।"
        )

    generated_at = datetime.now(timezone.utc).isoformat()
    fingerprint = _fingerprint(signals)
    limitations = [
        "observable signal से subjective experience सीधे सिद्ध नहीं होता",
        "confidence एक deterministic evidence/coverage proxy है; calibrated probability नहीं",
        "model output को labelled evaluation और independent validation से calibrate करना आवश्यक है",
    ]

    result = {
        "status": status,
        "language": "hi",
        "intent": str(context.get("intent", "signal_interpretation")),
        "features": {
            "confidence": round(confidence, 3),
            "agreement": agreement,
            "quality": quality,
            "modalities": modalities,
            "sources": sources,
            "independent_sources": sources,
            "sample_count": len(signals),
            "evidence_grade": grade,
        },
    }

    return {
        "schema_version": "1.0",
        "generated_at": generated_at,
        "pipeline": (
            "Observe -> Collect -> Clean -> Analyze -> Reason -> "
            "Translate -> Verify -> Audit -> Improve"
        ),
        "simple_language": statement,
        "fingerprint": fingerprint,
        "result": result,
        # Backward-compatible fields used by the deterministic quality gate.
        "status": status,
        "interpretation": {
            "statement": statement,
            "confidence": round(confidence, 3),
            "evidence_grade": grade,
            "limitations": limitations,
        },
        "features": result["features"],
        "provenance": {
            "context": context,
            "signal_fingerprint": fingerprint,
        },
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "code_mutation_allowed": False,
            "independent_verification_required": True,
        },
    }


if __name__ == "__main__":
    sample = [
        Signal("demo", 1.0, "unit", "local-demo", "2026-10-01T00:00:00Z")
    ]
    print(json.dumps(interpret(sample), ensure_ascii=False, indent=2))
