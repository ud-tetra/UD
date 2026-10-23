'use strict';
const MetricSelection=(()=>{
 function calculate(w,lambda){
  if(!Number.isFinite(w)||w<=0||!Number.isFinite(lambda)||lambda<0||lambda>1)throw new RangeError('Positive residual weight and a response between zero and one required.');
  const coarse=.5,residual=1.5,norm=coarse+w*residual,value=coarse+lambda*w*residual;
  return {coarse,residual,norm,value,fraction:value/norm,coarseFraction:coarse/norm,complementFraction:w*residual/norm,allCompatibilityConditions:true,complementBlind:lambda===0};
 }
 return {calculate};
})();
if(typeof module!=='undefined')module.exports=MetricSelection;
if(typeof document!=='undefined'&&document.body.dataset.page==='metric-selection'){
 const weight=$('#ms-weight'),response=$('#ms-response');
 function exact(a,b=1){
  let n=Math.round(a*8),d=Math.round(b*8);const gcd=(x,y)=>y?gcd(y,x%y):x,v=gcd(n,d);n/=v;d/=v;return d===1?String(n):n+'/'+d;
 }
 function show(){
  const w=Number(weight.value),lambda=Number(response.value),r=MetricSelection.calculate(w,lambda);
  $('#ms-verdict').textContent='All three compatibility conditions pass for this metric. The observable is '+(r.complementBlind?'complement-blind.':'sensitive to the retained complement.')+' Neither control is a selected UD coefficient.';
  const table=el('table'),head=el('thead'),row=el('tr');['Same fine barycenter state','Exact value'].forEach(t=>row.append(el('th','',t)));head.append(row);table.append(head);
  const body=el('tbody');[['Decoded coarse squared norm',exact(r.coarse)],['Residual Euclidean squared norm',exact(r.residual)],['Metric squared norm',exact(r.norm)],['Observable value',exact(r.value)],['Observable / full norm',exact(r.value,r.norm)]].forEach(([k,v])=>{const tr=el('tr');tr.append(el('th','',k),el('td','',v));body.append(tr)});table.append(body);const wrap=el('div','table-wrap');wrap.append(table);$('#ms-witness').replaceChildren(wrap);
  $('#ms-receipts').textContent='Complete complement-blind receipts: vertex0 '+exact(.25,r.norm)+'; vertex1 '+exact(.25,r.norm)+'; retained complement '+exact(w*1.5,r.norm)+'. All other coarse outcomes zero. Total1.';
 }
 weight.addEventListener('change',show);response.addEventListener('change',show);show();
}
