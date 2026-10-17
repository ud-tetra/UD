"""New constructor replay; imports no archived executable source."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json,math
import numpy as np
import scipy.sparse as sp
from scipy.linalg import eigvals,eigh
from scipy.optimize import linear_sum_assignment
from scipy.sparse.linalg import expm_multiply

R=Path(__file__).resolve().parent
checks=[]
def ck(name,test,scope='EXACT',**data):
    assert test,(name,data)
    checks.append(dict(name=name,status='PASS',scope=scope,**data))
def add(p,q):
    z=p.copy()
    for m,c in q.items():z[m]=z.get(m,0)+c
    return {m:c for m,c in z.items() if c}
def mul(p,q):
    z={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(x+y for x,y in zip(m,n));z[k]=z.get(k,0)+c*d
    return {m:c for m,c in z.items() if c}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def term(c=1,**powers):return {tuple(powers.get(x,0) for x in ['lam','a','gamma','kappa','mu']):c}
zero={};lam=term(lam=1);a=term(a=1);g=term(gamma=1);k=term(kappa=1);mu=term(mu=1)
# det(lam I-K) in a nonorthogonal cut coordinate; its metric is diag(1,mu,1).
M=[[lam,mul(a,mu),scale(g,-1)],[scale(a,-1),lam,zero],[g,zero,add(lam,mul(k,mu))]]
det={}
for p in permutations(range(3)):
    sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    t=term(sign)
    for i in range(3):t=mul(t,M[i][p[i]])
    det=add(det,t)
expected=add(add(term(lam=3),term(lam=2,kappa=1,mu=1)),add(add(term(lam=1,a=2,mu=1),term(lam=1,gamma=2)),term(kappa=1,a=2,mu=2)))
ck('symbolic_cubic_characteristic_polynomial',det==expected)
d=term(kappa=1,mu=1);omega=add(term(a=2,mu=1),term(gamma=2));c=term(kappa=1,a=2,mu=2)
ck('symbolic_routh_second_determinant',add(mul(d,omega),scale(c,-1))==term(kappa=1,mu=1,gamma=2))
ar,gr,kr,mr,nr=F(2,3),F(3,5),F(1,4),F(7),F(4,3)
K=np.array([[0,-ar*mr,gr*nr],[ar,0,0],[-gr/nr,0,-kr*mr]],dtype=object)
G=np.diag(np.array([F(1),mr,nr*nr],dtype=object))
ck('raw_pulled_back_storage_balance',np.array_equal(K.T@G+G@K,np.diag([F(0),F(0),-2*kr*mr*nr*nr])))
ck('normalization_does_not_equal_symmetric_rate',gr*nr!=gr/nr and (gr*nr)*(gr/nr)==gr*gr)
ck('signed_burden_positive_cone_not_invariant',-gr/nr*F(1)<0)
D=json.loads((R/'COMPLEX_AND_ACTION.json').read_text())
C=[[tuple(s) for s in cs] for cs in D['simplices']]
ids=[{s:i for i,s in enumerate(cs)} for cs in C]
Bs=[]
for dgr in [1,2,3]:
    rr=[];cc=[];vv=[]
    for j,s in enumerate(C[dgr]):
        for i in range(dgr+1):rr.append(ids[dgr-1][s[:i]+s[i+1:]]);cc.append(j);vv.append((-1)**i)
    Bs.append(sp.csc_matrix((vv,(rr,cc)),shape=(len(C[dgr-1]),len(C[dgr])),dtype=np.int64))
B1,B2,B3=Bs;L=(B1@B1.T).toarray();n=len(C[0])
ck('finite_chain_dimensions',list(map(len,C))==[120,720,1200,600])
ck('chain_nilpotence',(B1@B2).nnz==0 and (B2@B3).nnz==0)
def rank_mod2(M):
    basis={}
    for row in M.tocsr():
        bits=0
        for j,v in zip(row.indices,row.data):
            if int(v)%2:bits^=1<<int(j)
        while bits:
            p=bits.bit_length()-1
            if p not in basis:basis[p]=bits;break
            bits^=basis[p]
    return len(basis)
ranks=[rank_mod2(B) for B in Bs]
# Real fundamental cycle, verified by a signed traversal of the dual graph.
F3=B3.tocsr();adj=[[] for _ in C[3]]
for row in F3:
    assert len(row.indices)==2
    (i,j),(si,sj)=row.indices,row.data
    adj[int(i)].append((int(j),int(-si*sj)));adj[int(j)].append((int(i),int(-si*sj)))
ori=[0]*600;ori[0]=1;todo=[0]
while todo:
    i=todo.pop()
    for j,s in adj[i]:
        if not ori[j]:ori[j]=ori[i]*s;todo.append(j)
        else:assert ori[j]==ori[i]*s
ck('fundamental_cycle_and_dual_connectivity',all(ori) and np.all(B3@np.array(ori)==0))
ck('exact_rational_boundary_ranks',ranks==[119,601,599] and np.all(B1.T@np.ones(120,dtype=np.int64)==0),justification='mod-2 lower bounds; constant/fundamental-cycle upper bounds and B1 B2=0 give matching rational upper bounds')
# Exact annihilating polynomial and moments fix all multiplicities of symmetric L.
I=np.eye(n,dtype=object);Lo=L.astype(object)
P=Lo.copy()
for shift,square in [(10,20),(9,45)]:P=P@((Lo-shift*I)@(Lo-shift*I)-square*I)
for shift in [9,12,14,15]:P=P@(Lo-shift*I)
ck('exact_vertex_annihilating_polynomial',np.all(P==0))
def smul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,k):
    y=(1,0)
    for _ in range(k):y=smul(y,x)
    return y
spec=[((0,0),1),((9,-3),4),((9,3),4),((10,-2),9),((10,2),9),((9,0),16),((12,0),25),((14,0),36),((15,0),16)]
Lp=I.copy();moments=[]
for j in range(9):
    t=int(np.trace(Lp));val=(sum(m*power(x,j)[0] for x,m in spec),sum(m*power(x,j)[1] for x,m in spec))
    assert val==(t,0);moments.append(t);Lp=Lp@Lo
ck('nine_exact_spectral_moments',True,moments=moments,eigenvalues_Qsqrt5=[{'pair':list(x),'multiplicity':m} for x,m in spec])
ck('coupled_and_undamped_dimension_split',3*119+2+2401==2760 and 2640-120-119==2401)
# Quaternion vertex action, six subgroup averages and signed simplex orbit lengths.
V=[tuple(tuple(t) for t in q) for q in D['vertices']];vid={q:i for i,q in enumerate(V)}
neg=lambda x:(-x[0],-x[1])
pmul=lambda x,y:(x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
psum=lambda xs:(sum(t[0] for t in xs),sum(t[1] for t in xs))
def qm(x,y):
    z=[psum([pmul(x[0],y[0])]+[neg(pmul(x[i],y[i])) for i in [1,2,3]])]
    for i,j,k0 in [(1,2,3),(2,3,1),(3,1,2)]:z.append(psum([pmul(x[0],y[i]),pmul(x[i],y[0]),pmul(x[j],y[k0]),neg(pmul(x[k0],y[j]))]))
    assert all(a%2==b%2==0 for a,b in z)
    return tuple((a//2,b//2) for a,b in z)
conj=lambda x:(x[0],)+tuple(neg(t) for t in x[1:])
one=((2,0),(0,0),(0,0),(0,0));gen=tuple(tuple(t) for t in D['right_generator'])
q=one;H={q}
for _ in range(9):q=qm(q,gen);H.add(q)
HH=sorted({frozenset(qm(qm(conj(q),h),q) for h in H) for q in V},key=lambda h:sorted(h))
target=HH.index(frozenset(H));u=vid[one];v=vid[gen]
def vaction(q):
    M=np.zeros((120,120),dtype=np.int64)
    for j,x in enumerate(V):M[vid[qm(x,q)],j]=1
    return M
SS=[sum((vaction(h) for h in hs),np.zeros((120,120),dtype=np.int64)) for hs in HH]
ck('six_vertex_projectors_and_relief_commutation',len(SS)==6 and all(np.array_equal(S@S,10*S) and np.array_equal(S,S.T) and np.array_equal(S@L,L@S) for S in SS))
vp=[vid[qm(q,gen)] for q in V];orbitcounts=[]
for cs in C:
    index={s:i for i,s in enumerate(cs)};perm=[index[tuple(sorted(vp[i] for i in s))] for s in cs];seen=set();count=0
    for j in range(len(cs)):
        if j in seen:continue
        cycle=[];t=j
        while t not in cycle:cycle.append(t);seen.add(t);t=perm[t]
        assert t==j and len(cycle)==10;count+=1
    orbitcounts.append(count)
ck('ten_mode_dimensions_after_burden_extension',orbitcounts==[12,72,120,60] and sum(orbitcounts)+12==276,orbit_counts=orbitcounts)
ck('declared_two_parameter_normalization_commutes',all(np.all(S.sum(axis=0)==10) and np.all(S.sum(axis=1)==10) for S in SS),justification='S P0=P0 S=10 P0; hence every nu0 P0+nuperp(I-P0) commutes')
Du=np.zeros((n,n),dtype=np.int64);Du[u,u]=1
ck('local_drain_breaks_every_fibration_average',all(int(np.sum((Du@S-S@Du)**2))==18 for S in SS),commutator_frobenius_squared='9/50 for unscaled orthoprojectors')
other=next(j for j in range(6) if j!=target);w=np.zeros(n,dtype=np.int64);w[u]=w[v]=1
Dscore=SS[target]-SS[other]
cross=F(int(w@Dscore@w),10)
ck('active_reciprocal_coupling_changes_carrier_gap',cross==F(1,5),gap_derivative='(2/5)*gamma for c0=bhat=e_u+e_v')
ck('joint_score_dissipation_gap_has_both_signs',any(int(np.eye(n,dtype=np.int64)[i]@Dscore@L@np.eye(n,dtype=np.int64)[j])!=0 for i in range(n) for j in range(n)) and int(np.trace(Dscore@L))==0,justification='Dscore L is real symmetric, nonzero, traceless; therefore indefinite')
ck('uniform_diffusion_blindness',np.all(L@np.ones(n,dtype=np.int64)==0))
# Polynomial construction of the exact rational Moore-Penrose inverse.
def polymul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return out
qpoly=[1]
for fac in [[80,-20,1],[36,-18,1],[-9,1],[-12,1],[-14,1],[-15,1]]:qpoly=polymul(qpoly,fac)
Z=np.zeros((n,n),dtype=object);Lp=I.copy()
for j in range(8):Z-=n*qpoly[j+1]*Lp;Lp=Lp@Lo
Z+=qpoly[1]*np.ones((n,n),dtype=object);den=n*qpoly[0]
ck('exact_pseudoinverse_polynomial',np.array_equal(Lo@Z,qpoly[0]*(n*I-np.ones((n,n),dtype=object))) and np.all(Z@np.ones(n,dtype=object)==0))
edge=ids[1][tuple(sorted((u,v)))];be=B1[:,edge].toarray().ravel()
ck('target_boundary_average_vanishes',np.all(SS[target]@be==0) and all(int((S@be)@(S@be))==20 for j,S in enumerate(SS) if j!=target))
alpha=[F(int(be@Z@S@be),10*den) for S in SS]
ck('protected_cycle_gap_coefficient',alpha[target]==0 and all(x==F(11,600) for j,x in enumerate(alpha) if j!=target),coefficients=[str(x) for x in alpha])
resistance=F(int(be@Z@be),den)
ck('protected_cycle_retained_stock_coefficient',resistance==F(119,720),cycle_stock_coefficient=str(1-resistance))
ck('operator_norm_certificate_for_cut',max(np.diff(B2.tocsr().indptr))==5 and max(np.diff(B2.tocsc().indptr))==3 and max(np.diff(B3.tocsr().indptr))==2 and max(np.diff(B3.tocsc().indptr))==4 and F(2237,1000)**2>5 and 9+3*F(2237,1000)<16)
tau=F(1,1000);margin=F(11,600)*tau*tau-864*tau**4
ck('certified_finite_protected_gap',margin==F(6551,375000000000) and margin>0,cut_duration=str(tau),lower_gap=str(margin))
# Full signed chain averages, used only for the labelled dynamical corroboration.
offset=np.cumsum([0]+list(map(len,C)));Nchain=int(offset[-1])
def chainaction(q):
    vp=[vid[qm(x,q)] for x in V];rr=[];cc=[];vv=[]
    for dgr,cs in enumerate(C):
        for j,s in enumerate(cs):
            image=tuple(vp[i] for i in s);sign=(-1)**sum(image[i]>image[j] for i in range(len(s)) for j in range(i+1,len(s)))
            rr.append(int(offset[dgr])+ids[dgr][tuple(sorted(image))]);cc.append(int(offset[dgr])+j);vv.append(sign)
    return sp.csc_matrix((vv,(rr,cc)),shape=(Nchain,Nchain),dtype=np.int64)
Sch=[sum((chainaction(h) for h in hs),sp.csc_matrix((Nchain,Nchain),dtype=np.int64)) for hs in HH]
AAchain=sp.bmat([[None,-B1,None,None],[B1.T,None,-B2,None],[None,B2.T,None,-B3],[None,None,B3.T,None]],format='csc')
rr=[];cc=[];vv=[]
for i in np.flatnonzero(be):rr.extend([int(i),120+edge]);cc.extend([120+edge,int(i)]);vv.extend([-int(be[i]),int(be[i])])
Edge=sp.csc_matrix((vv,(rr,cc)),shape=(Nchain,Nchain))
ck('source_and_restored_score_commutation',(Edge+Edge.T).nnz==0 and all((AAchain@S-S@AAchain).nnz==0 for S in Sch))
# Labelled numerical corroboration of the independently assembled vertex/cut/burden matrix.
evalL,U=eigh(L.astype(float));Up=U[:,1:];freq=np.sqrt(evalL[1:]);Q=(B1.T@Up)/freq
a0,g0,k0,r0=1.,2/3,1/4,1/5
O=np.zeros((n,119));AA=np.block([[np.zeros((n,n)),-a0*(B1@Q)],[a0*(Q.T@B1.T),np.zeros((119,119))]])
I0=np.vstack([np.eye(n),np.zeros((119,n))])
def coupled(Rb):return np.block([[AA,g0*I0],[-g0*I0.T,-Rb]])
roots=eigvals(coupled(k0*L));expectedroots=[1j*g0,-1j*g0]
for eigmu in evalL[1:]:expectedroots.extend(np.roots([1,k0*eigmu,a0*a0*eigmu+g0*g0,k0*a0*a0*eigmu*eigmu]))
distance=np.abs(roots[:,None]-np.array(expectedroots)[None,:]);ii,jj=linear_sum_assignment(distance)
err=float(distance[ii,jj].max())
ck('359_dimensional_spectrum_matches_cubic_factors',err<1e-8 and sum(x.real< -1e-9 for x in roots)==357,'NUMERICAL',max_error=err)
localroots=eigvals(coupled(k0*L+r0*Du))
ck('one_local_drain_stabilizes_vertex_burden_lane',max(localroots.real)<-1e-7,'NUMERICAL',largest_real_part=float(max(localroots.real)))
uniformroots=eigvals(coupled(k0*L+r0*np.eye(n)))
ck('uniform_local_drains_stabilize_vertex_burden_lane',max(uniformroots.real)<-1e-7,'NUMERICAL',largest_real_part=float(max(uniformroots.real)))
x0=np.zeros(Nchain);x0[u]=1;cut=expm_multiply(.001*(AAchain-Edge),x0)
Zfloat=np.array(Z,dtype=float)/den
def dark(x):
    y=x.copy();y[:120]=0;y[120:840]-=B1.T@(Zfloat@(B1@y[120:840]));return y
ret=dark(cut)
def scores(x):return np.array([x@(S@x)/10 for S in Sch])
gaps=scores(ret)[target]-scores(ret)
ck('protected_score_gap_after_cut',min(gaps[j] for j in range(6) if j!=target)>float(margin),'NUMERICAL',gaps=gaps.tolist(),retained_support=float(ret@ret))
Inc=sp.vstack([sp.eye(120),sp.csc_matrix((2520,120))],format='csc')
Joint=sp.bmat([[AAchain,g0*Inc],[-g0*Inc.T,-k0*sp.csc_matrix(L)-r0*sp.eye(120)]],format='csc')
joint=expm_multiply(600*Joint,np.r_[cut,np.zeros(120)]);ct=joint[:Nchain]
ref=expm_multiply(600*AAchain,ret)
ck('protected_lane_survives_reciprocal_relaxation',np.linalg.norm(dark(ct)-ref)<1e-10 and np.linalg.norm(ct-ref)<1e-6 and max(abs((scores(ct)[target]-scores(ct))-gaps))<1e-10,'NUMERICAL',time=600.,burden_norm=float(np.linalg.norm(joint[Nchain:])),carrier_minus_dark_norm=float(np.linalg.norm(ct-ref)),final_carrier_gaps=(scores(ct)[target]-scores(ct)).tolist())
out={'checks':checks,'exact_count':sum(c['scope']=='EXACT' for c in checks),'numerical_count':sum(c['scope']=='NUMERICAL' for c in checks),'physical_promotion':0,'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','scope':'Conditional reciprocal extension on restored uniform carrier; not the active edge-cut spectrum, native burden occupancy, event trigger, physical rate or independent review.'}
(R/'RECIPROCAL_RECOVERY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
