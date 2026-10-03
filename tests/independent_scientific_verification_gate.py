import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 s=json.loads((ROOT/"schemas/independent-scientific-verification.schema.json").read_text())
 assert "verification_state" in s["required"]
 assert "VERIFIED" in s["properties"]["verification_state"]["enum"]
 assert "INDEPENDENT_REPLICATION" in s["properties"]["replication_status"]["enum"]
 r=subprocess.run([sys.executable,str(ROOT/"factory/independent_scientific_verification_gate.py")],cwd=ROOT,text=True,capture_output=True)
 assert r.returncode==0,r.stderr+r.stdout
 print("Independent scientific verification hardening test: PASS")
if __name__=="__main__":main()
