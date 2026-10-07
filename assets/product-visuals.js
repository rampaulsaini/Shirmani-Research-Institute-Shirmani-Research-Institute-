/* SHIRMANI Supreme Product Visual Engine — deterministic unique 4K SVG per product */
(function(global){
"use strict";
function hashCode(s){let h=2166136261;for(let i=0;i<String(s).length;i++){h^=String(s).charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
function esc(v){return String(v??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
function money(n){return Number(n||0)===0?"FREE":"₹"+Number(n||0).toLocaleString("en-IN")}
function visual(p){
 p=p||{};
 const key=String(p.id||p.name||"SHIRMANI-PRODUCT"),h=hashCode(key),a=h%360,b=(h>>>8)%360,c=(h>>>16)%360,uid="v"+h;
 const rawTitle=String(p.name||"SHIRMANI Digital Product"),title=esc(rawTitle.slice(0,58));
 const id=esc(p.id||"PRODUCT"),family=esc(String(p.family||p.category||"DIGITAL PRODUCT").slice(0,34));
 const engine=esc(String(p.engine||"SUPREME").slice(0,28));
 const desc=esc(String(p.short_description||p.description||"Unique customer-facing digital product").replace(/\s+/g," ").slice(0,92));
 const price=esc(money(p.offer_price_inr??p.price_inr??0));
 const titleSize=rawTitle.length>38?112:rawTitle.length>28?138:168;
 const emblemX=3020+(h%240), emblemY=1380+((h>>>12)%180);
 const svg='<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-label="'+title+' — SHIRMANI unique 4K product visual"><defs>'+
 '<linearGradient id="'+uid+'g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="hsl('+a+',78%,22%)"/><stop offset=".48" stop-color="hsl('+b+',70%,11%)"/><stop offset="1" stop-color="hsl('+c+',72%,6%)"/></linearGradient>'+
 '<radialGradient id="'+uid+'r"><stop stop-color="#fff" stop-opacity=".24"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'+
 '<filter id="'+uid+'s"><feGaussianBlur stdDeviation="34"/></filter></defs>'+
 '<rect width="3840" height="2160" fill="#03060d"/><rect x="70" y="70" width="3700" height="2020" rx="120" fill="url(#'+uid+'g)"/>'+
 '<circle cx="3180" cy="430" r="720" fill="url(#'+uid+'r)"/><circle cx="650" cy="1740" r="470" fill="hsl('+a+',80%,65%)" opacity=".07"/>'+
 '<ellipse cx="1910" cy="1790" rx="1370" ry="190" fill="#000" opacity=".5" filter="url(#'+uid+'s)"/>'+
 '<rect x="155" y="155" width="3530" height="1850" rx="95" fill="none" stroke="#e7c85b" stroke-opacity=".72" stroke-width="9"/>'+
 '<path d="M220 1540 C720 1110 1120 1810 1690 1370 S2780 1100 3620 1510" fill="none" stroke="#66ddff" stroke-opacity=".32" stroke-width="24"/>'+
 '<path d="M260 1580 C820 1210 1180 1880 1710 1430 S2820 1180 3560 1550" fill="none" stroke="#72e6aa" stroke-opacity=".18" stroke-width="12"/>'+
 '<circle cx="'+emblemX+'" cy="'+emblemY+'" r="285" fill="none" stroke="#e7c85b" stroke-opacity=".42" stroke-width="12"/><circle cx="'+emblemX+'" cy="'+emblemY+'" r="195" fill="none" stroke="#66ddff" stroke-opacity=".28" stroke-width="8"/>'+
 '<path d="M'+(emblemX-150)+' '+emblemY+'h300M'+emblemX+' '+(emblemY-150)+'v300" stroke="#fff" stroke-opacity=".16" stroke-width="6"/>'+
 '<text x="300" y="420" fill="#66ddff" font-family="system-ui,sans-serif" font-size="86" font-weight="900">꙰ SHIRMANI SUPREME DIGITAL PRODUCT</text>'+
 '<text x="300" y="790" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="'+titleSize+'" font-weight="900">'+title+'</text>'+
 '<text x="300" y="970" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="70" font-weight="900">'+id+'</text>'+
 '<text x="300" y="1085" fill="#e7c85b" font-family="system-ui,sans-serif" font-size="64" font-weight="800">'+family+' · '+engine+'</text>'+
 '<text x="300" y="1190" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="48" font-weight="650" opacity=".92">'+desc+'</text>'+
 '<rect x="300" y="1290" width="690" height="158" rx="79" fill="#03060d" opacity=".78" stroke="#e7c85b" stroke-opacity=".48" stroke-width="5"/>'+
 '<text x="370" y="1393" fill="#fff" font-family="system-ui,sans-serif" font-size="66" font-weight="900">'+price+'</text>'+
 '<text x="300" y="1815" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="48" font-weight="700" opacity=".9">4K · UNIQUE PRODUCT IDENTITY · SHORT DESCRIPTION · QR LONG DESCRIPTION</text>'+
 '<text x="300" y="1895" fill="#66ddff" font-family="system-ui,sans-serif" font-size="38" font-weight="800" opacity=".85">IDENTITY KEY · '+uid+' · QC / GATE / SHOWROOM READY</text></svg>';
 return "data:image/svg+xml;charset=UTF-8,"+encodeURIComponent(svg);
}
global.SHIRMANI_PRODUCT_VISUAL={hashCode,visual};
})(window);