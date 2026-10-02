from pathlib import Path
import json

ROOT=Path('generated/supreme-nlp')

def load(name):
    p=ROOT/name
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None

def verify_status(r):
    x=r.get('result',r)
    v=x.get('verification') or r.get('verification') or {}
    return str(v.get('status','UNVERIFIED')).upper()

def main():
    layers={k:load(v) for k,v in {'baseline':'status.json','multimodal':'multimodal-status.json','practitioner':'practitioner-status.json'}.items()}
    layers={k:v for k,v in layers.items() if v is not None}
    statuses={k:verify_status(v) for k,v in layers.items()}
    failures=[]
    if not layers: failures.append('no layer records available')
    if any(v not in {'UNVERIFIED','UNKNOWN'} for v in statuses.values()):
        failures.append('verification status stronger than UNVERIFIED detected')
    report={'schema_version':'supreme-nlp-cross-layer-v1','status':'PASS' if not failures else 'BLOCKED','layers_present':sorted(layers),'verification_status':statuses,'failures':failures,'governance':{'fail_closed':True,'aggregation_creates_no_new_evidence':True,'subjective_experience_claim_allowed':False,'scheduled_code_mutation_allowed':False,'independent_verification_required':True}}
    ROOT.mkdir(parents=True,exist_ok=True)
    (ROOT/'cross-layer-consistency.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': main()