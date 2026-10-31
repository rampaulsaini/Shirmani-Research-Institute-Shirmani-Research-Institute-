import hashlib
import json
from datetime import datetime, timezone

LEVELS = ("foundation", "professional", "advanced", "research")
DELIVERY = ("online", "offline", "hybrid")

def _now():
    return datetime.now(timezone.utc).isoformat()

def _hash(payload):
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def build_program(title, subject, level="professional", delivery="online",
                  languages=None, fee_inr=0, duration_weeks=8):
    if not title or not subject:
        raise ValueError("title_and_subject_required")
    if level not in LEVELS:
        raise ValueError("invalid_level")
    if delivery not in DELIVERY:
        raise ValueError("invalid_delivery")
    if fee_inr < 0:
        raise ValueError("fee_must_be_nonnegative")
    if duration_weeks <= 0:
        raise ValueError("duration_must_be_positive")
    program = {
        "title": title.strip(),
        "subject": subject.strip(),
        "level": level,
        "delivery": delivery,
        "languages": sorted(set(languages or ["en"])),
        "fee_inr": int(fee_inr),
        "duration_weeks": int(duration_weeks),
        "curriculum": [
            "foundations",
            "guided_learning",
            "practical_projects",
            "assessment",
            "capstone",
        ],
        "quality": {
            "source_attribution_required": True,
            "original_material_required": True,
            "university_affiliation_claim_allowed": False,
            "recognized_degree_claim_allowed": False,
        },
    }
    program["program_hash"] = _hash(program)
    program["created_at"] = _now()
    return program

def validate_program(program):
    required = ("title", "subject", "level", "delivery", "curriculum", "program_hash")
    missing = [k for k in required if k not in program]
    if missing:
        raise ValueError("missing:" + ",".join(missing))
    if program["level"] not in LEVELS or program["delivery"] not in DELIVERY:
        raise ValueError("invalid_program")
    return True
