#!/usr/bin/env python3
"""Fail-closed recovery for the canonical SHIRMANI product catalog."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

_SAFE_PRODUCT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def load_rows(path: Path) -> list[dict[str, Any]]:
    """Return product rows from a JSON catalog, or [] when it is absent/invalid."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(data, dict):
        return []
    rows = data.get("products", [])
    return rows if isinstance(rows, list) else []


def validate_rows(rows: list[Any], source: str) -> None:
    """Reject malformed rows and unsafe/colliding stable IDs before production."""
    ids: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{source} contains a non-object product row; refusing production.")
        product_id = str(row.get("id", "")).strip()
        if not product_id:
            raise ValueError(f"{source} contains a row without a stable product ID; refusing production.")
        if not _SAFE_PRODUCT_ID.fullmatch(product_id):
            raise ValueError(f"{source} contains an unsafe product ID {product_id!r}; refusing production.")
        ids.append(product_id)
    normalized_ids = [product_id.casefold() for product_id in ids]
    if len(normalized_ids) != len(set(normalized_ids)):
        raise ValueError(f"{source} contains duplicate or case-colliding product IDs; refusing production.")


def ensure_catalog(catalog_path: Path, registry_path: Path) -> dict[str, Any]:
    """Preserve a valid catalog byte-for-byte; recover only an empty/invalid one."""
    rows = load_rows(catalog_path)
    if rows:
        validate_rows(rows, str(catalog_path))
        return {"action": "kept-existing", "product_count": len(rows)}

    registry_rows = load_rows(registry_path)
    if not registry_rows:
        raise ValueError(
            f"Canonical catalog is empty and {registry_path} is missing, invalid, or empty; "
            "refusing to produce a misleading batch."
        )
    validate_rows(registry_rows, str(registry_path))
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(
        json.dumps({"schema_version": 2, "products": registry_rows}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {"action": "restored-from-registry", "product_count": len(registry_rows)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--registry", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = ensure_catalog(args.catalog, args.registry)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
