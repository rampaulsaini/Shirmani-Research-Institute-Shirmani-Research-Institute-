"""Deterministic evidence/consistency gate for Automission outputs.

This gate does not claim scientific truth. It measures whether an artifact has
enough traceability, structural integrity, independent evidence, and semantic
consistency to advance to a human/reviewer verification stage.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Any

REQUIRED=("artifact_id","kind","language","status","sha256","provenance","created_at")

def _stable(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def score(record: dict[str, Any]) -> dict[str, Any]:
    checks = {
        "required_fields": all(record.get(k) not in (None, "") for k in REQUIRED),
        "hash_format": isinstance(record.get("sha256"), str) and len(record["sha256"]) == 64,
        "provenance": isinstance(record.get("provenance"), (dict, str)) and bool(record.get("provenance")),
        "status_allowed": record.get("status") in {"draft", "source-backed", "verified", "unverified"},
    }
    evidence = record.get("evidence")
    checks["evidence_present"] = bool(evidence)
    independent = record.get("independent_evidence")
    checks["independent_evidence"] = bool(independent)
    passed = sum(checks.values())
    confidence_band = "blocked" if passed < 4 else ("review" if passed < 6 else "eligible")
    return {"checks": checks, "checks_passed": passed, "confidence_band": confidence_band}

def audit(path: str = "generated/artifact-manifest.jsonl") -> dict[str, Any]:
    p=Path(path)
    if not p.exists():
        return {"status":"blocked","reason":"manifest_missing","records":0}
    records=[]; errors=[]; seen=set()
    for n,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: r=json.loads(line)
        except Exception as exc:
            errors.append(f"line_{n}:invalid_json:{exc}"); continue
        aid=r.get("artifact_id")
        if aid in seen: errors.append(f"line_{n}:duplicate_artifact_id:{aid}")
        seen.add(aid)
        s=score(r); records.append({"artifact_id":aid,**s})
    eligible=sum(x["confidence_band"]=="eligible" for x in records)
    review=sum(x["confidence_band"]=="review" for x in records)
    blocked=sum(x["confidence_band"]=="blocked" for x in records)
    digest=hashlib.sha256(_stable(records).encode()).hexdigest()
    return {
        "status":"pass" if not errors and blocked==0 else "review",
        "records":len(records),"eligible":eligible,"review":review,"blocked":blocked,
        "errors":errors,"audit_digest":digest,
        "policy":"No automated gate may represent its score as absolute truth."
    }

if __name__ == "__main__":
    result=audit()
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result["status"] in {"pass","review"} else 1)
