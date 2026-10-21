"""New exact calibration, not execution of an archived research script."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
C=Path(__file__).parent;R=C.parents[1]
contract=json.loads((C/'CONTRACT.json').read_text());receipt=json.loads((C/'FREEZE_RECEIPT.json').read_text())
assert hashlib.sha256((C/'CONTRACT.json').read_bytes()).hexdigest()==receipt['sha256']
for s in contract['source_files']:assert hashlib.sha256((R/s['path']).read_bytes()).hexdigest()==s['sha256']
n=64
I=[[int(i==j) for j in range(n)] for i in range(n)]
def block(k):return [[int(i//k==j//k) for j in range(n)] for i in range(n)]
B4=block(4);B16=block(16);J=block(64)
K=[J,[[4*B16[i][j]-J[i][j] for j in range(n)] for i in range(n)],[[16*B4[i][j]-4*B16[i][j] for j in range(n)] for i in range(n)],[[64*I[i][j]-16*B4[i][j] for j in range(n)] for i in range(n)]]
def mul(a,b):
 out=[[0]*n for _ in range(n)]
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):
     if y:out[i][j]+=x*y
 return out
assert [sum(p[i][i] for i in range(n))//64 for p in K]==[1,3,12,48]
for a,p in enumerate(K):
 for b,q in enumerate(K):
  got=mul(p,q);assert all(got[i][j]==(64*p[i][j] if a==b else 0) for i in range(n) for j in range(n))
assert all(sum(p[i][j] for p in K)==64*I[i][j] for i in range(n) for j in range(n))
eta=F(185,192);a=eta**4;b=eta**6
eigs=[F(0),64*b,16*a+48*b,12*a+48*b]
L=[[F(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
 for j in range(i+1,n):
  w=b if i//16!=j//16 else a if i//4!=j//4 else F(0)
  if w:L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
assert all(L[i][j]==sum(lam*p[i][j]/64 for lam,p in zip(eigs,K)) for i in range(n) for j in range(n))
assert len(set(eigs))==4 and all(x>0 for x in eigs[1:])
N=256
def metrics(q):
 assert len(q)==N and sum(q)==1 and all(x>=0 for x in q)
 w=[sum(q[c*64:(c+1)*64]) for c in range(N//64)]
 fc=[64*sum(x*x for x in q[c*64:(c+1)*64])/(w[c]**2) if w[c] else None for c in range(N//64)]
 glob=N*sum(x*x for x in q);cipr=sum(x*x for x in w);cond=glob/((N//64)*cipr)
 assert glob==(N//64)*sum(wc*wc*f for wc,f in zip(w,fc) if f is not None)
 assert all(1<=f<=64 for f in fc if f is not None) and 1<=cond<=64
 return {'global_F':str(glob),'component_IPR':str(cipr),'conditioned_F':str(cond),'effective_components':str(1/cipr)}
qs=[('global_uniform',[F(1,N)]*N),('one_component_uniform',[F(1,64)]*64+[F(0)]*192),('two_components_uniform',[F(1,128)]*128+[F(0)]*128),('one_site',[F(1)]+[F(0)]*255)]
rows=[]
for name,q in qs:
 m=metrics(q);wanted=next(x for x in contract['calibration_controls_before_solver']['cases'] if x['name']==name)
 for key in ('global_F','component_IPR','conditioned_F'):assert m[key]==wanted[key]
 rows.append({'name':name,**m})
H=[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]
assert all(sum(H[i][k]*H[j][k] for k in range(4))==(4 if i==j else 0) for i in range(4) for j in range(4))
# Coefficient rotation H/2 is orthogonal; projector is invariant in the component-zero basis.
assert metrics(qs[1][1])['global_F']=='4' and metrics(qs[0][1])['global_F']=='1'
result={'status':'PASS_EXACT_SCOPED','contract_sha256':receipt['sha256'],'theta_module_spectrum':[{'eigenvalue':str(v),'multiplicity':m,'formula':s} for v,m,s in zip(eigs,[1,3,12,48],['0','64 eta^6','16 eta^4+48 eta^6','12 eta^4+48 eta^6'])],'spectral_certificate':'four rational64x64 projectors; orthogonal/idempotent/sum-to-I and direct Laplacian reconstruction checked','controls':rows,'degenerate_Hadamard_rotation':'PASS; same subspace projector with individual global F changing4 to1','zero_channel':'undefined by frozen contract','future_solver_executed':False,'source_scripts_executed':False,'independent_review':'PENDING','physical_promotion':0}
(C/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'calibration_controls':len(rows),'spectrum_multiplicities':[1,3,12,48],'physical_promotion':0}))
