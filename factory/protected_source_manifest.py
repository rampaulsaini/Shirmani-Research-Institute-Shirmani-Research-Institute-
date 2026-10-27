#!/usr/bin/env python3
"""Build a deterministic manifest of explicitly captured protected user sources."""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "protected" / "user-source"
OUT = ROOT / "generated" / "protected-user-source-manifest.json"

TEXT_SUFFIXES = {".md",".txt",".html",".htm",".json",".yaml",".yml",".csv",".xml",".srt",".vtt"}

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def source_id(rel_path, digest):
    return "user-source-" + hashlib.sha256((rel_path + ":" + digest).encode("utf-8")).hexdigest()[:24]

def read_language(path):
    meta = path.with_suffix(path.suffix + ".meta.json")
    if not meta.is_file():
        return "unspecified"
    try:
        value = json.loads(meta.read_text(encoding="utf-8")).get("language")
        return value.strip() if isinstance(value, str) and value.strip() else "unspecified"
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return "unspecified"

def main():
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    records = []
    for path in sorted(SOURCE_ROOT.rglob("*")):
        if not path.is_file() or path.name.endswith(".meta.json") or path.name == "README.md":
            continue
        data = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        digest = sha256_bytes(data)
        records.append({
            "source_id": source_id(rel, digest),
            "source_type": "USER_ORIGINAL_TEXT" if path.suffix.lower() in TEXT_SUFFIXES else "OTHER_USER_SOURCE",
            "language": read_language(path),
            "path": rel,
            "content_sha256": digest,
            "byte_length": len(data),
            "preservation": {
                "verbatim": True,
                "derivative_of": None,
                "transformations_allowed": False
            }
        })

    payload = {
        "manifest_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": SOURCE_ROOT.relative_to(ROOT).as_posix(),
        "record_count": len(records),
        "records": records,
        "integrity": {
            "source_bytes_modified": False,
            "historical_missing_material_reconstructed": False,
            "derivatives_included_as_original": False
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"record_count": len(records), "output": OUT.relative_to(ROOT).as_posix()}, ensure_ascii=False))

if __name__ == "__main__":
    main()
