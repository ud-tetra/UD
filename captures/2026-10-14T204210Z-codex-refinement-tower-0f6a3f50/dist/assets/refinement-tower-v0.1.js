'use strict';
const RefinementTower=(()=>{
 function counts(level){
  if(!Number.isInteger(level)||level<0||level>4)throw new RangeError('Choose a retained level from zero to four.');
  let f=[4,6,4,1],previous=15;const out=[];
  for(let l=0;l<=level;l++){
   const dimension=f.reduce((a,b)=>a+b,0);out.push({level:l,f:[...f],dimension,newDirections:l===0?0:dimension-previous,totalDetails:dimension-15});previous=dimension;
   const [v,e,t,c]=f;f=[v+e+t+c,2*e+6*t+14*c,6*t+36*c,24*c];
  }return out;
 }
 function witness(degree){
  if(![1,2,3].includes(degree))throw new RangeError('Positive detail degree required.');
  const factor=[1,2,6,24][degree],sequentialDetail=2,freshDetail=2*factor;
  return {factor,sequentialDetail,freshDetail,coarseStock:1,sequentialTotal:3,freshTotal:1+freshDetail,sequentialFraction:1/3,freshFraction:1/(1+freshDetail)};
 }
 return {counts,witness};
})();
if(typeof module!=='undefined')module.exports=RefinementTower;
if(typeof document!=='undefined'&&document.body.dataset.page==='refinement-tower'){
 const level=$('#rt-level'),degree=$('#rt-degree');
 function table(headers,rows){
  const t=el('table'),h=el('thead'),r=el('tr');headers.forEach(x=>r.append(el('th','',x)));h.append(r);t.append(h);const b=el('tbody');rows.forEach(xs=>{const r=el('tr');xs.forEach(x=>r.append(el('td','',String(x))));b.append(r)});t.append(b);const wrap=el('div','table-wrap');wrap.append(t);return wrap;
 }
 function show(){
  const rows=RefinementTower.counts(Number(level.value)),w=RefinementTower.witness(Number(degree.value));
  $('#rt-counts').replaceChildren(table(['Level','Face vector','Full directions','Added directions','Retained details'],rows.map(r=>[r.level,'('+r.f.join(', ')+')',r.dimension.toLocaleString('en-US'),r.newDirections.toLocaleString('en-US'),r.totalDetails.toLocaleString('en-US')])));
  $('#rt-verdict').textContent='Two-step detail calibration differs by factor '+w.factor+'. Both prescriptions preserve the same original coarse norm and generator. Regrouping coherence requires transported detail pairings.';
  $('#rt-witness').replaceChildren(table(['Same retained input','Sequential calibration','Fresh composite calibration'],[['Detail squared norm',w.sequentialDetail,w.freshDetail],['Coarse unit vertex added: total',w.sequentialTotal,w.freshTotal],['Absolute coarse stock',1,1],['Coarse / full norm','1/3','1/'+w.freshTotal]]));
 }
 level.addEventListener('change',show);degree.addEventListener('change',show);show();
}
