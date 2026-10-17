'use strict';
const $=s=>document.querySelector(s);
const el=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n};
const link=(label,href,cls='text-link')=>{const a=el('a',cls,label);a.href=href;return a};
const menu=$('.menu-toggle');menu?.addEventListener('click',()=>{const active=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(active));$('.sidebar').classList.toggle('menu-open',active)});
const page=document.body.dataset.page;
if(page==='primer'){
 const descriptions=['C₀ stores four vertex amplitudes. Coordinate count does not identify four spacetime dimensions.','C₁ stores six oriented edge amplitudes. Its cut and cycle subspaces each have rank three under the declared unit metric.','C₂ stores four oriented triangular face amplitudes. A shared face is retained as one reservoir.','C₃ stores one oriented cell amplitude. Adding a filled cell changes the chain complex, not merely its drawing.','The filled tetrahedron has 15 chain coordinates: four vertices, six edges, four faces and one cell.'];
 document.querySelectorAll('[data-degree]').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('[data-degree]').forEach(x=>{x.classList.toggle('selected',x===b);x.setAttribute('aria-pressed',String(x===b))});
  const index=b.dataset.degree==='all'?4:Number(b.dataset.degree);$('#degree-description').textContent=descriptions[index];$('#degree-count').replaceChildren(document.createTextNode([4,6,4,1,15][index]+' '),el('small','', 'coordinates'));
  const svg=$('.explorer .tetra');['vertices','edges','faces','body'].forEach((cls,i)=>{svg.querySelector('.tetra-'+cls).style.opacity=index===4||i===index?'1':'.12'});
 }));
 document.querySelectorAll('[data-degree]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.degree==='0')));
}
async function fetchJSON(path){const r=await fetch(path);if(!r.ok)throw new Error('Source data could not be loaded.');return r.json()}
if(page==='sources'){
 let all=[],filtered=[],limit=35;
 const query=$('#source-query'),group=$('#source-group'),params=new URLSearchParams(location.search);query.value=params.get('q')||'';group.value=params.get('group')||'';
 $('#result-count').textContent='Loading the source registry…';
 const normalize=s=>String(s).normalize('NFKC').toLowerCase();
 function detail(id){
  const s=all.find(x=>x.id===id);if(!s)return;
  const box=el('article','source-detail');box.id='selected-source';const close=el('button','close-detail','×');close.setAttribute('aria-label','Close source detail');close.addEventListener('click',()=>{$('#source-detail').replaceChildren();const p=new URLSearchParams(location.search);p.delete('id');history.replaceState(null,'','?'+p)});
  box.append(close,el('div','eyebrow',s.id+' / '+s.group),el('h2','',s.title),el('span','tag',s.status),el('p','',s.note));
  const meta=el('div','source-meta');meta.textContent=(s.sha256?'View SHA-256: '+s.sha256+' · ':'')+(s.size_bytes?'Size: '+s.size_bytes.toLocaleString()+' bytes':'');box.append(meta);
  const actions=el('div','actions');if(s.local)actions.append(link(s.original?'Download substantive view ↓':'Download source ↓',s.local));if(s.url)actions.append(link('Open original source ↗',s.url));if(s.original?.local)actions.append(link('Original input bytes ↓',s.original.local));else if(s.original)actions.append(link('Original ZIP with member bytes ↓','/sources/05-DistinctionDynamics_Full_Repository_v1.zip'));box.append(actions);
  if(s.related_source_ids?.length){const related=el('div','actions');s.related_source_ids.forEach(id=>related.append(link(id+' · related source','/sources/?id='+id,'citation')));box.append(related)}
  if(s.ledger_ids?.length){const related=el('div','actions');s.ledger_ids.forEach(id=>related.append(link('LEDGER:'+id,'/reconciliation/?row='+id,'citation')));box.append(related)}
  if(s.original){const original=el('details');original.append(el('summary','','Original intake provenance'));original.append(el('p','source-meta','Original SHA-256: '+s.original.sha256+' · '+s.original.size_bytes+' bytes. Original text is preserved as received; this view is a separate authored source crosswalk.'));box.append(original)}
  if(s.content){const d=el('details');d.open=true;d.append(el('summary','', 'Read source text · original formatting and qualifiers retained'));const pre=el('pre','',s.content);pre.tabIndex=0;d.append(pre);box.append(d)}else box.append(el('p','muted','Text is not embedded for this source. Use the available original/download link, or consult the stated intake limitation.'));
  $('#source-detail').replaceChildren(box);const p=new URLSearchParams(location.search);p.set('id',id);history.replaceState(null,'','?'+p);box.scrollIntoView({block:'start'});box.tabIndex=-1;box.focus({preventScroll:true});
 }
 function render(){
  const terms=normalize(query.value).split(/\s+/).filter(Boolean);
  filtered=all.filter(s=>(!group.value||s.group===group.value)&&terms.every(t=>normalize(s.id+' '+s.title+' '+s.status+' '+s.note+' '+s.content).includes(t)));
  $('#result-count').textContent=filtered.length.toLocaleString()+' matching sources · showing '+Math.min(limit,filtered.length)+'. Labels reproduce source status; catalog inclusion is not promotion.';
  const frag=document.createDocumentFragment();filtered.slice(0,limit).forEach(s=>{const row=el('article','source-item');row.append(el('div','mono',s.id));const c=el('div');const open=el('button','source-open','Inspect provenance & source →');open.addEventListener('click',()=>detail(s.id));c.append(el('h3','',s.title),el('p','',s.group+' · '+s.status),el('p','',s.note),open);row.append(c);frag.append(row)});$('#source-results').replaceChildren(frag);$('#more-sources').hidden=limit>=filtered.length;
 }
 let timer;const update=()=>{clearTimeout(timer);timer=setTimeout(()=>{limit=35;render();const p=new URLSearchParams(location.search);if(query.value)p.set('q',query.value);else p.delete('q');if(group.value)p.set('group',group.value);else p.delete('group');history.replaceState(null,'','?'+p)},140)};
 query.addEventListener('input',update);group.addEventListener('change',update);$('#more-sources').addEventListener('click',()=>{limit+=35;render()});
 fetchJSON('/assets/sources.json').then(d=>{all=d;render();if(params.get('id'))detail(params.get('id'))}).catch(e=>{$('#result-count').textContent=e.message+' The Papers remain directly accessible.'});
}
if(page==='ledger'){
 let rows=[];const input=$('#ledger-query'),bin=$('#ledger-bin');
 function render(){const q=input.value.toLowerCase();const filtered=rows.filter(r=>(!bin.value||r.claim_bin===bin.value)&&Object.values(r).join(' ').toLowerCase().includes(q));$('#ledger-count').textContent=filtered.length+' of '+rows.length+' source rows. Later amendments retain separate authority.';const f=document.createDocumentFragment();filtered.forEach(r=>{const a=el('article','ledger-row');a.id=r.id;a.append(el('div','mono',r.id));const c=el('div');c.append(el('h3','',r.symbol),el('div','form',r.exact_form),el('span','tag',r.claim_bin),el('p','', 'Source status: '+r.status),el('p','muted','Next gate: '+r.next_gate));if(r.reconciliation_notes)c.append(el('p','muted',r.reconciliation_notes));a.append(c);f.append(a)});$('#ledger-results').replaceChildren(f)}
 input.addEventListener('input',render);bin.addEventListener('change',render);fetchJSON('/assets/ledger.json').then(d=>{rows=d.rows;render()}).catch(e=>{$('#ledger-count').textContent=e.message});
}
if(page==='reconciliation'){
 let records=[],amendments=[];const input=$('#reconcile-query'),filter=$('#reconcile-filter'),param=new URLSearchParams(location.search);input.value=param.get('row')||param.get('q')||'';
 function render(){
  const terms=input.value.toLowerCase().split(/\s+/).filter(Boolean);
  const result=records.filter(r=>(!filter.value||(filter.value==='amended'?r.amendment_ids.length:r.version_relation===filter.value))&&terms.every(q=>JSON.stringify(r).toLowerCase().includes(q)));
  $('#reconcile-count').textContent=result.length+' of '+records.length+' reconciled source rows. Each retains original source status; proof-dependency completeness is OPEN_GATED.';
  const frag=document.createDocumentFragment();result.forEach(r=>{
   const a=el('article','ledger-row');a.id='ROW-'+r.row_id;a.append(el('div','mono','LEDGER:'+r.row_id));const c=el('div');c.append(el('h3','',r.source_row.symbol),el('div','form',r.source_row.exact_form),el('span','tag',r.current_disposition),el('p','','Original bin: '+r.source_row.claim_bin+' · Original status: '+r.source_row.status),el('p','muted',r.reuse_limit));
   const links=el('div','actions');links.append(link('Original later ledger','/sources/?id=L65','citation'));if(r.historical_source_id)links.append(link('Historical v0.39','/sources/?id=A20','citation'));r.amendment_ids.forEach(id=>links.append(link(id,'#'+id,'citation')));c.append(links);
   const detail=el('details');detail.append(el('summary','','Version and reference details'));detail.append(el('p','muted','Version relation: '+r.version_relation+(r.changed_fields.length?' · changed fields: '+r.changed_fields.join(', '):'')));
   if(r.historical_row)detail.append(el('pre','source-meta',JSON.stringify(r.historical_row,null,2)));
   const refs=el('div','actions');r.explicit_references.forEach(ref=>refs.append(ref.in_ledger?link('LEDGER:'+ref.ref_id+' ('+ref.field+')','/reconciliation/?row='+ref.ref_id,'citation'):el('span','citation',ref.namespace+':'+ref.ref_id+' · external criterion')));detail.append(refs,el('p','muted',r.dependency_graph_status),el('p','muted',r.verification));c.append(detail);a.append(c);frag.append(a);
  });$('#reconcile-rows').replaceChildren(frag);
 }
 let timer;input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(render,100)});filter.addEventListener('change',render);
 fetchJSON('/assets/reconciliation.json').then(d=>{records=d.rows;amendments=d.amendments;render()}).catch(e=>{$('#reconcile-count').textContent=e.message});
}
