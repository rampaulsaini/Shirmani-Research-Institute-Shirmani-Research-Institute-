"""Supreme evidence-fusion layer: observable signals -> plain-language NLP.

This layer is deterministic and evidence-first. It can represent signals from
humans, animals, plants, environments and non-living systems, but it does not
convert measurements into claims of subjective experience.
"""
from __future__ import annotations
import hashlib, json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from statistics import mean, pstdev
from typing import Any

@dataclass(frozen=True)
class ObservedSignal:
    source_type: str
    modality: str
    feature: str
    value: float
    quality: float
    source_id: str
    observed_at: str

def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))

def _fingerprint(signals: list[ObservedSignal]) -> str:
    payload = json.dumps([asdict(s) for s in signals], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def _agreement(signals: list[ObservedSignal]) -> float:
    values = [s.value for s in signals if s.quality > 0]
    if len(values) < 2:
        return 0.0 if not values else 1.0
    spread = pstdev(values)
    scale = max(abs(mean(values)), 1.0)
    return _clamp(1.0 - spread / scale)

def fuse(signals: list[ObservedSignal], context: dict[str, Any] | None = None) -> dict[str, Any]:
    context = context or {}
    valid = [
        s for s in signals
        if s.source_id and s.modality and s.feature and 0.0 <= s.quality <= 1.0
    ]
    modalities = sorted({s.modality for s in valid})
    sources = sorted({s.source_id for s in valid})
    source_types = sorted({s.source_type for s in valid})
    quality = mean([s.quality for s in valid]) if valid else 0.0
    agreement = _agreement(valid)
    diversity = _clamp(len(modalities) / 3.0)
    replication = _clamp(len(sources) / 3.0)
    confidence = _clamp(0.15 * quality + 0.20 * agreement + 0.30 * diversity + 0.35 * replication)

    if not valid:
        status = "INSUFFICIENT_DATA"
        statement = "पर्याप्त सत्यापनयोग्य observable signal उपलब्ध नहीं है।"
    elif confidence >= 0.80 and len(modalities) >= 2 and len(sources) >= 2:
        status = "EVIDENCE_SUPPORTED_INTERPRETATION"
        statement = (
            f"{len(valid)} observable signals में {len(modalities)} modalities और "
            f"{len(sources)} source IDs का pattern मिला है। यह signal-based "
            "interpretation है; subjective experience का प्रत्यक्ष प्रमाण नहीं।"
        )
    else:
        status = "PRELIMINARY_INTERPRETATION"
        statement = (
            f"{len(valid)} observable signals का प्रारंभिक pattern मिला है। "
            "अधिक independent evidence और labelled validation की आवश्यकता है।"
        )

    return {
        "record_version": "1.0",
        "status": status,
        "observed_signal": {
            "count": len(valid),
            "source_types": source_types,
            "modalities": modalities,
            "independent_sources": len(sources),
        },
        "inference": {
            "plain_language": statement,
            "confidence": round(confidence, 4),
            "agreement": round(agreement, 4),
            "mean_quality": round(quality, 4),
        },
        "verification": {
            "status": "UNVERIFIED",
            "independent_verification_required": True,
            "counter_evidence_required": True,
        },
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "scheduled_code_mutation_allowed": False,
        },
        "provenance": {
            "context": context,
            "signal_fingerprint": _fingerprint(valid),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
        "limitations": [
            "observable signal से subjective experience सीधे सिद्ध नहीं होता",
            "confidence statistical/quality indicators से निकाला गया है, सत्य की गारंटी नहीं",
            "independent labelled evaluation और counter-evidence testing आवश्यक है",
        ],
    }
