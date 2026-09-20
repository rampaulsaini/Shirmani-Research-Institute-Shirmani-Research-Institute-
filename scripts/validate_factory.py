#!/usr/bin/env python3
"""Deterministic, dependency-free validation for the research-factory contracts."""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_JSON = {
    "generated/factory-status.json": ["generated_at", "mode", "status", "records", "qc", "dashboard_contract", "integrity"],
    "generated/agent-status.json": ["agents"],
    "generated/federation-status.json": [],
    "generated/source-registry.json": ["generated_at", "repository_count", "repositories"],
    "generated/research-index.json": ["schema_version", "status", "source_registry", "claim_records", "coverage", "integrity"],
}

def load_json(rel):
    path = ROOT / rel
    if not path.is_file():
        raise AssertionError(f"missing file: {rel}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"invalid JSON: {rel}: {exc}") from exc

def require_keys(obj, keys, rel):
    for key in keys:
        if key not in obj:
            raise AssertionError(f"{rel}: missing required key {key!r}")

def main():
    loaded = {}
    for rel, keys in REQUIRED_JSON.items():
        loaded[rel] = load_json(rel)
        require_keys(loaded[rel], keys, rel)

    factory = loaded["generated/factory-status.json"]
    if factory["records"] is not None and not isinstance(factory["records"], int):
        raise AssertionError("factory-status.json: records must be integer or null")
    if factory["integrity"].get("fabricated_metrics") is not False:
        raise AssertionError("factory-status.json: fabricated_metrics must be false")

    registry = loaded["generated/source-registry.json"]
    repos = registry["repositories"]
    if not isinstance(repos, list):
        raise AssertionError("source-registry.json: repositories must be an array")
    if registry["repository_count"] != len(repos):
        raise AssertionError("source-registry.json: repository_count does not match repositories length")

    index = loaded["generated/research-index.json"]
    if index["claim_records"] != []:
        raise AssertionError("research-index.json: continuity baseline expects zero verified claim records")
    if index["integrity"].get("fabricated_records") is not False:
        raise AssertionError("research-index.json: fabricated_records must be false")
    if index["integrity"].get("missing_data_preserved") is not True:
        raise AssertionError("research-index.json: missing_data_preserved must be true")

    print("FACTORY CONTRACT VALIDATION: PASS")
    print(f"JSON contracts checked: {len(REQUIRED_JSON)}")
    print(f"Registered repositories: {registry['repository_count']}")
    print("Verified claim records: 0")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FACTORY CONTRACT VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
