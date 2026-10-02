"""Fail-closed governance gate for the Supreme AI/ML/NLP Automission stack."""
from __future__ import annotations
import json
from pathlib import Path
from agents.impartiality_guard import assert_contract, merge_governance

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "agents/impartiality_guard.py",
    "docs/SUPREME-IMPARTIALITY-CONTRACT.md",
    "agents/supreme_nlp.py",
    "agents/automission_supervisor.py",
    "factory/supreme_system_orchestrator.py",
)

def _read(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        raise AssertionError(f"IMPARTIALITY_BLOCK: missing {path}")
    return p.read_text(encoding="utf-8")

def _check_workflows_are_read_only() -> None:
    wf = ROOT / ".github" / "workflows"
    for p in wf.glob("*.yml"):
        text = p.read_text(encoding="utf-8")
        if "schedule:" in text and "contents: write" in text:
            raise AssertionError(f"IMPARTIALITY_BLOCK: scheduled workflow requests contents: write: {p}")

def main() -> int:
    for path in REQUIRED:
        _read(path)
    contract_doc = _read("docs/SUPREME-IMPARTIALITY-CONTRACT.md")
    for phrase in ("Evidence first", "Identity-neutral evaluation", "Counter-evidence", "Fail closed", "Measured accuracy"):
        if phrase not in contract_doc:
            raise AssertionError(f"IMPARTIALITY_BLOCK: contract missing phrase: {phrase}")
    _check_workflows_are_read_only()
    base = {
        "fail_closed": True,
        "scheduled_code_mutation_allowed": False,
        "subjective_experience_claim_allowed": False,
        "independent_verification_required": True,
        "accuracy_is_measured_not_declared": True,
    }
    governance = merge_governance(base)
    assert_contract(governance)
    candidates = (
        ROOT / "generated" / "supreme-orchestrator" / "status.json",
        ROOT / "generated" / "supreme-nlp" / "automission-plan.json",
        ROOT / "generated" / "supreme-nlp" / "practitioner-status.json",
    )
    checked = 0
    for p in candidates:
        if not p.is_file():
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        assert_contract(data.get("governance") or {})
        checked += 1
    out = {
        "status": "PASS",
        "contract_version": "impartiality-v1",
        "generated_or_committed_records_checked": checked,
        "governance": governance,
        "failure_mode": "IMPARTIALITY_BLOCK",
    }
    out_path = ROOT / "generated" / "impartiality" / "status.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
