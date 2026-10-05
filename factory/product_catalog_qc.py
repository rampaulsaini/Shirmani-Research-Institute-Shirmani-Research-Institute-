import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"products"/"product-catalog.json"

def main():
    if not CATALOG.is_file(): raise SystemExit("PRODUCT_CATALOG_MISSING")
    data=json.loads(CATALOG.read_text(encoding="utf-8"))
    for k in ("schema_version","catalog_id","status","products","pipeline"):
        if k not in data: raise SystemExit("PRODUCT_CATALOG_MISSING_FIELD:"+k)
    products=data["products"]
    if not products: raise SystemExit("PRODUCT_CATALOG_EMPTY")
    ids=set()
    for p in products:
        for k in ("product_id","title_hi","type","price_inr","listing_state","verification_state"):
            if k not in p: raise SystemExit(f"PRODUCT_MISSING_FIELD:{p.get('product_id','unknown')}:{k}")
        if p["product_id"] in ids: raise SystemExit("DUPLICATE_PRODUCT_ID:"+p["product_id"])
        ids.add(p["product_id"])
        if not isinstance(p["price_inr"],(int,float)) or p["price_inr"]<0:
            raise SystemExit("INVALID_PRICE:"+p["product_id"])
        if p["verification_state"] not in {"NOT_VERIFIED","VERIFIED"}:
            raise SystemExit("INVALID_VERIFICATION_STATE:"+p["product_id"])
    print(json.dumps({"status":"PASS","catalog_id":data["catalog_id"],"product_count":len(products),"rule":"catalog readiness is not sales, payment or independent verification"},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
