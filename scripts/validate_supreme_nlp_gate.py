"""Fail-closed gate for generated Supreme NLP records.

This gate checks the executable governance contract without requiring third-party
schema libraries. It is intentionally stricter than syntax-only JSON validation.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

STATUS = Path("generated/supreme-nlp/status.json")
PLAN = Path("generated/supreme-nlp/automission-plan.json")


def fail(message: str) -> None:
    raise SystemExit(f"SUPREME_NLP_GATE_FAIL: {message}")


def main() -> None:
    if not STATUS.exists():
        fail("status record is missing")
    if not PLAN.exists():
        fail("automission plan is missing")

    status = json.loads(STATUS.read_text(encoding="utf-8"))
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    result = status.get("result") or {}
    verification = result.get("verification") or {}
    interpretation = result.get("interpretation") or {}
    provenance = status.get("provenance") or {}
    governance = plan.get("governance") or {}

    required = {
        "schema_version", "task_id", "generated_at", "pipeline",
        "result", "simple_language", "fingerprint", "provenance",
    }
    missing = sorted(required - status.keys())
    if missing:
        fail(f"missing top-level fields: {missing}")

    if status["schema_version"] != "supreme-nlp-v2":
        fail("unexpected schema version")
    if not isinstance(status["task_id"], str) or not status["task_id"]:
        fail("task_id must be non-empty")
    if not isinstance(status["simple_language"], str) or not status["simple_language"]:
        fail("simple_language must be non-empty")
    if not isinstance(status["fingerprint"], str) or len(status["fingerprint"]) != 64:
        fail("fingerprint must be a 64-character SHA-256 hex digest")

    canonical = json.dumps(result, sort_keys=True, ensure_ascii=False).encode("utf-8")
    expected = hashlib.sha256(canonical).hexdigest()
    if status["fingerprint"] != expected:
        fail("fingerprint does not match canonical result")

    if result.get("status") not in {"no_data", "insufficient_quality", "interpreted"}:
        fail("invalid result status")

    if result.get("status") == "interpreted":
        confidence = interpretation.get("confidence")
        if not isinstance(confidence, (int, float)) or not math.isfinite(confidence) or not 0 <= confidence <= 1:
            fail("confidence must be finite and within [0,1]")
        if interpretation.get("confidence_status") != "UNCALIBRATED":
            fail("confidence must remain explicitly UNCALIBRATED until calibrated")
        if verification.get("status") != "UNVERIFIED":
            fail("interpreted records must remain UNVERIFIED")
        if verification.get("independent_required") is not True:
            fail("independent verification requirement was weakened")
        if verification.get("replication_required") is not True:
            fail("replication requirement was weakened")

    if provenance.get("verification_status") != "UNVERIFIED":
        fail("provenance verification status was promoted")
    if governance.get("fail_closed") is not True:
        fail("Automission governance is not fail-closed")
    if governance.get("independent_verification_required") is not True:
        fail("Automission does not require independent verification")
    if governance.get("subjective_experience_claim_allowed") is not False:
        fail("subjective-experience claim boundary was weakened")
    if governance.get("scheduled_code_mutation_allowed") is not False:
        fail("scheduled code mutation boundary was weakened")
    if governance.get("accuracy_is_measured_not_declared") is not True:
        fail("accuracy governance contract was weakened")

    print("SUPREME_NLP_FAIL_CLOSED_GATE=PASS")


if __name__ == "__main__":
    main()
