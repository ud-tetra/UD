#!/usr/bin/env python3
"""Independent stdlib-only Fraction verification; no imports from primary code."""
from itertools import permutations, combinations, product
from fractions import Fraction as F
from pathlib import Path
import json

faces=list(combinations(range(4),3))
u=(-1,1,-1,1)
checks={}
def ck(name,predicate):
    if not predicate: raise AssertionError(name)
    checks[name]=checks.get(name,0)+1

def parity(xs):
    n=0
    for i in range(len(xs)):
        for j in range(i+1,len(xs)):
            if xs[i]>xs[j]: n+=1
    return -1 if n%2 else 1

def face_action(p):
    m=[[0]*4 for _ in range(4)]
    for j,f in enumerate(faces):
        seq=tuple(p[k] for k in f)
        row=faces.index(tuple(sorted(seq)))
        m[row][j]=parity(seq)
    return m

def transpose(a):return [list(x) for x in zip(*a)]
def multiply(a,x):return [sum(v*w for v,w in zip(row,x)) for row in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def rank(mat):
    m=[[F(x) for x in row] for row in mat]
    colcount=len(m[0]); rank=0
    for c in range(colcount):
        pivot=next((i for i in range(rank,len(m)) if m[i][c]),None)
        if pivot is None:continue
        m[rank],m[pivot]=m[pivot],m[rank]
        a=m[rank][c]
        m[rank]=[z/a for z in m[rank]]
        for i in range(len(m)):
            if i==rank:continue
            factor=m[i][c]
            if factor:m[i]=[x-factor*y for x,y in zip(m[i],m[rank])]
        rank+=1
    return rank

alternating=[]; trivial=[]
all_perms=list(permutations(range(4)))
for p in all_perms:
    m=face_action(p);s=parity(p)
    ck('parity_shell_transform',multiply(m,list(u))==[s*x for x in u])
    mt=transpose(m)
    for i in range(4):
        alternating.append([mt[i][j]-(s if i==j else 0) for j in range(4)])
        trivial.append([mt[i][j]-(1 if i==j else 0) for j in range(4)])
    for vector in product((-1,0,1),repeat=4):
        q=F(dot(u,vector),2)
        rv=multiply(m,vector)
        rq=F(dot(u,rv),2)
        ck('pseudoscalar_covariance',rq==s*q)
        ck('orientation_even_squared_readout',rq*rq==q*q)
# A hard four-face gate without an orientation or transport seed can be
# S4 invariant only if all four face gates agree.
for facegate in product((0,1), repeat=4):
    invariant=True
    for p in all_perms:
        m=face_action(p)
        unsigned=[[abs(z) for z in row] for row in m]
        if multiply(unsigned,list(facegate)) != list(facegate):
            invariant=False
            break
    ck('binary_hard_gate_all_or_none',invariant==(sum(facegate) in (0,4)))
ck('alternating_intertwiner_rank',rank(alternating)==3)
ck('trivial_intertwiner_rank',rank(trivial)==4)

for vector in product((-1,0,1),repeat=4):
    q=F(dot(u,vector),2)
    parallel=[F(z)*q/2 for z in u]
    perp=[F(a)-b for a,b in zip(vector,parallel)]
    ck('support_orthogonal_decomposition',dot(parallel,perp)==0)
    ck('support_orthogonal_decomposition',dot(vector,vector)==dot(perp,perp)+q*q)
    for a,b in ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17))):
        newface=[p+a*v for p,v in zip(perp,parallel)]
        newbulk=b*q
        ck('rational_transfer_conservation',dot(newface,newface)+newbulk*newbulk==dot(vector,vector))
        ck('support_transfer_bound',0<=newbulk*newbulk<=q*q)

# Four faces, one interior: closed if and only if all face slots present or none.
edges=list(combinations(range(4),2))
face_edges=[]
for f in faces:
    b=[0]*len(edges)
    for i in range(3):
        b[edges.index(f[:i]+f[i+1:])]=(-1)**i
    face_edges.append(b)
for mask in product((0,1),repeat=4):
    vals=[u[i]*mask[i] for i in range(4)]
    edge_boundary=[sum(face_edges[f][e]*vals[f] for f in range(4)) for e in range(6)]
    ck('binary_face_closure',all(z==0 for z in edge_boundary)==(sum(mask) in (0,4)))

# Same source input, two distinct occupied 3-cells and a HOLD, all stock-conserving.
face=[F(v,2) for v in u]
outputs=[]
for a,b,occupied in ((F(1),F(0),0),(F(3,5),F(4,5),1),(F(5,13),F(12,13),1)):
    new=[a*v for v in face]
    ck('same_prestate_support_receipt',dot(new,new)+b*b==1)
    outputs.append((occupied,tuple(new),b))
ck('distinct_same_prestate_outcomes',len(set(outputs))==3)

result={
  'artifact':'UD_K4_OMEGA0_PREBIRTH_SOURCE_CHANNEL_v1.1',
  'method':'Independent stdlib fractions.Fraction and hand-implemented Gaussian elimination',
  'groups':checks,'checks_total':sum(checks.values()),
  'signed_linear_channel_dimension':4-rank(alternating),
  'even_linear_channel_dimension':4-rank(trivial),
  'physical_promotion':0,
  'status':'PASS_SCOPED_CONDITIONAL'
}
Path(__file__).with_name('UD_K4_PREBIRTH_SOURCE_INDEPENDENT_RESULTS_v1.1.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',result['checks_total'],'independent exact checks;',len(checks),'groups')
print('signed Hom dim:',result['signed_linear_channel_dimension'],'even Hom dim:',result['even_linear_channel_dimension'])
