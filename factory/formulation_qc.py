#!/usr/bin/env python3
"""Fail-closed QC for deterministic formulation records."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
def sha(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
def artifact_text(kind, aid):
    if kind=="verse":
        p=OUT/"verse-corpus.jsonl"
        if not p.exists(): return None
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip() and str(json.loads(line).get("id"))==str(aid):
                return json.loads(line).get("text","")
        return None
    if kind=="book": p=OUT/("book-"+str(aid)+".md")
    elif kind=="research-paper": p=OUT/("research-paper-draft-"+str(aid)+".md")
    else: return None
    return p.read_text(encoding="utf-8") if p.exists() else None
def main():
    p=OUT/"formulation-records.jsonl"
    if not p.exists(): raise SystemExit("formulation-records.jsonl is missing")
    seen=set(); errors=[]; count=0; passed=0
    required=("id","artifact_id","kind","formulation_type","inputs","procedure","result","limitations","verification","provenance")
    for n,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        count+=1
        try: r=json.loads(line)
        except Exception as e:
            errors.append({"line":n,"error":"invalid_json:"+str(e)}); continue
        for k in required:
            if k not in r: errors.append({"line":n,"error":"missing:"+k})
        if r.get("id") in seen: errors.append({"line":n,"error":"duplicate_id"})
        seen.add(r.get("id"))
        text=artifact_text(r.get("kind"),r.get("artifact_id"))
        expected=sha(text) if text is not None else None
        inputs=r.get("inputs") or {}; result=r.get("result") or {}
        if inputs.get("content_sha256_from_artifact")!=expected:
            errors.append({"line":n,"error":"artifact_hash_reconstruction_mismatch"})
        if result.get("hash_match") is not (text is not None and expected==inputs.get("content_sha256_from_reasoning")):
            errors.append({"line":n,"error":"hash_match_result_mismatch"})
        if result.get("status")!="PASS":
            errors.append({"line":n,"error":"formulation_not_pass"})
        v=r.get("verification") or {}
        if v.get("status")!="NOT_VERIFIED" or v.get("independent") is not False or v.get("required") is not True:
            errors.append({"line":n,"error":"verification_gate_invalid"})
        if not isinstance(r.get("limitations"),list) or not r.get("limitations"):
            errors.append({"line":n,"error":"missing_limitations"})
        if not isinstance(r.get("source_ids") if "source_ids" in r else inputs.get("source_ids"),list):
            errors.append({"line":n,"error":"source_ids_not_list"})
        if not errors or errors[-1].get("line")!=n: passed+=1
    report={"version":1,"records":count,"passed_records":passed,"error_count":len(errors),
            "publication_gate":"PASS" if not errors else "BLOCK","errors":errors}
    (OUT/"FORMULATION-QC.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)
if __name__=="__main__": main()
