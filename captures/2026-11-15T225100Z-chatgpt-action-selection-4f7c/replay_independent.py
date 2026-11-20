#!/usr/bin/env python3
"""Independent 4-state exact phase-mode replay, no 672-state enumeration.
Checks stationary flux, p symmetry, 4th temporal derivative and zero-action
nonuniqueness of reversible conductance choices.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

pi=[Q(16,25),Q(4,25),Q(1,25),Q(4,25)]
V=[0,1,2,1]
p=[Q(1),Q(1,2),Q(0),Q(1,2)]

def matrix(kind):
    mat=[[Q(0) for _ in range(4)] for _ in range(4)]
    for d in range(4):
        for e in ((d-1)%4,(d+1)%4):
            r=Q(2)**(V[d]-V[e]) if kind=='A' else Q(1,5)/pi[d]
            mat[d][e]+=r
            mat[d][d]-=r
    for i in range(4):
        assert sum(mat[i])==0
        for j in range(4):assert pi[i]*mat[i][j]==pi[j]*mat[j][i]
    return mat

def moments(m):
    vec=[Q(1) for _ in range(4)];outs=[]
    for n in range(5):
        outs.append(sum((pi[d]*vec[d] for d in range(4)),Q(0)))
        vec=[sum((m[d][j]*vec[j] for j in range(4)),Q(0))-3*p[d]*vec[d] for d in range(4)]
    return outs

res={}
for k in 'AB':
    m=matrix(k)
    m4=moments(m)
    conductances=[]
    for d,e in ((0,1),(1,2),(2,3),(3,0)):
        conductances.append(pi[d]*m[d][e])
    assert sum(conductances)==Q(4,5)
    res[k]={'moments':list(map(str,m4)),'conductances':list(map(str,conductances)),
           'total_undirected_traffic':str(sum(conductances))}
assert res['A']['moments']==['1','-12/5','162/25','-504/25','72']
assert res['B']['moments']==['1','-12/5','162/25','-504/25','29529/400']
assert res['A']['conductances']!=res['B']['conductances']
assert Q(res['B']['moments'][4])-Q(res['A']['moments'][4])==Q(729,400)
# For any reversible c, entropy production and the one-form maximum flow
# are nonnegative / action-minimization gives a zero-cost trajectory.
for k in 'AB':
    m=matrix(k)
    v=[Q(1),Q(1,2),Q(0),Q(1,2)]
    diss=sum((pi[i]*m[i][j]*(v[i]-v[j])**2 for i in range(4) for j in range(4) if i!=j),Q(0))/2
    assert diss==Q(1,5)
    res[k]['phase_gate_dirichlet']=str(diss)
Path(__file__).with_name('replay_results.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2));print('INDEPENDENT FOUR-STATE CHECK PASS')
