#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; items=[]
for pattern,kind in [("book-*.md","digital-book-draft"),("research-paper-draft-*.md","research-paper-draft"),("verse-corpus.jsonl","verse-corpus"),("certificates/*.md","archival-certificate")]:
    for p in sorted(OUT.glob(pattern)): items.append({"path":str(p.relative_to(ROOT)),"kind":kind,"draft_only":kind!="archival-certificate"})
index={"generated_at":datetime.now(timezone.utc).isoformat(),"status":"INDEXED_NOT_PUBLISHED","items":items,"safety":"Research outputs are drafts and require independent verification; certificates are archival/participation records only.","canonical_source":"source-units.jsonl"}
(OUT/"publication-index.json").write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding="utf-8"); print("publication index:",len(items),"items")
