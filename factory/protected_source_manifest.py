#!/usr/bin/env python3
"""Inventory protected user-source bytes without rewriting them."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SOURCE_ROOT=ROOT/"protected"/"user-source"; OUT=ROOT/"generated"/"protected-user-source-manifest.json"
TEXT_SUFFIXES={".md",".txt",".html",".htm",".json",".yaml",".yml",".csv",".xml",".srt",".vtt"}
def digest(data): return hashlib.sha256(data).hexdigest()
def language_for(path):
    sidecar=path.with_suffix(path.suffix+".meta.json")
    if sidecar.exists():
        try:
            value=json.loads(sidecar.read_text(encoding="utf-8")).get("language")
            if isinstance(value,str) and value.strip(): return value.strip()
        except Exception: pass
    return "unspecified"
def source_id(rel,sha): return "user-source-"+hashlib.sha256((rel+":"+sha).encode("utf-8")).hexdigest()[:24]
def main():
    SOURCE_ROOT.mkdir(parents=True,exist_ok=True); records=[]
    for path in sorted(SOURCE_ROOT.rglob("*")):
        if not path.is_file() or path.name.endswith(".meta.json"): continue
        data=path.read_bytes(); rel=path.relative_to(ROOT).as_posix(); sha=digest(data)
        records.append({"id":source_id(rel,sha),"source_type":"USER_ORIGINAL_TEXT" if path.suffix.lower() in TEXT_SUFFIXES else "OTHER_USER_SOURCE","language":language_for(path),"path":rel,"content_sha256":sha,"byte_length":len(data),"provenance":{"recorded_at":datetime.now(timezone.utc).isoformat(),"capture_method":"repository_protected_source_inventory"},"preservation":{"verbatim":True,"derivative_of":None,"transformations_allowed":False}})
    payload={"version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"source_root":SOURCE_ROOT.relative_to(ROOT).as_posix(),"record_count":len(records),"records":records,"integrity":{"source_bytes_modified":False,"historical_missing_material_reconstructed":False,"derivatives_included_as_original":False}}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"record_count":len(records),"output":str(OUT.relative_to(ROOT))},ensure_ascii=False))
if __name__=="__main__": main()
