"""Provider-neutral measurable-signal -> plain-language NLP adapter."""
from __future__ import annotations
import hashlib, json, math
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_INPUT=ROOT/"generated/supreme-nlp/signal-input.jsonl"
DEFAULT_OUTPUT=ROOT/"generated/supreme-nlp/signal-language.json"

def fingerprint(value:Any)->str:
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def load_jsonl(path:Path)->list[dict[str,Any]]:
    rows=[]
    if not path.exists(): return rows
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: value=json.loads(line)
        except json.JSONDecodeError: continue
        if isinstance(value,dict):
            value["_line_number"]=n
            rows.append(value)
    return rows

def numeric_series(rows):
    out={}
    for row in rows:
        features=row.get("features")
        if not isinstance(features,dict): continue
        for key,value in features.items():
            if isinstance(value,bool): continue
            if isinstance(value,(int,float)) and math.isfinite(float(value)):
                out.setdefault(str(key),[]).append(float(value))
    return out

def slope(values):
    if len(values)<2: return 0.0
    xm=(len(values)-1)/2
    ym=mean(values)
    den=sum((i-xm)**2 for i in range(len(values)))
    return 0.0 if den==0 else sum((i-xm)*(v-ym) for i,v in enumerate(values))/den

def summarize(values):
    return {"sample_count":len(values),"mean":round(mean(values),8),
            "stddev":round(pstdev(values) if len(values)>1 else 0.0,8),
            "minimum":round(min(values),8),"maximum":round(max(values),8),
            "slope_per_sample":round(slope(values),8)}

def direction(s,scale):
    threshold=max(scale*0.05,1e-12)
    return "increasing" if s>threshold else "decreasing" if s<-threshold else "stable_or_uncertain"

def interpret(rows):
    series=numeric_series(rows)
    summaries={k:summarize(v) for k,v in series.items()}
    modalities=sorted({str(r.get("modality","unknown")).strip().lower() or "unknown" for r in rows})
    sources=sorted({str(r.get("source_id","unknown")).strip() or "unknown" for r in rows})
    completeness=mean([1.0 if isinstance(r.get("features"),dict) and r.get("features") else 0.0 for r in rows]) if rows else 0.0
    states=[str(r["features"]["state"]) for r in rows if isinstance(r.get("features"),dict) and "state" in r["features"]]
    contradiction=len(set(states))>1
    observations=[{"feature":k,"statistics":v,
                   "pattern":direction(float(v["slope_per_sample"]),max(float(v["stddev"]),abs(float(v["mean"])),1.0))}
                   for k,v in summaries.items()]
    if not rows:
        status="INSUFFICIENT_DATA"; confidence=0.0
        plain="कोई मान्य signal record उपलब्ध नहीं है; इसलिए कोई pattern interpretation नहीं बनाई गई।"
        uncertainty=["Input data is empty or unavailable."]; verification="UNVERIFIED"
    else:
        status="REVIEW" if contradiction else "INTERPRETED"
        confidence=0.20+0.20*min(len(rows)/30,1.0)+0.15*min(len(sources)/3,1.0)+0.15*min(len(series)/3,1.0)+0.20*completeness-(0.20 if contradiction else 0)
        confidence=round(max(0.0,min(0.90,confidence)),4)
        verification="REVIEW" if contradiction else "UNVERIFIED"
        pattern_text=", ".join(f"{x['feature']}={x['pattern']}" for x in observations) or "कोई पर्याप्त numerical pattern नहीं"
        plain=(f"मापे गए {len(rows)} records में {len(series)} numerical signals मिले। "
               f"देखे गए patterns: {pattern_text}। यह measurable signal pattern का वर्णन है; "
               "इसे अपने-आप subjective feeling, consciousness या intention का प्रमाण नहीं माना जाता।")
        uncertainty=[
            "Calibration and sensor quality are not independently established by this adapter.",
            "A deterministic pattern is not equivalent to causal or psychological explanation.",
            "Independent replication and task-specific evaluation are required for VERIFIED status."
        ]
        if contradiction: uncertainty.append("Multiple state labels were observed; interpretation requires review.")
    result={
        "schema_version":"1.0.0","status":status,
        "observed_signal":{"record_count":len(rows),"modalities":modalities,"independent_sources":sources,"series":summaries},
        "patterns":observations,
        "inference":{"label":"measurable-pattern-description","evidence":["deterministic descriptive statistics","temporal slope analysis","input provenance"],
                     "confidence":confidence,"provider":"shirmani-signal-to-language","task":"signal-pattern-to-plain-language"},
        "plain_language":plain,"uncertainty":uncertainty,
        "provenance":{"source":"generated/supreme-nlp/signal-input.jsonl","input_fingerprint":fingerprint(rows),
                      "model":"deterministic-signal-describer","model_version":"1.0.0"},
        "verification_state":verification,
        "required_next_gate":"independent replication + task-specific benchmark",
        "governance":{"fail_closed":True,"subjective_experience_claim_allowed":False,"independent_verification_required":True},
        "generated_at":datetime.now(timezone.utc).isoformat()
    }
    result["fingerprint"]=fingerprint(result)
    return result

def run(input_path=DEFAULT_INPUT,output_path=DEFAULT_OUTPUT):
    result=interpret(load_jsonl(input_path))
    output_path.parent.mkdir(parents=True,exist_ok=True)
    output_path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return result

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
