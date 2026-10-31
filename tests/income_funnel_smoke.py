#!/usr/bin/env python3
"""Regression checks for the canonical public customer-to-income path.

Run from the repository root: python3 tests/income_funnel_smoke.py
This checks repository source only; it does not prove Pages deployment, message
delivery, customer agreement, dispatch, payment, or revenue.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class LinksAndText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def load(relative: str) -> tuple[str, LinksAndText]:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"Missing required income-funnel page: {relative}")
    source = path.read_text(encoding="utf-8")
    parser = LinksAndText()
    parser.feed(source)
    parser.close()
    return source, parser


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    errors: list[str] = []

    try:
        index_source, index = load("index.html")
        offer_source, offer = load("first-paid-pilot-offer.html")
        sales_desk_source, sales_desk = load("showroom/global-product-sales-desk.html")
        enquiry_source, enquiry = load("writing-research-enquiry.html")
        showroom_source, showroom = load("showroom-public-interface.html")
        income_source, _ = load("income-action-center.html")
        outreach_source, outreach = load("global-client-outreach-workbench.html")
        pipeline_source, _ = load("income-client-pipeline.html")
    except (AssertionError, OSError, UnicodeError) as exc:
        print(f"INCOME FUNNEL SMOKE CHECK: FAILED\n- {exc}")
        return 1

    # One canonical entry page must point to the live offer, showroom and income workspace.
    for route in (
        "first-paid-pilot-offer.html",
        "showroom-public-interface.html",
        "income-action-center.html",
    ):
        if route not in [urlsplit(link).path for link in index.links]:
            errors.append(f"index.html is missing canonical route: {route}")

    offer_text = " ".join(offer.text)
    for phrase in ("₹499", "700 words", "scope", "payment terms", "not an order", "sale"):
        if phrase.casefold() not in offer_text.casefold() and phrase.casefold() not in offer_source.casefold():
            errors.append(f"Sales desk is missing clear offer/truth-boundary text: {phrase}")

    # Keep a single canonical offer section so mobile visitors do not see duplicate prices/CTAs.
    if "<h2>Service menu</h2>" in sales_desk_source:
        errors.append("Legacy sales desk repeats the starter offers in a second service-menu section")
    starter_section = offer_source.split("<h2>Starter offers</h2>", 1)
    if len(starter_section) != 2:
        errors.append("Canonical first-client offer is missing the starter-offers section")
    else:
        starter_cards = starter_section[1].split("<h2>Prepare a client enquiry</h2>", 1)[0]
        if starter_cards.count('<article class="offer">') != 3:
            errors.append("Canonical first-client offer must expose exactly three priced starter offers")
    if sales_desk_source.count("data-offer=") != 3:
        errors.append("Legacy sales desk must retain exactly three canonical priced offer actions")

    offer_urls = offer.links
    if not any(urlsplit(link).scheme == "mailto" for link in offer_urls):
        errors.append("Sales desk has no email enquiry action")
    if not any("wa.me/" in link for link in offer_urls):
        errors.append("Sales desk has no WhatsApp enquiry action")
    if not any(phrase in offer_source.casefold() for phrase in ("no order is placed", "no order is claimed", "does not create an order")):
        errors.append("Canonical offer must disclose that it does not create/claim an order")
    if not any(phrase in offer_source.casefold() for phrase in ("no message is sent automatically", "does not send email/whatsapp", "do not automatically send")):
        errors.append("Canonical offer must disclose that contact drafts are not automatically sent")

    # Outreach must use the same prices as the canonical first-client offer.
    # Editing is ₹499, website/blog copy is ₹999, and source-based research is ₹1,499.
    if "Source-linked Research Summary — proposed ₹1,499 pilot" not in outreach_source:
        errors.append("Outreach research-summary price must match the canonical ₹1,499 offer")
    if "Website / Blog Content — proposed ₹999 pilot" not in outreach_source:
        errors.append("Outreach website/blog price must match the canonical ₹999 offer")
    if "Hindi/English Writing & Editing — proposed ₹499 pilot" not in outreach_source:
        errors.append("Outreach editing price must match the canonical ₹499 offer")

    # The income tracker must support a portable backup without presenting local entries as verified payments.
    for marker in ('id="export"', 'CSV प्रमाण-बैकअप डाउनलोड करें', 'exported_at_utc',
                   'new Uint8Array([0xEF,0xBB,0xBF])',
                   'not independently verified'):
        if marker.casefold() not in income_source.casefold():
            errors.append(f"Income Action Center is missing backup/truth-boundary marker: {marker}")

    # The client pipeline must not count work-stage labels as proof of payment.
    for marker in (
        'id="paymentStatus"',
        'id="paymentRef"',
        "const hasPaymentProof=x=>x.paymentStatus==='Payment received — reference recorded'&&String(x.paymentRef||'').trim().length>0",
        "q('p').textContent=data.filter(hasPaymentProof).length",
        "q('r').textContent='₹'+data.filter(hasPaymentProof).reduce",
        "Number(x.amount)>0",
        "const validImportedRecord=x=>",
        "!validImportedRecord(x)||ids.has(x.id)",
        "Invalid payment records and duplicate IDs will be skipped.",
    ):
        if marker.casefold() not in pipeline_source.casefold():
            errors.append(f"Client pipeline is missing payment-evidence gate: {marker}")
    if "q('p').textContent=data.filter(x=>paid.includes(x.stage)).length" in pipeline_source:
        errors.append("Client pipeline must not count paid jobs from stage labels alone")

    # Payment guidance must remain consent-first and must not prefill an amount.
    offer_lower = offer_source.casefold()
    if "payment — only after written agreement" not in offer_lower:
        errors.append("Canonical offer must label payment as occurring only after written agreement")
    if "पहले लिखित सहमति" not in offer_source:
        errors.append("Canonical offer must explain written consent before payment")
    upi_links = [link for link in offer_urls if urlsplit(link).scheme == "upi"]
    if not upi_links:
        errors.append("Canonical offer must expose the documented UPI payment-intent link")
    elif any("am" in parse_qs(urlsplit(link).query) for link in upi_links):
        errors.append("UPI payment intent must not prefill an amount before written agreement")
    if "paypal" not in offer_lower or "transaction reference" not in offer_lower:
        errors.append("Canonical offer must include PayPal guidance and transaction-reference follow-up")
    if "does not" not in offer_lower or "process payments" not in offer_lower:
        errors.append("Canonical offer must disclose that the static page does not process payments")

    enquiry_text = " ".join(enquiry.text)
    for phrase in ("₹499", "₹999", "₹1,499", "WhatsApp", "लिखित", "भुगतान"):
        if phrase.casefold() not in enquiry_text.casefold() and phrase.casefold() not in enquiry_source.casefold():
            errors.append(f"Enquiry page is missing service/pricing/process text: {phrase}")
    if "mailto:" not in enquiry_source or "wa.me/" not in enquiry_source:
        errors.append("Enquiry page must provide email and WhatsApp draft actions")
    if "अपने-आप कोई संदेश नहीं भेजता" not in enquiry_source and "अपने आप कोई संदेश नहीं भेजता" not in enquiry_source:
        errors.append("Enquiry page must state that messages are not sent automatically")

    showroom_text = " ".join(showroom.text)
    if "Public Showroom" not in showroom_text:
        errors.append("Public showroom title/content is missing")
    if "dispatch" not in showroom_source.casefold():
        errors.append("Public showroom must expose dispatch state")

    if errors:
        print("INCOME FUNNEL SMOKE CHECK: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("INCOME FUNNEL SMOKE CHECK: PASS")
    print("Canonical entry, public showroom, priced starter offer, email/WhatsApp enquiry routes, CSV tracker backup, and no-false-sale disclosures are present.")
    print("This source-level gate does not verify live message delivery, customer acceptance, dispatch, payment, or deployed Pages output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
