#!/usr/bin/env python3
"""Build a production-first queue from the repository's existing public product registries."""
from __future__ import annotations
import json,re
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; OUT.mkdir(exist_ok=True)
def products():
    for p in [OUT/"1000-digital-products.json",OUT/"PRODUCT-PASSPORTS.json",OUT/"PRODUCT-PASSPORTS.jsonl"]:
        if not p.exists(): continue
        if p.suffix==".jsonl":
            rows=[]
            for line in p.read_text(encoding="utf-8").splitlines():
                try: rows.append(json.loads(line))
                except Exception: pass
            if rows:return rows
        try:d=json.loads(p.read_text(encoding="utf-8"))
        except Exception:continue
        if isinstance(d,dict) and isinstance(d.get("products"),list):return d["products"]
        if isinstance(d,list):return d
    return []
def norm(s):return re.sub(r"[^a-z0-9._-]+","-",str(s or "").lower()).strip("-")
def has_asset(pid,kind):
    stem=norm(pid)
    if kind=="passport": return (ROOT/"product-passport.html").exists()
    roots={"visual":[ROOT/"products"/"visuals",ROOT/"assets"/"products"],
           "vip":[ROOT/"products"/"vip-screenshots"],
           "demo":[ROOT/"products"/"demos",ROOT/"assets"/"demos"],
           "mp4":[ROOT/"products"/"mp4",ROOT/"assets"/"mp4",ROOT/"media"]}[kind]
    for r in roots:
        if not r.is_dir():continue
        for ext in ("png","jpg","jpeg","webp","svg","mp4","webm","html","json"):
            if (r/f"{stem}.{ext}").exists():return True
    return False
rows=[];counts={}
for p in products():
    pid=str(p.get("id") or p.get("product_id") or "")
    if not pid:continue
    gaps=[]
    for kind,label in [("visual","4K_VISUAL"),("demo","DEMO_ROUTE"),("mp4","PRODUCT_MP4"),("vip","VIP_SCREENSHOT")]:
        if not has_asset(pid,kind):gaps.append(label)
    if not p.get("short_description") and not p.get("description"):gaps.append("SHORT_DESCRIPTION")
    if not (p.get("price_inr") or p.get("offer_price_inr")):gaps.append("PRICE")
    if not p.get("qc_code"):gaps.append("QC_CODE")
    if not p.get("gate_no"):gaps.append("GATE_NO")
    for g in gaps:counts[g]=counts.get(g,0)+1
    rows.append({"id":pid,"name":p.get("name") or pid,"family":p.get("family"),"engine":p.get("engine"),
                 "production_state":p.get("production_state","QUEUED"),"sale_state":p.get("sale_state","NOT_YET_PRODUCED"),
                 "gaps":gaps,"priority":len(gaps)})
rows.sort(key=lambda x:(-x["priority"],x["id"]))
stamp=datetime.now(timezone.utc).isoformat()
manifest={"schema_version":"production-first-conveyor.v1","generated_at":stamp,"catalog_identities":len(rows),
          "fully_gap_free_records":sum(not r["gaps"] for r in rows),"records_with_production_gaps":sum(bool(r["gaps"]) for r in rows),
          "gap_counts":counts,"queue":rows[:5000],"principle":"Production first: workflow execution is not counted as a product."}
state={"generated_at":stamp,"catalog_identities":len(rows),
       "production_gap_records":manifest["records_with_production_gaps"],
       "fully_gap_free_records":manifest["fully_gap_free_records"],
       "top_gap":max(counts,key=counts.get) if counts else None,
       "top_gap_count":max(counts.values()) if counts else 0}
manifest_path=OUT/"production-first-conveyor.json"
state_path=OUT/"production-first-state.json"
def same_payload(path,current):
    try:
        previous=json.loads(path.read_text(encoding="utf-8"))
    except (OSError,ValueError):
        return False,None
    previous_payload={k:v for k,v in previous.items() if k!="generated_at"}
    current_payload={k:v for k,v in current.items() if k!="generated_at"}
    return previous_payload==current_payload,previous.get("generated_at")
manifest_same,previous_stamp=same_payload(manifest_path,manifest)
state_same,_=same_payload(state_path,state)
# Keep generated_at stable when only the clock changed. This prevents a scheduled
# run from creating a telemetry-only commit every five minutes.
if manifest_same and state_same and previous_stamp:
    stamp=previous_stamp
    manifest["generated_at"]=stamp
    state["generated_at"]=stamp
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
print(json.dumps(manifest["gap_counts"],ensure_ascii=False))
