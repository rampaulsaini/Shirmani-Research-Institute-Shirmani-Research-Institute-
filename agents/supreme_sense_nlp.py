"""Evidence-first multimodal signal -> simple-language NLP adapter.

The adapter is deliberately fail-closed: it translates measurable signals into
testable hypotheses, never into unverified claims about subjective experience.
"""
from __future__ import annotations

import hashlib
import json
from statistics import mean, pstdev
from typing import Any

ALLOWED_MODALITIES = {
    "audio", "electrical", "vibration", "temperature", "light", "motion",
    "chemical", "text", "image", "environmental",
}
QUALITY_FLOOR = 0.20
MIN_USABLE_SAMPLES = 2
MIN_MODALITIES_FOR_MULTIMODAL = 2


def _number(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def analyze(
    observations: list[dict[str, Any]],
    request: str = "signal interpretation",
) -> dict[str, Any]:
    clean: list[dict[str, Any]] = []
    for row in observations:
        modality = str(row.get("modality", "unknown")).strip().lower()
        value = _number(row.get("value", 0))
        quality = max(0.0, min(1.0, _number(row.get("quality", 0))))
        clean.append({
            "modality": modality,
            "feature": str(row.get("feature", "signal")),
            "value": value,
            "quality": quality,
            "source": str(row.get("source", "unknown")),
        })

    usable = [
        r for r in clean
        if r["modality"] in ALLOWED_MODALITIES and r["quality"] >= QUALITY_FLOOR
    ]
    modalities = sorted({r["modality"] for r in usable})
    sources = sorted({r["source"] for r in usable if r["source"] != "unknown"})
    qualities = [r["quality"] for r in usable]
    mean_quality = mean(qualities) if qualities else 0.0
    stability = 1.0
    if len(qualities) > 1:
        dispersion = pstdev(qualities)
        stability = max(0.0, min(1.0, 1.0 - dispersion))
    sample_factor = min(1.0, len(usable) / 20.0)
    modality_factor = min(1.0, len(modalities) / MIN_MODALITIES_FOR_MULTIMODAL)
    source_factor = min(1.0, len(sources) / 2.0)
    confidence = (
        0.55 * mean_quality
        + 0.20 * stability
        + 0.15 * sample_factor
        + 0.05 * modality_factor
        + 0.05 * source_factor
    )
    confidence = round(max(0.0, min(1.0, confidence)), 6)

    sufficient = len(usable) >= MIN_USABLE_SAMPLES
    fp = hashlib.sha256(
        json.dumps(clean, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()

    status = "CANDIDATE" if sufficient else "NO_CLAIM"
    return {
        "status": status,
        "request": request,
        "observations": clean,
        "summary": {
            "usable_observations": len(usable),
            "mean_quality": round(mean_quality, 6),
            "quality_stability": round(stability, 6),
            "modalities": len(modalities),
            "independent_sources": len(sources),
            "sample_count": len(usable),
        },
        "interpretation": {
            "type": "measurable-signal-hypothesis",
            "subjective_experience_proven": False,
            "confidence_basis": "quality+stability+sample+modality+source",
        },
        "confidence": confidence,
        "calibration": {
            "method": "deterministic_heuristic_v2",
            "requires_labelled_validation": True,
            "validated": False,
        },
        "verification": {
            "status": "UNVERIFIED",
            "promotion_allowed": False,
            "independent_verification_required": True,
        },
        "governance": {
            "fail_closed": True,
            "abstain_when_insufficient_evidence": True,
            "accuracy_is_measured_not_declared": True,
            "subjective_experience_claim_allowed": False,
            "scheduled_code_mutation_allowed": False,
        },
        "fingerprint": fp,
    }


def to_simple_language(record: dict[str, Any]) -> str:
    s = record["summary"]
    if not s["usable_observations"]:
        return "पर्याप्त विश्वसनीय मापनीय संकेत उपलब्ध नहीं हैं; इसलिए कोई निष्कर्ष नहीं दिया गया।"
    confidence = record.get("confidence", 0.0)
    return (
        f"प्रणाली ने {s['usable_observations']} उपयोगी मापनीय संकेत देखे और "
        f"{s['modalities']} प्रकार के संकेतों का विश्लेषण किया। "
        f"औसत डेटा-गुणवत्ता {s['mean_quality']:.1%} और अनुमानित "
        f"विश्वास-स्तर {confidence:.1%} है। यह केवल परीक्षणयोग्य परिकल्पना है; "
        "किसी व्यक्तिपरक अनुभव का प्रत्यक्ष प्रमाण अभी स्थापित नहीं है।"
    )
