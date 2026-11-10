import csv, tempfile, unittest
from pathlib import Path
import lead_agent as agent

class LeadAgentTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        agent.DB_PATH=Path(self.tmp.name)/"test.sqlite3"
        agent.init_db()
    def tearDown(self): self.tmp.cleanup()
    def write_csv(self, rows):
        path=Path(self.tmp.name)/"leads.csv"
        fields=["business_name","website","niche","country","contact_name","email","phone","source_url","need_evidence","contact_basis"]
        with path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
        return path
    def test_import_and_duplicate_domain(self):
        row={"business_name":"Acme","website":"https://www.acme.example","niche":"education","email":"sales@acme.example","need_evidence":"published tender","contact_basis":"official site"}
        path=self.write_csv([row,{"business_name":"Acme Ltd","website":"http://acme.example/","email":"other@acme.example"}])
        result=agent.import_csv(path)
        self.assertEqual(result["inserted"],1)
        self.assertEqual(result["duplicates"],1)
    def test_score_is_explainable_and_bounded(self):
        row={"business_name":"A","niche":"education","need_evidence":"need","website":"https://a.example","email":"a@a.example","phone":"","contact_basis":"official page","opt_out":0}
        score,reasons=agent.score_lead(row)
        self.assertEqual(score,100); self.assertEqual(len(reasons),5)
    def test_opt_out_suppresses_score_and_draft(self):
        row={"business_name":"A","niche":"","need_evidence":"","website":"","email":"","phone":"","contact_basis":"","opt_out":1}
        self.assertEqual(agent.score_lead(row),(0,["opt-out: suppressed"]))
        with agent.connect() as db:
            db.execute("INSERT INTO leads(business_name,opt_out,created_at,updated_at) VALUES('A',1,'x','x')")
        with self.assertRaises(ValueError): agent.draft_message(1)
    def test_draft_never_sends(self):
        with agent.connect() as db:
            db.execute("INSERT INTO leads(business_name,niche,created_at,updated_at) VALUES('A','education','x','x')")
        result=agent.draft_message(1)
        self.assertEqual(result["status"],"DRAFT")
        self.assertFalse(result["sender_invoked"])

if __name__=="__main__": unittest.main()
