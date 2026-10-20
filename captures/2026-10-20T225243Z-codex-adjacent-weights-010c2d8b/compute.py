from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,deque
from decimal import Decimal,localcontext
import argparse,json,zipfile,hashlib,math
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
R=args.repo.resolve();O=args.out.resolve();assert R!=O and R not in O.parents;O.mkdir(parents=True,exist_ok=False)
Z=R/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
sha=lambda b:hashlib.sha256(b).hexdigest();names=['sources/COMPLEX_AND_ACTION.json','modular_results.json','RESULTS.json'];raw={}
with zipfile.ZipFile(Z)as z:
 for n in names:raw[n]=z.read(n)
C,M,old=[json.loads(raw[n])for n in names];S=[[tuple(s)for s in g]for g in C['simplices']];dims=list(map(len,S));assert dims==[120,720,1200,600]
ix=[{s:i for i,s in enumerate(g)}for g in S];off=[0,120,840,2040];B=[None]
for k in range(1,4):B.append([{ix[k-1][s[:j]+s[j+1:]]:(-1)**j for j in range(k+1)}for s in S[k]])
def apply(cols,v):
 out=defaultdict(int)
 for j,c in v.items():
  for i,a in cols[j].items():out[i]+=a*c
 return {i:a for i,a in out.items()if a}
chain_checks=0
for k in [2,3]:
 for col in B[k]:assert not apply(B[k-1],col);chain_checks+=1
AI=[]
for k in range(1,4):
 cols=[{}for _ in range(2640)]
 for j,col in enumerate(B[k]):
  for i,a in col.items():cols[off[k]+j][off[k-1]+i]=-a;cols[off[k-1]+i][off[k]+j]=a
 AI.append(cols)
cross_checks=0
for a in range(3):
 for b in range(3):
  if a==b:continue
  for col in AI[b]:assert not apply(AI[a],col);cross_checks+=1
A=[{}for _ in range(2640)]
for ai in AI:
 for j,col in enumerate(ai):
  for i,v in col.items():assert i not in A[j];A[j][i]=v
for j,col in enumerate(A):
 for i,a in col.items():assert A[i][j]==-a
max_abs_row=max(sum(abs(v)for v in col.values())for col in A);assert max_abs_row==12
L=[[s for s in S[k]if 0 not in s and tuple(sorted((0,)+s))in ix[k+1]]for k in range(3)]
assert list(map(len,L))==[12,30,20];observed=[off[k]+ix[k][s]for k in range(3)for s in L[k]];assert observed==M['observed_indices']
cochain_entries=[]
for k in[1,2]:
 lower={ix[k-1][s]for s in L[k-1]};entries=0
 for s in L[k]:
  col=B[k][ix[k][s]];assert set(col)<=lower;entries+=len(col)
 cochain_entries.append(entries)
assert cochain_entries==[60,60]
faces=defaultdict(list)
for j,col in enumerate(B[3]):
 for i,a in col.items():faces[i].append((j,a))
assert all(len(v)==2 for v in faces.values());adj=defaultdict(list)
for a,b in faces.values():
 i,si=a;j,sj=b;adj[i].append((j,-si*sj));adj[j].append((i,-si*sj))
h=[None]*600;h[0]=1;q=deque([0])
while q:
 i=q.popleft()
 for j,s in adj[i]:
  v=h[i]*s
  if h[j]is None:h[j]=v;q.append(j)
  else:assert h[j]==v
assert all(v in[-1,1]for v in h)and not apply(B[3],dict(enumerate(h)))
assert not apply(A,{2040+i:v for i,v in enumerate(h)})
T=C['signed_simplex_permutations'];vp=C['vertex_permutation']
for k,g in enumerate(S):
 for j,s in enumerate(g):
  im=[vp[v]for v in s];sg=(-1)**sum(im[a]>im[b]for a in range(len(im))for b in range(a+1,len(im)))
  assert T[k][j]=={'destination':ix[k][tuple(sorted(im))],'sign':sg}
  if k==3:assert h[T[k][j]['destination']]==sg*h[j]
tau=ix[3][(0,33,34,41)];assert tau==0;orbit=[];j=tau
while j not in orbit:orbit.append(j);j=T[3][j]['destination']
assert len(orbit)==10 and j==tau
def fs(v):return str(v.numerator)+'/'+str(v.denominator)
def brackets(v,bits=160):
 n=math.isqrt((v.numerator<<(2*bits))//v.denominator);a=F(n,1<<bits);b=F(n+1,1<<bits);assert a*a<=v<b*b;return a,b
def display(v):
 with localcontext()as c:c.prec=25;return str(Decimal(v.numerator)/Decimal(v.denominator))
assert F(7*13**2,6*64**2)<F(1,16)
cases=[];parity_checks=0;metric_checks=0
for label,ids in [('single_tetrahedron',[tau]),('C10_tetrahedron_orbit',orbit)]:
 J=set(ids);m=len(J);b=apply(B[3],{i:h[i]for i in J})
 assert sum(v*v for v in b.values())==4*m
 for i in ids:
  for j in ids:assert sum(v*B[3][j].get(k,0)for k,v in B[3][i].items())==(4 if i==j else 0)
 obs_b={off[2]+i:v for i,v in b.items()if off[2]+i in observed};assert obs_b==({1680:1}if m==1 else{1680:1,1689:1})
 invariant={T[3][i]['destination']for i in J}==J;assert invariant==(m==10)
 rows=[]
 for e in[F(1,2),F(-1,2),F(1,2**20),F(1,2**40)]:
  d={i:(1+e if i in J else F(1))for i in range(600)};assert min(d.values())>0
  z={i:F(h[i])/d[i]for i in range(600)};assert not apply(B[3],{i:d[i]*z[i]for i in range(600)})
  old_bz=apply(B[3],z);assert old_bz=={i:-e*v/(1+e)for i,v in b.items()}
  zn=sum(v*v for v in z.values());inner=sum(h[i]*z[i]for i in range(600));sine2=F(1)-inner**2/(600*zn)
  expected=F(m*(600-m))*e*e/(600*((600-m)*(1+e)**2+m));assert sine2==expected>0
  # F K_D F^-1 = H^-1 A, H=diag(I,I,I,D^-2), and R F=R.
  for j,col in enumerate(B[3]):
   for i,v in col.items():
    assert (-v*d[j])/d[j]==-v
    assert d[j]*(d[j]*v)==d[j]**2*v
    assert (1/d[j]**2)*(d[j]**2*v)==v;metric_checks+=1
  assert all(i<2040 for i in observed)
  lo2=(F(15)*abs(e)/1024)**2/600;hi2=(F(17)*abs(e)/1024)**2/600
  lo=brackets(lo2)[0];hi=brackets(hi2)[1];angle=brackets(sine2)
  rows.append({'epsilon':fs(e),'new_dark_line_sine_squared':fs(sine2),'new_dark_line_sine_bracket':[fs(v)for v in angle],'sample_time':'1/64','named_face_global_index':1680,'signed_derivative':'-epsilon/sqrt600','finite_signal_magnitude_lower':fs(lo),'finite_signal_magnitude_upper':fs(hi),'finite_signal_display_interval':[display(lo),display(hi)],'conditional_disjoint_scalar_error_sufficient_upper':fs(lo/2),'scope':'Model response for exact initial h; total scalar error bound must be independently supplied under each hypothesis; no actual instrument gate'})
 cases.append({'label':label,'tetrahedron_indices':ids,'selected_count':m,'preserves_C10':invariant,'selected_boundary_Gram':'4*identity','perturbation_operator_norm':'2*abs(epsilon)','observed_derivative_coefficients':{str(i):-v for i,v in obs_b.items()},'unnormalized_weighted_boundary_h_norm_squared':4*m,'weighted_fundamental_cycle':'z_i=h0_i/(1+epsilon) on selected tetrahedra; h0_i otherwise','kernel_dimension':'NOT_COMPUTED; changing a hidden line does not prove shrinkage','rows':rows})
assert old['dynamic_unobservable_dimension']==747 and old['dynamic_observation_rank']==1893
result={'status':'DERIVED_GRADE_RATE_INVARIANCE_AND_WEIGHTED_KERNEL_MOTION','new_exact_checks':{'chain_dimensions':dims,'boundary_squared_columns':chain_checks,'vanishing_cross_channel_columns':cross_checks,'cochain_restriction_entries':cochain_entries,'max_abs_row_sum_A':12,'source_fundamental_cycle_closed':True,'metric_transform_triplet_checks':metric_checks,'orbit_length':10,'all_selected_boundary_columns_orthogonal':True,'finite_sample_relative_remainder_upper':'1183/24576','relative_remainder_less_than':'1/16'},'inherited_premises_not_rerun':{'nominal_dynamic_rank':1893,'nominal_dynamic_kernel':747,'nominal_observer_largest_invariant_kernel':True},'derived_rate_result':{'all_constant_nonzero_rates':'same N, dimension747 and historyrank1893; even at weighted-frequency collisions','arbitrary_locally_integrable_rates':'nominal N remains invariant/invisible; no equality claim','all_rates_zero':{'snapshot_and_history_rank':62,'kernel':2578},'physical_rate_selection':'OPEN'},'weighted_cases':cases,'source_supported_physical_constitutive_law':False,'new_fit_or_estimator_calls':0,'new_raw_acquisitions':0,'physical_promotion':0,'external_review':'PENDING'}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(O/'WITNESS.json').write_text(json.dumps({'fundamental_cycle_C3_coefficients':h,'anchor_tetrahedron':list(S[3][tau]),'C10_orbit':orbit,'observed_indices':observed,'nominal_h_normalizer_squared':600,'fixed_coordinates':'x for weighted-boundary unit-metric model','metric_coordinates':'y=diag(I,I,I,D)x; same readout values but transported preparation y0=D*h0, not h0'},indent=2)+'\n')
(O/'SOURCE_BINDINGS.json').write_text(json.dumps({'archive_path':str(Z.relative_to(R)),'archive_sha256':sha(Z.read_bytes()),'JSON_members':[{'path':n,'sha256':sha(raw[n]),'bytes':len(raw[n])}for n in names],'archived_scripts_executed':0,'nominal_rank_proofs_inherited_not_replayed':True},indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':result['new_exact_checks'],'cases':[{'label':c['label'],'C10':c['preserves_C10'],'signal_epsilon_2^-40':c['rows'][-1]['finite_signal_display_interval']}for c in cases]},indent=2))
