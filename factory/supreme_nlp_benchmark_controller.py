import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "supreme-nlp-benchmark-record.schema.json"
OUT = ROOT / "generated" / "supreme-nlp-benchmark-controller.json"

REQUIRED_KEYS = [
    "record_id","task","population_scope","dataset_fingerprint","model",
    "metric","direction","baseline","candidate","delta","uncertainty",
    "provenance","limitations","verification_state"
]

def validate_schema():
    data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = data.get("required", [])
    missing = [k for k in REQUIRED_KEYS if k not in required]
    if missing:
        raise RuntimeError("benchmark schema missing: " + ", ".join(missing))
    states = data["properties"]["verification_state"]["enum"]
    expected = ["REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED","PROPOSED_IMPROVEMENT"]
    if states != expected:
        raise RuntimeError("verification state contract changed unexpectedly")
    return data

def main():
    validate_schema()
    record = {
        "cycle_id": "benchmark-controller-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "READY_FOR_BENCHMARK_RECORDS",
        "promotion_policy": "fail-closed",
        "self_improvement": {
            "enabled": True,
            "mode": "proposal-only",
            "production_self_modification": False,
            "human_authorization_required": True
        },
        "required_evidence": REQUIRED_KEYS,
        "verification_rule": "VERIFIED requires independent verification evidence",
        "prohibited_shortcuts": [
            "workflow_success_as_accuracy",
            "confidence_as_truth",
            "missing_evidence_as_proof",
            "silent_governance_bypass"
        ]
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
