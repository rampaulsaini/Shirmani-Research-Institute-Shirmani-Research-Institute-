"""Deterministic, dependency-free regression benchmark for Supreme NLP."""

from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "supreme-nlp-benchmark.json"

POSITIVE = {"good","great","happy","love","excellent","श्रेष्ठ","अच्छा","प्रेम","उत्तम"}
NEGATIVE = {"bad","sad","hate","poor","danger","खराब","दुख","घृणा","खतरा"}

CASES = [
    ("en-pos-01", "great research", "positive-pattern"),
    ("en-pos-02", "excellent work", "positive-pattern"),
    ("en-neg-01", "bad result", "negative-pattern"),
    ("en-neg-02", "danger poor outcome", "negative-pattern"),
    ("en-neutral-01", "research paper", "neutral-or-uncertain"),
    ("hi-pos-01", "श्रेष्ठ प्रेम", "positive-pattern"),
    ("hi-pos-02", "अच्छा और उत्तम", "positive-pattern"),
    ("hi-neg-01", "खराब परिणाम", "negative-pattern"),
    ("hi-neg-02", "दुख और खतरा", "negative-pattern"),
    ("hi-neutral-01", "अनुसंधान प्रणाली", "neutral-or-uncertain"),
    ("mixed-pos-01", "great प्रेम", "positive-pattern"),
    ("mixed-neg-01", "bad खतरा", "negative-pattern"),
]

def infer(text: str) -> tuple[str, list[str]]:
    tokens = re.findall(r"[\w\u0900-\u097F]+", text.lower())
    pos = sorted(set(tokens) & POSITIVE)
    neg = sorted(set(tokens) & NEGATIVE)
    if len(pos) > len(neg):
        return "positive-pattern", pos
    if len(neg) > len(pos):
        return "negative-pattern", neg
    return "neutral-or-uncertain", pos + neg

def main():
    rows = []
    correct = 0
    for case_id, text, expected in CASES:
        predicted, evidence = infer(text)
        ok = predicted == expected
        correct += int(ok)
        rows.append({
            "id": case_id,
            "expected": expected,
            "predicted": predicted,
            "evidence": evidence,
            "correct": ok,
            "verification_state": "UNVERIFIED",
        })

    record = {
        "benchmark_id": "supreme-nlp-reference-v1",
        "task": "lexical-pattern-detection",
        "population_scope": "fixed multilingual regression fixture",
        "dataset_fingerprint": "fixture-embedded-v1",
        "model": {"name": "deterministic-baseline-nlp", "version": "0.2"},
        "metric": "accuracy",
        "result": correct / len(CASES),
        "sample_count": len(CASES),
        "correct_count": correct,
        "verification_state": "UNVERIFIED",
        "provenance": ["embedded benchmark fixture", "factory/supreme_nlp_benchmark.py"],
        "limitations": [
            "tiny fixed fixture",
            "lexical baseline only",
            "not representative of general language understanding",
            "not evidence of subjective feeling, consciousness or intention",
        ],
        "cases": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=False, indent=2))
    if correct != len(CASES):
        raise SystemExit("Reference NLP regression benchmark failed")

if __name__ == "__main__":
    main()
