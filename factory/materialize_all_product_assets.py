from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; OUT=ROOT/"products/production"
ENG={"calculator":"calculator","engineering":"calculator","text":"text","nlp":"text","knowledge":"text","seo":"seo","marketing":"seo","data":"data","files":"data","draw":"visual","pixel":"visual","visual":"visual","game":"game","quiz":"planner","productivity":"planner","time":"planner","research":"research","quality":"research","ai":"package","creator":"package","media":"package","commerce":"package","quantum":"quantum","access":"planner","nature":"package"}
TOOLS={
"calculator":'<input id=a type=number value=10><input id=b type=number value=5><select id=o><option>+</option><option>-</option><option>*</option><option>/</option><option>%</option></select><button onclick="run()">Run</button>',
"text":'<textarea id=x rows=8 placeholder="Text"></textarea><button onclick="run()">Analyze</button>',
"seo":'<input id=x placeholder="Title"><textarea id=y rows=6 placeholder="Description"></textarea><button onclick="run()">SEO</button>',
"data":'<textarea id=x rows=8 placeholder="JSON or CSV"></textarea><button onclick="run()">Inspect</button>',
"visual":'<textarea id=x rows=8 placeholder="Visual brief"></textarea><button onclick="run()">Build</button>',
"planner":'<input id=x placeholder="Topic"><textarea id=y rows=6 placeholder="Notes"></textarea><button onclick="run()">Plan</button>',
"research":'<input id=x placeholder="Claim"><input id=y placeholder="Source"><textarea id=z rows=6 placeholder="Evidence"></textarea><button onclick="run()">Research/QC</button>',
"package":'<textarea id=x rows=8 placeholder="Production brief"></textarea><button onclick="run()">Package</button>',
"quantum":'<select id=x><option>H</option><option>X</option><option>Z</option><option>CNOT</option></select><button onclick="run()">Simulate</button>',
"game":'<button onclick="run()">New Game</button><div id=b></div>'}
def visual_svg(p):
    """Create a product-specific 3840x2160 16:9 4K-ready pseudo-3D showroom visual."""
    pid=html.escape(str(p.get("id","")), quote=True)
    name=html.escape(str(p.get("name","Digital Product")), quote=True)
    family=html.escape(str(p.get("family",p.get("category","Digital Product"))), quote=True)
    engine=html.escape(str(p.get("engine","product")), quote=True)
    import hashlib
    h=hashlib.sha256(str(p.get("id","")).encode()).hexdigest()
    c1="#"+h[0:6]; c2="#"+h[6:12]; accent="#"+h[12:18]; uid="u"+h[:10]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-labelledby="{uid}t {uid}d">
<title id="{uid}t">{name} — SHIRMANI unique 4K product visual</title>
<desc id="{uid}d">Product-specific visual identity with a dimensional digital-product object, product ID, family and engine.</desc>
<defs>
 <linearGradient id="{uid}bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="#03060d"/></linearGradient>
 <linearGradient id="{uid}glass" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffffff" stop-opacity=".25"/><stop offset=".45" stop-color="#ffffff" stop-opacity=".07"/><stop offset="1" stop-color="#000000" stop-opacity=".35"/></linearGradient>
 <linearGradient id="{uid}edge" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f7d86a"/><stop offset=".5" stop-color="#67e8f9"/><stop offset="1" stop-color="#72e6aa"/></linearGradient>
 <radialGradient id="{uid}orb"><stop stop-color="{accent}" stop-opacity=".48"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
 <filter id="{uid}shadow"><feDropShadow dx="0" dy="34" stdDeviation="38" flood-opacity=".52"/></filter>
 <filter id="{uid}blur"><feGaussianBlur stdDeviation="42"/></filter>
</defs>
<rect width="3840" height="2160" fill="url(#{uid}bg)"/>
<circle cx="3150" cy="420" r="760" fill="url(#{uid}orb)" filter="url(#{uid}blur)"/>
<circle cx="680" cy="1770" r="520" fill="#67e8f9" opacity=".08" filter="url(#{uid}blur)"/>
<ellipse cx="2020" cy="1790" rx="1420" ry="210" fill="#000" opacity=".55" filter="url(#{uid}blur)"/>
<g filter="url(#{uid}shadow)">
 <path d="M520 1570 L760 650 L2850 470 L3350 1420 L1120 1735 Z" fill="url(#{uid}glass)" stroke="url(#{uid}edge)" stroke-width="14"/>
 <path d="M760 650 L1120 890 L3350 700 L2850 470 Z" fill="#ffffff" opacity=".10" stroke="#ffffff" stroke-opacity=".20" stroke-width="6"/>
 <path d="M1120 890 L1120 1735 L3350 1420 L3350 700 Z" fill="#000000" opacity=".18"/>
 <path d="M860 820 L1010 740 L2860 600 L3160 760 L1280 1010 Z" fill="#ffffff" opacity=".10"/>
 <path d="M900 1190 L2920 920" stroke="#67e8f9" stroke-opacity=".30" stroke-width="20"/>
 <path d="M900 1260 L2700 1010" stroke="#72e6aa" stroke-opacity=".18" stroke-width="12"/>
 <circle cx="2880" cy="1250" r="290" fill="none" stroke="#f7d86a" stroke-opacity=".45" stroke-width="12"/>
 <circle cx="2880" cy="1250" r="195" fill="none" stroke="#67e8f9" stroke-opacity=".30" stroke-width="8"/>
 <circle cx="2880" cy="1250" r="80" fill="{accent}" opacity=".22"/>
</g>
<text x="520" y="310" fill="#67e8f9" font-family="system-ui,sans-serif" font-size="76" font-weight="900" letter-spacing="10">꙰ SHIRMANI SUPREME DIGITAL PRODUCT</text>
<text x="520" y="760" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="132" font-weight="900">{name}</text>
<text x="520" y="900" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="62" font-weight="850">{family} · {engine}</text>
<rect x="520" y="980" width="620" height="118" rx="59" fill="#03060d" opacity=".82" stroke="#f7d86a" stroke-opacity=".55" stroke-width="5"/>
<text x="590" y="1060" fill="#f7d86a" font-family="system-ui,sans-serif" font-size="68" font-weight="900">{pid}</text>
<text x="520" y="1910" fill="#ffffff" opacity=".86" font-family="system-ui,sans-serif" font-size="44" font-weight="700" letter-spacing="3">UNIQUE PRODUCT IDENTITY · DIMENSIONAL 3D-STYLE · 3840×2160 · 16:9 · 4K-READY</text>
</svg>"""

def make(p):
 g=ENG.get(p["engine"],"package"); inp=TOOLS[g]
 data=json.dumps({k:p.get(k) for k in ["id","name","category","engine","price_inr","offer_price_inr","offer","description","guarantee","packing","qc_code","gate_no","dispatch_no"]},ensure_ascii=False)
 js=f"""const P={data};const O=x=>out.textContent=JSON.stringify(x,null,2);function run(){{let v=(document.getElementById('x')||{{value:''}}).value||'';O({{product_id:P.id,type:'{g.upper()}_PRODUCTION',input:v,qc_code:P.qc_code,gate_no:P.gate_no,dispatch_no:P.dispatch_no,status:'PRODUCED'}})}}"""
 if g=="calculator": js="""function run(){let a=+document.getElementById('a').value,b=+document.getElementById('b').value,o=document.getElementById('o').value,r=o=='+'?a+b:o=='-'?a-b:o=='*'?a*b:o=='/'?(b?a/b:'DIV0'):a%b;O({product_id:P.id,type:'CALCULATION',a,b,operation:o,result:r,status:'PRODUCED',qc_code:P.qc_code,gate_no:P.gate_no,dispatch_no:P.dispatch_no})}"""
 return f"""<!doctype html><html lang=hi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{html.escape(p['name'])}</title><style>body{{margin:0;background:#071018;color:#eef5f8;font:16px system-ui}}main{{max-width:1000px;margin:auto;padding:20px}}section{{background:#101923;border:1px solid #405466;border-radius:16px;padding:18px;margin:12px 0}}h1,h2{{color:#ffd84a}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px}}.m{{background:#081019;padding:12px;border-radius:9px}}input,textarea,select{{width:100%;box-sizing:border-box;padding:10px;margin:5px 0 10px;background:#081019;color:#fff;border:1px solid #405466;border-radius:8px}}button,a{{padding:10px 13px;border:0;border-radius:8px;background:#ffd84a;color:#111;font-weight:800;text-decoration:none;display:inline-block}}pre{{white-space:pre-wrap;background:#060b10;padding:12px}}</style><main><section style='padding:0;overflow:hidden'><div>{visual_svg(p)}</div></section><section><h1>꙰ {html.escape(p['name'])}</h1><p>{html.escape(p['description'])}</p><div class=grid><div class=m>Category<br><b>{html.escape(p['category'])}</b></div><div class=m>Base ₹{p['price_inr']}<br><b>Offer ₹{p['offer_price_inr']}</b></div><div class=m>Offer<br><b>{html.escape(p['offer'])}</b></div><div class=m>Product ID<br><b>{p['id']}</b></div></div></section><section><h2>QC Passport / QR Gate</h2><div class=grid><div class=m>QC<br><b>{p['qc_code']}</b></div><div class=m>Gate<br><b>{p['gate_no']}</b></div><div class=m>Dispatch<br><b>{p['dispatch_no']}</b></div><div class=m>Packing<br><b>{html.escape(p['packing'])}</b></div></div><p>Guarantee: {html.escape(p['guarantee'])}</p><div id=qr></div></section><section><h2>Working Product Module</h2>{inp}<pre id=out>Ready.</pre></section><section><h2>Showroom</h2><a href="../../products.html">All products</a> <a href="../production-launch-center.html?id={p['id']}">Launch Center</a></section></main><script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script><script>const out=document.getElementById('out');const P={data};const O=x=>out.textContent=JSON.stringify(x,null,2);new QRCode(document.getElementById('qr'),{{text:location.href+'|QC:{p['qc_code']}|GATE:{p['gate_no']}|DISPATCH:NO|PRICE:{p['offer_price_inr']}',width:150,height:150}});{js}</script></html>"""
def main():
 c=json.loads((GEN/"1000-digital-products.json").read_text(encoding="utf-8")); OUT.mkdir(parents=True,exist_ok=True)
 for p in c["products"]:(OUT/(p["id"].lower()+".html")).write_text(make(p),encoding="utf-8")
 s={"product_assets":len(c["products"]),"asset_directory":"products/production/","showroom":"products.html","state":"READY_FOR_QC","dispatch":"NO","principle":"Every catalog identity has a concrete browser product asset; QC/dispatch remain downstream."}
 (GEN/"concrete-product-asset-status.json").write_text(json.dumps(s,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
