#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OVERLAY=ROOT/"generated/concrete-production-overlay.json"
OUT=ROOT/"generated/global-product-directory"
SHARD_SIZE=500
def load(p):
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding="utf-8"))
    except Exception: return {}
def main():
    catalog=load(CAT).get("products",[])
    overlay=load(OVERLAY)
    concrete={str(x.get("id")):x for x in overlay.get("products",[]) if x.get("id")}
    OUT.mkdir(parents=True,exist_ok=True); rows=[]
    for p in catalog:
        pid=str(p.get("id","")).strip()
        if not pid: continue
        c=concrete.get(pid,{})
        official=p.get("official_url") or p.get("company_url") or p.get("source_url") or None
        rows.append({"product_id":pid,"name":p.get("name") or pid,"category":p.get("category") or p.get("family") or "Digital Product","family":p.get("family"),"engine":p.get("engine"),"short_description":p.get("short_description") or p.get("description") or "Customer-facing digital product.","use_case":p.get("use_case") or p.get("usage") or "See product demo and usage guide.","price_inr":p.get("offer_price_inr",p.get("price_inr")),"offer":p.get("offer"),"concrete_artifact":bool(c),"artifact_route":c.get("artifact_url") or c.get("public_result_route") or p.get("artifact_url"),"visual_route":f"products/visuals/{pid.lower()}.svg","demo_route":f"product-demo.html?id={pid}","mp4_route":f"products/demos/products/{pid.lower()}.mp4","vip_screenshot_route":f"products/demos/vip/{pid.lower()}.svg","passport_route":f"product-passport.html?id={pid}","official_link":official,"official_link_state":"MAPPED_FROM_SOURCE" if official else "NOT_SUPPLIED","outreach_state":"QUEUED_NOT_SENT","dispatch_state":c.get("dispatch") or "NOT_RELEASED"})
    shards=[]
    for i in range(0,len(rows),SHARD_SIZE):
        chunk=rows[i:i+SHARD_SIZE]; n=i//SHARD_SIZE+1; name=f"shard-{n:04d}.json"
        (OUT/name).write_text(json.dumps({"schema_version":1,"shard":n,"products":chunk},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        shards.append({"shard":n,"path":f"generated/global-product-directory/{name}","count":len(chunk)})
    concrete=sum(x["concrete_artifact"] for x in rows); official=sum(bool(x["official_link"]) for x in rows)
    idx={"schema_version":1,"generated_at_utc":datetime.now(timezone.utc).isoformat(),"source_catalog":"generated/1000-digital-products.json","source_overlay":"generated/concrete-production-overlay.json","current_catalog_identities":len(rows),"concrete_artifacts_mapped":concrete,"official_links_mapped":official,"official_links_missing":len(rows)-official,"shard_size":SHARD_SIZE,"shard_count":len(shards),"scale_targets":{"current":5000,"long_term":150000},"outreach_policy":"QUEUE_ONLY_UNTIL_AN_AUTHORIZED_EXTERNAL_CHANNEL_EXISTS","truth_boundary":"Catalog identity, workflow run, generated visual, demo or QC state is not by itself a sale or independent scientific verification.","shards":shards}
    (OUT/"index.json").write_text(json.dumps(idx,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog":len(rows),"concrete":concrete,"shards":len(shards),"official_links":official},ensure_ascii=False))
if __name__=="__main__": main()
