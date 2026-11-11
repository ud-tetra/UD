'use strict';
if(document.body.dataset.page==='dependencies'){
 (async()=>{
  const graph=await fetchJSON('/assets/dependencies-v0.14.json');
  const byId=new Map(graph.nodes.map(n=>[n.id,n]));
  const branch=$('#dependency-branch'),select=$('#dependency-node'),scenario=$('#dependency-scenario');
  const params=new URLSearchParams(location.search);let chosen=byId.get(params.get('node'));
  if(chosen)branch.value=chosen.branch;
  graph.scenarios.forEach(s=>{const o=el('option','',s.title);o.value=s.id;scenario.append(o)});
  function nodeLink(id){const n=byId.get(id),b=el('button','dependency-node-link',id+' · '+n.title);b.addEventListener('click',()=>{branch.value=n.branch;populate(id)});return b}
  function listEdges(heading,edges,upstream){
   const box=el('div','dependency-column');box.append(el('h3','',heading));
   if(!edges.length)box.append(el('p','muted',upstream?'Declared root object; inspect its source scope below.':'No further uses in this scoped register.'));
   edges.forEach(e=>{const c=el('article','dependency-edge');c.append(nodeLink(upstream?e.from:e.to),el('span','tag',e.kind.replaceAll('_',' ')),el('p','',e.reason));box.append(c)});return box;
  }
  function show(){
   const n=byId.get(select.value);chosen=n;
   const box=el('article','source-detail');box.append(el('div','eyebrow',n.id+' / '+n.branch),el('h2','',n.title),el('span','tag',n.status.replaceAll('_',' ')),el('p','form',n.objects),el('p','',n.conclusion));
   const neighborhood=el('div','dependency-neighborhood');
   neighborhood.append(listEdges('Premises →',graph.edges.filter(e=>e.to===n.id),true));
   const center=el('div','dependency-selected');center.append(el('span','mono',n.id),el('strong','',n.title),el('p','muted','Every arrow follows an explicit dependency.'));
   neighborhood.append(center,listEdges('→ Downstream uses',graph.edges.filter(e=>e.from===n.id),false));box.append(neighborhood);
   const refs=el('div');refs.append(el('h3','','Source binding'));
   n.citations.forEach(c=>{const s=graph.sources.find(s=>s.id===c.source_id),d=el('details');d.append(el('summary','',c.source_id+' · '+c.section));
    d.append(el('p','',s.title),el('p','source-meta','Exact text locator: '+c.anchor_text),el('p','source-meta','Source-text snapshot SHA-256: '+c.snapshot_sha256),el('p','muted',s.representation));
    const links=el('div','actions');links.append(link('Read source text snapshot',s.path),link('Inspect original provenance','/sources/?id='+s.id));if(s.original_url)links.append(link('Original source ↗',s.original_url));d.append(links);refs.append(d)});box.append(refs);
   if(n.ledger_ids.length){const links=el('div','actions');n.ledger_ids.forEach(id=>links.append(link('LEDGER:'+id,'/reconciliation/?row='+id,'citation')));box.append(links)}
   $('#dependency-detail').replaceChildren(box);$('#dependency-message').textContent=graph.scope;
   const p=new URLSearchParams(location.search);p.set('node',n.id);history.replaceState(null,'','?'+p);
   const exclusions=graph.excluded_inferences.filter(x=>byId.get(x.from).branch===branch.value);
   $('#dependency-exclusions').replaceChildren(...exclusions.map(x=>{const c=el('article','claim');c.append(el('h3','',x.from+' ⇏ '+x.to),el('p','',x.reason));return c}));
  }
  function populate(id){select.replaceChildren();graph.nodes.filter(n=>n.branch===branch.value).forEach(n=>{const o=el('option','',n.id+' · '+n.title);o.value=n.id;select.append(o)});select.value=id|| (branch.value==='polarity'?'P-CORRECT':'A-SCALE');show()}
  function audit(changes,note=''){
   const reached=new Map(),queue=[...changes.map(id=>({id,path:[id]}))];const roots=new Set(changes);
   while(queue.length){const item=queue.shift();graph.edges.filter(e=>e.from===item.id).forEach(e=>{if(!roots.has(e.to)&&!reached.has(e.to)){const path=[...item.path,e.to];reached.set(e.to,{path,edge:e});queue.push({id:e.to,path})}})}
   const result=el('div','dependency-audit');result.append(el('h3','',changes.join(', ')+' revised or withdrawn'),el('p','',reached.size+' downstream uses require scope review / pending rederivation for reuse.'),el('p','muted',graph.propagation_policy));if(note)result.append(el('p','',note));
   if(reached.size){const table=el('table'),head=el('tr');['Affected use','Declared status retained','Dependency path'].forEach(t=>head.append(el('th','',t)));const thead=el('thead');thead.append(head);table.append(thead);const tbody=el('tbody');reached.forEach((r,id)=>{const tr=el('tr'),cell=el('td');cell.append(nodeLink(id));tr.append(cell,el('td','',byId.get(id).status),el('td','source-meta',r.path.join(' → ')));tbody.append(tr)});table.append(tbody);const wrap=el('div','table-wrap');wrap.append(table);result.append(wrap)}
   else result.append(el('p','','This object has no licensed downstream dependency in the scoped graph.'));
   const intact=graph.nodes.filter(n=>!roots.has(n.id)&&!reached.has(n.id));const d=el('details');d.append(el('summary','',intact.length+' objects outside this change path'));const p=el('div','dependency-preserved');intact.forEach(n=>p.append(nodeLink(n.id)));d.append(p);result.append(d);$('#dependency-impact').replaceChildren(result);
  }
  branch.addEventListener('change',()=>populate());select.addEventListener('change',show);
  scenario.addEventListener('change',()=>{const s=graph.scenarios.find(s=>s.id===scenario.value);audit(s.changes,s.note)});
  $('#dependency-audit').addEventListener('click',()=>audit([chosen.id],'Custom hypothetical change of the selected object. This is not an amendment to the scientific registry.'));
  populate(chosen?.id);const first=graph.scenarios[0];audit(first.changes,first.note);
 })().catch(error=>{$('#dependency-message').textContent=error.message+' Use the report and graph downloads below.'});
}
