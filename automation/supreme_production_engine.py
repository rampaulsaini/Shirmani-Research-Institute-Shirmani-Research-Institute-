"""SHIRMANI Supreme Multi-Layer Production Engine.

Production-first: continuously materialize concrete executable product assets.
Verification is downstream quality/promotion, not the production workload.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, html, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-production"
PY=sys.executable
STREAMS=[("research",1),("nlp",2),("writing",3),("multilingual",4),("knowledge",5),
         ("publishing",6),("audio",7),("ml",8),("product",9),("archive",10)]

def load():
    p=ROOT/"generated"/"canonical-corpus.jsonl"
    if not p.exists(): return []
    rows=[]
    for line in p.read_text(encoding="utf-8",errors="ignore").splitlines():
        if line.strip():
            try: rows.append(json.loads(line))
            except Exception: pass
    return rows

def pid(stream,row):
    raw=f"{stream}|{row.get('id','')}|{row.get('source','')}|{row.get('text','')}"
    return hashlib.sha256(raw.encode()).hexdigest()[:24]

def product(stream,row,i):
    t=re.sub(r"\s+"," ",str(row.get("text",""))).strip()
    source=row.get("source") or row.get("repository") or "unknown"
    kinds={"research":"research-product","nlp":"nlp-product","writing":"writing-product",
           "multilingual":"language-product","knowledge":"knowledge-product",
           "publishing":"publishing-product","audio":"audio-product","ml":"ml-product",
           "product":"digital-product","archive":"archive-product"}
    return {"work_id":pid(stream,row),"stream":stream,"source_id":row.get("id",i),
            "source":source,"source_text":t[:4000],"status":"PRODUCED",
            "verification_status":"PENDING","generated_at":datetime.now(timezone.utc).isoformat(),
            "deliverable":{"type":kinds[stream],"production_package":True}}

def run_factory():
    results=[]
    for rel in ["factory/real_product_factory.py","factory/concrete_product_modules.py"]:
        r=subprocess.run([PY,str(ROOT/rel)],cwd=ROOT,text=True,capture_output=True,check=False)
        results.append({"step":rel,"exit_code":r.returncode,"output":(r.stdout+r.stderr)[-1200:]})
        if r.returncode!=0: raise SystemExit("Production step failed: "+rel)
    return results

def main():
    ts=datetime.now(timezone.utc).isoformat()
    OUT.mkdir(parents=True,exist_ok=True)
    factory_runs=run_factory()
    rows=load()
    q=OUT/"work-queue.jsonl"; counts={}
    with q.open("w",encoding="utf-8") as f:
        for i,row in enumerate(rows,1):
            for stream,_ in STREAMS:
                f.write(json.dumps(product(stream,row,i),ensure_ascii=False)+"\n")
                counts[stream]=counts.get(stream,0)+1
    catalog={}
    cp=ROOT/"generated"/"1000-digital-products.json"
    if cp.exists():
        try: catalog=json.loads(cp.read_text(encoding="utf-8"))
        except Exception: catalog={}
    asset_dir=ROOT/"products"/"production"
    actual_assets=len(list(asset_dir.glob("*.html"))) if asset_dir.exists() else 0
    stats={"generated_at":ts,"source_records":len(rows),"layers":len(STREAMS),
           "tasks":sum(counts.values()),"streams":counts,
           "concrete_catalog_products":catalog.get("product_count",0),
           "concrete_product_assets":actual_assets,"product_factory_status":"ACTIVE",
           "production_pipeline":["Institute Discovery","Factory Production","Concrete Product Asset",
                                  "QC Gate","Public Showroom","Sale","Downstream Verification"],
           "dispatch_default":"NO","chat_required_for_continuity":False,"factory_runs":factory_runs}
    (OUT/"production-status.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding="utf-8")
    rows_html="".join(f"<tr><td>{html.escape(k)}</td><td>{v:,}</td></tr>" for k,v in counts.items())
    page=f"""<!doctype html><html lang="hi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>꙰ SHIRMANI Supreme Production</title><style>body{{background:#080b11;color:#eef2f7;font:16px system-ui;max-width:1200px;margin:auto;padding:24px}}h1,h2{{color:#d4af37}}.card{{background:#111827;border:1px solid #334155;border-radius:16px;padding:18px;margin:12px 0}}table{{width:100%;border-collapse:collapse}}td,th{{padding:9px;border-bottom:1px solid #334155;text-align:left}}a{{color:#67e8f9}}</style>
<body><section class=card><h1>꙰ SHIRMANI Supreme Multi-Layer Production</h1>
<h2>{stats["concrete_catalog_products"]:,} concrete catalog products · {actual_assets:,} executable product assets</h2>
<p>Institute → Factory → Concrete Product → QC Gate → Public Showroom → Sale → downstream result verification.</p>
<p>Dispatch default: <b>NO</b> · Chat required for continuity: <b>NO</b></p>
<p><a href="../supreme-production-showroom.html">Production Showroom</a> · <a href="../products.html">All Products</a></p></section>
<section class=card><h2>Multi-layer work streams</h2><table><tr><th>Layer</th><th>Produced work units</th></tr>{rows_html}</table></section>
<section class=card><h2>Production principle</h2><p>Workflow activity is not counted as a finished product. The factory must materialize a concrete executable product asset before it is listed as a concrete product. QC evaluates the produced result; it is not the production objective.</p></section></body></html>"""
    (ROOT/"production-dashboard.html").write_text(page,encoding="utf-8")
    print(json.dumps(stats,ensure_ascii=False))

if __name__=="__main__":
    main()
