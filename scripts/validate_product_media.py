#!/usr/bin/env python3
"""Validate product-media records without pretending external assets were tested."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "shirmani-product-media-contract.json"
REQUIRED = set(json.loads(CONTRACT.read_text(encoding="utf-8"))["required_fields"])
ALLOWED_EVIDENCE = set(json.loads(CONTRACT.read_text(encoding="utf-8"))["allowed_evidence_states"])
ALLOWED_RELEASE = set(json.loads(CONTRACT.read_text(encoding="utf-8"))["allowed_release_states"])
MEDIA_FIELDS = ("passport_url", "qr_asset_path", "vip_screenshot_path", "demo_video_path",
                "usage_guide_url", "original_logo_asset_path")


def validate(records):
    errors = []
    seen_ids, seen_names, seen_qrs, seen_demos = set(), set(), set(), set()
    for i, record in enumerate(records):
        where = f"record[{i}]"
        missing = REQUIRED - set(record)
        if missing:
            errors.append(f"{where}: missing fields: {', '.join(sorted(missing))}")
            continue
        pid = record["product_id"]
        if not isinstance(pid, str) or not pid.strip():
            errors.append(f"{where}: product_id must be non-empty")
        elif pid in seen_ids:
            errors.append(f"{where}: duplicate product_id {pid}")
        seen_ids.add(pid)
        name = record["name"]
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{where}: name must be non-empty")
        elif name in seen_names:
            errors.append(f"{where}: duplicate product name {name}")
        seen_names.add(name)
        if record["evidence_state"] not in ALLOWED_EVIDENCE:
            errors.append(f"{where}: invalid evidence_state")
        if record["release_state"] not in ALLOWED_RELEASE:
            errors.append(f"{where}: invalid release_state")
        for field in MEDIA_FIELDS:
            value = record[field]
            if not isinstance(value, str):
                errors.append(f"{where}: {field} must be a string")
        qr = record["qr_asset_path"]
        if qr:
            if qr in seen_qrs:
                errors.append(f"{where}: QR asset reused: {qr}")
            seen_qrs.add(qr)
        demo = record["demo_video_path"]
        if demo:
            if demo in seen_demos:
                errors.append(f"{where}: demo video reused: {demo}")
            seen_demos.add(demo)
        media_complete = all(isinstance(record[f], str) and record[f].strip() for f in MEDIA_FIELDS)
        if record["release_state"] in {"VERIFIED", "PUBLISHED"} and not media_complete:
            errors.append(f"{where}: cannot be {record['release_state']} while required media fields are blank")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_product_media.py path/to/records.json")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    records = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(records, dict):
        records = [records]
    problems = validate(records)
    if problems:
        print("\n".join(f"FAIL: {item}" for item in problems))
        raise SystemExit(1)
    print(f"PASS: {len(records)} product record(s) passed structural checks.")
    print("Note: structural checks do not verify that URLs, files, QR scans, screenshots, or videos work.")
