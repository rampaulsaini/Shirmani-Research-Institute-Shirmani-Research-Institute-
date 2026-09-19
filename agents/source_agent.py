"""Source inventory agent."""
from pathlib import Path
import hashlib
EXT={'.md','.txt','.html','.htm','.json','.yml','.yaml','.py','.js','.ts','.css'}
def scan(root,repo):
    out=[]
    for p in Path(root).rglob('*'):
        if p.is_file() and p.suffix.lower() in EXT:
            t=p.read_text(encoding='utf-8',errors='ignore')
            out.append({'repository':repo,'path':str(p.relative_to(root)),'sha256':hashlib.sha256(t.encode()).hexdigest(),'chars':len(t)})
    return out
