#!/usr/bin/env python3
"""Deterministic multimodal-signal to plain-language research translator."""
from __future__ import annotations
import hashlib, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"; INPUT=OUT/"multimodal-signal-sample.jsonl"
RESULT=OUT/"multimodal-signal-nlp.jsonl"; QC=OUT/"MULTIMODAL-SIGNAL-NLP-QC.json"

def finite(x):
    return isinstance(x,(int,float)) and math.isfinite(x)

def translate(row):
    observations=row.get("observations",[])
    channels=[str(x.get("channel","unknown")) for x in observations if isinstance(x,dict)]
    values=[x.get("value") for x in observations if isinstance(x,dict) and finite(x.get("value"))]
    completeness=min(1.0,len(observations)/4.0)
    numeric=min(1.0,len(values)/max(1,len(observations)))
    confidence=round(0.25+0.50*completeness+0.25*numeric,4)
    return {
      "record_id":str(row.get("record_id","")),
      "source_type":row.get("source_type","synthetic"),
      "observations":observations,
      "interpretation":(
        f"मापे गए संकेतों में {', '.join(channels) or 'कोई निर्दिष्ट चैनल नहीं'} उपलब्ध हैं। "
        "इन संकेतों से केवल observable pattern की व्याख्या की जा रही है; subjective feeling या consciousness का दावा नहीं किया जा रहा है."
      ),
      "confidence":confidence,
      "uncertainty":[
        "Signal quality and sensor calibration must be independently checked.",
        "Model inference is not direct access to subjective experience.",
        "Independent verification is required before any VERIFIED status."
      ],
      "provenance":{
        "method":"deterministic_signal_to_language_v1",
        "input_hash":hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
      },
      "verification_status":"NOT_VERIFIED",
      "subjective_feeling_claim":False
    }

def main():
    OUT.mkdir(exist_ok=True)
    if not INPUT.exists():
        INPUT.write_text(json.dumps({"record_id":"demo-001","source_type":"plant","observations":[
          {"channel":"electrical_signal","value":0.42},
          {"channel":"temperature","value":24.1},
          {"channel":"vibration","value":0.08}
        ]},ensure_ascii=False)+"\n",encoding="utf-8")
    records=[]; errors=[]
    for n,line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try:
            rec=translate(json.loads(line))
            if not rec["record_id"]: errors.append({"line":n,"error":"missing_record_id"})
            records.append(rec)
        except Exception as exc:
            errors.append({"line":n,"error":f"invalid_input:{exc}"})
    RESULT.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in records),encoding="utf-8")
    for x in records:
        if x["verification_status"]!="NOT_VERIFIED" or x["subjective_feeling_claim"] is True:
            errors.append({"record_id":x["record_id"],"error":"fail_closed_verification_or_feeling_claim"})
        if not 0<=x["confidence"]<=1:
            errors.append({"record_id":x["record_id"],"error":"confidence_out_of_range"})
    report={"schema_version":1,"records":len(records),"errors":errors,
            "publication_gate":"PASS" if not errors else "BLOCK",
            "principle":"measured signal != inference != subjective feeling proof"}
    QC.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)

if __name__=="__main__": main()
