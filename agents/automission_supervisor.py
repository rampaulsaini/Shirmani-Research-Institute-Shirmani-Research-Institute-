"""Deterministic Automission supervisor for continuous quality improvement.

This supervisor proposes bounded actions. It never self-authorizes code mutation,
publication, deployment, scientific verification, or irreversible action.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone


def inspect(status_path="generated/supreme-nlp/status.json"):
    p = Path(status_path)
    if not p.exists():
        return {
            "schema_version": "1.1",
            "state": "NO_STATUS",
            "severity": "HIGH",
            "actions": ["generate a status record"],
            "gates": {"publication": "BLOCKED", "code_mutation": "DISABLED"},
        }

    d = json.loads(p.read_text(encoding="utf-8"))
    r = d.get("result", {})
    f = r.get("features", {})
    q = r.get("quality_diagnostics", {})
    u = d.get("uncertainty", {})
    actions = []

    if r.get("status") != "interpreted":
        actions.append("collect higher-quality signals")
    if f.get("evidence_grade") in {"C", "D"}:
        actions.append("increase evidence quality and independent validation")
    if f.get("agreement", 1) < .5:
        actions.append("investigate cross-signal disagreement")
    if f.get("modalities", 0) < 2:
        actions.append("add an independent modality where scientifically appropriate")
    if q.get("dropped_count", 0) > 0:
        actions.append("inspect and quarantine rejected inputs")
    if not u.get("confidence_is_calibrated", False):
        actions.append("calibrate confidence against a held-out labelled validation set")
    if u.get("independent_verification") != "VERIFIED":
        actions.append("keep scientific verification state separate and NOT_VERIFIED")

    if not actions:
        actions.append("continue scheduled monitoring and regression tests")

    return {
        "schema_version": "1.1",
        "state": "IMPROVEMENT_REQUIRED" if len(actions) > 1 else "MONITOR",
        "severity": "HIGH" if r.get("status") != "interpreted" else "MEDIUM" if len(actions) > 2 else "LOW",
        "actions": actions,
        "source_fingerprint": d.get("fingerprint"),
        "gates": {
            "publication": "BLOCKED" if u.get("independent_verification") != "VERIFIED" else "REVIEW_REQUIRED",
            "code_mutation": "DISABLED",
            "deployment": "HUMAN_APPROVAL_REQUIRED",
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    out = inspect()
    Path("generated/supreme-nlp").mkdir(parents=True, exist_ok=True)
    Path("generated/supreme-nlp/automission-plan.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))
