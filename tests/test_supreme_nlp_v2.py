import json
import importlib.util
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("benchmark_v2", ROOT/"supreme-nlp"/"benchmark_v2.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
evaluate=mod.evaluate

def main():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"b.jsonl"
        rows=[
          {"specimen_id":"a","experiment_id":"e1","split":"train","y_true":"0","y_pred":"0","confidence":0.1},
          {"specimen_id":"b","experiment_id":"e2","split":"test","y_true":"1","y_pred":"1","confidence":0.9},
          {"specimen_id":"c","experiment_id":"e3","split":"test","y_true":"0","y_pred":"0","confidence":0.1},
        ]
        p.write_text("\n".join(json.dumps(x) for x in rows),encoding="utf-8")
        r=evaluate(str(p))
        assert r["status"]=="OK"
        assert r["accuracy"]==1.0
        rows.append({"specimen_id":"a","experiment_id":"e4","split":"test","y_true":"1","y_pred":"1","confidence":0.9})
        p.write_text("\n".join(json.dumps(x) for x in rows),encoding="utf-8")
        assert evaluate(str(p))["status"]=="BLOCKED"
    print("SUPREME_NLP_V2_CONTRACT_TEST: PASS")

if __name__=="__main__":
    main()
