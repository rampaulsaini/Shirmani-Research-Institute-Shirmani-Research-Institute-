"""Corpus normalization and deduplication."""
import re,hashlib
def normalize(t):
    t=re.sub(r'<script[\\s\\S]*?</script>',' ',t,flags=re.I); t=re.sub(r'<style[\\s\\S]*?</style>',' ',t,flags=re.I); t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'https?://\\S+',' ',t); return re.sub(r'\\s+',' ',t).strip()
def units(t): return [x.strip(' -•#*_') for x in re.split(r'(?<=[.!?।॥])\\s+',normalize(t)) if 20<=len(x)<=800]
def dedupe(items):
    seen=set(); out=[]
    for x in items:
        h=hashlib.sha256(x.encode()).hexdigest()
        if h not in seen: seen.add(h); out.append((h,x))
    return out
