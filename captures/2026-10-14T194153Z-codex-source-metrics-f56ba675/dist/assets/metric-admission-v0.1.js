'use strict';
const MetricAdmission=(()=>{
  function calculate(q,p){
    if(!Number.isFinite(q)||q<=0||![1,2].includes(p))throw new RangeError('Positive shape and declared Rule A/B required.');
    const a=((1+q)/2)**p,b=((2*q+1)/3)**p,c=q**p;
    const squares=[4/a,2+2/a,4*a/b,2*(a+1)/b,4*b/c];
    return {a,b,c,squares,frequencies:squares.map(Math.sqrt),relation:squares[0]/squares[1]+squares[2]/squares[3],multiplicities:[1,2,1,2,1]};
  }
  function degree(g,convention){
    if(g.length!==4||g.some(x=>!Number.isFinite(x)||x<=0)||!['adjoint','mass'].includes(convention))throw new RangeError('Four positive metric entries and a declared convention required.');
    return [0,1,2].map(k=>2*Math.sqrt(convention==='adjoint'?g[k]/g[k+1]:1/(g[k]*g[k+1])));
  }
  return {calculate,degree};
})();
if(typeof module!=='undefined')module.exports=MetricAdmission;
if(typeof document!=='undefined'&&document.body.dataset.page==='metric-admission'){
  const rule=$('#mf-rule'),shape=$('#mf-shape');
  function show(){
    const q=Number(shape.value),p=Number(rule.value),r=MetricAdmission.calculate(q,p);
    const count=new Set(r.squares.map(x=>x.toPrecision(13))).size;
    $('#mf-verdict').textContent='Rule '+(p===1?'A':'B')+' · q='+q+' · '+count+' distinct positive '+(count===1?'band':'bands')+'. Full default n=10 admission: excluded in this fixed-rule, identical-copy family.';
    const table=el('table'),head=el('thead'),row=el('tr');
    ['Band','Squared frequency','Positive frequency','Multiplicity per sign'].forEach(t=>row.append(el('th','',t)));head.append(row);table.append(head);
    const body=el('tbody');['u','v','x','y','z'].forEach((label,i)=>{const tr=el('tr');[label,r.squares[i].toFixed(6),r.frequencies[i].toFixed(6),r.multiplicities[i]].forEach(t=>tr.append(el('td','',String(t))));body.append(tr)});table.append(body);
    const wrap=el('div','table-wrap');wrap.append(table);$('#mf-spectrum').replaceChildren(wrap);
    $('#mf-invariant').textContent='Source identity: u/v + x/y = '+r.relation.toFixed(12)+'. Display values are rounded; the proof and replay use exact rational arithmetic.';
  }
  rule.addEventListener('change',show);shape.addEventListener('change',show);show();
}
