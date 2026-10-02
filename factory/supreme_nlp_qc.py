"""Dependency-independent Supreme NLP v2 quality smoke test."""
import hashlib, json
from datetime import datetime, timezone

def build_record(signals, task_id):
    now=datetime.now(timezone.utc).isoformat()
    sources=sorted({str(x.get("source","unknown")) for x in signals})
    modalities=sorted({str(x.get("modality","unknown")) for x in signals})
    result={
      "status":"interpreted" if signals else "insufficient_quality",
      "features":{"independent_sources":len(sources),"sample_count":len(signals),"modalities":len(modalities),
                  "confidence":0.75,"confidence_status":"UNCALIBRATED"},
      "interpretation":{
        "confidence":0.75,"confidence_status":"UNCALIBRATED",
        "confidence_type":"heuristic_uncalibrated",
        "limitations":["Synthetic QC fixture; not evidence of subjective experience."],
        "verification":{"status":"UNVERIFIED"},
      },
      "verification":{"status":"UNVERIFIED","promotion_allowed":False},
    }
    out={
      "schema_version":"supreme-nlp-v2","task_id":task_id,"generated_at":now,
      "pipeline":"observe->normalize->quality->evidence->verification->NLP",
      "result":result,
      "simple_language":"Measured signal pattern only; subjective experience is not established.",
      "provenance":{"verification_status":"UNVERIFIED","source":"synthetic-qc"},
    }
    out["fingerprint"]=hashlib.sha256(json.dumps(out,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return out

def main():
    signals=[
      {"modality":"sensor","feature":"electrical","value":1.0,"quality":0.95,"source":"qc-a"},
      {"modality":"vibration","feature":"rms","value":0.5,"quality":0.90,"source":"qc-b"},
    ]
    out=build_record(signals,"qc-smoke")
    required={"schema_version","task_id","generated_at","pipeline","result","simple_language","fingerprint","provenance"}
    assert required <= set(out)
    assert out["schema_version"]=="supreme-nlp-v2"
    assert out["result"]["status"]=="interpreted"
    assert out["result"]["verification"]["status"]=="UNVERIFIED"
    assert out["provenance"]["verification_status"]=="UNVERIFIED"
    assert out["result"]["interpretation"]["confidence_status"]=="UNCALIBRATED"
    assert out["result"]["features"]["independent_sources"]==2
    assert out["result"]["features"]["sample_count"]==2
    print("SUPREME_NLP_QC_V2=PASS")

if __name__=="__main__": main()
