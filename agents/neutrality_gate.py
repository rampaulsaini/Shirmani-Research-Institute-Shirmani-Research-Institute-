"""Fail-closed neutrality and evidence gate for Supreme NLP Automission.

The user's Yatharth/Heart-View material is preserved as source material. This gate
does not decide whether that worldview is true or false. It separates:
SOURCE statements -> MODEL interpretations -> EVIDENCE -> VERIFICATION.

A scheduled run may diagnose and propose work, but cannot promote a claim to fact
or mutate production code.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Iterable
import hashlib
import json
from datetime import datetime, timezone


@dataclass(frozen=True)
class GateDecision:
    status: str
    reason_codes: tuple[str, ...]
    source_separation: bool
    evidence_required: bool
    independent_verification_required: bool
    production_mutation_allowed: bool
    generated_at: str


BLOCKING = {
    "UNVERIFIED",
    "SUBJECTIVE_EXPERIENCE_UNPROVEN",
    "SOURCE_AS_FACT",
    "MISSING_PROVENANCE",
    "CONFLICTING_EVIDENCE",
}


def classify(statement: dict[str, Any]) -> GateDecision:
    reasons: list[str] = []
    claim_type = str(statement.get("claim_type", "")).upper()
    verification = str(statement.get("verification_status", "UNVERIFIED")).upper()
    provenance = statement.get("provenance")
    evidence = statement.get("evidence", [])

    if not provenance:
        reasons.append("MISSING_PROVENANCE")
    if claim_type == "SOURCE_WORLDVIEW":
        reasons.append("SOURCE_AS_FACT")
    if claim_type in {"SUBJECTIVE_EXPERIENCE", "CONSCIOUSNESS_CLAIM"}:
        reasons.append("SUBJECTIVE_EXPERIENCE_UNPROVEN")
    if verification != "VERIFIED":
        reasons.append("UNVERIFIED")
    if not evidence:
        reasons.append("MISSING_EVIDENCE")

    reasons = list(dict.fromkeys(reasons))
    blocking = any(x in BLOCKING or x == "MISSING_EVIDENCE" for x in reasons)
    return GateDecision(
        status="HOLD" if blocking else "PASS",
        reason_codes=tuple(reasons),
        source_separation=claim_type != "SOURCE_WORLDVIEW",
        evidence_required=True,
        independent_verification_required=True,
        production_mutation_allowed=False,
        generated_at=datetime.now(timezone.utc).isoformat(),
    )


def audit(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    decisions = [classify(x) for x in records]
    held = sum(d.status == "HOLD" for d in decisions)
    passed = len(decisions) - held
    payload = [asdict(d) for d in decisions]
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return {
        "schema_version": "supreme-nlp-neutrality-v1",
        "status": "PASS" if held == 0 else "HOLD",
        "records": len(decisions),
        "passed": passed,
        "held": held,
        "decisions": payload,
        "fingerprint": digest,
        "governance": {
            "fail_closed": True,
            "source_worldview_is_not_automatically_fact": True,
            "subjective_experience_requires_operational_evidence": True,
            "independent_verification_required": True,
            "scheduled_production_code_mutation_allowed": False,
        },
    }
