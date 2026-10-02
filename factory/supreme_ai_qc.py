"""QC for the Supreme AI/ML/NLP/Automission stack."""
from __future__ import annotations
import json, sys
from pathlib import Path

REQUIRED = [
    "agents/supreme_nlp.py",
    "agents/ultra_automission.py",
    "tests/test_supreme_ai.py"
]

def main():
    errors=[]
    for p in REQUIRED:
        if not Path(p).is_file():
            errors.append("missing:"+p)
    status=Path("generated/supreme-nlp/status.json")
    if status.exists():
        try:
            d=json.loads(status.read_text(encoding="utf-8"))
            for k in ("architecture","status","features","interpretation","fingerprint"):
                if k not in d: errors.append("status_missing:"+k)
            c=float(d.get("interpretation",{}).get("confidence",0))
            if not 0 <= c <= 1: errors.append("confidence_out_of_range")
        except (OSError,json.JSONDecodeError) as e:
            errors.append("invalid_status:"+str(e))
    report={
        "publication_gate":"BLOCK" if errors else "PASS",
        "errors":errors,
        "checks":{
            "fail_closed":True,
            "subjective_experience_claim_allowed":False,
            "scheduled_source_mutation_allowed":False,
            "independent_verification_required":True
        }
    }
    Path("generated/supreme-nlp").mkdir(parents=True,exist_ok=True)
    Path("generated/supreme-nlp/qc.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=="__main__":
    sys.exit(main())
