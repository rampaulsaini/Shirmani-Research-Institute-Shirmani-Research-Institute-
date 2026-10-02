"""Minimal evidence-aware NLP result contract.

This module intentionally contains no claim that a sensor signal is a subjective
feeling. It provides a stable envelope for agents to attach observations,
inferences, evidence and uncertainty.
"""

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Verification:
    status: str = "unverified"
    independent_checks: list[str] = field(default_factory=list)


@dataclass
class AgentResult:
    task_id: str
    source_type: str
    claim: str
    evidence: list[Any] = field(default_factory=list)
    method: str = ""
    confidence: float = 0.0
    uncertainty: list[str] = field(default_factory=list)
    contradictions: list[str] = field(default_factory=list)
    verification: Verification = field(default_factory=Verification)
    plain_language: str = ""
    provenance: dict[str, str] = field(default_factory=dict)

    def validate(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.source_type not in {
            "measurement", "user_source", "external_evidence", "model_inference"
        }:
            raise ValueError("invalid source_type")
        if self.verification.status not in {
            "unverified", "verified", "rejected", "needs_review"
        }:
            raise ValueError("invalid verification status")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)
