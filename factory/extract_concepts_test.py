from extract_concepts import extract
rows=[{"id":"unit:content:docs/research/paper.md","source_path":"docs/research/paper.md","content_hash":"a"*64,"source_type":"research"}]
out=extract(rows); labels={x["label"] for x in out}
assert "research" in labels and "paper" in labels
assert all(x["status"]=="CANDIDATE" for x in out)
assert all(x["provenance"]["content_hash"]=="a"*64 for x in out)
print("CONCEPT EXTRACTION REGRESSION: PASS")
