"""Publishing status agent."""
import json
from pathlib import Path
def publish(out,status): Path(out,'factory-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
