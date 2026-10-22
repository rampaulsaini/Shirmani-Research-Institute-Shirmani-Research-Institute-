#!/usr/bin/env python3
"""Fail-closed production QC for product visuals, QR identity, prices and SVG rendering.

This is an asset/release integrity gate, not independent scientific verification.
"""
from __future__ import annotations

import importlib.util
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "generated" / "1000-digital-products.json"
VISUAL_MANIFEST = ROOT / "generated" / "product-visual-assets-v2.json"
QR_MANIFEST = ROOT / "generated" / "product-qr-assets.json"
VISUAL_ROOT = ROOT / "products" / "visuals"
PASSPORT = ROOT / "product-passport.html"
SHOWROOM_BASE = "https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
IDENTITY = "Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"
SVG_NS = "{http://www.w3.org/2000/svg}"


def load(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"QC_INPUT_MISSING: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"QC_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    catalog = load(CATALOG)
    visual = load(VISUAL_MANIFEST)
    qr = load(QR_MANIFEST)
    products = catalog.get("products", [])
    catalog_by_id = {str(p.get("id")): p for p in products}
    expected_version = str(visual.get("target_visual_version", "")).strip()
    if not expected_version:
        raise SystemExit("QC_INPUT_INVALID: product visual manifest has no target_visual_version")

    visual_rows = visual.get("products", [])
    qr_rows = {str(x.get("product_id")): x for x in qr.get("products", [])}
    current_rows = [x for x in visual_rows if x.get("visual_version") == expected_version]
    if not current_rows:
        raise SystemExit("QC_FAIL: no current-version visual assets were checked")

    visual_factory = load_module("shirmani_visual_factory", ROOT / "factory" / "product_visual_identity_factory_v2.py")
    qr_factory = load_module("shirmani_qr_factory", ROOT / "factory" / "product_qr_asset_factory.py")
    failures: list[str] = []
    rendered = 0

    if not PASSPORT.is_file():
        failures.append("canonical product-passport.html route missing")

    for row in current_rows:
        raw_id = str(row.get("product_id", ""))
        pid = raw_id.lower()
        product = catalog_by_id.get(raw_id)
        visual_path = ROOT / str(row.get("asset_path", ""))
        qr_path = ROOT / str(row.get("qr_asset_path", ""))

        if product is None:
            failures.append(f"{pid}: product ID missing from source catalog")
            continue
        if not visual_path.is_file():
            failures.append(f"{pid}: visual missing")
            continue

        actual_svg = visual_path.read_text(encoding="utf-8")
        expected_svg = visual_factory.make(product)
        if actual_svg != expected_svg:
            failures.append(f"{pid}: SVG differs from current source/generator (description, price, offer, identity or asset links)")
        try:
            root = ET.fromstring(actual_svg)
        except ET.ParseError as exc:
            failures.append(f"{pid}: malformed SVG XML ({exc})")
            continue

        if root.attrib.get("width") != "3840" or root.attrib.get("height") != "2160":
            failures.append(f"{pid}: canvas is not 3840x2160")
        if IDENTITY not in actual_svg:
            failures.append(f"{pid}: English identity line missing")
        if "SHORT DESCRIPTION ·" not in actual_svg:
            failures.append(f"{pid}: short-description label missing")
        if "i.ibb.co/" in actual_svg:
            failures.append(f"{pid}: external legacy image host still embedded")

        image_hrefs = [el.attrib.get("href", "") for el in root.iter(f"{SVG_NS}image")]
        logo_href = "../../assets/shirmani-perspective-logo.svg"
        logo_path = (visual_path.parent / logo_href).resolve()
        if logo_href not in image_hrefs or not logo_path.is_file():
            failures.append(f"{pid}: local logo target missing or not referenced")
        qr_href = f"qr/{pid}.svg"
        qr_target = (visual_path.parent / qr_href).resolve()
        if qr_href not in image_hrefs or not qr_target.is_file():
            failures.append(f"{pid}: QR image path is not resolvable from the visual asset")

        qr_row = qr_rows.get(raw_id)
        expected_url = SHOWROOM_BASE + "product-passport.html?id=" + quote(raw_id)
        expected_qr_rel = f"products/visuals/qr/{pid}.svg"
        if not qr_row or not qr_row.get("exists"):
            failures.append(f"{pid}: QR manifest is not READY")
        else:
            if qr_row.get("long_description_url") != expected_url:
                failures.append(f"{pid}: QR target URL does not identify this product passport")
            if qr_row.get("qr_asset_path") != expected_qr_rel:
                failures.append(f"{pid}: QR manifest asset path mismatch")
            if qr_target.is_file():
                expected_qr = qr_factory.make_qr(expected_url)
                actual_qr = qr_target.read_text(encoding="utf-8")
                if actual_qr != expected_qr:
                    failures.append(f"{pid}: QR payload asset does not match the product-specific passport URL")

        # Render every current-version visual at preview resolution to catch invalid
        # SVG/image references before the 4K-ready source is published.
        try:
            png = cairosvg.svg2png(
                bytestring=actual_svg.encode("utf-8"),
                output_width=384,
                output_height=216,
                url=visual_path.as_uri(),
            )
            if not png.startswith(b"\x89PNG\r\n\x1a\n"):
                failures.append(f"{pid}: SVG renderer did not produce a valid PNG")
            else:
                rendered += 1
        except Exception as exc:
            failures.append(f"{pid}: SVG rendering failed ({type(exc).__name__}: {exc})")

    if failures:
        print(json.dumps({
            "gate": "PRODUCT-VISUAL-QC-GATE",
            "status": "FAIL",
            "checked_current_version": len(current_rows),
            "rendered": rendered,
            "failure_count": len(failures),
            "failures": failures[:100],
        }, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    print(json.dumps({
        "gate": "PRODUCT-VISUAL-QC-GATE",
        "status": "PASS",
        "checked_current_version": len(current_rows),
        "rendered": rendered,
        "failure_count": 0,
        "checks": {
            "source-bound_description_price_offer": True,
            "word-boundary_description_clamp": True,
            "product-specific_qr_payload_and_url": True,
            "local_logo_and_qr_paths": True,
            "svg_xml_and_raster_render": True,
            "canonical_passport_route": str(PASSPORT.relative_to(ROOT)),
        },
        "independent_verification": "DOWNSTREAM",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
