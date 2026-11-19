#!/usr/bin/env python3
"""Audit SHIRMANI SUPREME source media without treating candidates as authorised assets.

Usage:
  python scripts/audit_character_assets.py
  python scripts/audit_character_assets.py --external-media /path/to/recording.mp4

Exit codes: 0 = inventory generated (assets may remain blocked); 2 = invalid config/input.
This tool never uploads media, contacts providers, or changes asset files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".wav", ".mp3", ".m4a", ".ogg", ".mp4", ".mov", ".webm"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _media_record(path: Path, display_path: str, origin: str) -> dict:
    return {
        "path": display_path,
        "origin": origin,
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "suffix": path.suffix.lower(),
    }


def audit(root: Path, external_media: list[Path] | None = None) -> dict:
    config_path = root / "config" / "authorized-voice-integration.json"
    if not config_path.is_file():
        raise ValueError(f"Missing config: {config_path.relative_to(root)}")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    expected = config.get("source_assets", {})
    expected_hashes = {
        "photo": expected.get("photo_sha256"),
        "audio": expected.get("audio_sha256"),
    }
    candidates = []
    matched = {"photo": [], "audio": []}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in MEDIA_SUFFIXES:
            continue
        relative = path.relative_to(root).as_posix()
        candidates.append(_media_record(path, relative, "repository"))
    for index, raw_path in enumerate(external_media or [], start=1):
        path = raw_path.expanduser().resolve()
        if not path.is_file():
            raise ValueError(f"External media file not found: {path.name}")
        if path.suffix.lower() not in MEDIA_SUFFIXES:
            raise ValueError(f"Unsupported external media type: {path.suffix or '(no extension)'}")
        # Avoid exposing the caller's full local filesystem path in the report.
        display_path = f"EXTERNAL_MEDIA/{index}-{path.name}"
        candidates.append(_media_record(path, display_path, "external_input"))

    for item in candidates:
        for kind, expected_hash in expected_hashes.items():
            if expected_hash and item["sha256"].lower() == str(expected_hash).lower():
                matched[kind].append(item["path"])

    consent = config.get("consent", {})
    photo_state = "HASH_MATCH_FOUND — AUTHORISATION STILL REQUIRES HUMAN CONFIRMATION" if matched["photo"] else "BLOCKED — SOURCE PHOTO HASH NOT FOUND"
    audio_state = "HASH_MATCH_FOUND — AUTHORISATION STILL REQUIRES HUMAN CONFIRMATION" if matched["audio"] else "BLOCKED — SOURCE AUDIO HASH NOT FOUND"
    return {
        "schema_version": 1,
        "status": "INVENTORY_ONLY_NOT_PRODUCTION_VERIFICATION",
        "consent_status_from_config": consent.get("status", "UNSPECIFIED"),
        "provider_connection": consent.get("provider_connection", "UNSPECIFIED"),
        "photo": {"expected_sha256": expected_hashes["photo"], "matching_paths": matched["photo"], "state": photo_state},
        "audio": {"expected_sha256": expected_hashes["audio"], "matching_paths": matched["audio"], "state": audio_state},
        "candidate_media_count": len(candidates),
        "candidate_media": sorted(candidates, key=lambda x: x["path"]),
        "limitations": [
            "A filename, file hash, or matching hash does not establish ownership, consent, or provider authorisation.",
            "An MP4 container hash is not the same as the hash of its embedded audio track; extract and authorise a source audio file separately if needed.",
            "External media are read-only inputs; their bytes are not copied into the repository or uploaded.",
            "No provider API, avatar, voice clone, lip-sync, or live presentation is tested.",
            "No media file is modified, uploaded, or published by this audit."
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--external-media", type=Path, action="append", default=[],
        help="Optional local media file outside the repository to hash as an untrusted candidate. Repeat for multiple files."
    )
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        report = audit(root, args.external_media)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "AUDIT_ERROR", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
