#!/usr/bin/env python3
import json,html,hashlib,urllib.parse
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
BATCH=100
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-"
FAMILIES=[
("Counting & Math","calculator","Smart Calculator Lab"),
("Text & Language","text","Quick Text & Language Lab"),
("Conversion","converter","Universal Unit Converter Lab"),
("Data & JSON","json","JSON Formatter Lab"),
("Color & Design","color","Color Palette Studio"),
("Markdown & Writing","markdown","Markdown Preview Studio"),
("Regex & Developer","regex","Regex Pattern Lab"),
("Date & Time","date","Date Difference Lab"),
("Numbers & Bases","base","Base Conversion Lab"),
("Percentages","percent","Percentage Lab"),
("CSV & Tables","csv","CSV Analyzer Lab"),
("Planning","plan","Task Planning Studio")]
def esc(x): return html.escape(str(x or ""),quote=True)
def mkprice(i): return 79+(i*37)%221
def mkdesc(i,f): return f"Customer-facing {f[0].lower()} tool for practical digital work. Product {i:04d} is reusable, browser-based and publicly accessible."
def module(f):
 e=f[1]
 fields={
 "calculator":'<input id="a" type="number" value="10"><select id="op"><option>+</option><option>-</option><option>*</option><option>/</option></select><input id="b" type="number" value="5">',
 "text":'<textarea id="x" rows="7" placeholder="Paste text…"></textarea>',
 "converter":'<input id="x" type="number" value="1"><select id="a"><option>m</option><option>cm</option><option>km</option><option>ft</option><option>in</option></select><select id="b"><option>cm</option><option>m</option><option>km</option><option>ft</option></select>',
 "json":'<textarea id="x" rows="7">{"hello":"world"}</textarea>',
 "color":'<input id="n" type="number" value="5" min="1" max="12">',
 "markdown":'<textarea id="x" rows="7"># Hello\n**SHIRMANI**</textarea>',
 "regex":'<input id="p" value="\\b\\w+\\b"><textarea id="x" rows="5">Sample text</textarea>',
 "date":'<input id="a" type="date"><input id="b" type="date">',
 "base":'<input id="x" value="FF"><input id="a" type="number" value="16"><input id="b" type="number" value="10">',
 "percent":'<input id="a" type="number" value="20"><input id="b" type="number" value="500">',
 "csv":'<textarea id="x" rows="7">name,value\nA,10\nB,20</textarea>',
 "plan":'<textarea id="x" rows="7" placeholder="Describe the objective…"></textarea>'}[e]
 return fields
def js(e):
 c='const v=id=>document.getElementById(id)?.value||"";const out=x=>document.getElementById("out").textContent=JSON.stringify({product_id:PID,engine:ENGINE,production_state:"PRODUCED",...x},null,2);'
 return c+{
 "calculator":'function run(){let a=+v("a"),b=+v("b"),o=v("op");out({type:"CALCULATION",a,b,operation:o,result:o=="+"?a+b:o=="-"?a-b:o=="*"?a*b:b?a/b:"DIV0"})}',
 "text":'function run(){let x=v("x");out({type:"TEXT_ANALYSIS",characters:x.length,words:(x.match(/\\S+/g)||[]).length,lines:x?x.split(/\\n/).length:0})}',
 "converter":'function run(){let x=+v("x"),a=v("a"),b=v("b"),m={m:1,cm:.01,km:1000,ft:.3048,in:.0254};out({type:"UNIT_CONVERSION",value:x,from:a,to:b,result:x*m[a]/m[b]})}',
 "json":'function run(){try{out({type:"JSON_FORMAT",valid:true,value:JSON.parse(v("x"))})}catch(e){out({type:"JSON_FORMAT",valid:false,error:e.message})}}',
 "color":'function run(){let n=Math.max(1,Math.min(12,+v("n")||5)),a=[];for(let i=0;i<n;i++)a.push("#"+Math.floor(Math.random()*16777215).toString(16).padStart(6,"0"));out({type:"COLOR_PALETTE",colors:a})}',
 "markdown":'function run(){let x=v("x");out({type:"MARKDOWN_PREVIEW",source:x,html:x.replace(/^# (.*)$/gm,"<h1>$1</h1>").replace(/\\*\\*(.*?)\\*\\*/g,"<strong>$1</strong>")})}',
 "regex":'function run(){try{let r=new RegExp(v("p"),"g");out({type:"REGEX_TEST",valid:true,matches:v("x").match(r)||[]})}catch(e){out({type:"REGEX_TEST",valid:false,error:e.message})}}',
 "date":'function run(){out({type:"DATE_DIFFERENCE",days:Math.round(Math.abs(new Date(v("b"))-new Date(v("a")))/86400000)})}',
 "base":'function run(){try{out({type:"BASE_CONVERSION",result:parseInt(v("x"),+v("a")).toString(+v("b")).toUpperCase()})}catch(e){out({type:"BASE_CONVERSION",error:e.message})}}',
 "percent":'function run(){out({type:"PERCENTAGE",percent:+v("a"),base:+v("b"),value:(+v("a")*+v("b"))/100})}',
 "csv":'function run(){let r=v("x").trim().split(/\\n/).filter(Boolean).map(x=>x.split(","));out({type:"CSV_ANALYSIS",rows:r.length,columns:Math.max(0,...r.map(x=>x.length)),headers:r[0]||[]})}',
 "plan":'function run(){out({type:"PLAN",objective:v("x"),steps:["objective","inputs","execute","QC","archive"]})}'
 }[e]
def page(p):
 return f'''<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(p["name"])}</title><style>body{{margin:0;background:#060b12;color:#f4f7fb;font:16px system-ui;line-height:1.6}}main{{max-width:1100px;margin:auto;padding:18px}}section{{background:#101923;border:1px solid #34485b;border-radius:18px;padding:18px;margin:12px 0}}h1,h2{{color:#f2cf58}}input,textarea,select{{width:100%;box-sizing:border-box;background:#081019;color:#fff;padding:10px;border:1px solid #405466;border-radius:9px;margin:5px 0}}button,a{{padding:10px 13px;background:#f2cf58;color:#111;border:0;border-radius:9px;font-weight:900;text-decoration:none;display:inline-block;margin:4px;cursor:pointer}}pre{{white-space:pre-wrap;background:#05090e;padding:12px;border-radius:10px}}.muted{{color:#aeb9c8}}</style></head><body><main><section><h1>꙰ {esc(p["name"])}</h1><p class="muted">{esc(p["description"])}</p><b>{p["id"]}</b> · {esc(p["category"])} · ₹{p["price_inr"]}</section><section><h2>QC / Gate / Dispatch</h2><p>QC: <b>{p["qc_code"]}</b> · Gate: <b>{p["gate_no"]}</b> · Dispatch: <b>NO</b></p></section><section><h2>Working Product Module</h2>{module(next(f for f in FAMILIES if f[1]==p["engine"]))}<br><button onclick="run()">Run Product</button><pre id="out">Ready.</pre></section><section><a href="../../showroom-public-interface.html">Showroom</a><a href="../../product-passport.html?id={p["id"]}">Product Passport</a><a href="../../products/visuals/{p["id"].lower()}.svg">4K Product Visual</a></section></main><script>const PID="{p["id"]}",ENGINE="{p["engine"]}";{js(p["engine"])}</script></body></html>'''
def visual(p):
 pid=p["id"];h=int(hashlib.sha256(pid.encode()).hexdigest()[:6],16);c1=f"hsl({h%360},78%,25%)";c2=f"hsl({h//7%360},72%,10%)";url=f"{BASE}/product-passport.html?id={pid}";qr="https://api.qrserver.com/v1/create-qr-code/?size=430x430&data="+urllib.parse.quote(url,safe="")
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs><rect width="3840" height="2160" fill="url(#g)"/><rect x="70" y="70" width="3700" height="2020" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/><circle cx="360" cy="360" r="205" fill="#061016" stroke="#e7c85b" stroke-width="14"/><image href="{BASE}/assets/shirmani-perspective-logo.svg" x="175" y="175" width="370" height="370"/><text x="360" y="640" text-anchor="middle" fill="#f6d35f" font-size="40" font-weight="900">Shiromani Rampal Saini</text><text x="360" y="692" text-anchor="middle" fill="#fff" font-size="22" font-weight="700">SHIRMANI HEART-VIEW · IMPARTIAL UNDERSTANDING</text><text x="360" y="730" text-anchor="middle" fill="#d9e3ef" font-size="18">Beyond Comparison · Beyond Time · Beyond Words · Beyond Love</text><text x="360" y="764" text-anchor="middle" fill="#d9e3ef" font-size="18">Eternal · Real · Natural Truth · Directly Present</text><text x="610" y="190" fill="#66ddff" font-size="52" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text><rect x="3160" y="120" width="570" height="690" rx="44" fill="#061016" stroke="#e7c85b" stroke-width="10"/><text x="3270" y="210" fill="#fff" font-size="42" font-weight="900">LONG DESCRIPTION</text><text x="3400" y="260" fill="#fff" font-size="42" font-weight="900">/ PRODUCT DETAILS</text><rect x="3250" y="300" width="390" height="390" fill="#fff"/><image href="{qr}" x="3260" y="310" width="370" height="370"/><text x="3290" y="750" fill="#66ddff" font-size="27" font-weight="900">SCAN FOR LONG DESCRIPTION</text><text x="520" y="820" fill="#66ddff" font-size="76" font-weight="900">{pid}</text><text x="520" y="1040" fill="#fff" font-size="112" font-weight="900">{esc(p["name"])}</text><text x="520" y="1170" fill="#72e6aa" font-size="62" font-weight="800">{esc(p["category"])} · {esc(p["engine"])}</text><text x="520" y="1290" fill="#fff" font-size="43" font-weight="650">SHORT DESCRIPTION · {esc(p["description"])}</text><rect x="520" y="1450" width="730" height="125" rx="62" fill="#03060d" stroke="#e7c85b" stroke-width="5"/><text x="590" y="1535" fill="#fff" font-size="62" font-weight="900">₹{p["price_inr"]}</text><text x="520" y="1770" fill="#fff" font-size="35" font-weight="800">4K · UNIQUE PRODUCT IDENTITY · SHORT DESCRIPTION + QR LONG DESCRIPTION</text><text x="520" y="1840" fill="#e7c85b" font-size="32" font-weight="700">QC · {p["qc_code"]} · GATE · {p["gate_no"]} · DISPATCH · NO</text></svg>'''
def main():
 now=datetime.now(timezone.utc).isoformat();ov=json.loads((ROOT/"generated/concrete-production-overlay.json").read_text());st=json.loads((ROOT/"generated/live-production-state.json").read_text());ms=json.loads((ROOT/"generated/multi-layer-production-status.json").read_text())
 target=int(st.get("five_thousand_scale_target",5000));start=int(st.get("concrete_repository_assets",len(ov.get("products",[]))))+1;end=min(target,start+BATCH-1);new=[]
 for i in range(start,end+1):
  f=FAMILIES[(i-1)%len(FAMILIES)];pid=f"SP-{i:04d}";p={"id":pid,"category":f[0],"engine":f[1],"name":f"SHIRMANI {f[2]} {i:04d}","description":mkdesc(i,f),"price_inr":mkprice(i),"offer_price_inr":mkprice(i),"offer":"PUBLIC LAUNCH PRICE","production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","artifact_url":f"products/concrete/{pid}.html","asset_path":f"products/visuals/{pid.lower()}.svg","qc_code":f"QC-PROD-{pid}","gate_no":"GATE-PRODUCTION","dispatch_no":"NO","production_batch":"BATCH-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),"produced_at":now}
  (ROOT/"products/concrete"/f"{pid}.html").write_text(page(p),encoding="utf-8");(ROOT/"products/visuals"/f"{pid.lower()}.svg").write_text(visual(p),encoding="utf-8");new.append(p)
 if not new:return
 ov["products"]=ov.get("products",[])+new;ov["produced_count"]=len(ov["products"]);ov["remaining_count"]=target-len(ov["products"]);ov["generated_at"]=now
 st.update({"generated_at":now,"concrete_repository_assets":len(ov["products"]),"current_catalog_pending":max(0,target-len(ov["products"])),"remaining_to_scale_target":max(0,target-len(ov["products"])),"concrete_materialization_percent_of_scale_target":round(100*len(ov["products"])/target,2),"module_products_generated":len(ov["products"]),"state":"PRODUCTION_IN_PROGRESS"})
 ms["generated_at"]=now;ms["last_cycle_tasks"]=len(new);ms["last_cycle_concrete_results"]=len(new);ms["scheduled_work_units"]=int(ms.get("scheduled_work_units",0))+len(new);ms.setdefault("production_outputs",{}).update({"concrete_results_this_cycle":len(new),"production_modules":len(ov["products"]),"verified_records":0})
 passfile=ROOT/"generated/PRODUCT-PASSPORTS.jsonl";seen=set()
 if passfile.exists():
  for line in passfile.read_text(encoding="utf-8").splitlines():
   try:seen.add(json.loads(line).get("id"))
   except:pass
 with passfile.open("a",encoding="utf-8") as f:
  for p in new:
   if p["id"] not in seen:f.write(json.dumps(p,ensure_ascii=False)+"\n")
 (ROOT/"generated/production-batch-report.json").write_text(json.dumps({"generated_at":now,"batch_size":len(new),"first_product":new[0]["id"],"last_product":new[-1]["id"],"remaining_to_5000":max(0,target-len(ov["products"])),"production_first":True,"verification":"downstream"},indent=2)+"\n")
 (ROOT/"generated/concrete-production-overlay.json").write_text(json.dumps(ov,ensure_ascii=False,indent=2)+"\n");(ROOT/"generated/live-production-state.json").write_text(json.dumps(st,ensure_ascii=False,indent=2)+"\n");(ROOT/"generated/multi-layer-production-status.json").write_text(json.dumps(ms,ensure_ascii=False,indent=2)+"\n")
 print("PRODUCED",len(new),"TOTAL",len(ov["products"]),"REMAINING",max(0,target-len(ov["products"])))
if __name__=="__main__":main()
