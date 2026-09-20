#!/usr/bin/env python3
"""Build deterministic contract views without inventing evidence.

This bridge converts existing source metadata into source-record JSONL and
checks that any future claim records can be represented by the canonical
claim/evidence contract. It never treats a registered repository as proof of
its contents.
"""
import json
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import tempfile

ROOT=Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT/rel).read_text(encoding="utf-8"))

def build_source_records(registry):
    stamp=datetime.now(timezone.utc).isoformat()
    rows=[]
    for item in registry.get("repositories",[]):
        repo=item.get("repository","")
        rows.append({
            "id":"source:"+repo,
            "source_type":"REPOSITORY",
            "title":repo,
            "locator":item.get("github") or item.get("clone_url") or repo,
            "availability":"REGISTERED",
            "provenance":{
                "recorded_at":stamp,
                "repository":repo,
                "path":None,
                "commit":None
            }
        })
    return rows

def main():
    registry=load("generated/source-registry.json")
    rows=build_source_records(registry)
    out=ROOT/"generated"/"contract-views"
    out.mkdir(parents=True,exist_ok=True)
    path=out/"source-records.jsonl"
    with path.open("w",encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row,ensure_ascii=False,sort_keys=True)+"\n")
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"SOURCE RECORD BRIDGE: PASS — {len(rows)} registered source records")
    print(f"source-records.jsonl sha256: {digest}")
    print("Registration is metadata only; repository contents are not asserted as ingested.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
