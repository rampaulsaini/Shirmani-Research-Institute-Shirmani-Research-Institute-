"""Fail-closed orchestration contract for the Nishpaksh live presenter.

This module does not clone a person, prove identity, or grant scientific
verification. It defines the deterministic boundary between:
question -> evidence/context -> answer policy -> authorized voice -> visual
presentation/lip-sync.

External providers (TTS/avatar/live transport) must supply their own consent,
authentication, availability and runtime guarantees.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Iterable
import re


INSUFFICIENT_EVIDENCE = "अभी पर्याप्त प्रमाण उपलब्ध नहीं है।"


@dataclass(frozen=True)
class EvidenceItem:
    title: str
    source: str
    independently_verified: bool = False
    supports_claim: bool = True


@dataclass(frozen=True)
class PresenterPolicy:
    authorized_voice: bool
    authorized_visual_identity: bool
    evidence_available: bool
    evidence_independently_verified: bool
    philosophical_identity_statement: bool = False
    harmful_or_disparaging: bool = False


def classify_claim(text: str) -> str:
    """Classify only the response boundary; never infer a person's identity."""
    lowered = (text or "").lower()
    identity_terms = (
        "मैं", "मेरा स्वरूप", "मेरा स्थायी परिचय", "सर्व भौमिक सत्य",
        "i am", "my identity", "my permanent identity",
    )
    scientific_terms = (
        "प्रमाण", "वैज्ञानिक", "science", "scientific", "evidence",
        "verified", "सिद्ध", "measurement", "experiment",
    )
    if any(term in lowered for term in scientific_terms):
        return "EMPIRICAL_OR_EVIDENCE_CLAIM"
    if any(term in lowered for term in identity_terms):
        return "PHILOSOPHICAL_OR_IDENTITY"
    return "GENERAL"


def build_answer_policy(
    question: str,
    evidence: Iterable[EvidenceItem],
    policy: PresenterPolicy,
) -> dict[str, Any]:
    """Return a presentation-safe answer policy.

    Rules:
    * never fabricate evidence;
    * never convert philosophical identity into scientific fact;
    * never present workflow success as independent verification;
    * never speak through an unauthorized voice/visual identity;
    * abstain when a factual claim lacks adequate supporting evidence.
    """
    items = [e for e in evidence if e.supports_claim]
    verified = [e for e in items if e.independently_verified]
    claim_class = classify_claim(question)

    if policy.harmful_or_disparaging:
        answer_mode = "RESPECTFUL_REFRAME"
    elif claim_class == "PHILOSOPHICAL_OR_IDENTITY":
        answer_mode = "ATTRIBUTE_AS_IDENTITY_OR_AUTHOR_CLAIM"
    elif not items:
        answer_mode = "ABSTAIN_INSUFFICIENT_EVIDENCE"
    elif claim_class == "EMPIRICAL_OR_EVIDENCE_CLAIM" and not verified:
        answer_mode = "ANSWER_WITH_UNVERIFIED_LABEL"
    else:
        answer_mode = "ANSWER_WITH_SOURCES"

    return {
        "claim_class": claim_class,
        "answer_mode": answer_mode,
        "evidence_count": len(items),
        "independently_verified_evidence_count": len(verified),
        "verification_status": "VERIFIED" if verified else "UNVERIFIED",
        "abstention_text": INSUFFICIENT_EVIDENCE
        if answer_mode == "ABSTAIN_INSUFFICIENT_EVIDENCE" else None,
        "presentation": {
            "authorized_voice_required": True,
            "authorized_voice_available": policy.authorized_voice,
            "authorized_visual_identity_required": True,
            "authorized_visual_identity_available": policy.authorized_visual_identity,
            "natural_eye_contact": True,
            "natural_facial_movement": True,
            "lip_sync_required": True,
            "voice_face_timing_coherence": True,
            "context_first": True,
        },
    }


def build_live_presentation_plan(
    question: str,
    evidence: Iterable[EvidenceItem],
    policy: PresenterPolicy,
) -> dict[str, Any]:
    """Build a provider-neutral plan for a live Q&A presenter."""
    answer = build_answer_policy(question, evidence, policy)

    # A missing authorization boundary must stop presentation rather than
    # silently falling back to another person's voice or identity.
    if not policy.authorized_voice or not policy.authorized_visual_identity:
        runtime_status = "BLOCKED_AUTHORIZATION"
    else:
        runtime_status = "READY_FOR_PROVIDER"

    return {
        "system": "NISHPAKSH-LIVE-PRESENTER-V1",
        "runtime_status": runtime_status,
        "pipeline": [
            "VOICE_INPUT_OR_TEXT_INPUT",
            "CONTEXT_RETRIEVAL",
            "EVIDENCE_CHECK",
            "ANSWER_POLICY",
            "AUTHORIZED_VOICE",
            "PHOTO_OR_AVATAR_PRESENTATION",
            "NATURAL_GAZE_AND_FACIAL_MOTION",
            "ACCURATE_LIP_SYNC",
            "LIVE_OUTPUT",
            "AUDIT_RECORD",
        ],
        "answer": answer,
        "audit": {
            "scientific_verification_granted": False,
            "workflow_success_is_not_scientific_verification": True,
            "identity_claims_are_not_auto_promoted_to_empirical_facts": True,
        },
    }


def render_answer(
    answer_policy: dict[str, Any],
    answer_text: str,
    sources: Iterable[EvidenceItem] = (),
) -> str:
    """Attach transparent status/source notes without changing the answer."""
    mode = answer_policy["answer_mode"]
    if mode == "ABSTAIN_INSUFFICIENT_EVIDENCE":
        return INSUFFICIENT_EVIDENCE
    if mode == "ANSWER_WITH_UNVERIFIED_LABEL":
        return f"{answer_text}\n\nस्थिति: UNVERIFIED — स्वतंत्र सत्यापन अभी स्थापित नहीं है।"
    if mode == "ATTRIBUTE_AS_IDENTITY_OR_AUTHOR_CLAIM":
        return f"{answer_text}\n\nस्थिति: यह पहचान/दार्शनिक वक्तव्य के रूप में प्रस्तुत है; इसे स्वतः वैज्ञानिक प्रमाण नहीं माना जाता।"

    source_lines = [f"- {item.title}: {item.source}" for item in sources if item.supports_claim]
    if source_lines:
        return f"{answer_text}\n\nस्रोत:\n" + "\n".join(source_lines)
    return answer_text


def contract_snapshot(question: str, evidence: Iterable[EvidenceItem], policy: PresenterPolicy) -> dict[str, Any]:
    """JSON-friendly snapshot for a UI, workflow, or audit record."""
    return asdict(policy) | build_live_presentation_plan(question, evidence, policy)
