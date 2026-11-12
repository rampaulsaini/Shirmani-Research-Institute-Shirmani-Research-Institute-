#!/usr/bin/env python3
"""Product-first multi-lane production fabric. Verification is downstream."""
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; CFG=ROOT/"factory/production-lanes.json"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--batch-size",type=int,default=2500); a=ap.parse_args()
    c=json.loads(CFG.read_text(encoding="utf-8")); src=OUT/"source-units.jsonl"
    if not src.exists(): raise SystemExit("source-units.jsonl required")
    sources=[json.loads(x) for x in src.read_text(encoding="utf-8").splitlines() if x.strip()]
    lanes=c["lanes"]; cur=int(c.get("cursor",0)); stamp=datetime.now(timezone.utc).isoformat()
    rows=[]; slots=min(max(1,a.batch_size),len(sources)*len(lanes))
    for off in range(slots):
        lane=lanes[(cur+off)%len(lanes)]; s=sources[(cur+off)%len(sources)]
        action=lane["actions"][off%len(lane["actions"])]; sid=str(s.get("id"))
        tid=hashlib.sha256(f'{lane["id"]}|{sid}|{action}'.encode()).hexdigest()[:20]
        rows.append({"task_id":tid,"lane":lane["id"],"discipline":lane["discipline"],"task_type":action,
          "source_id":sid,"source_repository":s.get("repository"),"source_path":s.get("path"),
          "source_hash":s.get("source_hash"),"output_contract":lane["output_contract"],
          "status":"PRODUCTION_GENERATED","verification":{"status":"DOWNSTREAM","independent_verification":False},
          "routing":{"mode":"multi-layer-automission","compute":"deterministic-first",
                     "optional_acceleration":"NVIDIA_API_KEY","quantum_mode":"quantum-inspired scheduling only"},
          "created_at":stamp})
    out=OUT/"production-lane-results.jsonl"; seen=set()
    if out.exists():
        for x in out.read_text(encoding="utf-8").splitlines():
            if x.strip():
                try: seen.add(json.loads(x)["task_id"])
                except Exception: pass
    new=[r for r in rows if r["task_id"] not in seen]
    with out.open("a",encoding="utf-8") as f:
        for r in new: f.write(json.dumps(r,ensure_ascii=False)+"\n")
    total=sum(1 for x in out.open(encoding="utf-8") if x.strip())
    counts={l["id"]:0 for l in lanes}
    for r in new: counts[r["lane"]]+=1
    status={"generated_at":stamp,"architecture":"product-first multi-layer AI/ML/NLP production fabric",
      "cycle_batch_requested":a.batch_size,"cycle_new_tasks":len(new),"cycle_duplicates":len(rows)-len(new),
      "cumulative_production_tasks":total,"lanes":[{"id":l["id"],"discipline":l["discipline"]} for l in lanes],
      "cycle_distribution":counts,"production_role":"primary",
      "verification_role":"downstream quality/evidence telemetry",
      "quantum_statement":"Quantum-inspired scheduling label only; no claim of quantum hardware execution.",
      "source_of_truth":"generated/production-lane-results.jsonl"}
    (OUT/"PRODUCTION-FABRIC-STATUS.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    c["cursor"]=cur+slots; CFG.write_text(json.dumps(c,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
