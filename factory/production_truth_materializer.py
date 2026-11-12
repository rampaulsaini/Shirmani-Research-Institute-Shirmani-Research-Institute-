#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
src=json.loads((ROOT/"factory/production_truth_registry.json").read_text(encoding="utf-8"))
out=ROOT/"generated"; out.mkdir(exist_ok=True)
rows=[]
for o in src["offers"]:
    r=dict(o)
    if o.get("evidence_path"):
        p=ROOT/o["evidence_path"]
        if o["id"]=="P007":
            r["evidence_present"]=p.exists() and any(p.glob("certificate-*.md"))
        else:
            r["evidence_present"]=p.exists() and p.is_file() and p.stat().st_size>0
    else:
        r["evidence_present"]=False
    rows.append(r)
delivery_ready=sum(1 for r in rows if r["status"]=="DELIVERY_ASSET_EXISTS" and r.get("evidence_present"))
blocked=sum(1 for r in rows if r["status"]=="BLOCKED_ASSET_REQUIRED")
inquiry=sum(1 for r in rows if r["status"]=="INQUIRY_READY")
payload={"generated_at":datetime.now(timezone.utc).isoformat(),"principle":"REAL_PRODUCTION_ONLY","offer_count":len(rows),"delivery_ready_assets":delivery_ready,"inquiry_ready_services":inquiry,"blocked_missing_assets":blocked,"sales_claim":False,"income_claim":False,"workflow_run_is_product":False,"offers":rows,"next_gate":"No paid digital product may be labeled DELIVERY_READY until the actual deliverable asset and delivery path are evidenced."}
(out/"production-truth.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"
",encoding="utf-8")
badges={"DELIVERY_ASSET_EXISTS":"DELIVERY ASSET EXISTS","INQUIRY_READY":"INQUIRY READY","BLOCKED_ASSET_REQUIRED":"BLOCKED — ASSET REQUIRED"}
cards=[]
for r in rows:
    state=badges[r["status"]]
    detail="Actual repository delivery evidence is present." if r.get("evidence_present") else r.get("required_evidence","External evidence required.")
    cards.append("<article><small>"+r["id"]+" · "+r["type"]+"</small><h2>"+r["name"]+"</h2><strong>"+state+"</strong><p>"+detail+"</p></article>")
page="<!doctype html><html lang='hi'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>SHIRMANI Production Truth</title><style>body{margin:0;background:#080b11;color:#eef2f7;font-family:system-ui,sans-serif;line-height:1.5}main{max-width:1200px;margin:auto;padding:24px}h1,h2{color:#d4af37}.hero,article{background:#111827;border:1px solid #334155;border-radius:16px;padding:18px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin-top:14px}small{color:#67e8f9}strong{color:#6ee7b7}.warn{color:#fbbf24}a{color:#67e8f9}</style></head><body><main><section class='hero'><h1>꙰ SHIRMANI — Production Truth</h1><p><b>यह dashboard workflow runs को products नहीं मानता।</b> केवल वास्तविक delivery evidence को DELIVERY ASSET EXISTS माना जाता है।</p><p><b>"+delivery_ready+"</b> delivery-asset products · <b>"+inquiry+"</b> inquiry-ready services · <b>"+blocked+"</b> products blocked for missing assets.</p><p><a href='../products.html'>Product Catalog</a> · <a href='production-results.jsonl'>Production Results</a> · <a href='production-truth.json'>Machine-readable truth</a></p></section><div class='grid'>"+cards.join("")+"</div><section class='hero' style='margin-top:16px'><h2>मुख्य नियम</h2><p>Automation → production card → actual deliverable → delivery path → delivery evidence → customer transaction → audit.</p><p class='warn'>Internal Automission output is useful infrastructure, but it is not a customer sale or completed product by itself.</p></section></main></body></html>"
(out/"production-truth.html").write_text(page,encoding="utf-8")
print(json.dumps({"delivery_ready":delivery_ready,"inquiry_ready":inquiry,"blocked":blocked},ensure_ascii=False))
