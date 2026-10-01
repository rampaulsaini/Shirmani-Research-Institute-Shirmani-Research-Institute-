"""Regression tests for the dependency-free Supreme NLP gate."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.supreme_nlp import run_self_test, validate_record


def test_self_test():
    result = run_self_test()
    assert result["ok"] is True
    assert result["record"]["status"] == "verified"
    assert result["quality_score"] == 1.0
    assert all(result["guards"].values())


def test_missing_field_rejected():
    record = {
        "event_id": "x",
        "source_type": "synthetic",
        "observations": [{"x": 1}],
        "interpretation": {"plain_language": "x", "claim_type": "observation"},
        "confidence": 0.5,
        "evidence": [{"id": "e"}],
        "verification": {"independent_check": True},
    }
    try:
        validate_record(record)
    except ValueError as exc:
        assert "missing required fields" in str(exc)
    else:
        raise AssertionError("missing provenance must be rejected")


def test_scientific_claim_requires_independent_verification():
    record = {
        "event_id": "scientific-1",
        "source_type": "synthetic",
        "observations": [{"signal": 1}],
        "interpretation": {"plain_language": "candidate finding", "claim_type": "scientific_claim"},
        "confidence": 0.8,
        "evidence": [{"id": "e1"}, {"id": "e2"}],
        "verification": {"independent_check": False},
        "provenance": {"source": "test"},
    }
    try:
        validate_record(record)
    except ValueError as exc:
        assert "independent verification" in str(exc)
    else:
        raise AssertionError("unverified scientific claim must be rejected")


def test_observations_and_evidence_must_be_objects():
    record = {
        "event_id": "shape-1",
        "source_type": "synthetic",
        "observations": ["bad"],
        "interpretation": {"plain_language": "x", "claim_type": "observation"},
        "confidence": 0.5,
        "evidence": [{"id": "e"}],
        "verification": {"independent_check": True},
        "provenance": {"source": "test"},
    }
    try:
        validate_record(record)
    except ValueError as exc:
        assert "observation" in str(exc)
    else:
        raise AssertionError("invalid observation shape must be rejected")


if __name__ == "__main__":
    test_self_test()
    test_missing_field_rejected()
    test_scientific_claim_requires_independent_verification()
    test_observations_and_evidence_must_be_objects()
    print("SUPREME_NLP_REGRESSION_TESTS=PASS")
