#!/usr/bin/env python3
"""Build the four-stage product pipeline board from the catalogue."""
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/"showroom/data/catalog.json").read_text(encoding="utf-8"))
board={"schemaVersion":"1.0.0","generatedAt":datetime.now(timezone.utc).isoformat(),"stages":[
{"id":"institute","name":"Research Institute","purpose":"Define user problem, scope, differentiator, and audience."},
{"id":"factory","name":"Product Factory","purpose":"Create specification, passport, usage guide, and demo plan."},
{"id":"qc","name":"Quality Control","purpose":"Check fields, claims, pricing, guide/demo, and release readiness."},
{"id":"showroom","name":"Public Showroom","purpose":"Publish discoverable cards with accurate readiness labels."}],
"counts":{"catalogueEntries":len(catalog["products"]),"specification":0,"prototype":0,"productionReady":0,"demoPublished":0,"priced":0},"products":[]}
for p in catalog["products"]:
 r=p.get("readiness","Unspecified")
 if r=="Specification": board["counts"]["specification"]+=1
 if r.startswith("Prototype"): board["counts"]["prototype"]+=1
 if r=="Production-ready": board["counts"]["productionReady"]+=1
 if p.get("demo"): board["counts"]["demoPublished"]+=1
 if p.get("price") is not None: board["counts"]["priced"]+=1
 board["products"].append({"id":p["id"],"name":p["name"],"currentStage":"factory-specification","pipeline":["institute","factory","qc","showroom"],"qc":{"requiredFieldsPresent":all(p.get(k) for k in ("id","name","category","description","readiness")),"guideLinked":bool(p.get("guide")),"demoPublished":bool(p.get("demo")),"priceConfigured":p.get("price") is not None,"releaseEligible":False,"reason":"Functional implementation, tests, product-specific demo, support terms, and release review are still required."},"nextAction":"Implement and test the actual tool; publish a product-specific demo and usage guide."})
out=ROOT/"showroom/data/production-board.json";out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(board,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Production board built for {len(board['products'])} products; production-ready={board['counts']['productionReady']}")
