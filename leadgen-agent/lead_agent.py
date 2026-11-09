#!/usr/bin/env python3
"""Local-first, human-reviewed lead CRM with optional Ollama drafting."""
from __future__ import annotations
import argparse, csv, json, os, re, sqlite3, sys, urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
DB_PATH = Path(os.getenv("LEAD_DB_PATH", str(ROOT / "data" / "leads.sqlite3")))
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def clean(value):
    return (value or "").strip()

def norm_domain(url):
    raw = clean(url)
    if not raw: return ""
    try:
        host = urlparse(raw if "://" in raw else "https://" + raw).hostname or ""
        return host.lower().removeprefix("www.")
    except ValueError:
        return ""

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    return db

def init_db():
    with connect() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS leads (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          business_name TEXT NOT NULL,
          website TEXT DEFAULT '', niche TEXT DEFAULT '', country TEXT DEFAULT '',
          contact_name TEXT DEFAULT '', email TEXT DEFAULT '', phone TEXT DEFAULT '',
          source_url TEXT DEFAULT '', need_evidence TEXT DEFAULT '',
          contact_basis TEXT DEFAULT '', score INTEGER NOT NULL DEFAULT 0,
          score_reasons TEXT DEFAULT '[]', status TEXT NOT NULL DEFAULT 'NEW',
          opt_out INTEGER NOT NULL DEFAULT 0,
          next_followup_at TEXT DEFAULT '', created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
          UNIQUE(business_name, website)
        );
        CREATE TABLE IF NOT EXISTS messages (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
          channel TEXT NOT NULL, direction TEXT NOT NULL,
          body TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'DRAFT',
          approved_by TEXT DEFAULT '', approved_at TEXT DEFAULT '',
          provider_message_id TEXT DEFAULT '', created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS events (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
          event_type TEXT NOT NULL, detail TEXT DEFAULT '', created_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
        CREATE INDEX IF NOT EXISTS idx_followup ON leads(next_followup_at);
        CREATE INDEX IF NOT EXISTS idx_messages_lead ON messages(lead_id);
        """)
    return str(DB_PATH)

def find_duplicate(db, row):
    email = clean(row.get("email")).lower()
    phone = re.sub(r"\D", "", clean(row.get("phone")))
    domain = norm_domain(row.get("website"))
    name = clean(row.get("business_name")).casefold()
    candidates = db.execute("SELECT * FROM leads").fetchall()
    for lead in candidates:
        if email and email == clean(lead["email"]).lower(): return lead
        existing_phone = re.sub(r"\D", "", clean(lead["phone"]))
        if phone and phone == existing_phone: return lead
        if domain and domain == norm_domain(lead["website"]): return lead
        if name and name == clean(lead["business_name"]).casefold(): return lead
    return None

def import_csv(path):
    init_db()
    inserted = updated = duplicates = 0
    with open(path, newline="", encoding="utf-8-sig") as f, connect() as db:
        for raw in csv.DictReader(f):
            row = {k: clean(v) for k, v in raw.items() if k}
            business = row.get("business_name", "")
            if not business: continue
            duplicate = find_duplicate(db, row)
            if duplicate:
                duplicates += 1
                # Enrich blanks only; never overwrite an existing verified contact silently.
                updates = {}
                for key in ("website","niche","country","contact_name","email","phone","source_url","need_evidence","contact_basis"):
                    if not clean(duplicate[key]) and row.get(key): updates[key] = row[key]
                if updates:
                    assignments = ", ".join(f"{k}=?" for k in updates)
                    db.execute(f"UPDATE leads SET {assignments}, updated_at=? WHERE id=?",
                               [*updates.values(), now(), duplicate["id"]])
                    updated += 1
                continue
            db.execute("""INSERT INTO leads
              (business_name,website,niche,country,contact_name,email,phone,source_url,need_evidence,contact_basis,created_at,updated_at)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
              tuple(row.get(k,"") for k in ("business_name","website","niche","country","contact_name","email","phone","source_url","need_evidence","contact_basis")) + (now(),now()))
            inserted += 1
    return {"inserted":inserted,"duplicates":duplicates,"enriched":updated}

def score_lead(row):
    score, reasons = 0, []
    def add(points, reason):
        nonlocal score
        score += points
        if points: reasons.append(reason)
    add(25 if clean(row["niche"]) else 0, "niche documented (+25)")
    add(25 if clean(row["need_evidence"]) else 0, "specific need evidence recorded (+25)")
    add(15 if clean(row["website"]) and norm_domain(row["website"]) else 0, "business website recorded (+15)")
    add(20 if clean(row["email"]) or clean(row["phone"]) else 0, "business contact route recorded (+20)")
    add(15 if clean(row["contact_basis"]) else 0, "contact basis/source recorded (+15)")
    if row["opt_out"]:
        return 0, ["opt-out: suppressed"]
    return min(score,100), reasons

def score_all():
    init_db()
    with connect() as db:
        rows=db.execute("SELECT * FROM leads").fetchall()
        for row in rows:
            score,reasons=score_lead(row)
            db.execute("UPDATE leads SET score=?,score_reasons=?,updated_at=? WHERE id=?",
                       (score,json.dumps(reasons),now(),row["id"]))
    return len(rows)

def ollama_generate(prompt):
    payload=json.dumps({"model":OLLAMA_MODEL,"prompt":prompt,"stream":False,
                        "options":{"temperature":0.2}}).encode()
    req=urllib.request.Request(OLLAMA_URL+"/api/generate",data=payload,
        headers={"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=90) as response:
        data=json.loads(response.read().decode("utf-8"))
    return clean(data.get("response"))

def draft_message(lead_id):
    init_db()
    with connect() as db:
        lead=db.execute("SELECT * FROM leads WHERE id=?",(lead_id,)).fetchone()
        if not lead: raise ValueError("Lead not found")
        if lead["opt_out"]: raise ValueError("Lead is opted out; drafting suppressed")
        context={k:lead[k] for k in ("business_name","niche","country","website","need_evidence","contact_name")}
        prompt=("Write a concise, respectful first-contact business email in English. "
          "Use only these verified fields; do not invent facts, claims, relationship, or urgency. "
          "Offer a short scope discussion, ask permission to send details, and include a polite opt-out. "
          "No fake personalization. Return subject and body only.\n"
          + json.dumps(context,ensure_ascii=False))
        try:
            result=ollama_generate(prompt)
            source="ollama:"+OLLAMA_MODEL
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError):
            result=("Subject: A small, clearly scoped pilot from Shirmani Research Institute\n\n"
              f"Hello {clean(lead['contact_name']) or 'Team'},\n\n"
              f"I’m contacting you because {clean(lead['business_name'])} is listed in the "
              f"{clean(lead['niche']) or 'your sector'} area. Shirmani Research Institute offers "
              "Hindi/English writing and source-based research summaries. Would a short outline "
              "of a small, fixed-scope pilot be useful? If this is not relevant, please let me know "
              "and I will not follow up.\n\nRegards,\nShirmani Research Institute")
            source="safe-template-fallback"
        cur=db.execute("INSERT INTO messages(lead_id,channel,direction,body,status,created_at) VALUES(?,?,?,?,?,?)",
                       (lead_id,"EMAIL","OUTBOUND_DRAFT",f"[{source}]\n{result}","DRAFT",now()))
        db.execute("INSERT INTO events(lead_id,event_type,detail,created_at) VALUES(?,?,?,?)",
                   (lead_id,"MESSAGE_DRAFTED",f"message_id={cur.lastrowid}; sender not invoked",now()))
        return {"message_id":cur.lastrowid,"status":"DRAFT","sender_invoked":False,"body":result}

def record_incoming(lead_id, channel, body, consent_context):
    """Record an inbound message only when caller supplies a consent/context reference."""
    if not clean(consent_context): raise ValueError("Consent/context reference required")
    init_db()
    with connect() as db:
        if not db.execute("SELECT 1 FROM leads WHERE id=?",(lead_id,)).fetchone():
            raise ValueError("Lead not found")
        cur=db.execute("INSERT INTO messages(lead_id,channel,direction,body,status,created_at) VALUES(?,?,?,?,?,?)",
          (lead_id,channel,"INBOUND",clean(body),"RECEIVED",now()))
        db.execute("INSERT INTO events(lead_id,event_type,detail,created_at) VALUES(?,?,?,?)",
          (lead_id,"INBOUND_RECEIVED",f"message_id={cur.lastrowid}; context={clean(consent_context)}",now()))
        return cur.lastrowid

def list_leads():
    init_db()
    with connect() as db:
        return [dict(r) for r in db.execute("SELECT id,business_name,niche,country,score,status,opt_out,email,phone FROM leads ORDER BY score DESC,id").fetchall()]

def main():
    p=argparse.ArgumentParser(description="Shirmani Local Lead Agent")
    sub=p.add_subparsers(dest="cmd",required=True)
    sub.add_parser("init")
    imp=sub.add_parser("import-csv"); imp.add_argument("file")
    sub.add_parser("score")
    dr=sub.add_parser("draft"); dr.add_argument("lead_id",type=int)
    sub.add_parser("list")
    args=p.parse_args()
    if args.cmd=="init": print(init_db())
    elif args.cmd=="import-csv": print(json.dumps(import_csv(args.file),ensure_ascii=False))
    elif args.cmd=="score": print(json.dumps({"scored":score_all()}))
    elif args.cmd=="draft": print(json.dumps(draft_message(args.lead_id),ensure_ascii=False,indent=2))
    elif args.cmd=="list": print(json.dumps(list_leads(),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
