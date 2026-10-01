"""Deterministic benchmark for the Supreme NLP evidence-preserving baseline.

This benchmark measures implementation behaviour on synthetic, labelled cases.
It is NOT a scientific validation of biological, emotional, conscious, or
subjective experience claims. Real-world accuracy requires independent labelled
datasets and domain-specific evaluation.
"""
from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any

from agents.supreme_nlp import summarize, to_simple_language, fingerprint

CASES: list[tuple[str, list[dict[str, Any]], str]] = [
    (
        "stable",
        [
            {"modality": "synthetic", "feature": "x", "value": 1.00, "quality": 1.0, "source": "a"},
            {"modality": "synthetic", "feature": "x", "value": 1.02, "quality": 1.0, "source": "b"},
            {"modality": "synthetic", "feature": "x", "value": 0.98, "quality": 1.0, "source": "c"},
            {"modality": "synthetic", "feature": "x", "value": 1.01, "quality": 1.0, "source": "d"},
        ],
        "stable_pattern",
    ),
    (
        "moderate",
        [
            {"modality": "synthetic", "feature": "x", "value": 0.60, "quality": 1.0, "source": "a"},
            {"modality": "synthetic", "feature": "x", "value": 1.00, "quality": 1.0, "source": "b"},
            {"modality": "synthetic", "feature": "x", "value": 1.40, "quality": 1.0, "source": "c"},
            {"modality": "synthetic", "feature": "x", "value": 1.00, "quality": 1.0, "source": "d"},
        ],
        "moderate_variability_pattern",
    ),
    (
        "high",
        [
            {"modality": "synthetic", "feature": "x", "value": 0.00, "quality": 1.0, "source": "a"},
            {"modality": "synthetic", "feature": "x", "value": 2.00, "quality": 1.0, "source": "b"},
            {"modality": "synthetic", "feature": "x", "value": 0.00, "quality": 1.0, "source": "c"},
            {"modality": "synthetic", "feature": "x", "value": 2.00, "quality": 1.0, "source": "d"},
        ],
        "high_variability_pattern",
    ),
]


def run() -> dict[str, Any]:
    results = []
    correct = 0
    for case_id, signals, expected in CASES:
        result = summarize(signals)
        observed = (result.get("interpretation") or {}).get("state")
        ok = observed == expected
        correct += int(ok)
        text = to_simple_language(result)
        results.append({
            "case": case_id,
            "expected": expected,
            "observed": observed,
            "correct": ok,
            "has_uncertainty_language": "प्रमाण नहीं" in text,
            "fingerprint": fingerprint(result),
        })

    accuracy = correct / len(CASES)
    uncertainty_ok = all(x["has_uncertainty_language"] for x in results)
    deterministic_ok = all(bool(x["fingerprint"]) for x in results)
    status = "PASS" if accuracy == 1.0 and uncertainty_ok and deterministic_ok else "BLOCK"
    return {
        "benchmark": "supreme-nlp-synthetic-v1",
        "status": status,
        "dataset_type": "synthetic_internal_regression",
        "cases": len(CASES),
        "classification_accuracy": round(accuracy, 4),
        "uncertainty_language_contract": uncertainty_ok,
        "deterministic_fingerprints": deterministic_ok,
        "results": results,
        "limitations": [
            "Synthetic regression accuracy is not real-world model accuracy.",
            "No biological, emotional, consciousness, or subjective-experience claim is validated by this benchmark.",
            "External labelled datasets and independent replication are required for scientific performance claims.",
        ],
    }


if __name__ == "__main__":
    out = run()
    Path("generated/supreme-nlp").mkdir(parents=True, exist_ok=True)
    Path("generated/supreme-nlp/benchmark.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))
    raise SystemExit(0 if out["status"] == "PASS" else 1)
