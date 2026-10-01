"""Dependency-free confidence calibration and benchmark utilities.

The calibration layer evaluates whether confidence values track observed
binary outcomes. It is a quality signal for the pipeline, not proof of model
truth or consciousness.
"""
from __future__ import annotations

from typing import Iterable, Dict, Any, List, Tuple

DEFAULT_BINS = 5
MAX_ECE = 0.25
MAX_BRIER = 0.25
MIN_ACCURACY = 0.80


def _validate_pair(confidence: Any, outcome: Any) -> Tuple[float, int]:
    confidence = float(confidence)
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be between 0 and 1")
    if outcome not in (0, 1, False, True):
        raise ValueError("outcome must be binary")
    return confidence, int(bool(outcome))


def calibration_metrics(records: Iterable[Dict[str, Any]], bins: int = DEFAULT_BINS) -> Dict[str, Any]:
    """Return accuracy, Brier score and expected calibration error (ECE)."""
    if bins < 2:
        raise ValueError("bins must be at least 2")
    pairs = [_validate_pair(r.get("confidence"), r.get("outcome")) for r in records]
    if not pairs:
        raise ValueError("at least one calibration record is required")

    accuracy = sum((p >= 0.5) == bool(y) for p, y in pairs) / len(pairs)
    brier = sum((p - y) ** 2 for p, y in pairs) / len(pairs)
    ece = 0.0
    bin_details: List[Dict[str, Any]] = []

    for index in range(bins):
        lower = index / bins
        upper = (index + 1) / bins
        members = [
            (p, y) for p, y in pairs
            if lower <= p < upper or (index == bins - 1 and p == upper)
        ]
        if not members:
            continue
        mean_confidence = sum(p for p, _ in members) / len(members)
        mean_outcome = sum(y for _, y in members) / len(members)
        gap = abs(mean_confidence - mean_outcome)
        weight = len(members) / len(pairs)
        ece += weight * gap
        bin_details.append({
            "lower": lower,
            "upper": upper,
            "count": len(members),
            "mean_confidence": mean_confidence,
            "empirical_accuracy": mean_outcome,
            "gap": gap,
        })

    return {
        "sample_count": len(pairs),
        "accuracy": accuracy,
        "brier_score": brier,
        "expected_calibration_error": ece,
        "bins": bin_details,
    }


def run_calibration_suite() -> Dict[str, Any]:
    """Run a deterministic fixture with explicit quality thresholds."""
    fixture = [
        {"confidence": 0.90, "outcome": 1},
        {"confidence": 0.80, "outcome": 1},
        {"confidence": 0.70, "outcome": 0},
        {"confidence": 0.20, "outcome": 0},
        {"confidence": 0.30, "outcome": 0},
        {"confidence": 0.60, "outcome": 1},
        {"confidence": 0.95, "outcome": 1},
        {"confidence": 0.10, "outcome": 0},
        {"confidence": 0.85, "outcome": 1},
        {"confidence": 0.40, "outcome": 0},
    ]
    metrics = calibration_metrics(fixture)
    guards = {
        "minimum_accuracy": metrics["accuracy"] >= MIN_ACCURACY,
        "maximum_brier_score": metrics["brier_score"] <= MAX_BRIER,
        "maximum_ece": metrics["expected_calibration_error"] <= MAX_ECE,
    }
    return {
        "ok": all(guards.values()),
        "metrics": metrics,
        "thresholds": {
            "minimum_accuracy": MIN_ACCURACY,
            "maximum_brier_score": MAX_BRIER,
            "maximum_ece": MAX_ECE,
        },
        "guards": guards,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_calibration_suite(), indent=2))
