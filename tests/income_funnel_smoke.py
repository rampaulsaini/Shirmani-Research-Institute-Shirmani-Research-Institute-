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
        svc002_source, svc002 = load("sri-svc-002-research-summary.html")
        svc003_source, svc003 = load("sri-svc-003-detailed-research-report.html")
        sales_desk_source, sales_desk = load("showroom/global-product-sales-desk.html")
        enquiry_source, enquiry = load("writing-research-enquiry.html")
        showroom_source, showroom = load("showroom-public-interface.html")
        clean_showroom_source, _ = load("supreme-clean-showroom.html")
        income_source, _ = load("income-action-center.html")
        outreach_source, outreach = load("global-client-outreach-workbench.html")
        pipeline_source, _ = load("income-client-pipeline.html")
        showroom_pipeline_source, _ = load("showroom/income-first-client-pipeline.html")
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
    for phrase in ("₹999", "500 words", "scope", "payment terms", "not an order", "sale"):
        if phrase.casefold() not in offer_text.casefold() and phrase.casefold() not in offer_source.casefold():
            errors.append(f"Sales desk is missing clear offer/truth-boundary text: {phrase}")

    # Keep a single canonical offer section so mobile visitors do not see duplicate prices/CTAs.
    if "<h2>Service menu</h2>" in sales_desk_source:
        errors.append("Legacy sales desk repeats the starter offers in a second service-menu section")
    starter_section = offer_source.split("<h2>Three scoped pilot services</h2>", 1)
    if len(starter_section) != 2:
        errors.append("Canonical first-client offer is missing the three-pilot-services section")
    else:
        starter_cards = starter_section[1].split("<h2>Prepare a client enquiry</h2>", 1)[0]
        if starter_cards.count('<article class="offer">') != 3:
            errors.append("Canonical first-client offer must expose exactly three priced starter offers")
    if sales_desk_source.count("data-offer=") != 3:
        errors.append("Legacy sales desk must retain exactly three canonical priced offer actions")
    for selector_value in (
        "Hindi OR English Writing / Editing · SRI-SVC-001",
        "Research Summary · SRI-SVC-002",
        "Detailed Research Report · SRI-SVC-003",
    ):
        if f'<option>{selector_value}</option>' not in sales_desk_source or f'data-service="{selector_value}"' not in sales_desk_source:
            errors.append(f"Sales desk offer button and enquiry selector are not aligned: {selector_value}")
    if "<option>Hindi and English</option>" in sales_desk_source:
        errors.append("Sales desk must not offer a bilingual selection inside single-language pilot packages")
    for package_label in (
        "SRI-SVC-001 · Writing / Editing · ₹999",
        "SRI-SVC-002 · Research Summary · ₹1,999",
        "SRI-SVC-003 · Detailed Research Report · ₹2,999",
    ):
        if f"<option>{package_label}</option>" not in enquiry_source:
            errors.append(f"Writing/research enquiry form is missing package selector: {package_label}")
    if "<option>Hindi + English</option>" in enquiry_source:
        errors.append("Writing/research enquiry form must not offer a bilingual selection in single-language pilots")

    # Superseded website/blog copy pricing must not conflict with the canonical SVC-003 report offer.
    for stale_label in ("Article / Website Copy", "Website / Blog Content", "Website / Blog Draft"):
        if stale_label.casefold() in enquiry_source.casefold():
            errors.append(f"Writing/research enquiry page still contains superseded offer: {stale_label}")

    # The main public showroom must use the same three canonical SKUs and must not retain the old ₹2,999 website/blog offer.
    for marker in ("SRI-SVC-001", "SRI-SVC-002", "SRI-SVC-003", "sri-svc-002-research-summary.html", "sri-svc-003-detailed-research-report.html"):
        if marker not in showroom_source:
            errors.append(f"Public showroom is missing canonical service route or SKU: {marker}")
    for stale_label in ("SRI-WEB-PILOT-03", "Website / Blog Content", "SRI-RES-PILOT-02"):
        if stale_label.casefold() in showroom_source.casefold():
            errors.append(f"Public showroom still contains superseded pilot offer: {stale_label}")
    if "https://rzp.io/rzp/UhC1i8c" not in showroom_source:
        errors.append("Public showroom SVC-001 payment route must match the canonical Razorpay checkout")
    if "9622254967@ptyes" in showroom_source or "paypal" in showroom_source.casefold() or "upi://" in showroom_source:
        errors.append("Public showroom must not retain superseded manual UPI/PayPal payment instructions")
    if 'service: "SRI-SVC-001 Hindi OR English Writing & Editing"' not in showroom_source:
        errors.append("Public showroom enquiry payload must use the canonical SVC-001 writing/editing identity")
    if "Hindi/English Writing & Research" in showroom_source:
        errors.append("Public showroom must not label the SVC-001 enquiry as bilingual research")
    if "SRI-SVC-001 — Hindi OR English Writing & Editing" not in clean_showroom_source:
        errors.append("Supreme clean showroom must use the canonical SVC-001 service identity")
    if 'service:"SRI-SVC-001 Hindi OR English Writing & Editing"' not in clean_showroom_source:
        errors.append("Supreme clean showroom enquiry payload must use the canonical SVC-001 service identity")

    offer_urls = offer.links
    if not any(urlsplit(link).scheme == "mailto" for link in offer_urls):
        errors.append("Sales desk has no email enquiry action")
    if not any("wa.me/" in link for link in offer_urls):
        errors.append("Sales desk has no WhatsApp enquiry action")
    if not any(phrase in offer_source.casefold() for phrase in ("no order is placed", "no order is claimed", "does not create an order")):
        errors.append("Canonical offer must disclose that it does not create/claim an order")
    if not any(phrase in offer_source.casefold() for phrase in ("no message is sent automatically", "does not send email/whatsapp", "do not automatically send")):
        errors.append("Canonical offer must disclose that contact drafts are not automatically sent")

    # Outreach must use the same three service identities and prices as the canonical offer.
    if "Source-linked Research Summary — proposed ₹1,999 pilot" not in outreach_source:
        errors.append("Outreach SRI-SVC-002 price must match the canonical ₹1,999 offer")
    if "Detailed Research Report — proposed ₹2,999 pilot" not in outreach_source:
        errors.append("Outreach SRI-SVC-003 price must match the canonical ₹2,999 offer")
    if "Hindi OR English Writing & Editing — proposed ₹999 pilot" not in outreach_source:
        errors.append("Outreach SRI-SVC-001 price must match the canonical ₹999 offer")

    # New research packages must have standalone detail pages and no premature checkout.
    for source, page_text, sku, price, marker in (
        (svc002_source, " ".join(svc002.text), "SRI-SVC-002", "₹1,999", "अधिकतम 3 सहमत"),
        (svc003_source, " ".join(svc003.text), "SRI-SVC-003", "₹2,999", "अधिकतम 8 सहमत"),
    ):
        if sku not in source or price not in page_text:
            errors.append(f"{sku} detail page is missing its identifier or price")
        if marker not in source.casefold():
            errors.append(f"{sku} detail page is missing its agreed source limit")
        if "mailto:" not in source or "wa.me/" not in source:
            errors.append(f"{sku} detail page is missing enquiry routes")
        if not any("\n" in parse_qs(urlsplit(link).query).get("body", [""])[0] for link in (svc002.links if sku == "SRI-SVC-002" else svc003.links) if urlsplit(link).scheme == "mailto"):
            errors.append(f"{sku} email enquiry must preserve readable line breaks")
        if "rzp.io" in source or "upi://" in source or "paypal" in source.casefold():
            errors.append(f"{sku} must not show a payment route before its own checkout is configured")
        if "स्वतंत्र वैज्ञानिक" not in source:
            errors.append(f"{sku} must explain the independent-verification boundary")

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

    # The current showroom income pipeline must be included in the smoke gate.
    # Check its duplicate guard, local-only storage boundary, and honest payment/contact labels.
    for marker in (
        "function normalizeContact(v)",
        "function normalizeOrg(v)",
        "const duplicate=contactKey?leads.find",
        "normalizeContact(x.contact)===contactKey",
        "normalizeOrg(x.org)===orgKey",
        "x.service===record.service",
        "if(duplicate)",
        "localStorage.setItem(key,JSON.stringify(leads))",
        "अलग device पर अपने-आप sync नहीं होगा",
        "संदेश अपने-आप नहीं भेजा जाता",
        'id="paymentRef"',
        "x.stage==='Payment verified'",
        "Number(x.amount)>0",
    ):
        if marker.casefold() not in showroom_pipeline_source.casefold():
            errors.append(f"Current showroom income pipeline is missing duplicate/payment/truth-boundary control: {marker}")
    # Payment guidance must remain consent-first and must not prefill an amount.
    offer_lower = offer_source.casefold()
    if "payment — only after written agreement" not in offer_lower:
        errors.append("Canonical offer must label payment as occurring only after written agreement")
    if "पहले लिखित सहमति" not in offer_source:
        errors.append("Canonical offer must explain written consent before payment")
    payment_links = [link for link in offer_urls if link == "https://rzp.io/rzp/UhC1i8c"]
    if not payment_links:
        errors.append("Canonical offer must expose the existing Razorpay SRI-SVC-001 checkout")
    if any(urlsplit(link).scheme == "upi" for link in offer_urls):
        errors.append("Canonical offer must not expose the legacy manual UPI payment route")
    if "paypal" in offer_lower:
        errors.append("Canonical offer must not expose the legacy PayPal payment route")
    if "transaction reference" not in offer_lower:
        errors.append("Canonical offer must explain transaction-reference follow-up")
    if "does not" not in offer_lower or "process payments" not in offer_lower:
        errors.append("Canonical offer must disclose that the static page does not process payments")

    enquiry_text = " ".join(enquiry.text)
    for phrase in ("₹999", "₹1,999", "₹2,999", "WhatsApp", "लिखित", "भुगतान"):
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
