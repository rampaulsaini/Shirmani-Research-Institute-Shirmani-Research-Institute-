"""Fail-closed verification helpers.

These helpers distinguish source-backed evidence from independent verification.
Evidence alone can never produce a VERIFIED decision.
"""
from __future__ import annotations

from typing import Any


def classify(text: str, source: str | None = None) -> dict[str, Any]:
    """Classify provenance without implying truth."""
    if source:
        return {
            "status": "source-backed",
            "reason": "Source trace exists; external truth is not implied.",
            "independent": False,
            "verification_status": "NOT_VERIFIED",
        }
    return {
        "status": "unverified",
        "reason": "No source trace was supplied.",
        "independent": False,
        "verification_status": "NOT_VERIFIED",
    }


def verify(
    text: str,
    evidence: str = "",
    *,
    independent: bool = False,
    reviewer: str = "",
    reviewer_role: str = "",
    counter_evidence_reviewed: bool = False,
    reproducibility_status: str = "",
    audit_recorded: bool = False,
) -> dict[str, Any]:
    """Return a verification state without manufacturing independent review.

    A claim is VERIFIED only when all independent-review prerequisites are
    explicitly present. Merely supplying evidence never promotes a claim.
    """
    prerequisites = {
        "evidence": bool(evidence.strip()),
        "independent": independent is True,
        "reviewer": bool(reviewer.strip()),
        "reviewer_role": bool(reviewer_role.strip()),
        "counter_evidence_reviewed": counter_evidence_reviewed is True,
        "reproducible_test": reproducibility_status.upper() in {"PASSED", "SUPPORTED"},
        "audit_recorded": audit_recorded is True,
    }
    verified = all(prerequisites.values())

    return {
        "text": text,
        "status": "verified" if verified else "unverified",
        "verification_status": "VERIFIED" if verified else "NOT_VERIFIED",
        "independent": independent is True,
        "evidence": evidence,
        "prerequisites": prerequisites,
        "fail_closed": True,
    }
