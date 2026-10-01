"""Explainable multimodal signal -> NLP layer for SHIRMANI Automission.

This module translates measured signals into conservative natural-language
descriptions. It does not claim that a sensor signal proves subjective
experience, consciousness, emotion, or intent. Every interpretation carries
evidence, uncertainty, and a confidence band.

The design is dependency-free and deterministic so it can run inside the
existing fail-closed quality loop before heavier ML models are introduced.
"""
from __future__ import annotations

import math
import statistics
from typing import Any

SCHEMA_VERSION = "1.0"


def _finite(values: list[float]) -> list[float]:
    return [float(v) for v in values if math.isfinite(float(v))]


def summarize_signal(
    values: list[float],
    *,
    sample_rate_hz: float | None = None,
    baseline: list[float] | None = None,
    channel: str = "unknown",
) -> dict[str, Any]:
    """Produce deterministic signal features and an uncertainty-aware summary."""
    xs = _finite(values)
    if not xs:
        return {
            "schema_version": SCHEMA_VERSION,
            "channel": channel,
            "status": "INSUFFICIENT_DATA",
            "sample_count": 0,
            "features": {},
        }

    mean = statistics.fmean(xs)
    minimum, maximum = min(xs), max(xs)
    stdev = statistics.pstdev(xs) if len(xs) > 1 else 0.0
    rms = math.sqrt(statistics.fmean([x * x for x in xs]))

    baseline_mean = None
    delta = None
    if baseline:
        bs = _finite(baseline)
        if bs:
            baseline_mean = statistics.fmean(bs)
            delta = mean - baseline_mean

    duration = None
    if sample_rate_hz and sample_rate_hz > 0:
        duration = len(xs) / sample_rate_hz

    return {
        "schema_version": SCHEMA_VERSION,
        "channel": channel,
        "status": "OK",
        "sample_count": len(xs),
        "features": {
            "mean": round(mean, 9),
            "min": round(minimum, 9),
            "max": round(maximum, 9),
            "stddev": round(stdev, 9),
            "rms": round(rms, 9),
            "range": round(maximum - minimum, 9),
            "baseline_mean": None if baseline_mean is None else round(baseline_mean, 9),
            "delta_from_baseline": None if delta is None else round(delta, 9),
            "duration_seconds": None if duration is None else round(duration, 9),
        },
    }


def interpret_signal(summary: dict[str, Any], *, context: str = "") -> dict[str, Any]:
    """Translate measured features into cautious plain language.

    The output describes observable patterns first. It never converts a
    physical signal into a claim of subjective feeling.
    """
    if summary.get("status") != "OK":
        return {
            "schema_version": SCHEMA_VERSION,
            "interpretation_status": "INSUFFICIENT_DATA",
            "plain_language": "पर्याप्त संकेत उपलब्ध नहीं हैं; विश्वसनीय व्याख्या नहीं की जा सकती।",
            "confidence": 0.0,
            "claims": [],
            "evidence": [],
        }

    f = summary["features"]
    delta = f.get("delta_from_baseline")
    stdev = float(f.get("stddev", 0.0))
    signal_range = float(f.get("range", 0.0))
    n = int(summary.get("sample_count", 0))

    claims: list[str] = []
    evidence: list[str] = []

    if delta is not None:
        if abs(delta) > max(stdev * 2.0, 1e-12):
            direction = "ऊपर" if delta > 0 else "नीचे"
            claims.append(f"मापित औसत baseline की तुलना में {direction} बदला हुआ है।")
            evidence.append("baseline_delta")
        else:
            claims.append("मापित औसत baseline के आसपास है।")
            evidence.append("baseline_delta")

    if stdev > 0:
        claims.append("संकेत में मापनीय परिवर्तनशीलता मौजूद है।")
        evidence.append("standard_deviation")
    else:
        claims.append("संकेत इस नमूने में लगभग स्थिर है।")
        evidence.append("standard_deviation")

    if signal_range > 0:
        claims.append("संकेत में न्यूनतम और अधिकतम मान के बीच स्पष्ट अंतर है।")
        evidence.append("range")

    if context.strip():
        claims.append(f"दिया गया संदर्भ: {context.strip()}")

    # Confidence is a data-quality indicator, not probability of a feeling.
    completeness = min(1.0, n / 100.0)
    feature_coverage = len(evidence) / 3.0
    confidence = round(0.25 + 0.5 * completeness + 0.25 * feature_coverage, 6)

    plain = " ".join(claims)
    limitation = (
        "यह मापित संकेतों का वर्णन है; इससे अपने-आप चेतना, भावना, इच्छा "
        "या subjective experience सिद्ध नहीं होता।"
    )

    return {
        "schema_version": SCHEMA_VERSION,
        "interpretation_status": "OBSERVABLE_SIGNAL_DESCRIPTION",
        "plain_language": f"{plain} {limitation}",
        "confidence": confidence,
        "confidence_meaning": "data/feature completeness only; not a probability of subjective experience",
        "claims": claims,
        "evidence": evidence,
    }


def translate_signal(
    values: list[float],
    *,
    sample_rate_hz: float | None = None,
    baseline: list[float] | None = None,
    channel: str = "unknown",
    context: str = "",
) -> dict[str, Any]:
    """End-to-end deterministic signal -> features -> plain-language NLP."""
    summary = summarize_signal(
        values,
        sample_rate_hz=sample_rate_hz,
        baseline=baseline,
        channel=channel,
    )
    interpretation = interpret_signal(summary, context=context)
    return {
        "schema_version": SCHEMA_VERSION,
        "pipeline": "observe->clean->summarize->interpret->explain",
        "summary": summary,
        "interpretation": interpretation,
    }
