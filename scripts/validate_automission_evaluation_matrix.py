import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"docs/yatharth-governance/automission-evaluation-matrix.json"
def main():
    c=json.loads(P.read_text(encoding="utf-8"))
    required={"accuracy","precision","recall","f1","calibration","selective_risk","robustness","latency_p50","latency_p95","latency_p99","error_rate","abstention_rate","provenance_completeness","reproducibility"}
    assert required <= set(c["dimensions"])
    suites=set(c["test_suites"])
    assert {"golden_set","counter_evidence","edge_cases","regression","unseen","adversarial"} <= suites
    rules=set(c["comparison_rules"])
    assert "a_missing_metric_is_not_a_pass" in rules
    assert "a_regression_in_a_critical_metric_blocks_release" in rules
    assert c["speed_rules"]["parallelize_independent_test_suites"] is True
    assert c["speed_rules"]["never_skip_critical_tests_for_latency"] is True
    b=c["release_boundary"]
    assert b["benchmark_pass_is_not_truth_verification"] is True
    assert b["benchmark_pass_is_not_real_world_guarantee"] is True
    assert b["workflow_success_is_not_independent_verification"] is True
    assert b["independent_verified_claims"] == 0 and b["live_claim"] is False
    print("Automission Deterministic Evaluation Matrix Gate: PASS")
if __name__=="__main__": main()
