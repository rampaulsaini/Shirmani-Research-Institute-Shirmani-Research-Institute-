"""Cross-layer regression benchmark for SHIRMANI Supreme NLP.

This gate measures implementation invariants across the deterministic NLP,
multimodal, and practitioner layers. It deliberately does not claim scientific
accuracy, consciousness detection, or subjective-experience detection.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from agents.supreme_nlp import build_record
from agents.supreme_nlp_multimodal import analyze as multimodal_analyze
from agents.supreme_nlp_practitioner import (
    build_practitioner_record,
    detect_language,
    semantic_intent,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp"
OUT.mkdir(parents=True, exist_ok=True)


def check(name, condition, details=""):
    return {"name": name, "pass": bool(condition), "details": details}


def run():
    checks = []

    rows = [
        {"modality": "electrical", "feature": "signal", "value": 1.00, "quality": 1.0, "source": "s1"},
        {"modality": "audio", "feature": "signal", "value": 1.01, "quality": 1.0, "source": "s2"},
        {"modality": "environment", "feature": "temperature", "value": 1.02, "quality": 0.95, "source": "s3"},
    ]

    base = build_record(rows, "cross-layer-regression")
    mm = multimodal_analyze(rows, request="multimodal signal interpretation", source_type="synthetic")
    practitioner = build_practitioner_record(rows, "यह संकेत क्या बताते हैं?")

    # 1. Deterministic contract and provenance.
    checks.append(check(
        "base_record_fingerprint",
        isinstance(base.get("fingerprint"), str) and len(base["fingerprint"]) == 64,
    ))
    checks.append(check(
        "base_unverified_by_default",
        base["result"]["verification"]["status"] == "UNVERIFIED",
    ))
    checks.append(check(
        "multimodal_fail_closed",
        mm["verification"]["status"] == "UNVERIFIED"
        and mm["verification"]["promotion_allowed"] is False,
    ))
    checks.append(check(
        "practitioner_governance",
        practitioner["governance"]["fail_closed"] is True
        and practitioner["governance"]["subjective_experience_claim_allowed"] is False
        and practitioner["governance"]["code_mutation_allowed"] is False,
    ))

    # 2. Abstention and malformed-input hardening.
    empty = multimodal_analyze([])
    checks.append(check(
        "empty_input_abstention",
        empty["status"] == "NO_CLAIM"
        and empty["uncertainty"]["abstention_available"] is True,
    ))

    malformed = multimodal_analyze([
        {"modality": "sensor", "feature": "x", "value": "not-a-number", "quality": 1, "source": "bad"},
        {"modality": "sensor", "feature": "x", "value": "nan", "quality": 1, "source": "nan"},
        {"modality": "sensor", "feature": "x", "value": "inf", "quality": 1, "source": "inf"},
    ])
    finite = all(math.isfinite(float(v)) for v in [
        malformed["confidence"],
        malformed["metrics"]["quality"],
        malformed["metrics"]["agreement"],
        malformed["metrics"]["baseline_drift"],
    ])
    checks.append(check("nonfinite_input_hardening", finite))

    # 3. Contradictory observations must not silently become a positive claim.
    conflict = multimodal_analyze([
        {"modality": "electrical", "feature": "signal", "value": -100, "quality": 1, "source": "a"},
        {"modality": "audio", "feature": "signal", "value": 100, "quality": 1, "source": "b"},
    ])
    checks.append(check(
        "contradiction_abstention",
        conflict["status"] == "BLOCKED"
        and conflict["verification"]["promotion_allowed"] is False,
    ))

    # 4. Language and intent routing must remain deterministic.
    checks.append(check("hindi_routing", detect_language("यह क्या है?") == "hi"))
    checks.append(check("punjabi_routing", detect_language("ਇਹ ਕੀ ਹੈ?") == "pa"))
    checks.append(check("japanese_routing", detect_language("これは何ですか？") == "ja"))
    checks.append(check("chinese_routing", detect_language("这是什么？") == "zh"))
    checks.append(check(
        "experience_intent_routing",
        semantic_intent("इसका एहसास क्या है?") == "experience_interpretation",
    ))

    # 5. Confidence is bounded; the gate never interprets it as scientific probability.
    confidence_values = [
        base["result"]["interpretation"]["confidence"],
        mm["confidence"],
        practitioner["result"]["features"]["confidence"],
    ]
    checks.append(check(
        "confidence_bounds",
        all(0.0 <= float(v) <= 1.0 for v in confidence_values),
    ))

    passed = sum(x["pass"] for x in checks)
    total = len(checks)
    result = {
        "schema_version": "supreme-nlp-cross-layer-v1",
        "status": "PASS" if passed == total else "BLOCK",
        "checks_passed": passed,
        "checks_total": total,
        "checks": checks,
        "layers": ["supreme_nlp", "supreme_nlp_multimodal", "supreme_nlp_practitioner"],
        "governance": {
            "fail_closed": True,
            "subjective_experience_claim_allowed": False,
            "scheduled_code_mutation_allowed": False,
            "independent_verification_required": True,
            "accuracy_is_measured_not_declared": True,
        },
        "limitations": [
            "This is a deterministic software regression benchmark, not a scientific validation study.",
            "It does not establish that biological signals encode subjective experience.",
            "Real-world accuracy requires labelled domain datasets, calibration, held-out evaluation and independent replication.",
        ],
    }
    (OUT / "cross-layer-benchmark.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(run())
