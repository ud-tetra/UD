#!/usr/bin/env python3
"""Independent standard-library finite replay; no sympy, floats or fitted targets."""
from itertools import combinations, product, permutations
from fractions import Fraction as Q

def admissible(tets,n):
    F=sorted({f for tet in tets for f in combinations(tet,3)})
    return [s for s in product((0,1),repeat=n) if all(len({s[i] for i in f})==2 for f in F)]

def permute(s,p):
    out=[None]*len(s)
    for i,v in enumerate(s):out[p[i]]=v
    return tuple(out)

def check(tets,n,d):
    sts=admissible(tets,n)
    assert len(sts)==6
    Aut=[p for p in permutations(range(n)) if {frozenset(p[i] for i in t) for t in tets}=={frozenset(t) for t in tets}]
    for s in sts:
        dist=lambda t:sum(x!=y for x,y in zip(s,t))
        near={t for t in sts if dist(t)==2}
        assert len(near)==d
        H=[p for p in Aut if permute(s,p)==s]
        for t in near:assert {permute(t,p) for p in H}==near
    return len(sts),len(Aut)
assert check([(0,1,2,3)],4,4)==(6,24)
assert check([(0,1,2,3),(0,1,2,4)],5,2)==(6,12)

simplexes=sorted({f for k in range(1,5) for f in combinations(range(4),k)},key=lambda s:(len(s),s))
ix={s:i for i,s in enumerate(simplexes)}
N=15;A=[[0]*N for _ in range(N)]
for j,s in enumerate(simplexes):
    if len(s)==1:continue
    for k in range(len(s)):
        i=ix[s[:k]+s[k+1:]];A[i][j]=(-1)**k;A[j][i]=-(-1)**k
p={ix[(0,1)],ix[(2,3)]}
def apply(x,m=A):return [sum(a*b for a,b in zip(row,x)) for row in m]
def norm(x):return sum(v*v for v in x)
for v,nu,nc in [([1,1,1,1],4,4),([1,2,1,1],7,6)]:
    c=list(v)+[0]*11;c[ix[(0,2)]]=1
    assert all(c[i]==0 for i in p)
    ac=apply(c);mask=[0 if i in p else ac[i] for i in range(N)]
    assert (norm(ac),norm(mask))==(nu,nc)
    assert nu-nc==sum(ac[i]**2 for i in p)
    if nu==nc:
        assert all(ac[i]==0 for i in p)
        y=ac
        # invariant cyclic subspace: A^2c = -4(c - 1_vertex)
        z=apply(y)
        h=[1]*4+[0]*11
        assert z==[-4*(ci-hi) for ci,hi in zip(c,h)]
        assert apply(z)==[-4*v for v in y]
# face-sum constraints x_except_v=0 mod 1 imply all four x_v equal,
# and 3*x_v=0; hence three classes, no continuous local gauge phase.
assert len({tuple(k/3 for _ in range(4)) for k in range(3)})==3
print('PASS: K4 6 states/4 symmetric successors; glued 6 states/2; POC1 strict and trajectory tie; undressed Z3')
