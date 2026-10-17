#!/usr/bin/env python3
"""Conservative, read-only GitHub Actions inventory. Never deletes or edits workflows."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# These terms are deliberately conservative review hints, not semantic proof.
_CRITICAL_WORK_HINTS = re.compile(
    r"(production|deploy|release|publish|persist|truth|integrity|backup|restore|"
    r"recovery|migration|factory|automission|security|state)",
    re.IGNORECASE,
)


def _top_level_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", text)
    return match.group(1) if match else None


def _events(text: str) -> list[str]:
    """Read top-level workflow event keys; conservative for YAML variants."""
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines)
                  if re.match(r"^on:\s*(?:#.*)?$", line)), None)
    if start is None:
        inline = re.search(r"(?m)^on:\s*\[([^]]*)\]", text)
        return sorted(
            x.strip().strip('"\'')
            for x in inline.group(1).split(",") if x.strip()
        ) if inline else []
    events: list[str] = []
    for line in lines[start + 1:]:
        if line and not line[0].isspace() and not line.startswith("#"):
            break
        match = re.match(r"^  ([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)", line)
        if match:
            events.append(match.group(1))
    return sorted(set(events))


def _concurrency_group(text: str) -> str | None:
    """Return a simple concurrency group value when it is statically readable."""
    match = re.search(r"(?m)^\s+group:\s*(.*?)\s*(?:#.*)?$", text)
    if not match:
        return None
    value = match.group(1).strip().strip('"\'')
    return value or None


def _timeout_values(text: str) -> list[int]:
    values = re.findall(r"(?m)^\s+timeout-minutes:\s*(\d+)\s*(?:#.*)?$", text)
    return sorted({int(value) for value in values})


def inspect_workflow(path: Path, root: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    name = _top_level_value(text, "name") or path.stem
    events = _events(text)
    permissions = re.search(r"(?ms)^permissions:\s*\n((?:^[ \t]+.*\n?)*)", text)
    permission_block = permissions.group(1) if permissions else ""
    write_permissions = bool(
        re.search(r"(?m)^\s+[A-Za-z0-9_-]+:\s*write\s*$", permission_block)
    )
    cancel = re.search(r"(?m)^\s+cancel-in-progress:\s*(true|false)\s*$", text)
    cancel_in_progress = cancel.group(1).lower() == "true" if cancel else None
    concurrency_group = _concurrency_group(text)
    timeout_values = _timeout_values(text)
    review_reasons = []

    if events == ["workflow_dispatch"]:
        review_reasons.append(
            "manual-dispatch-only: confirm this is still needed; not a deletion recommendation"
        )
    if write_permissions:
        review_reasons.append(
            "write-permission: retain unless a documented least-privilege replacement is verified"
        )
    if cancel_in_progress is True:
        review_reasons.append(
            "cancels-in-progress: inspect concurrency group and critical-work impact"
        )
        if write_permissions or _CRITICAL_WORK_HINTS.search(name + " " + path.as_posix()):
            review_reasons.append(
                "critical-work-cancellation-risk: verify this cannot cancel a production writer, "
                "deployment, persistence, recovery, or security gate"
            )
    if not timeout_values:
        review_reasons.append(
            "no-static-timeout-minutes-found: inspect job-level runtime bounds; "
            "this parser may not recognize all YAML forms"
        )

    return {
        "path": path.relative_to(root).as_posix(),
        "name": name.strip().strip('"\''),
        "events": events,
        "event_signature": "+".join(events) if events else "unknown",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "write_permissions": write_permissions,
        "concurrency_group": concurrency_group,
        "cancel_in_progress": cancel_in_progress,
        "timeout_minutes": timeout_values,
        "review_reasons": review_reasons,
    }


def build_report(root: Path) -> dict:
    workflow_dir = root / ".github" / "workflows"
    entries = []
    if workflow_dir.exists():
        for path in sorted(workflow_dir.iterdir()):
            if path.is_file() and path.suffix.lower() in {".yml", ".yaml"}:
                entries.append(inspect_workflow(path, root))

    by_hash: dict[str, list[str]] = defaultdict(list)
    by_name: dict[str, list[str]] = defaultdict(list)
    by_event_signature: dict[str, list[str]] = defaultdict(list)
    for item in entries:
        by_hash[item["sha256"]].append(item["path"])
        by_name[item["name"].casefold()].append(item["path"])
        by_event_signature[item["event_signature"]].append(item["path"])

    candidates = []
    for digest, paths in sorted(by_hash.items()):
        if len(paths) > 1:
            candidates.append({
                "type": "exact-content-duplicate-review",
                "paths": paths,
                "reason": "byte-identical files; verify references and triggers before any retirement",
            })
    for name, paths in sorted(by_name.items()):
        if len(paths) > 1:
            candidates.append({
                "type": "duplicate-name-review",
                "paths": paths,
                "reason": "same declared workflow name; inspect behavior and triggers manually",
            })
    for item in entries:
        if item["review_reasons"]:
            candidates.append({
                "type": "workflow-risk-review",
                "paths": [item["path"]],
                "reason": "; ".join(item["review_reasons"]),
            })

    event_counts: dict[str, int] = defaultdict(int)
    for item in entries:
        for event in item["events"]:
            event_counts[event] += 1

    return {
        "schema_version": 2,
        "mode": "read-only",
        "deletion_performed": False,
        "changes_performed": False,
        "scope": ".github/workflows/*.yml and *.yaml in the checked-out repository",
        "workflow_count": len(entries),
        "event_counts": dict(sorted(event_counts.items())),
        "exact_duplicate_groups": sum(1 for paths in by_hash.values() if len(paths) > 1),
        "duplicate_name_groups": sum(1 for paths in by_name.values() if len(paths) > 1),
        "same_event_signature_groups": sum(
            1 for paths in by_event_signature.values() if len(paths) > 1
        ),
        "workflows": entries,
        "review_candidates": candidates,
        "policy": [
            "A candidate is a human-review lead, never an automatic deletion instruction.",
            "Matching event signatures are not proof of duplicate behavior.",
            "Do not retire security, deployment, persistence, data-integrity, or recovery workflows based on names or run counts.",
            "Before any removal, prove replacement coverage, inspect dependencies and recent run history, preserve the file in version control, and test on a branch.",
            "Skipped, cancelled, pending, and successful runs are distinct states and must not be conflated.",
            "This static audit does not inspect live run queues, job dependencies, external repositories, or deployed services.",
        ],
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(build_report(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
