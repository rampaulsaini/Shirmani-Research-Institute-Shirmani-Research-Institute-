"""Deterministic confidence-drift guard for the Supreme NLP gate.

Compares a trusted baseline calibration profile with a current profile and
blocks silent degradation. Metrics are descriptive quality signals, not proof
that a model is truthful or that a biological/physical signal represents
subjective experience.
"""
from __future__ import annotations

from typing import Any, Dict


DEFAULT_MAX_ACCURACY_DROP = 0.10
DEFAULT_MAX_BRIER_INCREASE = 0.10
DEFAULT_MAX_ECE_INCREASE = 0.10


def _metric(profile: Dict[str, Any], name: str) -> float:
    metrics = profile.get("metrics")
    if not isinstance(metrics, dict) or name not in metrics:
        raise ValueError(f"profile.metrics.{name} is required")
    value = float(metrics[name])
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"profile.metrics.{name} must be between 0 and 1")
    return value


def compare_calibration(
    baseline: Dict[str, Any],
    current: Dict[str, Any],
    *,
    max_accuracy_drop: float = DEFAULT_MAX_ACCURACY_DROP,
    max_brier_increase: float = DEFAULT_MAX_BRIER_INCREASE,
    max_ece_increase: float = DEFAULT_MAX_ECE_INCREASE,
) -> Dict[str, Any]:
    """Return a deterministic pass/fail decision and metric deltas."""
    limits = {
        "accuracy_drop": float(max_accuracy_drop),
        "brier_increase": float(max_brier_increase),
        "ece_increase": float(max_ece_increase),
    }
    if any(value < 0.0 or value > 1.0 for value in limits.values()):
        raise ValueError("drift thresholds must be between 0 and 1")

    base_accuracy = _metric(baseline, "accuracy")
    current_accuracy = _metric(current, "accuracy")
    base_brier = _metric(baseline, "brier_score")
    current_brier = _metric(current, "brier_score")
    base_ece = _metric(baseline, "expected_calibration_error")
    current_ece = _metric(current, "expected_calibration_error")

    accuracy_drop = max(0.0, base_accuracy - current_accuracy)
    brier_increase = max(0.0, current_brier - base_brier)
    ece_increase = max(0.0, current_ece - base_ece)

    guards = {
        "accuracy": accuracy_drop <= limits["accuracy_drop"],
        "brier_score": brier_increase <= limits["brier_increase"],
        "expected_calibration_error": ece_increase <= limits["ece_increase"],
    }

    return {
        "ok": all(guards.values()),
        "baseline": {
            "accuracy": base_accuracy,
            "brier_score": base_brier,
            "expected_calibration_error": base_ece,
        },
        "current": {
            "accuracy": current_accuracy,
            "brier_score": current_brier,
            "expected_calibration_error": current_ece,
        },
        "deltas": {
            "accuracy_drop": accuracy_drop,
            "brier_increase": brier_increase,
            "ece_increase": ece_increase,
        },
        "thresholds": limits,
        "guards": guards,
    }
