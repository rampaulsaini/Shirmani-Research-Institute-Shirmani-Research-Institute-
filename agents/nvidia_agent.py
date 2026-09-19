"""Optional NVIDIA NIM/API agent for higher-quality generation.

The factory remains fully runnable without this integration. When NVIDIA_API_KEY is
present, this agent can enrich a small, resumable batch through NVIDIA's
OpenAI-compatible hosted endpoint.
"""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any

DEFAULT_BASE_URL = "https://integrate.api.nvidia.com/v1"
DEFAULT_MODEL = "nvidia/nemotron-3-super-120b-a12b"


def enabled() -> bool:
    return bool(os.getenv("NVIDIA_API_KEY"))


def chat(prompt: str, system: str = "", model: str | None = None,
         temperature: float = 0.4, max_tokens: int = 2048) -> str:
    key = os.getenv("NVIDIA_API_KEY")
    if not key:
        raise RuntimeError("NVIDIA_API_KEY is not configured")
    payload: dict[str, Any] = {
        "model": model or os.getenv("NVIDIA_MODEL", DEFAULT_MODEL),
        "messages": [],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    if system:
        payload["messages"].append({"role": "system", "content": system})
    payload["messages"].append({"role": "user", "content": prompt})

    req = urllib.request.Request(
        os.getenv("NVIDIA_BASE_URL", DEFAULT_BASE_URL).rstrip("/") + "/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def enrich_record(text: str, source: str = "unknown") -> dict[str, Any]:
    system = (
        "You are the optional NVIDIA research-generation agent in a provenance-first "
        "research factory. Preserve the distinction between user-authored philosophy, "
        "source-backed material, hypotheses, and independently verified facts. Do not "
        "claim scientific proof merely because a source exists. Return concise, useful "
        "Hindi research prose."
    )
    prompt = (
        "Source: " + source + "\n\n"
        "Source text:\n" + text[:12000] + "\n\n"
        "Produce a structured enrichment with exactly these headings:\n"
        "प्रश्न\nसार\nपरीक्षण-योग्य बिंदु\nसीमाएँ\n"
        "Use the source text faithfully and label uncertainty."
    )
    return {"text": chat(prompt, system=system), "model": os.getenv("NVIDIA_MODEL", DEFAULT_MODEL)}
