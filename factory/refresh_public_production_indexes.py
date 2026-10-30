#!/usr/bin/env python3
"""Rebuild derived public production indexes from already-produced lane records.

This does not rerun production or rewrite lane artifacts. It validates the
current queue against existing lane outputs, then materializes the canonical
result stream, latest cycle shard, catalog summary, and archive index.
"""
from __future__ import annotations

import json
import os
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
QUEUE = GEN / "production-work-queue.jsonl"
RESULTS = GEN / "production-results.jsonl"
LANES = GEN / "public-production"
ARCHIVE = LANES / "archive"
CATALOG = GEN / "public-production-catalog.json"
ARCHIVE_INDEX = ARCHIVE / "index.json"


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.is_file():
        raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: missing {path.relative_to(ROOT)}")
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"PUBLIC_INDEX_REFRESH_FAILED: invalid JSONL {path.relative_to(ROOT)}:{line_no}: {exc}"
            )
        if not isinstance(row, dict):
            raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: non-object row in {path}:{line_no}")
        rows.append(row)
    return rows


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def atomic_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> None:
    queue_rows = read_jsonl(QUEUE)
    if not queue_rows:
        raise SystemExit("PUBLIC_INDEX_REFRESH_FAILED: production queue is empty")

    queue_by_id = {}
    cycles = set()
    for row in queue_rows:
        task_id = str(row.get("task_id", "")).strip()
        if not task_id or task_id in queue_by_id:
            raise SystemExit("PUBLIC_INDEX_REFRESH_FAILED: queue task IDs are missing or duplicated")
        try:
            cycle = int(row["cycle"])
            slot = int(row["slot"])
        except (KeyError, TypeError, ValueError):
            raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: queue task {task_id} has invalid cycle/slot")
        row["_cycle"] = cycle
        row["_slot"] = slot
        queue_by_id[task_id] = row
        cycles.add(cycle)

    if len(cycles) != 1:
        raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: queue spans multiple cycles: {sorted(cycles)}")

    lane_files = sorted(p for p in LANES.glob("*.jsonl") if p.is_file())
    if not lane_files:
        raise SystemExit("PUBLIC_INDEX_REFRESH_FAILED: no public production lane files found")

    produced_by_id = {}
    lane_counts = Counter()
    for lane_file in lane_files:
        lane_name = lane_file.stem
        for row in read_jsonl(lane_file):
            task_id = str(row.get("task_id", "")).strip()
            if not task_id or task_id in produced_by_id:
                raise SystemExit("PUBLIC_INDEX_REFRESH_FAILED: produced task IDs are missing or duplicated")
            queued = queue_by_id.get(task_id)
            if queued is None:
                raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: output task {task_id} is absent from current queue")
            integrity = row.get("integrity") if isinstance(row.get("integrity"), dict) else {}
            try:
                row_cycle = int(row.get("cycle"))
                row_slot = int(row.get("slot"))
            except (TypeError, ValueError):
                raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: output task {task_id} has invalid cycle/slot")
            if row_cycle != queued["_cycle"] or row_slot != queued["_slot"]:
                raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: output task {task_id} does not match queued cycle/slot")
            if row.get("lane") != lane_name or row.get("status") != "PRODUCED":
                raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: output task {task_id} has wrong lane/status")
            if row.get("module") != queued.get("module") or integrity.get("source_bound") is not True:
                raise SystemExit(f"PUBLIC_INDEX_REFRESH_FAILED: output task {task_id} lacks matching source binding")
            produced_by_id[task_id] = row
            lane_counts[lane_name] += 1

    missing = sorted(set(queue_by_id) - set(produced_by_id))
    if missing:
        raise SystemExit(
            f"PUBLIC_INDEX_REFRESH_FAILED: {len(missing)} queued tasks lack produced lane records; "
            f"first missing IDs: {missing[:5]}"
        )

    results = sorted(produced_by_id.values(), key=lambda row: (int(row["slot"]), str(row["task_id"])))
    latest_cycle = next(iter(cycles))
    generated_at = datetime.now(timezone.utc).isoformat()
    archive_file = ARCHIVE / f"production-cycle-{latest_cycle:06d}.jsonl"

    # Only derived aggregate/index files are refreshed; lane records remain untouched.
    atomic_jsonl(RESULTS, results)
    atomic_jsonl(archive_file, results)

    archive_files = sorted(p.name for p in ARCHIVE.glob("production-cycle-*.jsonl") if p.is_file())
    atomic_json(ARCHIVE_INDEX, {
        "generated_at": generated_at,
        "shard_strategy": "one JSONL file per production cycle",
        "cycle_shards": len(archive_files),
        "files": archive_files,
        "latest_cycle": latest_cycle,
        "latest_cycle_records": len(results),
        "integrity": {
            "records_are_produced_artifacts": True,
            "queue_to_lane_records_one_to_one": True,
            "independent_verification_claim": False
        }
    })
    atomic_json(CATALOG, {
        "generated_at": generated_at,
        "principle": "Production first; verification downstream.",
        "cycle": latest_cycle,
        "cycle_results": len(results),
        "lanes": dict(sorted(lane_counts.items())),
        "artifacts": [
            f"generated/public-production/{name}.jsonl" for name in sorted(lane_counts)
        ] + [
            "generated/production-results.jsonl",
            "generated/public-production/archive/index.json"
        ],
        "integrity": {
            "generated_output_is_concrete": True,
            "source_bound": True,
            "queue_to_lane_records_one_to_one": True,
            "independent_verification_claim": False
        }
    })

    print(json.dumps({
        "cycle": latest_cycle,
        "queued_tasks": len(queue_rows),
        "produced_lane_records": len(results),
        "lane_counts": dict(sorted(lane_counts.items())),
        "archive_shards": len(archive_files),
        "derived_indexes_refreshed": 3,
        "lane_records_rewritten": 0,
        "independent_verification_claim": False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
