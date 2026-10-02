"""Fail-closed impartiality audit for Supreme NLP artifacts and policy."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    p = load_json(ROOT / "factory/supreme-nlp-impartiality-policy.json")
    assert p["fail_closed"] is True
    assert p["preferred_conclusion"] is None
    required = set(p["mandatory_fields"])
    assert required == {
        "evidence_refs", "counter_evidence_refs", "uncertainty",
        "verification_status", "provenance"
    }

    contract = load_json(ROOT / "schemas/supreme-nlp-contract.json")
    assert contract["fail_closed"] is True
    assert contract["truth_boundary"]["direct_feeling_claims"] == "NOT_INFERRED"
    assert contract["truth_boundary"]["verified"] == "REQUIRES_INDEPENDENT_VERIFICATION_RECORD"

    agent = (ROOT / "agents/supreme_nlp_agent.py").read_text(encoding="utf-8")
    assert '"status": "UNVERIFIED"' in agent
    assert "not direct proof of subjective emotion" in agent
    assert "independently verify before promotion" in agent

    practitioner = (ROOT / "agents/supreme_nlp_practitioner.py").read_text(encoding="utf-8")
    assert '"subjective_experience_claim_allowed":False' in practitioner
    assert '"independent_verification_required":True' in practitioner

    print("IMPARTIALITY_AUDIT=PASS")
    print("FAIL_CLOSED=PASS")
    print("PREFERRED_CONCLUSION=None")
    print("COUNTER_EVIDENCE_REQUIRED=PASS")
    print("INDEPENDENT_VERIFICATION_REQUIRED=PASS")

if __name__ == "__main__":
    main()
