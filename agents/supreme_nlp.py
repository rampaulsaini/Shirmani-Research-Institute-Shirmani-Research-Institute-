"""Supreme NLP: observable multimodal signals -> conservative, auditable language.

The baseline is dependency-light and deterministic. Domain ML models can replace
individual feature stages without changing the evidence, uncertainty and
verification contract.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import sqrt, isfinite
from typing import Any, Dict, Iterable
import hashlib, json

VERSION = "supreme-nlp-v2"

@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    unit: str = ""
    quality: float = 1.0
    source: str = "unknown"
    timestamp: str = ""
    baseline_mean: float | None = None
    baseline_std: float | None = None

def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        return max(lo, min(hi, float(x)))
    except (TypeError, ValueError):
        return lo

def normalize_signal(raw: Dict[str, Any]) -> Signal:
    try:
        value = float(raw.get("value", 0.0))
    except (TypeError, ValueError):
        value = 0.0
    if not isfinite(value):
        value = 0.0
    def opt_num(name):
        try:
            v = raw.get(name)
            return None if v is None else float(v)
        except (TypeError, ValueError):
            return None
    return Signal(
        modality=str(raw.get("modality", "unknown")),
        feature=str(raw.get("feature", "unknown")),
        value=value,
        unit=str(raw.get("unit", "")),
        quality=_clip(raw.get("quality", 1.0)),
        source=str(raw.get("source", "unknown")),
        timestamp=str(raw.get("timestamp", "")),
        baseline_mean=opt_num("baseline_mean"),
        baseline_std=opt_num("baseline_std"),
    )

def _evidence_grade(count: int, quality: float, modalities: int, sources: int) -> str:
    score = (
        0.35 * _clip(count / 20) +
        0.30 * quality +
        0.20 * _clip(modalities / 4) +
        0.15 * _clip(sources / 3)
    )
    return "A" if score >= .85 else "B" if score >= .70 else "C" if score >= .50 else "D"

def _baseline_drift(rows: list[Signal]) -> float:
    candidates = []
    for s in rows:
        if s.baseline_mean is None:
            continue
        scale = abs(s.baseline_std or 0.0)
        if scale <= 1e-12:
            scale = max(abs(s.baseline_mean), 1.0)
        candidates.append(min(1.0, abs(s.value - s.baseline_mean) / (3.0 * scale)))
    return sum(candidates) / len(candidates) if candidates else 0.0

def summarize(signals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [normalize_signal(x) for x in signals]
    if not rows:
        return {"status": "no_observable_signal", "interpretation": None, "signals": []}
    usable = [s for s in rows if s.quality > 0]
    if not usable:
        return {"status": "insufficient_quality", "interpretation": None,
                "signals": [asdict(s) for s in rows]}

    mean = sum(s.value for s in usable) / len(usable)
    variance = sum((s.value - mean) ** 2 for s in usable) / len(usable)
    spread = sqrt(max(variance, 0.0))
    quality = sum(s.quality for s in usable) / len(usable)
    modalities = len({s.modality for s in usable})
    sources = len({s.source for s in usable if s.source != "unknown"})
    anomaly = _clip((spread / (abs(mean) + 1e-9)) / 3.0)
    agreement = 1.0 - anomaly
    drift_score = _baseline_drift(usable)

    if anomaly >= .66:
        state = "high_variability_pattern"
    elif anomaly >= .33:
        state = "moderate_variability_pattern"
    else:
        state = "stable_pattern"

    raw_confidence = _clip(
        .15 + .35 * quality + .20 * agreement +
        .15 * _clip(len(usable) / 20) + .10 * _clip(modalities / 4) +
        .05 * _clip(sources / 3)
    )
    confidence = round(raw_confidence, 4)
    evidence = [
        f"{s.modality}:{s.feature}={s.value}{s.unit} "
        f"(quality={s.quality:.2f}; source={s.source})"
        for s in usable
    ]
    limitations = [
        "यह observable signals की model-based interpretation है, subjective feeling का direct proof नहीं।",
        "Biological/physical claims के लिए domain calibration, labelled data और independent replication आवश्यक हैं।",
        "Confidence UNCALIBRATED है जब तक labelled evaluation data से calibration स्थापित न हो।",
        "Alternative explanations और sensor artefacts को independent testing से अलग करना आवश्यक है।",
    ]
    return {
        "status": "interpreted",
        "interpretation": {
            "state": state,
            "confidence": confidence,
            "confidence_status": "UNCALIBRATED",
            "evidence": evidence,
            "limitations": limitations,
        },
        "features": {
            "mean": mean, "spread": spread, "anomaly_score": anomaly,
            "agreement": agreement, "quality": quality,
            "modalities": modalities, "independent_sources": sources,
            "sample_count": len(usable), "drift_score": round(drift_score, 4),
            "evidence_grade": _evidence_grade(len(usable), quality, modalities, sources),
        },
        "verification": {
            "status": "UNVERIFIED", "independent_required": True,
            "replication_required": True,
        },
        "signals": [asdict(s) for s in rows],
    }

def to_simple_language(result: Dict[str, Any]) -> str:
    if result.get("status") != "interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है, इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i, f = result["interpretation"], result["features"]
    return (
        f"मिले हुए संकेतों में '{i['state']}' जैसा पैटर्न दिखाई देता है। "
        f"प्रारंभिक confidence {i['confidence']:.0%} है और evidence grade {f['evidence_grade']} है। "
        "यह observable संकेतों की व्याख्या है; इसे किसी जीव के प्रत्यक्ष भाव, चेतना या subjective experience का प्रमाण नहीं माना जाना चाहिए।"
    )

def fingerprint(result: Dict[str, Any]) -> str:
    payload = json.dumps(result, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def build_record(signals: Iterable[Dict[str, Any]], task_id: str) -> Dict[str, Any]:
    result = summarize(signals)
    return {
        "schema_version": VERSION,
        "task_id": task_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "observe->normalize->quality->feature->multimodal->interpret->NLP->confidence->verification->audit",
        "result": result,
        "simple_language": to_simple_language(result),
        "fingerprint": fingerprint(result),
        "provenance": {
            "generator": "agents/supreme_nlp.py",
            "contract": "observable-signal-only",
            "verification_status": "UNVERIFIED",
        },
    }
