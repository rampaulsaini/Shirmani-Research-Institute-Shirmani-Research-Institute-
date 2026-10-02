import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "docs" / "supreme-nlp-practitioner-contract.md",
    ROOT / "docs" / "supreme-nlp-evaluation-gate.md",
    ROOT / "schemas" / "supreme-nlp-evaluation.schema.json",
    ROOT / "schemas" / "agent-governance.json",
    ROOT / "factory" / "supreme_nlp_contract_qc.py",
    ROOT / "factory" / "supreme_nlp_evaluation_qc.py",
]

def main():
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    if missing:
        raise SystemExit("BLOCKED: missing required artifacts: " + ", ".join(missing))

    governance = json.loads((ROOT / "schemas" / "agent-governance.json").read_text(encoding="utf-8"))
    evaluation = json.loads((ROOT / "schemas" / "supreme-nlp-evaluation.schema.json").read_text(encoding="utf-8"))

    checks = {
        "fail_closed": governance.get("fail_closed") is True,
        "provenance_required": governance.get("provenance_required_for_claims") is True,
        "fabrication_prohibited": governance.get("fabrication_prohibited") is True,
        "verification_states_fail_closed": evaluation.get("properties", {}).get("verification_state", {}).get("enum")
        == ["REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"],
        "baseline_numeric": evaluation.get("properties", {}).get("baseline", {}).get("type") == "number",
        "result_numeric": evaluation.get("properties", {}).get("result", {}).get("type") == "number",
    }

    status = "PASS" if all(checks.values()) else "BLOCKED"
    telemetry = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "checks": checks,
        "accuracy_claim_policy": "measured_benchmark_only",
        "biological_signal_policy": "signal_inference_is_not_proof_of_subjective_feeling",
    }

    out = ROOT / "generated" / "supreme-nlp-operational-health.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(telemetry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if status != "PASS":
        raise SystemExit("Operational health gate BLOCKED")
    print("SHIRMANI Supreme NLP Operational Health: PASS")

if __name__ == "__main__":
    main()
