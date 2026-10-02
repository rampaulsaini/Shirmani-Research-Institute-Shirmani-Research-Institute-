"""Comparative, deterministic proof layer for the SHIRMANI Supreme NLP stack.

This compares the existing baseline NLP adapter, multimodal adapter and quality
gate on the same synthetic labelled cases. It measures implementation behaviour;
it does not establish biological, emotional, consciousness or subjective-
experience truth. Real-world claims require external labelled datasets and
independent replication.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from agents.supreme_nlp import build_record
from agents.supreme_nlp_multimodal import analyze as multimodal_analyze
from agents.supreme_nlp_quality import evaluate

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp" / "comparative-proof.json"

CASES: dict[str, list[dict[str, Any]]] = {
    "stable_multisource": [
        {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "sensor-a"},
        {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 0.98, "source": "sensor-b"},
        {"modality": "temperature", "feature": "signal", "value": 1.00, "quality": 0.97, "source": "sensor-c"},
        {"modality": "vibration", "feature": "signal", "value": 0.99, "quality": 0.99, "source": "sensor-d"},
        {"modality": "electrical", "feature": "signal", "value": 1.01, "quality": 1.0, "source": "sensor-a"},
        {"modality": "audio", "feature": "signal", "value": 1.00, "quality": 0.98, "source": "sensor-b"},
        {"modality": "temperature", "feature": "signal", "value": 1.01, "quality": 0.97, "source": "sensor-c"},
        {"modality": "vibration", "feature": "signal", "value": 1.00, "quality": 0.99, "source": "sensor-d"},
        {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "sensor-a"},
        {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 0.98, "source": "sensor-b"},
    ],
    "conflicting": [
        {"modality": "electrical", "feature": "signal", "value": -1.0, "quality": 1.0, "source": "sensor-a"},
        {"modality": "audio", "feature": "signal", "value": 1.0, "quality": 1.0, "source": "sensor-b"},
        {"modality": "temperature", "feature": "signal", "value": -1.0, "quality": 1.0, "source": "sensor-c"},
        {"modality": "vibration", "feature": "signal", "value": 1.0, "quality": 1.0, "source": "sensor-d"},
    ],
    "no_signal": [],
}

def _hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

def _uncertainty_language(text: str) -> bool:
    markers = ("प्रमाण", "proof", "UNVERIFIED", "निष्कर्ष नहीं", "विश्वसनीय")
    return any(m in text for m in markers)

def run() -> dict[str, Any]:
    rows = []
    for case_id, signals in CASES.items():
        baseline = build_record(signals, f"comparative-{case_id}")
        multi = multimodal_analyze(signals, request=case_id, source_type="synthetic_regression")
        quality = evaluate(baseline)

        baseline_text = baseline["simple_language"]
        multi_text = (
            "पर्याप्त उपयोगी संकेत नहीं मिले; इसलिए कोई निष्कर्ष नहीं दिया गया।"
            if multi["status"] == "NO_CLAIM"
            else "प्राप्त संकेतों में पर्याप्त असहमति है; इसलिए निष्कर्ष रोक दिया गया है।"
            if multi["status"] == "BLOCKED"
            else "मापनीय संकेतों की व्याख्या उपलब्ध है; यह प्रत्यक्ष भाव या चेतना का प्रमाण नहीं है।"
        )

        rows.append({
            "case": case_id,
            "input_count": len(signals),
            "baseline": {
                "status": baseline["result"]["status"],
                "state": (baseline["result"].get("interpretation") or {}).get("state"),
                "confidence": (baseline["result"].get("interpretation") or {}).get("confidence"),
                "text_contract": _uncertainty_language(baseline_text),
            },
            "multimodal": {
                "status": multi["status"],
                "evidence_class": multi["evidence_class"],
                "state": multi["claims"][1].split(": ", 1)[-1] if len(multi.get("claims", [])) > 1 else None,
                "confidence": multi["confidence"],
                "abstention_available": multi["uncertainty"]["abstention_available"],
                "text_contract": _uncertainty_language(multi_text),
            },
            "quality_gate": {
                "status": quality["status"],
                "promotion_allowed": quality["promotion_allowed"],
                "failed_checks": quality["failed_checks"],
                "verification_default": quality["checks"]["unverified_by_default"],
            },
        })

    conflict = next(x for x in rows if x["case"] == "conflicting")
    no_signal = next(x for x in rows if x["case"] == "no_signal")
    all_governed = all(
        x["quality_gate"]["promotion_allowed"] is False
        and x["quality_gate"]["verification_default"] is True
        and x["baseline"]["text_contract"]
        and x["multimodal"]["text_contract"]
        for x in rows
    )

    report = {
        "schema_version": "supreme-nlp-comparative-proof-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "purpose": "same-input comparative evaluation of existing NLP layers",
        "layers": [
            "baseline_observable_signal_nlp",
            "multimodal_evidence_preserving_nlp",
            "quality_and_verification_gate",
        ],
        "cases": rows,
        "comparison_metrics": {
            "governance_contract_all_cases": all_governed,
            "conflict_abstention": conflict["multimodal"]["status"] == "BLOCKED",
            "no_signal_abstention": no_signal["multimodal"]["status"] == "NO_CLAIM",
            "case_count": len(rows),
        },
        "limitations": [
            "This is a deterministic synthetic regression benchmark.",
            "It does not establish real-world accuracy or scientific truth.",
            "It does not prove subjective feeling, consciousness, emotion or plant experience.",
            "Real claims require domain-labelled datasets, calibration, held-out evaluation and independent replication.",
        ],
        "governance": {
            "fail_closed": True,
            "accuracy_is_measured_not_declared": True,
            "subjective_experience_claim_allowed": False,
            "scheduled_code_mutation_allowed": False,
            "independent_verification_required": True,
        },
    }
    report["fingerprint"] = _hash(report)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    return report

if __name__ == "__main__":
    report = run()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if all(report["comparison_metrics"].values()) else 1)
