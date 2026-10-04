#!/usr/bin/env python3
"""Fail-closed validation for Research Paper source intake."""
import json
from pathlib import Path

source = json.loads(Path("federation/research-paper-source-intake.json").read_text(encoding="utf-8"))
claims = json.loads(Path("generated/research-paper-claims.json").read_text(encoding="utf-8"))

assert source["repository"] == claims["source_repository"]
assert source["verification_status"] == "UNVERIFIED"
assert source["independent_verification_required"] is True
assert source["claim_registry"] == "generated/research-paper-claims.json"
assert source["intake_status"] == "REGISTERED"
assert source["downstream_flow"] == [
    "SOURCE","CLAIM","EVIDENCE","FORMULATION_TEST",
    "INDEPENDENT_VERIFICATION","QC","PUBLICATION","ARCHIVE"
]
assert all(c["verification_status"] == "UNVERIFIED" for c in claims["claims"])
assert all(c["status"] == "AUTHOR_PROPOSITION" for c in claims["claims"])
print("Research Paper source intake: PASS (fail-closed)")
