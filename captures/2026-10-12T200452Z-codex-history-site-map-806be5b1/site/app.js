const docs = {
  manuscript:{title:"Current manuscript",label:"v2.3 · POC-1 corpus no-go",note:"Exact discrete mathematics is separated from physical interpretation.",kind:"html",file:"./content/manuscript-v2.3.html",source:"./source/TETRAHEDRAL_PACKET_COMPLEXES_JOP_LEAN_MANUSCRIPT_v2.3_POC1_CORPUS_NO_GO.md"},
  event:{title:"Constitutive Receipt-Index Event Operator",label:"Event operator · v0.1",note:"A constitutive source artifact with explicit theorem, gate, and gap boundaries.",kind:"html",file:"./content/event-operator.html",source:"./source/UD_CONSTITUTIVE_RECEIPT_INDEX_EVENT_OPERATOR_v0.1.md"},
  preevent:{title:"Pre-Event Held-Out Protocol",label:"Held-out protocol · v0.1",note:"Predictor inputs, frozen law, test procedure, and reopen rule.",kind:"html",file:"./content/pre-event-protocol.html",source:"./source/PRE_EVENT_HELDOUT_PROTOCOL_v0.1.md"},
  admission:{title:"Independent Corpus Admission Protocol",label:"Admission protocol · v0.2",note:"Forbidden repairs and admissibility verdicts for POC-1 evidence.",kind:"html",file:"./content/corpus-admission.html",source:"./source/POC1_INDEPENDENT_CORPUS_ADMISSION_PROTOCOL_v0.2.md"},
  audit:{title:"Public Corpus Admissibility Audit",label:"Admissibility audit · v0.1",note:"Candidate matrix, ruling, exact source no-go, and lawful dataset specification.",kind:"html",file:"./content/corpus-audit.html",source:"./source/POC1_PUBLIC_CORPUS_ADMISSIBILITY_AUDIT_v0.1.md"},
  verification:{title:"Exact Verification Record",label:"Machine verification · v0.1",note:"Exact verification results supplied with the manuscript package.",kind:"json",file:"./source/EXACT_VERIFICATION_v0.1.json",source:"./source/EXACT_VERIFICATION_v0.1.json"},
  ledger:{title:"Coefficient Provenance Ledger",label:"Provenance ledger · v0.45",note:"Constitutive receipt-index patch and coefficient provenance records.",kind:"json",file:"./source/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.45_CONSTITUTIVE_RECEIPT_INDEX_PATCH.json",source:"./source/UD_COEFFICIENT_PROVENANCE_LEDGER_v0.45_CONSTITUTIVE_RECEIPT_INDEX_PATCH.json"},
  archive21:{title:"Constitutive Manuscript",label:"Archived manuscript · v2.1",note:"Earlier constitutive manuscript retained for comparison and provenance.",kind:"html",file:"./content/manuscript-v2.1.html",source:"./source/TETRAHEDRAL_PACKET_COMPLEXES_JOP_LEAN_MANUSCRIPT_v2.1_CONSTITUTIVE.md"}
};
const collections = {
  protocols:{title:"Protocols",intro:"Frozen procedures governing admission and held-out evaluation.",items:["admission","preevent"]},
  evidence:{title:"Evidence & provenance",intro:"Audits and machine-readable records supporting the manuscript’s exact claims and source boundaries.",items:["audit","verification","event","ledger"]},
  archive:{title:"Archive",intro:"Prior manuscript state preserved as part of the package’s scientific provenance.",items:["archive21"]}
};
const main=document.querySelector("#main"),toc=document.querySelector("#toc"),sourceLink=document.querySelector("#sourceLink");
const editionLabel=document.querySelector("#editionLabel"),editionNote=document.querySelector("#editionNote");
let currentText="",headings=[];
function slug(){return location.hash.slice(2)||"primer"}
function setActive(route){document.querySelectorAll("[data-route]").forEach(a=>a.classList.toggle("active",a.dataset.route===route))}
function escapeHtml(s){return s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
function enhanceArticle(article){
  headings=[...article.querySelectorAll("h1,h2,h3")];
  const seen=new Map();
  headings.forEach((h,i)=>{let id=h.id||h.textContent.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"")||`section-${i}`;const n=seen.get(id)||0;seen.set(id,n+1);if(n)id+=`-${n+1}`;h.id=id});
  toc.innerHTML=headings.filter(h=>h.tagName!=="H1"||h!==headings[0]).map(h=>`<button class="level-${h.tagName.slice(1)}" data-target="${h.id}">${escapeHtml(h.textContent)}</button>`).join("");
  currentText=article.innerText;
  const observer=new IntersectionObserver(es=>{const top=es.filter(e=>e.isIntersecting).sort((a,b)=>a.boundingClientRect.top-b.boundingClientRect.top)[0];if(top)document.querySelectorAll("#toc [data-target]").forEach(a=>a.classList.toggle("active",a.dataset.target===top.target.id))},{rootMargin:"-90px 0px -70% 0px"});
  headings.forEach(h=>observer.observe(h));
}
async function showDocument(key,section){
  const d=docs[key]; if(!d)return showCollection("evidence");
  main.innerHTML='<div class="loading"><span class="tetra-loader"></span><p>Preparing the edition…</p></div>';
  const raw=await fetch(d.file).then(r=>{if(!r.ok)throw Error(r.status);return d.kind==="json"?r.json():r.text()});
  if(d.kind==="json"){
    const article=document.createElement("article");article.className="paper";
    article.innerHTML=`<div class="collection-header"><p class="eyebrow">${escapeHtml(d.label)}</p><h1>${escapeHtml(d.title)}</h1><p>${escapeHtml(d.note)}</p></div><pre class="json-view">${escapeHtml(JSON.stringify(raw,null,2))}</pre>`;
    main.replaceChildren(article);enhanceArticle(article);
  }else{
    const article=document.createElement("article");article.className="paper";article.innerHTML=raw;main.replaceChildren(article);enhanceArticle(article);
    if(key==="manuscript")addManuscriptVisualLinks(article);
  }
  editionLabel.textContent=d.label;editionNote.textContent=d.note;sourceLink.href=d.source;sourceLink.hidden=false;
  setActive(key==="manuscript"?"manuscript":Object.entries(collections).find(([,c])=>c.items.includes(key))?.[0]||"");
  if(section){requestAnimationFrame(()=>document.getElementById(section)?.scrollIntoView({behavior:"smooth"}))}else{window.scrollTo(0,0)}
  main.focus({preventScroll:true});
}
async function showPrimer(section){
  main.innerHTML='<div class="loading"><span class="tetra-loader"></span><p>Preparing the visual primer…</p></div>';
  const raw=await fetch("./content/primer.html").then(r=>{if(!r.ok)throw Error(r.status);return r.text()});
  const article=document.createElement("article");article.className="primer paper";article.innerHTML=raw;main.replaceChildren(article);enhanceArticle(article);setupPrimerInteractions(article);
  editionLabel.textContent="Visual primer · entry level";editionNote.textContent="Geometry, chains, transport, retriangulation, receipts, and falsification—before the formal manuscript.";
  sourceLink.hidden=true;setActive("primer");if(section){requestAnimationFrame(()=>document.getElementById(section)?.scrollIntoView({behavior:"smooth"}))}else{window.scrollTo(0,0)}main.focus({preventScroll:true});
}
function addManuscriptVisualLinks(article){
  const companions={
    "21-tetrahedral-carrier-and-opposite-edge-fiber":["primer-carrier","See the tetrahedral carrier"],
    "22-filled-tetrahedral-chain-carrier":["primer-chains","See the exploded chain complex"],
    "31-skew-transport-and-conserved-support":["primer-transport","See incidence transport"],
    "41-exact-hamming-branch-structure":["primer-fiber","Explore the binary address cube"],
    "51-oriented-pachner-pair":["primer-pachner","Compare the Pachner configurations"],
    "61-ray-nonidentifiability-before-psr":["primer-psr","Step through PSR reconstruction"],
    "71-intrinsic-held-out-design":["primer-heldout","See the 14 + 14 held-out split"]
  };
  Object.entries(companions).forEach(([id,[target,label]])=>{const heading=article.querySelector("#"+id);if(!heading)return;const link=document.createElement("a");link.className="visual-companion";link.href=`#/primer?section=${target}`;link.innerHTML=`<span>Visual companion</span>${label} →`;heading.insertAdjacentElement("afterend",link)});
}
function showCollection(key){
  const c=collections[key];if(!c)return showDocument("manuscript");
  main.innerHTML=`<section class="collection-header"><p class="eyebrow">Manuscript package</p><h1>${c.title}</h1><p>${c.intro}</p></section><section class="artifact-grid">${c.items.map(id=>{const d=docs[id];return `<a class="artifact-card" href="#/doc/${id}"><small>${d.label}</small><h2>${d.title}</h2><p>${d.note}</p></a>`}).join("")}</section>`;
  toc.innerHTML=c.items.map(id=>`<a href="#/doc/${id}">${docs[id].title}</a>`).join("");
  currentText=main.innerText;headings=[...main.querySelectorAll("h1,h2")];editionLabel.textContent="Complete source package";editionNote.textContent=c.intro;sourceLink.hidden=true;setActive(key);window.scrollTo(0,0);
}
function route(){const [s,query=""]=slug().split("?");const section=new URLSearchParams(query).get("section");if(s==="primer")showPrimer(section);else if(s.startsWith("doc/"))showDocument(s.slice(4),section);else if(collections[s])showCollection(s);else showDocument("manuscript",section)}
function setupPrimerInteractions(root){
  root.querySelectorAll("[data-matching]").forEach(button=>button.addEventListener("click",()=>{
    root.querySelectorAll("[data-matching]").forEach(b=>b.classList.toggle("active",b===button));
    root.querySelectorAll("[data-edge]").forEach(edge=>edge.classList.toggle("selected",edge.dataset.edge.includes(button.dataset.matching)));
    root.querySelector("#matchingReadout").textContent=button.dataset.label;
  }));
  root.querySelectorAll("[data-shell]").forEach(button=>button.addEventListener("click",()=>{
    const shell=button.dataset.shell;root.querySelectorAll("[data-shell]").forEach(b=>b.classList.toggle("active",b===button));
    root.querySelectorAll("[data-weight]").forEach(node=>node.classList.toggle("muted",node.dataset.weight!==shell));
    root.querySelector("#shellReadout").textContent=`Weight ${shell}: ${[1,3,3,1][shell]} address${shell==="0"||shell==="3"?"":"es"}`;
  }));
  root.querySelectorAll("[data-pachner]").forEach(button=>button.addEventListener("click",()=>{
    const state=button.dataset.pachner;root.querySelectorAll("[data-pachner]").forEach(b=>b.classList.toggle("active",b===button));
    root.querySelectorAll("[data-pachner-state]").forEach(view=>view.hidden=view.dataset.pachnerState!==state);
  }));
  root.querySelectorAll("[data-psr-step]").forEach(button=>button.addEventListener("click",()=>{
    const step=Number(button.dataset.psrStep);root.querySelectorAll("[data-psr-step]").forEach(b=>b.classList.toggle("active",Number(b.dataset.psrStep)<=step));
    root.querySelectorAll("[data-psr-layer]").forEach(layer=>layer.classList.toggle("visible",Number(layer.dataset.psrLayer)<=step));
    root.querySelector("#psrReadout").textContent=["Supports fix magnitudes, but not relative signs.","Forest-edge products propagate relative signs.","One root sign fixes each connected support component.","The chain ray is reconstructed up to its global projective sign."][step-1];
  }));
}
window.addEventListener("hashchange",route);route();
const dialog=document.querySelector("#searchDialog"),input=document.querySelector("#searchInput"),results=document.querySelector("#searchResults");
function openSearch(){dialog.showModal();setTimeout(()=>input.focus(),30)}
document.querySelector("#searchButton").addEventListener("click",openSearch);
document.addEventListener("keydown",e=>{if(e.key==="/"&&!/input|textarea/i.test(e.target.tagName)){e.preventDefault();openSearch()}});
input.addEventListener("input",()=>{const q=input.value.trim().toLowerCase();if(!q){results.innerHTML="<p>Type a term, theorem, symbol, or section title.</p>";return}const hits=headings.filter(h=>(h.textContent+" "+(h.nextElementSibling?.textContent||"")).toLowerCase().includes(q)).slice(0,12);results.innerHTML=hits.length?hits.map(h=>`<button type="button" data-jump="${h.id}"><strong>${escapeHtml(h.textContent)}</strong><span>${escapeHtml((h.nextElementSibling?.textContent||"").slice(0,150))}</span></button>`).join(""):`<p>No section-level matches. The term occurs ${currentText.toLowerCase().split(q).length-1} time(s) in this document.</p>`});
results.addEventListener("click",e=>{const hit=e.target.closest("[data-jump]");if(hit){dialog.close();document.getElementById(hit.dataset.jump)?.scrollIntoView({behavior:"smooth"})}});
const panel=document.querySelector("#tocPanel"),scrim=document.querySelector("#scrim");function menu(open){panel.classList.toggle("open",open);scrim.classList.toggle("show",open);document.querySelector("#menuButton").setAttribute("aria-expanded",open)}
document.querySelector("#menuButton").addEventListener("click",()=>menu(true));document.querySelector("#closeMenu").addEventListener("click",()=>menu(false));scrim.addEventListener("click",()=>menu(false));toc.addEventListener("click",e=>{const target=e.target.closest("[data-target]");if(target)document.getElementById(target.dataset.target)?.scrollIntoView({behavior:"smooth"});menu(false)});
