#!/usr/bin/env python3
"""Generate a tiny, fail-closed micro-counter for real verification progress."""
from datetime import datetime, timezone
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TARGET=int(json.loads((ROOT/'config/independent-verification-target.json').read_text())['verification_target'])
registry=json.loads((ROOT/'generated/VERIFICATION-REGISTRY.json').read_text())
records=json.loads((ROOT/'generated/independent-verification-records.json').read_text())
promotion=json.loads((ROOT/'generated/VERIFICATION-PROMOTION-QC.json').read_text())
prepared=len(records.get('records',[])); reviewed=int(registry.get('reviewed',0)); verified=int(registry.get('verified',0)); slots=int(promotion.get('queue_records',0))
if not (0<=verified<=reviewed<=prepared<=TARGET): raise SystemExit('MICRO_COUNTER_FAIL: counter invariants violated')
remaining=TARGET-verified; pct=round(verified/TARGET*100,6); reviewed_pct=round(reviewed/TARGET*100,6)
signal='VERIFIED_PROGRESS' if verified>0 else 'NO_VERIFIED_PROGRESS_YET'
out={'generated_at':datetime.now(timezone.utc).isoformat(),'target':TARGET,'micro_counter':{'verified':verified,'reviewed':reviewed,'prepared':prepared,'concrete_review_slots':slots,'remaining_to_target':remaining},'percent':{'verified_of_target':pct,'reviewed_of_target':reviewed_pct,'remaining_of_target':round(100-pct,6)},'truth_signal':signal,'rule':'A workflow heartbeat never increments VERIFIED. Only an explicit independent reviewer decision can increment the VERIFIED counter.'}
outdir=ROOT/'generated'; (outdir/'micro-verification-counter.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
def bar(v,w=20): return '█'*round(w*v/100)+'░'*(w-round(w*v/100))
md='# ꙰ SHIRMANI Micro Verification Counter\n\n**%s / %s VERIFIED — %s%%**\n\n%s\n\n- Prepared: **%s**\n- Reviewed: **%s**\n- Concrete review slots: **%s**\n- Independently VERIFIED: **%s**\n- Remaining: **%s**\n- Signal: **%s**\n\n> Scheduled workflow activity does not increment this counter. Only an explicit independent-review decision can increment VERIFIED.\n' % (format(verified,','),format(TARGET,','),pct,bar(pct),format(prepared,','),format(reviewed,','),format(slots,','),format(verified,','),format(remaining,','),signal)
(outdir/'micro-verification-counter.md').write_text(md,encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
