#!/usr/bin/env python3
"""Deterministic neutrality/epistemic-status QC.

This layer preserves source-defined propositions while preventing an AI agent
from silently converting authorship, model confidence, repetition, popularity,
authority, or workflow success into empirical verification.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "neutrality-contract.json"
ALLOWED = {
    "AUTHOR_DEFINED", "AUTHOR_PROPOSED", "EMPIRICAL_TESTABLE",
    "EVIDENCE_SUPPORTED", "NOT_VERIFIED", "CONTRADICTED"
}

def block(msg: str) -> None:
    raise SystemExit(f"NEUTRALITY-QC: BLOCK: {msg}")

def main() -> int:
    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    if policy.get("fail_closed") is not True:
        block("fail_closed must be true")
    if set(policy.get("claim_statuses", [])) != ALLOWED:
        block("claim status set is incomplete or unexpected")

    checked = 0
    for raw in sys.argv[1:]:
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        if not path.is_file():
            block(f"record missing: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        records = payload if isinstance(payload, list) else [payload]
        for r in records:
            checked += 1
            status = r.get("status", "NOT_VERIFIED")
            if status not in ALLOWED:
                block(f"invalid status {status!r}: {path}")
            if not r.get("claim_id") or not r.get("claim_text"):
                block(f"claim identity/text missing: {path}")
            if not r.get("provenance"):
                block(f"provenance missing: {path}")
            if status in {"EVIDENCE_SUPPORTED", "CONTRADICTED"}:
                if not r.get("reasoning_basis"):
                    block(f"reasoning basis missing for {status}: {path}")
            if status == "VERIFIED":
                block("VERIFIED is intentionally not a claim status; use the independent verification registry.")
            if r.get("verification_basis") == "model_confidence":
                block("model confidence cannot be verification")
            if r.get("verification_basis") == "workflow_success":
                block("workflow success cannot be verification")
            if r.get("authority_as_proof") is True:
                block("authority cannot be used as proof")
    print(f"NEUTRALITY-QC: PASS ({checked} records checked)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
