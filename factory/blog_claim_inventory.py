#!/usr/bin/env python3
"""Build a source-bound, fail-closed claim inventory from the canonical blog."""
import hashlib
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime, timezone

PRIMARY = "https://multicosmovision.blogspot.com/2026/06/blog-post_18.html"
FALLBACK = "https://multicosmovision.blogspot.com/2026/09/blog-post.html"
OUT = Path("generated/BLOG-CLAIM-INVENTORY.json")

class TextParser(HTMLParser):
    BLOCK = {"p","div","li","h1","h2","h3","h4","h5","h6","br","blockquote"}
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in {"script","style","noscript"}:
            self.skip += 1
        if tag in self.BLOCK and self.parts and self.parts[-1] != "\n":
            self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in {"script","style","noscript"} and self.skip:
            self.skip -= 1
        if tag in self.BLOCK:
            self.parts.append("\n")
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent":"ShirmaniResearch/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def normalize(text):
    text = text.replace("\r","")
    lines = [re.sub(r"\s+", " ", x).strip() for x in text.split("\n")]
    return "\n".join(x for x in lines if x)

def classify(s):
    low = s.lower()
    if any(x in low for x in ["मैं ", "मैंने ", "मेरे ", "मेरा ", "मेरी "]):
        return "PERSONAL_EXPERIENCE"
    if any(x in low for x in ["गुरु", "आरोप", "निकाल", "अनुयायी", "संगत", "घटना"]):
        return "EVENT_OR_ALLEGATION"
    if any(x in low for x in ["विज्ञान", "वैज्ञानिक", "समय", "मन ", "मस्तक", "बुद्धि", "जीव", "प्रकृति", "भौतिक"]):
        return "SCIENTIFIC_CLAIM"
    if any(x in low for x in ["सर्वभौमिक सत्य", "यथार्थ सिद्धांत", "यथार्थ युग", "शिरोमणि स्वरूप", "संपूर्ण संतुष्टि"]):
        return "PHILOSOPHICAL_PROPOSITION"
    if any(x in low for x in ["है", "हैं", "होता", "होती", "कर सकता", "कर सकती", "नहीं"]):
        return "GENERAL_CLAIM"
    return "GENERAL_CLAIM"

def main():
    raw = None
    used = None
    errors = []
    for url in (PRIMARY, FALLBACK):
        try:
            raw = fetch(url)
            used = url
            break
        except Exception as e:
            errors.append(f"{url}: {e}")
    if raw is None:
        raise SystemExit("SOURCE_FETCH_FAILED: " + " | ".join(errors))
    source_html_sha256 = hashlib.sha256(raw).hexdigest()
    parser = TextParser()
    parser.feed(raw.decode("utf-8", errors="replace"))
    text = normalize("".join(parser.parts))
    units = [x.strip() for x in text.split("\n") if len(x.strip()) >= 20]
    claims = []
    for idx, unit in enumerate(units, 1):
        # Keep sentences/paragraph-sized units; split only on clear sentence boundaries.
        pieces = [p.strip() for p in re.split(r"(?<=[.!?।])\s+", unit) if p.strip()]
        if not pieces:
            pieces = [unit]
        for piece in pieces:
            if len(piece) < 20:
                continue
            norm = re.sub(r"\s+", " ", piece)
            claim_basis = f"{used}\n{idx}\n{len(claims)+1}\n{norm}"
            h = hashlib.sha256(claim_basis.encode("utf-8")).hexdigest()
            tags = []
            low = norm.lower()
            if any(x in low for x in ["मैं ", "मैंने ", "मेरे ", "मेरा ", "मेरी "]):
                tags.append("PERSONAL_EXPERIENCE")
            if any(x in low for x in ["गुरु", "आरोप", "निकाल", "अनुयायी", "संगत", "घटना"]):
                tags.append("EVENT_OR_ALLEGATION")
            if any(x in low for x in ["विज्ञान", "वैज्ञानिक", "समय", "मन ", "मस्तक", "बुद्धि", "जीव", "प्रकृति", "भौतिक"]):
                tags.append("SCIENTIFIC_CLAIM")
            if any(x in low for x in ["सर्वभौमिक सत्य", "यथार्थ सिद्धांत", "यथार्थ युग", "शिरोमणि स्वरूप", "संपूर्ण संतुष्टि"]):
                tags.append("PHILOSOPHICAL_PROPOSITION")
            claims.append({
                "claim_id": "BLOG-" + h[:16],
                "source_url": used,
                "source_sha256": source_html_sha256,
                "source_text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                "source_unit": idx,
                "claim_text": norm,
                "claim_type": classify(norm),
                "claim_tags": sorted(set(tags)) or ["GENERAL_CLAIM"],
                "status": "UNVERIFIED",
                "verification": {
                    "evidence": [],
                    "counter_evidence": [],
                    "reproduction": [],
                    "reviewer": None,
                    "audit": None,
                    "conclusion": None
                }
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_url": used,
        "source_sha256": source_hash,
        "source_text_units": len(units),
        "claim_count": len(claims),
        "independent_verification_count": 0,
        "verified_count": 0,
        "publication_gate": "CHECK",
        "policy": "Source text is not proof. Every source occurrence remains traceable; no claim is VERIFIED without independent review and evidence.",
        "claims": claims
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "source_url": used,
        "source_text_units": len(units),
        "claim_count": len(claims),
        "verified_count": 0,
        "publication_gate": "CHECK"
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
