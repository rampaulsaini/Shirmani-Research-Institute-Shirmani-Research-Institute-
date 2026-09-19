"""Quality control agent."""
from pathlib import Path
def run(root):
    errors=[]
    for p in Path(root).rglob('*'):
        if p.is_file() and not p.read_text(encoding='utf-8',errors='ignore').strip(): errors.append('empty:'+str(p))
    return {'ok':not errors,'errors':errors}
