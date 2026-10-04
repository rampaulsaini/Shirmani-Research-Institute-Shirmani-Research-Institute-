#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
intake=json.loads((ROOT/"federation/research-paper-source-intake.json").read_text())
registry=json.loads((OUT/"research-paper-claims.json").read_text())
if intake["verification_status"]!="UNVERIFIED": raise SystemExit("Research Paper must remain UNVERIFIED")
target=OUT/"claim-evidence.jsonl"
rows=[json.loads(x) for x in target.read_text().splitlines() if x.strip()] if target.exists() else []
by_id={str(r.get("id")):r for r in rows}
for c in registry["claims"]:
    cid="claim:research-paper:"+c["id"]
    r=by_id.get(cid)
    if r:
        v=r.get("verification") or {}
        if v.get("status") not in ("NOT_VERIFIED","UNVERIFIED") or v.get("independent") is not False:
            raise SystemExit("Unsafe Research Paper verification state: "+cid)
        r["evidence"] = r.get("evidence") or [{"kind":"AUTHOR_DECLARATION","status":"SOURCE_TRACE","detail":"Author-declared proposition; traceability metadata only."}]
    else:
        by_id[cid]={"id":cid,"claim":c["claim"],"claim_category":c["category"],
          "artifact_type":"RESEARCH_PAPER","artifact_id":c["id"],
          "source_traceability":{"source_ids":[intake["source_id"]],"repository":intake["repository"],
          "ref":intake["ref"],"entrypoint":intake["public_entrypoint"]},
          "evidence":[{"kind":"AUTHOR_DECLARATION","status":"SOURCE_TRACE","detail":"Author-declared proposition; traceability metadata only."}],"verification":{"status":"NOT_VERIFIED","independent":False,
          "independent_verification_required":True,"independent_replication":False},
          "verification_questions":c["evidence_required"],
          "provenance":"AUTHOR_DECLARED_RESEARCH_PAPER"}
target.write_text("\n".join(json.dumps(by_id[k],ensure_ascii=False,sort_keys=True) for k in sorted(by_id))+"\n")
print("Research Paper adapter v2: PASS")
