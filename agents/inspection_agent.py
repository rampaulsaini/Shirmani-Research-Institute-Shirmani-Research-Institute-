"""Deterministic contract checks for Heart-View Inspection.

This module does not infer truth, personality, emotion, political preference,
mental state, or human worth. It validates session structure and safety gates.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

ALLOWED_TARGETS = {"SELF","EDUCATION","EMPLOYMENT","PUBLIC_SERVICE","PUBLIC_OFFICE","SKILL","CONTRIBUTION","OTHER"}
BIOMETRIC_KEYS = {"face","iris","eye","finger_vein","voice","gait","emotion"}

@dataclass(frozen=True)
class InspectionDecision:
    status: str
    reasons: tuple[str, ...]

def validate_session(session: Mapping[str, Any]) -> InspectionDecision:
    reasons: list[str] = []
    target = session.get("target", {})
    if target.get("type") not in ALLOWED_TARGETS:
        reasons.append("TARGET_REQUIRED_OR_UNSUPPORTED")
    consent = session.get("consent", {})
    if consent.get("analysis") is not True:
        reasons.append("ANALYSIS_CONSENT_REQUIRED")
    if consent.get("biometric_processing") is True:
        reasons.append("BIOMETRIC_PROCESSING_REQUIRES_SEPARATE_REVIEW")
    device = session.get("device_signals")
    if isinstance(device, Mapping):
        forbidden = sorted(set(device) & BIOMETRIC_KEYS)
        if forbidden:
            reasons.append("BIOMETRIC_INFERENCE_BLOCKED:" + ",".join(forbidden))
    claims = session.get("claims", [])
    if not isinstance(claims, list):
        reasons.append("CLAIMS_MUST_BE_A_LIST")
    else:
        for claim in claims:
            if not claim.get("evidence_refs"):
                reasons.append(f"EVIDENCE_MISSING:{claim.get('claim_id', 'unknown')}")
    if reasons:
        return InspectionDecision("CHECK", tuple(reasons))
    return InspectionDecision("HUMAN_REVIEW", ("STRUCTURE_AND_SAFETY_GATES_PASS",))

def summarize(session: Mapping[str, Any]) -> dict[str, Any]:
    decision = validate_session(session)
    return {"session_id": session.get("session_id"), "target": session.get("target", {}).get("type"), "status": decision.status, "reasons": list(decision.reasons), "verification": "NOT_VERIFIED", "automation_boundary": "QC_IS_NOT_INDEPENDENT_VERIFICATION"}
