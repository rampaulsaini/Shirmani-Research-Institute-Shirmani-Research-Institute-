import csv, tempfile, unittest
from unittest.mock import patch
from datetime import datetime, timezone
from pathlib import Path
import lead_agent as agent

class LeadAgentTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        agent.DB_PATH=Path(self.tmp.name)/"test.sqlite3"
        agent.init_db()
    def tearDown(self): self.tmp.cleanup()
    def buyer(self, **overrides):
        row={
            "business_name":"Acme", "website":"https://acme.example", "niche":"software",
            "country":"India", "contact_name":"Sales Team", "email":"sales@acme.example",
            "phone":"", "source_url":"https://acme.example/about",
            "need_evidence":"Published product documentation describes current workflow",
            "contact_basis":"Official business contact page",
            "current_product":"ExampleCRM Pro", "product_category":"CRM software",
            "buyer_evidence":"Organisation publicly documents active use of ExampleCRM Pro",
            "buyer_evidence_url":"https://acme.example/tools",
            "buyer_evidence_type":"self_declared",
            "evidence_checked_at":datetime.now(timezone.utc).isoformat(),
            "data_permission_basis":"Official public business contact route; use limited to relevant one-to-one enquiry",
            "contact_permission_status":"permitted_business_contact",
            "sri_product_match":"SRI CRM Starter", "sri_product_match_url":"https://sri.example/catalog/crm-starter",
            "permission_evidence_url":"https://acme.example/contact", "permission_checked_at":datetime.now(timezone.utc).isoformat(),
            "opt_out":0,
        }
        row.update(overrides)
        return row
    def write_csv(self, rows):
        path=Path(self.tmp.name)/"leads.csv"
        fields=list(self.buyer().keys())
        with path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
        return path
    def test_import_and_duplicate_domain(self):
        row=self.buyer()
        path=self.write_csv([row,{**row,"business_name":"Acme Ltd","website":"http://acme.example/"}])
        result=agent.import_csv(path)
        self.assertEqual(result["inserted"],1)
        self.assertEqual(result["duplicates"],1)
        with agent.connect() as db:
            saved=db.execute("SELECT current_product FROM leads").fetchone()
            self.assertEqual(saved["current_product"],"ExampleCRM Pro")
    def test_existing_buyer_with_permission_can_qualify(self):
        score,reasons=agent.score_lead(self.buyer())
        self.assertGreater(score,0)
        self.assertLessEqual(score,100)
        self.assertIn("required buyer, SRI product-match, and permission fields present; human validation still required",reasons)
    def test_generic_business_without_buyer_evidence_is_blocked(self):
        row=self.buyer(current_product="",product_category="",buyer_evidence="",buyer_evidence_url="",
                       buyer_evidence_type="",evidence_checked_at="")
        score,reasons=agent.score_lead(row)
        self.assertEqual(score,0)
        self.assertTrue(any("NOT_QUALIFIED" in reason for reason in reasons))
    def test_missing_permission_or_invalid_evidence_type_is_blocked(self):
        for changes in (
            {"contact_permission_status":"unknown"},
            {"data_permission_basis":""},
            {"permission_evidence_url":""},
            {"permission_checked_at":"2025-01-01T00:00:00+00:00"},
            {"buyer_evidence_type":"public_signal"},
        ):
            score,_=agent.score_lead(self.buyer(**changes))
            self.assertEqual(score,0)
    def test_missing_sri_catalogue_match_is_blocked(self):
        score,_=agent.score_lead(self.buyer(sri_product_match="",sri_product_match_url=""))
        self.assertEqual(score,0)
    def test_stale_buyer_evidence_is_blocked(self):
        score,_=agent.score_lead(self.buyer(evidence_checked_at="2025-01-01T00:00:00+00:00"))
        self.assertEqual(score,0)
    def test_opt_out_suppresses_score_and_draft(self):
        self.assertEqual(agent.score_lead(self.buyer(opt_out=1)),(0,["opt-out: suppressed"]))
        with agent.connect() as db:
            db.execute("INSERT INTO leads(business_name,opt_out,created_at,updated_at) VALUES('A',1,'x','x')")
        with self.assertRaises(ValueError): agent.draft_message(1)
    def test_unqualified_record_cannot_create_draft(self):
        with agent.connect() as db:
            db.execute("INSERT INTO leads(business_name,created_at,updated_at) VALUES('A','x','x')")
        with self.assertRaisesRegex(ValueError,"NOT_QUALIFIED"):
            agent.draft_message(1)
    def test_qualified_draft_never_sends(self):
        row=self.buyer()
        columns=list(row.keys())
        with agent.connect() as db:
            sql="INSERT INTO leads("+",".join(columns)+",created_at,updated_at) VALUES("+",".join("?" for _ in range(len(columns)+2))+")"
            db.execute(sql,[row[k] for k in columns]+["x","x"])
        with patch.object(agent,"ollama_generate",side_effect=agent.urllib.error.URLError("offline")):
            result=agent.draft_message(1)
        self.assertEqual(result["status"],"DRAFT")
        self.assertFalse(result["sender_invoked"])
        self.assertIn("same-category",result["body"])
    def test_legacy_database_gets_additive_migration(self):
        legacy=Path(self.tmp.name)/"legacy.sqlite3"
        original=agent.DB_PATH
        agent.DB_PATH=legacy
        with agent.connect() as db:
            db.execute("""CREATE TABLE leads (
              id INTEGER PRIMARY KEY AUTOINCREMENT, business_name TEXT NOT NULL,
              website TEXT DEFAULT '', niche TEXT DEFAULT '', country TEXT DEFAULT '',
              contact_name TEXT DEFAULT '', email TEXT DEFAULT '', phone TEXT DEFAULT '',
              source_url TEXT DEFAULT '', need_evidence TEXT DEFAULT '', contact_basis TEXT DEFAULT '',
              score INTEGER NOT NULL DEFAULT 0, score_reasons TEXT DEFAULT '[]',
              status TEXT NOT NULL DEFAULT 'NEW', opt_out INTEGER NOT NULL DEFAULT 0,
              next_followup_at TEXT DEFAULT '', created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
              UNIQUE(business_name, website))""")
            db.execute("INSERT INTO leads(business_name,created_at,updated_at) VALUES('Legacy','x','x')")
        agent.init_db()
        with agent.connect() as db:
            names={r["name"] for r in db.execute("PRAGMA table_info(leads)")}
            self.assertIn("current_product",names)
            self.assertIn("sri_product_match",names)
            self.assertIn("permission_evidence_url",names)
            self.assertEqual(db.execute("SELECT business_name FROM leads").fetchone()[0],"Legacy")
        agent.DB_PATH=original

if __name__=="__main__": unittest.main()
