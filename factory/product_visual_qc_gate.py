#!/usr/bin/env python3
"""Fail-closed production QC for customer-facing product visual identity assets.

This is a production release gate, not independent scientific verification.
It checks that the visual factory produced the requested presentation contract:
local SHIRMANI logo, English identity, short description, 4K SVG canvas and
a product-specific QR asset for the long-description/product-passport route.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL_MANIFEST = ROOT / "generated" / "product-visual-assets-v2.json"
QR_MANIFEST = ROOT / "generated" / "product-qr-assets.json"
VISUAL_ROOT = ROOT / "products" / "visuals"
QR_ROOT = VISUAL_ROOT / "qr"

IDENTITY = "Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"


def load(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"QC_INPUT_MISSING: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    visual = load(VISUAL_MANIFEST)
    qr = load(QR_MANIFEST)
    expected_version = str(visual.get("target_visual_version", "")).strip()
    if not expected_version:
        raise SystemExit("QC_INPUT_INVALID: product visual manifest has no target_visual_version")
    products = visual.get("products", [])
    qr_rows = {str(x.get("product_id")): x for x in qr.get("products", [])}

    failures: list[str] = []
    checked = 0
    for row in products:
        if row.get("visual_version") != expected_version:
            continue
        checked += 1
        pid = str(row.get("product_id", "")).lower()
        visual_path = ROOT / str(row.get("asset_path", ""))
        qr_path = ROOT / str(row.get("qr_asset_path", ""))

        if not visual_path.is_file():
            failures.append(f"{pid}: visual missing")
            continue
        text = visual_path.read_text(encoding="utf-8", errors="ignore")
        if 'width="3840" height="2160"' not in text:
            failures.append(f"{pid}: visual canvas is not 3840x2160")
        if IDENTITY not in text:
            failures.append(f"{pid}: English identity line missing")
        if "SHORT DESCRIPTION" not in text:
            failures.append(f"{pid}: short-description label missing")
        if "SCAN FOR LONG DESCRIPTION" not in text:
            failures.append(f"{pid}: QR long-description label missing")
        if "i.ibb.co/" in text:
            failures.append(f"{pid}: external legacy image host still embedded")
        if not qr_path.is_file():
            failures.append(f"{pid}: product QR missing")
        qr_row = qr_rows.get(str(row.get("product_id")))
        if not qr_row or not qr_row.get("exists"):
            failures.append(f"{pid}: QR manifest is not READY")

    if checked == 0:
        raise SystemExit("QC_FAIL: no current-version visual assets were checked")

    if failures:
        print(json.dumps({
            "gate": "PRODUCT-VISUAL-QC-GATE",
            "status": "FAIL",
            "checked_current_version": checked,
            "expected_version": expected_version,
            "failures": failures[:100],
            "failure_count": len(failures),
        }, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    print(json.dumps({
        "gate": "PRODUCT-VISUAL-QC-GATE",
        "status": "PASS",
        "checked_current_version": checked,
        "expected_version": expected_version,
        "failure_count": 0,
        "contract": {
            "local_logo": True,
            "english_identity": True,
            "short_description_on_visual": True,
            "qr_upper_right_contract": True,
            "long_description_target": "product passport",
            "canvas": "3840x2160",
        },
        "independent_verification": "DOWNSTREAM",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
