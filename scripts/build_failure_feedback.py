import json
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"generated/failure-registry.json"
out=ROOT/"generated/automission-feedback.json"

def main():
    x=json.loads(src.read_text(encoding="utf-8"))
    groups=x.get("failure_groups",[])
    ranked=sorted(groups,key=lambda g:(-int(g.get("count",0)),g.get("category",""),g.get("fingerprint","")))
    actions=[]
    for g in ranked[:25]:
        actions.append({
          "fingerprint":g["fingerprint"],
          "priority":"HIGH" if g["count"]>=3 else "NORMAL",
          "category":g["category"],
          "occurrences":g["count"],
          "recommended_action":"inspect_and_patch_then_retest",
          "automatic_source_mutation":False,
          "automatic_retry":False,
          "requires_subsequent_green_run":True
        })
    result={
      "schema_version":1,
      "source_generated_at":x.get("generated_at"),
      "feedback_mode":"bounded_human_review",
      "failure_groups_considered":len(groups),
      "feedback_items":actions,
      "safety_boundary":{
        "automatic_source_mutation":False,
        "automatic_retry":False,
        "failure_group_is_not_root_cause":True,
        "repair_is_not_fixed_until_retest":True
      }
    }
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"feedback_items":len(actions),"path":str(out)}))
if __name__=="__main__": main()
