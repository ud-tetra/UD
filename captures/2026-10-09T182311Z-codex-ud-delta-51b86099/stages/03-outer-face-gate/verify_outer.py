"""Exact common observable closure under face-cell gate families."""
import contextlib,io,json,runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('verify_gate.py')))
A=m['A']; R=m['R']; mul=m['mul']; rr=m['rref']; ix=m['ix']; zeros=m['zeros']; add=m['add']; scale=m['scale']; I=m['I']; tr=m['tr']
checks={}
def ck(name,v):
 checks[name]=bool(v)
 assert v,name
def gate(f,t):
 L=zeros(23,23); i,j=ix[f],ix[t]; L[i][j]=A[i][j]; L[j][i]=A[j][i]; return L
outer=gate((0,1,3),(0,1,2,3))
def closure(name,gens):
 O,_=rr(R); ranks=[len(O)]
 while True:
  N,_=rr(O+sum([mul(O,g) for g in gens],[]))
  if len(N)==len(O):break
  O=N;ranks.append(len(O))
 O,piv=rr(O); hs=[]
 for i,g in enumerate(gens):
  OG=mul(O,g); H=[[r[j] for j in piv] for r in OG]
  ck(name+'_intertwiner_'+str(i),mul(H,O)==OG);hs.append(H)
 ck(name+'_contains_original',len(rr(O+R)[0])==len(O))
 return {'ranks':ranks,'R':O,'generators':gens,'reduced_generators':hs}
all_gates=[gate(f,t) for t in m['m']['cells'] for f in m['m']['simp'][2] if set(f)<set(t)]
res={
 'outer_only':closure('outer_only',[A,outer]),
 'shared_and_outer':closure('shared_and_outer',[A,m['m']['L1'],m['m']['L2'],outer]),
 'all_face_cell':closure('all_face_cell',[A]+all_gates)}
ck('outer_dimension',res['outer_only']['ranks']==[6,7,8,9,10])
ck('shared_outer_dimension',res['shared_and_outer']['ranks']==[6,7,8,9,10])
ck('all_face_cell_dimension',res['all_face_cell']['ranks']==[6,10,14])
u=add([[v] for v in I[ix[(0,1,3)]]],[[v] for v in I[ix[(0,2,3)]]])
base=[[v] for v in I[ix[(0,1,2,3)]]]
xp=add(base,u);xm=add(base,scale(u,-1));Aoff=add(A,scale(outer,-1))
ck('witness_same_record',mul(R,xp)==mul(R,xm))
ck('witness_same_full_norm',mul(tr(xp),xp)==mul(tr(xm),xm))
dp=mul(R,mul(Aoff,xp));dm=mul(R,mul(Aoff,xm))
ck('witness_opposite_cell_derivatives',dp[0][0]==-1 and dm[0][0]==1)
R10=res['shared_and_outer']['R'];R14=res['all_face_cell']['R']
ck('ten_retains_outer_face',len(rr(R10+[I[ix[(0,1,3)]]])[0])==10)
faces=m['m']['simp'][2];cells=m['m']['cells'];edges=m['m']['simp'][1]
face_rows=[I[ix[f]] for f in faces];cell_rows=[I[ix[t]] for t in cells]
# Edge component of each face derivative is its oriented boundary circulation.
circs=[[A[ix[f]][j] if len(m['m']['flat'][j])==2 else 0 for j in range(23)] for f in faces]
ck('edge_circulation_rank_five',len(rr(circs)[0])==5)
natural=face_rows+cell_rows+circs
ck('fourteen_natural_span',len(rr(natural)[0])==14 and len(rr(natural+R14)[0])==14)
ck('eight_gate_controls',len(all_gates)==8)
out={'status':'development; candidate dynamic masks; physical promotion 0',
 'families':res,'witness':{'plus':'e0123+e013+e023','minus':'e0123-e013-e023',
 'closed_outer_retained_derivatives':[dp,dm]},'checks':checks,'passed':sum(checks.values()),'total':len(checks),
 'inherited_checks':{'baseline':m['m']['out']['passed'],'shared_gate':m['out']['passed']}}
Path(__file__).with_name('outer_results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'ranks':{k:v['ranks'] for k,v in res.items()},'passed':out['passed'],'total':out['total'],'inherited':out['inherited_checks']},indent=2))
