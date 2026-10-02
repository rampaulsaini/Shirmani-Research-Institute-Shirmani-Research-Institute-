"""Deterministic gate for multimodal signal -> NLP records."""
import json
import sys
from pathlib import Path

REQUIRED = {"record_id","timestamp","source_type","modality","raw_reference","measurement","detected_pattern","model_inference","plain_language","confidence","uncertainty","evidence","alternative_interpretations","verification_state"}
FORBIDDEN = ("proves consciousness","proof of consciousness","proves subjective feeling","proof of subjective feeling","definitively feels","definitively conscious")

def validate(record):
    errors=[]
    missing=REQUIRED-set(record)
    if missing: errors.append("missing fields: "+", ".join(sorted(missing)))
    try:
        confidence=float(record.get("confidence",-1))
        if not 0 <= confidence <= 1: errors.append("confidence must be between 0 and 1")
    except (TypeError,ValueError):
        errors.append("confidence must be numeric")
    text=" ".join(str(record.get(k,"")) for k in ("model_inference","plain_language")).lower()
    for phrase in FORBIDDEN:
        if phrase in text: errors.append("unsupported subjective-state claim: "+phrase)
    if not record.get("evidence"): errors.append("evidence is required")
    if not record.get("uncertainty"): errors.append("uncertainty must be explicit")
    if not record.get("alternative_interpretations"): errors.append("alternative interpretations must be recorded")
    return errors

if __name__ == "__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: python3 factory/supreme_senses_signal_qc.py <json-file>")
    record=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors=validate(record)
    print(json.dumps({"status":"BLOCKED" if errors else "PASS","errors":errors},ensure_ascii=False,indent=2))
    raise SystemExit(1 if errors else 0)
