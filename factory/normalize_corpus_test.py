#!/usr/bin/env python3
"""Regression test for deterministic corpus-unit normalization."""
from normalize_corpus import normalize

rows=[
 {"id":"content:a.md","source_path":"a.md","content_hash":"a"*64,"content_status":"AVAILABLE","language_hint":"markdown"},
 {"id":"content:b.png","source_path":"b.png","content_hash":"b"*64,"content_status":"BINARY_SKIPPED","language_hint":None},
 {"id":"content:c.txt","source_path":"c.txt","content_hash":"c"*64,"content_status":"UNAVAILABLE","language_hint":"text"}
]
units=normalize(rows)
assert [x["id"] for x in units]==["unit:content:a.md","unit:content:b.png","unit:content:c.txt"]
assert units[0]["status"]=="READY_FOR_ANALYSIS"
assert units[1]["unit_type"]=="BINARY_REFERENCE"
assert units[2]["status"]=="UNAVAILABLE"
assert units[0]["content_hash"]=="a"*64
print("CORPUS NORMALIZATION REGRESSION: PASS")
