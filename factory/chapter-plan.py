#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
units=[]
p=OUT/"canonical-corpus.jsonl"
if p.exists():
    for line in p.read_text(encoding="utf-8").splitlines():
        try: units.append(json.loads(line))
        except: pass
concepts=json.loads((OUT/"concept-map.json").read_text(encoding="utf-8")) if (OUT/"concept-map.json").exists() else {}
labels=list((concepts.get("concepts") or concepts).keys()) if isinstance(concepts,dict) else []
books=100; chapters_per_book=12
plan=[]
for b in range(1,books+1):
    chapters=[]
    for c in range(1,chapters_per_book+1):
        label=labels[((b-1)*chapters_per_book+c-1)%len(labels)] if labels else "निष्पक्ष समझ"
        chapters.append({"chapter":c,"theme":label,"source_units":[],"languages":["hi","pa","en"],"status":"DRAFT"})
    plan.append({"book":b,"title":f"डिजिटल महाग्रंथ {b:03d}","chapters":chapters,"status":"DRAFT"})
(OUT/"chapter-plan.json").write_text(json.dumps({"generated_at":datetime.now(timezone.utc).isoformat(),"books":plan,"total_books":books,"chapters_per_book":chapters_per_book},ensure_ascii=False,indent=2),encoding="utf-8")
print("chapter plan created:",books,"books",books*chapters_per_book,"chapters")
