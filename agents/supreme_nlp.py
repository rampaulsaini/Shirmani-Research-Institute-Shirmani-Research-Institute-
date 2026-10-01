"""Supreme NLP signal-to-language layer.

Turns observable multimodal signals into conservative, human-readable
interpretations. It never treats a model inference as proof of subjective
experience; claims must remain traceable to measurements and evidence.
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

@dataclass(frozen=True)
class Interpretation:
    state: str
    confidence: float
    evidence: List[str]
    limitations: List[str]

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
    )

def summarize(signals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [normalize_signal(x) for x in signals]
    if not rows:
        return {"status": "no_data", "interpretation": None, "signals": []}

    usable = [s for s in rows if s.quality > 0]
    if not usable:
        return {"status": "insufficient_quality", "interpretation": None,
                "signals": [asdict(s) for s in rows]}

    # Generic, domain-neutral anomaly score. Domain models can replace this
    # function while preserving the same evidence/uncertainty contract.
    mean = sum(s.value for s in usable) / len(usable)
    variance = sum((s.value - mean) ** 2 for s in usable) / len(usable)
    spread = sqrt(variance)
    quality = sum(s.quality for s in usable) / len(usable)
    anomaly = _clip((spread / (abs(mean) + 1e-9)) / 3.0)

    if anomaly >= 0.66:
        state = "high_variability_pattern"
    elif anomaly >= 0.33:
        state = "moderate_variability_pattern"
    else:
        state = "stable_pattern"

    confidence = _clip(0.35 + 0.45 * quality + 0.20 * (1.0 - min(anomaly, 1.0)))
    evidence = [
        f"{s.modality}:{s.feature}={s.value}{s.unit} (quality={s.quality:.2f})"
        for s in usable
    ]
    limitations = [
        "This is an interpretation of observable signals, not proof of subjective feeling.",
        "Domain-specific calibration and labelled data are required before biological claims.",
        "Confidence reflects this pipeline's evidence quality, not scientific certainty.",
    ]
    return {
        "status": "interpreted",
        "interpretation": asdict(Interpretation(state, round(confidence, 4), evidence, limitations)),
        "signals": [asdict(s) for s in rows],
        "features": {"mean": mean, "spread": spread, "anomaly_score": anomaly},
    }

def to_simple_language(result: Dict[str, Any]) -> str:
    if result.get("status") != "interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है, इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i = result["interpretation"]
    return (
        f"मिले हुए संकेतों में '{i['state']}' जैसा पैटर्न दिखाई देता है। "
        f"इस मॉडल का confidence {i['confidence']:.0%} है। "
        "यह संकेतों की व्याख्या है; इसे किसी जीव के प्रत्यक्ष भाव या चेतना का प्रमाण नहीं माना जाना चाहिए।"
    )

def fingerprint(result: Dict[str, Any]) -> str:
    payload = json.dumps(result, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def build_record(signals: Iterable[Dict[str, Any]], task_id: str) -> Dict[str, Any]:
    result = summarize(signals)
    return {
        "schema_version": "1.0",
        "task_id": task_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "observe->normalize->feature->interpret->NLP->audit",
        "result": result,
        "simple_language": to_simple_language(result),
        "fingerprint": fingerprint(result),
    }
