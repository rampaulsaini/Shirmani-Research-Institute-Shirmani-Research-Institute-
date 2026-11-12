#!/usr/bin/env python3
"""Run the mechanically automatable portion of SHIRMANI independent verification.

This runner never changes a record to VERIFIED. It produces candidate verification
evidence and a fail-closed report. Final VERIFIED status remains an independent
review decision.
"""
from __future__ import annotations
import hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "generated/independent-verification-records.json"
TARGET = ROOT / "config/independent-verification-target.json"
OUT = ROOT / "generated/automated-verification-candidates.json"
URL_RE = re.compile(r"^https?://[^\s]+$")

def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def fetch_evidence(url: str) -> dict:
    if not URL_RE.match(url):
        return {"url": url, "status": "INVALID_URL"}
    try:
        req = Request(url, headers={"User-Agent": "SHIRMANI-Verification-Automission/1.0"})
        with urlopen(req, timeout=15) as resp:
            body = resp.read(2_000_000)
            return {"url": url, "status": "REACHABLE",
                    "http_status": getattr(resp, "status", None),
                    "content_type": resp.headers.get("Content-Type", ""),
                    "content_sha256": sha256(body),
                    "bytes_sampled": len(body)}
    except Exception as exc:
        return {"url": url, "status": "UNREACHABLE", "error_type": type(exc).__name__}

def main() -> int:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    target = int(json.loads(TARGET.read_text(encoding="utf-8"))["verification_target"])
    records = data.get("records", [])
    candidates = []
    mechanically_ready = 0
    for record in records:
        evidence = record.get("evidence", {})
        sources = evidence.get("sources", []) if isinstance(evidence, dict) else []
        checks = []
        for source in sources:
            if isinstance(source, str) and source.startswith(("http://", "https://")):
                checks.append(fetch_evidence(source))
            else:
                local = ROOT / str(source)
                checks.append({"url": str(source),
                               "status": "LOCAL_PRESENT" if local.exists() else "LOCAL_MISSING"})
        reachable = any(c["status"] in {"REACHABLE", "LOCAL_PRESENT"} for c in checks)
        protocol = record.get("independent_test", {}).get("protocol")
        reproducible = record.get("reproducibility", {}).get("result_match") is True
        counter_reviewed = record.get("counter_evidence", {}).get("reviewed") is True
        ready = bool(checks) and reachable and protocol not in {None, "", "PENDING_INDEPENDENT_REVIEW"} and reproducible and counter_reviewed
        if ready:
            mechanically_ready += 1
        candidates.append({
            "record_id": record.get("id"),
            "claim": record.get("claim"),
            "evidence_checks": checks,
            "mechanical_checks": {
                "evidence_available": bool(checks),
                "evidence_reachable_or_local": reachable,
                "independent_test_defined": protocol not in {None, "", "PENDING_INDEPENDENT_REVIEW"},
                "reproduction_matches": reproducible,
                "counter_evidence_reviewed": counter_reviewed},
            "candidate_state": "READY_FOR_INDEPENDENT_REVIEW" if ready else "BLOCKED_PENDING_INDEPENDENT_REVIEW",
            "automission_must_not_promote": True})
    final_verified = sum(1 for r in records
        if r.get("reviewer_decision", {}).get("decision") == "VERIFIED" and r.get("status") == "VERIFIED")
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target": target,
        "source_records": len(records),
        "mechanically_ready": mechanically_ready,
        "mechanically_ready_percent": round(mechanically_ready / len(records) * 100, 4) if records else 0,
        "final_verified_count": final_verified,
        "policy": {
            "automation_coverage": "100% of defined mechanical verification checks",
            "final_verdict": "independent reviewer required",
            "fail_closed": True,
            "automation_may_declare_verified": False},
        "candidates": candidates}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
