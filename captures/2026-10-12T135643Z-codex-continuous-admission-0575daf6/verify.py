#!/usr/bin/env python3
"""Exact coefficient and event-count checks for a *candidate* contrast-zero law."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json
import random

VERTICES=tuple(range(4))
S=[list(combinations(VERTICES,k)) for k in range(1,5)]
SIMPLEX=sum(S,[])
IDX={simplex:i for i,simplex in enumerate(SIMPLEX)}
EDGES=S[1]
PAIRS=((0,5),(1,4),(2,3))
N=15

def generator():
    a=[[F(0) for _ in range(N)] for _ in range(N)]
    for high in SIMPLEX:
        if len(high)<2: continue
        j=IDX[high]
        for k in range(len(high)):
            i=IDX[high[:k]+high[k+1:]]
            a[i][j]=-F((-1)**k)
            a[j][i]=F((-1)**k)
    return a

def mv(a,c):
    return [sum((x*y for x,y in zip(row,c)),F(0)) for row in a]

def contrast_on_edges(edge_coordinates):
    e=[sum((edge_coordinates[j]**2 for j in p),F(0)) for p in PAIRS]
    return tuple(3*x-sum(e) for x in e)

def coefficients(a,c):
    ac=mv(a,c)
    u=[c[IDX[e]] for e in EDGES]
    v=[ac[IDX[e]]/2 for e in EDGES]
    u2=contrast_on_edges(u)
    v2=contrast_on_edges(v)
    uv=contrast_on_edges([x+y for x,y in zip(u,v)])
    return tuple(((x+y)/2,(x-y)/2,(z-x-y)/2)
                 for x,y,z in zip(u2,v2,uv))

def d_at_key_times(coeff):
    return (tuple(alpha+beta for alpha,beta,gamma in coeff),
            tuple(alpha+gamma for alpha,beta,gamma in coeff),
            tuple(alpha-beta for alpha,beta,gamma in coeff))

def kind(t):
    alpha,beta,gamma=t
    r2=beta*beta+gamma*gamma
    if r2==0 and alpha==0: return 'IDENTICALLY_ZERO'
    if alpha*alpha<r2: return 'TWO_SIMPLE_ZEROS_PER_PERIOD'
    if alpha*alpha==r2: return 'TANGENCY_NO_FLIP'
    return 'NO_ZERO'

def sign_of_order(mapped):
    return -1 if sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))%2 else 1

def group_action(g,c):
    result=[F(0)]*N
    for simplex in SIMPLEX:
        mapped=tuple(g[v] for v in simplex)
        result[IDX[tuple(sorted(mapped))]]=sign_of_order(mapped)*c[IDX[simplex]]
    return result

def pair_permutation(g):
    eidx={e:i for i,e in enumerate(EDGES)}
    q=[]
    for pair in PAIRS:
        mapped={eidx[tuple(sorted((g[v] for v in EDGES[k])))] for k in pair}
        q.append(next(j for j,p in enumerate(PAIRS) if set(p)==mapped))
    return q

def main():
    a=generator()
    alias=[F(t) for t in (2,-2,2,1,2,2,0,0,-2,2,0,2,1,2,1)]
    coeff=coefficients(a,alias)
    assert coeff==((F(59,4),F(-27,4),F(-16)),
                   (F(-1),F(9),F(2)),
                   (F(-55,4),F(-9,4),F(14)))
    start,mid,end=d_at_key_times(coeff)
    assert (start,mid,end)==((F(8),F(8),F(-16)),
                             (F(-5,4),F(1),F(1,4)),
                             (F(43,2),F(-10),F(-23,2)))
    assert all(kind(t)=='TWO_SIMPLE_ZEROS_PER_PERIOD' for t in coeff)
    assert [int(x*y<0) for x,y in zip(start,end)]==[0,1,0]
    assert [2,1,2]==[2 if start[i]*end[i]>0 and start[i]*mid[i]<0 else 1
                       for i in range(3)]
    zero=[F(0)]*N
    assert all(kind(t)=='IDENTICALLY_ZERO' for t in coefficients(a,zero))
    single_edge=[F(0)]*N;single_edge[IDX[(0,1)]]=F(1)
    assert kind(coefficients(a,single_edge)[0])=='TANGENCY_NO_FLIP'
    rng=random.Random(8317)
    fixtures=[zero,single_edge,alias]
    fixtures.extend([[F(rng.randrange(-2,3)) for _ in range(N)] for _ in range(100)])
    symmetry=0
    for c in fixtures:
        co=coefficients(a,c)
        for g in permutations(VERTICES):
            perm=pair_permutation(g)
            actual=coefficients(a,group_action(g,c))
            expected=[None]*3
            for i,j in enumerate(perm): expected[j]=co[i]
            assert actual==tuple(expected)
            symmetry+=1
    out={'status':'PASS','law_status':'CANDIDATE continuous sign-change admission',
         'alias_coefficients':[[str(x) for x in row] for row in coeff],
         'alias_window_simple_zero_counts':[2,1,2],
         'alias_endpoint_receipt':[0,1,0],
         'zero_state':'IDENTICALLY_ZERO no event by convention',
         'single_edge_A':'TANGENCY_NO_FLIP',
         'S4_coefficient_covariance_checks':symmetry,
         'full_period_per_active_pair':'pi/2 internal parameter, exactly two simple crossings',
         'independent_target':'NOT_RUN','physical_promotion':0}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
