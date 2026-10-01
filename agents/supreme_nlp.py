"""Supreme NLP: observable-signal -> conservative, auditable plain-language interpretation.

The baseline interpreter is deliberately model-agnostic. Domain models can replace
it without changing the evidence, provenance, uncertainty or safety contract.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from math import isfinite, sqrt
from typing import Any, Dict, Iterable, List
import hashlib
import json


@dataclass(frozen=True)
class Signal:
    modality: str
    feature: str
    value: float
    unit: str = ""
    quality: float = 1.0
    source: str = "unknown"
    timestamp: str = ""
    sensor_id: str = ""


def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))


def normalize_signal(raw: Dict[str, Any]) -> Signal:
    value = float(raw.get("value", 0.0))
    if not isfinite(value):
        raise ValueError("signal value must be finite")
    quality = _clip(raw.get("quality", 1.0))
    return Signal(
        modality=str(raw.get("modality", "unknown")).strip() or "unknown",
        feature=str(raw.get("feature", "unknown")).strip() or "unknown",
        value=value,
        unit=str(raw.get("unit", "")),
        quality=quality,
        source=str(raw.get("source", "unknown")).strip() or "unknown",
        timestamp=str(raw.get("timestamp", "")),
        sensor_id=str(raw.get("sensor_id", "")),
    )


def _evidence_grade(count: int, quality: float, modalities: int, agreement: float) -> str:
    score = (
        0.35 * _clip(count / 10)
        + 0.30 * quality
        + 0.20 * _clip(modalities / 3)
        + 0.15 * agreement
    )
    return "A" if score >= .85 else "B" if score >= .70 else "C" if score >= .50 else "D"


def _quality_diagnostics(rows: List[Signal]) -> Dict[str, Any]:
    if not rows:
        return {"input_count": 0, "usable_count": 0, "dropped_count": 0, "mean_quality": 0.0}
    usable = [s for s in rows if s.quality > 0]
    return {
        "input_count": len(rows),
        "usable_count": len(usable),
        "dropped_count": len(rows) - len(usable),
        "mean_quality": round(sum(s.quality for s in rows) / len(rows), 4),
    }


def summarize(signals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    rows: List[Signal] = []
    rejected: List[str] = []
    for raw in signals:
        try:
            rows.append(normalize_signal(raw))
        except (TypeError, ValueError) as exc:
            rejected.append(str(exc))

    if not rows:
        return {
            "status": "no_data",
            "interpretation": None,
            "signals": [],
            "quality_diagnostics": {
                "input_count": 0, "usable_count": 0, "dropped_count": 0, "mean_quality": 0.0
            },
            "rejected_inputs": rejected,
        }

    usable = [s for s in rows if s.quality > 0]
    diagnostics = _quality_diagnostics(rows)
    if not usable:
        return {
            "status": "insufficient_quality",
            "interpretation": None,
            "signals": [asdict(s) for s in rows],
            "quality_diagnostics": diagnostics,
            "rejected_inputs": rejected,
        }

    mean = sum(s.value for s in usable) / len(usable)
    variance = sum((s.value - mean) ** 2 for s in usable) / len(usable)
    spread = sqrt(variance)
    quality = sum(s.quality for s in usable) / len(usable)
    modalities = len({s.modality for s in usable})

    # Robust bounded variability indicator. It is a pattern statistic, not an
    # emotional/mental-state classifier.
    anomaly = _clip((spread / (abs(mean) + 1e-9)) / 3.0)
    agreement = 1.0 - anomaly

    if anomaly >= .66:
        state = "high_variability_pattern"
    elif anomaly >= .33:
        state = "moderate_variability_pattern"
    else:
        state = "stable_pattern"

    # Conservative confidence is intentionally capped below certainty until a
    # calibrated domain model and independent validation dataset are supplied.
    confidence = _clip(
        .15 + .40 * quality + .20 * agreement + .15 * _clip(len(usable) / 10)
        + .10 * _clip(modalities / 3),
        0.0,
        0.95,
    )

    evidence = [
        {
            "modality": s.modality,
            "feature": s.feature,
            "value": s.value,
            "unit": s.unit,
            "quality": round(s.quality, 4),
            "source": s.source,
            "timestamp": s.timestamp,
            "sensor_id": s.sensor_id,
        }
        for s in usable
    ]
    limitations = [
        "यह observable signals की model-based interpretation है, subjective feeling का direct proof नहीं।",
        "Biological/physical claims के लिए domain calibration, labelled data और independent replication आवश्यक हैं।",
        "Confidence pipeline evidence quality का bounded estimate है; scientific certainty नहीं।",
        "समान signal pattern के अनेक कारण हो सकते हैं; causal explanation अलग validation stage है।",
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
            "mean": mean,
            "spread": spread,
            "anomaly_score": anomaly,
            "agreement": agreement,
            "quality": quality,
            "modalities": modalities,
            "evidence_grade": _evidence_grade(len(usable), quality, modalities, agreement),
        },
        "signals": [asdict(s) for s in rows],
        "quality_diagnostics": diagnostics,
        "rejected_inputs": rejected,
    }


def to_simple_language(result: Dict[str, Any]) -> str:
    if result.get("status") != "interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला संकेत उपलब्ध नहीं है, इसलिए विश्वसनीय व्याख्या नहीं दी जा सकती।"
    i, f = result["interpretation"], result["features"]
    return (
        f"मिले हुए संकेतों में '{i['state']}' जैसा पैटर्न दिखाई देता है। "
        f"Bounded confidence {i['confidence']:.0%}, evidence grade {f['evidence_grade']} है। "
        "यह मापे गए संकेतों की व्याख्या है; इसे किसी जीव के प्रत्यक्ष भाव या चेतना का प्रमाण नहीं माना जाना चाहिए।"
    )


def fingerprint(result: Dict[str, Any]) -> str:
    payload = json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_record(signals: Iterable[Dict[str, Any]], task_id: str) -> Dict[str, Any]:
    result = summarize(signals)
    generated_at = datetime.now(timezone.utc).isoformat()
    return {
        "schema_version": "1.2",
        "task_id": task_id,
        "generated_at": generated_at,
        "pipeline": "observe->normalize->quality->feature->fusion->interpret->NLP->audit",
        "provenance": {
            "input_contract": "observable-signal-v1",
            "source_count": result.get("quality_diagnostics", {}).get("usable_count", 0),
            "generated_by": "agents.supreme_nlp.build_record",
        },
        "uncertainty": {
            "confidence_is_calibrated": False,
            "independent_verification": "NOT_VERIFIED",
            "causal_claim": "NOT_ESTABLISHED",
        },
        "result": result,
        "simple_language": to_simple_language(result),
        "fingerprint": fingerprint(result),
    }
