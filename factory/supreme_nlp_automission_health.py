import json
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-automission-health.json"

REQUIRED_FILES = [
    "docs/supreme-nlp-practitioner-contract.md",
    "docs/supreme-nlp-evaluation-gate.md",
    "docs/supreme-nlp-signal-to-language-contract-2026-10-02.md",
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "schemas/supreme-nlp-evaluation.schema.json",
    "schemas/supreme-nlp-automission-health.schema.json",
    "schemas/agent-governance.json",
    "factory/supreme_nlp_contract_qc.py",
    "factory/supreme_nlp_evaluation_qc.py",
    "factory/supreme_nlp_regression_gate.py",
]

def main():
    started = time.monotonic()
    blockers = []
    warnings = []

    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        blockers.append("Missing required files: " + ", ".join(missing))

    contract = ROOT / "docs/supreme-nlp-practitioner-contract.md"
    signal_contract = ROOT / "docs/supreme-nlp-signal-to-language-contract-2026-10-02.md"
    graph = ROOT / "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md"
    gov = ROOT / "schemas/agent-governance.json"
    schema = ROOT / "schemas/supreme-nlp-evaluation.schema.json"

    contract_text = contract.read_text(encoding="utf-8") if contract.exists() else ""
    signal_text = signal_contract.read_text(encoding="utf-8") if signal_contract.exists() else ""
    graph_text = graph.read_text(encoding="utf-8") if graph.exists() else ""

    for term in [
        "Measured signal", "Model inference", "Interpretation",
        "Confidence", "Unresolved uncertainty", "Accuracy is measured",
        "Fail-closed rules", "Independent verification"
    ]:
        if term not in contract_text:
            blockers.append("Contract missing required term: " + term)

    for term in [
        "Canonical pipeline", "Detected pattern", "Plain-language interpretation",
        "Feeling boundary", "Accuracy", "Automission role"
    ]:
        if term not in signal_text:
            blockers.append("Signal-to-language contract missing required term: " + term)

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

    contract_status = "PASS" if contract_text and signal_text and not any(
        "Contract" in x or "Signal-to-language" in x for x in blockers
    ) else "BLOCKED"
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
        "provenance": ["repository files", "deterministic contract checks"],
        "cycle_duration_seconds": round(time.monotonic() - started, 4),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))

    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
