import re

CHANNELS = {
    "employment": {"keywords": ("job","employment","hiring","career")},
    "freelancing": {"keywords": ("freelance","gig","contract","project")},
    "ai_marketing": {"keywords": ("marketing","lead","seo","content","advertising")},
    "digital_store": {"keywords": ("digital product","template","ebook","store","listing")},
    "yatharth_ai_music": {"keywords": ("music","song","audio","artist","release")},
    "economic_vision": {"keywords": ("business","market","economic","investment","strategy")},
}

def normalize_channel(value):
    value = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    return value if value in CHANNELS else None

def score(item):
    text = f'{item.get("title","")} {item.get("description","")}'.lower()
    channel = normalize_channel(item.get("channel"))
    if not channel:
        return 0
    hits = sum(1 for k in CHANNELS[channel]["keywords"] if re.search(r"\b" + re.escape(k) + r"\b", text))
    evidence = 2 if item.get("evidence_url") else 0
    return min(100, hits * 10 + evidence * 20)

def prepare(item):
    channel = normalize_channel(item.get("channel"))
    if not channel or not item.get("title") or not item.get("url") or not item.get("evidence_url"):
        return None
    item = dict(item)
    item["channel"] = channel
    item["score"] = max(float(item.get("score", 0)), score(item))
    item["status"] = "VERIFIED"
    return item
