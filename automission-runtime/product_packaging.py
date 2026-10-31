import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_FIELDS = ("title", "product_type", "description", "version")

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def build_manifest(spec, files=(), version="1.0.0"):
    missing = [key for key in REQUIRED_FIELDS if not spec.get(key)]
    if missing:
        raise ValueError("missing manifest fields: " + ",".join(missing))
    normalized_files = sorted({str(path) for path in files if str(path).strip()})
    manifest = {
        "title": spec["title"],
        "product_type": spec["product_type"],
        "description": spec["description"],
        "version": version,
        "files": normalized_files,
        "created_at": utc_now(),
    }
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    manifest["manifest_hash"] = hashlib.sha256(canonical.encode()).hexdigest()
    return manifest

def write_manifest(manifest, output: Path):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return output
