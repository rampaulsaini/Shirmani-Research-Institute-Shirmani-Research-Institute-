"""Fail-closed scientific validation protocol checker."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PROTOCOL = {
    "operational_definition", "population_scope", "sampling_plan",
    "instrument_calibration", "preprocessing_version", "model_version",
    "primary_endpoint", "evaluation_population", "blinded_holdout",
    "positive_controls", "negative_controls", "independent_replication",
    "counter_evidence_plan", "analysis_plan",
}

REQUIRED_EVIDENCE = {
    "observations", "measurement_quality", "task_metrics",
    "calibration_metrics", "holdout_results", "replication_results",
    "counter_evidence_review", "audit",
}

ALLOWED_STATUS = {"REGISTERED", "UNVERIFIED", "REVIEW", "VERIFIED", "BLOCKED"}


def sha256(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def validate_protocol(protocol: dict[str, Any]) -> list[str]:
    errors = [f"MISSING_PROTOCOL:{k}" for k in sorted(REQUIRED_PROTOCOL - protocol.keys())]
    if protocol.get("status", "UNVERIFIED") not in ALLOWED_STATUS:
        errors.append("INVALID_STATUS")
    if protocol.get("blinded_holdout") is not True:
        errors.append("BLINDED_HOLDOUT_REQUIRED")
    if protocol.get("independent_replication") is not True:
        errors.append("INDEPENDENT_REPLICATION_REQUIRED")
    if protocol.get("counter_evidence_plan") is not True:
        errors.append("COUNTER_EVIDENCE_PLAN_REQUIRED")
    return errors


def validate_evidence(evidence: dict[str, Any]) -> list[str]:
    return [f"MISSING_EVIDENCE:{k}" for k in sorted(REQUIRED_EVIDENCE - evidence.keys())]


def evaluate(protocol: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    errors = validate_protocol(protocol) + validate_evidence(evidence)
    metrics = evidence.get("task_metrics", {})
    holdout = evidence.get("holdout_results", {})
    replication = evidence.get("replication_results", {})
    calibration = evidence.get("calibration_metrics", {})

    if not metrics:
        errors.append("TASK_METRICS_EMPTY")
    if holdout.get("locked") is not True:
        errors.append("LOCKED_HOLDOUT_REQUIRED")
    if replication.get("independent") is not True:
        errors.append("INDEPENDENT_REPLICATION_REQUIRED")
    if calibration.get("evaluated") is not True:
        errors.append("CALIBRATION_EVALUATION_REQUIRED")
    if evidence.get("counter_evidence_review", {}).get("reviewed") is not True:
        errors.append("COUNTER_EVIDENCE_REVIEW_REQUIRED")
    if evidence.get("audit", {}).get("passed") is not True:
        errors.append("AUDIT_REQUIRED")

    verified = not errors and protocol.get("status") == "VERIFIED"
    return {
        "protocol_id": protocol.get("protocol_id", "unregistered"),
        "status": "VERIFIED" if verified else ("BLOCKED" if errors else "UNVERIFIED"),
        "verification_state": "VERIFIED" if verified else "UNVERIFIED",
        "promotion_allowed": verified,
        "errors": errors,
        "evidence_fingerprint": sha256(evidence),
        "governance": {
            "fail_closed": True,
            "automation_can_calculate_eligibility": True,
            "automation_can_create_independent_review": False,
            "subjective_experience_claim_allowed": False,
        },
    }


def main() -> int:
    protocol = {
        "protocol_id": "supreme-nlp-scientific-validation-v2",
        "status": "UNVERIFIED",
        "operational_definition": "registered measurable signal-to-language task",
        "population_scope": "to be registered",
        "sampling_plan": "to be registered",
        "instrument_calibration": "to be registered",
        "preprocessing_version": "to be registered",
        "model_version": "to be registered",
        "primary_endpoint": "to be registered",
        "evaluation_population": "to be registered",
        "blinded_holdout": True,
        "positive_controls": "required",
        "negative_controls": "required",
        "independent_replication": True,
        "counter_evidence_plan": True,
        "analysis_plan": "pre-registered",
    }
    evidence = {k: {} for k in REQUIRED_EVIDENCE}
    evidence["holdout_results"] = {"locked": False}
    evidence["replication_results"] = {"independent": False}
    evidence["calibration_metrics"] = {"evaluated": False}
    evidence["counter_evidence_review"] = {"reviewed": False}
    evidence["audit"] = {"passed": False}
    report = evaluate(protocol, evidence)
    out = ROOT / "generated" / "scientific-validation-gate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
