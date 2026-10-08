#!/usr/bin/env python3
"""Focused fail-closed tests for the independent verification gate."""

from pathlib import Path
import importlib.util
import pytest

SPEC = importlib.util.spec_from_file_location(
    "independent_verification_gate",
    Path(__file__).parents[1] / "scripts" / "independent_verification_gate.py",
)
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


def valid_verified_record():
    return {
        "id": "TEST-001",
        "status": "VERIFIED",
        "operational_definition": "A reproducible pass/fail observation.",
        "independent_sources": [{
            "locator": "https://example.org/independent-study",
            "independence_attested": True,
            "author_authored": False,
        }],
        "test_or_observation": {
            "protocol": "pre-registered protocol",
            "result": "PASS",
        },
        "counter_evidence_review": {"reviewed": True},
        "result": "PASS",
        "reviewer": {"identity": "independent-reviewer", "role": "reviewer"},
        "author_identity": "claim-author",
        "reviewed_at": "2026-10-08T00:00:00Z",
        "decision": "VERIFIED",
    }


def assert_gate_failure(record, expected):
    with pytest.raises(SystemExit, match=expected):
        GATE.validate_record(record)


def test_verified_record_requires_structured_independent_source():
    record = valid_verified_record()
    record["independent_sources"] = ["https://example.org/independent-study"]
    assert_gate_failure(record, "independent_sources must contain structured provenance objects")


def test_author_source_cannot_be_independent():
    record = valid_verified_record()
    record["independent_sources"][0]["author_authored"] = True
    assert_gate_failure(record, "author-authored material cannot be an independent source")


def test_independence_must_be_explicitly_attested():
    record = valid_verified_record()
    record["independent_sources"][0]["independence_attested"] = False
    assert_gate_failure(record, "independence_attested=true")


def test_test_protocol_and_result_are_required():
    record = valid_verified_record()
    record["test_or_observation"] = {"protocol": "protocol only"}
    assert_gate_failure(record, "test_or_observation requires protocol and result")


def test_counter_evidence_must_be_reviewed():
    record = valid_verified_record()
    record["counter_evidence_review"] = {"reviewed": False}
    assert_gate_failure(record, "counter_evidence_review must explicitly record reviewed=true")


def test_reviewer_must_be_distinct_from_author():
    record = valid_verified_record()
    record["reviewer"]["identity"] = record["author_identity"]
    assert_gate_failure(record, "reviewer must be distinct from the author")


def test_valid_verified_record_passes_record_level_gate():
    GATE.validate_record(valid_verified_record())
