"""Evidence-bounded multimodal signal -> plain-language NLP adapter.

This module translates measurable signals into human-readable observations.
It never labels a signal as subjective feeling or consciousness without evidence.
"""
from __future__ import annotations

from math import isfinite
from statistics import mean, pstdev
from typing import Any

SCHEMA_VERSION = "1.0"


def _finite(value: Any) -> float | None:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return None
    return x if isfinite(x) else None


def summarize_signal(
    name: str,
    values: list[float],
    *,
    unit: str = "",
    baseline: float | None = None,
    context: str = "",
) -> dict[str, Any]:
    """Return deterministic signal statistics and an uncertainty-bounded interpretation."""
    clean = [x for x in (_finite(v) for v in values) if x is not None]
    if not clean:
        return {
            "schema_version": SCHEMA_VERSION,
            "status": "NO_VALID_SIGNAL",
            "signal": name,
            "observation": "No valid numeric signal was available.",
            "interpretation": "No inference is made.",
            "confidence": 0.0,
            "uncertainty": 1.0,
            "evidence_boundary": "measured signal != subjective feeling",
        }

    avg = mean(clean)
    spread = pstdev(clean) if len(clean) > 1 else 0.0
    reference = _finite(baseline)
    delta = None if reference is None else avg - reference
    z = 0.0 if spread == 0.0 or reference is None else (avg - reference) / spread

    direction = "stable"
    if len(clean) >= 2:
        if clean[-1] > clean[0]:
            direction = "increasing"
        elif clean[-1] < clean[0]:
            direction = "decreasing"

    sample_factor = min(1.0, len(clean) / 20.0)
    stability_factor = 1.0 / (1.0 + spread / (abs(avg) + 1e-9))
    confidence = round(max(0.0, min(1.0, 0.5 * sample_factor + 0.5 * stability_factor)), 6)

    observation = (
        f"{name}: mean={avg:.6g}{unit}, direction={direction}, "
        f"spread={spread:.6g}{unit}"
    )
    if reference is not None:
        observation += f", baseline_delta={delta:.6g}{unit}, z={z:.6g}"

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "OBSERVATION_READY",
        "signal": name,
        "context": context,
        "samples": len(clean),
        "mean": avg,
        "spread": spread,
        "baseline": reference,
        "delta": delta,
        "z_score": z,
        "direction": direction,
        "observation": observation,
        "interpretation": (
            "A measurable signal pattern was detected. "
            "Its biological/physical meaning requires validated context and evidence."
        ),
        "plain_language": (
            f"मैंने {name} में {direction} पैटर्न देखा है। "
            "यह मापे गए संकेत का वर्णन है; इसे अपने-आप भावना, चेतना या अनुभव का प्रमाण नहीं माना जाता।"
        ),
        "confidence": confidence,
        "uncertainty": round(1.0 - confidence, 6),
        "evidence_boundary": "measured signal != model inference != subjective feeling",
    }
