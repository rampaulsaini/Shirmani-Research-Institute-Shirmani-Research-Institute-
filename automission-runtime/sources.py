import json
import os
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ALLOWED_SCHEMES = {"https"}

def fetch_json(url, timeout=20):
    parsed = urlparse(url)
    if parsed.scheme not in ALLOWED_SCHEMES or not parsed.netloc:
        raise ValueError("only HTTPS source URLs are allowed")
    req = Request(url, headers={"User-Agent":"AutomissionRuntime/1.0"})
    with urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))

def configured_sources():
    raw = os.getenv("AUTOMISSION_SOURCE_FEEDS", "")
    if not raw:
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]

def discover():
    items = []
    for url in configured_sources():
        try:
            data = fetch_json(url)
            records = data if isinstance(data, list) else data.get("items", [])
            for record in records:
                if not isinstance(record, dict):
                    continue
                required = {"title", "channel"}
                if not required.issubset(record):
                    continue
                record["source"] = record.get("source", url)
                record["evidence_url"] = record.get("evidence_url", record.get("url", url))
                items.append(record)
        except Exception:
            continue
    return items
