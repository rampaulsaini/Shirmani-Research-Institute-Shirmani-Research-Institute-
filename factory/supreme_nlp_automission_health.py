import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-automission-health.json"
HEALTH_SCHEMA = ROOT / "schemas/supreme-nlp-automission-health.schema.json"

REQUIRED_FILES = [
    "docs/supreme-nlp-practitioner-contract.md",
    "docs/supreme-nlp-evaluation-gate.md",
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "schemas/supreme-nlp-evaluation.schema.json",
    "schemas/supreme-nlp-automission-health.schema.json",
    "schemas/agent-governance.json",
    "factory/supreme_nlp_contract_qc.py",
    "factory/supreme_nlp_evaluation_qc.py",
    "docs/supreme-nlp-multimodal-signal-language-contract.md",
    "schemas/supreme-nlp-signal-interpretation.schema.json",
    "factory/supreme_nlp_signal_interpretation_qc.py",
]

def fingerprint(paths):
    h = hashlib.sha256()
    for rel in paths:
        p = ROOT / rel
        h.update(rel.encode())
        h.update(p.read_bytes())
    return h.hexdigest()

def run_gate(path):
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode, (result.stdout + result.stderr).strip()

HEALTH_REQUIRED = {
    "event_id", "timestamp", "repository", "contract_status", "schema_status",
    "governance_status", "graph_status", "regression_status",
    "verification_state", "blockers", "warnings", "provenance",
    "cycle_duration_seconds", "gate_results",
}

STATUS_VALUES = {
    "contract_status": {"PASS", "BLOCKED"},
    "schema_status": {"PASS", "BLOCKED"},
    "governance_status": {"PASS", "BLOCKED"},
    "graph_status": {"PASS", "BLOCKED"},
    "regression_status": {"PASS", "REVIEW", "BLOCKED"},
    "verification_state": {"REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"},
}

def schema_contract_check():
    if not HEALTH_SCHEMA.is_file():
        return ["Health schema file is missing."]
    try:
        schema = json.loads(HEALTH_SCHEMA.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["Health schema JSON is invalid."]
    if set(schema.get("required", [])) != HEALTH_REQUIRED:
        return ["Health schema required keys do not match the deterministic contract."]
    for field, allowed in STATUS_VALUES.items():
        actual = set(schema.get("properties", {}).get(field, {}).get("enum", []))
        if actual != allowed:
            return [f"Health schema enum mismatch for {field}."]
    if schema.get("additionalProperties") is not False:
        return ["Health schema must reject undeclared properties."]
    return []

def record_contract_check(record):
    blockers = []
    if set(record) != HEALTH_REQUIRED:
        blockers.append("Generated health record keys do not exactly match the health schema contract.")
    for field, allowed in STATUS_VALUES.items():
        if record.get(field) not in allowed:
            blockers.append(f"Invalid {field}: {record.get(field)!r}.")
    if not isinstance(record.get("blockers"), list) or not isinstance(record.get("warnings"), list):
        blockers.append("blockers/warnings must be arrays.")
    if not isinstance(record.get("provenance"), list) or not record.get("provenance"):
        blockers.append("provenance must be a non-empty array.")
    if not isinstance(record.get("cycle_duration_seconds"), (int, float)) or record.get("cycle_duration_seconds") < 0:
        blockers.append("cycle_duration_seconds must be a non-negative number.")
    return blockers

def main():
    started = time.monotonic()
    blockers = []
    warnings = []
    blockers.extend(schema_contract_check())

    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        blockers.append("Missing required files: " + ", ".join(missing))

    contract = ROOT / "docs/supreme-nlp-practitioner-contract.md"
    graph = ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
    gov = ROOT / "schemas/agent-governance.json"
    schema = ROOT / "schemas/supreme-nlp-evaluation.schema.json"

    contract_text = contract.read_text(encoding="utf-8") if contract.exists() else ""
    graph_text = graph.read_text(encoding="utf-8") if graph.exists() else ""

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
    if gov.exists():
        try:
            g = json.loads(gov.read_text(encoding="utf-8"))
            if all(g.get(k) is True for k in [
                "fail_closed", "provenance_required_for_claims", "fabrication_prohibited"
            ]):
                governance_status = "PASS"
            else:
                blockers.append("Agent governance is not fully fail-closed.")
        except json.JSONDecodeError:
            blockers.append("Agent governance JSON is invalid.")

    schema_status = "BLOCKED"
    if schema.exists():
        try:
            s = json.loads(schema.read_text(encoding="utf-8"))
            required = set(s.get("required", []))
            expected = {
                "record_id", "task", "dataset_fingerprint", "model", "metric",
                "baseline", "result", "confidence", "provenance", "verification_state"
            }
            if expected.issubset(required):
                schema_status = "PASS"
            else:
                blockers.append("Supreme NLP evaluation schema is missing required keys.")
        except json.JSONDecodeError:
            blockers.append("Supreme NLP evaluation schema is invalid.")

    gate_results = {}
    for name, path in [
        ("contract_qc", ROOT / "factory/supreme_nlp_contract_qc.py"),
        ("evaluation_qc", ROOT / "factory/supreme_nlp_evaluation_qc.py"),
        ("signal_interpretation_qc", ROOT / "factory/supreme_nlp_signal_interpretation_qc.py"),
    ]:
        if path.exists():
            code, output = run_gate(path)
            gate_results[name] = {"exit_code": code, "output": output[-2000:]}
            if code != 0:
                blockers.append(f"{name} failed with exit code {code}.")
        else:
            gate_results[name] = {"exit_code": None, "output": "missing"}
            blockers.append(f"{name} file is missing.")

    contract_status = "PASS" if contract_text and not any("Contract" in x for x in blockers) and gate_results["contract_qc"]["exit_code"] == 0 else "BLOCKED"
    graph_status = "PASS" if graph_text and not any("Total graph" in x for x in blockers) else "BLOCKED"
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
    record_blockers = record_contract_check(record)
    if record_blockers:
        print("\n".join(record_blockers))
        raise SystemExit(1)
    print(json.dumps(record, ensure_ascii=False, indent=2))

    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
