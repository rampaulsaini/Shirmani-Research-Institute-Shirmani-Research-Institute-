#!/usr/bin/env python3
"""Fail-closed deterministic QC for the Heart-View neutrality contract."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "heart-view-neutrality.json"
ALLOWED_STATUS = {"user-authored","source-backed","hypothesis","unverified","verified"}
ALLOWED_VERIFICATION = {"not-reviewed","evidence-supported","independently-verified"}
REQUIRED_FIELDS = {"claim","status","provenance","evidence","uncertainty","counterevidence","verification_state"}

def fail(msg: str) -> None:
    raise SystemExit(f"HEART-VIEW-NEUTRALITY-QC: BLOCK: {msg}")

def validate_agent_output(rec, path):
    missing=REQUIRED_FIELDS-set(rec)
    if missing:
        fail(f"{path}: missing fields {sorted(missing)}")
    if rec["status"] not in ALLOWED_STATUS:
        fail(f"{path}: invalid status {rec['status']!r}")
    if rec["verification_state"] not in ALLOWED_VERIFICATION:
        fail(f"{path}: invalid verification_state {rec['verification_state']!r}")
    if not isinstance(rec["uncertainty"], (str,int,float,bool,dict,list)) or rec["uncertainty"] in ("",None):
        fail(f"{path}: uncertainty must be explicit")
    if not rec["provenance"]:
        fail(f"{path}: provenance is required")
    if rec["verification_state"] == "independently-verified" and not rec.get("verification_record"):
        fail(f"{path}: independent verification requires verification_record")
    if rec.get("external_side_effects") and rec.get("requires_human_authorization") is not True:
        fail(f"{path}: external side effects require human authorization")

def validate_claim_evidence(rec, path):
    # The existing factory claim-evidence format is accepted without rewriting it.
    # This gate checks traceability, uncertainty, countercases and the explicit
    # boundary that provenance is not independent proof.
    required={"claim","source","evidence","countercases","verification","provenance"}
    missing=required-set(rec)
    if missing:
        fail(f"{path}: claim-evidence missing fields {sorted(missing)}")
    if not isinstance(rec["claim"], str):
        fail(f"{path}: claim must be text")
    if not isinstance(rec["source"], list) or not rec["source"]:
        fail(f"{path}: claim requires at least one source trace")
    if not isinstance(rec["evidence"], list) or not rec["evidence"]:
        fail(f"{path}: claim requires an explicit evidence section")
    if not isinstance(rec["countercases"], list) or not rec["countercases"]:
        fail(f"{path}: countercases must be preserved")
    verification=rec["verification"]
    if not isinstance(verification, dict):
        fail(f"{path}: verification must be an object")
    if verification.get("status") != "NOT_VERIFIED":
        fail(f"{path}: generated claim-evidence may not self-promote verification")
    if verification.get("independent") is not False:
        fail(f"{path}: generated claim-evidence must declare independent=false")
    if not rec["provenance"]:
        fail(f"{path}: provenance is required")
    formulation=rec.get("formulation", {})
    if formulation and formulation.get("result_status") not in (None, "NOT_VERIFIED"):
        fail(f"{path}: generated formulation may not self-promote verification")

def main() -> int:
    try:
        p=json.loads(POLICY.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid policy: {exc}")

    for key, value in {
        "fail_closed": True,
        "claims_require_provenance": True,
        "uncertainty_must_be_explicit": True,
        "counterevidence_must_be_preserved": True,
        "no_hidden_preference": True,
        "no_unsupported_inference": True,
        "no_automatic_verification": True,
        "no_automatic_irreversible_action": True,
        "human_authorization_required_for_external_side_effects": True,
    }.items():
        if p.get(key) is not value:
            fail(f"{key} must be {value!r}")

    contract=p.get("output_contract", {})
    if set(contract.get("required_fields", [])) != REQUIRED_FIELDS:
        fail("required output fields are incomplete")
    if set(contract.get("allowed_status", [])) != ALLOWED_STATUS:
        fail("status vocabulary mismatch")
    if set(contract.get("allowed_verification_state", [])) != ALLOWED_VERIFICATION:
        fail("verification vocabulary mismatch")

    checked=0
    for raw in sys.argv[1:]:
        path=Path(raw)
        if not path.is_absolute():
            path=ROOT/path
        if not path.is_file():
            fail(f"missing record file: {path}")
        try:
            payload=json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid JSON record {path}: {exc}")
        records=payload if isinstance(payload,list) else [payload]
        for rec in records:
            checked += 1
            if {"source","countercases","verification"} <= set(rec):
                validate_claim_evidence(rec, path)
            else:
                validate_agent_output(rec, path)

    print(f"HEART-VIEW-NEUTRALITY-QC: PASS (policy + {checked} records)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
