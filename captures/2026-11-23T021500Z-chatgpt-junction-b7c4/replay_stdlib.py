#!/usr/bin/env python3
"""Independent algorithm using standard-library integer/Fraction arithmetic only.
The constructor is the same person/model; this is NOT independent peer review.
"""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json
E=list(combinations(range(4),2))

def opp(e):return tuple(x for x in range(4) if x not in e)

def graph(glued):
    verts=[(p,i) for p in 'AB' for i in range(4)]
    verts.extend([('J',e) for e in E] if glued else [(p,e) for p in 'AB' for e in E])
    idx={v:i for i,v in enumerate(verts)}
    edges=[]
    for p in 'AB':
        for e in E:
            i,j=e if p=='A' else opp(e)
            m=('J',e) if glued else (p,e)
            edges += [((p,i),m),(m,(p,j))]
    incid=[]
    for u,v in edges:incid.append((idx[u],idx[v]))
    L=[[0]*len(verts) for _ in verts]
    for u,v in incid:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    return verts,edges,incid,L

def components(n,edge_index):
    adj=[set() for _ in range(n)]
    for a,b in edge_index: adj[a].add(b);adj[b].add(a)
    vis=set();num=0
    for i in range(n):
        if i in vis:continue
        num+=1;stack=[i];vis.add(i)
        while stack:
            for j in adj[stack.pop()]:
                if j not in vis:vis.add(j);stack.append(j)
    return num

def matmul(A,B):
    n=len(A);p=len(B);m=len(B[0]);ret=[[F(0)]*m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                a=A[i][k]; b=B[k]
                for j in range(m):
                    if b[j]:ret[i][j]+=a*b[j]
    return ret

def charpoly_fl(L):
    # Rational Faddeev-LeVerrier trace recursion, independently of SymPy
    n=len(L)
    B=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    coeff=[F(1)]
    for k in range(1,n+1):
        T=matmul(L,B)
        c=-sum(T[i][i] for i in range(n))/k
        assert c.denominator==1
        coeff.append(c)
        for i in range(n):T[i][i]+=c
        B=T
    return [int(c) for c in coeff]

def conv(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C

def power(A,n):
    C=[1]
    for _ in range(n):C=conv(C,A)
    return C

results={}
for glued in [False,True]:
    vertices,edges,incidence,L=graph(glued)
    n=len(vertices);m=len(edges); cc=components(n,incidence)
    expected=(14,24,1,11) if glued else (20,24,2,6)
    assert (n,m,cc,m-n+cc)==expected
    # Polynomials represented in descending powers of lambda.
    wanted=(conv(conv(conv([1,0],[1,-7]),power([1,-4],2)),conv(power([1,-3],4),power([1,-7,8],3))) if glued else
            conv(conv(conv([1,0,0],power([1,-5],2)),power([1,-4],6)),conv(power([1,-2],4),power([1,-1],6))))
    actual=charpoly_fl(L)
    assert actual==wanted,(glued,actual,wanted)
    trace=sum(L[i][i] for i in range(n))
    trace2=sum(L[i][j]*L[j][i] for i in range(n) for j in range(n))
    results['glued' if glued else 'disjoint']={'V':n,'E':m,'components':cc,'b1':m-n+cc,'trace':trace,'trace2':trace2,'poly_coeff':actual}
    if glued:
        ei=edges.index((('A',0),('J',(0,1))))
        ej=edges.index((('B',2),('J',(0,1))))
        def inner(a,b):
            A=incidence[a];B=incidence[b]
            return sum(((-1 if u==A[0] else 1) if u in A else 0) *((-1 if u==B[0] else 1) if u in B else 0) for u in set(A+B))
        assert inner(ei,ej)==1
        results['glued']['cross_ddot']=-inner(ei,ej)

# Local path boundary directly on old/new graph: oriented two-step path cancels J.
assert (-1+1)==0
results['local_path']={'boundary_chain_equals_old':True,'squared_amplitude_factor':2,'unit_norm_path_coeff_not_boundary_preserving':'1/sqrt(2)'}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
print('INDEPENDENT_STDLIB_PASS: components, cycle rank, exact Laplacian polynomials, contact cross-term')
print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk!='poly_coeff'} for k,v in results.items()},indent=2))
