import hashlib
import json
from datetime import datetime, timezone

AGENT_ROLES = (
    "research", "creator", "software", "book", "course",
    "animation", "film", "design", "qc", "localization",
    "seo", "packaging",
)

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def choose_agents(product_type):
    mapping = {
        "software": ["research", "software", "qc", "packaging", "seo"],
        "website": ["research", "software", "design", "qc", "packaging", "seo"],
        "ai_tool": ["research", "software", "qc", "packaging", "seo"],
        "book": ["research", "book", "qc", "localization", "packaging", "seo"],
        "course": ["research", "course", "design", "qc", "localization", "packaging", "seo"],
        "animation": ["research", "animation", "design", "qc", "packaging", "seo"],
        "cartoon": ["research", "animation", "design", "qc", "packaging", "seo"],
        "film": ["research", "film", "design", "qc", "packaging", "seo"],
        "music": ["research", "design", "qc", "packaging", "seo"],
        "painting": ["research", "design", "qc", "packaging", "seo"],
        "research": ["research", "qc", "localization", "packaging", "seo"],
        "service_package": ["research", "design", "qc", "packaging", "seo"],
    }
    return mapping.get(product_type, ["research", "qc", "packaging", "seo"])

def build_product_spec(title, product_type, description="", languages=None):
    if not title.strip():
        raise ValueError("title is required")
    if not product_type.strip():
        raise ValueError("product_type is required")
    spec = {
        "title": title.strip(),
        "product_type": product_type.strip(),
        "description": description.strip(),
        "languages": sorted(set(languages or ["en"])),
        "agents": choose_agents(product_type.strip()),
        "created_at": utc_now(),
    }
    canonical = json.dumps(spec, sort_keys=True, separators=(",", ":"))
    spec["spec_hash"] = hashlib.sha256(canonical.encode()).hexdigest()
    return spec

def validate_agent_plan(spec):
    agents = spec.get("agents", [])
    if not agents or any(agent not in AGENT_ROLES for agent in agents):
        raise ValueError("invalid product agent plan")
    return True
