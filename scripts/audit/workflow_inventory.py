#!/usr/bin/env python3
"""Build a read-only, evidence-preserving inventory of GitHub Actions workflows.

This is a triage aid, not an automatic deletion recommender. It uses conservative
line-based extraction (no third-party YAML dependency); every record remains
UNKNOWN until a human reviews behavior, consumers and run history.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = ROOT / ".github" / "workflows"

def _block(lines: list[str], key: str) -> list[str]:
    """Return an indented YAML block after a top-level key, conservatively."""
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:\s*(?:#.*)?$", line):
            start = i + 1
            break
    if start is None:
        return []
    out = []
    for line in lines[start:]:
        if line.strip() and not line.startswith((" ", "\t", "#")):
            break
        out.append(line)
    return out

def inspect_workflow(path: Path, root: Path = ROOT) -> dict:
    source = path.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    name_match = re.search(r"(?m)^name\s*:\s*(.*?)\s*$", source)
    name = name_match.group(1).strip().strip("'\"") if name_match else path.stem
    on_lines = _block(lines, "on") or _block(lines, "'on'")
    triggers = []
    for line in on_lines:
        match = re.match(r"^\s{2}([A-Za-z_][A-Za-z0-9_-]*)\s*:", line)
        if match and match.group(1) not in triggers:
            triggers.append(match.group(1))
    if on_lines and not triggers:
        top = next((x.strip() for x in lines if re.match(r"^(?:on|'on')\s*:", x)), "")
        if top:
            triggers = [f"RAW:{top}"]
    schedule_crons = []
    if "schedule" in triggers:
        schedule_crons = re.findall(r"(?m)^\s*cron\s*:\s*['\"]([^'\"]+)['\"]", source)
    permissions = _block(lines, "permissions")
    concurrency = _block(lines, "concurrency")
    jobs_block = _block(lines, "jobs")
    job_ids = []
    for line in jobs_block:
        match = re.match(r"^  ([A-Za-z_][A-Za-z0-9_-]*)\s*:", line)
        if match and match.group(1) not in job_ids:
            job_ids.append(match.group(1))
    action_refs = re.findall(r"(?m)^\s*uses\s*:\s*([^\s#]+)", source)
    unpinned_actions = [ref for ref in action_refs if not re.search(r"@[0-9a-fA-F]{40}$", ref)]
    upstream_workflows = []
    wr = re.search(r"(?ms)^\s{2}workflow_run\s*:\s*\n(.*?)(?=^\s{2}[A-Za-z_][A-Za-z0-9_-]*\s*:|\Z)", source)
    if wr:
        section = wr.group(1)
        names = re.findall(r"(?m)^\s*-\s*['\"]?([^\n'\"]+?)['\"]?\s*$", section)
        upstream_workflows = [n.strip() for n in names if n.strip() and n.strip() not in {"completed", "requested", "in_progress"}]
    return {
        "path": str(path.relative_to(root)),
        "name": name,
        "triggers": triggers,
        "schedule_crons": sorted(set(schedule_crons)),
        "permissions_declared": bool(permissions),
        "permissions_block": [line.rstrip() for line in permissions],
        "concurrency_declared": bool(concurrency),
        "concurrency_block": [line.rstrip() for line in concurrency],
        "job_ids": job_ids,
        "action_reference_count": len(action_refs),
        "unpinned_action_references": unpinned_actions,
        "workflow_run_upstream_names": upstream_workflows,
        "triage_status": "UNKNOWN",
        "deletion_candidate": False,
        "triage_note": "No removal decision made; compare implementation, consumers, run history and critical-path coverage.",
    }

def build_inventory(workflow_dir: Path = WORKFLOWS, root: Path = ROOT) -> dict:
    files = sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml")))
    records = [inspect_workflow(path, root=root) for path in files]
    name_counts = {}
    for record in records:
        name_counts[record["name"]] = name_counts.get(record["name"], 0) + 1
    for record in records:
        record["duplicate_display_name_count"] = name_counts[record["name"]]
        record["duplicate_name_is_not_removal_evidence"] = name_counts[record["name"]] > 1
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "static metadata inventory of .github/workflows/*.yml and *.yaml",
        "workflow_file_count": len(records),
        "triage_status_counts": {"UNKNOWN": len(records)},
        "policy": [
            "This report does not decide that a workflow is redundant or safe to delete.",
            "Duplicate display names and similar triggers are review signals only, never deletion evidence.",
            "Use run history, downstream consumers, artifacts, permissions, public outputs and recovery behavior before proposing changes.",
            "Preserve critical paths for deploy, security, persistence, product/media integrity, verification and recovery.",
        ],
        "workflows": records,
        "limitations": [
            "Conservative line-based extraction is not a complete YAML parser.",
            "Does not query GitHub Actions run history, repository settings, secrets, artifacts or deployed pages.",
            "Manual review is required before any consolidation, disabling or deletion.",
        ],
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-dir", type=Path, default=WORKFLOWS)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    report = build_inventory(args.workflow_dir, args.root)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Workflow inventory written: {args.output} ({report['workflow_file_count']} files)")
    else:
        print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
