"""Supreme Multimodal NLP — evidence-preserving signal-to-language engine.

Dependency-free control-plane component for the SHIRMANI Automission stack.
It fuses measurable observations across modalities, exposes counter-evidence,
estimates bounded confidence, and produces plain-language explanations.

Important boundary:
- A signal is evidence of a measured pattern, not proof of subjective feeling.
- Confidence is a bounded score, not a probability of truth unless externally calibrated.
- No production code mutation or autonomous high-impact action is performed.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib, json, math, re
from statistics import median
from typing import Any, Iterable

SCHEMA_VERSION = "1.0"

@dataclass(frozen=True)
class Observation:
    modality: str
    feature: str
    value: float
    quality: float = 1.0
    source: str = "unknown"
    unit: str = ""
    timestamp: str = ""
    baseline: float | None = None

    def normalized(self) -> "Observation":
        return Observation(
            modality=self.modality.strip().lower() or "unknown",
            feature=self.feature.strip().lower() or "unknown",
            value=float(self.value),
            quality=max(0.0, min(1.0, float(self.quality))),
            source=self.source.strip() or "unknown",
            unit=self.unit.strip(),
            timestamp=self.timestamp.strip(),
            baseline=None if self.baseline is None else float(self.baseline),
        )

def normalize(raw: dict[str, Any]) -> Observation:
    return Observation(
        modality=str(raw.get("modality", "unknown")),
        feature=str(raw.get("feature", "unknown")),
        value=float(raw.get("value", 0.0)),
        quality=float(raw.get("quality", 1.0)),
        source=str(raw.get("source", "unknown")),
        unit=str(raw.get("unit", "")),
        timestamp=str(raw.get("timestamp", "")),
        baseline=raw.get("baseline"),
    ).normalized()

def _clip(value: float) -> float:
    return max(0.0, min(1.0, float(value)))

def _mad(values: list[float]) -> float:
    if not values:
        return 0.0
    m = median(values)
    return median([abs(v - m) for v in values])

def _robust_deviation(value: float, values: list[float]) -> float:
    if len(values) < 3:
        return 0.0
    m = median(values)
    mad = _mad(values)
    if mad <= 1e-12:
        return 0.0 if math.isclose(value, m) else 1.0
    return _clip(abs(value - m) / (6.0 * mad))

def _trend(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    n = len(values)
    x_mean = (n - 1) / 2.0
    y_mean = sum(values) / n
    denom = sum((i - x_mean) ** 2 for i in range(n))
    if denom == 0:
        return 0.0
    slope = sum((i - x_mean) * (y - y_mean) for i, y in enumerate(values)) / denom
    scale = _mad(values) or (abs(y_mean) + 1e-9)
    return _clip(abs(slope) / (6.0 * scale))

def _language(text: str) -> str:
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    if re.search(r"[\u0A00-\u0A7F]", text):
        return "pa"
    return "en"

def _fingerprint(payload: Any) -> str:
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def analyze(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    rows = [normalize(x) for x in observations]
    usable = [x for x in rows if x.quality > 0]
    if not usable:
        return {
            "status": "insufficient_quality",
            "schema_version": SCHEMA_VERSION,
            "observations": [asdict(x) for x in rows],
            "interpretation": None,
            "counter_evidence": ["No observation passed the minimum quality boundary."],
            "limitations": ["No inference is produced without usable evidence."],
        }

    grouped: dict[tuple[str, str], list[Observation]] = {}
    for row in usable:
        grouped.setdefault((row.modality, row.feature), []).append(row)

    summaries = []
    for (modality, feature), group in sorted(grouped.items()):
        values = [x.value for x in group]
        qualities = [x.quality for x in group]
        mean = sum(values) / len(values)
        baseline_values = [x.baseline for x in group if x.baseline is not None]
        baseline = sum(baseline_values) / len(baseline_values) if baseline_values else None
        baseline_shift = (
            _clip(abs(mean - baseline) / (abs(baseline) + 1e-9) / 3.0)
            if baseline is not None else 0.0
        )
        variability = (
            _clip((max(values) - min(values)) / (abs(mean) + 1e-9) / 3.0)
            if len(values) > 1 else 0.0
        )
        summaries.append({
            "modality": modality,
            "feature": feature,
            "samples": len(values),
            "mean": mean,
            "quality": sum(qualities) / len(qualities),
            "baseline": baseline,
            "baseline_shift": baseline_shift,
            "variability": variability,
            "anomaly": _robust_deviation(mean, values),
            "trend": _trend(values),
            "sources": sorted({x.source for x in group}),
        })

    quality = sum(x.quality for x in usable) / len(usable)
    modalities = sorted({x.modality for x in usable})
    sources = sorted({x.source for x in usable})
    sample_count = len(usable)

    variability = sum(x["variability"] for x in summaries) / len(summaries)
    anomaly = sum(x["anomaly"] for x in summaries) / len(summaries)
    baseline_shift = sum(x["baseline_shift"] for x in summaries) / len(summaries)
    trends = sum(x["trend"] for x in summaries) / len(summaries)

    stable_groups = [g for g in summaries if g["variability"] < 0.5]
    corroboration = _clip(
        0.35 * _clip(len(modalities) / 3.0)
        + 0.35 * _clip(len(sources) / 3.0)
        + 0.30 * _clip(len(stable_groups) / max(1, len(summaries)))
    )
    disagreement = _clip(0.55 * variability + 0.45 * anomaly)
    evidence_completeness = _clip(
        0.30 * _clip(sample_count / 10.0)
        + 0.25 * quality
        + 0.20 * _clip(len(modalities) / 3.0)
        + 0.15 * _clip(len(sources) / 3.0)
        + 0.10
    )
    confidence = _clip(
        0.20 + 0.35 * evidence_completeness + 0.20 * corroboration
        + 0.15 * (1.0 - disagreement) + 0.10 * (1.0 - anomaly)
    )

    if baseline_shift >= 0.66:
        state = "substantial_baseline_shift_pattern"
    elif trends >= 0.50:
        state = "persistent_change_pattern"
    elif anomaly >= 0.66:
        state = "high_variability_or_anomaly_pattern"
    elif variability >= 0.33:
        state = "moderate_variability_pattern"
    else:
        state = "stable_observed_pattern"

    counter_evidence = []
    if disagreement >= 0.35:
        counter_evidence.append("Observed measurements contain meaningful disagreement or variability.")
    if len(modalities) < 2:
        counter_evidence.append("Only one modality is present; cross-modal corroboration is unavailable.")
    if len(sources) < 2:
        counter_evidence.append("Only one source is present; independent replication is unavailable.")
    if sample_count < 10:
        counter_evidence.append("Sample count is below the stronger-evidence threshold used by this control plane.")
    if not counter_evidence:
        counter_evidence.append("No major counter-evidence condition was detected by the deterministic checks.")

    limitations = [
        "यह measurable signals की computational interpretation है, प्रत्यक्ष subjective feeling या consciousness का प्रमाण नहीं।",
        "Confidence को labelled validation data पर calibration के बिना scientific certainty नहीं माना जा सकता।",
        "Biological, plant, environmental और non-living interpretations के लिए domain-specific sensors, controls और independent replication आवश्यक हैं।",
    ]

    result = {
        "status": "interpreted",
        "schema_version": SCHEMA_VERSION,
        "request_language": _language(request),
        "state": state,
        "features": {
            "sample_count": sample_count,
            "modalities": len(modalities),
            "sources": len(sources),
            "quality": round(quality, 6),
            "corroboration": round(corroboration, 6),
            "disagreement": round(disagreement, 6),
            "evidence_completeness": round(evidence_completeness, 6),
            "baseline_shift": round(baseline_shift, 6),
            "trend_strength": round(trends, 6),
            "anomaly_strength": round(anomaly, 6),
            "confidence": round(confidence, 6),
        },
        "group_summaries": summaries,
        "evidence": [asdict(x) for x in usable],
        "counter_evidence": counter_evidence,
        "limitations": limitations,
    }
    result["fingerprint"] = _fingerprint(result)
    return result

def explain_simple(result: dict[str, Any], language: str = "hi") -> str:
    if result.get("status") != "interpreted":
        return "अभी पर्याप्त गुणवत्ता वाला measurable signal उपलब्ध नहीं है; विश्वसनीय व्याख्या रोक दी गई है।"
    f = result["features"]
    state = result["state"]
    if language == "en":
        return (
            f"Measured data shows a '{state}' pattern. "
            f"Confidence={f['confidence']:.0%}; corroboration={f['corroboration']:.0%}; "
            f"samples={f['sample_count']}; modalities={f['modalities']}. "
            "This is a computational interpretation of observations, not proof of subjective experience."
        )
    return (
        f"मापे गए संकेतों में '{state}' जैसा पैटर्न दिखाई देता है। "
        f"विश्वास-मान {f['confidence']:.0%}, corroboration {f['corroboration']:.0%}, "
        f"नमूने {f['sample_count']} और modalities {f['modalities']} हैं। "
        "यह measurable signals की computational व्याख्या है; इसे प्रत्यक्ष भाव या चेतना का प्रमाण नहीं माना जाता।"
    )

def build_record(observations: Iterable[dict[str, Any]], request: str = "") -> dict[str, Any]:
    result = analyze(observations, request)
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "observe->normalize->quality->group->robust-analysis->fusion->counter-evidence->NLP->audit",
        "result": result,
        "simple_language": explain_simple(result, result.get("request_language", "hi")),
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "scientific_certainty_claim_allowed": False,
            "independent_verification_required": True,
            "scheduled_code_mutation_allowed": False,
        },
        "fingerprint": _fingerprint(result),
    }
