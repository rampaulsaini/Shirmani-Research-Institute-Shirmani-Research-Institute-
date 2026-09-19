import json
from pathlib import Path

def make_jobs(config, topics):
    jobs=[]
    products=config["products"]
    for kind,target in [("verse",products["verses"]),("book",products["digital_books"]),
                        ("research-paper",products["research_papers"]),
                        ("certificate",products["certificates"]),
                        ("audio-prompt",products["audio_prompts"])]:
        for i in range(1,int(target)+1):
            jobs.append({"job_id":f"{kind}-{i:06d}","kind":kind,"number":i,
                         "topic":topics[(i-1)%len(topics)],"status":"pending"})
    return jobs

def load(path):
    p=Path(path)
    if not p.exists(): return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]

def save(path,jobs):
    Path(path).write_text("\n".join(json.dumps(j,ensure_ascii=False) for j in jobs)+"\n",encoding="utf-8")

def claim_batch(jobs, batch_size=1000):
    claimed=[]
    for j in jobs:
        if j["status"]=="pending" and len(claimed)<batch_size:
            j["status"]="running"; claimed.append(j)
    return jobs,claimed
