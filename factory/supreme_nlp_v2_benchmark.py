"""Fail-closed deterministic Supreme NLP v2 adversarial regression gate."""
from pathlib import Path
import hashlib, json, math, re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-nlp-v2-benchmark.json"
POS={"good","great","happy","love","excellent","श्रेष्ठ","अच्छा","प्रेम","उत्तम"}
NEG={"bad","sad","hate","poor","danger","खराब","दुख","घृणा","खतरा"}
NEGATORS={"not","no","never","नहीं","न","मत"}
CASES=[("en-pos-01","great research","positive-pattern"),("en-neg-01","bad result","negative-pattern"),("en-neutral-01","research paper","neutral-or-uncertain"),("hi-pos-01","श्रेष्ठ प्रेम","positive-pattern"),("hi-neg-01","खराब परिणाम","negative-pattern"),("hi-neutral-01","अनुसंधान प्रणाली","neutral-or-uncertain"),("mixed-pos-01","great प्रेम","positive-pattern"),("mixed-neg-01","bad खतरा","negative-pattern"),("negation-en-01","not good","neutral-or-uncertain"),("negation-hi-01","नहीं अच्छा","neutral-or-uncertain"),("conflict-01","good bad","neutral-or-uncertain")]
def infer(text):
    tokens=re.findall(r"[\\w\\u0900-\\u097F]+",text.lower())
    pos=sorted(set(tokens)&POS); neg=sorted(set(tokens)&NEG)
    if set(tokens)&NEGATORS and (pos or neg): return "neutral-or-uncertain",sorted(set(tokens)&(POS|NEG))
    if len(pos)>len(neg): return "positive-pattern",pos
    if len(neg)>len(pos): return "negative-pattern",neg
    return "neutral-or-uncertain",pos+neg
def main():
    rows=[]; correct=0
    for case_id,text,expected in CASES:
        predicted,evidence=infer(text); ok=predicted==expected; correct+=int(ok)
        rows.append({"id":case_id,"expected":expected,"predicted":predicted,"evidence":evidence,"correct":ok,"verification_state":"UNVERIFIED"})
    accuracy=correct/len(CASES)
    gates={"all_cases_pass":correct==len(CASES),"accuracy_bounded":math.isfinite(accuracy) and 0<=accuracy<=1,"abstention_cases_present":any(r["id"].startswith(("negation","conflict")) for r in rows),"verification_remains_unverified":all(r["verification_state"]=="UNVERIFIED" for r in rows)}
    status="PASS" if all(gates.values()) else "BLOCK"
    record={"benchmark_id":"supreme-nlp-v2-adversarial-reference","model_version":"0.4","metric":"accuracy","result":accuracy,"sample_count":len(CASES),"correct_count":correct,"status":status,"gates":gates,"verification_state":"UNVERIFIED","cases":rows,"limitations":["tiny fixed fixture","lexical baseline only","not a general language benchmark","not evidence of subjective feeling, consciousness or intention"]}
    record["dataset_fingerprint"]=hashlib.sha256(json.dumps(CASES,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    record["fingerprint"]=hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(record,ensure_ascii=False,indent=2))
    return 0 if status=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())