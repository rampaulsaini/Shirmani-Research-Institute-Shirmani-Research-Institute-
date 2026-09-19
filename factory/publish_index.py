#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
entries=[]
for p in sorted(OUT.glob("*.md")):
    if p.name=="CATALOG.md": continue
    entries.append({"title":p.stem,"path":str(p.relative_to(ROOT)),"url_path":"/generated/"+p.name,"status":"DRAFT"})
idx={"generated_at":datetime.now(timezone.utc).isoformat(),"status":"INDEXED","base":"GitHub Pages","entries":entries,"research_policy":"All research papers remain drafts until independently verified."}
(OUT/"pages-index.json").write_text(json.dumps(idx,ensure_ascii=False,indent=2),encoding="utf-8")
print("pages index:",len(entries))
