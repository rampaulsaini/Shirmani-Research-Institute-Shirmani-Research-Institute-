#!/usr/bin/env python3
"""Read-only heuristic audit of public HTML/JavaScript surfaces; not a penetration test."""
from html.parser import HTMLParser
from pathlib import Path
import json, os, re, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"security"/"reports"/"public-surface-audit.json"
SKIP={".git","node_modules",".venv","venv","__pycache__","dist","build"}
EXTS={".html",".htm",".js",".mjs",".cjs"}
findings=[]; counts={"files_scanned":0,"html_files":0,"js_files":0,"oversized_skipped":0}
def add(severity,kind,path,detail,line=None):
    x={"severity":severity,"type":kind,"path":path,"detail":detail}
    if line is not None: x["line"]=line
    findings.append(x)
class Parser(HTMLParser):
    def __init__(self,path): super().__init__(convert_charrefs=True); self.path=path
    def handle_starttag(self,tag,attrs):
        a={k.lower():(v or "") for k,v in attrs}; line=self.getpos()[0]
        for key in ("href","src","action","formaction","xlink:href"):
            value=a.get(key,"").strip()
            if re.match(r"(?i)^javascript\\s*:",value): add("HIGH","javascript_url",self.path,tag+"["+key+"] uses javascript: URL",line)
            if value.lower().startswith("http://") and tag in {"script","iframe","form"}: add("MEDIUM","insecure_external_url",self.path,tag+"["+key+"] uses HTTP",line)
        if a.get("target","").lower()=="_blank" and not {"noopener","noreferrer"}.issubset(set(a.get("rel","").lower().split())):
            add("MEDIUM","unsafe_new_tab_link",self.path,"target=_blank needs rel=noopener noreferrer",line)
        if tag=="script" and a.get("src","").startswith(("http://","https://")) and not a.get("integrity"):
            add("REVIEW","external_script_without_sri",self.path,"Review trust/pinning for external script without integrity",line)
def main():
    for base,dirs,names in os.walk(ROOT):
        dirs[:]=[d for d in dirs if d not in SKIP]
        for name in names:
            p=Path(base)/name
            if p.suffix.lower() not in EXTS: continue
            rel=p.relative_to(ROOT).as_posix()
            try:
                if p.stat().st_size>1500000: counts["oversized_skipped"]+=1; continue
                data=p.read_text(encoding="utf-8",errors="replace")
            except OSError: continue
            counts["files_scanned"]+=1
            if p.suffix.lower() in {".html",".htm"}:
                counts["html_files"]+=1
                try: Parser(rel).feed(data)
                except Exception as e: add("REVIEW","html_parse_issue",rel,type(e).__name__)
            else: counts["js_files"]+=1
            for pattern,kind,detail in [
                (r"\\.innerHTML\\s*=","innerHTML_assignment","Review data flow; prefer textContent or allow-list sanitization for untrusted input"),
                (r"\\bdocument\\.write\\s*\\(","document_write","Review whether untrusted data can reach document.write"),
                (r"\\beval\\s*\\(","eval_usage","Review dynamic code execution"),
            ]:
                for m in re.finditer(pattern,data): add("REVIEW",kind,rel,detail,data.count("\\n",0,m.start())+1)
    high=sum(x["severity"]=="HIGH" for x in findings); med=sum(x["severity"]=="MEDIUM" for x in findings); review=sum(x["severity"]=="REVIEW" for x in findings)
    report={"schema_version":1,"scope":"static heuristic only; not penetration test/certification","counts":counts,"summary":{"high":high,"medium":med,"review":review},"findings":findings,"status":"BLOCKED_HIGH_FINDINGS" if high else "REVIEW_REQUIRED" if med or review else "NO_FINDINGS_IN_CHECKED_RULES"}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    summary=os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary,"a",encoding="utf-8") as f:
            f.write("# Public Surface Security Audit\\n\\n")
            f.write(f"- Scanned: {counts['files_scanned']} files (HTML {counts['html_files']}, JS {counts['js_files']})\\n- HIGH: {high}; MEDIUM: {med}; manual review: {review}\\n- Status: {report['status']}\\n\\n")
            f.write("> Static heuristic only; findings require triage and this is not a security guarantee.\\n")
            for x in findings[:200]: f.write(f"- {x['severity']} {x['path']}:{x.get('line','')} — {x['type']}: {x['detail']}\\n")
    return 1 if high else 0
if __name__=="__main__": sys.exit(main())
