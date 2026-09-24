import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
research_src=ROOT/"generated"/"research-queue.jsonl"
source_src=ROOT/"generated"/"source-units.jsonl"
out=ROOT/"generated"/"product-queue.jsonl"
rows=[]
if research_src.exists():
    input_rows=[json.loads(line) for line in research_src.read_text(encoding="utf-8").splitlines() if line.strip()]
    for i,r in enumerate(input_rows,1):
        rows.append({"product_id":f"P{i:06d}","research_id":r["research_id"],"title":f"Research-derived digital product {i:06d}","formats":["mahagranth","verse","paper","audio-script"],"source":r["source"],"buyer_benefit":"source-grounded digital content access","price":None,"currency":"INR","status":"draft","draft_only":True,"provenance_required":True,"verification_required":True,"human_review_required":True})
else:
    # The factory currently emits source-units.jsonl, not research-queue.jsonl.
    # Use those canonical-derived units as the product discovery input while
    # preserving research_id compatibility for downstream consumers.
    input_rows=[json.loads(line) for line in source_src.read_text(encoding="utf-8").splitlines() if line.strip()] if source_src.exists() else []
    for i,r in enumerate(input_rows,1):
        source = f"{r.get('repository','unknown')}:{r.get('path','unknown')}"
        rows.append({"product_id":f"P{i:06d}","research_id":f"S{i:06d}","title":f"Research-derived digital product {i:06d}","formats":["mahagranth","verse","paper","audio-script"],"source":source,"buyer_benefit":"source-grounded digital content access","price":None,"currency":"INR","status":"draft","draft_only":True,"provenance_required":True,"verification_required":True,"human_review_required":True})
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
