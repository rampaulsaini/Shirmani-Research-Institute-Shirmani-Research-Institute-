#!/usr/bin/env python3
import json,re,subprocess,hashlib,os,sys
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"factory/repos.json").read_text(encoding="utf-8"))
WORK=ROOT/"factory/_sources"; OUT=ROOT/"generated"; STATE=ROOT/"factory/state.json"
WORK.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
def run(c,cwd=None):
    p=subprocess.run(c,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=False)
    return p.returncode,p.stdout
def clone_sources():
    result=[]
    for full in CFG["repositories"]:
        if full == CFG.get("hub_repository"):
            result.append({"repository":full,"available":True,"skipped":"hub repository"})
            continue
        owner,name=full.split("/",1); dest=WORK/name
        if dest.exists():
            code,log=run(["git","-C",str(dest),"fetch","--depth","1","origin"])
            probe,_=run(["git","-C",str(dest),"rev-parse","--is-inside-work-tree"])
            available=(code==0 and probe==0)
        else:
            code,log=run(["git","clone","--depth","1",f"https://github.com/{full}.git",str(dest)])
            probe,_=run(["git","-C",str(dest),"rev-parse","--is-inside-work-tree"]) if dest.exists() else (1,"")
            available=(code==0 and probe==0)
        result.append({
            "repository":full,
            "available":available,
            "head_sha": (run(["git","-C",str(dest),"rev-parse","HEAD"])[1].strip() if available else None),
            "git_returncode":code,
            "diagnostic":log[-500:] if code != 0 else ""
        })
    return result
def collect():
    out=[]
    for p in WORK.rglob("*"):
        if ".git" in p.parts: continue
        if p.is_file() and p.suffix.lower() in {".md",".txt",".html",".htm",".json",".yml",".yaml"}:
            s=p.read_text(encoding="utf-8",errors="ignore")
            s=re.sub(r"<script[\s\S]*?</script>"," ",s,flags=re.I); s=re.sub(r"<style[\s\S]*?</style>"," ",s,flags=re.I)
            s=re.sub(r"<[^>]+>"," ",s); s=re.sub(r"https?://\S+"," ",s); s=re.sub(r"\s+"," ",s).strip()
            if len(s)>80: out.append((str(p.relative_to(WORK)),s[:12000]))
    return out
def units(items):
    u=[]
    for src,s in items:
        for x in re.split(r"(?<=[.!?।॥])\s+",s):
            x=x.strip(" -•#*_")
            if 20<=len(x)<=500: u.append((src,x))
    return u
def main():
    stamp = datetime.now(timezone.utc).isoformat()
    sources = clone_sources()
    u = units(collect())
    t = CFG["product_targets"]
    manifest = {
        "generated_at": stamp,
        "sources": sources,
        "targets": t,
        "units": len(u),
        "input_policy": "source-units.jsonl is the canonical input; generated products must not become source inputs"
    }
    (OUT/"manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    with (OUT/"source-units.jsonl").open("w", encoding="utf-8") as f:
        for i, (src, text) in enumerate(u, 1):
            record = {
                "id": i,
                "source": src,
                "text": text,
                "hash": hashlib.sha256(text.encode("utf-8")).hexdigest()
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    if "--bootstrap-only" in sys.argv:
        return
    verses=int(t["verses"]); books=int(t["digital_books"]); papers=int(t["research_papers"])
    if not u:
        raise RuntimeError("No usable source units found; refusing to generate fabricated products.")
    with (OUT/"verse-corpus.jsonl").open("w",encoding="utf-8") as f:
        for i in range(1,verses+1):
            src,base=u[(i-1)%len(u)]; h=hashlib.sha256(f"{i}|{src}|{base}".encode()).hexdigest()[:12]
            text=f"सूत्र {i:06d}: {base} — यह स्रोत-आधारित चिंतन-प्रारूप है; सत्यापन हेतु स्वतंत्र निरीक्षण आवश्यक है।"
            f.write(json.dumps({"id":i,"hash":h,"source":src,"text":text},ensure_ascii=False)+"\n")
    per=verses//books
    for b in range(1,books+1):
        start=(b-1)*per+1; end=b*per; lines=[f"# डिजिटल महाग्रंथ {b:03d}","","स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।",""]
        for n in range(start,end+1):
            src,base=u[(n-1)%len(u)]; lines += [f"## {n:06d}",base,f"स्रोत: {src} · स्वतंत्र परीक्षण अपेक्षित।",""]
        (OUT/f"book-{b:03d}.md").write_text("\n".join(lines),encoding="utf-8")
    for p in range(1,papers+1):
        src,base=u[(p-1)%len(u)]
        (OUT/f"research-paper-draft-{p:03d}.md").write_text(f"# Research Paper Draft {p:03d}\n\n## Abstract\nयह स्वचालित प्रारूप निष्पक्ष समझ, शमीकरण यथार्थ सिद्धांत, हृदय-दृष्टिकोण, मस्तक-दृष्टिकोण, प्रकृति और आत्म-अवलोकन से संबंधित उपलब्ध स्रोत-सामग्री को व्यवस्थित करता है।\n\n## Research question\n{base}\n\n## Method\nसार्वजनिक repository सामग्री का संग्रह, पाठ-सफाई, वाक्य-खंडन और स्रोत-ट्रेसिंग।\n\n## Status\nDraft generated automatically. स्वतंत्र peer review, empirical testing और source verification आवश्यक हैं।\n\n## Source\n{src}\n",encoding="utf-8")
    cert=OUT/"certificates"; cert.mkdir(exist_ok=True)
    for i in range(1,int(t["certificates"])+1):
        (cert/f"certificate-{i:04d}.md").write_text(f"# Digital Research Certificate {i:04d}\n\nयह archival/participation record है; academic, governmental, professional या scientific accreditation नहीं।\n\nGenerated: {stamp}\n",encoding="utf-8")
    (OUT/"CATALOG.md").write_text("# Omniverse Research Factory\n\n100 digital book drafts · 100,000 traceable verse records · 100 research-paper drafts · 1,000 archival certificates.\n\nAll generated research is draft material and requires independent verification.\n",encoding="utf-8")
if __name__=="__main__": main()
