#!/usr/bin/env python3
"""Fast integrity checks for the public showroom's customer-facing routes.

Run from the repository root: python3 tests/public_interface_smoke.py
This is not a browser rendering, accessibility, deployment, or security audit.
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    ROOT / "showroom-public.html",
    ROOT / "heart-view-preview.html",
    ROOT / "index.html",
    ROOT / "income-command-center.html",
    ROOT / "supreme-showroom.html",
    ROOT / "supreme-public-production-showroom.html",
    ROOT / "writing-research-enquiry.html",
    ROOT / "first-paid-pilot-offer.html",
)
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
REQUIRED_SHOWROOM_ROUTES = (
    "supreme-showroom.html",
    "writing-research-enquiry.html",
    "showroom/product-demo-test-drive-hub.html",
    "production-progress-map.html",
    "heart-view-preview.html",
    "voice-to-presentation-studio.html",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.text_parts: list[str] = []
        self.label_for: list[str] = []
        self.input_ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if attrs_dict.get("id"):
            self.ids.append(attrs_dict["id"])
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"])
        if tag == "label" and attrs_dict.get("for"):
            self.label_for.append(attrs_dict["for"])
        if tag in {"input", "select", "textarea"} and attrs_dict.get("id"):
            self.input_ids.append(attrs_dict["id"])

    def handle_data(self, data: str) -> None:
        self.text_parts.append(data)


def parse_html(path: Path, errors: list[str], cache: dict[Path, PageParser]) -> PageParser | None:
    if path in cache:
        return cache[path]
    if not path.is_file():
        errors.append(f"Missing required page: {path.relative_to(ROOT)}")
        return None
    parser = PageParser()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
    except (OSError, UnicodeError) as exc:
        errors.append(f"Could not read {path.relative_to(ROOT)}: {exc}")
        return None
    cache[path] = parser
    duplicates = sorted(key for key, count in Counter(parser.ids).items() if count > 1)
    if duplicates:
        errors.append(f"{path.relative_to(ROOT)} has duplicate id(s): {', '.join(duplicates)}")
    return parser


def main() -> int:
    errors: list[str] = []
    parsed: dict[Path, PageParser] = {}

    for page in PAGES:
        parser = parse_html(page, errors, parsed)
        if parser is None:
            continue
        visible_text = " ".join(parser.text_parts)
        for phrase in REQUIRED_TEXT.get(page.name, ()):
            if phrase.casefold() not in visible_text.casefold():
                errors.append(f"{page.relative_to(ROOT)} is missing required navigation/content text: {phrase}")

    showroom = ROOT / "showroom-public.html"
    showroom_parser = parsed.get(showroom)
    if showroom_parser:
        local_paths = {
            unquote(urlsplit(href).path)
            for href in showroom_parser.links
            if not urlsplit(href).scheme and not urlsplit(href).netloc and urlsplit(href).path
        }
        for required in REQUIRED_SHOWROOM_ROUTES:
            if required not in local_paths:
                errors.append(f"showroom-public.html is missing a required customer route: {required}")

    # Public Interface v3 live telemetry contract (without recursively crawling its legacy links).
    public_v3 = ROOT / "public-interface-v3.html"
    if not public_v3.is_file():
        errors.append("Missing required public entry point: public-interface-v3.html")
    else:
        source = public_v3.read_text(encoding="utf-8")
        for required in (
            'id="cycles24h"', 'id="success24h"', 'id="failed24h"',
            'id="activeRuns"', 'id="productionFreshness"',
            'api.github.com/repos/', '/actions/runs?branch=main',
            'generated/live-production-state.json', 'NOT CONNECTED',
            'स्वतंत्र QC', 'शून्य नहीं माना गया',
        ):
            if required.casefold() not in source.casefold():
                errors.append(f"public-interface-v3.html is missing telemetry/truth-boundary requirement: {required}")
        if "setInterval(" in source:
            errors.append("public-interface-v3.html must not poll GitHub API continuously and risk exhausting unauthenticated rate limits")

    # Check the current canonical income funnel's direct links too. Keep this
    # deliberately one level deep: legacy pages linked from these entry points
    # are not recursively crawled, but every CTA target must exist in the repo.
    direct_customer_pages = (
        ROOT / "public-interface-v3.html",
        ROOT / "showroom/first-client-pilot-desk.html",
        ROOT / "income-action-center.html",
        ROOT / "showroom/global-product-sales-desk.html",
        ROOT / "services-writing-research.html",
    )
    for page in direct_customer_pages:
        parse_html(page, errors, parsed)

    # The primary public entry must keep the paid-pilot path visible and honest.
    public_v3_source = (ROOT / "public-interface-v3.html").read_text(encoding="utf-8")
    for required in (
        "id=\"income-first\"",
        "₹499",
        "₹999",
        "₹1,499",
        "showroom/first-client-pilot-desk.html",
        "income-action-center.html",
        "wa.me/918082935186",
        "mailto:sainirampaul60@gmail.com",
        "वे अपने-आप संदेश नहीं भेजते",
        "ग्राहक की स्वीकृति",
    ):
        if required.casefold() not in public_v3_source.casefold():
            errors.append(f"public-interface-v3.html is missing income-funnel requirement: {required}")

    # Check every local target and every fragment on HTML pages, not only the
    # two pages that are the main focus of this smoke suite.
    checked_links = 0
    for page, parser in list(parsed.items()):
        for href in parser.links:
            target = urlsplit(href)
            if target.scheme or target.netloc or not target.path:
                continue
            checked_links += 1
            local_path = (page.parent / unquote(target.path)).resolve()
            if not local_path.is_relative_to(ROOT):
                errors.append(f"{page.relative_to(ROOT)} has a link escaping repository root: {href}")
                continue
            if not local_path.exists():
                errors.append(f"{page.relative_to(ROOT)} links to missing local target: {href}")
                continue
            if target.fragment and local_path.suffix.lower() in {".html", ".htm"}:
                target_parser = parse_html(local_path, errors, parsed)
                if target_parser and unquote(target.fragment) not in set(target_parser.ids):
                    errors.append(f"{page.relative_to(ROOT)} links to missing anchor: {href}")

    # Basic label association check on the primary public pages. This catches
    # regressions that can make forms harder to use with assistive technology.
    for page in PAGES:
        parser = parsed.get(page)
        if not parser:
            continue
        orphan_controls = sorted(set(parser.input_ids) - set(parser.label_for))
        # Some controls can have accessible names via aria-label; account for them
        # without trying to approximate the complete accessibility tree.
        source = page.read_text(encoding="utf-8")
        for control_id in orphan_controls:
            if f'id="{control_id}"' in source:
                import re
                pattern = rf'<(?:input|select|textarea)\b(?=[^>]*\bid="{re.escape(control_id)}")[^>]*aria-label='
                if re.search(pattern, source, flags=re.IGNORECASE):
                    continue
                errors.append(f"{page.relative_to(ROOT)} has a form control without a matching label/aria-label: {control_id}")

    if errors:
        print("PUBLIC INTERFACE SMOKE CHECK: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PUBLIC INTERFACE SMOKE CHECK: PASS ({len(parsed)} HTML pages parsed; {checked_links} local links checked)")
    print("Checked duplicate IDs, required customer routes, local targets/fragments, and basic form labels.")
    print("Note: this is not a browser, full accessibility, deployment, or provider-integration test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
