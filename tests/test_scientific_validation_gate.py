import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from factory.scientific_validation_gate import evaluate


def base_protocol():
    return {
        "protocol_id": "test-v2", "status": "UNVERIFIED",
        "operational_definition": "registered task",
        "population_scope": "registered population", "sampling_plan": "registered sampling",
        "instrument_calibration": "registered calibration", "preprocessing_version": "v1",
        "model_version": "v1", "primary_endpoint": "accuracy",
        "evaluation_population": "locked", "blinded_holdout": True,
        "positive_controls": "yes", "negative_controls": "yes",
        "independent_replication": True, "counter_evidence_plan": True,
        "analysis_plan": "registered",
    }


def base_evidence():
    return {
        "observations": {"n": 100}, "measurement_quality": {"calibrated": True},
        "task_metrics": {"accuracy": 0.90},
        "calibration_metrics": {"evaluated": True, "ece": 0.04},
        "holdout_results": {"locked": True},
        "replication_results": {"independent": True},
        "counter_evidence_review": {"reviewed": True},
        "audit": {"passed": True},
    }


def test_fail_closed_without_explicit_verified_review():
    report = evaluate(base_protocol(), base_evidence())
    assert report["status"] == "UNVERIFIED"
    assert report["promotion_allowed"] is False


def test_verified_requires_explicit_registered_status():
    protocol = base_protocol()
    protocol["status"] = "VERIFIED"
    report = evaluate(protocol, base_evidence())
    assert report["status"] == "VERIFIED"
    assert report["promotion_allowed"] is True


def test_holdout_is_mandatory():
    evidence = base_evidence()
    evidence["holdout_results"] = {"locked": False}
    report = evaluate(base_protocol(), evidence)
    assert "LOCKED_HOLDOUT_REQUIRED" in report["errors"]
    assert report["promotion_allowed"] is False
