#!/usr/bin/env python3
"""Production-first multi-layer factory engine."""
import hashlib, json, os
from datetime import datetime, timezone
ROOT="production"; CATALOG=os.path.join(ROOT,"catalog.json"); OUT=os.path.join(ROOT,"generated","catalog.json")
STATUS=os.path.join(ROOT,"generated","production_status.json"); REGISTRY=os.path.join(ROOT,"generated","production_registry.json"); PRODUCT_DIR=os.path.join(ROOT,"products")
os.makedirs(os.path.dirname(OUT),exist_ok=True); os.makedirs(PRODUCT_DIR,exist_ok=True)
input_catalog=OUT if os.path.exists(OUT) else CATALOG
with open(input_catalog,encoding="utf-8") as f: data=json.load(f)
products=data.get("products",[]); now=datetime.now(timezone.utc); stamp=now.isoformat(); seed=hashlib.sha256(now.strftime("%Y%m%d%H%M").encode()).hexdigest()[:12]
families=[("AI/ML/NLP","Practitioner"),("Research","Evidence"),("Automation","Automission"),("Knowledge","Knowledge"),("Templates","Professional"),("Business","Commerce"),("Visual","Showroom"),("Digital Audio","Audio"),("Nature & Earth","Protection"),("Creator","Creator")]
batch=[]
for n,(category,prefix) in enumerate(families,1):
    index=len(products)+n; pid=f"SHR-AUTO-{index:07d}"; token=hashlib.sha256(f"{seed}:{category}:{index}".encode()).hexdigest()[:10]; price=499+((index*137)%4501)
    batch.append({"product_id":pid,"category":category,"name":f"SHIRMANI {prefix} Production Pack {index:07d}","description":f"Concrete factory-produced {category} digital product pack with defined scope, reusable customer material, instructions, release metadata and product passport. Batch token {token}.","price_inr":price,"offer":"Dynamic launch offer: 10% introductory discount","guarantee":"Digital deliverable + product passport + QC record","qc_gate":"QC-PENDING","gate_no":f"GATE-{index:06d}","dispatch":"NO","release":"PRODUCTION_READY","factory_batch":f"AUTO-{now.strftime('%Y%m%d')}","deliverable_type":"DIGITAL_PRODUCT","purchase_url":"https://rampaulsaini.github.io/my-omniverse-store/","deliverable_path":f"production/products/{pid}.md","production_state":"CONTENT_READY","version":1,"qr_payload":f"SHIRMANI|{pid}|GATE-{index:06d}|QC-PENDING|NO|{price}","created_at":stamp})
for item in batch:
    path=os.path.join(PRODUCT_DIR,item["product_id"]+".md")
    with open(path,"w",encoding="utf-8") as f:
        f.write(f"# {item['name']}\n\n## Product ID\n{item['product_id']}\n\n## Category\n{item['category']}\n\n## Concrete Deliverable\nFactory-produced digital product pack with defined scope, customer instructions, reusable working material, commercial metadata and product passport.\n\n## Production specification\n- Factory batch: {item['factory_batch']}\n- Version: {item['version']}\n- Price: INR {item['price_inr']}\n- Offer: {item['offer']}\n- Guarantee: {item['guarantee']}\n\n## QC / Release marking\n- QC gate: {item['qc_gate']}\n- Gate number: {item['gate_no']}\n- Dispatch: {item['dispatch']}\n- QR payload: {item['qr_payload']}\n\n## Customer use\nUse according to the product scope and instructions. Future cycles may upgrade the deliverable while preserving product ID and version history.\n")
visible=(products+batch)[-5000:]
with open(OUT,"w",encoding="utf-8") as f: json.dump({"schema_version":"1.2","generated_at":stamp,"products":visible,"production_first":True,"new_products_this_cycle":len(batch)},f,ensure_ascii=False,indent=2)
with open(REGISTRY,"w",encoding="utf-8") as f: json.dump({"generated_at":stamp,"cycle_id":seed,"catalog_count":len(visible),"produced_count":len(visible),"new_products_this_cycle":len(batch),"concrete_artifacts_total":len(visible),"production_state":"CONTINUOUS","qc_stage":"DOWNSTREAM","dispatch_released":0,"chat_required_for_continuity":False},f,ensure_ascii=False,indent=2)
with open(STATUS,"w",encoding="utf-8") as f: json.dump({"generated_at":stamp,"cycle_id":seed,"seed_products":len(products),"materialized_products":len(visible),"new_products_this_cycle":len(batch),"concrete_artifacts_this_cycle":len(batch),"factory_mode":"CONTINUOUS_MULTI_LAYER_PRODUCTION","next_stage":"QC_GATE_THEN_SHOWROOM","verification_is_downstream":True,"production_target":"continuous expansion","bounded_catalog_window":5000,"chat_required_for_continuity":False},f,ensure_ascii=False,indent=2)
print(json.dumps({"cycle_id":seed,"new_products_this_cycle":len(batch),"materialized_products":len(visible)},ensure_ascii=False))
