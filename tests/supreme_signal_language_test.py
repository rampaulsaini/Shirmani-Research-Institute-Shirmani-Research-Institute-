import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated/supreme-nlp/signal-input.jsonl"; OUTPUT=ROOT/"generated/supreme-nlp/signal-language.json"
def main():
    INPUT.parent.mkdir(parents=True,exist_ok=True)
    INPUT.write_text("\n".join([
      json.dumps({"source_id":"sensor-a","modality":"plant-electrical","features":{"voltage":1.0,"temperature":20.0}}),
      json.dumps({"source_id":"sensor-a","modality":"plant-electrical","features":{"voltage":1.2,"temperature":20.4}}),
      json.dumps({"source_id":"sensor-b","modality":"environment","features":{"voltage":1.4,"temperature":20.8}}),
      json.dumps({"source_id":"sensor-b","modality":"environment","features":{"voltage":1.6,"temperature":21.0}})
    ])+"\n",encoding="utf-8")
    r=subprocess.run([sys.executable,str(ROOT/"supreme-nlp/signal_to_language.py")],cwd=ROOT,text=True,capture_output=True)
    assert r.returncode==0,r.stdout+r.stderr
    d=json.loads(OUTPUT.read_text(encoding="utf-8"))
    assert d["status"]=="INTERPRETED"; assert d["observed_signal"]["record_count"]==4
    assert d["inference"]["confidence"]<=0.90; assert d["verification_state"]=="UNVERIFIED"
    assert d["governance"]["fail_closed"] is True and d["governance"]["subjective_experience_claim_allowed"] is False
    assert d["patterns"]
    text=d["plain_language"].lower()
    assert "measurable signal pattern" in text
    assert "subjective feeling" in text
    print("SHIRMANI Supreme signal-to-language regression: PASS")
if __name__=="__main__": main()
