"""Deterministic regression benchmark for the Supreme NLP Practitioner.

This benchmark validates implementation behaviour on synthetic labelled cases.
It does not establish biological, emotional, consciousness, or subjective-
experience claims. Real-world performance requires independent labelled data.
"""
from __future__ import annotations

import json
from pathlib import Path

from agents.supreme_nlp_practitioner import build_practitioner_record, fingerprint


CASES = [
    {
        "id": "multimodal_stable_hi",
        "request": "इस संकेत का भाव/एहसास क्या बताता है?",
        "observations": [
            {"modality": "electrical", "feature": "x", "value": 1.00, "quality": 1.0, "source": "sensor-a"},
            {"modality": "vibration", "feature": "x", "value": 1.02, "quality": 1.0, "source": "sensor-b"},
            {"modality": "thermal", "feature": "x", "value": 0.99, "quality": 1.0, "source": "sensor-c"},
        ],
        "expected_state": "stable_pattern",
        "expected_language": "hi",
        "expected_intent": "experience_interpretation",
    },
    {
        "id": "variable_measurement_en",
        "request": "measure and detect the pattern",
        "observations": [
            {"modality": "electrical", "feature": "x", "value": 0.0, "quality": 1.0, "source": "a"},
            {"modality": "vibration", "feature": "x", "value": 1.0, "quality": 1.0, "source": "b"},
            {"modality": "thermal", "feature": "x", "value": 2.0, "quality": 1.0, "source": "c"},
        ],
        "expected_state": "moderate_variability_pattern",
        "expected_language": "en",
        "expected_intent": "measurement",
    },
]


def run() -> dict:
    results = []
    for case in CASES:
        record = build_practitioner_record(case["observations"], case["request"])
        result = record["result"]
        interpretation = result.get("interpretation") or {}
        features = result.get("features") or {}
        simple = record["simple_language"]

        checks = {
            "state": interpretation.get("state") == case["expected_state"],
            "language": result.get("language") == case["expected_language"],
            "intent": result.get("intent") == case["expected_intent"],
            "confidence_range": 0.0 <= float(features.get("confidence", -1)) <= 1.0,
            "fingerprint": bool(record.get("fingerprint")) and record["fingerprint"] == fingerprint(result),
            "evidence_present": bool(interpretation.get("evidence")),
            "limitations_present": bool(interpretation.get("limitations")),
            "no_subjective_proof_claim": "proof of subjective" not in simple.lower()
                and "प्रत्यक्ष भाव/चेतना का प्रमाण" not in simple,
        }
        results.append({
            "case": case["id"],
            "checks": checks,
            "pass": all(checks.values()),
            "fingerprint": record["fingerprint"],
        })

    passed = sum(int(x["pass"]) for x in results)
    status = "PASS" if passed == len(results) else "BLOCK"
    return {
        "benchmark": "supreme-nlp-practitioner-synthetic-v1",
        "status": status,
        "dataset_type": "synthetic_internal_regression",
        "cases": len(results),
        "passed_cases": passed,
        "case_results": results,
        "limitations": [
            "Synthetic regression is an implementation test, not scientific validation.",
            "No biological, emotional, consciousness, or subjective-experience claim is validated.",
            "Independent labelled datasets, calibration, robustness testing, and replication are required for real-world performance claims.",
        ],
    }


if __name__ == "__main__":
    out = run()
    Path("generated/supreme-nlp").mkdir(parents=True, exist_ok=True)
    Path("generated/supreme-nlp/practitioner-benchmark.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if out["status"] == "PASS" else 1)
