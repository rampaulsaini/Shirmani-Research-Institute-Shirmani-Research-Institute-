"""Deterministic task router with optional NVIDIA Hub routing."""
from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ROOT / "factory" / "nvidia-routing.json"
COMPANIES = ROOT / "factory" / "ai-companies.json"

def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def route(task_type: str, nvidia_enabled: bool | None = None) -> dict[str, Any]:
    routes = _load(ROUTES)["routes"]
    companies = _load(COMPANIES)["companies"]
    route_info = routes.get(task_type, {"agent": "research", "fallback": "research"})
    if nvidia_enabled is None:
        nvidia_enabled = bool(os.getenv("NVIDIA_API_KEY"))
    agent = route_info["agent"] if nvidia_enabled else route_info["fallback"]
    company = next((c for c in companies if agent in c["id"] or agent in c["skills"]), None)
    return {
        "task_type": task_type,
        "agent": agent,
        "fallback": route_info.get("fallback"),
        "hub": "NVIDIA AI Hub" if agent == "nvidia" else "free-deterministic",
        "company": company["id"] if company else None,
        "nvidia_enabled": nvidia_enabled,
        "verification_required": True,
    }

if __name__ == "__main__":
    print(json.dumps(route("research.deep"), ensure_ascii=False, indent=2))
