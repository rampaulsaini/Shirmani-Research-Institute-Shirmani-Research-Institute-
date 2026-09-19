import json
from pathlib import Path

def load_topics(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))["topics"]

def classify(text, topics):
    low=text.lower()
    hits=[]
    for t in topics:
        score=sum(1 for k in t["keywords"] if k.lower() in low)
        if score:
            hits.append((score,t["id"]))
    hits.sort(reverse=True)
    return [x[1] for x in hits[:3]] or ["general"]

def enrich(rows, topic_path):
    topics=load_topics(topic_path)
    return [{**r,"topics":classify(r.get("text",""),topics)} for r in rows]
