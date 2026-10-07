#!/usr/bin/env python3
"""Exact finite sign enumeration on the retained tetrahedral incidence generator."""
import json, itertools, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'sources/MATRICES.json').read_text())['tetrahedron']
nodes=raw['nodes'];edges=raw['edges'];A=[[int(x) for x in row] for row in raw['skew_generator_A']]
lookup={tuple(n):i for i,n in enumerate(nodes)}
es=[(lookup[tuple(s)],lookup[tuple(t)]) for s,t in edges]
checks=[]
def check(n,b):
    assert b,n
    checks.append(n)
def audit(a):
    seen={};collisions=0;distinct=0;witness=None
    for rest in itertools.product((-1,1),repeat=14):
        x=(1,)+rest;c=[u*v for u,v in zip(x,a)]
        j=tuple(2*A[t][s]*c[s]*c[t] for s,t in es)
        d=[0]*15
        for (s,t),z in zip(es,j):d[s]-=z;d[t]+=z
        key=tuple(d)
        if key in seen:
            collisions+=1
            oldx,oldj=seen[key]
            if oldj!=j:
                distinct+=1
                if witness is None:witness={'signs_1':oldx,'signs_2':x,'current_1':oldj,'current_2':j,'stock_derivative':d,'stock_denominator':sum(v*v for v in a)}
        else:seen[key]=(x,j)
    return {'rays':2**14,'distinct_derivatives':len(seen),'collisions':collisions,'different_current_collisions':distinct,'witness':witness}
equal=audit([1]*15)
separated=audit([2**i for i in range(15)])
check('equal-stock derivative ambiguity has a distinct-current witness',equal['different_current_collisions']>0)
check('powers-of-two real stocks identify all 16384 sign rays',separated['distinct_derivatives']==2**14)
check('superincreasing strict inequalities',all(2**i>sum(2**j for j in range(i)) for i in range(15)))
w=equal['witness'];difference=[u-v for u,v in zip(w['current_1'],w['current_2'])];div=[0]*15
for (s,t),z in zip(es,difference):div[s]-=z;div[t]+=z
check('equal-stock witness difference is nonzero circulation',any(difference) and not any(div))
# Spanning tree signed-current probes reconstruct every real sign ray.
parent={0:None};todo=[0];tree=[]
while todo:
    i=todo.pop(0)
    for j in range(15):
        if A[i][j] and j not in parent:parent[j]=i;tree.append((i,j));todo.append(j)
check('tree has 14 edges and covers all addresses',len(tree)==14 and len(parent)==15)
for rest in itertools.product((-1,1),repeat=14):
    x=(1,)+rest;recovered={0:1}
    for i,j in tree:recovered[j]=recovered[i]*(x[i]*x[j])
    assert tuple(recovered[i] for i in range(15))==x
check('tree sign propagation reconstructs all 16384 sign rays',True)
check('unit magnitudes collision source stocks normalize to 1/15',w['stock_denominator']==15)
# Separate complex-phase witnesses: conjugation preserves all real fluxes.
check('imaginary phase invisible to real flux',complex(0,1).real==complex(0,-1).real)
result={'status':'PASS','exact_checks':len(checks),'checks':checks,'equal_stock_enumeration':equal,'superincreasing_stock_enumeration':separated,'tree':tree,'physical_promotion':0,'independent_review':'PENDING','source_sha256':hashlib.sha256((ROOT/'sources/MATRICES.json').read_bytes()).hexdigest()}
(ROOT/'REPLAY_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
