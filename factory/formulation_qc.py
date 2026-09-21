#!/usr/bin/env python3
"""Fail-closed QC for deterministic formulation records."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"
def sha(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
_VERSE_INDEX = None

def artifact_text(kind, aid):
    global _VERSE_INDEX
    if kind=="verse":
        if _VERSE_INDEX is None:
            p=OUT/"verse-corpus.jsonl"
            if not p.exists(): return None
            _VERSE_INDEX={}
            for line in p.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    row=json.loads(line)
                    _VERSE_INDEX[str(row.get("id"))]=row.get("text","")
        return _VERSE_INDEX.get(str(aid))
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
        local=[]
        try: r=json.loads(line)
        except Exception as e:
            errors.append({"line":n,"error":"invalid_json:"+str(e)}); continue
        for k in required:
            if k not in r: local.append("missing:"+k)
        rid=r.get("id")
        if rid in seen: local.append("duplicate_id")
        seen.add(rid)
        text=artifact_text(r.get("kind"),r.get("artifact_id"))
        expected=sha(text) if text is not None else None
        inputs=r.get("inputs") or {}; result=r.get("result") or {}
        expected_match=(text is not None and expected==inputs.get("content_sha256_from_reasoning"))
        if inputs.get("content_sha256_from_artifact")!=expected: local.append("artifact_hash_reconstruction_mismatch")
        if result.get("hash_match") is not expected_match: local.append("hash_match_result_mismatch")
        if result.get("status")!="PASS": local.append("formulation_not_pass")
        v=r.get("verification") or {}
        if v.get("status")!="NOT_VERIFIED" or v.get("independent") is not False or v.get("required") is not True:
            local.append("verification_gate_invalid")
        if not isinstance(r.get("limitations"),list) or not r.get("limitations"): local.append("missing_limitations")
        if not isinstance(inputs.get("source_ids"),list): local.append("source_ids_not_list")
        if local:
            errors.extend({"line":n,"error":e} for e in local)
        else:
            passed+=1
    report={"version":1,"records":count,"passed_records":passed,"error_count":len(errors),
            "publication_gate":"PASS" if not errors else "BLOCK","errors":errors}
    (OUT/"FORMULATION-QC.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)
if __name__=="__main__": main()
