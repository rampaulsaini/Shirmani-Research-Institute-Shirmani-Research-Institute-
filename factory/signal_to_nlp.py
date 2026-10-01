"""Bounded multimodal signal-to-NLP interpretation layer.

This module translates observable, structured signals into plain-language
descriptions. It deliberately does not claim that a signal proves a subjective
experience. It reports measurements, detected patterns, hypotheses, and
confidence separately.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from math import isfinite
from typing import Any


@dataclass(frozen=True)
class SignalObservation:
    source: str
    feature: str
    value: float
    unit: str = ""
    baseline: float | None = None
    direction: str | None = None


def _finite(x: Any) -> bool:
    return isinstance(x, (int, float)) and isfinite(float(x))


def normalize_observation(item: dict[str, Any]) -> SignalObservation:
    if not isinstance(item, dict):
        raise TypeError("observation must be an object")
    source = str(item.get("source", "")).strip()
    feature = str(item.get("feature", "")).strip()
    if not source or not feature or not _finite(item.get("value")):
        raise ValueError("source, feature and finite numeric value are required")
    baseline = item.get("baseline")
    if baseline is not None and not _finite(baseline):
        raise ValueError("baseline must be numeric when supplied")
    direction = item.get("direction")
    if direction is not None:
        direction = str(direction).strip().lower()
        if direction not in {"rising", "falling", "stable", "variable"}:
            raise ValueError("unsupported direction")
    return SignalObservation(
        source=source,
        feature=feature,
        value=float(item["value"]),
        unit=str(item.get("unit", "")),
        baseline=float(baseline) if baseline is not None else None,
        direction=direction,
    )


def interpret_observations(items: list[dict[str, Any]]) -> dict[str, Any]:
    observations = [normalize_observation(x) for x in items]
    statements = []
    for o in observations:
        measurement = f"{o.value:g}{o.unit}"
        pattern = f" {o.direction}" if o.direction else ""
        baseline_text = ""
        if o.baseline is not None:
            delta = o.value - o.baseline
            baseline_text = f"; baseline difference {delta:+g}{o.unit}"
        statements.append(
            f"{o.source}: {o.feature} measured at {measurement}{pattern}{baseline_text}."
        )

    return {
        "schema_version": "1.0",
        "observations": [asdict(o) for o in observations],
        "plain_language": " ".join(statements) if statements else "No valid observations.",
        "interpretation_boundary": (
            "These statements describe observable signals. They do not by themselves "
            "establish consciousness, emotion, subjective experience, or intention."
        ),
        "hypothesis": (
            "A downstream ML model may classify the observed pattern against a "
            "validated reference dataset; classification remains a hypothesis until "
            "independently supported."
        ),
        "confidence": 0.0 if not observations else 1.0,
    }
