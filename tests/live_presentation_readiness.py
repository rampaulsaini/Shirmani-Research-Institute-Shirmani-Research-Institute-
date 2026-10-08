import json
from pathlib import Path

cfg = json.loads(Path('config/live-presentation-profile.json').read_text(encoding='utf-8'))
required = ['profile_id','portrait_asset_ref','voice_provider','voice_authorization_ref','content_policy_version','test_qa_status','lip_sync_status','preview_status','live_publish_status','last_verified_at']
blocked = [f'missing:{k}' for k in required if k not in cfg]
if not cfg.get('portrait_asset_ref'): blocked.append('portrait_asset_not_authorized')
if not cfg.get('voice_provider'): blocked.append('voice_provider_not_configured')
if not cfg.get('voice_authorization_ref'): blocked.append('voice_authorization_ref_missing')
if cfg.get('test_qa_status') != 'PASS': blocked.append('test_qa_not_passed')
if cfg.get('lip_sync_status') != 'PASS': blocked.append('lip_sync_not_passed')
if cfg.get('preview_status') != 'PASS': blocked.append('preview_not_passed')
if cfg.get('live_publish_status') != 'READY': blocked.append('live_publish_not_ready')
state = 'LIVE-READY' if not blocked else 'NOT LIVE-READY'
out = {'profile_id': cfg.get('profile_id'), 'state': state, 'blocked_reasons': blocked, 'truth_boundary': 'No live publication is declared without execution evidence.'}
Path('generated').mkdir(exist_ok=True)
Path('generated/live-presentation-readiness.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))
print('LIVE_PRESENTATION_GATE:', state)
