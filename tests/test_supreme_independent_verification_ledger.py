#!/usr/bin/env python3
"""Regression tests for the fail-closed independent verification ledger."""

import json
import tempfile
from pathlib import Path

from factory.supreme_independent_verification_ledger import (
    STATES,
    REQUIRED,
    scan_records,
    validate_record,
)


SCHEMA = {
    "required": REQUIRED,
    "properties": {
        "verification_state": {"enum": sorted(STATES)}
    },
}


def record(record_id, state="UNVERIFIED", **overrides):
    value = {
        "record_id": record_id,
        "source_record_id": "source-1",
        "claim_or_result": "bounded test claim",
        "verification_scope": "test scope",
        "evidence_refs": ["evidence-1"],
        "independent_verifier": "reviewer-1",
        "verification_method": "document review",
        "reviewed_at": "2026-10-05T00:00:00Z",
        "verification_state": state,
        "limitations": ["test-only"],
    }
    value.update(overrides)
    return value


def test_duplicate_record_ids_block():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.json").write_text(json.dumps(record("same")), encoding="utf-8")
        (root / "b.json").write_text(json.dumps(record("same")), encoding="utf-8")
        counts, blockers, seen = scan_records(root, SCHEMA)
        assert seen == 2
        assert counts["UNVERIFIED"] == 2
        assert any("duplicate record_id: same" in item for item in blockers)


def test_verified_record_requires_independent_fields():
    bad = record(
        "verified-missing-proof",
        "VERIFIED",
        independent_verifier="",
        verification_method="",
        reviewed_at="",
        evidence_refs=[],
    )
    errors = validate_record(bad, SCHEMA)
    assert "VERIFIED record missing independent_verifier" in errors
    assert "VERIFIED record missing verification_method" in errors
    assert "VERIFIED record missing reviewed_at" in errors
    assert "evidence_refs must be a non-empty array" in errors


def test_malformed_json_blocks_without_being_counted():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "broken.json").write_text("{not-json", encoding="utf-8")
        counts, blockers, seen = scan_records(root, SCHEMA)
        assert seen == 1
        assert all(value == 0 for value in counts.values())
        assert any("invalid JSON" in item for item in blockers)


if __name__ == "__main__":
    test_duplicate_record_ids_block()
    test_verified_record_requires_independent_fields()
    test_malformed_json_blocks_without_being_counted()
    print("Supreme independent verification ledger integrity: PASS")
