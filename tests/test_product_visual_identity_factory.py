"""Production visual identity contract tests.

These tests protect the customer-facing production layer:
- unique product identity
- 3840x2160 / 16:9 4K-ready SVG
- local SHIRMANI logo
- local per-product QR route
- short description on the visual
- no dependency on third-party QR image URLs in generated masters
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FACTORY = ROOT / "factory" / "product_visual_identity_factory.py"
SHOWROOM_JS = ROOT / "showroom-product-visuals.js"


def test_visual_factory_contract_is_local_and_4k_ready():
    text = FACTORY.read_text(encoding="utf-8")
    assert 'width="3840" height="2160"' in text
    assert 'aspect_ratio":"16:9"' in text
    assert 'assets/shirmani-perspective-logo.svg' in text
    assert 'qr_rel="qr/"+pid.lower()+".svg"' in text
    assert "SHORT DESCRIPTION" in text
    assert "api.qrserver.com" not in text


def test_showroom_prefers_repository_assets():
    text = SHOWROOM_JS.read_text(encoding="utf-8")
    assert 'assets/shirmani-perspective-logo.svg' in text
    assert 'products/visuals/qr/' in text
    assert 'SCAN FOR LONG DESCRIPTION' in text
    assert "Beyond Comparison" in text
    assert "Beyond Time" in text
    assert "Beyond Words" in text
    assert "Beyond Love" in text


def test_identity_line_is_complete():
    text = FACTORY.read_text(encoding="utf-8")
    identity = (
        "Shiromani Rampal Saini — Beyond Comparison · Beyond Time · "
        "Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"
    )
    assert identity in text
