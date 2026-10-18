#!/usr/bin/env python3
"""Check local links in public-facing HTML pages before publishing them.

Usage:
  python factory/public_interface_link_smoke.py
  python factory/public_interface_link_smoke.py public-interface.html showroom-public.html

The checker is intentionally read-only. It reports missing local targets; it does
not rewrite links, delete files, or claim that external services are available.
"""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAGES = (
    "public-interface.html",
    "showroom-public.html",
)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key.lower() in {"href", "src", "action"} and value:
                self.links.append((value.strip(), self.getpos()[0]))


def resolve_local_target(source: Path, raw_url: str) -> Path | None:
    value = raw_url.strip()
    if not value or value.startswith("#") or value.startswith("//"):
        return None
    parts = urlsplit(value)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(parts.path)
    if not path:
        return None
    target = (ROOT / path.lstrip("/")) if path.startswith("/") else (source.parent / path)
    # Keep checks inside the repository; links escaping the root are reported.
    try:
        target.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return target
    return target


def main() -> int:
    pages = [Path(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else [
        Path(name) for name in DEFAULT_PAGES
    ]
    failures: list[str] = []
    checked_pages = 0
    checked_links = 0

    for relative_page in pages:
        source = (ROOT / relative_page).resolve()
        try:
            source.relative_to(ROOT.resolve())
        except ValueError:
            failures.append(f"{relative_page}: page path escapes repository root")
            continue
        if not source.is_file():
            failures.append(f"{relative_page}: page does not exist")
            continue

        parser = LinkParser()
        parser.feed(source.read_text(encoding="utf-8"))
        checked_pages += 1
        for raw_url, line in parser.links:
            target = resolve_local_target(source, raw_url)
            if target is None:
                continue
            checked_links += 1
            try:
                target.resolve().relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{relative_page}:{line}: local URL escapes repository: {raw_url}")
                continue
            if not target.exists():
                failures.append(f"{relative_page}:{line}: missing local target: {raw_url}")

    print(
        f"PUBLIC_INTERFACE_LINK_SMOKE pages={checked_pages} "
        f"local_links={checked_links} failures={len(failures)}"
    )
    for failure in failures:
        print(f"FAIL {failure}")
    if failures:
        return 1
    print("PASS: all checked local links resolve; external integrations were not tested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
