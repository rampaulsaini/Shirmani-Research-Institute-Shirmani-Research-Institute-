"""Deterministic, dependency-free Supreme NLP regression benchmark.

Reports accuracy, macro precision/recall/F1 and confidence calibration for a
small fixed fixture. Results are scoped to this benchmark and never presented
as universal language-understanding accuracy.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"/"supreme-nlp-benchmark.json"
POSITIVE={"good","great","happy","love","excellent","श्रेष्ठ","अच्छा","प्रेम","उत्तम"}
NEGATIVE={"bad","sad","hate","poor","danger","खराब","दुख","घृणा","खतरा"}
LABELS=("positive-pattern","negative-pattern","neutral-or-uncertain")
CASES=[
("en-pos-01","great research","positive-pattern"),("en-pos-02","excellent work","positive-pattern"),
("en-neg-01","bad result","negative-pattern"),("en-neg-02","danger poor outcome","negative-pattern"),
("en-neutral-01","research paper","neutral-or-uncertain"),("hi-pos-01","श्रेष्ठ प्रेम","positive-pattern"),
("hi-pos-02","अच्छा और उत्तम","positive-pattern"),("hi-neg-01","खराब परिणाम","negative-pattern"),
("hi-neg-02","दुख और खतरा","negative-pattern"),("hi-neutral-01","अनुसंधान प्रणाली","neutral-or-uncertain"),
("mixed-pos-01","great प्रेम","positive-pattern"),("mixed-neg-01","bad खतरा","negative-pattern"),
("mixed-conflict-01","great bad","neutral-or-uncertain")]

def infer(text:str)->tuple[str,list[str],float]:
    tokens=re.findall(r"[\w\u0900-\u097F]+",text.lower())
    pos=sorted(set(tokens)&POSITIVE); neg=sorted(set(tokens)&NEGATIVE)
    if len(pos)>len(neg): return "positive-pattern",pos,min(.98,.75+.10*len(pos))
    if len(neg)>len(pos): return "negative-pattern",neg,min(.98,.75+.10*len(neg))
    return "neutral-or-uncertain",pos+neg,.50 if pos or neg else .60

def evaluate(rows):
    y=[r["expected"] for r in rows]; p=[r["predicted"] for r in rows]
    correct=sum(a==b for a,b in zip(y,p)); per=[]
    for label in LABELS:
        tp=sum(a==label and b==label for a,b in zip(y,p))
        fp=sum(a!=label and b==label for a,b in zip(y,p)); fn=sum(a==label and b!=label for a,b in zip(y,p))
        precision=tp/(tp+fp) if tp+fp else 0.0; recall=tp/(tp+fn) if tp+fn else 0.0
        f1=2*precision*recall/(precision+recall) if precision+recall else 0.0
        per.append((precision,recall,f1))
    bins=[[] for _ in range(10)]
    for row in rows:
        idx=min(9,int(max(0,min(1,row["confidence"]))*10)); bins[idx].append(row)
    ece=0.0
    for b in bins:
        if not b: continue
        conf=sum(r["confidence"] for r in b)/len(b); acc=sum(r["correct"] for r in b)/len(b)
        ece += len(b)/len(rows)*abs(conf-acc)
    return {"accuracy":round(correct/len(rows),6),
            "macro_precision":round(sum(x[0] for x in per)/3,6),
            "macro_recall":round(sum(x[1] for x in per)/3,6),
            "macro_f1":round(sum(x[2] for x in per)/3,6),
            "expected_calibration_error":round(ece,6)}

def main():
    rows=[]; correct=0
    for case_id,text,expected in CASES:
        predicted,evidence,confidence=infer(text); ok=predicted==expected; correct+=int(ok)
        rows.append({"id":case_id,"expected":expected,"predicted":predicted,"evidence":evidence,
                     "confidence":confidence,"correct":ok,"verification_state":"UNVERIFIED"})
    metrics=evaluate(rows)
    record={"benchmark_id":"supreme-nlp-reference-v2","task":"multilingual lexical-pattern-regression",
            "population_scope":"fixed multilingual regression fixture","dataset_fingerprint":"fixture-embedded-v2",
            "model":{"name":"deterministic-baseline-nlp","version":"0.3"},"metrics":metrics,
            "sample_count":len(rows),"correct_count":correct,"verification_state":"UNVERIFIED",
            "provenance":["embedded benchmark fixture","factory/supreme_nlp_benchmark.py"],
            "limitations":["tiny fixed fixture","lexical baseline only","not representative of general language understanding",
                           "not evidence of subjective feeling, consciousness or intention"],"cases":rows}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(record,ensure_ascii=False,indent=2))
    if correct != len(CASES): raise SystemExit("Supreme NLP regression benchmark failed")

if __name__=="__main__": main()
