import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(path):
    result = subprocess.run(
        [sys.executable, str(ROOT / path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, f"{path} failed:\n{result.stdout}\n{result.stderr}"

def main():
    run("factory/supreme_nlp_contract_qc.py")
    run("factory/supreme_nlp_evaluation_qc.py")
    run("factory/supreme_nlp_automission_health.py")
    run("tests/supreme_runtime_contract.py")
    schema = json.loads((ROOT / "schemas/supreme-nlp-automission-health.schema.json").read_text(encoding="utf-8"))
    record = json.loads(
        (ROOT / "generated/supreme-nlp-automission-health.json").read_text(encoding="utf-8")
    )
    required = {
        "event_id","timestamp","repository","contract_status","schema_status",
        "governance_status","graph_status","regression_status","verification_state",
        "blockers","warnings","provenance","cycle_duration_seconds","gate_results"
    }
    assert set(record) == set(schema["required"]) == required, "Telemetry keys differ from the health schema contract."
    assert schema["additionalProperties"] is False
    for field in [
        "contract_status", "schema_status", "governance_status",
        "graph_status", "regression_status", "verification_state"
    ]:
        assert record[field] in schema["properties"][field]["enum"], f"Invalid {field}"
    assert record["contract_status"] == "PASS"
    assert record["schema_status"] == "PASS"
    assert record["governance_status"] == "PASS"
    assert record["graph_status"] == "PASS"
    assert record["regression_status"] == "PASS"
    assert record["verification_state"] == "UNVERIFIED"
    assert record["blockers"] == []
    assert record["gate_results"]["contract_qc"]["exit_code"] == 0
    assert record["gate_results"]["evaluation_qc"]["exit_code"] == 0
    # Successful automation is deliberately not independent scientific verification.
    assert record["verification_state"] == "UNVERIFIED"
    print("SHIRMANI Supreme NLP Automission hardening tests: PASS")

if __name__ == "__main__":
    main()
