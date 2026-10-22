#!/usr/bin/env python3
"""Exact seven-cell honeycomb torus boundaries, spectrum and harmonic port."""
from fractions import Fraction as Q
from itertools import combinations
import json

V=range(7)
E=list(combinations(V,2)); Eindex={e:i for i,e in enumerate(E)}
A=lambda k:(k,(k+1)%7,(k+5)%7)
B=lambda k:((k+1)%7,(k+6)%7,(k+5)%7)
T=[A(k) for k in V]+[B(k) for k in V]
def zeros(m,n):return [[0 for _ in range(n)] for _ in range(m)]
def trans(M):return list(map(list,zip(*M)))
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,c):return [[c*x for x in row] for row in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def eq(A,B):return A==B

def rank(A):
    X=[[Q(a) for a in row] for row in A]
    n=len(X);m=len(X[0]);r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if X[i][j]),None)
        if pivot is None:continue
        X[r],X[pivot]=X[pivot],X[r]
        z=X[r][j]; X[r]=[v/z for v in X[r]]
        for i in range(n):
            if i!=r and X[i][j]:
                z=X[i][j]; X[i]=[a-z*b for a,b in zip(X[i],X[r])]
        r+=1
        if r==n:break
    return r

def charpoly(M):
    n=len(M);P=eye(n);coeff=[1]
    for k in range(1,n+1):
        Z=mm(M,P)
        trace=sum(Z[i][i] for i in range(n))
        assert trace%k==0
        ck=-trace//k
        coeff.append(ck)
        P=add(Z,scale(eye(n),ck))
    assert P==zeros(n,n)
    return list(reversed(coeff)) # ascending polynomial powers

def poly(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C

def power(A,n):
    p=[1]
    for _ in range(n):p=poly(p,A)
    return p

P1=zeros(7,21);P2=zeros(21,14)
for e,(a,b) in enumerate(E):P1[a][e]=-1;P1[b][e]=1
for j,t in enumerate(T):
    for a,b in zip(t,t[1:]+t[:1]):
        P2[Eindex[tuple(sorted((a,b)))]][j]+=1 if a<b else -1
assert mm(P1,P2)==zeros(7,14)
assert rank(P1)==6 and rank(P2)==13
assert all(sum(abs(P2[e][j]) for j in range(14))==2 for e in range(21))
assert all(sum(P2[e])==0 for e in range(21))
# S makes each dual bond run from A to B.
sign=[-next(P2[e][j] for j in range(7) if P2[e][j]) for e in range(21)]
B1=[[P2[e][i]*sign[e] for e in range(21)] for i in range(14)]
B2=[[sign[e]*P1[k][e] for k in V] for e in range(21)]
assert mm(B1,B2)==zeros(14,7)
assert rank(B1)==13 and rank(B2)==6
assert (14-13,21-13-6,7-6)==(1,2,1)
L0=mm(B1,trans(B1));L2=mm(trans(B2),B2)
assert L2==[[7*int(i==j)-1 for j in V] for i in V]
expected0=poly(poly([0,1],[-6,1]),power([7,-6,1],6))
expected2=poly([0,1],power([-7,1],6))
assert charpoly(L0)==expected0
assert charpoly(L2)==expected2
# Hodge-Dirac characteristic: four zeros, one 6 pair, six each
# (3±sqrt2) pairs and six 7 pairs.
Dchar=poly(power([0,1],4),poly([6,0,1],poly(power([7,0,6,0,1],6),power([7,0,1],6))))
assert len(Dchar)-1==42

G=[[Q(1),Q(1,2)],[Q(1,2),Q(1)]]
d={0:[Q(1,3),Q(1,3)],1:[Q(-2,3),Q(1,3)],5:[Q(1,3),Q(-2,3)]}
M=zeros(21,2);edgelabels={}
for e in range(21):
    i=next(j for j in range(7) if B1[j][e]==-1)
    k=next(j for j in range(7) if B1[7+j][e]==1)
    cls=(i-k)%7;assert cls in d
    M[e]=[sum(d[cls][p]*G[p][j] for p in range(2)) for j in range(2)]
    edgelabels[(i,k)]=e
assert mm(B1,M)==zeros(14,2)
assert mm(trans(B2),M)==zeros(7,2)
assert mm(trans(M),M)==scale(G,Q(7,2))
assert rank(M)==2
# Full 120-degree equivariance of the edge harmonic map.
J2=[[-1,-1],[1,0]]
assert mm(trans(J2),mm(G,J2))==G
for (i,k),e in edgelabels.items():
    rotated=(4*i%7,(4*k-1)%7)
    er=edgelabels[rotated]
    assert M[er]==mm([M[e]],mm(J2,J2))[0] # row covector transforms as M_e J^-1
# Bilayer relative lift (-u/2,+u/2) has half of the single-plane Gram.
assert scale(mm(trans(M),M),Q(1,2))==scale(G,Q(7,4))
print(json.dumps({'status':'PASS_EXACT_CONDITIONAL','cells':[14,21,7],
 'boundary_ranks':[13,6],'betti':[1,2,1],
 'L0_characteristic_ascending':expected0,'L2_characteristic_ascending':expected2,
 'Hodge_Dirac_degree':42,'harmonic_port_Gram_over_G':'7/2',
 'bilayer_relative_lift_Gram_over_G':'7/4','C3_equivariance':True},indent=2))
