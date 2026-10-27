#!/usr/bin/env python3
"""Validate protected-source records and fail on hash/provenance errors."""
import hashlib,json,sys
from pathlib import Path
REQUIRED={"source_id","exact_text","language","captured_at","content_hash","provenance","preservation_status"}
def main():
    if len(sys.argv)!=2: raise SystemExit("Usage: validate_protected_sources.py <jsonl>")
    p=Path(sys.argv[1])
    if not p.is_file(): raise SystemExit("Missing protected source file: "+str(p))
    seen=set(); errors=[]
    for n,raw in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
        if not raw.strip(): continue
        try: row=json.loads(raw)
        except json.JSONDecodeError as e: errors.append(f"{p}:{n}: invalid JSON: {e}"); continue
        miss=REQUIRED-row.keys()
        if miss: errors.append(f"{p}:{n}: missing fields: {sorted(miss)}"); continue
        if row["source_id"] in seen: errors.append(f"{p}:{n}: duplicate source_id: {row['source_id']}")
        seen.add(row["source_id"])
        if not isinstance(row["exact_text"],str): errors.append(f"{p}:{n}: exact_text must be string"); continue
        if row["content_hash"]!=hashlib.sha256(row["exact_text"].encode("utf-8")).hexdigest(): errors.append(f"{p}:{n}: content_hash mismatch")
        prov=row["provenance"]
        if not isinstance(prov,dict) or not prov.get("origin") or not prov.get("captured_at") or not prov.get("locator"): errors.append(f"{p}:{n}: incomplete provenance")
        if row["preservation_status"] not in {"CAPTURED","VERIFIED","QUARANTINED","SUPERSEDED"}: errors.append(f"{p}:{n}: invalid preservation_status")
    if errors: print("\n".join(errors),file=sys.stderr); return 1
    print(f"Protected source validation OK: {len(seen)} record(s)"); return 0
if __name__=="__main__": raise SystemExit(main())
