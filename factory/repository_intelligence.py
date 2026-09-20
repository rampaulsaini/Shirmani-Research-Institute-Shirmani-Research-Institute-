#!/usr/bin/env python3
"""Build a machine-readable inventory of the federated repositories.

The inventory is metadata-only and intentionally does not treat generated
artifacts as canonical knowledge. It records default branches and basic
repository characteristics so downstream agents can make source-aware choices.
"""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "factory/repos.json").read_text(encoding="utf-8"))
OUT = ROOT / "generated"
OUT.mkdir(parents=True, exist_ok=True)

def run(args):
    p = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return p.returncode, p.stdout.strip()

def inventory_repo(full):
    owner, name = full.split("/", 1)
    code, raw = run(["git", "ls-remote", "--symref", f"https://github.com/{full}.git", "HEAD"])
    branch = None
    head = None
    if code == 0:
        for line in raw.splitlines():
            if line.startswith("ref:") and "HEAD" in line:
                ref = line.split()[1]
                branch = ref.rsplit("/", 1)[-1]
            elif line and "\t" in line:
                head = line.split("\t", 1)[0]
    return {
        "repository": full,
        "owner": owner,
        "name": name,
        "default_branch": branch,
        "head_sha": head,
        "available": code == 0 and bool(head),
        "external_reference": not full.startswith("rampaulsaini/"),
        "inventory_method": "git-ls-remote",
    }

def main():
    now = datetime.now(timezone.utc).isoformat()
    repos = [inventory_repo(r) for r in CFG["repositories"]]
    payload = {
        "version": 1,
        "generated_at": now,
        "hub_repository": CFG["hub_repository"],
        "repository_count": len(repos),
        "repositories": repos,
        "policy": CFG["policy"],
    }
    (OUT / "repository-intelligence.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"repository_count": len(repos), "available": sum(x["available"] for x in repos)}))

if __name__ == "__main__":
    main()
