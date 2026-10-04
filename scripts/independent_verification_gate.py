#!/usr/bin/env python3
"""Fail-closed independent verification gate.

This tool never decides whether a claim is true. It enforces the evidence,
provenance, reproducibility and reviewer requirements before an independent
review decision may promote a record to an independent-verification state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

REQUIRED_VERIFICATION_FIELDS = (
    "operational_definition",
    "independent_sources",
    "test_or_observation",
    "counter_evidence_review",
    "result",
    "reviewer",
    "reviewed_at",
    "decision",
)
VERIFIED_STATES = {"VERIFIED", "INDEPENDENTLY_VERIFIED"}
ALLOWED_DECISIONS = {"VERIFIED", "NOT_VERIFIED", "CONTRADICTED", "INCONCLUSIVE"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"VERIFICATION_GATE_FAIL: {message}")


def validate_record(record: dict[str, Any]) -> None:
    rid = record.get("id")
    status = str(record.get("status", "")).upper()
    if not rid:
        fail("record missing id")
    if status in VERIFIED_STATES:
        missing = [k for k in REQUIRED_VERIFICATION_FIELDS if not record.get(k)]
        if missing:
            fail(f"{rid}: independent verification record missing {', '.join(missing)}")
        reviewer = record["reviewer"]
        if not isinstance(reviewer, dict) or not reviewer.get("identity") or not reviewer.get("role"):
            fail(f"{rid}: reviewer identity and role are required")
        sources = record.get("independent_sources")
        if not isinstance(sources, list) or not sources:
            fail(f"{rid}: at least one independent source is required")
        if record.get("decision") not in ALLOWED_DECISIONS:
            fail(f"{rid}: invalid decision")
        if record.get("decision") != "VERIFIED":
            fail(f"{rid}: independent verification state requires decision VERIFIED")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    args = ap.parse_args()

    path = Path(args.registry)
    data = json.loads(path.read_text(encoding="utf-8"))
    summary = data["verification_summary"]
    records = data["records"]

    if summary["queue_records"] != len(records):
        fail("queue_records does not equal registry length")

    verified = [r for r in records if str(r.get("status", "")).upper() in VERIFIED_STATES]
    evidence = [r for r in records if str(r.get("status", "")).upper() == "EVIDENCE-SUPPORTED"]

    if summary["independently_verified_records"] != len(verified):
        fail("independently_verified_records does not equal independent-verification states")
    expected_pct = round((len(verified) / len(records)) * 100, 6) if records else 0
    if summary["independent_verified_percent"] != expected_pct:
        fail("independent_verified_percent is inconsistent with records")
    if summary["evidence_supported_records"] != len(evidence):
        fail("evidence_supported_records is inconsistent with registry")

    ids = [r.get("id") for r in records]
    if len(ids) != len(set(ids)):
        fail("duplicate record id")

    for record in records:
        validate_record(record)

    print("Independent verification gate: PASS")
    print(
        f"queue={len(records)} evidence_supported={len(evidence)} "
        f"independently_verified={len(verified)}"
    )
    print(f"accepted_verified_states={sorted(VERIFIED_STATES)}")
    print(f"registry_sha256={sha256_file(path)}")
    print("No workflow success is treated as independent verification.")


if __name__ == "__main__":
    main()
