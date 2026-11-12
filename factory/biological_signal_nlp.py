"""Evidence-grounded biological-signal -> NLP interpretation layer.

This module translates measurable signals from living systems into simple
language while explicitly separating observation from interpretation.

It does NOT claim to detect subjective feelings or consciousness. For plants,
animals and other living systems it can describe measured responses/states
(e.g. stress-associated, hydration-associated, circadian, growth-related)
when supported by supplied evidence. For nonliving systems it reports
physical states/responses only.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Mapping, Sequence
import math


@dataclass(frozen=True)
class SignalObservation:
    subject_type: str
    signal: str
    value: float
    unit: str
    baseline: float | None = None
    direction: str | None = None
    source: str | None = None
    evidence_refs: tuple[str, ...] = ()
    timestamp: str | None = None


@dataclass(frozen=True)
class Interpretation:
    observation: str
    state: str
    simple_language: str
    confidence: float
    evidence_required: bool
    subjective_feeling_claim: bool = False

    def normalized(self) -> dict[str, Any]:
        return asdict(self)


def _finite(value: float) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def _delta_ratio(value: float, baseline: float | None) -> float | None:
    if baseline is None or baseline == 0:
        return None
    return (value - baseline) / abs(baseline)


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def interpret_signal(obs: SignalObservation) -> Interpretation:
    """Convert one measured observation into conservative plain language."""
    if not _finite(obs.value):
        return Interpretation(
            "Signal value is invalid.",
            "UNKNOWN",
            "The measurement cannot be interpreted because its value is invalid.",
            0.0,
            True,
        )

    subject = obs.subject_type.strip().lower()
    signal = obs.signal.strip().lower()
    delta = _delta_ratio(obs.value, obs.baseline)

    # Nonliving objects: describe measurable physical response only.
    if subject in {"nonliving", "object", "material", "machine", "device"}:
        if delta is not None and abs(delta) >= 0.20:
            direction = "increased" if delta > 0 else "decreased"
            msg = f"The measured {signal} has {direction} substantially from its baseline."
            return Interpretation(
                f"{signal} changed by {delta:+.1%} from baseline.",
                "PHYSICAL_CHANGE",
                msg,
                _clamp(min(0.99, 0.55 + abs(delta))),
                bool(obs.source or obs.evidence_refs),
            )
        return Interpretation(
            f"{signal} was measured at {obs.value:g} {obs.unit}.",
            "MEASURED_STATE",
            f"The measured {signal} is {obs.value:g} {obs.unit}.",
            0.60 if obs.source or obs.evidence_refs else 0.35,
            bool(obs.source or obs.evidence_refs),
        )

    # Living systems: map observations to response states, never to a claimed
    # private emotional experience.
    if subject in {"plant", "animal", "human", "living", "organism"}:
        if signal in {"leaf_angle", "leaf_angle_change", "wilting"} and delta is not None and delta < -0.20:
            return Interpretation(
                f"{signal} changed {delta:+.1%} from baseline.",
                "STRESS_ASSOCIATED_RESPONSE",
                "The measured pattern is associated with a stress-like response; it does not prove a feeling.",
                _clamp(0.65 + min(0.30, abs(delta))),
                bool(obs.source or obs.evidence_refs),
            )
        if signal in {"growth_rate", "growth"} and delta is not None and delta > 0.20:
            return Interpretation(
                f"{signal} changed {delta:+.1%} from baseline.",
                "GROWTH_ASSOCIATED_RESPONSE",
                "The measured pattern is consistent with increased growth activity.",
                _clamp(0.65 + min(0.30, delta)),
                bool(obs.source or obs.evidence_refs),
            )
        if signal in {"water_potential", "moisture", "soil_moisture"} and delta is not None and delta < -0.20:
            return Interpretation(
                f"{signal} changed {delta:+.1%} from baseline.",
                "HYDRATION_STRESS_ASSOCIATED",
                "The measured pattern is associated with lower water availability.",
                _clamp(0.65 + min(0.30, abs(delta))),
                bool(obs.source or obs.evidence_refs),
            )
        if signal in {"electrical_potential", "bioelectric_signal", "vocalization", "movement", "heart_rate"}:
            return Interpretation(
                f"{signal} was measured at {obs.value:g} {obs.unit}.",
                "PHYSIOLOGICAL_OR_BEHAVIORAL_SIGNAL",
                "A measurable biological response was detected; its meaning requires context and supporting evidence.",
                0.55 if obs.source or obs.evidence_refs else 0.30,
                bool(obs.source or obs.evidence_refs),
            )

    return Interpretation(
        f"{signal} was measured at {obs.value:g} {obs.unit}.",
        "OBSERVED_SIGNAL",
        "A measurable signal was detected, but there is not enough context to assign a specific biological state.",
        0.35 if obs.source or obs.evidence_refs else 0.20,
        bool(obs.source or obs.evidence_refs),
    )


def interpret_batch(observations: Sequence[SignalObservation]) -> dict[str, Any]:
    results = [interpret_signal(x) for x in observations]
    return {
        "schema_version": "1.0",
        "records": len(results),
        "interpretations": [x.normalized() for x in results],
        "truth_claim": False,
        "subjective_feeling_claims": sum(x.subjective_feeling_claim for x in results),
        "publication_ready": all(
            x.confidence >= 0.95 and x.evidence_required is False
            for x in results
        ) if results else False,
        "next_step": (
            "add independent evidence and contextual measurements before making stronger claims"
            if results else "provide measured observations"
        ),
    }
