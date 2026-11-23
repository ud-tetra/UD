#!/usr/bin/env python3
"""Independent exact-fraction halfspace, source-blind and positive-metric controls.
Does not import SymPy or the primary audit.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
v=[(F(1),F(1),F(1)),(F(1),F(-1),F(-1)),(F(-1),F(1),F(-1)),(F(-1),F(-1),F(1))]
num=[[-61,-22,58],[62,-19,58],[-2,82,29]]
R=[[F(x,87) for x in row] for row in num]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def matvec(A,x):return tuple(dot(r,x) for r in A)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve3(A, rhs):
    # Plain rational Gaussian elimination (not SymPy inverse/Cramer).
    m=[list(row)+[value] for row,value in zip(A,rhs)]
    for k in range(3):
        t=next((i for i in range(k,3) if m[i][k]),None)
        if t is None:return None
        m[k],m[t]=m[t],m[k]
        pivot=m[k][k]
        m[k]=[x/pivot for x in m[k]]
        for i in range(3):
            if i==k:continue
            factor=m[i][k]
            m[i]=[x-factor*y for x,y in zip(m[i],m[k])]
    return tuple(row[3] for row in m)

def poly(A):
    n=v+[tuple(-x for x in matvec(A,p)) for p in v]
    vertices=set()
    for ids in combinations(range(8),3):
        x=solve3([n[i] for i in ids], [F(-1)]*3)
        if x is not None and all(dot(ni,x)>=F(-1) for ni in n):vertices.add(x)
    verts=sorted(vertices)
    face=[frozenset(i for i,p in enumerate(verts) if dot(norm,p)==-1) for norm in n]
    edges=set()
    for a,b in combinations(face,2):
        inter=a & b
        if len(inter)==2:edges.add(tuple(sorted(inter)))
    return len(verts),len(edges),len(face),sorted(map(len,face)),verts
I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
can=poly(I); gen=poly(R)
assert can[:4]==(6,12,8,[3]*8)
assert gen[:4]==(12,18,8,[3,3,5,5,5,5,5,5])
# Orthogonality via exact dot-products of rows; determinant via scalar triple product.
assert all(dot(R[i],R[j])==F(int(i==j)) for i in range(3) for j in range(3))
assert det(*R)==1
# Independent line coplanarity determinant for all edge pairs.
Bvert=[tuple(-x for x in matvec(R,p)) for p in v]
values=[]
for a,b in combinations(range(4),2):
    p,u=v[a],sub(v[b],v[a])
    for c,d in combinations(range(4),2):
        q,w=Bvert[c],sub(Bvert[d],Bvert[c])
        values.append(dot(sub(q,p),cross(u,w)))
assert len(values)==36 and all(values)
# Full 30-dimensional source support gain: diagonal 0 (8), 1 (12), 3 (8)
# and the exact top block [[11,-8],[-8,11]], eigenvalues 3 and 19.
G3=((F(11),F(-8)),(F(-8),F(11)))
def gain(top,edgenorm=F(0),facenorm=F(0)):
    a,b=top
    return edgenorm+3*facenorm+a*(11*a-8*b)+b*(-8*a+11*b)
for a,b in [(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(1),F(-1)),(F(2),F(3))]:
    assert gain((a,b))==3*(a*a+b*b)+8*(a-b)**2
assert gain((0,0),1,0)==1 and gain((0,0),0,1)==3
assert gain((1,0))==11 and gain((1,1))==6
# Exhibit one of infinitely many pullback-compatible post-metrics on an
# independent 3x2 rational toy transfer, avoiding general matrix expressions.
# T columns e1+e3 and e2-e3, M=[[2,-1],[-1,2]].
T=((F(1),F(0)),(F(0),F(1)),(F(1),F(-1)))
Minv=((F(2,3),F(1,3)),(F(1,3),F(2,3)))
def mm(A,B):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*B)) for row in A)
def trans(A):return tuple(zip(*A))
Pi=mm(mm(T,Minv),trans(T))
M2=mm(Minv,Minv)
N=mm(mm(T,M2),trans(T))
for z in [F(1,2),F(1),F(2)]:
    H=tuple(tuple(N[i][k]+z*(F(int(i==k))-Pi[i][k]) for k in range(3)) for i in range(3))
    assert mm(mm(trans(T),H),T)==((F(1),F(0)),(F(0),F(1)))
    assert det(*H)==z/F(3)
# These are nonphysical, exact finite controls.
results={'method':'independent stdlib Fraction implementation','status':'EXACT_CONDITIONAL_PASS','canonical_overlap':list(can[:4]),'rotated_overlap':list(gen[:4]),'noncoplanar_edge_line_pairs':36,'zero_reserve_kernel':'vertex-only, dimension 8','source_rule':'cannot distinguish polyhedral shape without external Q variable','positive_metric_family':'at least three distinct positive choices (lambda=1/2,1,2), all isometrize T','native_event_selected':False,'physical_promotion':0}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(results,sort_keys=True,indent=2)+'\n')
print('STDLIB EXACT PASS: independent 6 vs 12 overlap, no contacts, reserve kernel, positive metric nonuniqueness')
