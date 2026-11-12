#!/usr/bin/env python3
"""Fail-closed deterministic Supreme NLP control-plane runner."""
from __future__ import annotations
import hashlib, json, math, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
OUT = GENERATED / "supreme-nlp-records.jsonl"
STATUS = GENERATED / "supreme-nlp-status.json"

def fingerprint(obj):
    raw=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    return hashlib.sha256(raw).hexdigest()

def numeric_values(signals):
    return [float(v) for v in signals.values()
            if isinstance(v,(int,float)) and math.isfinite(float(v))]

def process(row):
    text=str(row.get("text",""))
    signals=row.get("signals") or {}
    vals=numeric_values(signals)
    sample_count=len(vals)
    mean=sum(vals)/sample_count if vals else 0.0
    spread=max(vals)-min(vals) if vals else 0.0
    tokens=re.findall(r"\b[\wऀ-ॿ਀-੿]+\b",text.lower())
    counts=Counter(tokens)
    quality=1.0 if sample_count else (0.5 if text else 0.0)
    status="interpreted" if (text or vals) else "no_data"
    if quality < 0.5:
        status="insufficient_quality"
    simple=("मापनीय signal उपलब्ध है; यह केवल observable pattern का वर्णन है।"
            if vals else "मापनीय signal उपलब्ध नहीं है; subjective अवस्था का निष्कर्ष नहीं निकाला गया।")
    result={
        "status":status,
        "signals":[{"channel":k,"value":v} for k,v in signals.items()
                   if isinstance(v,(int,float)) and math.isfinite(float(v))],
        "features":{
            "mean":mean,"spread":spread,"anomaly_score":0.0,
            "agreement":1.0 if sample_count else 0.0,
            "quality":quality,"modalities":1 if vals else 0,
            "independent_sources":0,"sample_count":sample_count,
            "drift_score":0.0,"evidence_grade":"D"
        },
        "interpretation":{
            "state":"observable_signal_pattern" if vals else "no_observable_signal",
            "confidence":0.0 if not vals else 0.5,
            "confidence_status":"UNCALIBRATED",
            "evidence":[str(row.get("source") or row.get("repository") or "unknown")],
            "limitations":[
                "Subjective experience is not directly inferred.",
                "Confidence is uncalibrated and is not an accuracy claim."
            ]
        },
        "verification":{
            "status":"NOT_VERIFIED",
            "independent_required":True,
            "replication_required":True
        }
    }
    return {
        "schema_version":"supreme-nlp-v2",
        "task_id":str(row.get("id") or fingerprint(row)[:16]),
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "pipeline":"observe->normalize->feature_extraction->multimodal_fusion->nlp_interpretation->evidence_retrieval->independent_verification->confidence->audit->safe_publication",
        "result":result,
        "simple_language":simple,
        "fingerprint":fingerprint(row),
        "provenance":{
            "generator":"factory/supreme_nlp.py",
            "contract":"schemas/supreme-nlp-record.schema.json",
            "verification_status":"NOT_VERIFIED"
        }
    }

def main():
    GENERATED.mkdir(parents=True,exist_ok=True)
    source=GENERATED/"source-units.jsonl"
    rows=[]
    if source.exists():
        rows=[json.loads(x) for x in source.read_text(encoding="utf-8").splitlines() if x.strip()]
    records=[process(r) for r in rows[:1000]]
    OUT.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in records),encoding="utf-8")
    status={
        "schema_version":"supreme-nlp-v2",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "input_records":len(rows),"processed_records":len(records),
        "status":"READY" if source.exists() else "WAITING_FOR_SOURCE",
        "epistemic_policy":{
            "subjective_experience_direct_read":False,
            "observable_signal_translation":True,
            "unverified_claims_remain_unverified":True,
            "accuracy_is_measured_not_declared":True
        },
        "output":str(OUT.relative_to(ROOT))
    }
    STATUS.write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__":
    main()
