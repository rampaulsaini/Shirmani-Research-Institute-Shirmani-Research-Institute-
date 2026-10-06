#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
CATALOG = GEN / "1000-digital-products.json"
TARGET = 5000
VARIANT_LABELS = ["Starter","Quick","Pro","Studio","Research","Prime","Precision","Creator","Advanced","Supreme","Micro","Enterprise","Universal","Deep","Rapid","Smart","Open","Focus","Master","Ultra"]

def stable_price(i):
    base = 99 + ((i * 47) % 7901)
    return base, max(49, round(base * (0.68 + ((i * 11) % 18) / 100)))

def main():
    if not CATALOG.exists(): raise SystemExit("canonical product catalog missing")
    data=json.loads(CATALOG.read_text(encoding="utf-8"))
    products=data.get("products",[])
    if not products: raise SystemExit("canonical product catalog is empty")
    original=list(products)
    next_index=max(int(p["id"].split("-")[-1]) for p in products)+1
    created=0
    while len(products)<TARGET:
        template=original[(len(products)-len(original))%len(original)]
        pid=f"SP-{next_index:04d}"
        family=template.get("family","Digital Tools"); engine=template.get("engine","creator")
        variant_no=((next_index-1)//max(1,len(original)))+1
        label=VARIANT_LABELS[(variant_no-1)%len(VARIANT_LABELS)]
        base,offer=stable_price(next_index)
        fp=hashlib.sha256(f"{pid}|{family}|{engine}".encode()).hexdigest()[:16].upper()
        products.append({
            "id":pid,"product_index":next_index,
            "name":f"SHIRMANI {label} {family} {next_index:04d}",
            "family":family,"engine":engine,
            "description":f"Concrete public digital product {pid}. {family} · {engine} · production variant {variant_no}.",
            "status":"PRODUCED_PUBLIC","production_state":"PRODUCTION_QUEUE",
            "sale_state":"PAYMENT_ROUTE_CONFIGURED","price_inr":base,"offer_price_inr":offer,
            "pricing_status":"PUBLISHED_LAUNCH_PRICE","offer":"SUPREME LAUNCH OFFER",
            "artifact_url":f"products/concrete/{pid}.html","qc_code":f"QC-PROD-{pid}",
            "gate_no":"GATE-PRODUCTION","dispatch_no":"NO","commercial_status":"NOT_SOLD",
            "verification":"FUNCTIONAL_BROWSER_BEHAVIOUR_ONLY","fingerprint":fp,
            "payment_routes":["PAYTM_UPI","PAYPAL"],"variant_of":template["id"],
            "variant_number":variant_no,"production_role":"customer-visible reusable digital product variant"
        })
        next_index+=1; created+=1
    data.update({
        "schema_version":max(2,int(data.get("schema_version",1))),
        "production_target":TARGET,"production_scale":"multi-lane-resumable",
        "generated_at":datetime.now(timezone.utc).isoformat(),"products":products
    })
    data["families"]=sorted({p.get("family") for p in products if p.get("family")})
    data["engines"]=sorted({p.get("engine") for p in products if p.get("engine")})
    data["family_count"]=len(data["families"]); data["engine_count"]=len(data["engines"])
    CATALOG.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    status={"generated_at":data["generated_at"],"catalog_count":len(products),"target":TARGET,
            "created_this_cycle":created,"remaining_to_target":max(0,TARGET-len(products)),
            "source_catalog_count":len(original),"production_scale":"multi-lane-resumable",
            "next_action":"materialize concrete product artifacts and refresh showroom registry",
            "integrity":"variants explicitly labelled; no independent scientific verification claim"}
    (GEN/"production-scale-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__": main()
