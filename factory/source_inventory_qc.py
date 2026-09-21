#!/usr/bin/env python3
"""Fail-closed QC for the source inventory layer."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
INPUT = GEN / "source-inventory.jsonl"
REPORT = GEN / "SOURCE-INVENTORY-QC.json"

def main():
    errors = []
    ids = set()
    count = 0
    if not INPUT.exists() or INPUT.stat().st_size == 0:
        errors.append({"error":"missing_or_empty_source_inventory"})
    else:
        for line_no, line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            count += 1
            try:
                row = json.loads(line)
            except Exception as exc:
                errors.append({"line":line_no,"error":f"invalid_json:{exc}"})
                continue
            required = ["source_id","source_repository","source_path_or_url","source_type",
                        "source_status","title_or_label","content_hash","recorded_at",
                        "version","attribution","parent_source_id","notes"]
            for key in required:
                if key not in row:
                    errors.append({"line":line_no,"error":f"missing:{key}"})
            sid = row.get("source_id")
            if sid in ids:
                errors.append({"line":line_no,"error":"duplicate_source_id"})
            if sid:
                ids.add(sid)
            h = row.get("content_hash","")
            if len(h) != 64 or any(c not in "0123456789abcdef" for c in h):
                errors.append({"line":line_no,"error":"invalid_content_hash"})
            if row.get("source_status") != "REVIEW":
                errors.append({"line":line_no,"error":"unreviewed_inventory_must_remain_REVIEW"})
    report = {
        "version":1,
        "record_count":count,
        "unique_source_ids":len(ids),
        "error_count":len(errors),
        "publication_gate":"PASS" if not errors else "BLOCK",
        "generated_output_is_not_source":True,
        "independent_verification":"NOT_VERIFIED",
        "errors":errors,
    }
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
