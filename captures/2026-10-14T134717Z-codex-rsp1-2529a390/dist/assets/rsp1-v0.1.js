'use strict';
if(document.body.dataset.page==='source-programme'){
 (async()=>{
  const data=await fetchJSON('/sources/rsp1-v0.1/RSP1_PAIRED_SYNTHETIC_TRACES_v0.1.json');
  const select=$('#rsp-example'),previous=$('#rsp-previous'),next=$('#rsp-next');let tick=0;
  const notes={stock_and_refills:'Both branches start with the same stocks and finite refill queue. Compare exhaustion with the early hold latch.',cache_extinction:'Holding q fixed still requires a source-cache update. The viable index and idle correction cancel.',balanced_swap:'A zero net Hamming budget can contain two directed toggles. The close branch must commit the exchange and token consumption.',broken_cache:'A broken-seat cached latent bit clears before a zero refill advances the cursor. Neither changes the visible response.'};
  const mask=x=>x.join('');const scalar=(box,name,value)=>{const row=el('div','rsp-field');row.append(el('span','muted',name),el('strong','mono',String(value)));box.append(row)};
  function render(){
   const paired=data[select.value],limit=Math.max(paired.C.trace.length,paired.H.trace.length);tick=Math.min(tick,limit);
   $('#rsp-position').textContent='Ordinal tick '+tick+' / '+limit;previous.disabled=tick===0;next.disabled=tick===limit;$('#rsp-note').textContent=notes[select.value];
   const cards=[];
   for(const branch of ['C','H']){
    const run=paired[branch],row=tick<run.trace.length?run.trace[tick]:run.terminal,e=row.event,s=row.post_state;
    const card=el('article','source-detail rsp-card');card.append(el('div','eyebrow','RSP-1 / '+branch),el('h2','',branch==='C'?'Close on idle':'Hold open'));
    card.append(el('span','tag',row.transition_kind.replaceAll('_',' ')),el('p','muted',tick>=run.trace.length?'Model fixed point reached after '+run.committed_updates+' committed updates.':'Inspecting committed transition '+(tick+1)+'.'));
    const fields=el('div','rsp-fields');[['Response q',mask(s.q)],['Closure Theta',mask(e.theta_output)],['Cached latent L',mask(s.L)],['Idle response h',mask(e.h_output)],['Active stock r',s.r.join(', ')],['Bank cursor',s.cursor+' / '+s.bank.length],['Remaining stock',row.available_stock_after],['Viable index',e.viable_index],['Full budget mu',e.mu_theta],['Gross toggles',e.gross_pair_toggles],['Potential V',row.potential_before+' → '+row.potential_after]].forEach(([k,v])=>scalar(fields,k,v));card.append(fields);
    card.append(el('p','',row.response_tag.replaceAll('_',' ')+(row.halt_reason?' · '+row.halt_reason.replaceAll('_',' '):'')));
    const detail=el('details');detail.append(el('summary','','Complete pre-state and successor'));detail.append(el('pre','source-meta',JSON.stringify({pre_state:row.pre_state,post_state:row.post_state,event:e},null,2)));card.append(detail);
    const log=el('details');log.append(el('summary','',run.committed_updates+' committed transitions · expand trace'));const list=el('ol','rsp-log');run.trace.forEach((r,i)=>list.append(el('li','',i+': '+r.transition_kind+' / '+r.response_tag+' · mu '+r.event.mu_theta+' · gross '+r.event.gross_pair_toggles+' · stock '+r.available_stock_after)));log.append(list);card.append(log);cards.push(card);
   }
   $('#rsp-comparison').replaceChildren(...cards);
  }
  select.addEventListener('change',()=>{tick=0;render()});previous.addEventListener('click',()=>{tick--;render()});next.addEventListener('click',()=>{tick++;render()});render();
 })().catch(e=>{$('#rsp-note').textContent=e.message+' Use the downloadable paired traces and proof below.'});
}
