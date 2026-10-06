#!/usr/bin/env python3
from __future__ import annotations
import json, os, html, hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"generated/1000-digital-products.json"
FALLBACK=ROOT/"showroom-products.json"
OUT=ROOT/"products"/"production"
MANIFEST=ROOT/"generated/production-manifest.json"
STATUS=ROOT/"generated/production-progress.json"
BATCH=int(os.getenv("PRODUCTION_BATCH_SIZE","100"))
TARGET=int(os.getenv("PRODUCTION_TARGET","5000"))

def load_products():
    src=SOURCE if SOURCE.exists() else FALLBACK
    data=json.loads(src.read_text(encoding="utf-8"))
    return data.get("products", data if isinstance(data,list) else [])

def product_page(p):
    pid=str(p.get("id","PRODUCT")).strip()
    name=html.escape(str(p.get("name","Digital Product")))
    desc=html.escape(str(p.get("description") or p.get("engine") or "Customer-visible digital product artifact."))
    family=html.escape(str(p.get("family") or p.get("category") or "Digital"))
    price=p.get("price_inr", p.get("offer_price_inr", 0))
    try: price_text="FREE" if float(price or 0)==0 else "₹"+f"{int(float(price)):,}"
    except Exception: price_text="Rate on request"
    offer=html.escape(str(p.get("offer") or "Current public catalogue offer"))
    digest=hashlib.sha256(json.dumps(p,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:16]
    return f'''<!doctype html>
<html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}"><title>{name} · SHIRMANI Product</title>
<style>body{{margin:0;background:#070910;color:#f5f7fb;font:16px/1.65 system-ui,sans-serif}}main{{max-width:900px;margin:auto;padding:28px}}.card{{background:#101521;border:1px solid #273244;border-radius:18px;padding:24px;margin:16px 0}}h1,h2{{color:#e5c35b}}.tag{{color:#64d9ff;font-weight:800}}.price{{font-size:2rem;font-weight:900;color:#e5c35b}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}}.meta{{background:#0b1019;border:1px solid #273244;border-radius:10px;padding:12px}}a{{color:#64d9ff}}.cta{{display:inline-block;padding:11px 15px;border-radius:10px;background:#e5c35b;color:#111;text-decoration:none;font-weight:900}}</style></head><body><main>
<div class="tag">꙰ SHIRMANI RESEARCH INSTITUTE · CONCRETE PRODUCTION ARTIFACT</div>
<section class="card"><h1>{name}</h1><p>{desc}</p><p class="price">{price_text}</p><p><strong>Offer:</strong> {offer}</p></section>
<section class="card"><h2>Product passport</h2><div class="grid">
<div class="meta"><small>Product ID</small><br><strong>{html.escape(pid)}</strong></div><div class="meta"><small>Category</small><br><strong>{family}</strong></div>
<div class="meta"><small>Production state</small><br><strong>CONCRETE / PUBLIC</strong></div><div class="meta"><small>QC Gate</small><br><strong>QC-ARTIFACT</strong></div>
<div class="meta"><small>Dispatch</small><br><strong>NO — order/fulfilment is separate</strong></div><div class="meta"><small>Artifact fingerprint</small><br><strong>{digest}</strong></div>
</div></section>
<section class="card"><h2>Use / order</h2><p>This is the concrete customer-facing production artifact for the registered catalogue identity. Payment and fulfilment are separate states.</p>
<p><a class="cta" href="../../product-order.html?id={html.escape(pid)}">Order / request</a> &nbsp; <a href="../../showroom.html">Back to showroom</a></p></section>
<section class="card"><h2>Quality improvement</h2><p>Customer reviews, ratings and actionable feedback are production-improvement inputs. They are not scientific verification.</p></section>
</main></body></html>'''

def main():
    products=load_products()
    OUT.mkdir(parents=True,exist_ok=True)
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"schema_version":"1.0","products":[]}
    done={x["id"]:x for x in manifest.get("products",[]) if x.get("id")}
    ids=[str(p.get("id","")).strip() for p in products if p.get("id")]
    eligible=[p for p in products if p.get("id") and str(p["id"]) not in done]
    batch=eligible[:max(0,BATCH)]
    now=datetime.now(timezone.utc).isoformat()
    for p in batch:
        pid=str(p["id"]); path=OUT/f"{pid}.html"; path.write_text(product_page(p),encoding="utf-8")
        done[pid]={"id":pid,"path":str(path.relative_to(ROOT)).replace("\\","/"),"state":"CONCRETE_PUBLIC","qc_code":"QC-ARTIFACT","dispatch_state":"NO","generated_at":now}
    records=sorted(done.values(),key=lambda x:x["id"])
    MANIFEST.parent.mkdir(parents=True,exist_ok=True)
    MANIFEST.write_text(json.dumps({"schema_version":"1.0","generated_at":now,"source_count":len(ids),"concrete_public_count":len(records),"target":TARGET,"products":records},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    STATUS.write_text(json.dumps({"schema_version":"1.0","generated_at":now,"source_count":len(ids),"concrete_public_count":len(records),"remaining_source_products":max(0,len(ids)-len(records)),"target":TARGET,"batch_size":BATCH,"cycle_materialized":len(batch),"production_complete_for_source":len(records)>=len(ids),"target_complete":len(records)>=TARGET,"principle":"Production output is separate from independent scientific verification."},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"cycle_materialized":len(batch),"concrete_public_count":len(records),"source_count":len(ids)},ensure_ascii=False))

if __name__=="__main__":
    main()
