#!/usr/bin/env python3
"""Check the deployed GitHub Pages root and important public entry points.

This checks the deployed HTTP response, not merely the presence of source files.
Each URL, UTC timestamp, status, redirect destination and result is printed.
"""
from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

BASE = os.environ.get(
    "PAGES_BASE_URL",
    "https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-",
).rstrip("/")

ROUTES = [
    ("public root", BASE + "/", ("<html",)),
    ("direct index", BASE + "/index.html", ("<html",)),
    ("public product showroom", BASE + "/showroom/public-product-showroom.html", ("<html",)),
    ("character studio", BASE + "/showroom/heart-view-character-studio.html", ("<html",)),
    ("human presentation studio", BASE + "/showroom/shirmani-human-presentation-studio.html", ("<html",)),
    ("product demo production desk", BASE + "/showroom/product-demo-video-production-desk.html", ("<html",)),
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = False
        self.title_text = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.title = True
    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.title = False
    def handle_data(self, data):
        if self.title:
            self.title_text.append(data.strip())

def check(label: str, url: str, markers: tuple[str, ...]) -> bool:
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Shirmani-Pages-SmokeCheck/1.0 (+GitHub Actions)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
            final_url = response.geturl()
            body = response.read(2_000_000).decode("utf-8", errors="replace")
        parser = PageParser()
        parser.feed(body)
        title = " ".join(parser.title_text) or "(no title)"
        content_ok = all(marker.lower() in body.lower() for marker in markers)
        same_site = urlparse(final_url).netloc == urlparse(BASE).netloc
        ok = 200 <= status < 300 and content_ok and same_site
        print(
            f"[{'PASS' if ok else 'FAIL'}] {label} | checked_at={stamp} | "
            f"url={url} | http_status={status} | final_url={final_url} | "
            f"title={title!r} | content_marker_ok={content_ok} | same_site_redirect={same_site}"
        )
        return ok
    except urllib.error.HTTPError as exc:
        print(
            f"[FAIL] {label} | checked_at={stamp} | url={url} | "
            f"http_status={exc.code} | final_url={exc.geturl()} | error={exc.reason}"
        )
    except Exception as exc:
        print(
            f"[FAIL] {label} | checked_at={stamp} | url={url} | "
            f"error={type(exc).__name__}: {exc}"
        )
    return False

def main() -> int:
    print(f"GitHub Pages deployed-root smoke check | base={BASE} | started_at={datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    results = [check(label, url, markers) for label, url, markers in ROUTES]
    passed = sum(results)
    print(f"SUMMARY: {passed}/{len(results)} routes passed; finished_at={datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    if passed != len(results):
        print("FAILURE: deployed Pages route checks failed. A source file existing in Git does not prove successful deployment.", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
