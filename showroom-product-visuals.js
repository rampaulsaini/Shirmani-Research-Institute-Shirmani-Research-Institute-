(function(){
"use strict";
const esc=s=>String(s??"").replace(/[&<>"]/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]));
async function loadJsonl(path){
  const r=await fetch(path+"?ts="+Date.now(),{cache:"no-store"});
  if(!r.ok) throw Error(r.status);
  return (await r.text()).split(/\n/).filter(Boolean).map(x=>JSON.parse(x));
}
function passportUrl(id){return new URL("product-passport.html?id="+encodeURIComponent(id),location.href).href}
function decorate(){
  document.querySelectorAll("#grid .card").forEach(card=>{
    if(card.dataset.identityVisual==="1") return;
    const muted=card.querySelector(".muted");
    if(!muted) return;
    const m=muted.textContent.match(/\bSP-\d{4,}\b/);
    if(!m) return;
    const p=window.__SHIRMANI_PRODUCTS?.get(m[0]);
    if(!p || !window.SHIRMANI_PRODUCT_VISUAL) return;
    card.dataset.identityVisual="1";
    const wrap=document.createElement("div");
    wrap.className="sri-visual-wrap";
    wrap.style.cssText="position:relative;border-radius:14px;overflow:hidden;border:1px solid #30445a;background:#060b12;margin-bottom:6px";
    const img=document.createElement("img");
    img.src=window.SHIRMANI_PRODUCT_VISUAL.visual(p);
    img.alt=(p.name||p.id)+" — 4K unique product visual";
    img.loading="lazy";
    img.style.cssText="display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover";
    wrap.appendChild(img);
    const qrBox=document.createElement("div");
    qrBox.style.cssText="position:absolute;right:12px;bottom:12px;width:104px;padding:7px;background:#fff;border-radius:10px;box-shadow:0 8px 25px #0009;z-index:2";
    const q=document.createElement("div"); qrBox.appendChild(q);
    const label=document.createElement("div");
    label.textContent="QR • LONG DESCRIPTION";
    label.style.cssText="font:800 8px/1.2 system-ui,sans-serif;color:#111;text-align:center;margin-top:4px";
    qrBox.appendChild(label); wrap.appendChild(qrBox);
    card.insertBefore(wrap,card.firstChild);
    if(window.QRCode)new QRCode(q,{text:passportUrl(p.id)+"|PRODUCT:"+p.id+"|QC:"+(p.qc_code||"PENDING")+"|GATE:"+(p.gate_no||"PENDING")+"|DISPATCH:"+(p.dispatch_no||"NO"),width:90,height:90});
  });
}
async function boot(){
  try{
    const rows=await loadJsonl("generated/PRODUCT-PASSPORTS.jsonl");
    window.__SHIRMANI_PRODUCTS=new Map(rows.map(p=>[p.id,p]));
    if(!window.QRCode)await new Promise(resolve=>{const s=document.createElement("script");s.src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js";s.onload=resolve;s.onerror=resolve;document.head.appendChild(s)});
    const style=document.createElement("style");style.textContent=".sri-visual-wrap img{transition:transform .25s ease}.sri-visual-wrap:hover img{transform:scale(1.015)}";document.head.appendChild(style);
    decorate(); const grid=document.getElementById("grid"); if(grid)new MutationObserver(decorate).observe(grid,{childList:true,subtree:true});
  }catch(e){console.warn("SHIRMANI product visual layer unavailable",e)}
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();