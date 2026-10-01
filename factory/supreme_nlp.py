"""Evidence-gated multimodal NLP gateway."""
from __future__ import annotations
import hashlib,json,math
from datetime import datetime,timezone
from pathlib import Path

MODALITIES={"text","speech","image","video","audio","sensor","environmental","temporal"}

def _confidence(x):
    try:
        x=float(x)
        return x if math.isfinite(x) else None
    except (TypeError,ValueError):
        return None

def interpret(records):
    rows=[]
    for r in records:
        if not isinstance(r,dict): continue
        m=str(r.get("modality","unknown")).lower().strip()
        c=_confidence(r.get("confidence"))
        rows.append({"id":str(r.get("id","")),"modality":m,"value":r.get("value"),
                     "unit":r.get("unit"),"confidence":c,"supported":m in MODALITIES})
    valid=[r for r in rows if r["supported"]]
    rated=[r for r in valid if r["confidence"] is not None]
    mean=sum(r["confidence"] for r in rated)/len(rated) if rated else 0
    status="interpretable" if len(valid)>=2 and mean>=.70 else "insufficient_evidence"
    if status=="interpretable":
        text=("संकेतों में एक structured pattern मिला है। यह किसी अवस्था से "
              "संबंधित हो सकता है; इसे अपने-आप subjective experience का प्रमाण नहीं माना गया है।")
    else:
        text=("पर्याप्त प्रमाण नहीं मिला। प्रणाली ने अनुमान लगाने के बजाय abstain किया है।")
    out={"schema_version":"1.0","status":status,
         "generated_at":datetime.now(timezone.utc).isoformat(),
         "observation_count":len(valid),
         "observations":[f'{r["modality"]}: {r["value"]!r}' for r in valid[:20]],
         "mean_input_confidence":round(mean,4),
         "plain_language_interpretation":text,
         "claim_boundary":"Observed signals are not equivalent to subjective experience.",
         "verification_required":True,
         "independent_verification":status=="interpretable"}
    raw=json.dumps(out,sort_keys=True,ensure_ascii=False).encode()
    out["content_hash_sha256"]=hashlib.sha256(raw).hexdigest()
    return out

def run(src="generated/source-units.jsonl",dst="generated/supreme-nlp-report.json"):
    records=[]
    p=Path(src)
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            try:
                x=json.loads(line)
                if isinstance(x,dict) and "modality" in x: records.append(x)
            except json.JSONDecodeError: pass
    out=interpret(records)
    q=Path(dst); q.parent.mkdir(parents=True,exist_ok=True)
    q.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return out

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
