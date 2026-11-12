"""Fail-closed validator for the SHIRMANI impartial Automission contract."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs" / "SHIRMANI-NISHPAKSH-AUTOMISSION-CONTRACT.md"
REQUIRED_POLICY_TERMS = [
    "Person-neutral", "Doctrine-neutral", "Evidence-first",
    "Independent verification", "Counter-evidence",
    "No subjective-experience leap", "No scheduled production mutation",
    "Human agency", "Fail closed",
]

def main() -> None:
    text = POLICY.read_text(encoding="utf-8")
    missing = [x for x in REQUIRED_POLICY_TERMS if x not in text]
    if missing: raise SystemExit(f"POLICY_INCOMPLETE: {missing}")

    for path in [
        ROOT / "generated/supreme-nlp/status.json",
        ROOT / "generated/supreme-nlp/practitioner-status.json",
        ROOT / "generated/supreme-orchestrator/status.json",
]:
        if not path.exists(): continue
        data = json.loads(path.read_text(encoding="utf-8"))
        governance = data.get("governance", {})
        if governance:
            if governance.get("fail_closed") is not True: raise SystemExit(f"FAIL_CLOSED_REQUIRED: {path}")
            if governance.get("independent_verification_required") is not True: raise SystemExit(f"INDEPENDENT_VERIFICATION_REQUIRED: {path}")
            if governance.get("subjective_experience_claim_allowed") is True: raise SystemExit(f"SUBJECTIVE_EXPERIENCE_BOUNDARY_BROKEN: {path}")
            if governance.get("code_mutation_allowed") is True: raise SystemExit(f"CODE_MUTATION_BOUNDARY_BROKEN: {path}")
    print("SHIRMANI_NISHPAKSH_GOVERNANCE: PASS")
if __name__ == "__main__": main()
