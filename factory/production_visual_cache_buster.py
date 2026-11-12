#!/usr/bin/env python3
"""Refresh public product-page visual URLs when a product SVG/QR asset changes.

Production-only concern: this is cache invalidation for published visuals, not a
verification workflow. A changed visual gets a deterministic content hash in its
URL so GitHub Pages/CDN/browser caches cannot keep serving the previous asset.
"""
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products" / "concrete"
VISUALS = ROOT / "products" / "visuals"
QR = VISUALS / "qr"

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]

def refresh(path: Path) -> bool:
    pid = path.stem.lower()
    visual = VISUALS / f"{pid}.svg"
    qr = QR / f"{pid}.svg"
    if not visual.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    old_visual_prefix = f'../visuals/{pid}.svg'
    new_visual = f'{old_visual_prefix}?v={digest(visual)}'
    changed = False
    if old_visual_prefix in text and new_visual not in text:
        text = text.replace(old_visual_prefix, new_visual)
        changed = True
    if qr.exists():
        old_qr_prefix = f'../visuals/qr/{pid}.svg'
        new_qr = f'{old_qr_prefix}?v={digest(qr)}'
        if old_qr_prefix in text and new_qr not in text:
            text = text.replace(old_qr_prefix, new_qr)
            changed = True
    if changed:
        path.write_text(text, encoding="utf-8")
    return changed

def main():
    changed = 0
    for page in sorted(PRODUCTS.glob("SP-*.html")):
        changed += int(refresh(page))
    print(f"VISUAL_CACHE_REFRESH_CHANGED={changed}")

if __name__ == "__main__":
    main()
