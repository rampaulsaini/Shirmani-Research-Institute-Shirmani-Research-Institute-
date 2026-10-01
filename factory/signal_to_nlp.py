#!/usr/bin/env python3
"""Evidence-first multimodal signal to plain-language NLP adapter."""
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, pstdev

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_INPUT=ROOT/"generated"/"signal-input.jsonl"
DEFAULT_OUTPUT=ROOT/"generated"/"signal-nlp-output.jsonl"

def sha256(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def numeric_values(values):
    return [float(v) for v in values if isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v)]

def summarize_features(record):
    features=[]
    for name,value in sorted(record.get("observations",{}).items()):
        if isinstance(value,list):
            nums=numeric_values(value)
            if nums:
                features.append((name,{"count":len(nums),"mean":mean(nums),"std":pstdev(nums) if len(nums)>1 else 0.0,"min":min(nums),"max":max(nums)}))
            else:
                features.append((name,{"count":len(value),"values":value[:10]}))
        elif isinstance(value,(int,float,str,bool)) or value is None:
            features.append((name,value))
    return features

def interpret(record):
    features=summarize_features(record)
    names=[name for name,_ in features]
    pattern=(f"Observed {len(features)} measurable feature group(s): {', '.join(names[:8])}."
             if features else "No usable measurable features were supplied.")
    uncertainty=[
        "Sensor measurements can contain noise, drift, calibration error, or missing context.",
        "A detected pattern does not by itself establish subjective feeling, consciousness, intention, or causation.",
        "Interpretation confidence is limited by the supplied data and method; independent validation is required."
    ]
    interpretation=("The supplied measurements show the pattern described above. "
                     "This is a data-derived description, not a claim about inner experience."
                     if features else
                     "The system cannot form a grounded interpretation because measurable input features are absent.")
    return {
        "signal_id":str(record.get("signal_id","unknown")),
        "observed_features":[{"name":n,"value":v} for n,v in features],
        "pattern_summary":pattern,
        "interpretation":interpretation,
        "confidence":round(1.0 if features else 0.0,4),
        "uncertainty":uncertainty,
        "evidence_level":"derived_pattern" if features else "unverified",
        "provenance":{
            "input_hash":sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(",",":"))),
            "method":"deterministic-feature-summary-v1",
            "created_at":datetime.now(timezone.utc).isoformat()
        }
    }

def run(input_path,output_path):
    output_path.parent.mkdir(parents=True,exist_ok=True)
    count=0
    with input_path.open(encoding="utf-8") as src, output_path.open("w",encoding="utf-8") as dst:
        for line_no,line in enumerate(src,1):
            if not line.strip():
                continue
            try:
                dst.write(json.dumps(interpret(json.loads(line)),ensure_ascii=False)+"\n")
                count+=1
            except Exception as exc:
                raise SystemExit(f"signal record {line_no} failed closed: {exc}") from exc
    return count

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",default=str(DEFAULT_INPUT))
    parser.add_argument("--output",default=str(DEFAULT_OUTPUT))
    args=parser.parse_args()
    if not Path(args.input).exists():
        print(json.dumps({"records":0,"status":"NO_INPUT","message":"No signal input supplied; no interpretation fabricated."},ensure_ascii=False))
    else:
        print(json.dumps({"records":run(Path(args.input),Path(args.output)),"status":"PASS"},ensure_ascii=False))
