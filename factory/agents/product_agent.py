import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"research-queue.jsonl"; out=ROOT/"generated"/"product-queue.jsonl"
rows=[]
if src.exists():
    for i,line in enumerate(src.read_text(encoding="utf-8").splitlines(),1):
        r=json.loads(line)
        rows.append({"product_id":f"P{i:06d}","research_id":r["research_id"],"title":f"Research-derived digital product {i:06d}","formats":["mahagranth","verse","paper","audio-script"],"source":r["source"],"buyer_benefit":"source-grounded digital content access","price":None,"currency":"INR","status":"draft","draft_only":True,"provenance_required":True,"verification_required":True,"human_review_required":True})
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
# A separate catalog keeps generated product discovery machine-readable without
# implying that drafts are published, priced, sold, or independently verified.
catalog = ROOT/"generated"/"product-catalog.json"
catalog.write_text(json.dumps({
    "schema_version": "1.0",
    "generated_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
    "status": "draft_catalog",
    "truth_boundary": "drafts require provenance, verification and publication review before sale",
    "products": rows
}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print("product-agent:",len(rows),"catalog:",catalog)
