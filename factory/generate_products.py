#!/usr/bin/env python3
import json,re,hashlib
from pathlib import Path
from factory_model_adapter import generate
ROOT=Path(__file__).resolve().parents[1]; G=ROOT/"generated"
src=G/"canonical-corpus.jsonl"; prov=G/"provenance-ledger.jsonl"; out=G/"ai-output.jsonl"
pmap={}
if prov.exists():
    for line in prov.read_text(encoding="utf-8").splitlines():
        if line.strip(): pmap[json.loads(line)["canonical_id"]]=json.loads(line)
rows=[]
def fallback(text, lang):
    clean=re.sub(r"\s+"," ",text).strip()
    if lang=="hi": return "स्रोत-आधारित मसौदा: "+clean
    if lang=="pa": return "ਸਰੋਤ-ਆਧਾਰਿਤ ਮਸੌਦਾ: "+clean
    return "Source-grounded draft: "+clean
if src.exists():
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        r=json.loads(line); cid=r["canonical_id"]; text=r.get("text","").strip()
        if not text: continue
        pv=pmap.get(cid,{})
        for lang in ("hi","pa","en"):
            prompt=("Create a faithful draft from ONLY the supplied source. Preserve meaning. "
                    "Do not add facts, sources, citations, scientific validation, or claims not in the source. "
                    f"Language: {lang}.\nSOURCE:\n{text}")
            draft,method=generate(prompt,fallback(text,lang))
            gid="GEN-"+hashlib.sha256((cid+"|"+lang+"|"+draft).encode()).hexdigest()[:16]
            rows.append({"generation_id":gid,"canonical_id":cid,"provenance_id":pv.get("provenance_id"),
                         "language":lang,"text":draft,"method":method,"status":"DRAFT",
                         "source_grounded":True,"verification_required":True,
                         "scientific_validation":False,"noncanonical":True})
out.write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+"\n",encoding="utf-8")
print("generation-agent:",len(rows))
