#!/usr/bin/env python3
"""Deterministic QC for multimodal signal -> language records."""
from pathlib import Path
import json
SCHEMA=Path("schemas/multimodal-signal-interpretation.schema.json")
OUT=Path("generated/MULTIMODAL-SIGNAL-QC.json")
REQUIRED={"record_id","source","signals","interpretation","uncertainty","provenance"}
VALID={"OBSERVED","INFERRED","HYPOTHESIS","UNRESOLVED"}
def main():
    report={"schema_present":SCHEMA.exists(),"publication_gate":"BLOCK","records_checked":0,"errors":[],"integrity_rule":"observable_signal != inferred state != subjective experience"}
    if not SCHEMA.exists():
        report["errors"].append("Missing multimodal signal schema")
    else:
        paths=list(Path("generated").glob("multimodal-signal*.jsonl"))
        if not paths:
            report["publication_gate"]="CHECK"
            report["note"]="No multimodal records are present yet; schema and QC are ready."
        else:
            for path in paths:
                for lineno,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
                    if not line.strip(): continue
                    report["records_checked"]+=1
                    try: item=json.loads(line)
                    except json.JSONDecodeError as exc:
                        report["errors"].append(f"{path}:{lineno}: invalid JSON: {exc}"); continue
                    missing=REQUIRED-set(item)
                    if missing: report["errors"].append(f"{path}:{lineno}: missing fields {sorted(missing)}"); continue
                    it=item["interpretation"]
                    if it.get("status") not in VALID: report["errors"].append(f"{path}:{lineno}: invalid interpretation status")
                    c=it.get("confidence")
                    if not isinstance(c,(int,float)) or not 0<=c<=1: report["errors"].append(f"{path}:{lineno}: confidence must be 0..1")
                    if it.get("status")!="OBSERVED" and not item["uncertainty"]: report["errors"].append(f"{path}:{lineno}: uncertainty required for inference/hypothesis")
            report["publication_gate"]="PASS" if not report["errors"] else "BLOCK"
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    return 0 if report["publication_gate"]!="BLOCK" else 1
if __name__=="__main__": raise SystemExit(main())
