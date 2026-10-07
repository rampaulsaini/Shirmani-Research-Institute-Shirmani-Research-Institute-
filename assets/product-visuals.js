/* SHIRMANI Supreme Product Visual Engine v5 — logo-first, product-first, QR upper-right */
(function(global){
"use strict";
function hashCode(s){let h=2166136261;for(let i=0;i<String(s).length;i++){h^=String(s).charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
function esc(v){return String(v??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
function money(n){return Number(n||0)===0?"FREE":"₹"+Number(n||0).toLocaleString("en-IN")}
function wrap(text,max){const words=String(text||"").split(/\s+/),lines=[];let line="";for(const w of words){if((line+" "+w).trim().length>max&&line){lines.push(line);line=w}else line=(line+" "+w).trim()}if(line)lines.push(line);return lines.slice(0,3)}
function visual(p){
 p=p||{};const key=String(p.id||p.name||"SHIRMANI-PRODUCT"),h=hashCode(key),a=h%360,b=(h>>>8)%360,c=(h>>>16)%360,uid="v5"+h;
 const title=esc(String(p.name||"SHIRMANI Digital Product").slice(0,62)),id=esc(p.id||"PRODUCT");
 const family=esc(String(p.family||p.category||"DIGITAL PRODUCT").slice(0,34)),engine=esc(String(p.engine||"SUPREME").slice(0,28));
 const descLines=wrap(String(p.short_description||p.description||"Unique customer-facing digital product").replace(/\s+/g," "),52).map(esc);
 const price=esc(money(p.offer_price_inr??p.price_inr??0));
 const base=global.location&&global.location.origin?global.location.origin:"https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-";
 const target=base+"/product-passport.html?id="+encodeURIComponent(key);
 const qr="https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=10&data="+encodeURIComponent(target);
 const logo=base+"/assets/shirmani-perspective-logo.svg";
 const identity="Shiromani Rampal Saini · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present";
 const svg='<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160"><defs>'+
 '<linearGradient id="'+uid+'g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="hsl('+a+',78%,24%)"/><stop offset=".48" stop-color="hsl('+b+',72%,11%)"/><stop offset="1" stop-color="hsl('+c+',78%,5%)"/></linearGradient>'+
 '<radialGradient id="'+uid+'r"><stop stop-color="#fff" stop-opacity=".28"/><stop offset=".42" stop-color="#67e8f9" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'+
 '<filter id="'+uid+'gl"><feGaussianBlur stdDeviation="22"/></filter></defs>'+
 '<rect width="3840" height="2160" fill="url(#'+uid+'g)"/><circle cx="2050" cy="1100" r="760" fill="url(#'+uid+'r)"/>'+
 '<path d="M260 1540 C980 1180 1280 1820 2020 1450 S3040 1260 3630 1510" fill="none" stroke="#1ee7ff" stroke-opacity=".45" stroke-width="42" filter="url(#'+uid+'gl)"/>'+
 '<path d="M260 1540 C980 1180 1280 1820 2020 1450 S3040 1260 3630 1510" fill="none" stroke="#2ce7c9" stroke-width="8"/>'+
 '<rect x="70" y="70" width="3700" height="2020" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/>'+
 '<rect x="150" y="125" width="580" height="580" rx="80" fill="#061016" stroke="#e7c85b" stroke-width="12"/><image href="'+logo+'" x="205" y="180" width="470" height="470" preserveAspectRatio="xMidYMid meet"/>'+
 '<text x="440" y="760" text-anchor="middle" fill="#f6d35f" font-family="system-ui,sans-serif" font-size="34" font-weight="950">SHIRMANI HEART-VIEW</text>'+
 '<text x="440" y="815" text-anchor="middle" fill="#d9e3ef" font-family="system-ui,sans-serif" font-size="19" font-weight="750">'+esc(identity)+'</text>'+
 '<text x="830" y="190" fill="#66ddff" font-family="system-ui,sans-serif" font-size="52" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text>'+
 '<text x="520" y="900" fill="#66ddff" font-family="system-ui,sans-serif" font-size="76" font-weight="900">'+id+'</text>'+
 '<text x="520" y="1100" fill="#fff" font-family="system-ui,sans-serif" font-size="'+(String(p.name||"").length>30?100:122)+'" font-weight="900">'+title+'</text>'+
 '<text x="520" y="1225" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="62" font-weight="800">'+family+' · '+engine+'</text>'+
 '<text x="520" y="1340" fill="#fff" font-family="system-ui,sans-serif" font-size="43" font-weight="650">SHORT DESCRIPTION</text>'+
 descLines.map((x,i)=>'<text x="520" y="'+(1400+i*58)+'" fill="#dce7f2" font-family="system-ui,sans-serif" font-size="39" font-weight="650">'+x+'</text>').join('')+
 '<rect x="520" y="1600" width="730" height="125" rx="62" fill="#03060d" stroke="#e7c85b" stroke-width="5"/><text x="590" y="1685" fill="#fff" font-family="system-ui,sans-serif" font-size="62" font-weight="900">'+price+'</text>'+
 '<rect x="2920" y="105" width="720" height="790" rx="48" fill="#061016" stroke="#e7c85b" stroke-width="10"/><text x="3060" y="205" fill="#fff" font-family="system-ui,sans-serif" font-size="46" font-weight="950">LONG DESCRIPTION</text><text x="3230" y="265" fill="#fff" font-family="system-ui,sans-serif" font-size="46" font-weight="950">/ PRODUCT DETAILS</text><rect x="3050" y="330" width="470" height="470" fill="#fff"/><image href="'+qr+'" x="3060" y="340" width="450" height="450"/><text x="3070" y="850" fill="#66ddff" font-family="system-ui,sans-serif" font-size="28" font-weight="900">SCAN FOR LONG DESCRIPTION</text>'+
 '<text x="520" y="1860" fill="#fff" opacity=".86" font-family="system-ui,sans-serif" font-size="35" font-weight="800">3840×2160 4K MASTER · UNIQUE PRODUCT IDENTITY · DEMO VIDEO · QC/GATE/DISPATCH · LONG-PASSPORT QR</text></svg>';
 return "data:image/svg+xml;charset=UTF-8,"+encodeURIComponent(svg);
}
global.SHIRMANI_PRODUCT_VISUAL={hashCode,visual,version:"v6-logo-first-qr-upper-right"};
})(window);