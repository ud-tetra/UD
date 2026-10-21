#!/usr/bin/env python3
"""THM534 S23-S28: exact 64-mask S4, dissipation and source-routing audit.
Requires Python 3, SymPy, NumPy. No native packet gate rule is claimed.
"""
import itertools
import numpy as np
import sympy as S
V=range(4); E=list(itertools.combinations(V,2)); F=list(itertools.combinations(V,3))
B1=S.zeros(4,6); B2=S.zeros(6,4); B3=S.zeros(4,1)
for e,(u,v) in enumerate(E): B1[u,e]=-1; B1[v,e]=1
for f,face in enumerate(F):
    for k in range(3): B2[E.index(face[:k]+face[k+1:]),f]=(-1)**k
for k in range(4): B3[F.index(tuple(x for x in V if x!=k)),0]=(-1)**k
I=S.eye(4); ones=S.ones(4,1)
assert B1*B2==S.zeros(4,4) and B2*B3==S.zeros(6,1)
assert B1.T*B1+B2*B2.T==4*S.eye(6)

# Binary local-vs-cell closure are *countermodel candidate selectors*, not canon.
def selectors(chi,beta,tau):
    T=[beta[u]*beta[v]*tau[i] for i,(u,v) in enumerate(E)]
    return (tuple(chi[u]*chi[v]*T[i] for i,(u,v) in enumerate(E)),
            tuple(S.prod(chi)*T[i] for i in range(6)))
chi=(1,1,1,0); beta=(1,1,1,1);tau=(1,)*6
l,c=selectors(chi,beta,tau)
assert l==(1,1,0,1,0,0) and c==(0,)*6
rho=S.Matrix([1,0,0,0])
def step(x,h):
    H=S.diag(*h); j=-H*B1.T*x/4
    return x+B1*j,j,B2.T*j
p,j,F0=step(rho,l)
pc,jc,Fc=step(rho,c)
assert list(p)==[S.Rational(1,2),S.Rational(1,4),S.Rational(1,4),0]
assert list(F0)==[0,S.Rational(1,4),S.Rational(1,4),0]
assert pc==rho and Fc==S.zeros(4,1)

# Both selectors are equivariant under every 24-vertex relabeling.
for perm in itertools.permutations(V):
    chi2=[0]*4; beta2=[0]*4; tau2=[0]*6
    for u in V: chi2[perm[u]]=chi[u];beta2[perm[u]]=beta[u]
    for i,(u,v) in enumerate(E):
        tau2[E.index(tuple(sorted((perm[u],perm[v]))))]=tau[i]
    L,C=selectors(chi2,beta2,tau2)
    for i,(u,v) in enumerate(E):
        jidx=E.index(tuple(sorted((perm[u],perm[v]))))
        assert (L[jidx],C[jidx])==(l[i],c[i])
    assert {tuple(sorted((perm[u],perm[v]))) for u,v in E}==set(E)
assert selectors((1,)*4,(1,)*4,(1,)*6)==((1,)*6,(1,)*6)

# Exact matrix proof control: S25 circulation-budget difference PSD on ALL 64 masks.
ranks={}
for bits in itertools.product((0,1),repeat=6):
    H=S.diag(*bits); P=I-B1*H*B1.T/4
    Q=-B2.T*H*B1.T/4
    W=I-P.T*P-Q.T*Q
    eig=W.eigenvals()
    assert all(lam.is_nonnegative is True for lam in eig)
    ranks[W.rank()]=ranks.get(W.rank(),0)+1
assert ranks=={0:1,1:6,2:19,3:38}

# S28 exact decay with permanent nonuniform gate; no long-lived curvature.
P=I-B1*S.diag(*l)*B1.T/4
assert P.eigenvals()=={S.Integer(1):2,S.Rational(1,4):2}
for n in range(8):
    x=P**n*rho
    _,_,fn=step(x,l)
    assert fn==F0/(4**n)

# S26 funded repetition witness, and S27 source-routing nonuniqueness.
s=rho-p
assert list(s)==[S.Rational(1,2),-S.Rational(1,4),-S.Rational(1,4),0]
assert sum(s)==0 and p+s==rho
mean=ones/4
D0=((rho-mean).T*(rho-mean))[0]
Dp=((p-mean).T*(p-mean))[0]
W=2*((p-mean).T*s)[0]+(s.T*s)[0]
assert (D0,Dp,W)==(S.Rational(3,4),S.Rational(1,8),S.Rational(5,8))
assert (F0.T*F0)[0]==S.Rational(1,8)
k=-j;other=k+B2[:,0]
assert B1*k==s and B1*other==s
assert B2.T*(j+k)==S.zeros(4,1)
assert B2.T*(j+other)!=S.zeros(4,1)

# Numeric stress: arbitrarily varying masks or held nonuniform candidate mask.
b=np.array(B1,dtype=float); f=np.array(B2,dtype=float)
rng=np.random.default_rng(534080)
max_drift=max_budget=max_tail=0.0; nonflat=0
for run in range(16):
    x=rng.random(4);x/=x.sum(); m=x.sum()
    initial=np.linalg.norm(x-x.mean())**2; accum=0.
    for n in range(256):
        mask=rng.integers(0,2,6) if run<8 else np.array(l,dtype=int)
        current=-(mask*(b.T@x))/4
        curl=f.T@current; xn=x+b@current
        assert xn.min()>=-1e-13
        accum+=float(curl@curl)
        max_drift=max(max_drift,abs(xn.sum()-m))
        if np.linalg.norm(curl)>1e-12: nonflat+=1
        if n>=192:max_tail=max(max_tail,float(np.linalg.norm(curl)))
        x=xn
    final=np.linalg.norm(x-x.mean())**2
    max_budget=max(max_budget,max(0,accum-(initial-final)))
    assert accum<=initial-final+1e-11
assert max_drift<2e-13 and max_budget<1e-12
print('PASS S23-S28 exact 24 S4 rebasings, 64 masks, fixed mask geometric decay')
print('PASS exact variance-funded loop and source-routing counterexample')
print('PASS numerical',16*256,'steps,',nonflat,'nonzero-curl; drift',max_drift)
print('max curvature budget violation',max_budget,'tail',max_tail)
print('Original THM-534 source and packet gate dynamics OPEN; physical promotion 0')
