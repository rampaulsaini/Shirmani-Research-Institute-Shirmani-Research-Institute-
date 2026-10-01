#!/usr/bin/env python3
"""Deterministic evidence gate for perception-to-language records.

This gate is model-agnostic. It validates provenance, uncertainty and the
observation -> inference evidence boundary before an agent may emit language.
It never treats model confidence or workflow success as proof of subjective
experience or scientific truth.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ALLOWED = {
    "OBSERVED",
    "DERIVED",
    "INFERRED",
    "HYPOTHESIS",
    "AUTHOR_CLAIM",
    "UNVERIFIED",
}
MODALITIES = {"text", "audio", "image", "video", "sensor", "structured", "mixed"}
SUBJECT_TYPES = {"human", "animal", "plant", "ecosystem", "machine", "object", "unknown"}


def _is_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def validate(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("record_id", "timestamp", "status", "modality", "content", "provenance")

    for key in required:
        if key not in record or record[key] in (None, ""):
            errors.append(f"missing:{key}")

    if not isinstance(record.get("record_id"), str) or not record.get("record_id"):
        errors.append("invalid:record_id")
    if not _is_datetime(record.get("timestamp")):
        errors.append("invalid:timestamp")
    if record.get("status") not in ALLOWED:
        errors.append("invalid:status")
    if record.get("modality") not in MODALITIES:
        errors.append("invalid:modality")
    if "subject_type" in record and record["subject_type"] not in SUBJECT_TYPES:
        errors.append("invalid:subject_type")
    if not isinstance(record.get("content"), str) or not record.get("content").strip():
        errors.append("invalid:content")

    provenance = record.get("provenance")
    if not isinstance(provenance, dict) or not provenance.get("source_id"):
        errors.append("invalid:provenance")

    features = record.get("features", [])
    if not isinstance(features, list):
        errors.append("invalid:features")

    evidence_refs = record.get("evidence_refs", [])
    if not isinstance(evidence_refs, list) or any(
        not isinstance(item, str) or not item.strip() for item in evidence_refs
    ):
        errors.append("invalid:evidence_refs")

    uncertainty = record.get("uncertainty")
    if uncertainty is not None and (
        isinstance(uncertainty, bool)
        or not isinstance(uncertainty, (int, float))
        or not 0 <= uncertainty <= 1
    ):
        errors.append("invalid:uncertainty")

    if record.get("human_review") is not None and not isinstance(record["human_review"], bool):
        errors.append("invalid:human_review")

    # Evidence boundary: an inferred interpretation needs traceable evidence.
    if record.get("status") == "INFERRED" and not evidence_refs:
        errors.append("inferred_requires_evidence_refs")

    # A model identity is required whenever a record claims model-derived inference.
    if record.get("status") in {"DERIVED", "INFERRED"}:
        if not record.get("model") or not record.get("model_version"):
            errors.append("model_derived_requires_model_identity")

    # Explicit abstention is allowed and preferred when evidence is insufficient.
    if record.get("status") == "UNVERIFIED" and not record.get("content"):
        errors.append("unverified_requires_explanation")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: nlp_perception_gate.py RECORD.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "REJECT", "errors": [f"input:{exc}"]}, ensure_ascii=False))
        return 1

    if not isinstance(record, dict):
        print(json.dumps({"status": "REJECT", "errors": ["input:not_object"]}, ensure_ascii=False))
        return 1

    errors = validate(record)
    result = {
        "status": "PASS" if not errors else "REJECT",
        "record_id": record.get("record_id"),
        "evidence_boundary": "OK" if not errors else "BLOCKED",
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
