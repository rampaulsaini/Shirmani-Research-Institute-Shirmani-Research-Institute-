from __future__ import annotations
import json, os, re, urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"generated"
REPO=os.environ.get("GITHUB_REPOSITORY","rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-"); TOKEN=os.environ.get("GITHUB_TOKEN","")
def api(path):
    req=urllib.request.Request("https://api.github.com"+path,headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {TOKEN}","X-GitHub-Api-Version":"2022-11-28"})
    with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
def extract(body):
    body=body or ""
    def field(label):
        m=re.search(rf"### {re.escape(label)}\s*\n\s*(.+?)(?=\n### |\Z)",body,re.S|re.I); return m.group(1).strip() if m else ""
    pid=field("Product ID").split()[0].upper()
    try: rating=int(re.search(r"\d+",field("Overall rating")).group())
    except Exception: rating=0
    return pid,rating,field("Product experience"),field("Improvement request")
def main():
    OUT.mkdir(exist_ok=True); issues=[]; page=1
    while page<=10:
        data=api(f"/repos/{REPO}/issues?state=all&labels=product-review&per_page=100&page={page}")
        if not data: break
        issues.extend([x for x in data if "pull_request" not in x])
        if len(data)<100: break
        page+=1
    reviews=defaultdict(list); rows=[]
    for x in issues:
        pid,rating,experience,improvement=extract(x.get("body"))
        if not re.fullmatch(r"SP-\d{4}",pid) or not 1<=rating<=5: continue
        row={"issue":x["number"],"product_id":pid,"rating":rating,"experience":experience,"improvement":improvement,"state":x["state"],"updated_at":x["updated_at"]}
        rows.append(row); reviews[pid].append(row)
    cp=OUT/"1000-digital-products.json"; catalog=json.loads(cp.read_text(encoding="utf-8"))
    for p in catalog.get("products",[]):
        rr=reviews.get(p["id"],[]); ratings=[r["rating"] for r in rr]; avg=round(sum(ratings)/len(ratings),2) if ratings else None
        p["review_count"]=len(rr); p["review_rating"]=avg
        p["review_quality_signal"]="HIGH" if avg is not None and avg>=4.5 else "POSITIVE" if avg is not None and avg>=4 else "IMPROVEMENT" if avg is not None else "NO_REVIEWS"
        p["improvement_queue_count"]=sum(1 for r in rr if r["improvement"])
    summary={"generated_at":datetime.now(timezone.utc).isoformat(),"review_count":len(rows),"reviewed_products":len(reviews),"average_rating":round(sum(r["rating"] for r in rows)/len(rows),2) if rows else None,"purpose":"Public customer experience signals feed continuous product-quality improvement.","verification_scope":"Reviews are product-experience inputs; they do not constitute independent verification.","products":{pid:{"count":len(rs),"average_rating":round(sum(r["rating"] for r in rs)/len(rs),2),"improvement_requests":sum(1 for r in rs if r["improvement"])} for pid,rs in reviews.items()}}
    (OUT/"public-reviews.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"review-quality-dashboard.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    catalog["review_system"]=summary; cp.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
