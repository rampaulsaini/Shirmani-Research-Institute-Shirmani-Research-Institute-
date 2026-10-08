#!/usr/bin/env python3
"""Deterministic unique digital-product/tool cycle.

Candidates are proposals only. A candidate is not promoted to VERIFIED or
published until asset, delivery, evidence and independent-verification gates pass.
"""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

CATALOG=Path("factory/product-catalog.json")
OUT=Path("generated/unique-digital-product-cycle.json")

SEEDS=[
 {"name":"Evidence Traceability Card Builder","type":"browser-tool","value":"Turn a research claim into a compact claim-source-evidence-verification card."},
 {"name":"Independent Verification Progress Map","type":"browser-tool","value":"Visualize queued, reviewed and independently VERIFIED research records without granting promotion."},
 {"name":"Product Reality Readiness Checker","type":"browser-tool","value":"Check asset evidence, delivery path, packaging and publication readiness before release."},
 {"name":"Research Claim Provenance Packager","type":"digital-tool","value":"Package claim provenance, source references and evidence metadata into a reusable research record."},
 {"name":"Automission Cycle Product Scorecard","type":"browser-tool","value":"Score each product/tool cycle for uniqueness, evidence, delivery, usability and review readiness."},
 {"name":"Heart-View Reasoning Worksheet","type":"downloadable-template","value":"A structured worksheet for separating observation, reasoning, evidence and independent verification."},
 {"name":"Digital Product Offer Comparator","type":"browser-tool","value":"Compare digital offers by uniqueness, deliverability, evidence state and customer value."},
 {"name":"Research-to-Product Brief Generator","type":"browser-tool","value":"Convert an eligible research insight into a product brief while keeping verification downstream."}
]

def norm(s): return " ".join(str(s).casefold().split())

catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
existing=[]
for lane in catalog.get("lanes",[]):
    for offer in lane.get("offers",[]):
        existing += [norm(offer.get("name","")), norm(offer.get("id",""))]

cycle=int(datetime.now(timezone.utc).timestamp()//300)
ordered=sorted(SEEDS, key=lambda x: hashlib.sha256(f"{cycle}:{x['name']}".encode()).hexdigest())
selected=[]
for candidate in ordered:
    key=norm(candidate["name"])
    if key not in existing and not any(key==norm(x["name"]) for x in selected):
        selected.append(candidate)
    if len(selected)>=3:
        break

payload={
 "generated_at":datetime.now(timezone.utc).isoformat(),
 "cycle_id":cycle,
 "mode":"UNIQUE_DIGITAL_PRODUCT_AND_TOOL_DISCOVERY",
 "uniqueness_rule":"candidate name must not already exist in canonical product catalog",
 "promotion_rule":"PROPOSAL_ONLY until asset, delivery, evidence and independent verification gates pass",
 "selected_candidates":selected,
 "next_gates":["SOURCE_ASSET","PRODUCT_RECORD","PACKAGING","PRODUCT_PAGE","DELIVERY_PATH","EVIDENCE","VERIFICATION"]
}
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"
",encoding="utf-8")
print(json.dumps(payload,ensure_ascii=False,indent=2))
