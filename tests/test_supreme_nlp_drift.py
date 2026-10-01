"""Regression tests for confidence-drift protection."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.supreme_nlp_drift import compare_calibration


BASELINE = {
    "metrics": {
        "accuracy": 0.90,
        "brier_score": 0.10,
        "expected_calibration_error": 0.08,
    }
}


def test_small_drift_passes():
    current = {
        "metrics": {
            "accuracy": 0.84,
            "brier_score": 0.14,
            "expected_calibration_error": 0.12,
        }
    }
    result = compare_calibration(BASELINE, current)
    assert result["ok"] is True
    assert all(result["guards"].values())


def test_large_accuracy_drop_fails():
    current = {
        "metrics": {
            "accuracy": 0.70,
            "brier_score": 0.10,
            "expected_calibration_error": 0.08,
        }
    }
    result = compare_calibration(BASELINE, current)
    assert result["ok"] is False
    assert result["guards"]["accuracy"] is False


def test_large_brier_increase_fails():
    current = {
        "metrics": {
            "accuracy": 0.90,
            "brier_score": 0.25,
            "expected_calibration_error": 0.08,
        }
    }
    result = compare_calibration(BASELINE, current)
    assert result["ok"] is False
    assert result["guards"]["brier_score"] is False


def test_large_ece_increase_fails():
    current = {
        "metrics": {
            "accuracy": 0.90,
            "brier_score": 0.10,
            "expected_calibration_error": 0.30,
        }
    }
    result = compare_calibration(BASELINE, current)
    assert result["ok"] is False
    assert result["guards"]["expected_calibration_error"] is False


if __name__ == "__main__":
    test_small_drift_passes()
    test_large_accuracy_drop_fails()
    test_large_brier_increase_fails()
    test_large_ece_increase_fails()
    print("SUPREME_NLP_DRIFT_TESTS=PASS")
