#!/usr/bin/env python3
"""Canonical deterministic 5,000-product catalogue for production-first Automission.

Existing seed identities are preserved. Additional identities are deterministic
template expansions and remain CATALOG_ONLY until a real factory artifact exists.
"""
from __future__ import annotations
import json
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"generated/production-registry.json"
OVERLAY=ROOT/"generated/concrete-production-overlay.json"
TARGET=5000

def _seeds():
    data=json.loads(REGISTRY.read_text(encoding="utf-8"))
    rows=data.get("products",[])
    if not rows: raise SystemExit("production-registry.json has no seed products")
    return rows

def _overlay():
    if not OVERLAY.exists(): return set()
    try: data=json.loads(OVERLAY.read_text(encoding="utf-8"))
    except Exception: return set()
    return {str(x.get("id")) for x in data.get("products",[]) if x.get("id")}

def _normalize(base, idx, concrete):
    q=deepcopy(base); pid=f"SP-{idx:04d}"
    q["id"]=pid; q["catalog_identity"]=True; q["catalog_index"]=idx
    q["concrete_production"]=bool(concrete)
    q.setdefault("category",q.get("family","Digital Product"))
    q.setdefault("description",f"Customer-facing SHIRMANI digital product for {q.get('family','digital')} workflows.")
    q.setdefault("guarantee","Digital delivery subject to published product terms.")
    q.setdefault("packing","Digital Product Passport + Demo + Usage Guide")
    q.setdefault("offer","PUBLIC LAUNCH"); q.setdefault("price_inr",0)
    q.setdefault("offer_price_inr",q.get("price_inr",0))
    q.setdefault("qc_code",f"QC-CATALOG-{idx:04d}")
    q.setdefault("gate_no","GATE-PRODUCTION"); q.setdefault("dispatch_no","NO")
    q["artifact_url"]=q.get("artifact_url",f"products/production/{pid.lower()}.html")
    q["passport_url"]=f"product-passport.html?id={pid}"
    q["demo_route"]=f"product-demo.html?id={pid}"
    q["usage_route"]=f"product-usage.html?id={pid}"
    q["production_state"]="PRODUCED" if concrete else "CATALOG_ONLY"
    q["sale_state"]="READY_FOR_ORDER" if concrete else "QUEUED_FOR_PRODUCTION"
    return q

def load_catalog(target=TARGET):
    seeds=_seeds(); produced=_overlay(); out=[]
    for i in range(1,target+1):
        base=deepcopy(seeds[i-1]) if i<=len(seeds) else deepcopy(seeds[(i-1)%len(seeds)])
        if i>len(seeds):
            series=((i-1)//len(seeds))+1
            base["name"]=f"{base.get('name','SHIRMANI Product')} · Expansion {series} · {i:04d}"
            base["unit_no"]=f"5000.{i:04d}"
        out.append(_normalize(base,i,f"SP-{i:04d}" in produced))
    return out

def write_catalog(path=None):
    rows=load_catalog(); path=Path(path) if path else ROOT/"generated/canonical-5000-product-catalog.json"
    payload={"schema_version":1,"generated_at":"deterministic-runtime","catalog_target":TARGET,
             "catalog_count":len(rows),"concrete_count":sum(x["concrete_production"] for x in rows),
             "remaining_to_concrete_target":sum(not x["concrete_production"] for x in rows),
             "production_first":True,
             "truth_boundary":"CATALOG_ONLY is not a concrete product; concrete production requires a repository artifact.",
             "products":rows}
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return path,payload

if __name__=="__main__":
    p,payload=write_catalog()
    print(json.dumps({"path":str(p),"catalog_count":payload["catalog_count"],"concrete_count":payload["concrete_count"],"remaining":payload["remaining_to_concrete_target"]},ensure_ascii=False))
