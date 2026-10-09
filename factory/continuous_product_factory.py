#!/usr/bin/env python3
"""Continuous SHIRMANI product factory: 5,000 concrete browser products."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, html, json, os, re, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"products/continuous"; VIS=ROOT/"products/visuals/continuous"; DEM=ROOT/"products/demos/continuous"
STATE=ROOT/"generated/continuous-production-state.json"; MAN=ROOT/"generated/continuous-production-manifest.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
LOGO=BASE+"assets/shirmani-perspective-logo.svg"; COUNT=5000
ENGINES=[
("TEXT","Text Signal Extractor","text","Extract words, characters and lines."),
("DATA","CSV Insight Table","csv","Parse CSV into rows and columns."),
("JSON","JSON Schema Lens","json","Format and inspect JSON."),
("TIME","Time Zone Matrix","time","Compare local time and UTC."),
("URL","URL Inspector","url","Parse URL components."),
("COLOR","Contrast Studio","color","Preview a color value."),
("MARKDOWN","Markdown Previewer","markdown","Preview basic Markdown."),
("REGEX","Regex Test Bench","regex","Test a regular expression."),
("ENCODE","Base64 Utility","base64","Encode text as Base64."),
("HASH","SHA-256 Fingerprint","hash","Create a SHA-256 digest."),
("NUMBER","Precision Calculator","calc","Evaluate basic arithmetic."),
("DIFF","Text Difference Viewer","diff","Compare two text blocks."),
("CASE","Case Transformer","case","Transform text case."),
("UUID","UUID Studio","uuid","Generate UUID v4."),
("TIMESTAMP","Timestamp Converter","timestamp","Convert Unix timestamps."),
("HTML","HTML Escape Studio","html","Escape HTML entities."),
("SLUG","Slug Builder","slug","Create URL-friendly slugs."),
("PASSWORD","Password Strength Lens","password","Estimate strength locally."),
("META","SEO Meta Draft","meta","Draft description metadata."),
("UNITS","Unit Converter","units","Convert common length units.")
]
MODES=["Quick","Research","Creator","Developer","Business","Education","Public","Studio","Precision","Live"]
CONTEXTS=["Research","Product","Content","Data","Education","Publishing","Marketing","Engineering","Science","Documentation","Archive","Operations","Planning","Analysis","Presentation","Quality","Support","Web","Knowledge","Media","Finance","Projects","Reporting","Experiment","Workflow"]
def esc(x): return html.escape(str(x),quote=True)
def spec(n):
    ei=n//250; r=n%250; mi=r//25; ci=r%25
    code,name,kind,desc=ENGINES[ei]
    return {"id":"SRI-AUTO-%05d"%(n+1),"name":name+" — "+MODES[mi]+" "+CONTEXTS[ci],"engine":kind,"family":code,"mode":MODES[mi],"context":CONTEXTS[ci],"short_description":desc}
def visual(p):
    h=hashlib.sha256(p["id"].encode()).hexdigest(); c1="#"+h[:6]; c2="#"+h[6:12]; pid=p["id"]
    passport=BASE+"product-passport.html?id="+urllib.parse.quote(pid)
    qr="https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=8&data="+urllib.parse.quote(passport,safe="")
    return '<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160"><defs><linearGradient id="g"><stop stop-color="%s"/><stop offset=".6" stop-color="%s"/><stop offset="1" stop-color="#050910"/></linearGradient></defs><rect width="3840" height="2160" fill="url(#g)"/><rect x="25" y="25" width="3790" height="2110" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/><circle cx="280" cy="290" r="205" fill="#061016" stroke="#e7c85b" stroke-width="12"/><image href="%s" x="85" y="95" width="390" height="390"/><text x="545" y="150" fill="#e7c85b" font-family="system-ui" font-size="68" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text><text x="545" y="235" fill="white" font-family="system-ui" font-size="31" font-weight="800">Shiromani Rampal Saini · Impartial Understanding · Beyond Comparison · Beyond Time</text><text x="545" y="282" fill="white" font-family="system-ui" font-size="31" font-weight="800">Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present</text><text x="500" y="760" fill="#62e6ff" font-family="system-ui" font-size="70" font-weight="900">PRODUCT IDENTITY</text><text x="500" y="900" fill="white" font-family="system-ui" font-size="88" font-weight="900">%s</text><text x="500" y="1010" fill="#6ee7a8" font-family="system-ui" font-size="52" font-weight="800">%s · %s · %s</text><rect x="500" y="1080" width="650" height="105" rx="52" fill="#050910" stroke="#e7c85b" stroke-width="5"/><text x="560" y="1150" fill="#e7c85b" font-family="system-ui" font-size="55" font-weight="900">%s</text><text x="500" y="1280" fill="#62e6ff" font-family="system-ui" font-size="42" font-weight="800">SHORT DESCRIPTION · %s</text><rect x="2970" y="95" width="650" height="760" rx="45" fill="#fff"/><image href="%s" x="3060" y="180" width="470" height="470"/><text x="3060" y="725" fill="#050910" font-family="system-ui" font-size="38" font-weight="900">SCAN FOR LONG DETAILS</text><text x="500" y="2030" fill="#c8d0dc" font-family="system-ui" font-size="30">3840×2160 · 16:9 · 4K-ready · unique identity · production-first</text></svg>' % (c1,c2,LOGO,esc(p["name"]),esc(p["family"]),esc(p["mode"]),esc(p["context"]),pid,esc(p["short_description"]),qr)
def js(kind):
    pre="var o=document.getElementById('out'),v=document.getElementById('input').value,esc=function(s){return String(s).replace(/[&<>]/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[m]})};"
    c={"text":"o.innerHTML='Words: '+(v.trim()?v.trim().split(/\\s+/).length:0)+'<br>Characters: '+v.length+'<br>Lines: '+(v?v.split(/\\n/).length:0);","csv":"var r=v.trim()?v.trim().split(/\\n/).map(function(x){return x.split(',')}):[];o.innerHTML='Rows: '+r.length+'<br>Columns: '+(r[0]?r[0].length:0)+'<pre>'+esc(JSON.stringify(r.slice(0,20),null,2))+'</pre>';","json":"try{o.innerHTML='<pre>'+esc(JSON.stringify(JSON.parse(v),null,2))+'</pre>'}catch(e){o.textContent='Invalid JSON: '+e.message}","time":"o.textContent=new Date().toString()+' | UTC: '+new Date().toISOString();","url":"try{var u=new URL(v);o.innerHTML='Protocol: '+esc(u.protocol)+'<br>Host: '+esc(u.host)+'<br>Path: '+esc(u.pathname)+'<br>Query: '+esc(u.search)}catch(e){o.textContent='Enter a valid URL.'}","color":"o.innerHTML='<div style=\"height:90px;background:'+esc(v||'#fff')+'\"></div>Color: '+esc(v||'#fff');","markdown":"o.innerHTML=esc(v).replace(/^# (.*)$/gm,'<h2>$1</h2>').replace(/\\*\\*(.*?)\\*\\*/g,'<b>$1</b>').replace(/\\n/g,'<br>');","regex":"try{var a=v.split(/\\n/,2),m=(a[1]||'').match(new RegExp(a[0]||'','g'))||[];o.innerHTML='Matches: '+m.length+'<pre>'+esc(m.join('\\n'))+'</pre>'}catch(e){o.textContent=e.message}","base64":"try{o.textContent=btoa(unescape(encodeURIComponent(v)))}catch(e){o.textContent=e.message}","hash":"crypto.subtle.digest('SHA-256',new TextEncoder().encode(v)).then(function(b){o.textContent=Array.from(new Uint8Array(b)).map(function(x){return x.toString(16).padStart(2,'0')}).join('')});","calc":"try{o.textContent=Function('return ('+v.replace(/[^0-9+\\-*/().% ]/g,'')+')')()}catch(e){o.textContent='Invalid expression'}","diff":"var a=v.split(/\\n---\\n/);o.innerHTML='<pre>'+esc(a[0]||'')+'\\n---\\n'+esc(a[1]||'')+'</pre>';","case":"o.textContent=v.toLowerCase().replace(/\\b\\w/g,function(x){return x.toUpperCase()});","uuid":"o.textContent=crypto.randomUUID();","timestamp":"var d=new Date(v?Number(v)*1000:Date.now());o.textContent=isNaN(d)?'Invalid timestamp':d.toISOString();","html":"o.textContent=esc(v);","slug":"o.textContent=v.toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');","password":"var s=(v.length>=12?2:v.length>=8?1:0)+(/[A-Z]/.test(v)?1:0)+(/[a-z]/.test(v)?1:0)+(/[0-9]/.test(v)?1:0)+(/[^A-Za-z0-9]/.test(v)?1:0);o.textContent='Local heuristic score: '+s+'/6';","meta":"o.textContent='<meta name=\"description\" content=\"'+esc(v)+'\">';","units":"var n=Number(v);o.textContent=isFinite(n)?n+' m = '+(n*100).toFixed(2)+' cm = '+(n*3.28084).toFixed(3)+' ft':'Enter a number.'"}
    return pre+c.get(kind,"o.textContent='Engine ready.'")
def page(p):
    pid=p["id"]; passport=BASE+"product-passport.html?id="+urllib.parse.quote(pid); vis=BASE+"products/visuals/continuous/"+pid.lower()+".svg"; demo=BASE+"products/demos/continuous/"+pid.lower()+".html"
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s · %s</title><style>body{margin:0;background:#050910;color:#f5f7fb;font:16px/1.6 system-ui}main{max-width:1050px;margin:auto;padding:20px}.hero,.tool{background:#0d1722;border:1px solid #304457;border-radius:18px;padding:20px;margin:14px 0}.hero{border:2px solid #e7c85b}h1,h2{color:#e7c85b}textarea{width:100%%;box-sizing:border-box;padding:12px;background:#07111b;color:#fff;border:1px solid #3b556b;border-radius:10px}button,a{display:inline-block;padding:10px 14px;border-radius:10px;background:#e7c85b;color:#111;text-decoration:none;font-weight:900;border:0;margin:4px;cursor:pointer}pre{white-space:pre-wrap;background:#07111b;padding:14px;border-radius:10px}img{max-width:100%%;border-radius:14px}</style></head><body><main><section class="hero"><img src="%s" alt="%s"><h1>%s</h1><p>%s</p><p><b>%s</b> · %s · %s · %s</p><p>FREE PUBLIC TOOL · production-first · sale/payment not claimed</p><a href="%s">Product Passport</a><a href="%s">Interactive Demo</a></section><section class="tool"><h2>Live tool</h2><textarea id="input" rows="8" placeholder="Enter sample input…"></textarea><button onclick="run()">Run</button><div id="out" style="margin-top:12px"></div></section><section class="tool"><h2>Evidence boundary</h2><p>Concrete product artifact and customer-facing presentation. Independent scientific verification, sale, payment and dispatch are separate states.</p></section></main><script>function run(){%s}</script></body></html>' % (esc(p["name"]),pid,vis,esc(p["name"]),esc(p["name"]),esc(p["short_description"]),pid,esc(p["family"]),esc(p["mode"]),esc(p["context"]),passport,demo,js(p["engine"]))
def demo(p):
    return '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Demo · %s</title><style>body{margin:0;background:#050910;color:white;font:18px system-ui;display:grid;place-items:center;min-height:100vh}.card{width:min(900px,90vw);padding:32px;border:2px solid #e7c85b;border-radius:22px;background:#0d1722;text-align:center}.step{display:none;padding:25px;border-radius:15px;background:#07111b}.on{display:block}button{padding:12px 18px;border:0;border-radius:10px;background:#e7c85b;font-weight:900}</style></head><body><div class="card"><h1>Product Demo</h1><h2>%s</h2><div id="s1" class="step on">① Open the product and enter sample input.</div><div id="s2" class="step">② Run the tool and inspect the result.</div><div id="s3" class="step">③ Open Product Passport for long details and usage notes.</div><button onclick="next()">Next</button></div><script>var n=1;function next(){document.getElementById("s"+n).classList.remove("on");n=n%%3+1;document.getElementById("s"+n).classList.add("on")}</script></body></html>' % (esc(p["name"]),esc(p["name"]))
def main():
    for d in (OUT,VIS,DEM): d.mkdir(parents=True,exist_ok=True)
    existing={x.stem.upper() for x in OUT.glob("*.html")}; batch=max(1,min(25,int(os.environ.get("PRODUCT_BATCH","12")))); made=[]
    for n in range(COUNT):
        p=spec(n)
        if p["id"] in existing: continue
        (OUT/(p["id"].lower()+".html")).write_text(page(p),encoding="utf-8")
        (VIS/(p["id"].lower()+".svg")).write_text(visual(p),encoding="utf-8")
        (DEM/(p["id"].lower()+".html")).write_text(demo(p),encoding="utf-8")
        made.append(p)
        if len(made)>=batch: break
    rows=[]
    for f in sorted(OUT.glob("*.html")):
        n=int(f.stem.upper().split("-")[-1])-1; p=spec(n)
        rows.append({**p,"product_url":BASE+str(f.relative_to(ROOT)).replace("\\","/"),"visual_url":BASE+str((VIS/(f.stem+".svg")).relative_to(ROOT)).replace("\\","/"),"demo_url":BASE+str((DEM/(f.stem+".html")).relative_to(ROOT)).replace("\\","/"),"state":"PRODUCED_PUBLIC"})
    now=datetime.now(timezone.utc).isoformat()
    MAN.write_text(json.dumps({"schema_version":1,"generated_at":now,"target":COUNT,"concrete_products":len(rows),"remaining_to_5000":COUNT-len(rows),"created_this_cycle":len(made),"engine_families":len(ENGINES),"modes":len(MODES),"contexts":len(CONTEXTS),"demo_route":"product-specific interactive HTML; MP4 rendering is a separate media factory","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    STATE.write_text(json.dumps({"generated_at":now,"target":COUNT,"concrete_products":len(rows),"remaining_to_5000":COUNT-len(rows),"created_this_cycle":len(made),"production_first":True,"latest_ids":[p["id"] for p in made],"truth_boundary":"Generated artifacts are not automatically independently scientifically verified."},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"created_this_cycle":len(made),"concrete_products":len(rows),"remaining_to_5000":COUNT-len(rows)}))
if __name__=="__main__": main()
