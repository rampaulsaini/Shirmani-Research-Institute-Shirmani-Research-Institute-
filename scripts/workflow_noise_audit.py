#!/usr/bin/env python3
"""Conservative, read-only GitHub Actions inventory. Never deletes or edits workflows."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

TEXT_SUFFIXES = {".yml", ".yaml", ".py", ".md", ".json", ".toml", ".sh", ".js", ".ts"}
SCAN_ROOTS = (".github", "scripts", "docs")
ROOT_TEXT_FILES = ("README.md", "CONTRIBUTING.md", "Makefile")


def _top_level_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", text)
    return match.group(1) if match else None


def _events(text: str) -> list[str]:
    """Read only top-level workflow event keys; conservative for YAML variants."""
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r"^on:\s*(?:#.*)?$", line)), None)
    if start is None:
        inline = re.search(r"(?m)^on:\s*\[([^]]*)\]", text)
        return sorted(x.strip().strip("\\\"'") for x in inline.group(1).split(",") if x.strip()) if inline else []
    events: list[str] = []
    for line in lines[start + 1:]:
        if line and not line[0].isspace() and not line.startswith("#"):
            break
        match = re.match(r"^  ([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)", line)
        if match:
            events.append(match.group(1))
    return sorted(set(events))


def _reference_index(root: Path, workflow_paths: list[Path]) -> dict[str, list[str]]:
    """Find literal path/name references in likely source/config/docs; never infer safety from absence."""
    scan_files: set[Path] = set()
    for relative_root in SCAN_ROOTS:
        base = root / relative_root
        if base.exists():
            scan_files.update(
                p for p in base.rglob("*")
                if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES and p.stat().st_size <= 2_000_000
            )
    scan_files.update(p for p in (root / name for name in ROOT_TEXT_FILES) if p.is_file())
    index: dict[str, list[str]] = {}
    for workflow in workflow_paths:
        rel = workflow.relative_to(root).as_posix()
        basename = workflow.name
        matches: list[str] = []
        for source in sorted(scan_files):
            if source == workflow:
                continue
            try:
                text = source.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if rel in text or basename in text:
                matches.append(source.relative_to(root).as_posix())
        index[rel] = matches
    return index


def inspect_workflow(path: Path, root: Path, referenced_by: list[str] | None = None) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    name = _top_level_value(text, "name") or path.stem
    events = _events(text)
    permissions = re.search(r"(?ms)^permissions:\s*\n((?:^[ \t]+.*\n?)*)", text)
    permission_block = permissions.group(1) if permissions else ""
    write_permissions = bool(re.search(r"(?m)^\s+[A-Za-z0-9_-]+:\s*write\s*$", permission_block))
    cancel = re.search(r"(?m)^\s+cancel-in-progress:\s*(true|false)\s*$", text)
    cancel_in_progress = cancel.group(1).lower() == "true" if cancel else None
    concurrency = re.search(r"(?m)^\s+group:\s*(.*?)\s*$", text)
    cron_values = re.findall(r'(?m)^\s+-\s+cron:\s*["\']?([^"\'\n]+)', text)
    review_reasons = []
    if events == ["workflow_dispatch"]:
        review_reasons.append("manual-dispatch-only: confirm this is still needed; not a deletion recommendation")
    if write_permissions:
        review_reasons.append("write-permission: retain unless a documented least-privilege replacement is verified")
    if cancel_in_progress is True:
        review_reasons.append("cancels-in-progress: inspect concurrency group and critical-work impact")
    return {
        "path": path.relative_to(root).as_posix(),
        "name": name.strip().strip("\\\"'"),
        "events": events,
        "schedule_crons": cron_values,
        "concurrency_group": concurrency.group(1).strip().strip("\\\"'") if concurrency else None,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "write_permissions": write_permissions,
        "cancel_in_progress": cancel_in_progress,
        "referenced_by": referenced_by or [],
        "reference_scan": "literal-reference-scan; absence is not proof of no dependency",
        "review_reasons": review_reasons,
    }


def build_report(root: Path) -> dict:
    workflow_dir = root / ".github" / "workflows"
    paths = []
    if workflow_dir.exists():
        paths = [p for p in sorted(workflow_dir.iterdir()) if p.is_file() and p.suffix.lower() in {".yml", ".yaml"}]
    references = _reference_index(root, paths)
    entries = [inspect_workflow(path, root, references.get(path.relative_to(root).as_posix(), [])) for path in paths]
    by_hash: dict[str, list[str]] = defaultdict(list)
    by_name: dict[str, list[str]] = defaultdict(list)
    for item in entries:
        by_hash[item["sha256"]].append(item["path"])
        by_name[item["name"].casefold()].append(item["path"])
    candidates = []
    for digest, dup_paths in sorted(by_hash.items()):
        if len(dup_paths) > 1:
            candidates.append({
                "type": "exact-content-duplicate-review",
                "paths": dup_paths,
                "referenced_by": {p: references.get(p, []) for p in dup_paths},
                "reason": "byte-identical files; compare references, triggers, run history and required checks before any retirement",
            })
    for _, dup_paths in sorted(by_name.items()):
        if len(dup_paths) > 1:
            candidates.append({
                "type": "duplicate-name-review",
                "paths": dup_paths,
                "referenced_by": {p: references.get(p, []) for p in dup_paths},
                "reason": "same declared workflow name; inspect behavior and triggers manually",
            })
    for item in entries:
        if item["review_reasons"]:
            candidates.append({
                "type": "workflow-risk-review",
                "paths": [item["path"]],
                "referenced_by": {item["path"]: item["referenced_by"]},
                "reason": "; ".join(item["review_reasons"]),
            })
    return {
        "schema_version": 2,
        "mode": "read-only",
        "deletion_performed": False,
        "scope": "workflow files plus literal references in .github, scripts, docs, and selected root project files",
        "workflow_count": len(entries),
        "exact_duplicate_groups": sum(1 for values in by_hash.values() if len(values) > 1),
        "duplicate_name_groups": sum(1 for values in by_name.values() if len(values) > 1),
        "workflows": entries,
        "review_candidates": candidates,
        "policy": [
            "A candidate is a human-review lead, never an automatic deletion instruction.",
            "A literal reference is evidence to inspect; no detected reference is not proof that a workflow is unused.",
            "Do not retire security, deployment, persistence, data-integrity, or recovery workflows based on names or run counts.",
            "Before any removal, prove replacement coverage, inspect dependencies and recent run history, preserve the file in version control, and test on a branch.",
            "Skipped, cancelled, pending, and successful runs are distinct states and must not be conflated.",
            "Never auto-cancel production writers or deployment workflows as a noise-reduction shortcut.",
        ],
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(build_report(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
