#!/usr/bin/env python3
"""Evidence-first multimodal observation -> plain-language NLP layer.

This module does NOT claim to detect subjective feelings from raw signals.
It converts explicitly measured observations into simple language and keeps
observations, hypotheses and uncertainty separate.

The design is intentionally model-agnostic: future ML/NLP models can plug into
this contract without changing the evidence boundary.
"""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "nlp-observation.schema.json"

SUBJECT_LABELS = {
    "human": "मानव",
    "animal": "जीव",
    "plant": "वनस्पति",
    "nonliving_system": "निर्जीव प्रणाली",
    "environmental_system": "पर्यावरणीय प्रणाली",
    "unknown": "अज्ञात प्रणाली",
}

def finite_number(value):
    return isinstance(value, (int, float)) and math.isfinite(value)

def validate(record):
    errors = []
    required = ("observation_id", "subject_type", "observations", "interpretation_policy")
    for key in required:
        if key not in record:
            errors.append(f"missing:{key}")
    if record.get("subject_type") not in SUBJECT_LABELS:
        errors.append("invalid:subject_type")
    observations = record.get("observations")
    if not isinstance(observations, list) or not observations:
        errors.append("invalid:observations")
    else:
        for i, item in enumerate(observations):
            for key in ("channel", "value", "unit", "timestamp"):
                if key not in item:
                    errors.append(f"observation[{i}]:missing:{key}")
    policy = record.get("interpretation_policy")
    if not isinstance(policy, dict):
        errors.append("invalid:interpretation_policy")
    elif policy.get("measured_vs_inferred") is not True:
        errors.append("policy:measured_vs_inferred_must_be_true")
    elif policy.get("abstain_on_missing_evidence") is not True:
        errors.append("policy:abstain_on_missing_evidence_must_be_true")
    return errors

def translate(record):
    errors = validate(record)
    if errors:
        return {"status":"BLOCK", "errors":errors}
    subject = SUBJECT_LABELS[record["subject_type"]]
    observations = record["observations"]
    lines = [f"{subject} के बारे में {len(observations)} मापे गए संकेत उपलब्ध हैं।"]
    for item in observations:
        value = item["value"]
        if finite_number(value):
            value_text = f"{value:g}"
        else:
            value_text = str(value)
        lines.append(f"- {item['channel']}: {value_text} {item['unit']} ({item['timestamp']})")
    lines.append("इन मापों से केवल दर्ज संकेतों का वर्णन किया गया है; किसी व्यक्तिपरक भाव/चेतना का निष्कर्ष स्वतः नहीं निकाला गया है।")
    lines.append("यदि किसी भाव-अवस्था की वैज्ञानिक व्याख्या करनी हो, तो स्वतंत्र रूप से परिभाषित संकेत, तुलना-समूह, परीक्षण-विधि और प्रतिकूल/वैकल्पिक व्याख्याओं की आवश्यकता होगी।")
    return {
        "status":"PASS",
        "observation_id":record["observation_id"],
        "subject_type":record["subject_type"],
        "plain_language":"\n".join(lines),
        "inference_status":"NOT_ESTABLISHED",
        "confidence":"NOT_SCORED_WITHOUT_VALIDATION_DATA",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "safety_rule":"measured_signal != subjective_feeling",
    }

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: supreme_nlp.py INPUT.json OUTPUT.json")
    inp, out = map(Path, sys.argv[1:3])
    record = json.loads(inp.read_text(encoding="utf-8"))
    result = translate(record)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if result["status"] == "BLOCK":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
