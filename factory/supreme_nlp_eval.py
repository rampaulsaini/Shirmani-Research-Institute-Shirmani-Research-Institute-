"""Deterministic, dependency-free quality evaluation for Supreme NLP outputs.

This module measures empirical model behavior; it never treats confidence as
proof of subjective experience and never promotes an interpretation to verified.
"""

from __future__ import annotations

from typing import Sequence


def _validate_labels(values: Sequence[str], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if any(not isinstance(v, str) or not v for v in values):
        raise ValueError(f"{name} must contain non-empty strings")


def _validate_parallel(*values: Sequence[object]) -> None:
    if len({len(v) for v in values}) != 1:
        raise ValueError("all evaluation sequences must have equal length")


def _validate_confidences(confidences: Sequence[float]) -> None:
    if any(isinstance(c, bool) or not 0.0 <= float(c) <= 1.0 for c in confidences):
        raise ValueError("confidences must be finite values in [0, 1]")


def classification_metrics(
    y_true: Sequence[str],
    y_pred: Sequence[str],
    confidences: Sequence[float] | None = None,
    abstained: Sequence[bool] | None = None,
) -> dict[str, float]:
    """Return deterministic accuracy, macro precision/recall/F1 and abstention."""
    _validate_labels(y_true, "y_true")
    _validate_labels(y_pred, "y_pred")
    _validate_parallel(y_true, y_pred)
    n = len(y_true)

    if confidences is not None:
        _validate_parallel(y_true, confidences)
        _validate_confidences(confidences)
    if abstained is not None:
        _validate_parallel(y_true, abstained)
        if any(not isinstance(a, bool) for a in abstained):
            raise ValueError("abstained must contain booleans")

    labels = sorted(set(y_true) | set(y_pred))
    precision, recall, f1 = [], [], []
    for label in labels:
        tp = sum(t == label and p == label for t, p in zip(y_true, y_pred))
        fp = sum(t != label and p == label for t, p in zip(y_true, y_pred))
        fn = sum(t == label and p != label for t, p in zip(y_true, y_pred))
        p = tp / (tp + fp) if tp + fp else 0.0
        r = tp / (tp + fn) if tp + fn else 0.0
        f = 2 * p * r / (p + r) if p + r else 0.0
        precision.append(p)
        recall.append(r)
        f1.append(f)

    result = {
        "sample_count": float(n),
        "accuracy": sum(t == p for t, p in zip(y_true, y_pred)) / n,
        "macro_precision": sum(precision) / len(precision),
        "macro_recall": sum(recall) / len(recall),
        "macro_f1": sum(f1) / len(f1),
        "abstention_rate": sum(abstained) / n if abstained is not None else 0.0,
    }
    if confidences is not None:
        result["mean_confidence"] = sum(map(float, confidences)) / n
        result["expected_calibration_error"] = expected_calibration_error(
            y_true, y_pred, confidences
        )
    return result


def expected_calibration_error(
    y_true: Sequence[str],
    y_pred: Sequence[str],
    confidences: Sequence[float],
    bins: int = 10,
) -> float:
    """Compute ECE using confidence in the emitted label."""
    _validate_labels(y_true, "y_true")
    _validate_labels(y_pred, "y_pred")
    _validate_parallel(y_true, y_pred, confidences)
    if bins < 1:
        raise ValueError("bins must be positive")
    _validate_confidences(confidences)

    buckets: list[list[int]] = [[] for _ in range(bins)]
    for i, confidence in enumerate(confidences):
        index = min(bins - 1, int(float(confidence) * bins))
        buckets[index].append(i)

    total = len(y_true)
    error = 0.0
    for bucket in buckets:
        if not bucket:
            continue
        accuracy = sum(y_true[i] == y_pred[i] for i in bucket) / len(bucket)
        mean_conf = sum(float(confidences[i]) for i in bucket) / len(bucket)
        error += len(bucket) / total * abs(accuracy - mean_conf)
    return error


def robustness_consistency(
    baseline_predictions: Sequence[str],
    perturbed_predictions: Sequence[str],
) -> float:
    """Measure prediction consistency under a controlled perturbation."""
    _validate_labels(baseline_predictions, "baseline_predictions")
    _validate_labels(perturbed_predictions, "perturbed_predictions")
    _validate_parallel(baseline_predictions, perturbed_predictions)
    return sum(a == b for a, b in zip(baseline_predictions, perturbed_predictions)) / len(
        baseline_predictions
    )


def quality_gate(
    metrics: dict[str, float],
    *,
    min_accuracy: float = 0.75,
    min_macro_f1: float = 0.70,
    max_ece: float = 0.15,
    min_robustness: float = 0.80,
) -> dict[str, object]:
    """Fail closed when empirical quality thresholds are not met."""
    required = ("accuracy", "macro_f1", "expected_calibration_error", "robustness")
    missing = [key for key in required if key not in metrics]
    if missing:
        return {"status": "FAIL", "reason": "missing_metrics", "missing": missing}

    checks = {
        "accuracy": metrics["accuracy"] >= min_accuracy,
        "macro_f1": metrics["macro_f1"] >= min_macro_f1,
        "expected_calibration_error": metrics["expected_calibration_error"] <= max_ece,
        "robustness": metrics["robustness"] >= min_robustness,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "thresholds": {
            "min_accuracy": min_accuracy,
            "min_macro_f1": min_macro_f1,
            "max_ece": max_ece,
            "min_robustness": min_robustness,
        },
    }
