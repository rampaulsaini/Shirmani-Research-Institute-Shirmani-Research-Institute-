#!/usr/bin/env python3
"""Inventory exact protected-source files by byte hash; never rewrite source bytes."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"protected"/"user-source"
OUT=ROOT/"generated"/"protected-user-source-manifest.json"
def main():
    SRC.mkdir(parents=True,exist_ok=True)
    records=[]; now=datetime.now(timezone.utc).isoformat()
    for p in sorted(SRC.rglob("*")):
        if not p.is_file() or p.name.endswith(".meta.json"): continue
        data=p.read_bytes(); rel=p.relative_to(ROOT).as_posix()
        sha=hashlib.sha256(data).hexdigest()
        records.append({"source_id":"user-source-"+sha[:24],"path":rel,"content_sha256":sha,"byte_length":len(data),"captured_at":now,"verbatim":True})
    payload={"manifest_version":1,"generated_at":now,"source_root":"protected/user-source","record_count":len(records),"records":records,"integrity":{"source_bytes_modified":False,"missing_material_reconstructed":False}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Protected-source inventory: {len(records)} file(s)")
if __name__=="__main__": main()
