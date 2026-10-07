(function(){
"use strict";
const esc=s=>String(s??"").replace(/[&<>"]/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]));
function visual(p){
 let h=0,id=String(p.id||"");for(let i=0;i<id.length;i++)h=((h<<5)-h+id.charCodeAt(i))|0;
 const hx=n=>"#"+Math.abs((h+n*2654435761)>>>0).toString(16).padStart(8,"0").slice(0,6);
 const c1=hx(1),c2=hx(2),a=hx(3);
 return '<div class="product-visual"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" role="img" aria-label="'+esc(p.name)+' product visual"><defs><linearGradient id="g-'+esc(id)+'" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="'+c1+'"/><stop offset="1" stop-color="'+c2+'"/></linearGradient></defs><rect width="1200" height="650" fill="#060b12"/><rect x="35" y="35" width="1130" height="580" rx="42" fill="url(#g-'+esc(id)+')" opacity=".96"/><circle cx="1010" cy="145" r="90" fill="'+a+'" opacity=".28"/><circle cx="1080" cy="225" r="145" fill="#fff" opacity=".08"/><path d="M90 510 C280 410 330 590 510 470 S800 420 1100 505" fill="none" stroke="#fff" stroke-width="5" opacity=".28"/><text x="90" y="105" fill="#fff" font-family="system-ui,sans-serif" font-size="28" font-weight="800">꙰ SHIRMANI DIGITAL PRODUCT</text><text x="90" y="205" fill="#fff" font-family="system-ui,sans-serif" font-size="52" font-weight="900">'+esc(p.name)+'</text><text x="90" y="265" fill="#fff" font-family="system-ui,sans-serif" font-size="25" opacity=".9">'+esc(p.family||p.category)+' · '+esc(p.engine)+'</text><rect x="90" y="325" width="330" height="64" rx="32" fill="#060b12" opacity=".72"/><text x="125" y="367" fill="#fff" font-family="system-ui,sans-serif" font-size="24" font-weight="800">'+esc(id)+'</text><text x="90" y="565" fill="#fff" font-family="system-ui,sans-serif" font-size="22" opacity=".9">UNIQUE PRODUCT IDENTITY · PRIME DIGITAL PACK</text></svg></div><div class="visual-caption">Unique product identity visual · '+esc(id)+'</div>';
}
async function boot(){
 let catalog;try{catalog=await fetch("generated/1000-digital-products.json?visuals="+Date.now(),{cache:"no-store"}).then(r=>r.json())}catch(e){return}
 const map=new Map((catalog.products||[]).map(p=>[p.id,p]));
 if(!window.QRCode){await new Promise(resolve=>{const s=document.createElement("script");s.src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js";s.onload=resolve;s.onerror=resolve;document.head.appendChild(s)})}
 const style=document.createElement("style");style.textContent=".product-visual{border-radius:14px;overflow:hidden;border:1px solid #30445a;background:#060b12;margin-bottom:4px}.product-visual svg{display:block;width:100%;height:auto}.visual-caption{font-size:.72rem;color:#aeb9c8;letter-spacing:.04em;text-transform:uppercase;margin:0 0 5px}.qr-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:4px}.qr{width:96px;min-height:96px;padding:6px;background:#fff;border-radius:10px;display:grid;place-items:center}.qr img{max-width:96px;height:auto}";document.head.appendChild(style);
 const decorate=()=>document.querySelectorAll("#grid .card").forEach(card=>{
  if(card.dataset.identityVisual==="1")return;
  const muted=card.querySelector(".muted");if(!muted)return;const m=muted.textContent.match(/\bSP-\d{4,}\b/);if(!m)return;const p=map.get(m[0]);if(!p)return;
  card.dataset.identityVisual="1";const wrap=document.createElement("div");const pid=String(p.id||"").toLowerCase();wrap.innerHTML='<div class="product-visual"><img src="products/visuals/'+encodeURIComponent(pid)+'.svg" alt="'+esc(p.name)+' — unique 4K product identity" width="3840" height="2160" loading="lazy" onerror="this.onerror=null;this.parentElement.outerHTML='+JSON.stringify(visual(p))+'"></div><div class="visual-caption">Unique product identity visual · '+esc(p.id)+'</div>';card.insertBefore(wrap,card.firstChild);
  const qr=document.createElement("div");qr.className="qr-row";qr.innerHTML='<div class="qr"></div><span class="muted">QR: Product Passport · QC · Gate · Dispatch</span>';
  const action=card.querySelector("p:last-child");if(action)card.insertBefore(qr,action);
  const qimg=qr.querySelector(".qr");qimg.innerHTML='<img src="products/visuals/qr/'+encodeURIComponent(String(p.id).toLowerCase())+'.svg" alt="QR — long description" width="96" height="96" loading="lazy">';if(window.QRCode && !qimg.querySelector("img"))new QRCode(qimg,{text:location.origin+location.pathname.replace(/[^/]*$/,"")+"product-passport.html?id="+encodeURIComponent(p.id)+"|QC:"+(p.qc_code||"PENDING")+"|GATE:"+(p.gate_no||"PENDING")+"|DISPATCH:"+(p.dispatch_no||"NO")+"|PRICE:"+(p.offer_price_inr||""),width:84,height:84});
 });
 const grid=document.getElementById("grid");if(grid)new MutationObserver(decorate).observe(grid,{childList:true,subtree:true});decorate();
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",boot);else boot();
})();