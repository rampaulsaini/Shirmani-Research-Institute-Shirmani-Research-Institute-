#!/usr/bin/env python3
"""Fail-closed release evidence validator for SHIRMANI SUPREME Character Studio.

This validates a submitted evidence packet; it does not call HeyGen, create media,
or independently prove claims. A human reviewer must verify artifacts.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from typing import Any

TIERS = ("V1", "V2", "V3", "V4")
REQUIRED_FAILURE_PATHS = ("timeout", "rate_limit", "network_disconnect", "provider_outage", "insufficient_evidence")

def percentile(values: list[float], p: float) -> float:
    """Nearest-rank percentile; reject empty samples or invalid percentile."""
    if not values or not 0 <= p <= 100:
        raise ValueError("percentile requires samples and p in [0, 100]")
    ordered = sorted(float(value) for value in values)
    rank = max(1, int((p / 100.0) * len(ordered) + 0.999999))
    return ordered[min(rank - 1, len(ordered) - 1)]

def validate_packet(packet: dict[str, Any]) -> list[str]:
    """Return blocking reasons; empty means structurally eligible for human review."""
    errors: list[str] = []
    candidate, tiers = packet.get("release_candidate"), packet.get("tiers")
    if not isinstance(candidate, dict) or not isinstance(tiers, dict):
        return ["release_candidate and tiers objects are required"]
    build_id = candidate.get("build_id")
    if not isinstance(build_id, str) or not build_id.strip():
        errors.append("release_candidate.build_id is required")
    if candidate.get("reviewed") is not True:
        errors.append("release_candidate.reviewed must be true after human evidence review")
    if candidate.get("security_checks_passed") is not True:
        errors.append("release_candidate.security_checks_passed must be true")

    for tier in TIERS:
        item = tiers.get(tier)
        if not isinstance(item, dict):
            errors.append(f"{tier}: evidence object missing")
            continue
        if item.get("status") != "PASS":
            errors.append(f"{tier}: status must be PASS (got {item.get('status', 'MISSING')})")
        if item.get("build_id") != build_id or not build_id:
            errors.append(f"{tier}: build_id must match release candidate")
        urls = item.get("evidence_urls")
        if not isinstance(urls, list) or not urls or any(
            not isinstance(url, str) or not url.startswith("https://") for url in urls
        ):
            errors.append(f"{tier}: real HTTPS evidence URLs are required")

    v1 = tiers.get("V1", {})
    if isinstance(v1, dict):
        checks = v1.get("assertions")
        keys = ("hindi_prompt", "english_prompt", "evidence_states", "insufficient_evidence_notice", "original_photo_policy")
        if not isinstance(checks, dict) or not all(checks.get(k) is True for k in keys):
            errors.append("V1: all five Character Studio assertions must be true")

    v2 = tiers.get("V2", {})
    if isinstance(v2, dict):
        if v2.get("authorization_verified") is not True:
            errors.append("V2: provider-side voice authorization evidence missing")
        if not isinstance(v2.get("audio_output_url"), str) or not v2["audio_output_url"].startswith("https://"):
            errors.append("V2: real generated audio URL is required")

    v3 = tiers.get("V3", {})
    if isinstance(v3, dict):
        source_hash = v3.get("source_sha256")
        if not isinstance(source_hash, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", source_hash):
            errors.append("V3: actual source asset SHA-256 is required")
        if not isinstance(v3.get("rendered_video_url"), str) or not v3["rendered_video_url"].startswith("https://"):
            errors.append("V3: real rendered video URL is required")
        samples, threshold = v3.get("lip_sync_offset_ms"), v3.get("lip_sync_threshold_ms")
        if not isinstance(samples, list) or not samples or any(
            not isinstance(n, (int, float)) or n < 0 for n in samples
        ):
            errors.append("V3: non-negative measured lip_sync_offset_ms samples are required")
        elif not isinstance(threshold, (int, float)) or threshold <= 0:
            errors.append("V3: positive declared lip_sync_threshold_ms is required")
        elif max(samples) > threshold:
            errors.append("V3: measured lip-sync offset exceeds declared threshold")

    v4 = tiers.get("V4", {})
    if isinstance(v4, dict):
        latencies = v4.get("latency_ms")
        if not isinstance(latencies, list) or len(latencies) < 5 or any(
            not isinstance(n, (int, float)) or n < 0 for n in latencies
        ):
            errors.append("V4: at least five non-negative real latency samples are required")
        else:
            v4["computed_p50_ms"] = percentile(latencies, 50)
            v4["computed_p95_ms"] = percentile(latencies, 95)
        failures = v4.get("failure_paths")
        if not isinstance(failures, dict) or not all(failures.get(k) is True for k in REQUIRED_FAILURE_PATHS):
            errors.append("V4: timeout, rate-limit, network, provider-outage, and insufficient-evidence tests must pass")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="JSON evidence packet from real test runs")
    parser.add_argument("--write-report", type=Path, help="write packet plus gate result")
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"release_status": "BLOCKED", "errors": [str(exc)]}, indent=2))
        return 2
    if not isinstance(packet, dict):
        print(json.dumps({"release_status": "BLOCKED", "errors": ["packet root must be an object"]}, indent=2))
        return 2
    errors = validate_packet(packet)
    result = {
        "release_status": "ELIGIBLE_FOR_HUMAN_REVIEW" if not errors else "BLOCKED",
        "errors": errors,
        "warning": "Structural validation is not independent verification. Review actual artifacts before release."
    }
    rendered = json.dumps({"packet": packet, "gate": result}, ensure_ascii=False, indent=2)
    print(rendered)
    if args.write_report:
        args.write_report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(main())
