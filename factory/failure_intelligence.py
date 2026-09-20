#!/usr/bin/env python3
"""Collect and deduplicate GitHub Actions failures without mutating workflows.

The collector is intentionally evidence-first:
- workflow runs are counted separately from workflow definitions;
- failed runs are grouped by workflow/job/step;
- logs are sampled only for the newest failed runs;
- no automatic retry or source-code mutation is performed;
- missing API data remains explicitly unavailable.
"""
import hashlib
import json
import os
import re
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone

API = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY", "rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
MAX_LOG_RUNS = int(os.environ.get("FAILURE_LOG_SAMPLE_RUNS", "50"))
MAX_RUN_PAGES = int(os.environ.get("FAILURE_RUN_PAGES", "20"))

def api(path):
    url = API + path if path.startswith("/") else path
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "shirmani-failure-intelligence",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def api_text(path):
    url = API + path if path.startswith("/") else path
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "shirmani-failure-intelligence",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")

def redact(value):
    text = str(value or "")
    text = re.sub(r"gh[pousr]_[A-Za-z0-9_\-]+", "<TOKEN>", text)
    text = re.sub(r"x-access-token:[^@\s]+@", "x-access-token:<TOKEN>@", text)
    return text[:500]

def normalize_signal(text):
    text = redact(text).lower()
    text = re.sub(r"\b\d{4}-\d{2}-\d{2}t\d{2}:\d{2}:\d{2}(?:\.\d+)?z\b", "<timestamp>", text)
    text = re.sub(r"/home/runner/work/[^\s]+", "<runner-path>", text)
    text = re.sub(r"\b[0-9a-f]{7,40}\b", "<sha>", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def fingerprint(parts):
    basis = "|".join(normalize_signal(x) for x in parts)
    return "fail_" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:20]

def failed_step_names(job):
    return [
        s.get("name")
        for s in (job.get("steps") or [])
        if s.get("conclusion") in {"failure", "cancelled", "timed_out"}
    ]

def classify(signal, step):
    s = (signal + " " + step).lower()
    if "syntaxerror" in s or "py_compile" in s or "python" in s and "validate" in s:
        return "python-syntax-or-validation"
    if "publication gate" in s or "qc" in s and "block" in s:
        return "qc-publication-gate"
    if "timeout" in s or "timed out" in s:
        return "timeout"
    if "permission" in s or "403" in s or "401" in s:
        return "permissions"
    if "not found" in s or "404" in s:
        return "missing-resource"
    if "rate limit" in s or "429" in s:
        return "rate-limit"
    if "network" in s or "connection" in s or "could not resolve" in s:
        return "network"
    return "uncategorized"

def collect():
    runs = []
    for page in range(1, MAX_RUN_PAGES + 1):
        payload = api(f"/repos/{REPO}/actions/runs?per_page=100&page={page}")
        page_runs = payload.get("workflow_runs") or []
        runs.extend(page_runs)
        if len(page_runs) < 100:
            break

    failures = [r for r in runs if r.get("conclusion") == "failure"]
    workflow_counts = Counter(r.get("name") for r in failures)
    fingerprints = defaultdict(lambda: {
        "count": 0, "workflow_names": set(), "jobs": set(), "steps": set(),
        "category": "uncategorized", "sample_run_ids": [], "signals": []
    })

    for run in failures:
        run_id = run.get("id")
        try:
            jobs = (api(f"/repos/{REPO}/actions/runs/{run_id}/jobs?per_page=100").get("jobs") or [])
        except Exception:
            jobs = []

        failed_jobs = [j for j in jobs if j.get("conclusion") == "failure"]
        for job in failed_jobs or [{}]:
            steps = failed_step_names(job)
            step = steps[0] if steps else (job.get("name") or "unknown-step")
            signal = ""
            if run_index < MAX_LOG_RUNS and job.get("id"):
                try:
                    log = api_text(f"/repos/{REPO}/actions/jobs/{job['id']}/logs")
                    signal_lines = [
                        redact(line) for line in str(log).splitlines()
                        if re.search(r"##\[error\]|Traceback|SyntaxError|Error:|Exception|failed|FAIL|BLOCK", line, re.I)
                    ]
                    signal = signal_lines[-1] if signal_lines else ""
                except Exception:
                    signal = ""

            fp = fingerprint([run.get("name"), job.get("name"), step, signal])
            item = fingerprints[fp]
            item["count"] += 1
            item["workflow_names"].add(run.get("name"))
            if job.get("name"):
                item["jobs"].add(job.get("name"))
            item["steps"].add(step)
            item["category"] = classify(signal, step)
            if len(item["sample_run_ids"]) < 5:
                item["sample_run_ids"].append(run_id)
            if signal and signal not in item["signals"] and len(item["signals"]) < 3:
                item["signals"].append(signal)

    groups = []
    for fp, item in sorted(fingerprints.items(), key=lambda x: (-x[1]["count"], x[0])):
        groups.append({
            "fingerprint": fp,
            "count": item["count"],
            "category": item["category"],
            "workflow_names": sorted(item["workflow_names"]),
            "jobs": sorted(item["jobs"]),
            "failed_steps": sorted(item["steps"]),
            "sample_run_ids": item["sample_run_ids"],
            "signals": item["signals"],
        })

    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": REPO,
        "semantics": {
            "workflow_run_count": len(runs),
            "failed_run_count": len(failures),
            "workflow_definition_count_not_measured": True,
            "automatic_repair": False,
            "automatic_retry": False,
            "log_sampling_limit": MAX_LOG_RUNS,
        },
        "failed_runs_by_workflow": dict(sorted(workflow_counts.items(), key=lambda x: (-x[1], x[0]))),
        "failure_groups": groups,
        "limitations": [
            "Jobs/logs can be unavailable for deleted, expired or inaccessible runs.",
            "Fingerprinting is deterministic grouping, not proof of a single root cause.",
            "A repair must be validated by a subsequent run before it is considered fixed.",
        ],
    }

def main():
    output = collect()
    os.makedirs("generated", exist_ok=True)
    path = "generated/failure-registry.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({
        "path": path,
        "workflow_run_count": output["semantics"]["workflow_run_count"],
        "failed_run_count": output["semantics"]["failed_run_count"],
        "failure_group_count": len(output["failure_groups"]),
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
