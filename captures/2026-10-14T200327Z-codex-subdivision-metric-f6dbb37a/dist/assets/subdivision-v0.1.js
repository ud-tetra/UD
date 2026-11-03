'use strict';
const SubdivisionGate=(()=>{
 const factors=[1,2,6,24];
 function inspect(branch){
  const common={old:15,fine:149,complement:134,factors};
  const modes={
   ordinary:{norm:'Fails in positive degrees',boundary:'Exact',generator:'Fails',vertex:1,defect:7,pairing:'Unit Euclidean target metric',normFactors:factors,note:'The source map preserves oriented boundaries and increases Euclidean norm by degree.'},
   bounded:{norm:'Contractive native map; isometric with retained residual',boundary:'Exact',generator:'Fails',vertex:1/Math.sqrt(24),defect:7/24,pairing:'Unit Euclidean native and residual metrics',normFactors:factors.map(x=>x/24),note:'The source bounded branch retains lost native norm in a separate residual carrier. It attenuates singleton readout.'},
   degree:{norm:'Exact',boundary:'Fails',generator:'Not admitted by this boundary-preserving contract',vertex:1,defect:null,pairing:'Unit Euclidean target metric',normFactors:factors.map(()=>1),note:'Normalizing each degree separately changes relative boundary factors. Edge boundary defect squared: 3−2√2.'},
   diagonal:{norm:'Exact',boundary:'Exact',generator:'Fails',vertex:1,defect:11,pairing:'Target degree metric I/(k+1)!; defect uses this metric',normFactors:factors.map(()=>1),note:'A simple metric compensation does not make the embedded image invariant under the new weighted adjoint.'},
   retraction:{norm:'Exact conditional',boundary:'Exact',generator:'Exact conditional',vertex:1,defect:0,pairing:'H=RᵀR+QᵀWQ; W positive, Q=I−SR',normFactors:factors.map(()=>1),note:'Authored metric extension: coarse dynamics is retained. The metric is generally nondiagonal, with134 fine complement directions; source selection and local support/readout remain open.'}
  };
  if(!Object.hasOwn(modes,branch))throw new RangeError('Unknown declared branch.');
  return {...common,...modes[branch]};
 }
 return {inspect};
})();
if(typeof module!=='undefined')module.exports=SubdivisionGate;
if(typeof document!=='undefined'&&document.body.dataset.page==='subdivision'){
 const select=$('#sg-branch');
 function show(){
  const r=SubdivisionGate.inspect(select.value);
  $('#sg-verdict').textContent=r.note;
  const table=el('table'),head=el('thead'),row=el('tr');['Condition','Result'].forEach(t=>row.append(el('th','',t)));head.append(row);table.append(head);
  const body=el('tbody');[['Native norm',r.norm],['Boundary equation',r.boundary],['Generator equation',r.generator],['Old singleton amplitude',r.vertex.toFixed(6)],['Vertex generator defect squared',r.defect===null?'Separate boundary failure; no generator-admission claim':r.defect.toFixed(6)],['Declared pairing',r.pairing]].forEach(([k,v])=>{const tr=el('tr');tr.append(el('th','',k),el('td','',v));body.append(tr)});table.append(body);const wrap=el('div','table-wrap');wrap.append(table);$('#sg-conditions').replaceChildren(wrap);
  $('#sg-factors').textContent='Squared norm factors by degree 0,1,2,3: '+r.normFactors.map(x=>x.toFixed(6)).join(', ')+'. Values are rounded; the replay is exact.';
 }
 select.addEventListener('change',show);show();
}
