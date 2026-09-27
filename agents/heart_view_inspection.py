"""Purpose-first, evidence-aware inspection state engine.

This module deliberately does not perform biometric identification, protected-trait
inference, autonomous hiring, public-office qualification, or moral-worth scoring.
"""
from dataclasses import dataclass, field
from typing import List

PURPOSES = {
    "SELF_HUMAN_REFLECTION",
    "EDUCATION",
    "JOB_OR_ROLE_APPLICATION",
    "PUBLIC_SERVICE_ROLE_REVIEW",
    "RESEARCH_PARTICIPATION",
    "OTHER_DECLARED_PURPOSE",
}

STATES = [
    "DRAFT","IN_REVIEW","EXPLAINED","HUMAN_REVIEW_REQUIRED",
    "APPEAL_OPEN","FINALIZED","ARCHIVED"
]

@dataclass
class Inspection:
    purpose: str
    consent: bool = False
    evidence: List[str] = field(default_factory=list)
    state: str = "DRAFT"
    warnings: List[str] = field(default_factory=list)

    def validate(self) -> None:
        if self.purpose not in PURPOSES:
            raise ValueError("PURPOSE_REQUIRED")
        if not self.consent:
            raise ValueError("CONSENT_REQUIRED")
        allowed = {"SELF_REPORTED","SOURCE_LINKED","TASK_OBSERVED",
                   "EXTERNALLY_VERIFIED","NOT_VERIFIED","DISPUTED"}
        unknown = set(self.evidence) - allowed
        if unknown:
            raise ValueError("UNKNOWN_EVIDENCE_STATE")

    def prepare(self) -> dict:
        self.validate()
        self.state = "IN_REVIEW"
        if self.purpose in {"JOB_OR_ROLE_APPLICATION", "PUBLIC_SERVICE_ROLE_REVIEW"}:
            self.state = "HUMAN_REVIEW_REQUIRED"
            self.warnings.append("CONSEQUENTIAL_DECISION_REQUIRES_ACCOUNTABLE_HUMAN_REVIEW")
        if not self.evidence or "NOT_VERIFIED" in self.evidence:
            self.warnings.append("EVIDENCE_INCOMPLETE_OR_NOT_INDEPENDENTLY_VERIFIED")
        return {
            "purpose": self.purpose,
            "state": self.state,
            "evidence": list(self.evidence),
            "warnings": list(self.warnings),
            "automation_limits": [
                "NO_BIOMETRIC_IDENTITY_DECISION",
                "NO_PROTECTED_TRAIT_INFERENCE",
                "NO_AUTONOMOUS_HIRING_OR_PUBLIC_OFFICE_DECISION",
                "NO_MORAL_WORTH_SCORE",
            ],
        }
