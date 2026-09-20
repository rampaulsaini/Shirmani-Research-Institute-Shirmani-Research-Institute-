#!/usr/bin/env python3
"""Deterministic metadata-only concept candidate extraction.

Concept candidates are derived only from source path/source type metadata.
No semantic claim is inferred from file content at this stage.
"""
import argparse,json,re
from pathlib import Path
STOP={"readme","docs","src","scripts","research","assets","code","documentation","markdown","html","json"}
def labelize(value):
    value=re.sub(r"[_\-.]+"," ",value).strip().lower()
    return re.sub(r"\s+"," ",value)
def extract(rows):
    out=[]; seen=set()
    for row in rows:
        candidates=[]
        source_type=row.get("source_type")
        if source_type: candidates.append(("SOURCE_TYPE",labelize(source_type)))
        path=row.get("source_path") or row.get("path") or ""
        for part in Path(path).parts[:-1]:
            label=labelize(part)
            if label and label not in STOP and len(label)>=3: candidates.append(("PATH_SEGMENT",label))
        for derivation,label in candidates:
            key=(row["id"],label)
            if key in seen: continue
            seen.add(key)
            out.append({"id":f"concept:{row['id']}:{label}","unit_id":str(row["id"]),"label":label,"derivation":derivation,"status":"CANDIDATE","provenance":{"content_hash":row["content_hash"]}})
    return out
def main():
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output"); a=p.parse_args()
    rows=[json.loads(x) for x in Path(a.input).read_text(encoding="utf-8").splitlines() if x.strip()]
    out=extract(rows); Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text("".join(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n" for x in out),encoding="utf-8")
    print(f"CONCEPT_CANDIDATES: {len(out)}")
if __name__=="__main__": raise SystemExit(main())
