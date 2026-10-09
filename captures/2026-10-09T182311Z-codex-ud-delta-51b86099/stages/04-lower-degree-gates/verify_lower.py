"""Exact loss of observable compression under lower-degree dynamic gates."""
import runpy,io,contextlib,json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 m=runpy.run_path(str(Path(__file__).with_name('verify_outer.py')))
rr=m['rr'];mul=m['mul'];A=m['A'];gate=m['gate'];R=m['R14'];add=m['add'];scale=m['scale'];tr=m['tr'];I=m['I'];ix=m['ix'];zeros=m['zeros']
flat=m['m']['m']['flat'];B=m['m']['m']['B'];checks={}
def ck(k,v):
 checks[k]=bool(v)
 assert v,k
EF=[gate(e,f) for f in flat if len(f)==3 for e in flat if len(e)==2 and set(e)<set(f)]
VE=gate((0,),(0,1));one=gate((0,1),(0,1,2))
families={'one_edge_face':[A]+m['all_gates']+[one],
          'all_edge_face':[A]+m['all_gates']+EF,
          'plus_one_vertex_edge':[A]+m['all_gates']+EF+[VE]}
results={}
for name,gs in families.items():
 O,_=rr(R);seq=[len(O)]
 while True:
  N,_=rr(O+sum([mul(O,g) for g in gs],[]))
  if len(N)==len(O):break
  O=N;seq.append(len(O))
 O,piv=rr(O);hs=[]
 for j,g in enumerate(gs):
  OG=mul(O,g);H=[[row[i] for i in piv] for row in OG]
  ck(name+'_intertwiner_'+str(j),mul(H,O)==OG);hs.append(H)
 results[name]={'ranks':seq,'R':O,'reduced_generators':hs}
ck('sixteen',results['one_edge_face']['ranks']==[14,15,16])
ck('twenty_two',results['all_edge_face']['ranks']==[14,18,22])
ck('twenty_three',results['plus_one_vertex_edge']['ranks']==[14,19,23])
u=[[int(len(t)==1)] for t in flat]
ck('uniform_vertex_null_A',mul(A,u)==zeros(23,1))
ck('uniform_vertex_null_all_upper_gates',all(mul(g,u)==zeros(23,1) for g in m['all_gates']+EF))
R22=results['all_edge_face']['R']
ck('uniform_vertex_unseen22',mul(R22,u)==zeros(22,1))
ck('vertex_gate_exposes_uniform',mul(R22,mul(VE,u))!=zeros(22,1))
# Exact gradient-mode witness: initially invisible in R14, exposed by closing one edge-face link.
grad=[[B[ix[(0,)]][j] if len(flat[j])==2 else 0] for j in range(23)]
ck('gradient_hidden14',mul(R,grad)==zeros(14,1))
off=add(A,scale(one,-1));diff=mul(R,mul(off,grad))
ck('gradient_exposed_by_edge_face_gate',diff!=zeros(14,1))
ck('shared_face_derivative_one',mul(off,grad)[ix[(0,1,2)]][0]==1)
ck('twenty_one_edge_face_controls',len(EF)==21)
ck('full_record_rank',len(rr(results['plus_one_vertex_edge']['R'])[0])==23)
out={'scope':'development; arbitrary real initial states; common autonomous linear output records',
     'families':results,'checks':checks,'passed':sum(checks.values()),'total':len(checks),
     'inherited':{'baseline':18,'shared_face':21,'outer_face':28},
     'gradient_witness':grad,'uniform_vertex_witness':u}
Path(__file__).with_name('lower_results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'ranks':{k:v['ranks'] for k,v in results.items()},'passed':out['passed'],'total':out['total']},indent=2))
