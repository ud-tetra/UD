#!/usr/bin/env python3
"""Independent exact replay: stationary two-step mode moments and source-gate family.
Uses no sympy/scipy/numpy and does not import the main verification script.
"""
from itertools import combinations, combinations_with_replacement
from fractions import Fraction as Q
from math import factorial
import json

faces=[(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4)]
F=len(faces); M=2
pairs=[]
for a,b in combinations(range(F),2):
    if len(set(faces[a])&set(faces[b]))==2:
        pairkind='inner' if (3 in faces[a] and 3 in faces[b]) or (4 in faces[a] and 4 in faces[b]) else 'seam'
        pairs.append((a,b,pairkind))
assert sum(t[2]=='seam' for t in pairs)==9
occ=[]
for pts in combinations_with_replacement(range(F),M):
    occ.append(tuple(pts.count(j) for j in range(F)))
assert len(occ)==28
z=lambda x:sum((x[i] if 3 in f else -x[i] if 4 in f else 0) for i,f in enumerate(faces))

def phase_rule(q):return (Q(1),q,Q(0),q)

def Qobservable(fn, state, phase, kappa):
    d,x=state
    original=fn(state)
    out=Q(0)
    for jump in (-1,1):out+=Q(1,2)*(fn(((d+jump)%4,x))-original)
    for a,b,kind in pairs:
        strength=Q(1) if kind=='inner' else phase[d]
        multiplier=1+kappa*(x[a]+x[b]-1)
        for src,dst in ((a,b),(b,a)):
            if x[src] and strength:
                y=list(x);y[src]-=1;y[dst]+=1
                out+=x[src]*strength*multiplier*(fn((d,tuple(y)))-original)
    return out

def run(q,kappa):
    phase=phase_rule(q)
    weights={x:Q(factorial(M),F**M*__import__('math').prod(factorial(k) for k in x)) for x in occ}
    assert sum(weights.values())==1
    coords=[(d,x) for d in range(4) for x in occ]
    prob=lambda state:weights[state[1]]/4
    var=sum(prob(st)*z(st[1])**2 for st in coords)
    assert var==Q(12,7)
    zfunc=lambda st:Q(z(st[1]))
    drift={st:Qobservable(zfunc,st,phase,kappa) for st in coords}
    qdrift=lambda st:drift[st]
    r1=sum(prob(st)*z(st[1])*drift[st] for st in coords)/var
    r2=sum(prob(st)*z(st[1])*Qobservable(qdrift,st,phase,kappa) for st in coords)/var
    return (r1,r2)

results={
'harmonic':run(Q(1,2),Q(0)),
'squared':run(Q(1,4),Q(0)),
'strict':run(Q(0),Q(0)),
'occupancy_interaction':run(Q(1,2),Q(1))}
expected={'harmonic':(Q(-3,2),Q(27,8)),'squared':(Q(-9,8),Q(81,32)),
          'strict':(Q(-3,4),Q(9,4)),'occupancy_interaction':(Q(-27,14),Q(351,56))}
assert results==expected,(results,expected)
# Same first-harmonic quadrature limits but continuum of source laws.
assert phase_rule(Q(1,2))!=phase_rule(Q(1,4))
assert results['occupancy_interaction'][0] / results['harmonic'][0]==Q(9,7)
assert results['occupancy_interaction'][1]!=results['harmonic'][1]*Q(9,7)**2
print(json.dumps({'status':'PASS','implementation':'stdlib independent 112-state exact marginal','results':{k:[str(x) for x in val] for k,val in results.items()},'physical_promotion':0},indent=2))
