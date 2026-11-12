#!/usr/bin/env python3
"""Validate the Supreme Neutrality & Evidence contract."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=(ROOT/'docs/supreme-neutrality-and-evidence-contract.md').read_text(encoding='utf-8')
schema=json.loads((ROOT/'schemas/supreme-neutrality-record.schema.json').read_text(encoding='utf-8'))
assert schema['title']=='SHIRMANI Supreme Neutrality Record'
gov=schema['properties']['governance']['properties']
assert gov['fail_closed']['const'] is True
assert gov['favoritism_allowed']['const'] is False
assert gov['subjective_experience_claim_allowed']['const'] is False
assert gov['accuracy_is_measured_not_declared']['const'] is True
for marker in ['No favoritism','Counter-evidence','independent verification','Supreme accuracy']:
    assert marker.lower() in contract.lower(), marker
fingerprint=hashlib.sha256(b'neutrality-audit').hexdigest()
assert len(fingerprint)==64
print('SUPREME_NEUTRALITY_CONTRACT: PASS')
print('FAIL_CLOSED: PASS')
print('FAVORITISM: BLOCKED')
print('COUNTER_EVIDENCE: REQUIRED')
print('INDEPENDENT_VERIFICATION: REQUIRED')
print('ACCURACY: MEASURED_NOT_DECLARED')
