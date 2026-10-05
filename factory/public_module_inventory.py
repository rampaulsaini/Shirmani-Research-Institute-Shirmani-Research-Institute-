#!/usr/bin/env python3
"""Build a public-first production map from the repository's actual modules.

A file/page is mapped for production visibility only; existence is not
treated as implementation, execution, or independent verification.
"""
from pathlib import Path
import json,re
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
SKIP={".git","_sources","__pycache__"}
LANES={
"research":("research","paper","evidence","knowledge","archive"),
"ai_ml_nlp":("ai","ml","nlp","automission","agent","model"),
"content":("content","audio","video","music","podcast","media","story"),
"platform":("platform","dashboard","hub","portal","social"),
"economic":("income","employment","market","store","product","economic","value"),
"federation":("federation","repository","network"),
"security_quality":("security","quality","qc","verification","audit","governance"),
"automation":("workflow","factory","automation","orchestrator","worker"),
}
STATUS_RE=re.compile(r"\b(PLANNED|ARCHITECTURE|DESIGN|AVAILABLE BY MODULE|ACTIVE IN FACTORY|READY|ACTIVE|RECORDED|NOT_YET_RUN|UNAVAILABLE)\b",re.I)

def lane(path,text):
 s=(str(path)+" "+text[:1500]).lower()
 for name,keys in LANES.items():
  if any(k in s for k in keys): return name
 return "platform"

def status(text):
 vals={m.upper() for m in STATUS_RE.findall(text[:12000])}
 for p in ("ACTIVE","READY","RECORDED","ACTIVE IN FACTORY","AVAILABLE BY MODULE","ARCHITECTURE","DESIGN","PLANNED","NOT_YET_RUN","UNAVAILABLE"):
  if p in vals:return p
 return "UNSPECIFIED"

def main():
 rows=[]
 for p in ROOT.rglob("*"):
  if not p.is_file() or p.suffix.lower() not in {".html",".md",".yml",".yaml",".py",".json"}: continue
  if any(x in p.parts for x in SKIP) or str(p.relative_to(ROOT)).startswith("generated/"): continue
  text=p.read_text(encoding="utf-8",errors="ignore")
  rel=p.relative_to(ROOT)
  rows.append({"path":str(rel),"type":p.suffix.lower()[1:],"lane":lane(rel,text),"status":status(text),"bytes":p.stat().st_size})
 rows.sort(key=lambda x:(x["lane"],x["status"],x["path"]))
 counts={}; states={}
 for r in rows:
  counts[r["lane"]]=counts.get(r["lane"],0)+1
  states[r["status"]]=states.get(r["status"],0)+1
 now=datetime.now(timezone.utc).isoformat()
 payload={"version":1,"generated_at":now,"purpose":"public-first production module map","module_count":len(rows),"lane_counts":counts,"status_counts":states,"integrity":{"source":"repository files","fabricated_execution_claim":False,"independent_verification_claim":False},"modules":rows}
 OUT.mkdir(exist_ok=True)
 (OUT/"public-module-inventory.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 cards="".join(f"<article class='card'><b>{r['path']}</b><span>{r['lane']}</span><strong>{r['status']}</strong></article>" for r in rows)
 lanes="".join(f"<article class='card'><b>{k}</b><span>{v:,} mapped</span></article>" for k,v in sorted(counts.items()))
 html=f"""<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SHIRMANI Public Module Production Map</title><style>body{{margin:0;background:#0b0d14;color:#f5f5f5;font-family:system-ui,sans-serif}}main{{max-width:1250px;margin:auto;padding:24px}}h1,h2{{color:#d4af37}}.hero,.card{{background:rgba(255,255,255,.05);border:1px solid rgba(212,175,55,.25);border-radius:14px;padding:16px}}.hero{{margin-bottom:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px}}.card{{display:flex;flex-direction:column;gap:6px}}.card span{{color:#67e8f9;font-size:.85rem}}.card strong{{color:#fbbf24}}.metric{{font-size:1.8rem;color:#d4af37;font-weight:800}}a{{color:#d4af37}}</style></head><body><main><section class="hero"><h1>꙰ Public Module Production Map</h1><p>Repository के वास्तविक modules/files को production lanes में map किया गया है। यह <b>काम की visibility</b> है; मौजूद file अपने-आप implementation या verification का प्रमाण नहीं है।</p><div class="metric">{len(rows):,} modules/files mapped</div><p>Generated: {now}</p><p><a href="../public-production-command-center.html">Production Command Center</a> · <a href="../index.html">Main Hub</a></p></section><h2>Production lanes</h2><div class="grid">{lanes}</div><h2>Module inventory</h2><div class="grid">{cards}</div></main></body></html>"""
 (OUT/"public-module-production-map.html").write_text(html,encoding="utf-8")
 print(json.dumps({"module_count":len(rows),"lane_counts":counts,"status_counts":states},ensure_ascii=False))

if __name__=="__main__": main()
