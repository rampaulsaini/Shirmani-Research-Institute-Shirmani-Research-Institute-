"""Regression tests for the dependency-free Supreme NLP gate."""
from factory.supreme_nlp import run_self_test, validate_record

def test_self_test():
    result = run_self_test()
    assert result["ok"] is True
    assert result["record"]["status"] == "verified"
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

if __name__ == "__main__":
    test_self_test()
    test_missing_field_rejected()
    print("SUPREME_NLP_REGRESSION_TESTS=PASS")
