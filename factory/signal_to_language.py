"""Evidence-first multimodal signal → plain-language interpretation.

Separates measured signals from model interpretation. It does not claim direct
access to subjective feelings or consciousness.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from math import isfinite
from statistics import mean, pstdev
from typing import Iterable

@dataclass(frozen=True)
class SignalObservation:
    name: str
    value: float
    baseline: float
    unit: str = ""
    direction: str = "higher_is_more"

    def delta(self) -> float:
        if not isfinite(self.value) or not isfinite(self.baseline):
            raise ValueError("signal values must be finite")
        return self.value - self.baseline

def normalize_observations(observations: Iterable[SignalObservation]) -> list[SignalObservation]:
    result = list(observations)
    if not result:
        raise ValueError("at least one observation is required")
    for item in result:
        if not item.name.strip():
            raise ValueError("signal name cannot be empty")
        if item.direction not in {"higher_is_more", "lower_is_more", "two_sided"}:
            raise ValueError("unsupported signal direction")
    return result

def signal_features(observations: Iterable[SignalObservation]) -> dict:
    obs = normalize_observations(observations)
    deltas = [x.delta() for x in obs]
    magnitudes = [abs(x) for x in deltas]
    return {
        "count": len(obs),
        "mean_delta": round(mean(deltas), 6),
        "mean_absolute_delta": round(mean(magnitudes), 6),
        "dispersion": round(pstdev(deltas), 6) if len(deltas) > 1 else 0.0,
        "signals": [asdict(x) | {"delta": round(x.delta(), 6)} for x in obs],
    }

def plain_language_interpretation(observations: Iterable[SignalObservation], *, context: str = "unknown", model_confidence: float = 0.0) -> dict:
    if not 0.0 <= model_confidence <= 1.0:
        raise ValueError("model_confidence must be between 0 and 1")
    features = signal_features(observations)
    n = features["count"]
    if features["mean_absolute_delta"] == 0:
        pattern = "signals are close to the supplied baseline"
    elif features["mean_delta"] > 0:
        pattern = "the measured signals are, on average, above the supplied baseline"
    else:
        pattern = "the measured signals are, on average, below the supplied baseline"
    return {
        "context": context,
        "observation_summary": f"{n} measurable signal(s) were analyzed; {pattern}.",
        "simple_language": (
            f"Observed pattern: {pattern}. "
            "This describes measured data, not a direct reading of subjective feeling."
        ),
        "confidence": round(model_confidence, 6),
        "epistemic_status": "measurement_plus_model_interpretation",
        "uncertainty": (
            "Subjective experience, consciousness, or emotion is not established "
            "unless independently validated by an appropriate study."
        ),
        "features": features,
    }
