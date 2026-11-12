#!/usr/bin/env python3
"""Deterministic evidence-fusion gate for AI/ML/NLP Automission.

This module improves practical precision and speed by cross-checking the
canonical reasoning, claim/evidence and provenance ledgers.  Its score is a
quality signal, never a probability of truth, and it can never create VERIFIED
status.
"""
from __future__ import annotations
import hashlib, json, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
OUT = GENERATED / "supreme-evidence-fusion.json"
ALLOWED_EVIDENCE = {"SUPPORTED","PARTIAL","UNAVAILABLE","CONTRADICTED","NOT_VERIFIED"}
SAFE_UNVERIFIED = {"NOT_VERIFIED","UNVERIFIED","UNKNOWN","DRAFT",""}
INDEPENDENT = {"VERIFIED","INDEPENDENTLY_VERIFIED"}

def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], int]:
    rows, malformed = [], 0
    if not path.exists():
        return rows, malformed
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                rows.append(value)
            else:
                malformed += 1
        except json.JSONDecodeError:
            malformed += 1
    return rows, malformed

def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def parse_time(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def source_id_set(rows: list[dict[str, Any]]) -> set[str]:
    return {str(r.get("id")) for r in rows if r.get("id") is not None}

def audit(root: Path = ROOT) -> dict[str, Any]:
    claim_path = root / "generated/claim-evidence.jsonl"
    reasoning_path = root / "generated/reasoning-manifest.jsonl"
    provenance_path = root / "generated/provenance-ledger.jsonl"
    source_path = root / "generated/source-units.jsonl"

    claims, claim_bad = read_jsonl(claim_path)
    reasoning, reasoning_bad = read_jsonl(reasoning_path)
    provenance, provenance_bad = read_jsonl(provenance_path)
    sources, source_bad = read_jsonl(source_path)

    claim_ids = [str(r.get("id","")) for r in claims]
    duplicate_claim_ids = len(claim_ids) - len(set(x for x in claim_ids if x))
    source_ids = source_id_set(sources)
    reasoning_ids = {f"{r.get('kind')}:{r.get('artifact_id')}" for r in reasoning}
    provenance_ids = {str(r.get("artifact_id")) for r in provenance}

    checks = []
    def check(name: str, passed: bool, detail: Any = None):
        item = {"name": name, "status": "PASS" if passed else "BLOCK", "detail": detail}
        checks.append(item)
        return passed

    check("claim_evidence_present", bool(claims), len(claims))
    check("claim_evidence_json_valid", claim_bad == 0, {"malformed": claim_bad})
    check("reasoning_json_valid", reasoning_bad == 0, {"malformed": reasoning_bad})
    check("provenance_json_valid", provenance_bad == 0, {"malformed": provenance_bad})
    check("source_json_valid", source_bad == 0, {"malformed": source_bad})
    check("unique_claim_ids", duplicate_claim_ids == 0, duplicate_claim_ids)

    unsafe_verified = 0
    missing_fields = 0
    unresolved_sources = 0
    bad_evidence_states = 0
    bad_provenance = 0
    bad_verification = 0
    cross_record_gaps = 0
    malformed_timestamps = 0

    for row in claims:
        required = ("id","claim","definitions","source","evidence","formulation",
                    "countercases","verification","conclusion","provenance")
        missing_fields += sum(1 for key in required if key not in row)
        evidence = row.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            bad_evidence_states += 1
        else:
            states = {str(e.get("status","")).upper() for e in evidence if isinstance(e, dict)}
            if not states or not states.issubset(ALLOWED_EVIDENCE):
                bad_evidence_states += 1
        verification = row.get("verification") or {}
        vstatus = str(verification.get("status","")).upper()
        if vstatus in INDEPENDENT or verification.get("independent") is True:
            # This gate never accepts a generated record's own verification as proof.
            bad_verification += 1
        if vstatus not in {"PASS","CHECK","FAIL","NOT_VERIFIED",""}:
            bad_verification += 1
        trace = row.get("source_traceability") or {}
        ids = {str(x) for x in trace.get("source_ids", [])}
        if trace.get("resolved") is not True or not ids or not ids.issubset(source_ids):
            unresolved_sources += 1
        prov = row.get("provenance") or {}
        if not prov.get("generator") or not prov.get("created_at") or not prov.get("content_hash"):
            bad_provenance += 1
        if not parse_time(prov.get("created_at")):
            malformed_timestamps += 1
        if str(row.get("id","")).startswith("claim:"):
            suffix = str(row["id"])[len("claim:"):]
            if suffix not in reasoning_ids:
                cross_record_gaps += 1
        # Any explicit VERIFIED state is treated as unsafe unless independently
        # supported outside this generated record.
        if str(row.get("status", row.get("verification_status",""))).upper() in INDEPENDENT:
            unsafe_verified += 1

    # Provenance must remain fail-closed.
    for row in provenance:
        if row.get("verification_status") not in {"NOT_VERIFIED","UNVERIFIED"} or row.get("independent") is not False:
            bad_provenance += 1
        if not row.get("content_sha256") or not row.get("generator") or not parse_time(row.get("created_at")):
            bad_provenance += 1

    hard = {
        "missing_required_fields": missing_fields,
        "unresolved_sources": unresolved_sources,
        "bad_evidence_states": bad_evidence_states,
        "bad_verification_states": bad_verification,
        "unsafe_verified_states": unsafe_verified,
        "bad_provenance": bad_provenance,
        "cross_record_gaps": cross_record_gaps,
        "malformed_timestamps": malformed_timestamps,
    }
    checks.extend([
        {"name":"required_fields", "status":"PASS" if missing_fields == 0 else "BLOCK", "detail":missing_fields},
        {"name":"source_resolution", "status":"PASS" if unresolved_sources == 0 else "BLOCK", "detail":unresolved_sources},
        {"name":"evidence_state_vocabulary", "status":"PASS" if bad_evidence_states == 0 else "BLOCK", "detail":bad_evidence_states},
        {"name":"verification_boundary", "status":"PASS" if bad_verification == 0 and unsafe_verified == 0 else "BLOCK",
         "detail":{"invalid":bad_verification,"unsafe_verified":unsafe_verified}},
        {"name":"provenance_integrity", "status":"PASS" if bad_provenance == 0 else "BLOCK", "detail":bad_provenance},
        {"name":"cross_record_consistency", "status":"PASS" if cross_record_gaps == 0 else "BLOCK", "detail":cross_record_gaps},
        {"name":"timestamp_integrity", "status":"PASS" if malformed_timestamps == 0 else "BLOCK", "detail":malformed_timestamps},
    ])

    pass_count = sum(c["status"] == "PASS" for c in checks)
    quality_signal = round(100 * pass_count / len(checks), 2) if checks else 0.0
    status = "BLOCKED" if any(c["status"] == "BLOCK" for c in checks) else "PASS"
    return {
        "schema_version":"3.0",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "status":status,
        "quality_signal_percent":quality_signal,
        "records":{"claims":len(claims),"reasoning":len(reasoning),"provenance":len(provenance),"sources":len(sources)},
        "hard_fail_metrics":hard,
        "checks":checks,
        "decision":{
            "automission_action":"CONTINUE" if status=="PASS" else "HOLD_AND_REVIEW",
            "verified_promotion":"NEVER_AUTOMATED",
            "publication":"BLOCKED_ON_ANY_HARD_FAILURE"
        },
        "truth_boundary":"This report measures pipeline integrity only; it does not establish truth, model correctness, or independent verification.",
    }

def main() -> int:
    report = audit()
    GENERATED.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
