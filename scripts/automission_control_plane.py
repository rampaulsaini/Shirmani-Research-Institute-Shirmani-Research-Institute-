"""Fail-closed Automission control-plane primitives."""
from __future__ import annotations
import hashlib, json, time
from dataclasses import dataclass, field
from typing import Any, Iterable

UNKNOWN = "UNKNOWN"
DETERMINISTIC = "DETERMINISTIC"
ESCALATE_REVIEW = "ESCALATE_REVIEW"
QUARANTINE = "QUARANTINE"

@dataclass(frozen=True)
class AgentVote:
    agent_id: str
    decision: str
    confidence: float

@dataclass
class Decision:
    case_id: str
    decision: str
    confidence: float
    evidence_ids: list[str]
    abstained: bool
    route: str
    reasons: list[str] = field(default_factory=list)
    disagreement: bool = False

def fingerprint(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()

def route_decision(*, case_id: str, decision: str, confidence: float,
                   evidence_ids: Iterable[str], abstained: bool = False,
                   votes: Iterable[AgentVote] = (), evidence_conflict: bool = False) -> Decision:
    evidence = list(dict.fromkeys(evidence_ids))
    votes = list(votes)
    reasons = []
    disagreement = len({v.decision for v in votes}) > 1 if votes else False
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be within [0,1]")
    if abstained:
        decision = UNKNOWN
        reasons.append("abstention")
    if not evidence:
        reasons.append("missing_evidence")
    if confidence < 0.70:
        reasons.append("low_confidence")
    if evidence_conflict:
        reasons.append("conflicting_evidence")
    if disagreement:
        reasons.append("agent_disagreement")
    must_escalate = bool(reasons)
    route = ESCALATE_REVIEW if must_escalate else DETERMINISTIC
    if must_escalate and decision != UNKNOWN and (not evidence or evidence_conflict or disagreement):
        decision = UNKNOWN
    return Decision(case_id, decision, confidence, evidence, decision == UNKNOWN,
                    route, reasons, disagreement)

def detect_drift(baseline: dict[str, Any], current: dict[str, Any],
                 relative_threshold: float = 0.20) -> dict[str, Any]:
    changes = {}
    for key in sorted(set(baseline) | set(current)):
        if key not in baseline or key not in current:
            changes[key] = {"kind": "schema_change"}
            continue
        old, new = baseline[key], current[key]
        if isinstance(old, (int, float)) and isinstance(new, (int, float)):
            relative = abs(float(new) - float(old)) / max(abs(float(old)), 1e-12)
            if relative > relative_threshold:
                changes[key] = {"kind": "numeric_drift", "relative_change": relative}
        elif old != new:
            changes[key] = {"kind": "value_drift"}
    return {"drift": bool(changes), "changes": changes,
            "action": QUARANTINE if changes else "CONTINUE"}

def recover(attempts: int, max_attempts: int = 2, idempotent: bool = True) -> dict[str, Any]:
    if attempts < 0:
        raise ValueError("attempts cannot be negative")
    if attempts >= max_attempts or not idempotent:
        return {"action": QUARANTINE, "attempts": attempts, "retry_allowed": False}
    return {"action": "RETRY", "attempts": attempts + 1, "retry_allowed": True}

def audit_record(*, event_id: str, component: str, model_version: str,
                 policy_version: str, input_value: Any, decision: Decision,
                 latency_ms: float, previous_hash: str = "GENESIS",
                 timestamp: float | None = None) -> dict[str, Any]:
    body = {
        "event_id": event_id, "timestamp": timestamp if timestamp is not None else time.time(),
        "component": component, "model_version": model_version, "policy_version": policy_version,
        "input_fingerprint": fingerprint(input_value), "route": decision.route,
        "decision": decision.decision, "confidence": decision.confidence,
        "abstained": decision.abstained, "evidence_ids": decision.evidence_ids,
        "latency_ms": float(latency_ms), "reasons": decision.reasons,
        "previous_hash": previous_hash,
    }
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    body["record_hash"] = "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return body

def validate_audit_chain(records: Iterable[dict[str, Any]]) -> bool:
    previous = "GENESIS"
    required = {"event_id","timestamp","component","model_version","policy_version",
                "input_fingerprint","route","decision","confidence","abstained",
                "evidence_ids","latency_ms","record_hash"}
    for record in records:
        if record.get("previous_hash") != previous or not required.issubset(record):
            return False
        body = {k: v for k, v in record.items() if k != "record_hash"}
        canonical = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        expected = "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        if record["record_hash"] != expected:
            return False
        previous = record["record_hash"]
    return True

if __name__ == "__main__":
    d = route_decision(case_id="self-test", decision="SUPPORTED", confidence=0.91,
                       evidence_ids=["fixture:e1"],
                       votes=[AgentVote("a","SUPPORTED",0.91), AgentVote("b","SUPPORTED",0.90),
                              AgentVote("c","SUPPORTED",0.92)])
    a = audit_record(event_id="self-test-1", component="control-plane",
                     model_version="test", policy_version="1.0.0",
                     input_value={"case": "self-test"}, decision=d, latency_ms=1)
    assert d.route == DETERMINISTIC and validate_audit_chain([a])
    assert route_decision(case_id="unsafe", decision="SUPPORTED", confidence=0.99,
                          evidence_ids=[]).decision == UNKNOWN
    assert detect_drift({"x":100},{"x":130})["action"] == QUARANTINE
    assert recover(2)["action"] == QUARANTINE
    print(json.dumps({"status":"PASS","mode":"FAIL_CLOSED","independent_verified_claims":0}, indent=2))
