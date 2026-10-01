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

    required_performance = (
        "parallelize_independent_gates",
        "cancel_stale_runs",
        "bounded_retries",
        "cache_immutable_dependencies",
        "never_trade_evidence_for_latency",
    )
    for k in required_performance:
        assert c["performance"].get(k) is True, f"performance control disabled: {k}"

    boolean_accuracy_controls = (
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
    )
    for k in boolean_accuracy_controls:
        assert c["accuracy"].get(k) is True, f"accuracy control disabled: {k}"

    assert c["accuracy"]["minimum_independent_agents"] >= 3
    assert c["accuracy"]["unresolved_disagreement_output"] == "UNKNOWN"

    for k in (
        "fail_closed_on_unknown_gate",
        "high_impact_actions_require_human_review",
        "counter_evidence_must_be_preserved",
        "ai_output_cannot_be_independent_verification",
        "secrets_must_not_enter_logs_or_artifacts",
    ):
        assert c["safety"].get(k) is True, f"safety control disabled: {k}"

    print("Supreme Automission Contract: PASS")

if __name__ == "__main__":
    main()
