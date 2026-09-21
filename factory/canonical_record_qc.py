#!/usr/bin/env python3
"""Fail-closed validation for canonical knowledge records.

This validates structure, stable IDs, source hashes and active-state semantics.
It does not claim that canonical records are true; it only checks integrity and
traceability of the generated canonical layer.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
INPUT = GEN / "canonical-knowledge.jsonl"
MANIFEST = GEN / "canonical-knowledge-manifest.json"
REPORT = GEN / "CANONICAL-RECORD-QC.json"

def stable_id(row):
    key = "|".join([
        row.get("repository", ""),
        row.get("branch") or "",
        row.get("path", ""),
        row.get("source_hash", ""),
    ])
    return "ck_" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:24]

def main():
    errors = []
    seen = set()
    records = 0
    active = 0

    if not INPUT.exists() or INPUT.stat().st_size == 0:
        errors.append({"error": "missing_or_empty_canonical_knowledge"})
    else:
        for line_no, line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            records += 1
            try:
                row = json.loads(line)
            except Exception as exc:
                errors.append({"line": line_no, "error": f"invalid_json:{exc}"})
                continue

            required = ["id","repository","path","source_hash","text","source_type",
                        "first_seen_at","last_seen_at","active"]
            for key in required:
                if key not in row:
                    errors.append({"line": line_no, "error": f"missing:{key}"})

            rid = row.get("id")
            if rid in seen:
                errors.append({"line": line_no, "error": "duplicate_id"})
            if rid:
                seen.add(rid)
                if rid != stable_id(row):
                    errors.append({"line": line_no, "error": "stable_id_mismatch"})

            source_hash = row.get("source_hash")
            if source_hash:
                if source_hash != hashlib.sha256(str(row.get("text", "")).encode("utf-8")).hexdigest():
                    errors.append({"line": line_no, "error": "source_hash_mismatch"})

            if row.get("active") is True:
                active += 1

    manifest = {}
    if MANIFEST.exists():
        try:
            manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append({"error": f"invalid_manifest:{exc}"})
    else:
        errors.append({"error": "missing_canonical_manifest"})

    if manifest:
        if manifest.get("record_count") != records:
            errors.append({"error": "manifest_record_count_mismatch"})
        if manifest.get("active_record_count") != active:
            errors.append({"error": "manifest_active_record_count_mismatch"})
        if manifest.get("generated_output_is_not_source") is not True:
            errors.append({"error": "generated_output_source_boundary_missing"})

    report = {
        "version": 1,
        "records": records,
        "active_records": active,
        "unique_ids": len(seen),
        "error_count": len(errors),
        "publication_gate": "PASS" if not errors else "BLOCK",
        "generated_output_is_not_source": True,
        "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
