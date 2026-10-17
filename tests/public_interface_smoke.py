#!/usr/bin/env python3
"""Fast smoke checks for the public showroom's primary navigation pages.

This is a local-link/markup integrity check, not a browser rendering or security audit.
Run from the repository root: python3 tests/public_interface_smoke.py
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "showroom-public.html", ROOT / "heart-view-preview.html")
REQUIRED_TEXT = {
    "showroom-public.html": (
        "Public Showroom",
        "Writing / Research काम दें",
        "Heart-View Preview",
        "Product Catalogue",
    ),
    "heart-view-preview.html": (
        "Heart-View Preview",
        "Voice-to-Presentation Studio",
        "Lip-sync",
        "Live question-and-answer",
    ),
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if attrs_dict.get("id"):
            self.ids.append(attrs_dict["id"])
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"])

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)


def main() -> int:
    errors: list[str] = []
    parsed: dict[Path, PageParser] = {}

    for page in PAGES:
        if not page.is_file():
            errors.append(f"Missing required page: {page.relative_to(ROOT)}")
            continue
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
        parsed[page] = parser

        duplicates = sorted(key for key, count in Counter(parser.ids).items() if count > 1)
        if duplicates:
            errors.append(f"{page.relative_to(ROOT)} has duplicate id(s): {', '.join(duplicates)}")

        visible_text = " ".join(parser.text_parts)
        for phrase in REQUIRED_TEXT[page.name]:
            if phrase.casefold() not in visible_text.casefold():
                errors.append(f"{page.relative_to(ROOT)} is missing required navigation/content text: {phrase}")

        for href in parser.links:
            target = urlsplit(href)
            if target.scheme or target.netloc or not target.path:
                continue
            local_path = (page.parent / unquote(target.path)).resolve()
            if not local_path.is_relative_to(ROOT):
                errors.append(f"{page.relative_to(ROOT)} has a link escaping repository root: {href}")
                continue
            if not local_path.exists():
                errors.append(f"{page.relative_to(ROOT)} links to missing local target: {href}")
                continue
            if target.fragment and local_path.suffix.lower() in {".html", ".htm"}:
                if local_path in parsed:
                    target_ids = set(parsed[local_path].ids)
                    if unquote(target.fragment) not in target_ids:
                        errors.append(f"{page.relative_to(ROOT)} links to missing anchor: {href}")

    if errors:
        print("PUBLIC INTERFACE SMOKE CHECK: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PUBLIC INTERFACE SMOKE CHECK: PASS ({len(parsed)} pages parsed)")
    print("Checked duplicate IDs, required navigation copy, and local link targets.")
    print("Note: this is not a browser, accessibility, deployment, or provider-integration test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
