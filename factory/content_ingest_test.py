#!/usr/bin/env python3
"""Regression tests for deterministic content discovery."""
import hashlib
import tempfile
from pathlib import Path
from factory.content_ingest import discover

def main():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "README.md").write_text("निष्पक्ष समझ ꙰\n", encoding="utf-8")
        (root / "generated").mkdir()
        (root / "generated" / "ignored.json").write_text("ignored", encoding="utf-8")
        (root / ".git").mkdir()
        (root / ".git" / "ignored.txt").write_text("ignored", encoding="utf-8")
        expected = hashlib.sha256("निष्पक्ष समझ ꙰\n".encode("utf-8")).hexdigest()

        first = discover(root)
        second = discover(root)
        assert [{k:v for k,v in x.items() if k != "provenance"} for x in first] == [{k:v for k,v in x.items() if k != "provenance"} for x in second]
        assert len(first) == 1
        assert first[0]["source_path"] == "README.md"
        assert first[0]["content_hash"] == expected
        assert first[0]["content_status"] == "AVAILABLE"

    print("CONTENT INGEST TEST: PASS")

if __name__ == "__main__":
    main()
