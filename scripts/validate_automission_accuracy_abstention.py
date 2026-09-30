import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs/yatharth-governance/automission-accuracy-abstention-contract.json"

def main():
    c = json.loads(P.read_text(encoding="utf-8"))
    pipeline = c["decision_pipeline"]
    for step in ("input_validation","model_execution","independent_cross_check",
                 "disagreement_analysis","confidence_calibration",
                 "abstain_when_threshold_not_met","traceable_output"):
        assert step in pipeline
    rules = c["quality_rules"]
    assert all(rules.values())
    for metric in ("accuracy","precision","recall","f1","calibration_error",
                   "abstention_rate","selective_risk","disagreement_rate",
                   "p50_latency","p95_latency","p99_latency"):
        assert metric in c["metrics"]
    boundary = c["release_boundary"]
    assert boundary["accuracy_is_not_truth"] is True
    assert boundary["confidence_is_not_certainty"] is True
    assert boundary["ensemble_agreement_is_not_independent_verification"] is True
    assert boundary["benchmark_success_is_not_real_world_guarantee"] is True
    assert boundary["independent_verified_claims"] == 0
    assert boundary["live_claim"] is False
    print("Automission Accuracy & Abstention Gate: PASS")

if __name__ == "__main__":
    main()
