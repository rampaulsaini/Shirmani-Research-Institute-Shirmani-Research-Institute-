#!/usr/bin/env python3
import json,re,subprocess,hashlib,os,sys,shutil
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/"factory/repos.json").read_text(encoding="utf-8"))
WORK=ROOT/"factory/_sources"; OUT=ROOT/"generated"
WORK.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)

TEXT_EXT={".md",".txt",".html",".htm",".json",".yml",".yaml"}

def run(c,cwd=None):
    p=subprocess.run(c,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=False)
    return p.returncode,p.stdout

def classify_source(path, text):
    p=path.lower()
    if ".github/workflows/" in p or p.endswith(".yml") or p.endswith(".yaml"):
        return "workflow"
    if "research" in p or "paper" in p:
        return "research"
    if any(x in p for x in ("manifest","philosophy","truth","yatharth","nishpaksh")):
        return "philosophy"
    if p.endswith((".html",".htm")):
        return "documentation"
    if p.endswith(".json"):
        return "media-metadata" if any(x in p for x in ("media","audio","image","video","asset")) else "documentation"
    if any(x in p for x in ("src/","script","code","main.py","app.py")):
        return "code"
    return "documentation"

def source_type_enum(kind):
    return {
        "research": "PAPER",
        "philosophy": "OTHER",
        "workflow": "OTHER",
        "documentation": "OTHER",
        "media-metadata": "OTHER",
        "code": "REPOSITORY",
    }.get(kind, "OTHER")


def source_record(repository, branch, path, raw_text, normalized_text, source_kind, recorded_at):
    identity=f"{repository}:{path}"
    source_id="SRC-"+hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    return {
        "source_id": source_id,
        "source_repository": repository,
        "source_path_or_url": path,
        "source_type": source_type_enum(source_kind),
        "source_status": "ORIGINAL",
        "title_or_label": Path(path).name,
        "content_hash": hashlib.sha256(raw_text.encode("utf-8")).hexdigest(),
        "normalized_content_hash": hashlib.sha256(normalized_text.encode("utf-8")).hexdigest(),
        "recorded_at": recorded_at,
        "version": branch or "UNKNOWN",
        "attribution": repository,
        "parent_source_id": None,
        "notes": "Inventory record emitted by the source-first factory; no source wording is rewritten by this record."
    }


def clone_sources():
    result=[]
    token=os.environ.get("FACTORY_GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    for full in CFG["repositories"]:
        if full == CFG.get("hub_repository"):
            result.append({"repository":full,"available":True,"skipped":"hub repository"})
            continue
        owner,name=full.split("/",1); dest=WORK/name
        expected=full.lower(); contaminated=False
        if dest.exists() and (dest/".git").exists():
            _,remote=run(["git","-C",str(dest),"remote","get-url","origin"])
            if expected not in remote.lower():
                contaminated=True; shutil.rmtree(dest,ignore_errors=True)
        elif dest.exists():
            shutil.rmtree(dest,ignore_errors=True)
        auth_url=f"https://x-access-token:{token}@github.com/{full}.git" if token else f"https://github.com/{full}.git"
        code=1; log=""
        if not dest.exists():
            code,log=run(["git","clone","--depth","1",auth_url,str(dest)])
            if code != 0 and token:
                shutil.rmtree(dest,ignore_errors=True)
                code,log=run(["git","-c","credential.helper=","clone","--depth","1",f"https://github.com/{full}.git",str(dest)])
        else:
            code,log=run(["git","-c","credential.helper=","-C",str(dest),"fetch","--depth","1","origin"])
            if code==0:
                code,log=run(["git","-C",str(dest),"reset","--hard","origin/HEAD"])
            elif token:
                shutil.rmtree(dest,ignore_errors=True)
                code,log=run(["git","clone","--depth","1",f"https://github.com/{full}.git",str(dest)])
        available=False; head=None; remote=""; branch=None
        if dest.exists():
            probe_code,probe=run(["git","-C",str(dest),"rev-parse","--is-inside-work-tree"])
            _,remote=run(["git","-C",str(dest),"remote","get-url","origin"])
            _,branch_out=run(["git","-C",str(dest),"symbolic-ref","--short","refs/remotes/origin/HEAD"])
            branch=branch_out.strip().removeprefix("origin/") or None
            if code==0 and probe_code==0 and probe.strip()=="true" and expected in remote.lower():
                available=True
                _,head=run(["git","-C",str(dest),"rev-parse","HEAD"]); head=head.strip()
        result.append({"repository":full,"available":available,"head_sha":head,
                       "default_branch":branch,"git_returncode":code,"remote_ok":expected in remote.lower(),
                       "contaminated_source_removed":contaminated,"authenticated_clone":bool(token),
                       "diagnostic":log[-800:] if code!=0 or not available else ""})
    return result

def collect(source_meta):
    by_name={x["repository"].split("/",1)[1]:x for x in source_meta if x.get("available")}
    out=[]; inventory=[]; stamp=datetime.now(timezone.utc).isoformat()
    for p in WORK.rglob("*"):
        if ".git" in p.parts: continue
        if p.is_file() and p.suffix.lower() in TEXT_EXT:
            repo_dir=p.relative_to(WORK).parts[0]; meta=by_name.get(repo_dir,{})
            raw=p.read_text(encoding="utf-8",errors="ignore")
            s=re.sub(r"<script[\s\S]*?</script>"," ",raw,flags=re.I); s=re.sub(r"<style[\s\S]*?</style>"," ",s,flags=re.I)
            s=re.sub(r"<[^>]+>"," ",s); s=re.sub(r"https?://\S+"," ",s); s=re.sub(r"\s+"," ",s).strip()
            if len(s)>80:
                rel=str(p.relative_to(WORK/repo_dir)); kind=classify_source(rel,s)
                out.append({"repository":meta.get("repository",repo_dir),"branch":meta.get("default_branch"),
                            "path":rel,"text":s[:12000],"source_type":kind,
                            "raw_content_hash":hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                            "collected_at":stamp})
                inventory.append(source_record(meta.get("repository",repo_dir),meta.get("default_branch"),
                                                rel,raw,s,kind,stamp))
    return out, inventory

def units(items):
    u=[]
    for item in items:
        for x in re.split(r"(?<=[.!?।॥])\s+",item["text"]):
            x=x.strip(" -•#*_")
            if 20<=len(x)<=500:
                row=dict(item); row["text"]=x; row["source_hash"]=hashlib.sha256(x.encode("utf-8")).hexdigest(); u.append(row)
    return u

def framework_policy():
    path = ROOT / "factory" / "shirmani-framework.json"
    return json.loads(path.read_text(encoding="utf-8"))

def generated_claim_meta(text, source_id):
    framework = framework_policy()
    lower = text.lower()
    if any(x in lower for x in ("सर्वश्रेष्ठ", "यथार्थ युग", "शिरोमणि", "संपूर्ण संतुष्टि", "हृदय दृष्टिकोण")):
        claim_class = "user_philosophy"
    elif any(x in lower for x in ("सिद्ध", "प्रमाण", "वैज्ञानिक", "science", "empirical")):
        claim_class = "unverified_claim"
    else:
        claim_class = "creative_expression"
    return {"framework_id": framework["framework_id"], "framework_version": framework.get("version"),
            "claim_classes": framework.get("claim_classes", []), "method_stack": framework.get("method_stack", []),
            "claim_class": claim_class,
            "method_trace": ["source_provenance", "textual_context", "cross-source-comparison", "independent_verification"],
            "source_ids": [str(source_id)], "evidence_status": "requires_independent_verification",
            "human_review_required": True}

def main():
    stamp=datetime.now(timezone.utc).isoformat(); sources=clone_sources(); collected, inventory=collect(sources); u=units(collected); t=CFG["product_targets"]
    manifest={"generated_at":stamp,"sources":sources,"targets":t,"units":len(u),"architecture":"source-first; generated products never become canonical inputs"}
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    with (OUT/"source-records.jsonl").open("w",encoding="utf-8") as f:
        for record in inventory:
            f.write(json.dumps(record,ensure_ascii=False) + "\n")

    with (OUT/"source-units.jsonl").open("w",encoding="utf-8") as f:
        for i,item in enumerate(u,1):
            row={"id":i,"repository":item["repository"],"branch":item["branch"],"path":item["path"],"source_hash":item["source_hash"],"raw_content_hash":item.get("raw_content_hash"),"text":item["text"],"source_type":item["source_type"],"collected_at":item["collected_at"]}
            f.write(json.dumps(row,ensure_ascii=False)+"\n")
    if "--bootstrap-only" in sys.argv: return
    if not u: raise RuntimeError("No usable source units found; source isolation/authentication must be fixed before generation.")
    verses=int(t["verses"]); books=int(t["digital_books"]); papers=int(t["research_papers"])
    with (OUT/"verse-corpus.jsonl").open("w",encoding="utf-8") as f:
        for i in range(1,verses+1):
            item=u[(i-1)%len(u)]
            source_id=((i-1)%len(u))+1
            text=f"सूत्र {i:06d}: {item['text']} — यह स्रोत-आधारित चिंतन-प्रारूप है; सत्यापन हेतु स्वतंत्र निरीक्षण आवश्यक है।"
            meta=generated_claim_meta(text, source_id)
            record={"id":i,"agent":"verse","source":item["repository"],"source_ids":meta["source_ids"],
                    "content_hash":hashlib.sha256(text.encode("utf-8")).hexdigest(),"status":"draft","text":text,
                    "framework":{"framework_id":meta["framework_id"],"framework_version":meta["framework_version"],
                                 "claim_classes":meta["claim_classes"],"method_stack":meta["method_stack"]},
                    "claim_class":meta["claim_class"],"method_trace":meta["method_trace"],
                    "evidence_status":meta["evidence_status"],"human_review_required":meta["human_review_required"]}
            f.write(json.dumps(record,ensure_ascii=False)+"\n")
    per=max(1,verses//books)
    for b in range(1,books+1):
        start=(b-1)*per+1; end=min(b*per,verses); lines=[f"# डिजिटल महाग्रंथ {b:03d}","","स्वचालित स्रोत-संग्रहण से बना शोध-प्रारूप; इसे वैज्ञानिक/ऐतिहासिक प्रमाणित निष्कर्ष न माना जाए।",""]
        for n in range(start,end+1):
            item=u[(n-1)%len(u)]; lines += [f"## {n:06d}",item["text"],f"स्रोत: {item['repository']}:{item['path']} · स्वतंत्र परीक्षण अपेक्षित।",""]
        (OUT/f"book-{b:03d}.md").write_text("\n".join(lines),encoding="utf-8")
    for p in range(1,papers+1):
        item=u[(p-1)%len(u)]
        (OUT/f"research-paper-draft-{p:03d}.md").write_text(f"# Research Paper Draft {p:03d}\n\n## Abstract\nयह स्वचालित प्रारूप उपलब्ध स्रोत-सामग्री को व्यवस्थित करता है।\n\n## Research question\n{item['text']}\n\n## Method\nस्रोत-संग्रह, पाठ-सफाई, वाक्य-खंडन और स्रोत-ट्रेसिंग।\n\n## Status\nDraft generated automatically. स्वतंत्र peer review, empirical testing और source verification आवश्यक हैं।\n\n## Source\n{item['repository']}:{item['path']}\n",encoding="utf-8")
    cert=OUT/"certificates"; cert.mkdir(exist_ok=True)
    for i in range(1,int(t["certificates"])+1):
        (cert/f"certificate-{i:04d}.md").write_text(f"# Digital Research Certificate {i:04d}\n\nयह archival/participation record है; academic, governmental, professional या scientific accreditation नहीं।\n\nGenerated: {stamp}\n",encoding="utf-8")
    (OUT/"CATALOG.md").write_text("# Omniverse Research Factory\n\n100 digital book drafts · 100,000 traceable verse records · 100 research-paper drafts · 1,000 archival certificates.\n\nAll generated research is draft material and requires independent verification.\n",encoding="utf-8")

if __name__=="__main__": main()
