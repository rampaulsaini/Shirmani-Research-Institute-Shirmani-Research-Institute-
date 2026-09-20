#!/usr/bin/env python3
"""Build a deterministic manifest of tracked source files without rewriting source content."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
OUT.mkdir(parents=True, exist_ok=True)

def git(args):
    p = subprocess.run(["git", *args], cwd=ROOT, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout

def main():
    stamp = datetime.now(timezone.utc).isoformat()
    commit = git(["rev-parse", "HEAD"]).strip()
    branch = git(["branch", "--show-current"]).strip() or None
    files = []
    for raw in git(["ls-files", "-z"]).split("\0"):
        if not raw:
            continue
        path = ROOT / raw
        if not path.is_file():
            continue
        data = path.read_bytes()
        files.append({
            "path": raw,
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data),
        })
    files.sort(key=lambda x: x["path"])
    manifest = {
        "manifest_version": "1.0",
        "generated_at": stamp,
        "repository_commit": commit,
        "branch": branch,
        "source_count": len(files),
        "integrity": "sha256",
        "scope": "git-tracked repository files",
        "files": files,
    }
    payload = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    (OUT / "deterministic-source-manifest.json").write_text(payload, encoding="utf-8")
    print(f"Deterministic source manifest: {len(files)} files")

if __name__ == "__main__":
    main()
