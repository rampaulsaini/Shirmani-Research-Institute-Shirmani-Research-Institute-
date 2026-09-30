import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs/yatharth-governance/automission-drift-recovery-contract.json"

def main():
    c = json.loads(P.read_text(encoding="utf-8"))
    required = {
        "input_distribution","label_distribution","feature_distribution",
        "embedding_distribution","model_output_distribution",
        "confidence_calibration","task_accuracy","latency",
        "error_rate","abstention_rate"
    }
    assert required <= set(c["drift_dimensions"])
    rules = set(c["monitoring_rules"])
    assert "detect_regression_before_release" in rules
    assert "retain_evidence_for_alerts" in rules
    response = c["response_policy"]
    assert response["critical"] == "fail_closed_and_block_release"
    assert response["rollback"].startswith("return_to_last_approved_artifact")
    boundary = c["safety_boundary"]
    assert boundary["drift_alert_is_not_proof_of_cause"] is True
    assert boundary["drift_pass_is_not_truth_verification"] is True
    assert boundary["workflow_success_is_not_independent_verification"] is True
    assert boundary["automatic_rollback_must_not_delete_audit_history"] is True
    assert boundary["independent_verified_claims"] == 0
    assert boundary["live_claim"] is False
    print("Automission Drift & Recovery Contract Gate: PASS")

if __name__ == "__main__":
    main()
