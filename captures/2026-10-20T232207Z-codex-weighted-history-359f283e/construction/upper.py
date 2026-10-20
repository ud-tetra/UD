from pathlib import Path
from fractions import Fraction as F
import json,zipfile,math,time,gzip,hashlib
import numpy as np
from flint import fmpz_mat
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';O=P/'c26_work';W=O/'upper';W.mkdir(exist_ok=True)
with np.load(O/'OPERATORS.npz',allow_pickle=False)as z:G=z['G'];C=z['C0'];J=z['J'].tolist()
U=np.vstack([C,np.eye(600,dtype=np.int64)[J]]).astype(object)
Z=R/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:q=list(reversed(json.loads(z.read('modular_results.json'))['qL_coefficients']))
fs=[[0,1]]+[[-k,1]for k in[3,4,5,6,7,8,9,12,14,15]]+[[a,b,1]for a,b in[(80,-20),(36,-18),(55,-15),(44,-14),(23,-11),(27,-11),(29,-11),(5,-10),(23,-10),(9,-9),(15,-9),(11,-8),(1,-7),(11,-7),(3,-5),(1,-3)]]+[[-28,33,-11,1],[-24,33,-11,1],[464,-484,165,-22,1]]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
prod=[1]
for f in fs:prod=mul(prod,f)
assert prod==q
def divide(a,b):
 a=list(a);r=[0]*(len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);x=a[-1];r[k]=x
  for j,y in enumerate(b):a[k+j]-=x*y
  while a and a[-1]==0:a.pop()
 assert not a;return r
cols=[[(int(i),int(G[i,j]))for i in np.flatnonzero(G[:,j])]for j in range(600)]
def step(A):
 out=np.zeros(A.shape,dtype=object)
 for j,col in enumerate(cols):
  for i,c in col:out[:,j]+=c*A[:,i]
 return out
start=time.perf_counter();powers=[U]
for _ in range(53):powers.append(step(powers[-1]))
ann=sum((a*powers[i]for i,a in enumerate(q)),np.zeros(U.shape,dtype=object));assert all(x==0 for x in ann.flat)
records=[];basisfiles=[]
def upper(V,label,fi):
 A=fmpz_mat(V.tolist());E,den,rank=A.rref();den=int(den)
 piv=[]
 for i in range(rank):piv.append(next(j for j in range(600)if E[i,j]!=0))
 assert len(set(piv))==rank
 B=fmpz_mat(rank,600,[E[i,j]for i in range(rank)for j in range(600)])
 assert all(B[i,piv[j]]==(den if i==j else 0)for i in range(rank)for j in range(rank))
 VP=fmpz_mat(V.shape[0],rank,[A[i,j]for i in range(V.shape[0])for j in piv])
 assert VP*B==den*A
 payload={'factor_index':fi,'label':label,'denominator':str(den),'pivot_columns':piv,'basis_rows':[[str(B[i,j])for j in range(600)]for i in range(rank)],'input_rows':V.shape[0],'columns':600,'upper_dimension':rank,'membership_identity':'V[:,piv]*B=den*V; B[:,piv]=den*I'}
 b=(json.dumps(payload,separators=(',',':'))+'\n').encode();name=f'{fi:02d}_{label}.json.gz';out=gzip.compress(b,mtime=0);(W/name).write_bytes(out);basisfiles.append({'path':'upper/'+name,'sha256':hashlib.sha256(out).hexdigest(),'bytes':len(out),'uncompressed_bytes':len(b)})
 return rank
for fi,f in enumerate(fs):
 h=divide(q,f);degree=len(f)-1;Vs=[]
 for j in range(degree):Vs.append(sum((a*powers[i+j]for i,a in enumerate(h)),np.zeros(U.shape,dtype=object)))
 V=np.vstack(Vs);V0=np.vstack([v[:20]for v in Vs]);rw=upper(V,'augmented',fi);r0=upper(V0,'nominal',fi)
 rec={'factor_index':fi,'coefficients_ascending':f,'degree':degree,'nominal_upper':r0,'augmented_upper':rw};records.append(rec);print(json.dumps(rec),flush=True)
 if fi==0:
  hrow=V[20];assert all(abs(int(v))==abs(int(hrow[0]))for v in hrow)and hrow[0]!=0
result={'status':'PASS_EXACT_FACTOR_ROW_MEMBERSHIP_UPPER_CERTIFICATES','annihilator_seed_rows':30,'annihilator_degree':53,'U_q_G_zero_entries_checked':18000,'factors':records,'nominal_rank_upper':sum(r['nominal_upper']for r in records),'augmented_dimension_upper':sum(r['augmented_upper']for r in records),'basis_files':basisfiles,'elapsed_seconds':time.perf_counter()-start,'physical_promotion':0}
(O/'UPPER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'nominal_upper':result['nominal_rank_upper'],'augmented_upper':result['augmented_dimension_upper'],'elapsed':result['elapsed_seconds']}),flush=True)
