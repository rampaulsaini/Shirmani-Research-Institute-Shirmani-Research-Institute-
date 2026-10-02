"""Fail-closed evidence gate for multimodal Supreme NLP Automission."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN=[r"direct proof of subjective experience",r"proved subjective experience",r"proven consciousness",r"भावना.*सिद्ध",r"एहसास.*सिद्ध",r"चेतना.*सिद्ध"]
REQUIRED=["subjective experience","independent","uncertainty"]
def main()->int:
    p=ROOT/"generated/supreme-nlp/practitioner-status.json"
    if not p.exists(): print("BLOCK: missing practitioner record"); return 1
    d=json.loads(p.read_text(encoding="utf-8")); g=d.get("governance",{})
    errors=[]
    if g.get("fail_closed") is not True: errors.append("fail_closed required")
    if g.get("subjective_experience_claim_allowed") is not False: errors.append("subjective experience claims blocked")
    if g.get("independent_verification_required") is not True: errors.append("independent verification required")
    text=json.dumps(d,ensure_ascii=False).lower()
    errors += [f"forbidden certainty pattern: {x}" for x in FORBIDDEN if re.search(x,text)]
    limits=json.dumps((d.get("result") or {}).get("interpretation",{}).get("limitations",[]),ensure_ascii=False).lower()
    errors += [f"missing evidence boundary: {x}" for x in REQUIRED if x not in limits and x not in text]
    out={"status":"PASS" if not errors else "BLOCK","errors":errors,"policy":{"observable_signal_translation":True,"subjective_experience_as_fact":False,"independent_verification_required":True,"fail_closed":True}}
    q=ROOT/"generated/supreme-nlp/truth-gate.json"; q.parent.mkdir(parents=True,exist_ok=True); q.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())