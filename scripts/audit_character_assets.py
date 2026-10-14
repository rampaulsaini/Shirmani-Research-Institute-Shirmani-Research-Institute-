#!/usr/bin/env python3
"""Audit whether authorized photo/audio SHA-256 values match local source assets.

This is a local repository audit, not proof of consent, provider upload, or
avatar/lip-sync integration. Missing matches are reported as NOT VERIFIED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Iterable

ASSET_TYPES = {
    "photo": {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"},
    "audio": {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"},
}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".next", "dist", "build"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_candidates(root: Path, extensions: set[str]) -> Iterable[Path]:
    """Yield supported media files without traversing generated/dependency dirs."""
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            path = Path(current) / name
            if path.suffix.lower() in extensions and not path.is_symlink() and path.is_file() and path.stat().st_size > 0:
                yield path


def find_hash_matches(root: Path, expected_hash: str, kind: str) -> list[str]:
    """Return relative paths whose file hash exactly matches the configured hash."""
    if kind not in ASSET_TYPES:
        raise ValueError(f"Unsupported asset kind: {kind}")
    if not isinstance(expected_hash, str) or len(expected_hash) != 64:
        raise ValueError(f"Configured {kind} SHA-256 must be a 64-character hex string")
    try:
        int(expected_hash, 16)
    except ValueError as exc:
        raise ValueError(f"Configured {kind} SHA-256 is not hexadecimal") from exc

    matches = []
    for path in iter_candidates(root, ASSET_TYPES[kind]):
        try:
            if sha256_file(path).lower() == expected_hash.lower():
                matches.append(path.relative_to(root).as_posix())
        except (OSError, PermissionError):
            # An unreadable candidate cannot count as a match.
            continue
    return matches


def audit(config_path: Path, root: Path) -> dict:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    assets = config.get("source_assets")
    if not isinstance(assets, dict):
        raise ValueError("Config must contain a source_assets object")

    report = {
        "schema_version": 1,
        "scope": "local file hash matching only",
        "provider_integration": "NOT VERIFIED",
        "consent": config.get("consent", {}).get("status", "NOT VERIFIED"),
        "assets": {},
    }
    for kind, key in (("photo", "photo_sha256"), ("audio", "audio_sha256")):
        expected = assets.get(key)
        if not expected:
            report["assets"][kind] = {
                "status": "NOT VERIFIED",
                "reason": f"Missing {key} in configuration",
                "matches": [],
            }
            continue
        matches = find_hash_matches(root, expected, kind)
        report["assets"][kind] = {
            "status": "HASH MATCH" if matches else "NOT VERIFIED",
            "expected_sha256": expected,
            "matches": matches,
            "reason": "Exact SHA-256 match found" if matches else
                      "No supported local source file matched the configured SHA-256",
        }
    report["overall_status"] = (
        "HASH MATCH" if all(v["status"] == "HASH MATCH" for v in report["assets"].values())
        else "NOT VERIFIED"
    )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(),
                        help="Repository root to scan (default: current directory)")
    parser.add_argument("--config", type=Path,
                        default=Path("config/authorized-voice-integration.json"),
                        help="Config path, relative to --root unless absolute")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 when either original asset is not hash-matched")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    config_path = args.config if args.config.is_absolute() else root / args.config
    try:
        report = audit(config_path, root)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"overall_status": "AUDIT ERROR", "error": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if args.strict and report["overall_status"] != "HASH MATCH" else 0


if __name__ == "__main__":
    sys.exit(main())
