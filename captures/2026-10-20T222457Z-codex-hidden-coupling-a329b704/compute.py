from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,deque
from decimal import Decimal,localcontext
import json,zipfile,hashlib,math,argparse
parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,required=True);parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
R=args.repo.resolve();O=args.out.resolve()
assert O!=R and R not in O.parents,'Output must be outside the append-only repository'
O.mkdir(parents=True,exist_ok=False)
Z=R/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
members=['sources/COMPLEX_AND_ACTION.json','modular_results.json','RESULTS.json'];bindings=[];data={}
with zipfile.ZipFile(Z)as z:
 for n in members:
  b=z.read(n);data[n]=json.loads(b);bindings.append({'member':n,'sha256':sha(b),'bytes':len(b)})
C=data[members[0]];M=data[members[1]];old=data[members[2]]
S=[[tuple(s) for s in grade] for grade in C['simplices']];dims=list(map(len,S));assert dims==[120,720,1200,600]
index=[{s:i for i,s in enumerate(g)}for g in S];off=[0,120,840,2040]
for k in [2,3]:
 for s in S[k]:
  chain=defaultdict(int)
  for j in range(k+1):
   f=s[:j]+s[j+1:]
   for l in range(k):chain[f[:l]+f[l+1:]]+=(-1)**(j+l)
  assert all(v==0 for v in chain.values())
faces=defaultdict(list)
for t,s in enumerate(S[3]):
 for j in range(4):faces[s[:j]+s[j+1:]].append((t,(-1)**j))
assert len(faces)==1200 and all(len(v)==2 for v in faces.values())
adj=defaultdict(list)
for a,b in faces.values():
 i,si=a;j,sj=b;adj[i].append((j,-si*sj));adj[j].append((i,-si*sj))
h=[None]*600;h[0]=1;queue=deque([0])
while queue:
 i=queue.popleft()
 for j,f in adj[i]:
  v=h[i]*f
  if h[j]is None:h[j]=v;queue.append(j)
  else:assert h[j]==v
assert all(v in(-1,1)for v in h)
assert all(sum(h[t]*s for t,s in rows)==0 for rows in faces.values())
link=[]
for k in range(3):link.append([s for s in S[k]if 0 not in s and tuple(sorted((0,)+s))in index[k+1]])
obs=[off[k]+index[k][s]for k in range(3)for s in link[k]]
assert obs==M['observed_indices'] and list(map(len,link))==[12,30,20]
assert len(set(obs))==62 and all(i<2040 for i in obs)
# Exact unnormalized harmonic images: B1^T*ones=0, B3*h=0.
assert all(-1+1==0 for e in S[1])
# Independently check the declared T action against actual simplex images/signs.
vp=C['vertex_permutation'];T=C['signed_simplex_permutations']
assert sorted(vp)==list(range(120))
for k,g in enumerate(S):
 assert sorted(a['destination']for a in T[k])==list(range(len(g)))
 for i,s in enumerate(g):
  image=[vp[v]for v in s];sign=(-1)**sum(image[a]>image[b]for a in range(len(image))for b in range(a+1,len(image)))
  assert T[k][i]=={'destination':index[k][tuple(sorted(image))],'sign':sign}
  if k==0:assert sign==1
  if k==3:assert h[T[k][i]['destination']]==sign*h[i]
for k,g in enumerate(S):
 for i in range(len(g)):
  j=i;sg=1
  for _ in range(10):sg*=T[k][j]['sign'];j=T[k][j]['destination']
  assert j==i and sg==1
def trim(p):
 while p and p[-1]==0:p.pop()
 return p
def rem(a,b):
 a=list(map(F,a));b=list(map(F,b))
 while len(a)>=len(b):
  f=a[-1]/b[-1];d=len(a)-len(b)
  for j in range(len(b)):a[d+j]-=f*b[j]
  trim(a)
 return a
def primitive(p):
 if not p:return []
 den=math.lcm(*(v.denominator for v in p));a=[int(v*den)for v in p];g=math.gcd(*a);return [F(v//g)for v in a]
def value(p,x):
 r=F(0)
 for v in reversed(p):r=r*x+v
 return r
q=list(reversed(M['qL_coefficients']));assert len(q)==54 and q[0]==0 and q[1]!=0 and q[-1]==1
q1=q[1:];sturm=[list(map(F,q1)),[F(i*q1[i])for i in range(1,len(q1))]]
while sturm[-1]:
 r=rem(sturm[-2],sturm[-1])
 if not r:break
 sturm.append(primitive([-v for v in r]))
assert len(sturm[-1])==1 # q1 squarefree, and q has a simple zero root.
def variation(x):
 signs=[1 if v>0 else -1 for p in sturm if (v:=value(p,x))!=0]
 return sum(a!=b for a,b in zip(signs,signs[1:]))
assert value(q1,0)!=0 and value(q1,16)!=0 and variation(0)-variation(16)==52
assert old['dynamic_observation_rank']==1893 and old['dynamic_unobservable_dimension']==747
assert old['stationary_dark_dimension']==1 and old['oscillatory_dark_dimension']==746
observed_ranks=[r['dynamic_rank_C']for r in old['complex_sector_results']];assert sum(observed_ranks)==2523
def fs(v):return str(v.numerator)+'/'+str(v.denominator)
def sqrt_bounds(v,bits=160):
 assert v>=0
 n=math.isqrt((v.numerator<<(2*bits))//v.denominator);l=F(n,1<<bits);u=F(n+1,1<<bits)
 assert l*l<=v<u*u
 return l,u
def display(v):
 with localcontext()as c:c.prec=25;return str(Decimal(v.numerator)/Decimal(v.denominator))
N=4096;variance=F(N*N-1,48);fourth=F((N*N-1)*(3*N*N-7),3840);a=F(N-1,4)
assert sum((F(j,2)-a)**2 for j in range(N))/N==variance
assert sum((F(j,2)-a)**4 for j in range(N))/N==fourth
rows=[]
for k in[20,30,40]:
 e=F(1,2**k);assert value(q,e*e)!=0 and e*a<1
 upper=e*e*variance;lower=upper-e**4*fourth/3;assert 0<lower<upper<F(1,2)
 lo=sqrt_bounds(lower/10)[0];hi=sqrt_bounds(upper/10)[1]
 condition=sqrt_bounds((1-upper)/upper)[0]
 rows.append({'epsilon':fs(e),'M':N,'spacing':'1/2','center_time':fs(a),'centered_time_variance':fs(variance),'centered_fourth_moment':fs(fourth),'mean_centered_sine_squared_lower':fs(lower),'mean_centered_sine_squared_upper':fs(upper),'harmonic_plane_weak_singular_lower':fs(lo),'harmonic_plane_weak_singular_upper':fs(hi),'full_map_smallest_positive_singular_upper':fs(hi),'full_map_positive_condition_lower':fs(condition),'display_plane_weak_singular_interval':[display(lo),display(hi)],'display_condition_lower':display(condition),'scope':'Certified bounds for normalized62channel state-observation map; no full-Hankel or321column estimator condition claim'})
result={'status':'EXACT_CONDITIONAL_HIDDEN_COUPLING_THEOREM','native_identities_newly_checked':{'chain_dimensions':dims,'boundary_squared_zero':True,'dual_connected_and_fundamental_cycle_closed':True,'fundamental_cycle_norm_squared':600,'uniform_vertex_norm_squared':120,'link_f_vector':[12,30,20],'observed_uniform_vertex_norm_squared':12,'Ru_norm_squared':'1/10','Rh_zero':True,'both_harmonics_T_fixed':True,'signed_T_reconstructed_and_T_power10_identity':True,'q_squarefree_degree':53,'q_nonzero_roots_in_0_16':52},'inherited_not_recomputed':{'nominal_history_rank':1893,'nominal_hidden_dimension':747,'harmonic_dimension':2,'isolated_sector_ranks':observed_ranks},'derived':{'perturbed_history_rank':1894,'perturbed_hidden_dimension':746,'nonaliased_sampling_sufficient_M':106,'m0_rank':256,'m0_hidden':8,'sum_isolated_sector_ranks':2524,'individually_dark_dimension':116,'mixed_dark_quotient_dimension':630,'unrestricted_hidden_skew_parameter_dimension':747*746//2,'preserves':['Euclidean skewness and norm','declaredC10 action','odd chain-parity anticommutation'],'does_not_preserve_or_claim':['native adjacent-degree HodgeDirac form','locality','Pachner or incidence provenance','physical source law']},'rows':rows,'physical_promotion':0,'external_review':'PENDING'}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(O/'HARMONIC_WITNESS.json').write_text(json.dumps({'u0':{'grade':0,'coefficients':[1]*120,'normalizer_squared':120},'h0':{'grade':3,'coefficients':h,'normalizer_squared':600},'orientation_anchor':'first sorted tetrahedron coefficient+1','epsilon_perturbation':'epsilon*(u*h^T-h*u^T), u=u0/sqrt120,h=h0/sqrt600','no_dense_perturbation_matrix_allocated':True,'observed_indices':obs},indent=2)+'\n')
(O/'SOURCE_BINDINGS.json').write_text(json.dumps({'source_archive':str(Z.relative_to(R)),'source_archive_sha256':sha(Z.read_bytes()),'members':bindings,'read_only_JSON_intake':True,'archived_scripts_executed':0,'basis_rank_claims_inherited_not_replayed':True},indent=2)+'\n')
print(json.dumps({'status':result['status'],'rows':[{'epsilon':r['epsilon'],'weak_singular':r['display_plane_weak_singular_interval'],'condition_lower':r['display_condition_lower']}for r in rows]},indent=2))
