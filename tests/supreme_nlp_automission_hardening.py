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
    record = json.loads(
        (ROOT / "generated/supreme-nlp-automission-health.json").read_text(encoding="utf-8")
    )
    required = {
        "event_id","timestamp","repository","contract_status","schema_status",
        "governance_status","graph_status","regression_status","verification_state",
        "blockers","warnings","provenance","cycle_duration_seconds","gate_results"
    }
    assert required.issubset(record), f"Missing telemetry keys: {sorted(required - set(record))}"
    assert record["contract_status"] == "PASS"
    assert record["schema_status"] == "PASS"
    assert record["governance_status"] == "PASS"
    assert record["graph_status"] == "PASS"
    assert record["regression_status"] == "PASS"
    assert record["verification_state"] == "UNVERIFIED"
    assert record["blockers"] == []
    assert record["gate_results"]["contract_qc"]["exit_code"] == 0
    assert record["gate_results"]["evaluation_qc"]["exit_code"] == 0
    print("SHIRMANI Supreme NLP Automission hardening tests: PASS")

if __name__ == "__main__":
    main()
