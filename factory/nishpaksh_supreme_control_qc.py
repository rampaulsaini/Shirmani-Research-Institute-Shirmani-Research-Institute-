#!/usr/bin/env python3
"""Deterministic QC for the Nishpaksh Supreme Control Contract."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "yatharth-governance" / "nishpaksh-supreme-control-contract.md"
GOV = ROOT / "schemas" / "agent-governance.json"

REQUIRED = [
    "Equal evaluation rule",
    "Evidence-first rule",
    "Counter-evidence rule",
    "Uncertainty rule",
    "No preference injection",
    "Conflict rule",
    "Independent verification rule",
    "Human-impact rule",
    "Audit rule",
    "Fail-closed rule",
    "Accuracy",
]

def main():
    text = CONTRACT.read_text(encoding="utf-8")
    missing = [term for term in REQUIRED if term not in text]
    if missing:
        raise SystemExit("Nishpaksh contract missing: " + ", ".join(missing))

    gov = json.loads(GOV.read_text(encoding="utf-8"))
    if gov.get("fail_closed") is not True:
        raise SystemExit("Governance is not fail-closed")
    if gov.get("provenance_required_for_claims") is not True:
        raise SystemExit("Claim provenance requirement is missing")
    if gov.get("fabrication_prohibited") is not True:
        raise SystemExit("Fabrication prohibition is missing")
    if gov.get("authorization", {}).get("verification_promotion") != "independent_verification_required":
        raise SystemExit("Independent verification boundary is missing")

    print("SHIRMANI Nishpaksh Supreme Control Contract: PASS")

if __name__ == "__main__":
    main()
