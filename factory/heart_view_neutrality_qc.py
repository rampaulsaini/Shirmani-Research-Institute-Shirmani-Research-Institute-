#!/usr/bin/env python3
"""Deterministic fail-closed QC for SHIRMANI HEART-VIEW neutrality.

This gate checks governance invariants only. It never upgrades a claim's status.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "heart-view-neutrality-policy.json"

REQUIRED_STATUSES = {
    "USER_SOURCE", "AUTHOR_DEFINED", "AUTHOR_PROPOSED", "HYPOTHESIS",
    "EMPIRICAL_TESTABLE", "EVIDENCE_SUPPORTED", "NOT_VERIFIED",
    "CONTRADICTED", "VERIFIED"
}

def block(message: str) -> None:
    raise SystemExit(f"HEART-VIEW-NEUTRALITY-QC: BLOCK: {message}")

def main() -> int:
    try:
        p = json.loads(POLICY.read_text(encoding="utf-8"))
    except Exception as exc:
        block(f"cannot read policy: {exc}")

    principles = p.get("principles", {})
    required_true = (
        "equal_evidence_rules", "no_identity_weighting", "no_authority_weighting",
        "no_majority_truth_rule", "counter_evidence_required", "uncertainty_required",
        "provenance_required", "independent_verification_required",
        "source_claims_preserved_as_source_claims", "fail_closed"
    )
    for key in required_true:
        if principles.get(key) is not True:
            block(f"principle {key!r} is not enabled")

    if set(p.get("claim_statuses", [])) != REQUIRED_STATUSES:
        block("claim-status taxonomy is incomplete or changed")

    promotion = p.get("promotion_rules", {})
    for key in (
        "USER_SOURCE_to_VERIFIED",
        "AUTHOR_DEFINED_to_VERIFIED_without_test",
        "AUTHOR_PROPOSED_to_VERIFIED_without_test",
        "HYPOTHESIS_to_VERIFIED_without_independent_test",
    ):
        if promotion.get(key) is not False:
            block(f"unsafe promotion rule enabled: {key}")

    required_promotion = {
        "operational_definition", "independent_source_or_reproducible_test",
        "counter_evidence_review", "provenance", "reviewer_identity_or_role",
        "timestamp", "explicit_decision"
    }
    if set(promotion.get("EVIDENCE_SUPPORTED_to_VERIFIED_requires", [])) != required_promotion:
        block("verification promotion requirements are incomplete")

    boundary = p.get("multimodal_nlp_boundary", {})
    if boundary.get("subjective_experience_direct_claim_allowed") is not False:
        block("direct subjective-experience claims must remain blocked")
    if boundary.get("alternative_explanations_required") is not True:
        block("alternative explanations are not required")

    forbidden = set(p.get("optimization_targets", {}).get("never_optimize_by", []))
    required_forbidden = {
        "removing_uncertainty", "suppressing_counter_evidence",
        "inflating_confidence", "treating_repetition_as_proof",
        "treating_workflow_success_as_verification"
    }
    if forbidden != required_forbidden:
        block("optimization safety constraints are incomplete")

    print("HEART-VIEW-NEUTRALITY-QC: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
