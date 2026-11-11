'use strict';
// Exact finite-label calculator shared with the Python construction; no physical simulation claim.
const JointCarrier = (()=>{
 function blank(N){return {w:0,h:Array(N).fill(0),records:Array(N).fill(0)}}
 function copy(x){return JSON.parse(JSON.stringify(x))}
 function action(clock,N,B){const j=Math.floor(clock/(N+1)),i=clock%(N+1);return {kind:i<N?'COMPUTE':j<B?'RESET_EXPORT':'WRAP_IDLE',episode:j,slot:i<N?i:null,donor:i===N&&j<B?j:null}}
 function step(x,spec,N,B){const out=copy(x),a=action(x.clock,N,B),L=(B+1)*(N+1);
  if(a.kind==='COMPUTE'){const i=a.slot,w=x.active.w;out.active.w=(x.active.h[i]+spec.successor[w])%spec.successor.length;out.active.h[i]=w;out.active.records[i]=(x.active.records[i]+spec.receipt[w])%spec.record_dimension}
  if(a.kind==='RESET_EXPORT'){out.active=copy(x.donors[a.donor]);out.donors[a.donor]=copy(x.active)}
  out.clock=(x.clock+1)%L;return out;
 }
 function trace(spec,N,B,extra=false){const L=(B+1)*(N+1);let x={clock:0,active:blank(N),donors:Array.from({length:B},()=>blank(N))};const rows=[copy(x)];for(let k=0;k<L-1+(extra?N+1:0);k++){x=step(x,spec,N,B);rows.push(copy(x))}return rows}
 function resources(d,m,N,B){const L=(B+1)*(N+1),D=BigInt(d)**BigInt(N+1)*BigInt(m)**BigInt(N);return {L,K:L-1,D,joint:BigInt(L)*D**BigInt(B+1),bits:Math.ceil(Math.log2(L))+(B+1)*((N+1)*Math.ceil(Math.log2(d))+N*Math.ceil(Math.log2(m))),history:(B+1)*N,records:(B+1)*N,compute:(B+1)*N,resets:B}}
 return {blank,action,step,trace,resources};
})();
if(typeof module!=='undefined')module.exports=JointCarrier;
if(typeof document!=='undefined'&&document.body.dataset.page==='joint-carrier'){
 (async()=>{
 const w=await fetchJSON('/sources/joint-carrier-v0.1/JOINT_CARRIER_WITNESS_v0.1.json');
 const branch=$('#jc-branch'),ticks=$('#jc-ticks'),resets=$('#jc-resets'),post=$('#jc-post'),slider=$('#jc-step');let rows=[],spec,N,B,r;
 const table=(headers,data)=>{const wrap=el('div','jc-table-wrap'),t=el('table','jc-table'),head=el('thead'),tr=el('tr');headers.forEach(h=>tr.append(el('th','',h)));head.append(tr);t.append(head);const body=el('tbody');data.forEach(row=>{const tr=el('tr');row.forEach(v=>tr.append(el('td','',String(v))));body.append(tr)});t.append(body);wrap.append(t);return wrap};
 function payload(name,p){const card=el('article','source-detail');const s=spec.states[p.w];card.append(el('h3','',name),el('p','mono','Work '+p.w+' · q '+s.q.join('')+' · stock '+s.r.join(',')),el('p','mono','State memory ['+p.h.join(', ')+']'),el('p','mono','Receipts ['+p.records.join(', ')+']'));const details=el('details');details.append(el('summary','','Complete encoded work state'),el('pre','source-meta',JSON.stringify(s,null,2)));card.append(details);return card}
 function update(){const k=Number(slider.value),x=rows[k],inside=k<=r.K,a=k?JointCarrier.action(rows[k-1].clock,N,B):null,used=inside?Math.min(B,Math.floor(k/(N+1))):B;
  $('#jc-position').textContent=k+' / '+r.K+' certified';$('#jc-prev').disabled=k===0;$('#jc-next').disabled=k===rows.length-1;
  const v=$('#jc-verdict');v.className='hr-verdict '+(inside?'hr-match':'hr-mismatch');v.textContent=(inside?'INSIDE DECLARED WINDOW · ':'OUTSIDE DECLARED WINDOW · ')+(a?a.kind.replaceAll('_',' ')+' → clock '+x.clock:'Prepared clock and complete bank');
  const clock=el('div','jc-clock-strip');for(let i=0;i<r.L;i++){const cell=el('span',i===x.clock?'jc-clock-cell selected':'jc-clock-cell',String(i));cell.title=JointCarrier.action(i,N,B).kind+' · episode '+Math.floor(i/(N+1));clock.append(cell)}$('#jc-clock').replaceChildren(el('p','muted','Master clock '+x.clock+' of '+r.L+' addresses · relative address '+x.clock%(N+1)+' · episode address '+Math.floor(x.clock/(N+1))),clock);
  const cards=el('div','rsp-comparison');cards.append(payload('Active payload',x.active));x.donors.forEach((p,j)=>cards.append(payload(j<used?'Outgoing block '+j+' · consumed':'Fresh reset block '+j+' · untouched',p)));$('#jc-payloads').replaceChildren(cards);
  let stock=s=>s.r.reduce((a,b)=>a+b,0)+s.bank.slice(s.cursor).reduce((a,row)=>a+row.reduce((a,b)=>a+b,0),0),active=stock(spec.states[x.active.w]),fresh=x.donors.slice(used).reduce((a,p)=>a+stock(spec.states[p.w]),0),out=x.donors.slice(0,used).reduce((a,p)=>a+stock(spec.states[p.w]),0);
  $('#jc-stock').textContent=(inside?'Encoded RSP stock ledger: ':'Post-window labels; supply guarantee no longer applies: ')+'active '+active+' · untouched donors '+fresh+' · outgoing remaining '+out+'. Historical state and receipt copies are nonspendable descriptions.';
  $('#jc-resources').replaceChildren(table(['Resource','Allocated / scheduled','Disposition at this transition'],[
   ['Master clock',r.L+' addresses; '+r.K+' certified transitions','Address '+x.clock+'; payload swaps never reset it'],
   ['State memory',r.history+' cells of dimension '+spec.states.length,used*N+' outgoing; '+N+' active; '+(B-used)*N+' in fresh donors'],
   ['Receipt memory',r.records+' cells of dimension '+spec.record_dimension,used*N+' outgoing; '+N+' active; '+(B-used)*N+' in fresh donors'],
   ['Reset donors',B+' complete independent payloads',used+' consumed; '+(B-used)+' untouched'],
   ['Compute ticks',r.compute+' scheduled ticks',(B+1)+' episodes × '+N+' ticks'],
   ['Payload capacity',r.D.toLocaleString()+' labels','Work + '+N+' state + '+N+' receipt factors'],
   ['Complete joint capacity',r.joint.toLocaleString()+' labels','Clock + active + all donor/outgoing blocks'],
   ['Separate binary allocation',r.bits+' bits','Capacity; no entropy or heat minimum'],
   ['Complete restart donor',r.joint.toLocaleString()+' labels','Not supplied by the current schedule']
  ]));
  if(!inside){const p=el('p','muted','The operator continues reversibly on dirty cells. Clock wrap supplies no fresh memory, receipt cell, stock or donor. A decoded work label may coincide temporarily; that does not renew the window.');$('#jc-payloads').append(p)}
 }
 function reset(){N=Number(ticks.value);B=Number(resets.value);spec=w.branches[branch.value].specification;r=JointCarrier.resources(spec.states.length,spec.record_dimension,N,B);rows=JointCarrier.trace(spec,N,B,post.checked);slider.max=rows.length-1;slider.value=Math.min(Number(slider.value),rows.length-1);$('#jc-dictionary').replaceChildren(el('pre','source-meta',JSON.stringify({states:spec.states,receipts:spec.record_dictionary},null,2)));update()}
 [branch,ticks,resets,post].forEach(n=>n.addEventListener('change',reset));slider.addEventListener('input',update);$('#jc-prev').addEventListener('click',()=>{slider.value=Math.max(0,Number(slider.value)-1);update()});$('#jc-next').addEventListener('click',()=>{slider.value=Math.min(rows.length-1,Number(slider.value)+1);update()});reset();
 })().catch(e=>{$('#jc-verdict').textContent=e.message+' The complete proof and replay remain available below.'});
}
