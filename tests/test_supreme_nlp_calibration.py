"""Regression tests for Supreme NLP confidence calibration."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.supreme_nlp_calibration import (
    calibration_metrics,
    run_calibration_suite,
)


def test_calibration_suite_passes():
    result = run_calibration_suite()
    assert result["ok"] is True
    assert result["metrics"]["sample_count"] == 10
    assert result["metrics"]["accuracy"] >= 0.80


def test_calibration_metrics_are_deterministic():
    result = calibration_metrics([
        {"confidence": 0.9, "outcome": 1},
        {"confidence": 0.1, "outcome": 0},
    ])
    assert result["accuracy"] == 1.0
    assert result["brier_score"] == 0.01
    assert result["expected_calibration_error"] == 0.1


def test_invalid_confidence_is_rejected():
    try:
        calibration_metrics([{"confidence": 1.1, "outcome": 1}])
    except ValueError as exc:
        assert "between 0 and 1" in str(exc)
    else:
        raise AssertionError("out-of-range confidence must be rejected")


def test_non_binary_outcome_is_rejected():
    try:
        calibration_metrics([{"confidence": 0.5, "outcome": 2}])
    except ValueError as exc:
        assert "binary" in str(exc)
    else:
        raise AssertionError("non-binary outcome must be rejected")


if __name__ == "__main__":
    test_calibration_suite_passes()
    test_calibration_metrics_are_deterministic()
    test_invalid_confidence_is_rejected()
    test_non_binary_outcome_is_rejected()
    print("SUPREME_NLP_CALIBRATION_TESTS=PASS")
