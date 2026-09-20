#!/usr/bin/env python3
"""Minimal JSON integrity validator using only the Python standard library.

Schema-level validation is intentionally conservative here; CI can add a JSON
Schema validator later without making the free-first pipeline depend on it.
"""

import json
import sys
from pathlib import Path


def validate(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, (dict, list)):
        raise ValueError(f"{path}: root must be an object or array")


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print("No JSON files supplied.")
        return 0
    for path in paths:
        validate(path)
        print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
