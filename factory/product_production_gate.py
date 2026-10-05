#!/usr/bin/env python3
"""Concrete SHIRMANI product-production gate.

100200 is the production batch identifier. Product numbering begins at .001.
Each produced module receives QC code, verification code, gate number and
explicit dispatch state. These identifiers never imply completed verification,
sale, payment or delivery.
"""
from __future__ import annotations
import hashlib, html, io, json, os
from datetime import datetime, timezone
from pathlib import Path
import qrcode
import qrcode.image.svg

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; QUEUE=GEN/"production-work-queue.jsonl"
OUT=GEN/"product-production"; COUNTER=GEN/"product-production-counter.json"
BATCH=os.environ.get("PRODUCTION_BATCH_NO","100200")
LIMIT=int(os.environ.get("PRODUCTION_BATCH_SIZE","500"))

def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()

def queue():
    if not QUEUE.exists(): return []
    out=[]
    for line in QUEUE.read_text(encoding="utf-8",errors="ignore").splitlines():
        try:
            if line.strip(): out.append(json.loads(line))
        except Exception: pass
    return out[:LIMIT]

def sequence_start():
    state={"batch_no":BATCH,"next_sequence":1}
    if COUNTER.exists():
        try: state.update(json.loads(COUNTER.read_text(encoding="utf-8")))
        except Exception: pass
    if str(state.get("batch_no"))!=BATCH: state={"batch_no":BATCH,"next_sequence":1}
    return max(1,int(state.get("next_sequence",1))),state

def qr(payload):
    code=qrcode.QRCode(border=2,box_size=4)
    code.add_data(json.dumps(payload,ensure_ascii=False,separators=(",",":"))); code.make(fit=True)
    img=code.make_image(image_factory=qrcode.image.svg.SvgPathImage)
    buf=io.BytesIO(); img.save(buf); return buf.getvalue().decode()

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    tasks=queue(); start,state=sequence_start()
    cycle=tasks[0].get("cycle",int(datetime.now(timezone.utc).timestamp()//300)) if tasks else int(datetime.now(timezone.utc).timestamp()//300)
    batchdir=OUT/f"batch-{BATCH}"; batchdir.mkdir(parents=True,exist_ok=True)
    products=[]
    for i,t in enumerate(tasks):
        n=start+i; no=f".{n:03d}" if n<1000 else f".{n}"
        raw=f"{BATCH}|{no}|{t.get('task_id','')}|{t.get('module','')}"
        qc="QC-"+digest(raw+"|QC")[:12].upper()
        ver="V-"+digest(raw+"|VERIFY")[:12].upper()
        gate="G-"+digest(raw+"|GATE")[:8].upper()
        payload={"product_id":f"SHIRMANI-{BATCH}{no}","batch_no":BATCH,"product_no":no,
                 "qc_code":qc,"verification_code":ver,"gate_no":gate,"dispatch":"NO",
                 "production_status":"PRODUCED","delivery_status":"NOT_DISPATCHED",
                 "commercial_status":"NOT_SOLD","independent_verification":"NOT_CLAIMED",
                 "source":t.get("module",""),"task_id":t.get("task_id"),"cycle":cycle}
        products.append({**payload,"product_name":"SHIRMANI "+str(t.get("lane","PRODUCT")).upper()+" — "+
                         Path(t.get("module","product")).stem.replace("_"," ").replace("-"," ").title(),
                         "production_timestamp":now(),
                         "qc":{"status":"QC_GATE_PENDING","checks":["source-bound","schema","package-completeness","provenance"]},
                         "verification":{"status":"DOWNSTREAM_PENDING"},
                         "dispatch_gate":{"dispatch":"NO","reason":"QC/owner/delivery gates are not bypassed"},
                         "qr_svg":qr(payload)})
    if products:
        state.update(batch_no=BATCH,next_sequence=start+len(products),last_product_no=products[-1]["product_no"],last_cycle=cycle)
        COUNTER.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    stamp=str(cycle); jf=batchdir/f"cycle-{stamp}.jsonl"
    jf.write_text("".join(json.dumps(p,ensure_ascii=False)+"\n" for p in products),encoding="utf-8")
    cards=[]
    for p in products:
        cards.append(f"<article><h2>{html.escape(p['product_id'])}</h2><h3>{html.escape(p['product_name'])}</h3>"
                     f"<p>Batch <b>{html.escape(BATCH)}</b> · Product <b>{html.escape(p['product_no'])}</b> · Gate <b>{html.escape(p['gate_no'])}</b></p>"
                     f"<p>QC <b>{html.escape(p['qc_code'])}</b> · Verification <b>{html.escape(p['verification_code'])}</b></p>"
                     f"<p>PRODUCED · DISPATCH <b>NO</b> · NOT_SOLD · DOWNSTREAM_PENDING</p>{p['qr_svg']}"
                     f"<p><small>Source: {html.escape(p['source'])}</small></p></article>")
    page=("<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
          f"<title>SHIRMANI Production Batch {BATCH}</title><style>body{{background:#0b0d14;color:#eee;font-family:system-ui;margin:0;padding:20px}}"
          "article{background:#151b26;border:1px solid #394454;border-radius:12px;padding:15px;margin:8px;display:inline-block;width:calc(50% - 50px);vertical-align:top}h1,h2{color:#d4af37}svg{max-width:160px;background:#fff;padding:6px}@media(max-width:700px){article{width:90%}}</style>"
          f"<h1>꙰ SHIRMANI Concrete Product Production</h1><p>Batch {BATCH} · Cycle {cycle} · Products {len(products)} · Sequence starts .001</p>"
          + "".join(cards))
    hp=batchdir/f"cycle-{stamp}.html"; hp.write_text(page,encoding="utf-8")
    manifest={"schema_version":1,"batch_no":BATCH,"cycle":cycle,
              "product_sequence_start":products[0]["product_no"] if products else None,
              "product_sequence_end":products[-1]["product_no"] if products else None,
              "products_produced":len(products),"jsonl":str(jf.relative_to(ROOT)),
              "html":str(hp.relative_to(ROOT)),
              "truth_boundary":"Codes identify QC/verification/gate state; they do not claim completed verification, sale, payment or delivery."}
    (batchdir/f"cycle-{stamp}-manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"CURRENT-BATCH.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
