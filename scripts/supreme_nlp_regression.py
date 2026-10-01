#!/usr/bin/env python3
"""Deterministic Supreme NLP regression gate.

The gate measures engineering properties instead of claiming perfect accuracy.
It enforces an evidence boundary for signal-to-language translation:
observable data may be described; subjective experience is never upgraded from
a model score alone. Dependency-free so it can run in every Automission cycle.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ALLOWED_LEVELS = {"OBSERVED", "DERIVED", "INFERRED", "HYPOTHESIS", "UNVERIFIED"}
FORBIDDEN_CERTAINTY = (
    "proves the organism feels",
    "proves subjective experience",
    "scientifically verified by ai",
    "confidence proves truth",
)

def finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)

def validate_record(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("record_id", "level", "input_provenance", "observation", "uncertainty")
    for key in required:
        if key not in record:
            errors.append(f"missing:{key}")
    if record.get("level") not in ALLOWED_LEVELS:
        errors.append("invalid:level")
    if not isinstance(record.get("input_provenance"), dict):
        errors.append("invalid:input_provenance")
    if not isinstance(record.get("observation"), dict):
        errors.append("invalid:observation")
    uncertainty = record.get("uncertainty")
    if not finite_number(uncertainty) or not 0 <= uncertainty <= 1:
        errors.append("invalid:uncertainty")
    text = json.dumps(record, ensure_ascii=False).lower()
    if any(fragment in text for fragment in FORBIDDEN_CERTAINTY):
        errors.append("integrity:unsupported-certainty-language")
    level = record.get("level")
    evidence = record.get("evidence", [])
    if level in {"INFERRED", "HYPOTHESIS"} and not isinstance(evidence, list):
        errors.append("missing:evidence-list")
    if level == "INFERRED" and not evidence:
        errors.append("inferred-without-evidence")
    return errors

def evaluate(records: list[dict[str, Any]]) -> dict[str, Any]:
    results = [validate_record(r) for r in records]
    passed = sum(not errors for errors in results)
    total = len(records)
    return {
        "records": total,
        "passed": passed,
        "failed": total - passed,
        "pass_rate": round(passed / total, 6) if total else 0.0,
        "all_valid": total > 0 and passed == total,
        "errors": [{"index": i, "errors": e} for i, e in enumerate(results) if e],
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic Supreme NLP regression checks.")
    parser.add_argument("file", type=Path, help="JSON array or JSONL evaluation records")
    args = parser.parse_args()
    raw = args.file.read_text(encoding="utf-8")
    try:
        parsed = json.loads(raw)
        records = parsed if isinstance(parsed, list) else [parsed]
    except json.JSONDecodeError:
        records = [json.loads(line) for line in raw.splitlines() if line.strip()]
    if not all(isinstance(r, dict) for r in records):
        raise SystemExit("Input must contain JSON objects.")
    report = evaluate(records)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["all_valid"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
