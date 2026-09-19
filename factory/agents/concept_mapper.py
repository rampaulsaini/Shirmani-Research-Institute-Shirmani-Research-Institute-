import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"canonical-corpus.jsonl"; out=ROOT/"generated"/"concept-map.json"
terms=["निष्पक्ष समझ","यथार्थ","हृदय","मस्तक","आत्म-अवलोकन","प्रकृति","OpenUSD","GPU","Python","C++","Omniverse","research"]
counts={t:0 for t in terms}; records=0
if src.exists():
    for line in src.read_text(encoding="utf-8").splitlines():
        r=json.loads(line); records+=1; text=r["text"].lower()
        for t in terms:
            if t.lower() in text: counts[t]+=1
out.write_text(json.dumps({"records":records,"concept_counts":counts},ensure_ascii=False,indent=2),encoding="utf-8")
print("concept-mapper:",records)
