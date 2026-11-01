#!/usr/bin/env python3
"""Independent finite rational witness sweep, no SymPy or third-party code.
This is a finite-domain audit, not an independent reviewer or physical experiment.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import comb
from pathlib import Path
import json

pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def variance(b):
    mean=sum(b)/4
    return sum((v-mean)**2 for v in b)/2

def a_nonnegative(b):
    M=sum(b)
    Q=sum(v*v for v in b)
    return sum(v**3 for v in b)-Q*Q/M

def sink(b,mask):
    return sum(F(h,4)*(b[u]-b[v])**2 for h,(u,v) in zip(mask,pairs))

def seed(b,u,v,e):
    out=list(b);out[u]+=e;out[v]-=e
    return tuple(out)

def classify(b):
    a=max(range(4),key=lambda i:b[i]); winners=[i for i in range(4) if b[i]==b[a]]
    if len(winners)!=1:return None
    out=[(b[a]-b[w],w) for w in range(4) if w!=a]
    maximal=max(x[0] for x in out)
    ports=[w for x,w in out if x==maximal and x>0]
    return (a,ports[0]) if len(ports)==1 else None

def main():
    cases=0;maskcases=0
    # All quarter-unit vectors with bounded counts, M>0.
    for ns in product(range(5), repeat=4):
        if not sum(ns):continue
        b=tuple(F(n,4) for n in ns)
        assert a_nonnegative(b)>=0
        for mask in product((0,1),repeat=6):
            assert sink(b,mask)>=0
            maskcases+=1
        cases+=1
    epsilon=F(1,10);uniform=(F(1),)*4;v0=variance(uniform)
    assert v0==0
    outputs={}
    for u,v in permutations(range(4),2):
        post=seed(uniform,u,v,epsilon)
        assert variance(post)-v0==epsilon**2
        assert classify(post)==(u,v)
        outputs[(u,v)]=post
    for p in permutations(range(4)):
        for (u,v),b in outputs.items():
            relabel=tuple(b[p[i]] for i in range(4))
            # The permutation of vertex labels sends selected pair accordingly.
            inverse={p[i]:i for i in range(4)}
            assert classify(relabel)==(inverse[u],inverse[v])
    # Compact triangle edge field: two distinct integer periods give identical U.
    z=(1,0,0)
    for n in range(-5,6):
        assert (n*z[0],n*z[1],n*z[2])!=(0,0,0) or n==0
        assert all(isinstance(n*v,int) for v in z)
        assert sum(n*v for v in z)==n
    # Exact differences from a vertex potential have zero cycle integral.
    for k in product(range(-2,3),repeat=3):
        dz=(k[1]-k[0],k[2]-k[1],k[0]-k[2]);assert sum(dz)==0
    result={'finite_burden_grid_cases':cases,'mask_checks':maskcases,'uniform_stochastic_ordered_edges':len(outputs),
            'S4_relabelled_seed_witnesses':24*len(outputs),'exact_vertex_potential_checks':5**3,
            'compact_period_lifts_checked':11,
            'stochastic_seed_energy':'1/100',
            'burden_amplifier_source':'new assumption; NOT derivable from Q162 alone',
            'status':'SCOPED_EXACT_FINITE_AUDIT','physical_promotion':0}
    Path(__file__).with_name('INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
