#!/usr/bin/env python3
"""Free-first JSON integrity and small JSON-Schema validator.

With one or more JSON paths, validates JSON syntax/root shape.
With exactly two arguments where the second is a schema file, also validates
the first document against the schema's common structural keywords.
"""
import json
import sys
from pathlib import Path


def validate_json(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, (dict, list)):
        raise ValueError(f"{path}: root must be an object or array")
    return data


def check_schema(data, schema, path="$"):
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(data, dict):
            raise ValueError(f"{path}: expected object")
        for key in schema.get("required", []):
            if key not in data:
                raise ValueError(f"{path}: missing required property {key!r}")
        props = schema.get("properties", {})
        for key, value in data.items():
            if key in props:
                check_schema(value, props[key], f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                raise ValueError(f"{path}: unexpected property {key!r}")
    elif expected == "array":
        if not isinstance(data, list):
            raise ValueError(f"{path}: expected array")
        item_schema = schema.get("items")
        if item_schema:
            for i, item in enumerate(data):
                check_schema(item, item_schema, f"{path}[{i}]")
    elif expected == "string" and not isinstance(data, str):
        raise ValueError(f"{path}: expected string")
    elif expected == "integer" and (not isinstance(data, int) or isinstance(data, bool)):
        raise ValueError(f"{path}: expected integer")
    elif expected == "number" and (not isinstance(data, (int, float)) or isinstance(data, bool)):
        raise ValueError(f"{path}: expected number")
    elif expected == "boolean" and not isinstance(data, bool):
        raise ValueError(f"{path}: expected boolean")

    if "minimum" in schema and isinstance(data, (int, float)) and data < schema["minimum"]:
        raise ValueError(f"{path}: below minimum {schema['minimum']}")


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print("No JSON files supplied.")
        return 0

    if len(paths) == 2 and paths[1].name.endswith(".schema.json"):
        data = validate_json(paths[0])
        schema = validate_json(paths[1])
        check_schema(data, schema)
        print(f"PASS {paths[0]} against {paths[1]}")
        return 0

    for path in paths:
        validate_json(path)
        print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
