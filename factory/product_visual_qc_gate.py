#!/usr/bin/env python3
"""Fail-closed production QC for customer-facing product visual identity assets.

This is a production release gate, not independent scientific verification.
It checks that the visual factory produced the requested presentation contract:
local SHIRMANI logo, English identity, short description, 4K SVG canvas and
a product-specific QR asset for the long-description/product-passport route.
"""
from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL_MANIFEST = ROOT / "generated" / "product-visual-assets-v2.json"
QR_MANIFEST = ROOT / "generated" / "product-qr-assets.json"
VISUAL_ROOT = ROOT / "products" / "visuals"
QR_ROOT = VISUAL_ROOT / "qr"
CATALOG_PATH = ROOT / "generated" / "1000-digital-products.json"
PASSPORT_BASE = "https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/product-passport.html?id="

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
    catalog = load(CATALOG_PATH).get("products", [])
    catalog_rows = {str(x.get("id")): x for x in catalog if isinstance(x, dict)}
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
        try:
            svg_root = ET.fromstring(text)
        except ET.ParseError as exc:
            failures.append(f"{pid}: SVG XML parse failed: {exc}")
            continue
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
        expected_qr_href = f'qr/{pid}.svg'
        if f'href="{expected_qr_href}"' not in text:
            failures.append(f"{pid}: visual does not reference its matching local QR asset")
        if not qr_path.is_file():
            failures.append(f"{pid}: product QR missing")
        qr_row = qr_rows.get(str(row.get("product_id")))
        if not qr_row or not qr_row.get("exists") or qr_row.get("state") != "READY":
            failures.append(f"{pid}: QR manifest is not READY")
        elif qr_row.get("long_description_url") != PASSPORT_BASE + str(row.get("product_id")):
            failures.append(f"{pid}: QR target does not match this product passport")
        source_product = catalog_rows.get(str(row.get("product_id")))
        if not source_product:
            failures.append(f"{pid}: canonical product record missing")
        else:
            expected_price = int(source_product.get("offer_price_inr", source_product.get("price_inr", 0)) or 0)
            if f"₹{expected_price:,}</text>" not in text:
                failures.append(f"{pid}: visual price does not match canonical product price")
        description_nodes = [
            node for node in svg_root.iter()
            if node.tag.endswith("text") and "SHORT DESCRIPTION" in "".join(node.itertext())
        ]
        if not description_nodes:
            failures.append(f"{pid}: short description text node missing")
        elif not any(child.tag.endswith("tspan") for child in description_nodes[0]):
            failures.append(f"{pid}: short description is not wrapped into measurable SVG lines")
        elif any("…" in "".join(child.itertext()) for child in description_nodes[0] if child.tag.endswith("tspan")):
            last_line = next((child for child in reversed(list(description_nodes[0])) if child.tag.endswith("tspan")), None)
            if last_line is None or not "".join(last_line.itertext()).rstrip().endswith("…"):
                failures.append(f"{pid}: truncated description is not marked at a word boundary")

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
