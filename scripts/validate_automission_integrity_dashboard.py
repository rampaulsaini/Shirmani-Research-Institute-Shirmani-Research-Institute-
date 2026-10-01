import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"docs/yatharth-governance/automission-integrity-dashboard.schema.json"

def main():
    x=json.loads(P.read_text(encoding="utf-8"))
    gates=x["required_gates"]
    assert len(gates)==len(set(gates))==8
    assert "UNKNOWN" in x["status_vocabulary"]
    assert "FAIL" in x["status_vocabulary"]
    assert x["performance_rules"]["parallelizable_gates_should_run_independently"] is True
    assert x["performance_rules"]["never_trade_evidence_integrity_for_latency"] is True
    assert x["performance_rules"]["fail_closed_on_unknown_gate"] is True
    assert x["accuracy_rules"]["unknown_is_not_pass"] is True
    assert x["accuracy_rules"]["workflow_success_is_not_independent_verification"] is True
    assert x["accuracy_rules"]["ai_output_can_verify"] is False
    assert set(["generated_at","commit_sha","gate_results","independent_verified_claims","live_claim","verification_boundary","fail_closed"]).issubset(x["required_status_fields"])
    print("Automission Unified Integrity Dashboard Contract Gate: PASS")

if __name__=="__main__":
    main()
