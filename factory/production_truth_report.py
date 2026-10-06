#!/usr/bin/env python3
"""Canonical production-truth report for the SHIRMANI digital-product factory."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; CAT=GEN/"1000-digital-products.json"; OUT=GEN/"SHIRMANI-PRODUCTION-TRUTH.md"
catalog=json.loads(CAT.read_text(encoding="utf-8")); products=catalog.get("products",[])
assets=[p for p in products if (ROOT/p["asset"]).is_file()]
modules={p["module"] for p in products if (ROOT/p["module"]).is_file()}
ready=sum(p.get("status")=="READY_FOR_QC" for p in products); catalog_ready=sum(p.get("commercial_status")=="CATALOG_READY" for p in products); dispatch=sum(p.get("dispatch_no") not in (None,"","NO") for p in products)
lines=["# SHIRMANI Production Truth","",f"> Generated: {datetime.now(timezone.utc).isoformat()}","",
"## Current measurable state","",f"- Catalog identities: **{len(products)} / 1016**",f"- Concrete browser assets present: **{len(assets)} / 1016**",f"- Reusable family modules present: **{len(modules)} / 25**",f"- READY_FOR_QC: **{ready} / {len(products)}**",f"- CATALOG_READY: **{catalog_ready} / {len(products)}**",f"- Dispatch records: **{dispatch} / {len(products)}**","- Sales/payment settlement: **NOT CLAIMED**","- External delivery evidence: **NOT CLAIMED by this repository report**","- Independent scientific verification: **NOT CLAIMED**","",
"## Production truth","", "Catalog identity is not a sale. A concrete browser asset is not payment settlement. QC readiness is not independent verification.","",
"## Canonical chain","", "**1016 catalog identities → 1016 concrete assets → QC → dispatch gate → commercial delivery evidence → downstream verification**"]
OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
assert len(products)==1016
assert len(assets)==1016
assert len(modules)==25
print("\n".join(lines))
