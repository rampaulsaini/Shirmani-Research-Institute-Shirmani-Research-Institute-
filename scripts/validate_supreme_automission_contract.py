import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs/yatharth-governance/supreme-automission-contract.json"

def main():
    c = json.loads(P.read_text(encoding="utf-8"))
    b = c["truth_boundary"]
    assert b["architecture_is_not_deployment"]
    assert b["benchmark_is_not_truth_verification"]
    assert b["workflow_success_is_not_independent_verification"]
    assert b["independent_verified_claims"] == 0
    assert b["live_claim"] is False
    assert len(c["pipeline"]) >= 12
    for k in ("parallelize_independent_gates","cancel_stale_runs","bounded_retries","cache_immutable_dependencies","never_trade_evidence_for_latency"):
        assert c["performance"][k] is True
    accuracy = c["accuracy"]
    required_accuracy_flags = [
        "track_accuracy",
        "track_macro_precision_recall_f1",
        "track_brier_score",
        "track_calibration_error",
        "track_selective_risk",
        "track_p50_p95_p99_latency",
        "track_error_rate",
        "track_provenance_completeness",
        "track_reproducibility",
        "abstain_on_unknown_or_insufficient_evidence",
        "multi_agent_consensus_required",
        "evidence_completeness_required",
    ]
    for k in required_accuracy_flags:
        assert accuracy[k] is True, f"accuracy requirement disabled: {k}"
    assert accuracy["minimum_independent_agents"] >= 3
    assert accuracy["unresolved_disagreement_output"] == "UNKNOWN"
    assert accuracy["drift_detection"] is True
    budgets = c["performance"]["quality_budgets"]
    assert budgets["max_p95_latency_ms"] > 0
    assert budgets["max_p99_latency_ms"] >= budgets["max_p95_latency_ms"]
    assert 0 <= budgets["max_error_rate"] <= 1
    assert 0 <= budgets["max_expected_calibration_error"] <= 1
    assert 0 <= budgets["max_selective_risk"] <= 1
    assert 0 <= budgets["min_coverage"] <= 1
    assert budgets["min_provenance_completeness"] == 1.0
    for k,v in c["safety"].items():
        assert v is True
    print("Supreme Automission Contract: PASS")

if __name__ == "__main__":
    main()
