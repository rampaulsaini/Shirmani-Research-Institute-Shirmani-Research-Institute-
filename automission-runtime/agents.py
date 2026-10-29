import re

CHANNELS = {
    "employment": {"keywords": ("job", "employment", "hiring", "career")},
    "freelancing": {"keywords": ("freelance", "gig", "contract", "project")},
    "ai_marketing": {"keywords": ("marketing", "lead", "seo", "content", "advertising")},
    "digital_store": {"keywords": ("digital product", "template", "ebook", "store", "listing")},
    "yatharth_ai_music": {"keywords": ("music", "song", "audio", "artist", "release")},
    "economic_vision": {"keywords": ("business", "market", "economic", "investment", "strategy")},
}


def normalize_channel(value):
    value = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    return value if value in CHANNELS else None


def score(item):
    """Rank an opportunity for triage; this score is not verification."""
    text = f'{item.get("title", "")} {item.get("description", "")}'.lower()
    channel = normalize_channel(item.get("channel"))
    if not channel:
        return 0
    hits = sum(
        1 for keyword in CHANNELS[channel]["keywords"]
        if re.search(r"\\b" + re.escape(keyword) + r"\\b", text)
    )
    evidence_present = bool(item.get("evidence_url"))
    return min(100, hits * 10 + (20 if evidence_present else 0))


def prepare(item):
    """Normalize a candidate; URLs permit review, never independent verification."""
    channel = normalize_channel(item.get("channel"))
    if not channel or not item.get("title") or not item.get("url") or not item.get("evidence_url"):
        return None
    prepared = dict(item)
    prepared["channel"] = channel
    prepared["score"] = max(float(prepared.get("score", 0)), score(prepared))
    prepared["status"] = "REVIEW_REQUIRED"
    prepared["evidence_status"] = "PRESENT_UNVERIFIED"
    prepared["verification_reason"] = (
        "Source URLs are available, but independent verification has not been recorded."
    )
    return prepared
