import hashlib
import json
from datetime import datetime, timezone

SERVICES = (
    "case_intake", "document_organization", "legal_research",
    "precedent_verification", "case_summary", "mediation_support",
    "drafting_support", "status_tracking",
)

def _now():
    return datetime.now(timezone.utc).isoformat()

def _hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()

def build_case_plan(title, jurisdiction, service, language="en"):
    if not title or not jurisdiction:
        raise ValueError("title_and_jurisdiction_required")
    if service not in SERVICES:
        raise ValueError("unsupported_legal_service")
    plan = {
        "title": title.strip(),
        "jurisdiction": jurisdiction.strip(),
        "service": service,
        "language": language,
        "workflow": [
            "intake",
            "document_index",
            "source_research",
            "citation_verification",
            "counter_argument_check",
            "qualified_human_review",
        ],
        "ai_role": "decision_support_only",
        "binding_judgment": False,
        "generated_at": _now(),
    }
    plan["plan_hash"] = _hash(plan)
    return plan

def validate_case_plan(plan):
    required = ("title", "jurisdiction", "service", "workflow", "plan_hash")
    if any(key not in plan for key in required):
        raise ValueError("incomplete_case_plan")
    if plan["service"] not in SERVICES:
        raise ValueError("unsupported_legal_service")
    if plan.get("ai_role") != "decision_support_only":
        raise ValueError("ai_role_boundary_violation")
    if plan.get("binding_judgment") is not False:
        raise ValueError("binding_judgment_requires_authorized_human_court")
    return True
