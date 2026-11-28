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
          contact_basis TEXT DEFAULT '',
          current_product TEXT DEFAULT '', product_category TEXT DEFAULT '',
          buyer_evidence TEXT DEFAULT '', buyer_evidence_url TEXT DEFAULT '',
          buyer_evidence_type TEXT DEFAULT '', evidence_checked_at TEXT DEFAULT '',
          data_permission_basis TEXT DEFAULT '', contact_permission_status TEXT DEFAULT '',
          sri_product_match TEXT DEFAULT '', sri_product_category TEXT DEFAULT '', sri_product_match_url TEXT DEFAULT '',
          permission_evidence_url TEXT DEFAULT '', permission_checked_at TEXT DEFAULT '',
          comparison_evidence_url TEXT DEFAULT '', comparison_checked_at TEXT DEFAULT '',
          quality_comparison_result TEXT DEFAULT '', total_cost_comparison_result TEXT DEFAULT '',
          comparison_summary TEXT DEFAULT '', added_value TEXT DEFAULT '',
          score INTEGER NOT NULL DEFAULT 0,
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
        # Additive migrations preserve existing local databases.
        existing = {r["name"] for r in db.execute("PRAGMA table_info(leads)").fetchall()}
        additions = {
          "current_product": "TEXT DEFAULT ''", "product_category": "TEXT DEFAULT ''",
          "buyer_evidence": "TEXT DEFAULT ''", "buyer_evidence_url": "TEXT DEFAULT ''",
          "buyer_evidence_type": "TEXT DEFAULT ''", "evidence_checked_at": "TEXT DEFAULT ''",
          "data_permission_basis": "TEXT DEFAULT ''", "contact_permission_status": "TEXT DEFAULT ''",
          "sri_product_match": "TEXT DEFAULT ''", "sri_product_category": "TEXT DEFAULT ''",
          "sri_product_match_url": "TEXT DEFAULT ''",
          "permission_evidence_url": "TEXT DEFAULT ''", "permission_checked_at": "TEXT DEFAULT ''",
          "comparison_evidence_url": "TEXT DEFAULT ''", "comparison_checked_at": "TEXT DEFAULT ''",
          "quality_comparison_result": "TEXT DEFAULT ''", "total_cost_comparison_result": "TEXT DEFAULT ''",
          "comparison_summary": "TEXT DEFAULT ''", "added_value": "TEXT DEFAULT ''"
        }
        for name, declaration in additions.items():
            if name not in existing:
                db.execute(f"ALTER TABLE leads ADD COLUMN {name} {declaration}")
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
                for key in ("website","niche","country","contact_name","email","phone","source_url","need_evidence","contact_basis","current_product","product_category","buyer_evidence","buyer_evidence_url","buyer_evidence_type","evidence_checked_at","data_permission_basis","contact_permission_status","sri_product_match","sri_product_category","sri_product_match_url","permission_evidence_url","permission_checked_at","comparison_evidence_url","comparison_checked_at","quality_comparison_result","total_cost_comparison_result","comparison_summary","added_value"):
                    if not clean(duplicate[key]) and row.get(key): updates[key] = row[key]
                if updates:
                    assignments = ", ".join(f"{k}=?" for k in updates)
                    db.execute(f"UPDATE leads SET {assignments}, updated_at=? WHERE id=?",
                               [*updates.values(), now(), duplicate["id"]])
                    updated += 1
                continue
            db.execute("""INSERT INTO leads
              (business_name,website,niche,country,contact_name,email,phone,source_url,need_evidence,contact_basis,current_product,product_category,buyer_evidence,buyer_evidence_url,buyer_evidence_type,evidence_checked_at,data_permission_basis,contact_permission_status,sri_product_match,sri_product_category,sri_product_match_url,permission_evidence_url,permission_checked_at,comparison_evidence_url,comparison_checked_at,quality_comparison_result,total_cost_comparison_result,comparison_summary,added_value,created_at,updated_at)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
              tuple(row.get(k,"") for k in ("business_name","website","niche","country","contact_name","email","phone","source_url","need_evidence","contact_basis","current_product","product_category","buyer_evidence","buyer_evidence_url","buyer_evidence_type","evidence_checked_at","data_permission_basis","contact_permission_status","sri_product_match","sri_product_category","sri_product_match_url","permission_evidence_url","permission_checked_at","comparison_evidence_url","comparison_checked_at","quality_comparison_result","total_cost_comparison_result","comparison_summary","added_value")) + (now(),now()))
            inserted += 1
    return {"inserted":inserted,"duplicates":duplicates,"enriched":updated}

def buyer_gate(row):
    """Fail closed unless existing digital-product use and lawful contact basis are evidenced."""
    required = {
        "current_product": "current digital product/tool",
        "product_category": "digital product category",
        "buyer_evidence": "existing purchase/use evidence",
        "buyer_evidence_url": "evidence source URL",
        "buyer_evidence_type": "evidence type",
        "evidence_checked_at": "evidence review date",
        "data_permission_basis": "data-use permission/licence basis",
        "contact_permission_status": "contact permission status",
        "sri_product_match": "existing SRI product match",
        "sri_product_category": "SRI product category",
        "sri_product_match_url": "SRI catalogue/product evidence URL",
        "permission_evidence_url": "contact/data permission evidence URL",
        "permission_checked_at": "permission review date",
        "comparison_evidence_url": "comparative test evidence URL",
        "comparison_checked_at": "comparative test review date",
        "quality_comparison_result": "quality comparison result",
        "total_cost_comparison_result": "total-cost comparison result",
        "comparison_summary": "comparison method and result summary",
        "added_value": "specific added value",
    }
    def value(key):
        return row[key] if key in row.keys() else ""
    missing = [label for key, label in required.items() if not clean(value(key))]
    if missing:
        return False, ["missing: " + ", ".join(missing)]
    if not norm_domain(value("buyer_evidence_url")):
        return False, ["buyer evidence URL is invalid"]
    if not norm_domain(value("sri_product_match_url")):
        return False, ["SRI product match URL is invalid"]
    if not norm_domain(value("permission_evidence_url")):
        return False, ["permission evidence URL is invalid"]
    if not norm_domain(value("comparison_evidence_url")):
        return False, ["comparison evidence URL is invalid"]
    if clean(value("product_category")).casefold() != clean(value("sri_product_category")).casefold():
        return False, ["SRI product category does not exactly match the buyer's current category"]
    if clean(value("quality_comparison_result")).lower() != "better":
        return False, ["comparative quality result is not documented as better"]
    if clean(value("total_cost_comparison_result")).lower() != "lower":
        return False, ["comparative total-cost result is not documented as lower"]
    evidence_type = clean(value("buyer_evidence_type")).lower()
    if evidence_type not in {"self_declared", "verified_purchase", "partner_authorized", "licensed_dataset"}:
        return False, ["evidence type is not an accepted proof class"]
    permission = clean(value("contact_permission_status")).lower()
    if permission not in {"consented", "permitted_business_contact", "existing_relationship"}:
        return False, ["contact permission is not explicitly valid"]
    try:
        checked = datetime.fromisoformat(clean(value("evidence_checked_at")).replace("Z", "+00:00"))
        permission_checked = datetime.fromisoformat(clean(value("permission_checked_at")).replace("Z", "+00:00"))
        comparison_checked = datetime.fromisoformat(clean(value("comparison_checked_at")).replace("Z", "+00:00"))
        if checked.tzinfo is None:
            checked = checked.replace(tzinfo=timezone.utc)
        if permission_checked.tzinfo is None:
            permission_checked = permission_checked.replace(tzinfo=timezone.utc)
        if comparison_checked.tzinfo is None:
            comparison_checked = comparison_checked.replace(tzinfo=timezone.utc)
        current = datetime.now(timezone.utc)
        for label, reviewed in (("buyer evidence", checked), ("permission evidence", permission_checked), ("comparison evidence", comparison_checked)):
            age = current - reviewed.astimezone(timezone.utc)
            if age < timedelta(days=-1) or age > timedelta(days=180):
                return False, [label + " is future-dated or stale (over 180 days)"]
    except (TypeError, ValueError):
        return False, ["evidence review date must be ISO-8601"]
    return True, ["buyer, permission, same-category match, better-quality and lower-total-cost evidence fields present; human validation still required"]

def score_lead(row):
    qualified, gate_reasons = buyer_gate(row)
    if row["opt_out"]:
        return 0, ["opt-out: suppressed"]
    if not qualified:
        return 0, ["NOT_QUALIFIED: existing digital buyer gate blocked", *gate_reasons]
    score, reasons = 0, list(gate_reasons)
    def add(points, reason):
        nonlocal score
        score += points
        if points: reasons.append(reason)
    add(15 if clean(row["niche"]) else 0, "niche documented (+15)")
    add(15 if clean(row["need_evidence"]) else 0, "specific need evidence recorded (+15)")
    add(10 if clean(row["website"]) and norm_domain(row["website"]) else 0, "business website recorded (+10)")
    add(15 if clean(row["email"]) or clean(row["phone"]) else 0, "business contact route recorded (+15)")
    add(10 if clean(row["contact_basis"]) else 0, "contact source recorded (+10)")
    add(10 if clean(row["source_url"]) else 0, "source URL recorded (+10)")
    add(10 if clean(row["country"]) else 0, "country recorded (+10)")
    add(5 if clean(row["contact_name"]) else 0, "contact name recorded (+5)")
    return min(score, 100), reasons

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
        qualified, reasons = buyer_gate(lead)
        if not qualified: raise ValueError("NOT_QUALIFIED: " + "; ".join(reasons))
        context={k:lead[k] for k in ("business_name","niche","country","website","need_evidence","contact_name","current_product","product_category","buyer_evidence","sri_product_match","comparison_summary","added_value")}
        prompt=("Write a concise, respectful business email in English to an established buyer of a digital product. "
          "Use only these supplied facts; do not invent product use, comparative superiority, savings, relationship, or urgency. "
          "Refer to the current product/category, the documented comparison summary and the specific added value; ask permission to share details. "
          "Include a polite opt-out. Return subject and body only.\n"
          + json.dumps(context,ensure_ascii=False))
        try:
            result=ollama_generate(prompt)
            source="ollama:"+OLLAMA_MODEL
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError):
            result=("Subject: A relevant option in your existing digital product category\n\n"
              f"Hello {clean(lead['contact_name']) or 'Team'},\n\n"
              f"I understand that {clean(lead['business_name'])} uses {clean(lead['current_product'])} "
              f"in the {clean(lead['product_category'])} category, based on the recorded source. "
              f"An existing SRI catalogue match is {clean(lead['sri_product_match'])}. "
              f"Our recorded comparison summary is: {clean(lead['comparison_summary'])}. "
              f"The specific added value is: {clean(lead['added_value'])}. "
              "May I share the supporting evidence and full scope for your review? "
              "If this is not relevant, please let me know and I will not follow up.\n\nRegards,\nShirmani Research Institute")
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
