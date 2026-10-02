import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-integrity-governor.json"

REQUIRED = [
    "docs/supreme-nlp-practitioner-contract.md",
    "docs/supreme-nlp-evaluation-gate.md",
    "docs/supreme-nlp-benchmark-and-self-improvement.md",
    "docs/supreme-ai-ml-nlp-automission-total-graph-2026-10-01.md",
    "docs/ultra-mega-infinity-quantum-ai-ml-nlp-automission.md",
    "schemas/agent-governance.json",
    "schemas/supreme-nlp-evaluation.schema.json",
    "schemas/supreme-nlp-automission-health.schema.json",
    "schemas/supreme-nlp-benchmark-record.schema.json",
]

GATES = [
    ("contract_qc", "factory/supreme_nlp_contract_qc.py"),
    ("evaluation_qc", "factory/supreme_nlp_evaluation_qc.py"),
    ("health_qc", "factory/supreme_nlp_automission_health.py"),
    ("benchmark_controller", "factory/supreme_nlp_benchmark_controller.py"),
    ("quantum_orchestrator", "factory/ultra_mega_infinity_quantum_automission.py"),
]

REQUIRED_TERMS = {
    "docs/supreme-nlp-practitioner-contract.md": [
        "Measured signal", "Model inference", "Interpretation",
        "Confidence", "Unresolved uncertainty", "Independent verification"
    ],
    "docs/ultra-mega-infinity-quantum-ai-ml-nlp-automission.md": [
        "Multimodal Perception", "Agent Mesh", "Five-minute loop",
        "Fail-closed", "Accuracy"
    ],
}

def run(path):
    p = ROOT / path
    if not p.is_file():
        return {"status": "MISSING", "exit_code": None, "output": ""}
    r = subprocess.run(
        [sys.executable, str(p)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    return {
        "status": "PASS" if r.returncode == 0 else "FAIL",
        "exit_code": r.returncode,
        "output": (r.stdout + r.stderr)[-1800:],
    }

def main():
    started = time.monotonic()
    blockers = []
    warnings = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            blockers.append("missing:" + rel)

    for rel, terms in REQUIRED_TERMS.items():
        p = ROOT / rel
        if p.exists():
            body = p.read_text(encoding="utf-8")
            for term in terms:
                if term not in body:
                    blockers.append(f"contract-missing:{rel}:{term}")

    gov = ROOT / "schemas/agent-governance.json"
    if gov.exists():
        try:
            data = json.loads(gov.read_text(encoding="utf-8"))
            for key in ("fail_closed", "provenance_required_for_claims", "fabrication_prohibited"):
                if data.get(key) is not True:
                    blockers.append("governance-fail-open:" + key)
        except json.JSONDecodeError:
            blockers.append("governance-invalid-json")

    results = {}
    for name, path in GATES:
        results[name] = run(path)
        if results[name]["status"] != "PASS":
            blockers.append(f"gate-failed:{name}")

    # A workflow/gate pass is deliberately NOT treated as model accuracy.
    accuracy_evidence = "NOT_ESTABLISHED"
    verification_state = "BLOCKED" if blockers else "UNVERIFIED"

    record = {
        "event_id": "supreme-nlp-integrity-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repository": "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
        "governor_status": "BLOCKED" if blockers else "READY_FOR_EVALUATION",
        "verification_state": verification_state,
        "accuracy_evidence": accuracy_evidence,
        "accuracy_rule": "Workflow success is not model accuracy; benchmark evidence is required.",
        "self_improvement_rule": "Proposal-only; production self-modification requires human authorization.",
        "biological_signal_rule": "Signals may be translated into plain language, but signal, inference, interpretation, confidence and uncertainty remain distinct.",
        "fail_closed": True,
        "blockers": blockers,
        "warnings": warnings,
        "gate_results": results,
        "cycle_duration_seconds": round(time.monotonic() - started, 4),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    if blockers:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
