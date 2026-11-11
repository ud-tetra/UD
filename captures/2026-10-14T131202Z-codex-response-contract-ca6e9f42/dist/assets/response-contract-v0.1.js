'use strict';
if(document.body.dataset.page==='source-contract'){
 const masks=Array.from({length:8},(_,n)=>[n>>2&1,n>>1&1,n&1]);const label=x=>x.join('');
 const selects={};
 [['T','Prospective integrity T','111'],['L','Prospective latent presence L','100'],['prior','Aligned prior Theta','011']].forEach(([id,title,value])=>{
  const l=el('label','dependency-label',title),s=el('select');s.id='response-'+id;masks.forEach(m=>{const o=el('option','',label(m));o.value=label(m);s.append(o)});s.value=value;l.append(s);$('#response-controls').append(l);selects[id]=s;s.addEventListener('change',render);
 });
 function render(){
  const T=[...selects.T.value].map(Number),L=[...selects.L.value].map(Number),prior=[...selects.prior.value].map(Number),omega=T.map((t,p)=>t*L[p]),I=T.map((t,p)=>t*(1-L[p])),i=I.reduce((a,b)=>a+b,0);
  const responses=masks.filter(h=>h.every((v,p)=>v<=I[p])).map(h=>{const theta=omega.map((w,p)=>1-w-h[p]);return {h,theta,j:h.reduce((a,b)=>a+b,0),mu:theta.reduce((a,b)=>a+b,0)-prior.reduce((a,b)=>a+b,0)}});
  const summary=el('div','inventory-banner');[[label(omega),'viable mask omega'],[label(I),'intact-null potential I'],[String(responses.length),'admitted responses']].forEach(([n,t])=>{const d=el('div');d.append(el('b','',n),el('span','',t));summary.append(d)});$('#response-summary').replaceChildren(summary);
  $('#response-rows').replaceChildren(...responses.map(r=>{const tr=el('tr');[label(r.h),label(r.theta),String(r.j),(r.mu>0?'+':'')+r.mu].forEach(v=>tr.append(el('td','mono',v)));return tr}));
  const box=el('aside','callout');box.append(el('strong','',i===0?'No idle choice remains on this supplied domain.':i+' intact-null address'+(i===1?'':'es')+' still need a source law.'));
  box.append(el('p','',i===0?'The conditional response is unique once these prospective T and L are independently supplied. This does not derive them from a native pre-state.':'At each idle count j the address multiplicity is binomial('+i+',j). A deterministic equivariant rule using only these T and L can select h=000 or h='+label(I)+'. Extra distinguishing state or a declared stochastic kernel needs its own source.'));
  box.append(el('p','muted','All rows are admissible conditional alternatives. They are not scored predictions, observed frequencies or probability weights.'));$('#response-symmetry').replaceChildren(box);
 }
 render();
}
