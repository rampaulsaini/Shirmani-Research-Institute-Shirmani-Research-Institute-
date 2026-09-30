import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs/yatharth-governance/automission-performance-contract.json"

def main():
    c = json.loads(P.read_text(encoding="utf-8"))
    hard = set(c["hard_quality_rules"])
    required = {
        "no_claim_is_verified_without_qualifying_independent_human_review",
        "no_model_may_suppress_counter_evidence_to_improve_a_score",
        "no_latency_target_may_override_safety_or_evidence_requirements",
        "no_aggregate_accuracy_metric_may_hide_class_specific_failure",
        "unknown_must_remain_unknown_until_supported_by_evidence",
        "high_impact_decisions_require_human_review",
        "fail_closed_on_integrity_or_provenance_failure",
    }
    assert required <= hard
    dims = c["evaluation_dimensions"]
    for key in ("factual_accuracy","precision_recall","calibration","robustness","provenance","reproducibility","latency","recovery"):
        assert key in dims
    boundary = c["release_boundary"]
    assert boundary["performance_pass_is_not_truth_verification"] is True
    assert boundary["benchmark_pass_is_not_real_world_guarantee"] is True
    assert boundary["workflow_success_is_not_independent_verification"] is True
    assert boundary["independent_verified_claims"] == 0
    assert boundary["live_claim"] is False
    print("Automission Performance Contract Gate: PASS")

if __name__ == "__main__":
    main()
