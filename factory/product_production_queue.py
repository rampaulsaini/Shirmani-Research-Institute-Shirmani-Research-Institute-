#!/usr/bin/env python3
"""Product-first production queue.

Turns every configured product/service offer into an explicit production job
before verification. This is orchestration metadata, not a claim that the
underlying media/service has already been rendered or sold.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
CATALOG = ROOT / "factory" / "product-catalog.json"

def main():
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat()
    jobs = []
    for lane in sorted(catalog.get("lanes", []), key=lambda x: (x.get("priority", 999), x.get("id", ""))):
        for offer in lane.get("offers", []):
            jobs.append({
                "job_id": offer["id"],
                "lane": lane["id"],
                "priority": lane.get("priority", 999),
                "name": offer["name"],
                "delivery": offer.get("delivery"),
                "destination": offer.get("destination"),
                "price_inr": offer.get("price_inr"),
                "store": offer.get("store"),
                "status": "READY_TO_PRODUCE",
                "stages": ["PRODUCT_BRIEF","CONTENT_OR_CREATIVE_PRODUCTION","PACKAGING","PRODUCT_PAGE","DELIVERY_PATH","MARKETING_DRAFT","QC","INDEPENDENT_VERIFICATION","PUBLICATION"],
                "verification_position": "DOWNSTREAM_OF_PRODUCTION",
                "generated_at": now
            })
    OUT.mkdir(exist_ok=True)
    (OUT / "PRODUCT-PRODUCTION-QUEUE.json").write_text(json.dumps({
        "strategy":"PRODUCT_FIRST","generated_at":now,"total_jobs":len(jobs),
        "ready_to_produce":len(jobs),
        "principle":"Production creates the result; verification evaluates the result downstream.",
        "jobs":jobs
    }, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"PRODUCT_PRODUCTION_QUEUE: {len(jobs)} jobs ready")
if __name__=="__main__":
    main()
