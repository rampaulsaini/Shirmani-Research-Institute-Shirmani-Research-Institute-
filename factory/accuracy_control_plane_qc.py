#!/usr/bin/env python3
"""Fail-closed validator for the deterministic accuracy-control report."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "generated" / "ACCURACY-CONTROL.json"


def main() -> int:
    if not REPORT.is_file():
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: report missing")
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    required = {
        "schema_version", "control_plane", "interpretation", "records",
        "verified_records_promoted", "mean_readiness_score",
        "failure_counts", "fail_closed", "publication_gate"
    }
    missing = required - set(data)
    if missing:
        raise SystemExit(f"ACCURACY-CONTROL-QC: BLOCK: missing fields {sorted(missing)}")
    if data["fail_closed"] is not True:
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: fail_closed must be true")
    if data["verified_records_promoted"] != 0:
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: control plane must never promote verification")
    if not (0 <= float(data["mean_readiness_score"]) <= 100):
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: score outside [0,100]")
    if data["publication_gate"] not in {"PASS", "BLOCK"}:
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: invalid publication gate")
    if "truth probability" not in data["interpretation"]:
        raise SystemExit("ACCURACY-CONTROL-QC: BLOCK: interpretation boundary missing")
    print("ACCURACY-CONTROL-QC: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
