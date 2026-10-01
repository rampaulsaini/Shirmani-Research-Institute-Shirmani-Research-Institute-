"""Controlled continuous-improvement engine for Automission.

The engine is intentionally idempotent and evidence-gated:
OBSERVE -> ANALYZE -> PROPOSE -> TEST -> VERIFY -> AUDIT -> PUBLISH.
No stage may silently upgrade an unverified claim to verified.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any
import hashlib, json


STAGES = ("observe", "analyze", "propose", "test", "verify", "audit", "publish")


@dataclass(frozen=True)
class MissionResult:
    mission_id: str
    stage: str
    status: str
    verification_required: bool
    evidence: list[str]
    metrics: dict[str, float]
    created_at: str


def mission_id(payload: Any) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def run_cycle(payload: dict[str, Any], metrics: dict[str, float] | None = None) -> dict[str, Any]:
    mid = mission_id(payload)
    m = dict(metrics or {})
    result = MissionResult(
        mission_id=mid,
        stage="verify",
        status="candidate",
        verification_required=True,
        evidence=list(payload.get("evidence", [])),
        metrics=m,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    return asdict(result)


def publish_gate(result: dict[str, Any]) -> tuple[bool, list[str]]:
    errors = []
    if result.get("verification_required") is not True:
        errors.append("VERIFICATION_GATE_MISSING")
    if not result.get("evidence"):
        errors.append("EVIDENCE_MISSING")
    if result.get("status") != "verified":
        errors.append("NOT_INDEPENDENTLY_VERIFIED")
    return (not errors, errors)
