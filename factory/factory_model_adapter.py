#!/usr/bin/env python3
"""Provider-neutral, free-first text generation adapter.

Default: deterministic source-grounded synthesis. An external command can be
enabled with MODEL_COMMAND, but the core factory never requires a paid API.
The command receives the prompt on stdin and must return text on stdout.
"""
import os, subprocess

def generate(prompt, fallback):
    command=os.environ.get("MODEL_COMMAND","").strip()
    if not command:
        return fallback, "deterministic"
    try:
        p=subprocess.run(command, input=prompt, text=True, shell=True,
                         capture_output=True, timeout=120)
        if p.returncode==0 and p.stdout.strip():
            return p.stdout.strip(), "external-command"
    except Exception:
        pass
    return fallback, "deterministic-fallback"
