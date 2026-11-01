#!/usr/bin/env python3
"""Numerical corroboration of analytic angular cocycle and harmonic-norm envelope."""
from math import atan2,pi
from collections import Counter
from verify_transfer_and_scaling import build_tets,subcomplex

def winding_rings(m, r, z):
    # CCW square boundary with (m,m) at center.
    v=[]
    v += [(x,m-r,z) for x in range(m-r,m+r)]
    v += [(m+r,y,z) for y in range(m-r,m+r)]
    v += [(x,m+r,z) for x in range(m+r,m-r,-1)]
    v += [(m-r,y,z) for y in range(m+r,m-r,-1)]
    assert len(v)==8*r
    return v

def check(N):
    center=N//2
    q={(center,center,k) for k in range(3)}
    K=subcomplex({t for t in build_tets(N) if set(t).isdisjoint(q)})
    V,E,F,T=K
    lookup={e:i for i,e in enumerate(E)}
    def polar(v):return atan2(v[1]-center,v[0]-center)
    def wrap(x):
        while x<=-pi:x+=2*pi
        while x>pi:x-=2*pi
        return x
    omega=[wrap(polar(b)-polar(a))/(2*pi) for a,b in E]
    def val(u,v):
        e=tuple(sorted((u,v)))
        return omega[lookup[e]]*(1 if u==e[0] else -1)
    assert max(abs(val(a,b)+val(b,c)+val(c,a)) for a,b,c in F)<1e-12
    rings=[]
    for z in (0,1,2):
        for r in range(1,center+1):
            loop=winding_rings(center,r,z)
            p=sum(val(loop[i],loop[(i+1)%len(loop)]) for i in range(len(loop)))
            assert abs(abs(p)-1)<1e-12,(z,r,p)
            rings.append(p)
    groups=Counter()
    for a,b in E:
        r=min(max(abs(a[0]-center),abs(a[1]-center)),
              max(abs(b[0]-center),abs(b[1]-center)))
        assert r>=1
        assert abs(omega[lookup[(a,b)]])<=1/r+1e-12
        groups[r]+=1
        assert groups[r]<=336*r
    observed=sum(x*x for x in omega)
    harmonic=sum(1/r for r in range(1,center+1))
    assert observed<=336*harmonic
    assert len(rings)==3*center
    return {'N':N,'edge_count':len(E),'cochain_norm_sq':observed,
            'analytical_upper':336*harmonic,'min_ring_count':len(rings),
            'ring_periods':rings,'edges_by_min_radius':dict(sorted(groups.items()))}

if __name__=='__main__':
    for n in (4,6,8,10):
        print(check(n))
