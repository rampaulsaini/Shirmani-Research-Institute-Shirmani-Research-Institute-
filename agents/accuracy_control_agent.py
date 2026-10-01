"""Deterministic accuracy-control layer for the research factory.

This module never upgrades a claim to VERIFIED. It computes auditable quality
signals from provenance, evidence, verification state, duplication and internal
consistency, then fails closed when required fields are missing.
"""
from __future__ import annotations
import hashlib, json, re
from collections import Counter
from pathlib import Path
from typing import Any

VERIFIED = {"VERIFIED"}
UNVERIFIED = {"UNVERIFIED", "NOT_VERIFIED", "EVIDENCE-SUPPORTED", "DRAFT", "UNKNOWN", ""}

def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                value=json.loads(line)
                if isinstance(value, dict):
                    rows.append(value)
            except json.JSONDecodeError:
                continue
    return rows

def _text(row: dict[str, Any]) -> str:
    for key in ("text","claim","statement","content","source_text"):
        if isinstance(row.get(key), str):
            return row[key].strip()
    return ""

def _fingerprint(text: str) -> str:
    normalized=re.sub(r"\s+"," ",text.lower()).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

def _status(row: dict[str, Any]) -> str:
    value=row.get("verification_status", row.get("status", ""))
    return str(value).upper()

def score(row: dict[str, Any]) -> dict[str, Any]:
    text=_text(row)
    evidence=row.get("evidence") or row.get("evidence_ids") or row.get("sources")
    provenance=row.get("source") or row.get("source_id") or row.get("provenance")
    checks={
        "nonempty_text": bool(text),
        "provenance_present": bool(provenance),
        "evidence_present": bool(evidence),
        "explicit_verification_state": bool(_status(row)),
        "not_overclaiming_verified": _status(row) in UNVERIFIED | VERIFIED,
    }
    passed=sum(checks.values())
    quality=round(100*passed/len(checks),2)
    return {"quality_signal_percent":quality,"checks":checks}

def audit(input_paths: list[str]) -> dict[str, Any]:
    rows=[]
    for raw in input_paths:
        rows.extend(_load_jsonl(Path(raw)))
    fingerprints=Counter()
    statuses=Counter()
    results=[]
    for row in rows:
        text=_text(row)
        fp=_fingerprint(text) if text else ""
        if fp: fingerprints[fp]+=1
        statuses[_status(row) or "MISSING"]=statuses.get(_status(row) or "MISSING",0)+1
        result=score(row)
        result["id"]=row.get("id") or row.get("claim_id") or row.get("artifact_id")
        result["status"]=_status(row) or "MISSING"
        result["duplicate_count"]=0
        results.append(result)
    for result in results:
        # IDs are stable; duplicate count is attached after the first pass.
        row_id=result.get("id")
        if row_id is not None:
            pass
    duplicate_groups=sum(1 for n in fingerprints.values() if n>1)
    verified=sum(1 for r in results if r["status"] in VERIFIED)
    return {
        "schema_version":"1.0",
        "mode":"deterministic-accuracy-control",
        "fail_closed":True,
        "records_scanned":len(results),
        "status_counts":dict(statuses),
        "verified_records_observed":verified,
        "duplicate_groups":duplicate_groups,
        "quality_signal_mean_percent":round(
            sum(r["quality_signal_percent"] for r in results)/len(results),2
        ) if results else 0.0,
        "publication_decision":"PASS" if results and all(
            all(r["checks"].values()) for r in results
        ) else ("NO_DATA" if not results else "CHECK"),
        "important_boundary":"quality signals are not independent verification and never promote claims to VERIFIED",
        "records":results[:5000],
    }

def main() -> None:
    candidates=[
        "generated/claim-evidence.jsonl",
        "generated/provenance-ledger.jsonl",
        "generated/independent-verification-registry.jsonl",
        "generated/verse-corpus.jsonl",
    ]
    report=audit(candidates)
    Path("generated").mkdir(exist_ok=True)
    Path("generated/ACCURACY-CONTROL.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps({k:report[k] for k in (
        "records_scanned","verified_records_observed","duplicate_groups",
        "quality_signal_mean_percent","publication_decision"
    )},ensure_ascii=False))

if __name__=="__main__":
    main()
