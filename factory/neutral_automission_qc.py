import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHARTER = ROOT / 'docs' / 'yatharth-governance' / 'neutral-automission-charter.md'
GOV = ROOT / 'schemas' / 'agent-governance.json'

REQUIRED = [
    'Source separation', 'No automatic endorsement', 'Counter-evidence search',
    'Symmetric testability', 'Uncertainty preservation', 'Evidence-weighted output',
    'No persuasion objective', 'Fail closed', 'measured signal', 'model inference',
    'independent verification', 'Human Gate',
]

def main():
    text = CHARTER.read_text(encoding='utf-8')
    missing = [term for term in REQUIRED if term.lower() not in text.lower()]
    if missing:
        raise SystemExit('Neutral Automission charter missing: ' + ', '.join(missing))
    gov = json.loads(GOV.read_text(encoding='utf-8'))
    checks = {
        'fail_closed': gov.get('fail_closed') is True,
        'provenance_required_for_claims': gov.get('provenance_required_for_claims') is True,
        'fabrication_prohibited': gov.get('fabrication_prohibited') is True,
    }
    failed = [k for k, ok in checks.items() if not ok]
    if failed:
        raise SystemExit('Governance baseline failed: ' + ', '.join(failed))
    forbidden_patterns = ['automatically proven', 'guaranteed truth', '100% accurate', 'always correct']
    lowered = text.lower()
    found = [p for p in forbidden_patterns if p in lowered]
    if found:
        raise SystemExit('Unsupported certainty language detected: ' + ', '.join(found))
    print('SHIRMANI Neutral Automission Governance: PASS')
    print('Fail-closed + provenance + counter-evidence + uncertainty gates present.')

if __name__ == '__main__':
    main()