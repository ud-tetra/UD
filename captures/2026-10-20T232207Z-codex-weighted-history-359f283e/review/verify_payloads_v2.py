#!/usr/bin/env python3
"""Independent compact upper memberships and modular minor replay.
Rebuilds operators from oriented dual faces, never executes producer code.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,zipfile,math
import numpy as np
from flint import fmpz_mat,nmod_mat
P=Path(__file__).resolve().parent;B=P.parent;Z=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip';W=B/'c26_work'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
with zipfile.ZipFile(Z)as z:C=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'));R=json.loads(z.read('modular_results.json'))
S=[[tuple(s)for s in g]for g in C['simplices']];faces=defaultdict(list)
for j,t in enumerate(S[3]):
 for k in range(4):faces[t[:k]+t[k+1:]].append((j,(-1)**k))
nb=[[]for _ in range(600)]
for pair in faces.values():
 (i,a),(j,b)=pair;nb[i].append((j,a*b));nb[j].append((i,a*b))
ns=np.array([[i for i,a in x]for x in nb],dtype=np.int64);ss=np.array([[a for i,a in x]for x in nb],dtype=np.int64)
def step(v):
 out=4*v
 for k in range(4):out=out+v[:,ns[:,k]]*ss[:,k]
 return out
J=[];i=0;T=C['signed_simplex_permutations'][3]
while i not in J:J.append(i);i=T[i]['destination']
assert i==0 and len(J)==10
U=np.zeros((30,600),dtype=object)
for k,f in enumerate(R['link_simplices'][2]):
 for j,a in faces[tuple(f)]:U[k,j]=a
for k,j in enumerate(J):U[20+k,j]=1
powers=[U]
for i in range(53):powers.append(step(powers[-1]))
q=list(reversed(R['qL_coefficients']));assert all(v==0 for v in sum((a*powers[i]for i,a in enumerate(q)),np.zeros(U.shape,dtype=object)).flat)
profiles=json.loads((P/'FACTOR_RESULTS.json').read_text())['factor_rows']
def div(a,b):
 a=a[:];h=[0]*(len(a)-len(b)+1)
 for k in reversed(range(len(h))):
  v=a[k+len(b)-1];h[k]=v
  for j,w in enumerate(b):a[k+j]-=v*w
 assert not any(a);return h
zipfile_path=W/'UPPER_WITNESSES.zip';upper=[];checks=0
with zipfile.ZipFile(zipfile_path)as z:
 assert len(z.namelist())==60
 for fi,row in enumerate(profiles):
  f=row['factor_coefficients_ascending'];h=div(q,f);blocks=[]
  for sh in range(len(f)-1):blocks.append(sum((a*powers[k+sh]for k,a in enumerate(h)),np.zeros(U.shape,dtype=object)))
  for label in ['nominal','augmented']:
   name=f'{fi:02d}_{label}.json';a=json.loads(z.read(name));V=np.vstack([v[:20]for v in blocks])if label=='nominal'else np.vstack(blocks);r=row['nominal_rank_Q']if label=='nominal'else row['augmented_rank_Q'];piv=a['pivot_columns'];den=list(map(int,a['row_denominators']));br=[list(map(int,v))for v in a['basis_rows']]
   assert a['factor_index']==fi and a['label']==label and a['upper_dimension']==r and a['input_rows']==V.shape[0] and a['columns']==600;checks+=1
   assert len(piv)==len(set(piv))==r and all(type(i)is int and 0<=i<600 for i in piv);checks+=1
   assert len(br)==len(den)==r and all(d!=0 for d in den)and all(len(v)==600 for v in br);checks+=1
   assert all(br[i][piv[j]]==(den[i]if i==j else 0)for i in range(r)for j in range(r));checks+=1
   L=math.lcm(*den)if den else 1;AA=fmpz_mat(V.tolist());BB=fmpz_mat(r,600,[v for rr in br for v in rr]);XP=fmpz_mat(V.shape[0],r,[int(V[i,j])*(L//d)for i in range(V.shape[0])for j,d in zip(piv,den)])
   assert XP*BB==L*AA;checks+=1
   upper.append({'file':name,'dimension':r,'membership_identity_exact':True,'pivot_rank_identity_exact':True})
 print(json.dumps({'stage':'all60_upper_memberships','pass':True}),flush=True)
lowerfile=W/'LOWER_WITNESSES.json';lowerdata=json.loads(lowerfile.read_text());lower=[]
for w in lowerdata['witnesses']:
 label=w['case'];p=w['prime'];assert p==1009 and all(p%d for d in range(2,math.isqrt(p)+1));checks+=1
 d=np.full(600,2,dtype=np.int64);d[J]=3;seed=np.asarray(U if label=='augmented_nominal'else U[:20],dtype=np.int64);v=seed.copy();
 if label=='weighted':v=v*d
 rows=w['rows_time_major'];cols=w['columns'];r=w['rank_lower'];assert len(rows)==len(set(rows))==len(cols)==len(set(cols))==r;checks+=1
 last=max(rows)//len(seed);assert last==w['max_selected_power'] and last<600 and w['seed_rows']==len(seed);checks+=1
 blocks=[]
 for j in range(last+1):
  blocks.append(v%p);v=(step(v*d)*d)%p if label=='weighted'else step(v)%p
 H=np.vstack(blocks);det=int(nmod_mat(H[np.ix_(rows,cols)].tolist(),p).det());assert det==w['determinant_mod_prime'] and 0<det<p;checks+=1
 lower.append({'case':label,'rank_lower':r,'minor_dimension':r,'determinant_mod1009':det,'max_power_used':last,'pass':True})
result={'status':'PASS_ALL60_COMPACT_UPPER_MEMBERSHIPS_AND_THREE_MODULAR_MINORS','check_count':checks,'upper_payload_count':len(upper),'upper_membership_matrix_entries':sum((row['degree']*20+row['degree']*30)*600 for row in profiles),'source_archive_sha256':sha(Z),'upper_archive_sha256':sha(zipfile_path),'lower_witness_sha256':sha(lowerfile),'independent_factor_result_sha256':sha(P/'FACTOR_RESULTS.json'),'upper':upper,'lower':lower,'scope':{'independent_operator_construction':'signed dual-face adjacency','no_producer_or_archived_program_execution':True,'no_full2640_rank_or_SVD':True,'constructor_fmpz_rank_not_needed_for_replayed_upper_bound':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'PAYLOAD_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'checks':checks,'upper_files':len(upper),'minor_determinants':[x['determinant_mod1009']for x in lower]},indent=2))
