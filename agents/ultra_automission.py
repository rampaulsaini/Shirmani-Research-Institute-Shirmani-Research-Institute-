"""Continuous, fail-closed Automission controller."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ARCHITECTURE = "ULTRA-MEGA-INFINITY-QUANTUM-AI-ML-NLP-AUTOMISSION"


def _read_json(path: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def build_plan(
    nlp_status_path="generated/supreme-nlp/status.json",
    verification_path="generated/VERIFICATION-PROMOTION-QC.json",
):
    nlp = _read_json(nlp_status_path)
    verification = _read_json(verification_path)
    summary = nlp.get("summary") or {}
    confidence = float(nlp.get("confidence", 0) or 0)
    actions = []

    if not nlp:
        actions.append({"priority": "P0", "task": "initialize_multimodal_nlp_status"})
    if summary.get("sample_count", 0) < 20:
        actions.append({"priority": "P1", "task": "increase_observable_signal_samples"})
    if summary.get("independent_sources", 0) < 2:
        actions.append({"priority": "P1", "task": "add_independent_signal_source"})
    if summary.get("modalities", 0) < 2:
        actions.append({"priority": "P1", "task": "add_independent_modality"})
    if confidence < 0.70:
        actions.append({"priority": "P1", "task": "calibrate_nlp_confidence_on_labelled_data"})
    if not (nlp.get("calibration") or {}).get("validated", False):
        actions.append({"priority": "P1", "task": "run_labelled_calibration_benchmark"})
    if verification.get("publication_gate") != "PASS":
        actions.append({"priority": "P0", "task": "retain_fail_closed_verification_gate"})
    actions.append({"priority": "P2", "task": "run_regression_and_security_qc"})

    return {
        "architecture": ARCHITECTURE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "continuous-resumable-fail-closed",
        "actions": actions,
        "quality": {
            "confidence_source": "nlp.confidence",
            "promotion_requires_independent_verification": True,
            "calibration_required_before_high_confidence_claims": True,
        },
        "governance": {
            "verification_promotion": "independent_verification_required",
            "scheduled_source_mutation": False,
            "external_actions": "owner_authorization_required",
            "secrets_in_source": False,
        },
    }


def write_plan(path="generated/supreme-nlp/automission-plan.json"):
    plan = build_plan()
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return plan


if __name__ == "__main__":
    print(json.dumps(write_plan(), ensure_ascii=False, indent=2))
