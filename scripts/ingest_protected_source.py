#!/usr/bin/env python3
"""Append one exact protected-source record without rewriting its text."""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path

def make_record(source_id,exact_text,language,source_kind,locator,parent_context=None):
    now=datetime.now(timezone.utc).isoformat()
    return {"source_id":source_id,"exact_text":exact_text,"language":language,
            "captured_at":now,"parent_context":parent_context,
            "content_hash":hashlib.sha256(exact_text.encode("utf-8")).hexdigest(),
            "provenance":{"origin":source_kind,"captured_at":now,"locator":locator},
            "preservation_status":"CAPTURED","derivative_ids":[]}

def main():
    if len(sys.argv)!=3: raise SystemExit("Usage: ingest_protected_source.py <source.json> <output.jsonl>")
    src=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    required=["source_id","exact_text","language","source_kind","locator"]
    missing=[k for k in required if k not in src]
    if missing: raise SystemExit("Missing fields: "+", ".join(missing))
    row=make_record(src["source_id"],src["exact_text"],src["language"],src["source_kind"],src["locator"],src.get("parent_context"))
    with Path(sys.argv[2]).open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")
    print(row["source_id"],row["content_hash"])

if __name__=="__main__": main()
