#!/usr/bin/env python3
"""Conservative, read-only GitHub Actions inventory. Never deletes or edits workflows."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

CRITICAL_TERMS = (
    "production", "deploy", "deployment", "security", "persistence",
    "truth", "integrity", "backup", "rollback", "recovery", "release",
)


def _top_level_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", text)
    return match.group(1) if match else None


def _events(text: str) -> list[str]:
    """Read only top-level workflow event keys; conservative for YAML variants."""
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r"^on:\s*(?:#.*)?$", line)), None)
    if start is None:
        inline = re.search(r"(?m)^on:\s*\[([^]]*)\]", text)
        return sorted(x.strip().strip("\"'") for x in inline.group(1).split(",") if x.strip()) if inline else []
    events: list[str] = []
    for line in lines[start + 1:]:
        if line and not line[0].isspace() and not line.startswith("#"):
            break
        match = re.match(r"^  ([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)", line)
        if match:
            events.append(match.group(1))
    return sorted(set(events))


def _workflow_run_consumers(text: str) -> list[str]:
    """Extract declared workflow_run workflow names without needing a YAML dependency."""
    block = re.search(r"(?ms)^  workflow_run:\s*\n(.*?)(?=^\S|\Z)", text)
    if not block:
        return []
    workflows = re.search(r"(?ms)^\s+workflows:\s*\n((?:^[ \t]+.*\n?)*)", block.group(1))
    if not workflows:
        return []
    names = []
    for line in workflows.group(1).splitlines():
        match = re.match(r"^\s+-\s*[\"']?([^\"'#]+?)[\"']?\s*(?:#.*)?$", line)
        if match:
            value = match.group(1).strip()
            if value:
                names.append(value)
    return sorted(set(names))


def _concurrency(text: str) -> tuple[str | None, bool | None]:
    group = re.search(r"(?m)^\s+group:\s*(.*?)\s*$", text)
    cancel = re.search(r"(?m)^\s+cancel-in-progress:\s*(true|false)\s*$", text)
    group_value = group.group(1).strip().strip("\"'") if group else None
    cancel_value = cancel.group(1).lower() == "true" if cancel else None
    return group_value, cancel_value


def inspect_workflow(path: Path, root: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    name = _top_level_value(text, "name") or path.stem
    events = _events(text)
    permissions = re.search(r"(?ms)^permissions:\s*\n((?:^[ \t]+.*\n?)*)", text)
    permission_block = permissions.group(1) if permissions else ""
    write_permissions = bool(re.search(r"(?m)^\s+[A-Za-z0-9_-]+:\s*write\s*$", permission_block))
    concurrency_group, cancel_in_progress = _concurrency(text)
    criticality = "critical-review" if any(term in (name + " " + path.as_posix()).casefold()
                                             for term in CRITICAL_TERMS) else "standard-review"
    review_reasons = []
    if events == ["workflow_dispatch"]:
        review_reasons.append("manual-dispatch-only: confirm this is still needed; not a deletion recommendation")
    if write_permissions:
        review_reasons.append("write-permission: retain unless a documented least-privilege replacement is verified")
    if cancel_in_progress is True:
        review_reasons.append("cancels-in-progress: inspect concurrency group and critical-work impact")
    if criticality == "critical-review" and cancel_in_progress is True:
        review_reasons.append("critical-workflow-cancellation-risk: prove a newer run cannot suppress required production/security work")
    return {
        "path": path.relative_to(root).as_posix(),
        "name": name.strip().strip("\"'"),
        "events": events,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "write_permissions": write_permissions,
        "concurrency_group": concurrency_group,
        "cancel_in_progress": cancel_in_progress,
        "criticality": criticality,
        "workflow_run_consumers": _workflow_run_consumers(text),
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
    by_workflow_name: dict[str, list[str]] = defaultdict(list)
    for item in entries:
        by_hash[item["sha256"]].append(item["path"])
        by_name[item["name"].casefold()].append(item["path"])
        by_workflow_name[item["name"].casefold()].append(item["path"])
    candidates = []
    for digest, paths in sorted(by_hash.items()):
        if len(paths) > 1:
            candidates.append({"type": "exact-content-duplicate-review", "paths": paths,
                               "reason": "byte-identical files; verify references and triggers before any retirement"})
    for name, paths in sorted(by_name.items()):
        if len(paths) > 1:
            candidates.append({"type": "duplicate-name-review", "paths": paths,
                               "reason": "same declared workflow name; inspect behavior and triggers manually"})
    for item in entries:
        if item["review_reasons"]:
            candidates.append({"type": "workflow-risk-review", "paths": [item["path"]],
                               "reason": "; ".join(item["review_reasons"])})
    consumers = []
    for item in entries:
        for upstream_name in item["workflow_run_consumers"]:
            matched = by_workflow_name.get(upstream_name.casefold(), [])
            consumers.append({
                "upstream_workflow_name": upstream_name,
                "upstream_paths": matched,
                "consumer_path": item["path"],
                "resolution": "matched" if matched else "unresolved-name-review",
            })
            if not matched:
                candidates.append({
                    "type": "unresolved-workflow-run-reference",
                    "paths": [item["path"]],
                    "reason": f"workflow_run references {upstream_name!r}, but no local workflow with that declared name was found; verify external/renamed dependency before changing anything",
                })
    return {
        "schema_version": 2,
        "mode": "read-only",
        "deletion_performed": False,
        "scope": ".github/workflows/*.yml and *.yaml in the checked-out repository",
        "workflow_count": len(entries),
        "critical_review_count": sum(1 for item in entries if item["criticality"] == "critical-review"),
        "exact_duplicate_groups": sum(1 for paths in by_hash.values() if len(paths) > 1),
        "duplicate_name_groups": sum(1 for paths in by_name.values() if len(paths) > 1),
        "workflow_run_dependencies": consumers,
        "workflows": entries,
        "review_candidates": candidates,
        "policy": [
            "A candidate is a human-review lead, never an automatic deletion instruction.",
            "Do not retire security, deployment, persistence, data-integrity, or recovery workflows based on names or run counts.",
            "Before any removal, prove replacement coverage, inspect dependencies and recent run history, preserve the file in version control, and test on a branch.",
            "Skipped, cancelled, pending, and successful runs are distinct states and must not be conflated.",
            "Criticality is a keyword-based review hint, not a security classification or proof of importance.",
            "Dependency matching covers local workflow_run names only; inspect reusable workflows, scripts, artifacts, external repositories, and runtime dependencies separately.",
        ],
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(build_report(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
