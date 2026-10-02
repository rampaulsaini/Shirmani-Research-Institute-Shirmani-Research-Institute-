import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-automission-health.json"
CONTRACT_QC = ROOT / "factory" / "supreme_nlp_contract_qc.py"
EVALUATION_QC = ROOT / "factory" / "supreme_nlp_evaluation_qc.py"

REQUIRED_FILES = [
    "docs/supreme-nlp-practitioner-contract.md",
    "docs/supreme-nlp-evaluation-gate.md",
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "schemas/supreme-nlp-evaluation.schema.json",
    "schemas/supreme-nlp-automission-health.schema.json",
    "schemas/agent-governance.json",
    "factory/supreme_nlp_contract_qc.py",
    "factory/supreme_nlp_evaluation_qc.py",
]

def run_gate(path):
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode, (result.stdout + result.stderr).strip()

def main():
    started = time.monotonic()
    blockers = []
    warnings = []

    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        blockers.append("Missing required files: " + ", ".join(missing))

    contract_text = (ROOT / "docs/supreme-nlp-practitioner-contract.md").read_text(
        encoding="utf-8"
    ) if (ROOT / "docs/supreme-nlp-practitioner-contract.md").exists() else ""
    graph_text = (ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md").read_text(
        encoding="utf-8"
    ) if (ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md").exists() else ""

    for term in [
        "Measured signal", "Model inference", "Interpretation",
        "Confidence", "Unresolved uncertainty", "Accuracy is measured",
        "Fail-closed rules", "Independent verification"
    ]:
        if term not in contract_text:
            blockers.append("Contract missing required term: " + term)

    for term in ["Multimodal Perception", "NLP", "Independent Verification", "Continuous Improvement"]:
        if term not in graph_text:
            blockers.append("Total graph missing stage: " + term)

    governance_status = "BLOCKED"
    gov = ROOT / "schemas/agent-governance.json"
    if gov.exists():
        try:
            data = json.loads(gov.read_text(encoding="utf-8"))
            required_flags = ["fail_closed", "provenance_required_for_claims", "fabrication_prohibited"]
            if all(data.get(k) is True for k in required_flags):
                governance_status = "PASS"
            else:
                blockers.append("Agent governance is not fully fail-closed.")
        except json.JSONDecodeError:
            blockers.append("Agent governance JSON is invalid.")

    schema_status = "BLOCKED"
    schema = ROOT / "schemas/supreme-nlp-evaluation.schema.json"
    if schema.exists():
        try:
            data = json.loads(schema.read_text(encoding="utf-8"))
            required = set(data.get("required", []))
            expected = {
                "record_id", "task", "dataset_fingerprint", "model", "metric",
                "baseline", "result", "confidence", "provenance", "verification_state"
            }
            states = data.get("properties", {}).get("verification_state", {}).get("enum", [])
            if expected.issubset(required) and states == [
                "REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"
            ]:
                schema_status = "PASS"
            else:
                blockers.append("Supreme NLP evaluation schema contract failed.")
        except json.JSONDecodeError:
            blockers.append("Supreme NLP evaluation schema is invalid.")

    gate_results = {}
    for name, path in [("contract_qc", CONTRACT_QC), ("evaluation_qc", EVALUATION_QC)]:
        if path.exists():
            code, output = run_gate(path)
            gate_results[name] = {"exit_code": code, "output": output[-2000:]}
            if code != 0:
                blockers.append(f"{name} failed with exit code {code}.")
        else:
            gate_results[name] = {"exit_code": None, "output": "missing"}
            blockers.append(f"{name} file is missing.")

    contract_status = "PASS" if not any(x.startswith("Contract ") for x in blockers) and gate_results.get("contract_qc", {}).get("exit_code") == 0 else "BLOCKED"
    graph_status = "PASS" if graph_text and not any(x.startswith("Total graph ") for x in blockers) else "BLOCKED"
    regression_status = "BLOCKED" if blockers else "PASS"
    verification_state = "BLOCKED" if blockers else "UNVERIFIED"

    record = {
        "event_id": "supreme-nlp-health-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "contract_status": contract_status,
        "schema_status": schema_status,
        "governance_status": governance_status,
        "graph_status": graph_status,
        "regression_status": regression_status,
        "verification_state": verification_state,
        "blockers": blockers,
        "warnings": warnings,
        "provenance": ["repository files", "deterministic contract checks", "executed QC gates"],
        "cycle_duration_seconds": round(time.monotonic() - started, 4),
        "gate_results": gate_results,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))

    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
