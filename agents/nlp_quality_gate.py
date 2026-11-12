"""Lightweight multilingual NLP quality gate; not a truth detector."""
from __future__ import annotations
import re
from collections import Counter
from hashlib import sha256
TOKEN_RE=re.compile(r"[\w\u0900-\u097F\u0A00-\u0A7F]+",re.UNICODE)
def inspect(text,*,source_id=None):
    value=" ".join(str(text).split()); tokens=TOKEN_RE.findall(value)
    counts=Counter(t.casefold() for t in tokens)
    ratio=max(counts.values(),default=0)/max(len(tokens),1)
    flags=[]
    if len(tokens)<5: flags.append("too_short")
    if ratio>=0.40 and len(tokens)>=10: flags.append("high_repetition")
    if not source_id: flags.append("missing_source")
    if "\ufffd" in value: flags.append("replacement_character")
    return {"schema":"nlp-quality/v1","text_sha256":sha256(value.encode()).hexdigest(),
            "token_count":len(tokens),"unique_token_count":len(counts),
            "repetition_ratio":round(ratio,6),"flags":flags,
            "quality":"PASS" if not flags else "HOLD"}
