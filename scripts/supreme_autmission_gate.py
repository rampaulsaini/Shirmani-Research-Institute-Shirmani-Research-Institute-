#!/usr/bin/env python3
"""Deterministic, fail-closed integrity gate for the Automission research pipeline."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CLAIM_FIELDS = ("claim_id", "claim", "evidence_state", "verification_state", "provenance")

def load_jsonl(path: Path) -> tuple[list[dict[str, Any]], int]:
    rows = []
    malformed = 0
    if not path.exists():
        return rows, malformed
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict):
                rows.append(obj)
            else:
                malformed += 1
        except json.JSONDecodeError:
            malformed += 1
    return rows, malformed

def check_claim_records(root: Path) -> dict[str, Any]:
    candidates = [
        root / "generated/claim-evidence.jsonl",
        root / "generated/agent-run/claims-index.jsonl",
        root / "generated/agent-run/claims.jsonl",
    ]
    path = next((p for p in candidates if p.exists()), None)
    if path is None:
        return {"name":"claim-record-integrity","status":"REVIEW","reason":"No supported claim-evidence JSONL was found; no claim quality was inferred.","records":0,"malformed":0}
    rows, malformed = load_jsonl(path)
    missing = 0
    unsafe_verified = 0
    ids: set[str] = set()
    duplicates = 0
    for row in rows:
        rid = str(row.get("claim_id", "")).strip()
        if rid:
            if rid in ids:
                duplicates += 1
            ids.add(rid)
        if any(not str(row.get(k, "")).strip() for k in CLAIM_FIELDS):
            missing += 1
        if str(row.get("verification_state", "")).upper() in {"VERIFIED", "INDEPENDENTLY_VERIFIED"}:
            evidence = str(row.get("evidence_state", "")).upper()
            if evidence not in {"INDEPENDENT", "INDEPENDENTLY_VERIFIED"}:
                unsafe_verified += 1
    blocked = malformed > 0 or missing > 0 or unsafe_verified > 0
    status = "BLOCKED" if blocked else ("REVIEW" if duplicates else "PASS")
    return {"name":"claim-record-integrity","status":status,"source":str(path.relative_to(root)),"records":len(rows),"malformed":malformed,"missing_required_fields":missing,"duplicate_claim_ids":duplicates,"unsafe_verified_states":unsafe_verified}

def check_required_architecture(root: Path) -> dict[str, Any]:
    required = ["PROJECT-CONTINUITY.md","docs/yatharth-governance/ai-control-contract.md","factory","agents","schemas"]
    missing = [p for p in required if not (root / p).exists()]
    return {"name":"architecture-presence","status":"BLOCKED" if missing else "PASS","missing":missing}

def hash_report_inputs(root: Path) -> dict[str, Any]:
    files = []
    for rel in ("PROJECT-CONTINUITY.md","docs/yatharth-governance/ai-control-contract.md"):
        p = root / rel
        if p.is_file():
            files.append({"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size})
    return {"name":"provenance-anchor","status":"PASS" if files else "REVIEW","files":files}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    checks = [check_required_architecture(root), check_claim_records(root), hash_report_inputs(root)]
    status = "BLOCKED" if any(c["status"]=="BLOCKED" for c in checks) else ("REVIEW" if any(c["status"]=="REVIEW" for c in checks) else "PASS")
    report = {
        "schema_version":"2.0",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "status":status,
        "principles":[
            "fail_closed_on_malformed_or_unsafe_verification_states",
            "no_generated_text_is_independent_evidence",
            "missing_evidence_is_not_filled_by_inference",
            "pipeline_integrity_is_not_scientific_truth",
        ],
        "checks":checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status":status,"checks":len(checks)}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
