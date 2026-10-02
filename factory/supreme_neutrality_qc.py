"""Fail-closed neutrality and evidence-boundary QC for Supreme Automission."""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main() -> None:
    contract = load("schemas/supreme-neutrality-contract.json")
    governance = load("schemas/agent-governance.json")
    nlp = load("schemas/supreme-nlp-contract.json")

    assert contract["automation_policy"]["fail_closed"] is True
    assert contract["automation_policy"]["autonomous_irreversible_action"] is False
    assert contract["automation_policy"]["autonomous_financial_action"] is False
    assert contract["automation_policy"]["autonomous_verification_promotion"] is False
    assert contract["automation_policy"]["source_rewriting"] is False
    assert contract["automation_policy"]["self_modifying_production_code"] is False

    assert governance["fail_closed"] is True
    assert governance["default_status"] == "unverified"
    assert governance["fabrication_prohibited"] is True
    assert governance["provenance_required_for_claims"] is True
    assert governance["authorization"]["verification_promotion"] == "independent_verification_required"

    assert nlp["fail_closed"] is True
    assert nlp["fabrication_prohibited"] is True
    assert nlp["human_review_for_high_impact"] is True
    assert nlp["truth_boundary"]["direct_feeling_claims"] == "NOT_INFERRED"
    assert nlp["truth_boundary"]["verified"] == "REQUIRES_INDEPENDENT_VERIFICATION_RECORD"

    print("SUPREME NEUTRALITY QC: PASS")
    print("Policy: evidence-first / fail-closed / independently verifiable / non-coercive")

if __name__ == "__main__":
    main()
