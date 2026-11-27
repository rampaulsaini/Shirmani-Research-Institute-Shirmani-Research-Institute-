(()=>{"use strict";
const API_BASE="https://shirmani-research-institute-shirmani.onrender.com";
const panel=document.createElement("section");
panel.className="panel";
panel.setAttribute("aria-live","polite");
panel.style.cssText="border:1px solid #496783;background:#10243a;border-radius:12px;padding:12px;margin:12px 0";
const heading=document.createElement("strong");heading.textContent="Shared Shirmani API";
const status=document.createElement("span");status.textContent="Not checked";
status.style.cssText="display:block;margin:6px 0;color:#b9c8d8";
const note=document.createElement("small");note.textContent="Connection test only. This app's records remain in this browser unless you explicitly choose an available server submission.";
note.style.cssText="display:block;color:#b9c8d8";
const button=document.createElement("button");button.type="button";button.textContent="Check secure connection";
button.style.cssText="margin-top:8px;padding:9px 12px;border-radius:8px;border:0;background:#f2d17a;color:#17202a;font-weight:700";
button.addEventListener("click",async()=>{button.disabled=true;status.textContent="Checking API…";try{const response=await fetch(API_BASE+"/health",{method:"GET",headers:{Accept:"application/json"},cache:"no-store",mode:"cors",signal:AbortSignal.timeout(10000)});const body=await response.json().catch(()=>({}));if(!response.ok)throw new Error(body.status||body.error||("HTTP "+response.status));status.textContent="API reachable · "+(body.status||"response received");status.style.color="#86efac"}catch(error){status.textContent="Connection not verified · "+(error.name==="TimeoutError"?"timeout":"service/CORS/network unavailable");status.style.color="#fbbf24"}finally{button.disabled=false}});
panel.append(heading,status,note,button);
const header=document.querySelector("header");if(header)header.after(panel);else document.querySelector("main")?.prepend(panel);
window.SRI_API={
submitEnquiry:async lead=>{const response=await fetch(API_BASE+"/v1/enquiries",{method:"POST",mode:"cors",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify({name:lead.name,email:lead.email||"",phone:lead.phone||"",service:"Lead Desk",language:"Hindi",topic:lead.need||"Lead follow-up",goal:lead.note||"",consent:true})});const body=await response.json().catch(()=>({}));if(!response.ok)throw new Error(body.error||body.message||("HTTP "+response.status));return body}
};
})();