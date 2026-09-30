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
    for k,v in c["accuracy"].items():
        assert v is True
    for k,v in c["safety"].items():
        assert v is True
    print("Supreme Automission Contract: PASS")

if __name__ == "__main__":
    main()
