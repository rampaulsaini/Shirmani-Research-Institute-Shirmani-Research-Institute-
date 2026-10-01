#!/usr/bin/env python3
import json
from pathlib import Path
C=Path(__file__).resolve().parents[1]/"schemas"/"supreme-nlp-contract.json"
REQUIRED={"ingest","quality_control","feature_extraction","temporal_analysis","multimodal_fusion","inference","calibration","evidence_binding","plain_language_translation","independent_verification","audit"}
def main():
    c=json.loads(C.read_text(encoding="utf-8"))
    if set(c["pipeline"])!=REQUIRED: raise SystemExit("BLOCK: incomplete NLP pipeline")
    if not all(c["truth_boundary"].values()): raise SystemExit("BLOCK: truth boundary incomplete")
    if not all(c["quality"].values()): raise SystemExit("BLOCK: quality gates incomplete")
    a=c["automission"]
    if not a["fail_closed"] or a["scheduled_code_mutation"]: raise SystemExit("BLOCK: Automission boundary unsafe")
    if a["production_promotion"]!="independent_verification_and_owner_approval": raise SystemExit("BLOCK: promotion boundary unsafe")
    print("SUPREME-NLP-QC: PASS")
if __name__=="__main__": main()
