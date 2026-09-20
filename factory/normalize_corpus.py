#!/usr/bin/env python3
"""Deterministically map content-record JSONL into canonical corpus-unit metadata.

This stage does not read or invent source meaning. It creates traceable units
from already emitted content records; claims and evidence are downstream.
"""
import argparse, json
from pathlib import Path

def normalize(rows):
    out=[]
    for row in rows:
        status=row.get("content_status")
        if status=="AVAILABLE":
            unit_status="READY_FOR_ANALYSIS"
            unit_type="TEXT_FILE"
        elif status=="BINARY_SKIPPED":
            unit_status="BINARY_SKIPPED"
            unit_type="BINARY_REFERENCE"
        else:
            unit_status="UNAVAILABLE"
            unit_type="UNAVAILABLE_REFERENCE"
        out.append({
            "id":"unit:"+row["id"],
            "content_id":row["id"],
            "source_path":row["source_path"],
            "content_hash":row["content_hash"],
            "unit_type":unit_type,
            "status":unit_status,
            "language_hint":row.get("language_hint"),
            "provenance":{"source_record":row["id"]}
        })
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    a=p.parse_args()
    rows=[json.loads(x) for x in Path(a.input).read_text(encoding="utf-8").splitlines() if x.strip()]
    units=normalize(rows)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text("".join(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n" for x in units),encoding="utf-8")
    print(f"CORPUS_UNITS: {len(units)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
