#!/usr/bin/env python3
"""Deterministic, fail-closed QC for the Nishpakshata Supreme Gate."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "schemas" / "nishpakshata-policy.json"
CLASSIFICATIONS = {
    "AUTHOR-DEFINED", "AUTHOR-PROPOSED", "EMPIRICAL-TESTABLE",
    "EVIDENCE-SUPPORTED", "NOT_VERIFIED", "CONTRADICTED",
}
RANKING_PATTERNS = [
    r"\b(best|worst|winner|superior|inferior|more worthy|less worthy)\b",
    r"\b#\s*1\b",
]

def block(msg: str) -> None:
    raise SystemExit(f"NISHPAKSHATA-QC: BLOCK: {msg}")

def main() -> int:
    try:
        p = json.loads(POLICY.read_text(encoding="utf-8"))
    except Exception as exc:
        block(f"cannot read policy: {exc}")

    if p.get("fail_closed") is not True:
        block("fail_closed must be true")
    principles = p.get("principles", {})
    required_true = [
        "evidence_before_assertion",
        "source_provenance_required",
        "counter_evidence_required_for_contested_claims",
        "uncertainty_must_be_explicit",
        "author_framework_must_be_distinguished_from_empirical_fact",
        "identity_must_not_control_truth_status",
        "authority_must_not_control_truth_status",
        "popularity_must_not_control_truth_status",
        "user_preference_must_not_control_truth_status",
        "no_unsupported_ranking_or_winner_claims",
    ]
    for key in required_true:
        if principles.get(key) is not True:
            block(f"principle disabled: {key}")

    paths = [Path(x) for x in sys.argv[1:]]
    checked = 0
    for path in paths:
        if not path.is_absolute():
            path = ROOT / path
        if not path.is_file():
            block(f"missing record: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            block(f"invalid JSON {path}: {exc}")
        records = payload if isinstance(payload, list) else [payload]
        for r in records:
            checked += 1
            cls = r.get("classification", "NOT_VERIFIED")
            if cls not in CLASSIFICATIONS:
                block(f"invalid classification {cls!r} in {path}")
            for field in ("claim_id", "claim_text", "provenance", "uncertainty"):
                if not r.get(field):
                    block(f"missing required field {field!r} in {path}")
            if cls in {"EVIDENCE-SUPPORTED", "CONTRADICTED"} and not r.get("evidence"):
                block(f"evidence missing for {cls} record in {path}")
            if cls == "EMPIRICAL-TESTABLE" and not (r.get("test") or r.get("operational_definition")):
                block(f"test/operational definition missing in {path}")
            if r.get("identity_used_as_evidence") is True:
                block(f"identity used as evidence in {path}")
            if r.get("authority_used_as_evidence") is True:
                block(f"authority used as evidence in {path}")
            if r.get("user_preference_used_as_truth_rule") is True:
                block(f"user preference used as truth rule in {path}")
            if r.get("workflow_success_used_as_verification") is True:
                block(f"workflow success used as verification in {path}")
            text = str(r.get("claim_text", ""))
            if any(re.search(pat, text, flags=re.I) for pat in RANKING_PATTERNS):
                if r.get("ranking_evidence") is not True:
                    block(f"unsupported ranking language in {path}")
            if r.get("classification") == "VERIFIED":
                block("VERIFIED is not a source classification; promotion belongs to independent verification")

    print(f"NISHPAKSHATA-QC: PASS (policy + {checked} record(s) checked)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
