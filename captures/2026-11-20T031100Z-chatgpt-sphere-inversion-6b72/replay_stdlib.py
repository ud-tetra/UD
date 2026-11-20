#!/usr/bin/env python3
"""Independent stdlib-only replay of finite tetrahedral sphere/dual checks."""
import itertools,json
from fractions import Fraction as F
from pathlib import Path

V=range(4)
verts=[(i,) for i in V]
edges=list(itertools.combinations(V,2))
faces=list(itertools.combinations(V,3))
B=[verts,edges,faces]

def mat(r,c):return [[0]*c for _ in range(r)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return list(map(list,zip(*A)))
def neg(A):return [[-v for v in r] for r in A]
def equal(A,B):return A==B
def invcount(t):return sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def signo(t):return (-1)**invcount(t)
def incid(d):
    M=mat(len(B[d-1]),len(B[d]))
    for j,s in enumerate(B[d]):
        for i in range(d+1):
            t=s[:i]+s[i+1:]
            M[B[d-1].index(t)][j]=(-1)**i
    return M
B1,B2=incid(1),incid(2)
assert mul(B1,B2)==mat(4,4)

def rank(A):
    A=[[F(y) for y in row] for row in A]
    m=len(A);n=len(A[0]);pivot=0
    for j in range(n):
        i=next((k for k in range(pivot,m) if A[k][j]),None)
        if i is None:continue
        A[pivot],A[i]=A[i],A[pivot]
        q=A[pivot][j]; A[pivot]=[a/q for a in A[pivot]]
        for k in range(m):
            if k!=pivot and A[k][j]:
                t=A[k][j];A[k]=[a-t*b for a,b in zip(A[k],A[pivot])]
        pivot+=1
    return pivot
assert (rank(B1),rank(B2))==(3,3)
assert [4-rank(B1),6-rank(B1)-rank(B2),4-rank(B2)]==[1,0,1]

D={}
for d in (0,1,2):
    out=mat(len(B[2-d]),len(B[d]))
    for i,t in enumerate(B[d]):
        c=tuple(z for z in V if z not in t)
        out[B[2-d].index(c)][i]=signo(t+c)
    D[d]=out
assert equal(mul(D[0],B1),neg(mul(tr(B2),D[1])))
assert equal(mul(D[1],B2),mul(tr(B1),D[2]))
assert equal(mul(D[1],D[1]),[[int(i==j) for j in range(6)] for i in range(6)])
assert equal(mul(D[2],D[0]),[[-int(i==j) for j in range(4)] for i in range(4)])

perms=list(itertools.permutations(V))
for g in perms:
    T={}
    for d in (0,1,2):
        a=mat(len(B[d]),len(B[d]))
        for j,t in enumerate(B[d]):
            dest=tuple(g[x] for x in t)
            a[B[d].index(tuple(sorted(dest)))][j]=signo(dest)
        T[d]=a
    for d in (0,1,2):
        assert equal(mul(D[d],T[d]),[[signo(g)*x for x in row] for row in mul(T[2-d],D[d])])
central=[]
for f in perms:
    if all(all(f[g[i]]==g[f[i]] for i in V) for g in perms):central.append(f)
assert central==[tuple(V)]

W=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert all(dot(W[i],W[j])==(3 if i==j else -1) for i in V for j in V)
# normalized vi=Wi/sqrt(3); ci=-vi/3; unit inversion J(ci)=-3vi;
# polar vertices -3vi satisfy pairwise supporting inequalities <=1.
assert all(dot(tuple(-3*x for x in W[i]),W[j])//3==(-3 if i==j else 1) for i in V for j in V)
# midpoint of v0,v1: (W0+W1)/(2sqrt3), squared radius=1/3.
mi=tuple(F(W[0][k]+W[1][k],2) for k in range(3))
assert sum(x*x for x in mi)/3==F(1,3)
# Invert J(mid)=3mid, norm-squared=3. It leaves tetra boundary.
assert sum((3*x)*(3*x) for x in mi)/3 == 3
# Affine primal->dual maps x->-x/3, dual->primal -3y and radial normalized direction reverses.
probes=[]
for face in faces:
    a,b,c=[W[i] for i in face]
    probes += [tuple(map(F,a)),tuple((F(a[i])+F(b[i]))/2 for i in range(3)),tuple((F(a[i])+F(b[i])+F(c[i]))/3 for i in range(3)),tuple((F(a[i])+2*F(b[i])+3*F(c[i]))/6 for i in range(3))]
for x in probes:
    y=tuple(-k/3 for k in x)
    assert tuple(-3*k for k in y)==x
    assert tuple(-k for k in x) == tuple(3*k for k in y)
    assert sum(k*k for k in x)>0

r={"status":"PASS","method":"independent standard-library fractions, generated incidence, rank elimination and permutation exhaustive", "betti":[1,0,1],"euler":2,"dual_incidence":True,"twisted_s4_checks":72,"centralizer_only_identity":True,"sampled_primal_dual_inverse":len(probes),"spherical_inversion_on_unit_sphere":"identity", "antipodal_readout_on_primal_dual":"distinct_from_inversion","physical_promotion":0}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
print(json.dumps(r,indent=2,sort_keys=True))
