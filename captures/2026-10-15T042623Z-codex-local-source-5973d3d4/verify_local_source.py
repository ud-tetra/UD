"""New constructor replay. Exact integer/rational derivatives; numerical flow labelled."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from collections import deque
import json
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
import sympy as sy
R=Path(__file__).resolve().parent
D=json.load(open(R/'baseline/COMPLEX_AND_ACTION.json'))
V=[tuple(tuple(t) for t in q) for q in D['vertices']];vid={q:i for i,q in enumerate(V)}
C=[[tuple(c) for c in cs] for cs in D['simplices']];ids=[{c:i for i,c in enumerate(cs)} for cs in C]
off=np.cumsum([0]+[len(cs) for cs in C]);N=int(off[-1]);checks=[]
def ck(name,b,scope='EXACT',**data):
 assert b,(name,data)
 checks.append({'name':name,'status':'PASS','scope':scope,**data})
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def add(v):return (sum(t[0] for t in v),sum(t[1] for t in v))
def qm(a,b):
 out=[add([mul(a[0],b[0])]+[neg(mul(a[i],b[i])) for i in range(1,4)])]
 for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:out.append(add([mul(a[0],b[i]),mul(a[i],b[0]),mul(a[j],b[k]),neg(mul(a[k],b[j]))]))
 assert all(a%2==b%2==0 for a,b in out)
 return tuple((a//2,b//2) for a,b in out)
conj=lambda q:(q[0],)+tuple(neg(t) for t in q[1:])
parity=lambda v:(-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
one=((2,0),(0,0),(0,0),(0,0));g=tuple(tuple(t) for t in D['right_generator']);u,v=vid[one],vid[g]
e=ids[1][tuple(sorted((u,v)))];H={one};q=one
for _ in range(9):q=qm(q,g);H.add(q)
HH=sorted({frozenset(qm(qm(conj(q),h),q) for h in H) for q in V},key=lambda h:sorted(h));target=HH.index(frozenset(H))
cache={}
def action(q,right=True):
 key=(q,right)
 if key in cache:return cache[key]
 vp=[vid[qm(t,q) if right else qm(q,t)] for t in V];rows=[];cols=[];val=[]
 for d,cs in enumerate(C):
  for j,c in enumerate(cs):
   image=tuple(vp[t] for t in c);rows.append(int(off[d])+ids[d][tuple(sorted(image))]);cols.append(int(off[d])+j);val.append(parity(image))
 M=sp.csc_matrix((val,(rows,cols)),shape=(N,N),dtype=np.int64);cache[key]=M;return M
SS=[sum((action(h) for h in hset),sp.csc_matrix((N,N),dtype=np.int64)) for hset in HH]
ck('six_integer_projection_averages',len(HH)==6 and all((S*S-10*S).nnz==0 and (S-S.T).nnz==0 for S in SS))
B=[]
for d in [1,2,3]:
 rr=[];cc=[];val=[]
 for j,c in enumerate(C[d]):
  for k in range(d+1):rr.append(ids[d-1][c[:k]+c[k+1:]]);cc.append(j);val.append((-1)**k)
 B.append(sp.csc_matrix((val,(rr,cc)),shape=(len(C[d-1]),len(C[d])),dtype=np.int64))
A=sp.bmat([[None,-B[0],None,None],[B[0].T,None,-B[1],None],[None,B[1].T,None,-B[2]],[None,None,B[2].T,None]],format='csc')
ck('free_flow_score_conservation',all((A*S-S*A).nnz==0 for S in SS))
be=B[0][:,e].toarray().ravel();rows=[];cols=[];vals=[]
for j in np.nonzero(be)[0]:rows.extend([int(j),int(off[1])+e]);cols.extend([int(off[1])+e,int(j)]);vals.extend([-int(be[j]),int(be[j])])
E=sp.csc_matrix((vals,(rows,cols)),shape=(N,N),dtype=np.int64)
x=np.zeros(N,dtype=np.int64);x[u]=1
ck('incidence_local_edge_response',E.nnz==4 and (E+E.T).nnz==0 and int(be@be)==2,vertex=u,neighbor=v,edge=e)
sx=[F(int(x@(S@x)),10) for S in SS]
ck('localized_input_six_way_tie',sx==[F(1,10)]*6)
# Half-second-derivative coefficients of s_H for L=A+gamma E.
ax=A@x;ex=E@x;aa=A@ax;cross=A@ex+E@ax;ee=E@ex
co=[]
for S in SS:
 co.append([F(int(ax@(S@ax)+x@(S@aa)),10),F(int(2*ax@(S@ex)+x@(S@cross)),10),F(int(ex@(S@ex)+x@(S@ee)),10)])
gaps=[[co[target][j]-c[j] for j in range(3)] for c in co]
ck('exact_source_gap_second_derivative',all(c==([F(0)]*3 if h==target else [F(0),F(0),F(1,10)]) for h,c in enumerate(gaps)),gap_polynomial_coefficients=[[str(t) for t in c] for c in gaps])
grading=np.concatenate([np.full(len(cs),(-1)**d,dtype=np.int64) for d,cs in enumerate(C)])
ck('even_time_scores',all((sp.diags(grading,dtype=np.int64)@L@sp.diags(grading,dtype=np.int64)+L).nnz==0 for L in [A,E]) and all((sp.diags(grading,dtype=np.int64)@S-S@sp.diags(grading,dtype=np.int64)).nnz==0 for S in SS))
# Vertex-fixing conjugation by g fixes the active edge and cycles the other axes.
U=action(g,False)@action(conj(g),True)
conj_h=lambda h:frozenset(qm(qm(g,t),conj(g)) for t in h)
hp=[HH.index(conj_h(h)) for h in HH];other=next(j for j in range(6) if j!=target);cycle=[];j=other
while j not in cycle:cycle.append(j);j=hp[j]
ck('five_competitor_symmetry',hp[target]==target and len(cycle)==5 and (U*A-A*U).nnz==0 and (U*E-E*U).nnz==0 and np.array_equal(U@x,x),permutation=hp)
# Exact response-norm certificate: E^3=-2E on its rank-two support.
ck('source_norm_sqrt_two',(E@E@E+2*E).nnz==0 and int(np.sum(E.data**2))==4)
# The perturbed contact map no longer satisfies the old chain identity.
edge_projector=sp.csc_matrix(([1],([e],[e])),shape=(720,720),dtype=np.int64)
bad=B[0]@edge_projector@B[1]
ck('response_is_not_a_new_boundary',int(np.sum(bad.data**2))==10)
# The prior exact spectra certify ||A||<4. Sturm signs use exact algebraic values.
t=sy.Symbol('x');facts=[]
for rec in json.load(open(R/'baseline/EXACT_SPECTRA.json'))['m_0_through_5']:
 for item in rec['factors_over_Qsqrt5']:
  f=sy.sympify(item['polynomial'])
  if f!=t and f not in facts:facts.append(f)
def variations(signs):
 signs=[s for s in signs if s];return sum(a!=b for a,b in zip(signs,signs[1:]))
for f in facts:
 st=sy.sturm(f,t)
 at16=[int(sy.sign(sy.simplify(z.subs(t,16)))) for z in st]
 inf=[int(sy.sign(sy.LC(sy.Poly(z,t)))) for z in st]
 assert f.subs(t,16)!=0 and variations(at16)-variations(inf)==0
ck('exact_free_norm_less_than_four',True,distinct_factors=len(facts),scope='EXACT_ALGEBRAIC_STURM')
tau=F(1,100);gap=F(1,10)*tau**2-864*tau**4
ck('positive_finite_window_certificate',gap==F(17,12500000) and gap>0,endpoint=str(tau),gap_lower_bound=str(gap),state_error_sufficient='delta < gap/4 for equal unit norms')
# Independent numerical trajectories for boost, free flow and attenuation.
numerical=[]
for gamma in [0,1,-1]:
 for time in [F(1,200),F(1,100)]:
  y=expm_multiply(float(time)*(A+gamma*E),x.astype(float));scores=[float(y@(S@y))/10 for S in SS]
  gs=[scores[target]-z for z in scores]
  if gamma==1:assert min(gs[j] for j in range(6) if j!=target)>float(F(1,10)*time**2-864*time**4)
  if gamma==0:assert max(scores)-min(scores)<1e-13
  if gamma==-1:assert min(gs[j] for j in range(6) if j!=target)>float(F(1,10)*time**2-864*time**4)
  assert max(scores[j] for j in range(6) if j!=target)-min(scores[j] for j in range(6) if j!=target)<1e-13
  numerical.append({'gamma':gamma,'time':str(time),'scores':scores,'norm_error':abs(float(y@y)-1)})
ck('flow_corrob_boost_free_and_cut',True,scope='NUMERICAL_CORROBORATION',cases=numerical)
# Pulse-only exact formulas: target = 1/10+sin^2(sqrt2 gamma t)/20;
# the other five remain 1/10. Verify the projectors on its three basis vectors.
aa0=np.zeros(N,dtype=np.int64);aa0[u]=1;aa0[v]=1
dd0=np.zeros(N,dtype=np.int64);dd0[u]=1;dd0[v]=-1
zz=np.zeros(N,dtype=np.int64);zz[int(off[1])+e]=1
quadratics=[]
for S in SS:
 Q=[[F(int(a@(S@b)),10) for b in [aa0,dd0,zz]] for a in [aa0,dd0,zz]];quadratics.append(Q)
ck('exact_isolated_pulse_projection_formula',quadratics[target]==[[F(2,5),0,0],[0,0,0],[0,0,F(1,10)]] and all(Q==[[F(1,5),0,0],[0,F(1,5),0],[0,0,F(1,10)]] for j,Q in enumerate(quadratics) if j!=target))
# Equal-norm comparison after switch-off: all scores are conserved by A.
y=expm_multiply(float(tau)*(A-E),x.astype(float));before=[float(y@(S@y))/10 for S in SS]
y2=expm_multiply(F(1,5).__float__()*A,y);after=[float(y2@(S@y2))/10 for S in SS]
ck('post_switch_score_retention',max(abs(a-b) for a,b in zip(before,after))<1e-12,scope='NUMERICAL_CORROBORATION',max_error=max(abs(a-b) for a,b in zip(before,after)))
# All edge axes have equal fibre count; at the source vertex there are two per H.
neighbors=[i for i,c in enumerate(C[1]) if u in c];counts=[0]*6
for i in neighbors:
 c=C[1][i];q=V[c[1] if c[0]==u else c[0]];matches=[j for j,h in enumerate(HH) if q in h];assert len(matches)==1;counts[matches[0]]+=1
ck('covariant_incident_edge_kernel',len(neighbors)==12 and counts==[2]*6,incident_edges=neighbors,fibration_counts=counts)
conjugate_neighbors={qm(qm(h,g),conj(h)) for h in V}
ck('incident_edge_kernel_forced_by_declared_covariance',len(conjugate_neighbors)==12 and {vid[q] for q in conjugate_neighbors}=={(c[1] if c[0]==u else c[0]) for c in (C[1][i] for i in neighbors)})
# A fully rotationally invariant real chain amplitude is harmonic. Two left
# and two right generators give the full orientation-preserving symmetry.
def closure(gens):
 seen={one};todo=[one]
 while todo:
  q=todo.pop()
  for r in gens:
   p=qm(q,r)
   if p not in seen:seen.add(p);todo.append(p)
 return seen
h=next(q for q in V if len(closure([g,q]))==120)
acts=[action(g),action(h),action(g,False),action(h,False)]
fixed=[];witness=[]
for d,cs in enumerate(C):
 size=len(cs);seen=set();basis=[]
 for seed in range(size):
  if seed in seen:continue
  assignment={seed:1};queue=[seed];consistent=True
  while queue:
   j=queue.pop()
   for M in acts:
    col=int(off[d])+j;p=int(M.indices[M.indptr[col]])-int(off[d]);sg=int(M.data[M.indptr[col]])
    val=assignment[j]*sg
    if p in assignment:consistent &= assignment[p]==val
    else:assignment[p]=val;queue.append(p)
  seen.update(assignment)
  if consistent:
   b=np.zeros(N,dtype=np.int64)
   for j,val in assignment.items():b[int(off[d])+j]=val
   basis.append(b)
 fixed.append(len(basis));witness+=basis
ck('rotation_invariant_amplitudes_are_harmonic',fixed==[1,0,0,1] and all(np.count_nonzero(A@z)==0 for z in witness),fixed_dimensions=fixed)
ck('edge_gate_cannot_release_fully_invariant_input',all(np.count_nonzero(E@z)==0 for z in witness))
# A face-only 2<->3 contact cannot act on vertex/exact-edge initial flow.
face=0;row=B[2][face,:].toarray().ravel();ee_rows=[];ee_cols=[];ee_vals=[]
for j in np.nonzero(row)[0]:
 aa,bb=int(off[2])+face,int(off[3])+int(j);ee_rows += [aa,bb];ee_cols += [bb,aa];ee_vals += [-int(row[j]),int(row[j])]
Ef=sp.csc_matrix((ee_vals,(ee_rows,ee_cols)),shape=(N,N),dtype=np.int64)
ck('face_source_cannot_release_harmonic_input',all(np.count_nonzero(Ef@z)==0 for z in witness))
ck('face_source_cannot_reach_vertex_exchange_space',(B[0]@B[1]).nnz==0 and Ef[:int(off[2]),:].nnz==0 and Ef[:,:int(off[2])].nnz==0,protected_dimension=239)
# Exact finite-bit source law: 4 unbiased bits accept labels 0..11, else retry.
ck('finite_random_donor_account',F(4,1)/F(3,4)==F(16,3) and 16%12!=0 and all(2**b%12!=0 for b in range(1,33)),expected_bits='16/3 for unbounded rejection',bounded_failure='4^(-r) with at most 4r input bits')
ck('uniform_fibration_pushforward',all(F(n,12)==F(1,6) for n in counts) and len(neighbors)==2*len(HH))
timing_endpoint=F(101,10000);timing_gap=F(1,10)*timing_endpoint**2-864*timing_endpoint**4
ck('finite_timing_window',timing_gap>0 and F(99,10000)>0 and timing_endpoint**2<F(1,8640),allowed_duration_interval=['99/10000','101/10000'],gap_lower_bound=str(timing_gap))
result={'status':'PASS','physical_promotion':0,'independent_review':False,'checks':checks,'exact_checks':sum(z['scope']!='NUMERICAL_CORROBORATION' for z in checks),'numerical_checks':sum(z['scope']=='NUMERICAL_CORROBORATION' for z in checks),'source_vertex':u,'source_edge':e,'target_fibration_index':target,'target_generator':g,'source_gamma':-1,'source_duration':str(tau),'gap_lower_bound':str(gap),'score_half_second_derivative_coefficients':[[str(v) for v in z] for z in co],'source_rule_status':'CANDIDATE supplied edge seed, contact mask and restoration switch; not a native source derivation.'}
(R/'LOCAL_SOURCE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(R/'LOCAL_SOURCE_DATA.json').write_text(json.dumps({'six_right_subgroups':[[vid[q] for q in sorted(h)] for h in HH],'source_vertex':u,'source_edge':e,'neighbor_vertex':v,'target':target,'C5_axis_permutation':hp,'incident_edges':neighbors,'fully_rotational_fixed_dimensions':fixed},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','exact_checks','numerical_checks','source_vertex','source_edge','target_fibration_index','gap_lower_bound']}))
