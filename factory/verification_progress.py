#!/usr/bin/env python3
"""Build a fail-closed, machine-readable independent-verification progress map."""
from __future__ import annotations
import argparse, gzip, json
from collections import Counter
from pathlib import Path

def load_jsonl(path: Path):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line.strip():
                try:
                    yield line_no, json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"invalid JSON at {path}:{line_no}: {exc}") from exc

def pct(n, d):
    return round((100.0 * n / d), 2) if d else 0.0

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queue", required=True)
    p.add_argument("--registry", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    queue = list(load_jsonl(Path(args.queue)))
    registry = list(load_jsonl(Path(args.registry)))
    q_ids = {str(r.get("task_id")) for _, r in queue if r.get("task_id") is not None}
    r_ids = {str(r.get("task_id")) for _, r in registry if r.get("task_id") is not None}
    if len(q_ids) != len(queue) or len(r_ids) != len(registry):
        raise SystemExit("verification queue/registry contains missing or duplicate task IDs")
    if q_ids != r_ids:
        raise SystemExit("verification queue and registry task sets do not match")

    verification = Counter(str(r.get("verification_status", "UNKNOWN")).upper() for _, r in registry)
    status = Counter(str(r.get("status", "UNKNOWN")).upper() for _, r in registry)
    total = len(queue)
    verified = verification.get("VERIFIED", 0)
    reviewed = status.get("REVIEWED", 0)
    blocked = verification.get("BLOCKED", 0)
    remaining = max(total - verified, 0)

    report = {
        "version": 2,
        "scope": "independent-verification",
        "total_records": total,
        "queued_records": status.get("QUEUED", 0),
        "reviewed_records": reviewed,
        "verified_records": verified,
        "blocked_records": blocked,
        "remaining_to_verified": remaining,
        "verification_completion_pct": pct(verified, total),
        "review_completion_pct": pct(reviewed + verified, total),
        "target_records": total,
        "verification_remaining_pct": pct(remaining, total),
        "verification_status_counts": dict(sorted(verification.items())),
        "registry_status_counts": dict(sorted(status.items())),
        "promotion_policy": "FAIL_CLOSED",
        "workflow_success_is_not_verification": True,
        "human_or_independent_audit_required": True,
        "status": "VERIFICATION_REQUIRED" if verified < total else "VERIFICATION_COMPLETE",
        "next_action": (
            "Review the generated verification packets independently. A record may "
            "enter VERIFIED only after reviewer identity/audit, evidence references, "
            "countercase review, and reproduction/test requirements are satisfied."
        ),
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
