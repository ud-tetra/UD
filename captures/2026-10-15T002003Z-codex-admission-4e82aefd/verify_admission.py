#!/usr/bin/env python3
"""Independent exact carrier and candidate-controller certificates, no imported code."""
import itertools as it,json,pathlib,sys
import sympy as s
R=pathlib.Path(__file__).resolve().parent;checks={}
def check(name,condition,**data):
 assert condition,(name,data)
 checks[name]={'passed':True,**data}
cells=[list(it.combinations(range(4),k)) for k in range(1,5)]
offset=[0,4,10,14];boundaries=[]
for k in range(1,4):
 B=s.zeros(len(cells[k-1]),len(cells[k]))
 for j,tet in enumerate(cells[k]):
  for i in range(k+1):B[cells[k-1].index(tet[:i]+tet[i+1:]),j]=(-1)**i
 boundaries.append(B)
a,b,c,t=s.symbols('a b c t',real=True);A=s.zeros(15)
for k,(weight,B) in enumerate(zip([a,b,c],boundaries)):
 i,j=offset[k],offset[k+1]
 A[i:i+B.rows,j:j+B.cols]=-weight*B
 A[j:j+B.cols,i:i+B.rows]=weight*B.T
U=A.subs({a:1,b:1,c:1})
check('skew_and_chain',A.T==-A and all(boundaries[k]*boundaries[k+1]==s.zeros(boundaries[k].rows,boundaries[k+1].cols) for k in [0,1]))
pairs=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]];Ds=[]
for p in pairs:
 D=s.zeros(15)
 for edge in p:D[4+cells[1].index(edge),4+cells[1].index(edge)]=1
 Ds.append(D)
check('pair_projectors',all(D*D==D and D.T==D and s.trace(D)==2 for D in Ds))
for i,D in enumerate(Ds):
 idx=[j for j in range(15) if D[j,j]];rest=[j for j in range(15) if not D[j,j]]
 B=A.extract(idx,rest);C=D*A-A*D
 check('pair_'+str(i)+'_symbolic_coupling',B*B.T==2*(a*a+b*b)*s.eye(2) and C.T==C,
       beta_squared='2*(a**2+b**2)',third_channel_direct_dependence=False)
 check('pair_'+str(i)+'_stock_derivative',C==D*A+A.T*D and
       C*C==D*A*(s.eye(15)-D)*A.T*D+(s.eye(15)-D)*A.T*D*A*(s.eye(15)-D))
check('zero_direct_channel',all((D*A-A*D).subs({a:0,b:0})==s.zeros(15) for D in Ds))
# Signed S4 actions and induced pair permutations.
def sign_sort(x):return (-1)**sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))
actions=[];pair_perms=[]
for g in it.permutations(range(4)):
 T=s.zeros(15)
 for k,block in enumerate(cells):
  for j,face in enumerate(block):
   mapped=tuple(g[v] for v in face)
   T[offset[k]+block.index(tuple(sorted(mapped))),offset[k]+j]=sign_sort(mapped)
 pg=[]
 for i,p in enumerate(pairs):
  q={tuple(sorted(g[v] for v in edge)) for edge in p}
  j=next(j for j,qj in enumerate(pairs) if q==set(qj));pg.append(j)
  assert T*Ds[i]*T.T==Ds[j]
 assert T*A==A*T
 actions.append(T);pair_perms.append(pg)
check('signed_symmetry_and_stock_covariance',True,group_actions=24,projector_identities=72)
h=s.zeros(15,1);h[:4,0]=s.ones(4,1)/4
e0=s.eye(15)[:,0]
x=h+s.cos(2*t)*(e0-h)+s.sin(2*t)*U*e0/2
check('exact_vertex_trajectory',s.simplify(x.diff(t)-U*x)==s.zeros(15,1) and x.subs(t,0)==e0)
stocks=[s.trigsimp((x.T*D*x)[0]) for D in Ds]
check('symmetric_stock_trajectory',all(s.trigsimp(q-s.sin(2*t)**2/4)==0 for q in stocks),
      pair_stock='sin(2*t)**2/4')
lo,hi=s.Rational(1,16),s.Rational(3,16);on=s.pi/6;off=5*s.pi/12
check('transverse_simultaneous_switches',all(s.simplify(q.subs(t,on)-hi)==0 and
 s.simplify(q.subs(t,off)-lo)==0 and s.simplify(s.diff(q,t).subs(t,on))==s.sqrt(3)/4 and
 s.simplify(s.diff(q,t).subs(t,off))==-s.sqrt(3)/4 for q in stocks),
 first_on='pi/6',first_off='5*pi/12',all_three_addresses=True)
stabilizer=[pg for g,pg in zip(it.permutations(range(4)),pair_perms) if g[0]==0]
check('no_equivariant_single_address_at_symmetric_state',len(stabilizer)==6 and
 all(any(pg[i]!=i for pg in stabilizer) for i in range(3)),stabilizer_order=6,fixed_addresses=[])
edge=s.eye(15)[:,4];y0=U*edge/2
y=s.cos(2*t)*y0-s.sin(2*t)*edge
check('canonical_angular_bound_attainment',U*U*edge==-4*edge and (y0.T*y0)[0]==1 and
 s.simplify((y.T*Ds[0]*y)[0]-s.sin(2*t)**2)==0 and s.simplify(y.diff(t)-U*y)==s.zeros(15,1),
 attainable_crossing_time='(asin(sqrt(hi))-asin(sqrt(lo)))/2')
edge2=s.eye(15)[:,9]
constant=(s.cos(2*t)*edge+s.sin(2*t)*U*edge/2+s.sin(2*t)*edge2-s.cos(2*t)*U*edge2/2)/s.sqrt(2)
check('half_gap_noise_threshold_sharpness',s.simplify(constant.diff(t)-U*constant)==s.zeros(15,1)
 and s.simplify((constant.T*constant)[0])==1
 and s.trigsimp((constant.T*Ds[0]*constant)[0])==s.Rational(1,2),
 true_stock='1/2',thresholds=['3/8','5/8'],noise='sin(M*s)/8',
 effect='arbitrarily many toggles as M grows; no amplitude-only uniform count bound at epsilon=gap/2')
eta=s.symbols('eta',real=True)
vertex=s.eye(15)[:,0]+eta*s.eye(15)[:,1]
edge_amp=U*vertex/2
amplitudes=[s.factor((edge_amp.T*D*edge_amp)[0]/(1+eta**2)) for D in Ds]
check('no_uniform_global_interevent_gap',all(s.simplify(x-y)==0 for x,y in zip(amplitudes,[(eta-1)**2/(4*(eta**2+1)),s.Rational(1,4),s.Rational(1,4)])),
      argument='A crossing approaches the simultaneous B/C crossing as eta tends to zero from above',
      scope='per-address dwell does not give a positive uniform global event separation')
epsilon=s.Rational(1,64);nu=s.sqrt(39)/16
tminus=s.asin(2*s.sqrt(hi-epsilon))/2;tplus=s.asin(2*s.sqrt(hi+epsilon))/2
timing=max(float(s.N(on-tminus,60)),float(s.N(tplus-on,60)))
check('transverse_timing_numerical_corollary',timing<float(s.N(epsilon/nu,60)),
      status='NUMERICAL_CORROBORATION_OF_WRITTEN_CALCULUS_PROOF',
      largest_constant_bias_shift=timing,proved_bound=str(epsilon/nu))
# Noisy threshold dwell lower bounds; exact positivity is sufficient for all bounded noise paths.
check('bounded_noise_gap',hi-lo-2*epsilon==s.Rational(3,32),
      epsilon='1/64',effective_gap='3/32',linear_dwell='3/64')
check('serialization_count',len(list(it.permutations(range(3))))==6 and 2**2<6<=2**3,
      orders=6,worst_case_order_receipt_bits=3)
out={'passed':True,'check_families':len(checks),'checks':checks,
 'scope':'Exact finite carrier and declared passive hysteresis controller; written proofs supply general dwell/noise bounds.',
 'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','physical_promotion':0,
 'environment':{'python':sys.version,'sympy':s.__version__}}
(R/'ADMISSION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':True,'check_families':len(checks),'output':'ADMISSION_CHECKS.json'}))
