#!/usr/bin/env python3
"""Independent exact top-channel factor ranks from sparse face adjacency.
No archived program or native2640-observer rank is executed.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,zipfile,time
import numpy as np
from flint import fmpz_mat,nmod_mat
P=Path(__file__).resolve().parent;B=P.parent;Z=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(Z)as z:
 raw={n:z.read(n)for n in ['sources/COMPLEX_AND_ACTION.json','modular_results.json','HIDDEN_WITNESSES.json']}
C=json.loads(raw['sources/COMPLEX_AND_ACTION.json']);R=json.loads(raw['modular_results.json']);H=json.loads(raw['HIDDEN_WITNESSES.json']);S=[[tuple(s)for s in g]for g in C['simplices']]
faces=defaultdict(list)
for j,t in enumerate(S[3]):
 for k in range(4):faces[t[:k]+t[k+1:]].append((j,(-1)**k))
assert len(faces)==1200 and all(len(x)==2 for x in faces.values())
neighbors=[[]for _ in range(600)]
for pair in faces.values():
 (i,a),(j,b)=pair;neighbors[i].append((j,a*b));neighbors[j].append((i,a*b))
assert all(len(x)==4 and len({i for i,a in x})==4 for x in neighbors)
nb=np.array([[i for i,a in x]for x in neighbors],dtype=np.int64);sg=np.array([[a for i,a in x]for x in neighbors],dtype=np.int64)
J=[];i=S[3].index((0,33,34,41));T=C['signed_simplex_permutations'][3]
while i not in J:J.append(i);i=T[i]['destination']
assert i==J[0]and len(J)==10
U=np.zeros((30,600),dtype=object)
for k,f in enumerate(R['link_simplices'][2]):
 for j,a in faces[tuple(f)]:U[k,j]=a
for k,j in enumerate(J):U[20+k,j]=1
# G is rebuilt as signed dual-face adjacency, not B.T@B from the producer.
def rightG(v):
 w=4*v
 for k in range(4):w=w+v[:,nb[:,k]]*sg[:,k]
 return w
powers=[U]
for j in range(53):powers.append(rightG(powers[-1]))
q=list(reversed(R['qL_coefficients']));assert len(q)==54 and q[-1]==1
ann=sum((a*v for a,v in zip(q,powers)),np.zeros(U.shape,dtype=object));assert all(int(x)==0 for x in ann.flat)
def mul(a,b):
 p=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):p[i+j]+=x*y
 return p
def divmonic(a,b):
 p=a[:];out=[0]*(len(a)-len(b)+1)
 for k in reversed(range(len(out))):
  c=p[k+len(b)-1];out[k]=c
  for j,x in enumerate(b):p[k+j]-=c*x
 assert not any(p);return out
fs=[[0,1]]+[[-k,1]for k in [3,4,5,6,7,8,9,12,14,15]]+[[a,b,1]for a,b in [(80,-20),(36,-18),(55,-15),(44,-14),(23,-11),(27,-11),(29,-11),(5,-10),(23,-10),(9,-9),(15,-9),(11,-8),(1,-7),(11,-7),(3,-5),(1,-3)]]+[[-28,33,-11,1],[-24,33,-11,1],[464,-484,165,-22,1]]
prod=[1]
for f in fs:prod=mul(prod,f)
assert prod==q
rows=[];r0=0;raug=0
for f in fs:
 h=divmonic(q,f);assert mul(h,f)==q
 blocks=[]
 for shift in range(len(f)-1):
  v=sum((a*powers[k+shift]for k,a in enumerate(h)),np.zeros(U.shape,dtype=object));blocks.append(v)
 nom=np.vstack([v[:20]for v in blocks]);aug=np.vstack(blocks)
 n=int(fmpz_mat(nom.tolist()).rank());a=int(fmpz_mat(aug.tolist()).rank());r0+=n;raug+=a
 rows.append({'factor_coefficients_ascending':f,'degree':len(f)-1,'nominal_rank_Q':n,'augmented_rank_Q':a,'augmented_rows':aug.shape[0]})
 print(json.dumps(rows[-1]),flush=True)
# Separate lower witness at one prime; modular rank is used only as lower bound.
p=1009;d=np.full(600,2,dtype=np.int64);d[J]=3;v=np.asarray(U[:20],dtype=np.int64)*d;stack=[]
for j in range(600):
 stack.append(v.copy());v=(rightG(v*d)*d)%p
assert 72*(p-1)<2**63
rw=int(nmod_mat(np.vstack(stack).tolist(),p).rank())
assert r0==390 and raug==444 and rw==443
# The augmented cyclic space contains h and P_J h, hence D^-1h; its nonzero harmonic line gives weighted upper raug-1.
weighted_upper=raug-1;assert rw==weighted_upper
full=1893+2*(rw-r0)
result={'status':'PASS_EXACT_NOMINAL_AND_AUGMENTED_FACTOR_RANKS_WEIGHTED_SANDWICH','source_archive_sha256':sha(Z.read_bytes()),'JSON_member_sha256':{n:sha(b)for n,b in raw.items()},'construction':'Signed dual-face adjacency and explicit observed boundary rows from JSON','U_q_G_zero_exact':True,'q_factor_product_matches_authoritative_coefficients':True,'factor_rows':rows,'nominal_top_rank_Q':r0,'augmented_nominal_rank_Q':raug,'weighted_modular_lower_prime':p,'weighted_modular_lower':rw,'weighted_exact_upper':weighted_upper,'weighted_rank_Q_sandwich':rw,'derived_full_rank_using_inherited1893':full,'derived_full_kernel_dimension':2640-full,'scope':{'factor_rank_evaluations':'python-flint exact fmpz_mat rank, separate from modular lower','rank_upper_uses_exact_primary_factor_decomposition_and_UqG_identity':True,'native_full_observer_rank1893_inherited_not_rerun':True,'no_full_weighted2640_rank_matrix_or_SVD':True,'finite_conditioning_not_certified':True,'new_raw_or_estimator_calls':0,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'FACTOR_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'r0':r0,'raug':raug,'rweighted':rw,'full':full},indent=2))
