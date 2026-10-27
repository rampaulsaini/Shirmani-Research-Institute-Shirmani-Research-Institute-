#!/usr/bin/env python3
"""Check deployed GitHub Pages routes and income-offer price markers.

This checks deployed HTTP responses, not merely source-file presence. Each URL,
UTC timestamp, status, redirect destination and content-marker result is printed.
"""
from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urlparse

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
    ("public product catalog", BASE + "/products.html", ("SHIRMANI Real Product Catalog", "24 registered offers")),
    ("global service and sales desk", BASE + "/showroom/global-product-sales-desk.html", ("SHIRMANI | Global Service & Sales Desk", "Open First Client Pilot Desk")),
    ("first-client pilot desk", BASE + "/showroom/first-client-pilot-desk.html", ("SHIRMANI — First Client Pilot Desk", "WhatsApp")),
    ("writing and research service enquiry", BASE + "/services/writing-research-enquiry.html", ("Writing & Research Services", "Writing & Research Enquiry", 'data-offer="research-summary" data-price="₹1,499"', 'data-offer="website-blog" data-price="₹999"')),
    ("product order page", BASE + "/product-order.html", ("SHIRMANI Product Order", "Order / Payment")),
    (
        "income-first revenue control center",
        BASE + "/revenue-first-control-center.html",
        (
            "उत्पादन से वास्तविक आय तक",
            "₹499 · Editing pilot",
            "₹1,499 · Research summary",
            "₹999 · Website/blog draft",
        ),
    ),
    ("first paid pilot offer", BASE + "/first-paid-pilot-offer.html", ("Research & Writing — First Client Pilot", "₹499", "₹1,499", "₹999")),
    ("income client pipeline", BASE + "/income-client-pipeline.html", ("Client Pipeline & Delivery Tracker", "Measurable pipeline", "Add a real prospect / customer")),
    ("income client outreach desk", BASE + "/income-client-outreach-desk.html", ("Client Outreach & Delivery Desk", "Current service offer", "Seven-day measurable sprint")),
    ("live production state JSON", BASE + "/generated/live-production-state.json", ('"schema_version"', '"concrete_repository_assets"', '"dispatch_released"', '"payment_claimed"', '"truth_boundary"')),
    ("independent verification state JSON", BASE + "/generated/independent-verification-status.json", ('"queue_total"', '"verified_records"', '"verification_policy": "FAIL_CLOSED"', '"human_review_required_for_verified_promotion": true')),
    ("writing and research enquiry", BASE + "/writing-research-enquiry.html", ("Writing & Research Enquiry", "₹499", "₹1,499")),
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
        headers={"User-Agent": "Shirmani-Pages-SmokeCheck/1.1 (+GitHub Actions)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
            final_url = response.geturl()
            body = response.read(2_000_000).decode("utf-8", errors="replace")
        parser = PageParser()
        parser.feed(body)
        title = " ".join(parser.title_text) or "(no title)"
        missing_markers = [marker for marker in markers if marker.lower() not in body.lower()]
        content_ok = not missing_markers
        same_site = urlparse(final_url).netloc == urlparse(BASE).netloc
        ok = 200 <= status < 300 and content_ok and same_site
        print(
            f"[{'PASS' if ok else 'FAIL'}] {label} | checked_at={stamp} | "
            f"url={url} | http_status={status} | final_url={final_url} | "
            f"title={title!r} | content_marker_ok={content_ok} | "
            f"missing_markers={missing_markers!r} | same_site_redirect={same_site}"
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
    print(
        f"GitHub Pages deployed-root smoke check | base={BASE} | "
        f"started_at={datetime.now(timezone.utc).isoformat(timespec='seconds')}"
    )
    results = [check(label, url, markers) for label, url, markers in ROUTES]
    passed = sum(results)
    print(
        f"SUMMARY: {passed}/{len(results)} routes passed; "
        f"finished_at={datetime.now(timezone.utc).isoformat(timespec='seconds')}"
    )
    if passed != len(results):
        print(
            "FAILURE: deployed Pages route checks failed. A source file existing "
            "in Git does not prove successful deployment.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
