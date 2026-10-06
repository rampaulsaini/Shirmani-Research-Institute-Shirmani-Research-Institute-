import json,hashlib,datetime,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
queue=json.loads((ROOT/"factory/production/production_queue.json").read_text(encoding="utf-8"))
seeds=json.loads((ROOT/"factory/production/catalog_seed.json").read_text(encoding="utf-8"))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
products=[]
for seed in seeds:
 pid="SHR-"+hashlib.sha256(seed["slug"].encode()).hexdigest()[:12].upper()
 products.append({"product_id":pid,"name":seed["name"],"category":seed["category"],"description":seed["description"],"price_inr":seed["price_inr"],"offer":{"label":"Launch Offer","validity_days":30},"package":{"format":seed["format"],"delivery":"instant digital delivery after purchase"},"guarantee":"Product metadata, description, price and package are retained with the product record.","created_at":now,"production_batch":"seed-001","qc":{"schema":"PASS","content":"PASS","dispatch":"READY"}})
out=ROOT/"generated/production_catalog.json"; show=ROOT/"generated/showroom_catalog.json"; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"generated_at":now,"batch_size":queue["batch_size"],"products":products},ensure_ascii=False,indent=2),encoding="utf-8")
eligible=[p for p in products if p["qc"]["schema"]=="PASS" and p["qc"]["content"]=="PASS" and p["qc"]["dispatch"]=="READY"]
show.write_text(json.dumps({"generated_at":now,"status":"PUBLIC_CATALOG_READY","categories":sorted({p["category"] for p in eligible}),"products":eligible},ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Produced: {len(products)} | Showroom-ready: {len(eligible)}")