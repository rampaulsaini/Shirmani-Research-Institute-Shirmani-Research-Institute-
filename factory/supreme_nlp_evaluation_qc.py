#!/usr/bin/env python3
"""Fail-closed structural QC for Supreme NLP evaluation records.

This validates evaluation evidence; it does not manufacture model metrics.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "docs" / "supreme-nlp-evaluation-contract.md"
BENCHMARK = ROOT / "generated" / "supreme-nlp-benchmark-records.jsonl"

REQUIRED = (
    "benchmark_id",
    "dataset_id",
    "dataset_fingerprint",
    "model_id",
    "model_version",
    "task",
    "language",
    "sample_count",
    "metrics",
    "provenance",
    "timestamp",
)

def main():
    if not CONFIG.exists():
        raise SystemExit("Missing Supreme NLP evaluation contract")

    if not BENCHMARK.exists():
        # Architecture readiness is valid, but measured performance is not asserted.
        print("SUPREME NLP EVALUATION: NO MEASURED BENCHMARK RECORDS")
        return

    errors = []
    records = 0
    seen = set()

    for line_no, line in enumerate(BENCHMARK.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        records += 1
        try:
            r = json.loads(line)
        except Exception as exc:
            errors.append((line_no, f"invalid_json:{exc}"))
            continue

        missing = [k for k in REQUIRED if k not in r]
        errors.extend((line_no, f"missing:{k}") for k in missing)

        bid = r.get("benchmark_id")
        if bid in seen:
            errors.append((line_no, "duplicate_benchmark_id"))
        if bid:
            seen.add(bid)

        if not isinstance(r.get("sample_count"), int) or r.get("sample_count", 0) <= 0:
            errors.append((line_no, "invalid_sample_count"))

        if not isinstance(r.get("metrics"), dict) or not r.get("metrics"):
            errors.append((line_no, "missing_metrics"))

        provenance = r.get("provenance")
        if not isinstance(provenance, dict) or not provenance.get("source"):
            errors.append((line_no, "missing_provenance"))

        if r.get("status") == "VERIFIED" and r.get("independent_verification") is not True:
            errors.append((line_no, "unearned_verified_status"))

    report = {
        "version": 1,
        "records": records,
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "measured_accuracy_claim": False if not records else "records_present",
        "errors": [{"line": n, "error": e} for n, e in errors],
    }
    out = ROOT / "generated" / "SUPREME-NLP-EVALUATION-QC.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if errors:
        raise SystemExit(json.dumps(report, ensure_ascii=False))

    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
