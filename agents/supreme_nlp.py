"""Evidence-first multimodal signal -> language translation core.

This module deliberately separates observed signals from interpretation.
It never treats an inferred state as proof of subjective experience.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from statistics import mean, pstdev
from typing import Iterable, Mapping, Any
import math, json, hashlib


@dataclass(frozen=True)
class Signal:
    name: str
    value: float
    unit: str = ""
    timestamp: str = ""
    source: str = ""


@dataclass(frozen=True)
class Interpretation:
    state: str
    confidence: float
    evidence: tuple[str, ...]
    limitations: tuple[str, ...]


def _clamp(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def summarize_signals(signals: Iterable[Signal]) -> dict[str, Any]:
    xs = list(signals)
    values = [float(s.value) for s in xs]
    if not values:
        return {"count": 0, "mean": None, "std": None, "min": None, "max": None}
    return {
        "count": len(values),
        "mean": mean(values),
        "std": pstdev(values) if len(values) > 1 else 0.0,
        "min": min(values),
        "max": max(values),
    }


def translate(signals: Iterable[Signal], context: Mapping[str, Any] | None = None) -> Interpretation:
    """Create a conservative natural-language interpretation from numeric signals.

    Domain models can replace this heuristic while retaining the same contract.
    """
    xs = list(signals)
    summary = summarize_signals(xs)
    if not xs:
        return Interpretation(
            "कोई पर्याप्त संकेत उपलब्ध नहीं हैं", 0.0, (), ("अपर्याप्त डेटा",)
        )

    spread = float(summary["std"] or 0.0)
    count = int(summary["count"])
    # Stability is a property of the observed series, not an emotional claim.
    stability = 1.0 / (1.0 + spread)
    coverage = 1.0 - math.exp(-count / 10.0)
    confidence = _clamp(0.5 * stability + 0.5 * coverage)

    if spread < 0.1:
        state = "संकेत अपेक्षाकृत स्थिर दिखाई दे रहे हैं"
    elif spread < 1.0:
        state = "संकेतों में मध्यम परिवर्तन दिखाई दे रहा है"
    else:
        state = "संकेतों में स्पष्ट उतार-चढ़ाव दिखाई दे रहा है"

    evidence = tuple(
        f"{s.name}={s.value:g}{s.unit}" + (f" @ {s.timestamp}" if s.timestamp else "")
        for s in xs[:20]
    )
    limitations = (
        "यह observable signal की व्याख्या है; subjective भावना का प्रत्यक्ष प्रमाण नहीं।",
        "विश्वसनीय निष्कर्ष के लिए calibrated sensors, labelled data और independent validation आवश्यक हैं।",
    )
    return Interpretation(state, round(confidence, 6), evidence, limitations)


def make_record(signals: Iterable[Signal], context: Mapping[str, Any] | None = None) -> dict[str, Any]:
    xs = list(signals)
    interpretation = translate(xs, context)
    payload = {
        "schema_version": "1.0",
        "signals": [asdict(s) for s in xs],
        "interpretation": asdict(interpretation),
        "context": dict(context or {}),
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    payload["record_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return payload
