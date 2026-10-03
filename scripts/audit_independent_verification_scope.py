#!/usr/bin/env python3
"""Fail-closed scope-integrity audit for independent verification artifacts.

This audit prevents a stale or mismatched QC report from being treated as
evidence for a different queue scope. It does not promote any record to
VERIFIED.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
QUEUE = OUT / "independent-verification-queue.jsonl"
REGISTRY = OUT / "independent-verification-registry.jsonl"
SOURCE = OUT / "independent-verification-records.json"
QUEUE_QC = OUT / "VERIFICATION-QUEUE-QC.json"
PROMOTION_QC = OUT / "VERIFICATION-PROMOTION-QC.json"
REPORT = OUT / "INDEPENDENT-VERIFICATION-SCOPE-INTEGRITY.json"

def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None

def main() -> None:
    queue_count = count_jsonl(QUEUE)
    registry_count = count_jsonl(REGISTRY)
    source = load(SOURCE) or {}
    source_count = len(source.get("records", []))
    queue_qc = load(QUEUE_QC) or {}
    promotion_qc = load(PROMOTION_QC) or {}

    checks = {
        "queue_matches_authoritative_source": queue_count == source_count,
        "registry_matches_queue": registry_count == queue_count,
        "queue_qc_matches_actual_queue": queue_qc.get("records") == queue_count,
        "promotion_qc_matches_actual_registry": promotion_qc.get("records") == registry_count,
        "promotion_qc_queue_matches_actual_queue": promotion_qc.get("queue_records") == queue_count,
    }
    errors = [
        {"check": name, "actual_queue": queue_count, "actual_registry": registry_count,
         "source_records": source_count, "queue_qc_records": queue_qc.get("records"),
         "promotion_qc_records": promotion_qc.get("records"),
         "promotion_qc_queue_records": promotion_qc.get("queue_records")}
        for name, ok in checks.items() if not ok
    ]
    report = {
        "schema_version": "1.0.0",
        "queue_records_actual": queue_count,
        "authoritative_source_records": source_count,
        "review_registry_records_actual": registry_count,
        "queue_qc_records_reported": queue_qc.get("records"),
        "queue_qc_claim_records_reported": queue_qc.get("claim_records"),
        "promotion_qc_records_reported": promotion_qc.get("records"),
        "promotion_qc_queue_records_reported": promotion_qc.get("queue_records"),
        "checks": checks,
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "policy": "A QC result for one queue scope must never be accepted as evidence for another scope.",
        "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
