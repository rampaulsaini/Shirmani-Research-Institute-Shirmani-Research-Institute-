#!/usr/bin/env python3
"""Measure SHIRMANI product progress without inflating completion claims."""
from pathlib import Path
import json, re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
TARGET=5000
CAT_TARGET=150000
OUT=ROOT/"generated/product-scale-audit.json"

def load_rows():
    candidates=[
        ROOT/"generated/1000-digital-products.json",
        ROOT/"generated/production-registry.json",
        ROOT/"generated/concrete-production-overlay.json",
    ]
    for p in candidates:
        if not p.exists():
            continue
        try:
            d=json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        rows=d.get("products",[])
        if rows:
            return rows,p
    return [],None

def exists_for(pid, rel):
    return (ROOT/rel.format(pid=str(pid).lower())).exists()

rows,source=load_rows()
ids=[str(x.get("id","")).strip() for x in rows if str(x.get("id","")).strip()]
ids=list(dict.fromkeys(ids))
real_mp4=sum(exists_for(pid,"products/demos/products/{pid}.mp4") for pid in ids)
visual=sum(exists_for(pid,"products/visuals/{pid}.svg") for pid in ids)
vip=sum(exists_for(pid,"products/demos/vip/{pid}.svg") for pid in ids)

result={
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "catalogue_source":str(source.relative_to(ROOT)) if source else None,
    "concrete_product_records":len(ids),
    "target_products":TARGET,
    "product_record_progress_percent":round(min(100,len(ids)/TARGET*100),2),
    "remaining_product_records":max(0,TARGET-len(ids)),
    "real_product_specific_mp4":real_mp4,
    "real_product_specific_mp4_progress_percent":round(min(100,real_mp4/TARGET*100),2),
    "visual_assets":visual,
    "vip_passports":vip,
    "catalogue_target_records":CAT_TARGET,
    "catalogue_headroom_records":max(0,CAT_TARGET-len(ids)),
    "shard_count":1000,
    "shard_rule":"numeric(product_id) mod 1000",
    "truth_rule":"records and assets are counted independently; no synthetic completion inflation"
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
