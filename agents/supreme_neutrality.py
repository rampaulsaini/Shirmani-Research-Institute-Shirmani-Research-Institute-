"""Executable neutrality and evidence boundary for Supreme NLP."""
from __future__ import annotations
import hashlib, json
from typing import Any

VERSION = "1.0.0"

def _fingerprint(obj: Any) -> str:
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def build_neutrality_record(rows: list[dict[str, Any]], record_id: str) -> dict[str, Any]:
    features = [{"name": str(r.get("feature", "unknown")), "value": r.get("value")} for r in rows]
    modality = str(rows[0].get("modality", "unknown")) if rows else "unknown"
    if not rows:
        statement_type, simple, confidence, status = "UNKNOWN", "कोई पर्याप्त मापित संकेत उपलब्ध नहीं है; निष्कर्ष नहीं निकाला गया।", 0.0, "UNVERIFIED"
    else:
        statement_type = "OBSERVED"
        simple = "मापित संकेत उपलब्ध हैं। प्रणाली केवल देखे गए पैटर्न को बताती है; किसी जीव/वस्तु की निजी अनुभूति या चेतना का दावा नहीं करती।"
        confidence = min(1.0, sum(float(r.get("quality", 0)) for r in rows) / len(rows))
        status = "EVIDENCE-SUPPORTED" if confidence > 0 else "UNVERIFIED"
    payload = {
        "version": VERSION, "record_id": record_id,
        "observation": {"modality": modality, "features": features},
        "interpretation": {"statement_type": statement_type, "simple_language": simple, "confidence": round(confidence, 6)},
        "governance": {"neutrality": True, "equal-treatment": True, "evidence-first": True, "subjective-experience-claim-allowed": False, "fail_closed": True},
        "verification": {"independent_verification_required": True, "status": status}
    }
    payload["fingerprint"] = _fingerprint(payload)
    return payload
