#!/usr/bin/env node
/**
 * SHIRMANI Supreme Product Visual Factory
 * Produces deterministic 3840x2160 (4K-ready) SVG identity cards for every
 * concrete product module. Visuals are product assets, not scientific evidence.
 */
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const ROOT=process.cwd(), SRC=path.join(ROOT,"products","concrete"), OUT=path.join(ROOT,"products","visuals");
fs.mkdirSync(OUT,{recursive:true});

const esc=s=>String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
function hash(s){return crypto.createHash("sha256").update(String(s)).digest("hex");}
function hue(hex,offset){return (parseInt(hex.slice(offset,offset+6),16)%360+360)%360;}
function pickMeta(html,id){
  const title=(html.match(/<h1[^>]*>([\\s\\S]*?)<\\/h1>/i)?.[1]||html.match(/<title[^>]*>([\\s\\S]*?)<\\/title>/i)?.[1]||("SHIRMANI Digital Product "+id))
    .replace(/<[^>]+>/g,"").replace(/&amp;/g,"&").replace(/&#x27;/g,"'").trim();
  const category=(html.match(/Category<\\/?(?:br|b)?[^>]*>\\s*<b>([\\s\\S]*?)<\\/b>/i)?.[1]||
    html.match(/Category[^<]*<b>([\\s\\S]*?)<\\/b>/i)?.[1]||"Digital Product").replace(/<[^>]+>/g,"").trim();
  const engine=(html.match(/Engine[^<]*<b>([\\s\\S]*?)<\\/b>/i)?.[1]||"supreme").replace(/<[^>]+>/g,"").trim();
  const price=(html.match(/(?:Offer price|Price)[^<]*<b>₹?([0-9,]+)/i)?.[1]||"0").replace(/,/g,"");
  const qc=(html.match(/QC[^<]*<b>([^<]+)<\\/b>/i)?.[1]||"QC-PROD-"+id).trim();
  const gate=(html.match(/Gate[^<]*<b>([^<]+)<\\/b>/i)?.[1]||"GATE-PRODUCTION").trim();
  const key=hash(id+"|"+title+"|"+category+"|"+engine), a=hue(key,0), b=hue(key,6), c=hue(key,12);
  return {id,title,category,engine,price,qc,gate,a,b,c,key};
}
function svg(m){
 const uid=m.key.slice(0,12), title=esc(m.title.slice(0,52)), cat=esc(m.category.slice(0,32)), eng=esc(m.engine.slice(0,28));
 const objectKind=m.engine.toLowerCase().includes("calculator")?"CALCULATOR":
   m.engine.toLowerCase().includes("nlp")||m.engine.toLowerCase().includes("text")?"NLP":
   m.engine.toLowerCase().includes("research")?"RESEARCH":
   m.engine.toLowerCase().includes("marketing")?"MARKETING":
   m.engine.toLowerCase().includes("audio")?"AUDIO":"DIGITAL";
 return `<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-labelledby="title desc">
<title id="title">${title} — SHIRMANI 4K product visual</title><desc id="desc">Unique 4K-ready product identity for ${m.id}, ${cat}, ${eng}. Deterministic visual fingerprint ${m.key.slice(0,16)}.</desc>
<defs>
 <linearGradient id="${uid}g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="hsl(${m.a},78%,30%)"/><stop offset=".5" stop-color="hsl(${m.b},70%,12%)"/><stop offset="1" stop-color="hsl(${m.c},72%,5%)"/></linearGradient>
 <linearGradient id="${uid}glass" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#fff" stop-opacity=".24"/><stop offset="1" stop-color="#fff" stop-opacity=".035"/></linearGradient>
 <radialGradient id="${uid}orb"><stop stop-color="#fff" stop-opacity=".30"/><stop offset=".35" stop-color="hsl(${m.a},90%,70%)" stop-opacity=".24"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <filter id="${uid}blur"><feGaussianBlur stdDeviation="38"/></filter><filter id="${uid}shadow"><feDropShadow dx="0" dy="28" stdDeviation="32" flood-opacity=".48"/></filter>
</defs>
<rect width="3840" height="2160" fill="#03060d"/><rect x="70" y="70" width="3700" height="2020" rx="120" fill="url(#${uid}g)"/>
<circle cx="3180" cy="410" r="760" fill="url(#${uid}orb)"/><circle cx="640" cy="1790" r="620" fill="hsl(${m.b},90%,65%)" opacity=".08" filter="url(#${uid}blur)"/>
<g filter="url(#${uid}shadow)"><path d="M430 1780 L760 410 L3090 330 L3460 1680 Z" fill="url(#${uid}glass)" stroke="#e8c85c" stroke-opacity=".60" stroke-width="12"/>
<path d="M760 410 L1110 690 L3460 590 L3090 330 Z" fill="#fff" opacity=".08"/><path d="M1110 690 L1110 1600 L3460 1680 L3460 590 Z" fill="#000" opacity=".18"/></g>
<g transform="translate(2850 1130)"><circle r="370" fill="#03060d" opacity=".72" stroke="#e8c85c" stroke-width="12"/><circle r="285" fill="none" stroke="#64ddff" stroke-opacity=".48" stroke-width="10"/><circle r="205" fill="none" stroke="#70e6a0" stroke-opacity=".34" stroke-width="8"/><circle r="110" fill="hsl(${m.a},85%,62%)" opacity=".20"/><text text-anchor="middle" y="-12" fill="#fff" font-family="system-ui,sans-serif" font-size="62" font-weight="950">${objectKind}</text><text text-anchor="middle" y="78" fill="#e8c85c" font-family="system-ui,sans-serif" font-size="38" font-weight="800">${esc(m.id)}</text></g>
<text x="520" y="790" fill="#64ddff" font-family="system-ui,sans-serif" font-size="78" font-weight="950" letter-spacing="10">꙰ SHIRMANI SUPREME DIGITAL PRODUCT</text>
<text x="520" y="1100" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="136" font-weight="950">${title}</text>
<text x="520" y="1260" fill="#70e6a0" font-family="system-ui,sans-serif" font-size="64" font-weight="850">${cat} · ${eng}</text>
<rect x="520" y="1370" width="710" height="116" rx="58" fill="#03060d" opacity=".82" stroke="#e8c85c" stroke-opacity=".52" stroke-width="5"/><text x="585" y="1448" fill="#e8c85c" font-family="system-ui,sans-serif" font-size="66" font-weight="950">${esc(m.id)} · ₹${esc(Number(m.price||0).toLocaleString("en-IN"))}</text>
<text x="520" y="1590" fill="#fff" opacity=".88" font-family="system-ui,sans-serif" font-size="40" font-weight="750">3840×2160 · 16:9 · 4K-READY · UNIQUE PRODUCT VISUAL</text>
<text x="520" y="1660" fill="#fff" opacity=".62" font-family="system-ui,sans-serif" font-size="34">QC ${esc(m.qc)} · GATE ${esc(m.gate)} · PRODUCT IDENTITY FINGERPRINT ${m.key.slice(0,16)}</text>
<rect x="155" y="155" width="3530" height="1850" rx="95" fill="none" stroke="#e8c85c" stroke-opacity=".72" stroke-width="9"/></svg>`;
}
const files=fs.readdirSync(SRC).filter(f=>/^SP-\\d+\\.html$/i.test(f)).sort();
let written=0,skipped=0;
for(const file of files){
 const id=path.basename(file,".html").toUpperCase(), out=path.join(OUT,id.toLowerCase()+".svg");
 const m=pickMeta(fs.readFileSync(path.join(SRC,file),"utf8"),id);
 fs.writeFileSync(out,svg(m),"utf8"); written++;
}
const manifest={generated_at:new Date().toISOString(),source:"products/concrete/*.html",visual_directory:"products/visuals",format:"SVG 3840x2160 16:9 4K-ready",concrete_products:files.length,visuals_written:written,principle:"Every concrete product receives a deterministic product-specific public visual identity; visual quality is presentation metadata, not independent scientific verification."};
fs.writeFileSync(path.join(OUT,"manifest.json"),JSON.stringify(manifest,null,2)+"\n");
console.log(JSON.stringify(manifest,null,2));
