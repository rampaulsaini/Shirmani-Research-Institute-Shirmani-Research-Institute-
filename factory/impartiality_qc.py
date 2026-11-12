#!/usr/bin/env python3
"""Deterministic fail-closed QC for impartial Heart-View Automission governance."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "impartiality-governance.json"
SIGNAL_SCHEMA = ROOT / "schemas" / "supreme-nlp-signal-record.schema.json"
CONTRACT = ROOT / "schemas" / "supreme-nlp-contract.json"

def fail(msg: str) -> None:
    raise SystemExit("IMPARTIALITY-QC BLOCK: " + msg)

def load(path: Path):
    if not path.is_file():
        fail(f"missing required file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {path}: {exc}")

policy = load(POLICY)
signal_schema = load(SIGNAL_SCHEMA)
contract = load(CONTRACT)

if policy.get("fail_closed") is not True:
    fail("policy must be fail-closed")
principles = policy.get("principles", {})
required_principles = [
    "equal_treatment", "evidence_before_claim", "uncertainty_must_be_explicit",
    "counter_evidence_must_be_allowed", "independent_verification_required",
    "provenance_required", "subjective_experience_is_not_inferred_as_fact",
    "no_person_or_ideology_is_a_truth_authority", "high_impact_actions_require_human_review",
]
for key in required_principles:
    if principles.get(key) is not True:
        fail(f"principle missing or disabled: {key}")

if contract.get("fail_closed") is not True:
    fail("supreme NLP contract is not fail-closed")
if contract.get("fabrication_prohibited") is not True:
    fail("fabrication prohibition is disabled")
if contract.get("truth_boundary", {}).get("direct_feeling_claims") != "NOT_INFERRED":
    fail("direct-feeling truth boundary is unsafe")
if contract.get("truth_boundary", {}).get("verified") != "REQUIRES_INDEPENDENT_VERIFICATION_RECORD":
    fail("verification boundary is unsafe")

required_signal_fields = set(policy["required_record_fields"])
schema_required = set(signal_schema.get("required", []))
if not required_signal_fields.issubset(schema_required | {"provenance"}):
    fail("policy fields are not represented by the signal-record contract")

# Audit available generated signal records without inventing a benchmark result.
candidates = [
    ROOT / "generated" / "supreme-nlp-signal-records.jsonl",
    ROOT / "generated" / "supreme-nlp-signal-record.jsonl",
]
records = []
for path in candidates:
    if path.is_file():
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                records.append((path, n, json.loads(line)))
            except Exception as exc:
                fail(f"invalid JSONL {path}:{n}: {exc}")

for path, line_no, record in records:
    missing = required_signal_fields - set(record)
    if missing:
        fail(f"{path}:{line_no} missing {sorted(missing)}")
    if not 0 <= float(record["confidence"]) <= 1:
        fail(f"{path}:{line_no} confidence outside [0,1]")
    if not str(record["uncertainty"]).strip():
        fail(f"{path}:{line_no} uncertainty is empty")
    if not isinstance(record["counter_evidence_refs"], list):
        fail(f"{path}:{line_no} counter_evidence_refs must be a list")
    status = record.get("verification_status")
    if status == "INDEPENDENTLY_VERIFIED":
        provenance = record.get("provenance")
        if not isinstance(provenance, list) or not provenance:
            fail(f"{path}:{line_no} verified record lacks provenance")

print("IMPARTIALITY-QC PASS")
print(f"Audited generated signal records: {len(records)}")
print("Benchmark-dependent accuracy/bias claims remain NOT_PROVEN until evaluation data exists.")
