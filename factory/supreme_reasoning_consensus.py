#!/usr/bin/env python3
"""Bounded independent consensus supervisor for the AI-agent/ML/NLP factory."""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json, re, time

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[\w'-]+", re.UNICODE)

def read_jsonl(path):
    if not path.exists(): return []
    rows=[]
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: rows.append((n,json.loads(line)))
        except Exception as exc: rows.append((n,{"__error__":f"{type(exc).__name__}:{exc}"}))
    return rows

def text_signature(text):
    tokens=[x.lower() for x in TOKEN.findall(text or "") if len(x)>1]
    return sha256("\x1f".join(sorted(tokens)).encode()).hexdigest()

def evaluate(out_dir="generated/agent-run"):
    started=time.perf_counter()
    root=ROOT/out_dir
    manifest=root/"artifact-manifest.jsonl"
    verification=root/"contracts"/"verification-reports.jsonl"
    provenance=root/"provenance-index.jsonl"
    errors=[]; warnings=[]
    artifacts=read_jsonl(manifest); reports=read_jsonl(verification); prov=read_jsonl(provenance)
    seen_ids=set(); seen_hashes=set(); seen_text=set()
    source_missing=0; language_mismatch=0
    status_counts=Counter(); report_statuses=defaultdict(set)
    if not manifest.exists(): errors.append("MISSING_ARTIFACT_MANIFEST")
    for n,row in artifacts:
        if "__error__" in row: errors.append(f"INVALID_ARTIFACT_JSON:{n}"); continue
        aid=str(row.get("artifact_id") or row.get("id") or "")
        if not aid: errors.append(f"MISSING_ARTIFACT_ID:{n}"); continue
        if aid in seen_ids: errors.append(f"DUPLICATE_ARTIFACT_ID:{aid}")
        seen_ids.add(aid)
        digest=str(row.get("sha256") or row.get("content_hash") or "")
        if not digest: errors.append(f"MISSING_CONTENT_HASH:{aid}")
        elif digest in seen_hashes: warnings.append(f"DUPLICATE_CONTENT_HASH:{aid}")
        seen_hashes.add(digest)
        sig=text_signature(str(row.get("text") or ""))
        if sig in seen_text: warnings.append(f"DUPLICATE_NORMALIZED_TEXT:{aid}")
        seen_text.add(sig)
        sources=row.get("source_ids") or []
        if not isinstance(sources,list) or not sources: source_missing+=1
        status=str(row.get("verification_status") or row.get("status") or "UNKNOWN")
        status_counts[status]+=1
        lang=row.get("language"); route=row.get("language_route")
        if lang and isinstance(route,dict):
            routed=str(route.get("language") or route.get("code") or "")
            if routed and routed!=str(lang): language_mismatch+=1
    for n,row in reports:
        if "__error__" in row: errors.append(f"INVALID_VERIFICATION_REPORT_JSON:{n}"); continue
        aid=row.get("claim_id") or row.get("artifact_id") or row.get("id")
        status=row.get("status") or row.get("verification_status")
        if aid is not None and status is not None: report_statuses[str(aid)].add(str(status))
    conflicts=[{"artifact_id":k,"statuses":sorted(v)} for k,v in report_statuses.items() if len(v)>1]
    if conflicts: warnings.append(f"CROSS_MANIFEST_STATUS_CONFLICTS:{len(conflicts)}")
    provenance_ids=set()
    for n,row in prov:
        if "__error__" in row: errors.append(f"INVALID_PROVENANCE_JSON:{n}"); continue
        aid=str(row.get("artifact_id") or "")
        if aid: provenance_ids.add(aid)
    missing_provenance=seen_ids-provenance_ids
    if missing_provenance: warnings.append(f"MISSING_PROVENANCE_RECORDS:{len(missing_provenance)}")
    total=len(seen_ids)
    source_coverage=1.0 if total==0 else round((total-source_missing)/total,4)
    provenance_coverage=1.0 if total==0 else round(len(seen_ids & provenance_ids)/total,4)
    language_health=1.0 if total==0 else round((total-language_mismatch)/total,4)
    conflict_health=1.0 if not report_statuses else round(1.0-len(conflicts)/max(1,len(report_statuses)),4)
    structural_health=0.0 if errors else 1.0
    score=round(100*(0.30*structural_health+0.25*source_coverage+0.20*provenance_coverage+0.10*language_health+0.15*conflict_health),2)
    gate="PASS" if total>0 and not errors and score>=98 and not conflicts else "HOLD"
    if gate=="HOLD": warnings.append("ABSTAIN: reliability gate does not establish truth; independent verification remains required")
    result={"schema_version":"3.0","generated_at":datetime.now(timezone.utc).isoformat(),
            "mode":"supreme-reasoning-consensus-supervisor","truth_claim":False,"gate":gate,
            "reliability_index":score,
            "metrics":{"artifact_records":total,"source_coverage":source_coverage,"provenance_coverage":provenance_coverage,
                       "language_routing_health":language_health,"cross_manifest_conflict_health":conflict_health,
                       "structural_health":structural_health,"verification_reports":len(report_statuses),
                       "cross_manifest_conflicts":len(conflicts),"latency_ms":round((time.perf_counter()-started)*1000,2)},
            "status_counts":dict(status_counts),"errors":errors[:200],"warnings":warnings[:200],"conflicts":conflicts[:100],
            "next_actions":(["repair structural/provenance/source conflicts","rerun verification","keep publication blocked"]
                            if gate=="HOLD" else ["continue independent verification","monitor drift","publish only records whose verification policy permits publication"])}
    out=ROOT/"generated"/"supreme-reasoning-consensus-status.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return result

if __name__=="__main__": print(json.dumps(evaluate(),ensure_ascii=False,indent=2))
