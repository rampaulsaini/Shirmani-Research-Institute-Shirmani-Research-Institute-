"""Deterministic Automission supervisor for continuous quality improvement.

The supervisor is intentionally fail-closed: it diagnoses missing/weak evidence and
creates improvement actions, but it never promotes an interpretation to proof and
never mutates production code from a scheduled audit.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _load(path: str) -> dict[str, Any] | None:
    p = Path(path)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def inspect(status_path="generated/supreme-nlp/status.json"):
    d = _load(status_path)
    if d is None:
        return {
            "state": "NO_STATUS",
            "actions": [
                "generate a status record",
                "do not promote or publish an unverified interpretation",
            ],
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    r = d.get("result") or {}
    f = r.get("features") or {}
    i = r.get("interpretation") or {}
    actions: list[str] = []

    if r.get("status") != "interpreted":
        actions.append("collect higher-quality signals before interpretation")
    if f.get("evidence_grade") in {"C", "D"}:
        actions.append("increase evidence quality and independent validation")
    if f.get("agreement", 1) < 0.70:
        actions.append("investigate cross-signal disagreement")
    if f.get("modalities", 0) < 2:
        actions.append("add an independent modality where scientifically appropriate")
    if f.get("independent_sources", 0) < 2:
        actions.append("obtain an independent source or replication")
    if f.get("sample_count", 0) < 10:
        actions.append("increase sample count before making a stronger claim")
    if f.get("drift_score", 0) > 0.30:
        actions.append("run drift investigation and compare against the registered baseline")
    if i.get("confidence", 0) < 0.70 and r.get("status") == "interpreted":
        actions.append("calibrate confidence against labelled evaluation data")
    if not i.get("limitations"):
        actions.append("attach explicit limitations and provenance")
    if not actions:
        actions.append("continue scheduled monitoring and regression tests")

    return {
        "state": "IMPROVEMENT_REQUIRED" if len(actions) > 1 else "MONITOR",
        "actions": actions,
        "source_fingerprint": d.get("fingerprint"),
        "evidence_grade": f.get("evidence_grade"),
        "confidence": i.get("confidence"),
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "scheduled_code_mutation_allowed": False,
            "independent_verification_required": True,
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    out = inspect()
    Path("generated/supreme-nlp").mkdir(parents=True, exist_ok=True)
    Path("generated/supreme-nlp/automission-plan.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(out)
