#!/usr/bin/env python3
"""Aggregate public product reviews into a production-quality feedback signal."""
from __future__ import annotations
import json, os, re, subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"; OUT.mkdir(exist_ok=True)
def gh_issues():
    env=dict(os.environ); env["GH_TOKEN"]=env.get("GITHUB_TOKEN","")
    p=subprocess.run(["gh","issue","list","--state","all","--label","customer-review","--limit","1000","--json","number,title,body,state,createdAt,closedAt,url"],cwd=ROOT,text=True,capture_output=True,env=env,check=False)
    return json.loads(p.stdout or "[]") if p.returncode==0 else []
def rating(body):
    m=re.search(r"(?:rating|रेटिंग)\s*[:：]\s*([1-5])",body or "",re.I); return int(m.group(1)) if m else None
def product(body,title):
    m=re.search(r"(?:product\s*id|product|उत्पाद)\s*[:：]\s*([A-Z]{2}-?\d{3,6})",body or "",re.I)
    if m:return m.group(1).upper()
    m=re.search(r"SP-\d{4}",title or "",re.I); return m.group(0).upper() if m else "UNSPECIFIED"
def main():
    issues=gh_issues(); rows=[]; ratings=[]; by=defaultdict(list)
    for i in issues:
        rr=rating(i.get("body","")); pid=product(i.get("body",""),i.get("title",""))
        row={"issue":i.get("number"),"url":i.get("url"),"title":i.get("title"),"state":i.get("state"),"product_id":pid,"rating":rr,"created_at":i.get("createdAt"),"closed_at":i.get("closedAt")}
        rows.append(row)
        if rr is not None: ratings.append(rr); by[pid].append(rr)
    payload={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"review_count":len(rows),"rated_review_count":len(ratings),"average_rating":round(sum(ratings)/len(ratings),2) if ratings else None,"rating_distribution":dict(Counter(map(str,ratings))),"by_product":{p:{"reviews":len(v),"average_rating":round(sum(v)/len(v),2)} for p,v in by.items()},"reviews":rows,"quality_improvement":{"source":"public GitHub customer-review issues","production_use":"reviewed and low-rated products become improvement candidates","automatic_quality_claim":False}}
    (OUT/"public-review-quality.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"review_count":len(rows),"rated_review_count":len(ratings),"average_rating":payload["average_rating"]},ensure_ascii=False))
if __name__=="__main__": main()
