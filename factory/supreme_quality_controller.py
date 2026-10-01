"""Deterministic Supreme Quality Controller for the SHIRMANI Automission plane.

This controller does not claim perfect or scientific accuracy. It gates only
properties that can be mechanically checked: provenance, duplicate IDs,
content hashes, verification boundaries, and observable worker state.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
REPORT = OUT / "supreme-quality-report.json"

def read_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def jsonl(path: Path):
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def check_corpus():
    rows=jsonl(OUT/"verse-corpus.jsonl")
    ids=[str(r.get("id")) for r in rows]
    return {
        "records":len(rows),
        "duplicate_ids":len(ids)-len(set(ids)),
        "bad_content_hashes":sum(1 for r in rows if r.get("content_hash") != sha(str(r.get("text","")))),
        "missing_provenance":sum(1 for r in rows if not r.get("source_ids") or not r.get("method_trace")),
        "unsafe_verified_claims":sum(1 for r in rows if r.get("evidence_status") == "VERIFIED"),
    }

def check_verification():
    d=read_json(OUT/"independent-verification-status-2026-09-29.json", {})
    s=d.get("verification_summary", {})
    records=d.get("records", [])
    return {
        "queue_records":len(records),
        "independently_verified_records":s.get("independently_verified_records"),
        "independent_verified_percent":s.get("independent_verified_percent"),
        "fail_closed":all(r.get("status") != "VERIFIED" for r in records),
    }

def check_worker():
    d=read_json(OUT/"worker-status.json", {})
    return {
        "worker_observable":bool(d.get("generated_at")),
        "generated_at":d.get("generated_at"),
        "completed":d.get("completed", {}),
    }

def main():
    corpus=check_corpus()
    verification=check_verification()
    worker=check_worker()
    hard_failures=[]
    for key in ("duplicate_ids","bad_content_hashes","missing_provenance","unsafe_verified_claims"):
        if corpus[key] != 0:
            hard_failures.append(f"corpus.{key}={corpus[key]}")
    if verification["fail_closed"] is False:
        hard_failures.append("verification.fail_closed=false")
    checks={
        "corpus_integrity":not hard_failures and all(corpus[k] == 0 for k in ("duplicate_ids","bad_content_hashes","missing_provenance","unsafe_verified_claims")),
        "verification_boundary":verification["fail_closed"],
        "worker_observable":worker["worker_observable"],
    }
    report={
        "schema_version":"1.0",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "mode":"fail-closed-deterministic-quality-control",
        "claim_policy":"Only mechanically verified properties are marked PASS; perfect accuracy is not asserted.",
        "checks":checks,
        "passed_checks":sum(checks.values()),
        "total_checks":len(checks),
        "corpus":corpus,
        "verification":verification,
        "worker":worker,
        "hard_failures":hard_failures,
        "next_action":"CONTINUE_AUTOMISSION" if not hard_failures else "STOP_AND_REPAIR",
    }
    OUT.mkdir(parents=True,exist_ok=True)
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if hard_failures:
        raise SystemExit(2)

if __name__=="__main__":
    main()
