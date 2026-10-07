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
    pid=html.escape(str(p.get("id","")), quote=True)
    name=html.escape(str(p.get("name","Digital Product")), quote=True)
    family=html.escape(str(p.get("family",p.get("category","Digital Product"))), quote=True)
    engine=html.escape(str(p.get("engine","product")), quote=True)
    import hashlib
    h=hashlib.sha256(str(p.get("id","")).encode()).hexdigest()
    c1="#"+h[0:6]; c2="#"+h[6:12]; accent="#"+h[12:18]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-label="{name} product visual">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient><filter id="s"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-opacity=".35"/></filter></defs>
<rect width="1200" height="650" fill="#060b12"/><rect x="35" y="35" width="1130" height="580" rx="42" fill="url(#g)" opacity=".96" filter="url(#s)"/>
<circle cx="1010" cy="145" r="90" fill="{accent}" opacity=".25"/><circle cx="1080" cy="225" r="145" fill="#fff" opacity=".08"/>
<path d="M90 510 C280 410 330 590 510 470 S800 420 1100 505" fill="none" stroke="#fff" stroke-width="5" opacity=".28"/>
<text x="90" y="105" fill="#fff" font-family="system-ui,sans-serif" font-size="28" font-weight="800">꙰ SHIRMANI DIGITAL PRODUCT</text>
<text x="90" y="205" fill="#fff" font-family="system-ui,sans-serif" font-size="54" font-weight="900">{name}</text>
<text x="90" y="265" fill="#fff" font-family="system-ui,sans-serif" font-size="25" opacity=".9">{family} · {engine}</text>
<rect x="90" y="325" width="330" height="64" rx="32" fill="#060b12" opacity=".72"/><text x="125" y="367" fill="#fff" font-family="system-ui,sans-serif" font-size="24" font-weight="800">{pid}</text>
<text x="90" y="565" fill="#fff" font-family="system-ui,sans-serif" font-size="22" opacity=".9">PRODUCT IDENTITY · PRIME DIGITAL PACK</text>
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
