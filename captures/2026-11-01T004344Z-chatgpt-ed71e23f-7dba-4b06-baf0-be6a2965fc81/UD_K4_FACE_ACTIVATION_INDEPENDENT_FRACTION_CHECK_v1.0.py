#!/usr/bin/env python3
"""Independent pure-Fraction check for the K4 face-readiness and birth no-go.
No SymPy and no imports from the primary verification script.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

verts=tuple(range(4)); edges=tuple(combinations(verts,2)); faces=tuple(combinations(verts,3))
B=[[0 for _ in faces] for _ in edges]
for j,(p,q,r) in enumerate(faces):
    B[edges.index((q,r))][j]+=1
    B[edges.index((p,r))][j]-=1
    B[edges.index((p,q))][j]+=1
u=[-1,1,-1,1]
count=0

def check(value,label):
    global count
    if not value:raise AssertionError(label)
    count+=1

def dot(x,y):return sum((a*b for a,b in zip(x,y)),start=0)
def mv(M,x):return [dot(row,x) for row in M]
def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tpose(M):return [list(t) for t in zip(*M)]
G=matmul(tpose(B),B)
check(G==[[4*(i==j)-u[i]*u[j] for j in range(4)] for i in range(4)],'incidence spectral identity')
check(mv(B,u)==[0]*6,'closed tetrahedral boundary')
for c in product((F(-1),F(0),F(1)),repeat=4):
    norm=dot(c,c)
    boundary=mv(B,c)
    if not norm:
        check(not any(boundary),'empty chain')
        continue
    C=F(dot(u,c)**2,4*norm)
    D=F(dot(boundary,boundary),4*norm)
    check(C+D==1,'coherence partition')
    check(0<=C<=1 and 0<=D<=1,'coherence bounds')
    check((D==0)==(all(a==0 for a in boundary)),'boundary null iff readiness')

# Permutation covariance with sign for the oriented face coordinates.
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
for p in permutations(verts):
    cp=[0]*4
    for j,f in enumerate(faces):
        mapped=[p[v] for v in f]
        cp[faces.index(tuple(sorted(mapped)))]+=u[j]*sign(mapped)
    check(cp==[sign(p)*v for v in u],'oriented pseudovector covariance')

# A closed full shell and positive face amplitudes can remain unfilled,
# or admit a 3-cell under any source/angle rule; local conservation alone
# cannot choose which legal update occurs.
c=[F(v,2) for v in u]
check(dot(c,c)==1 and mv(B,c)==[0]*6,'unit coherent shell')
for a,b in ((F(3,5),F(4,5)),(F(5,13),F(12,13))):
    c_after=[a*v for v in c]
    q=dot(u,c)/2
    t=b*q
    check(dot(c_after,c_after)+t*t==1,'quadratic stock conservation')
    check(mv(B,c_after)==[0]*6,'coherent shell preserved')
    check(b!=0,'filled and hold differ')

# Both hold and automatic fill are S4-invariant on occupancy, but the
# primitive source has no choice rule for either map.
for mask in range(16):
    for p in permutations(verts):
        moved=sum(1<<p[i] for i in verts if mask & 1<<i)
        check((moved==15)==(mask==15),'automatic completion is symmetric')

result={'artifact':'UD_K4_FACE_ACTIVATION_INDEPENDENT_FRACTION_CHECK_v1.0',
        'checks_passed':count,'dependency':'no shared implementation with primary verifier',
        'status':'EXACT_FINITE_REPLICATION_OF_MATHEMATICAL_IDENTITY_ONLY',
        'physical_promotion':0}
Path(__file__).with_name('UD_K4_FACE_ACTIVATION_INDEPENDENT_RESULTS_v1.0.json').write_text(json.dumps(result,indent=2)+'\n')
print('Independent exact Fraction checks PASSED:',count)
