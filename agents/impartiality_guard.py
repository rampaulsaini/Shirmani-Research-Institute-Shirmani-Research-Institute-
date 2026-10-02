"""Machine-enforced impartiality contract for the SHIRMANI AI/ML/NLP stack."""
from __future__ import annotations
from typing import Any

CONTRACT_VERSION = "impartiality-v1"
REQUIRED_TRUE = (
    "evidence_first", "identity_neutral_evaluation", "uncertainty_explicit",
    "counterevidence_required_for_strong_claims", "no_person_or_group_preference",
    "independent_verification_required", "accuracy_is_measured_not_declared", "fail_closed",
)
REQUIRED_FALSE = ("scheduled_code_mutation_allowed", "subjective_experience_claim_allowed")

def contract() -> dict[str, Any]:
    return {
        "version": CONTRACT_VERSION,
        "evidence_first": True,
        "identity_neutral_evaluation": True,
        "uncertainty_explicit": True,
        "counterevidence_required_for_strong_claims": True,
        "no_person_or_group_preference": True,
        "independent_verification_required": True,
        "accuracy_is_measured_not_declared": True,
        "fail_closed": True,
        "scheduled_code_mutation_allowed": False,
        "subjective_experience_claim_allowed": False,
    }

def assert_contract(governance: dict[str, Any]) -> None:
    expected = contract()
    for key in REQUIRED_TRUE:
        if governance.get(key) is not True:
            raise AssertionError(f"IMPARTIALITY_BLOCK: {key} must be true")
    for key in REQUIRED_FALSE:
        if governance.get(key) is not False:
            raise AssertionError(f"IMPARTIALITY_BLOCK: {key} must be false")
    if governance.get("impartiality_contract_version") != CONTRACT_VERSION:
        raise AssertionError("IMPARTIALITY_BLOCK: wrong or missing contract version")
    for key, value in expected.items():
        if key in governance and governance[key] != value:
            raise AssertionError(f"IMPARTIALITY_BLOCK: immutable field mismatch: {key}")

def merge_governance(base: dict[str, Any]) -> dict[str, Any]:
    out = dict(base)
    out.update(contract())
    out["impartiality_contract_version"] = CONTRACT_VERSION
    return out
