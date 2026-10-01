"""Supreme NLP: observable-signal -> conservative plain-language interpretation.

Design contract:
- multimodal records are normalized before interpretation;
- uncertainty and data quality are explicit;
- inferred states are never presented as proof of subjective experience;
- every output carries provenance and a deterministic fingerprint;
- domain-specific models can replace the baseline interpreter without changing
  the evidence/uncertainty contract.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import sqrt
from typing import Any, Dict, Iterable, List
import hashlib, json

@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    unit: str = ""
    quality: float = 1.0
    source: str = "unknown"
    timestamp: str = ""

def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))

def normalize_signal(raw: Dict[str, Any]) -> Signal:
    return Signal(
        modality=str(raw.get("modality", "unknown")),
        feature=str(raw.get("feature", "unknown")),
        value=float(raw.get("value", 0.0)),
        unit=str(raw.get("unit", "")),
        quality=_clip(raw.get("quality", 1.0)),
        source=str(raw.get("source", "unknown")),
        timestamp=str(raw.get("timestamp", "")),
    )

def _evidence_grade(count: int, quality: float, modalities: int) -> str:
    score = 0.5 * _clip(count / 10) + 0.35 * quality + 0.15 * _clip(modalities / 3)
    return "A" if score >= .85 else "B" if score >= .70 else "C" if score >= .50 else "D"

def summarize(signals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [normalize_signal(x) for x in signals]
    if not rows:
        return {"status": "no_data", "interpretation": None, "signals": []}

    usable = [s for s in rows if s.quality > 0]
    if not usable:
        return {"status": "insufficient_quality", "interpretation": None,
                "signals": [asdict(s) for s in rows]}

    mean = sum(s.value for s in usable) / len(usable)
    variance = sum((s.value - mean) ** 2 for s in usable) / len(usable)
    spread = sqrt(variance)
    quality = sum(s.quality for s in usable) / len(usable)
    modalities = len({s.modality for s in usable})
    anomaly = _clip((spread / (abs(mean) + 1e-9)) / 3.0)

    if anomaly >= .66:
        state = "high_variability_pattern"
    elif anomaly >= .33:
        state = "moderate_variability_pattern"
    else:
        state = "stable_pattern"

    # Conservative confidence: evidence quality is bounded and disagreement
    # lowers confidence rather than being hidden.
    agreement = 1.0 - anomaly
    confidence = _clip(.20 + .45 * quality + .20 * agreement + .15 * _clip(len(usable) / 10))
    evidence = [
        f"{s.modality}:{s.feature}={s.value}{s.unit} (quality={s.quality:.2f}; source={s.source})"
        for s in usable
    ]
    limitations = [
        "यह observable signals की model-based interpretation है, subjective feeling का direct proof नहीं।",
        "Biological/physical claims के लिए domain calibration, labelled data और independent replication आवश्यक हैं।",
        "Confidence इस pipeline की evidence quality को दर्शाता है, scientific certainty को नहीं।",
    ]
    return {
        "status": "interpreted",
        "interpretation": {
            "state": state,
            "confidence": round(confidence, 4),
            "evidence": evidence,
            "limitations": limitations,
        },
        "features": {
            "mean": mean, "spread": spread, "anomaly_score": anomaly,
            "agreement": agreement, "quality": quality,
            "modalities": modalities, "evidence_grade": _evidence_grade(len(usable), quality, modalities),
        },
        "signals": [asdict(s) for s in rows],
    }

def to_simple_language(result: Dict[str, Any]) -> str:
    if result.get("status") != "interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है, इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i, f = result["interpretation"], result["features"]
    return (
        f"मिले हुए संकेतों में '{i['state']}' जैसा पैटर्न दिखाई देता है। "
        f"Confidence {i['confidence']:.0%}, evidence grade {f['evidence_grade']} है। "
        "यह संकेतों की व्याख्या है; इसे किसी जीव के प्रत्यक्ष भाव या चेतना का प्रमाण नहीं माना जाना चाहिए।"
    )

def fingerprint(result: Dict[str, Any]) -> str:
    payload = json.dumps(result, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def build_record(signals: Iterable[Dict[str, Any]], task_id: str) -> Dict[str, Any]:
    result = summarize(signals)
    return {
        "schema_version": "1.1",
        "task_id": task_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "observe->normalize->quality->feature->interpret->NLP->audit",
        "result": result,
        "simple_language": to_simple_language(result),
        "fingerprint": fingerprint(result),
    }
