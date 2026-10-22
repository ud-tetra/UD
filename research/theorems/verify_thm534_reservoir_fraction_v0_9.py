#!/usr/bin/env python3
"""Independent stdlib Fraction check for THM534 v0.9 candidate. No SymPy."""
from fractions import Fraction as Q
from itertools import combinations,product
edges=list(combinations(range(4),2));faces=list(combinations(range(4),3))
def step(x,r,beta=(1,)*4,tau=(1,)*6):
    a=[int(t>0) for t in r]
    h=[a[u]*a[v]*beta[u]*beta[v]*tau[k] for k,(u,v) in enumerate(edges)]
    j=[Q(-h[k],4)*(x[v]-x[u]) for k,(u,v) in enumerate(edges)]
    p=list(x)
    for k,(u,v) in enumerate(edges):p[u]-=j[k];p[v]+=j[k]
    s=[(r[k]-p[k])/4 for k in range(4)]
    xn=[p[k]+s[k] for k in range(4)]
    rn=[r[k]-s[k] for k in range(4)]
    f=[j[edges.index((b,c))]-j[edges.index((a,c))]+j[edges.index((a,b))]
        for a,b,c in faces]
    return xn,rn,p,s,j,f,h
def sq(v):return sum((a*a for a in v),Q(0))
count=nonzero=0
for bits in product((0,1),repeat=4):
    for v in range(4):
        x=[Q(int(k==v)) for k in range(4)]
        r=list(map(Q,bits))
        xn,rn,p,s,j,f,h=step(x,r)
        m=sum(x)+sum(r); mu=m/8
        E0=sq([a-mu for a in x+r])
        E1=sq([a-mu for a in xn+rn])
        assert m==sum(xn)+sum(rn)
        assert min(xn+rn)>=0
        assert E0-E1>=sq(f)+Q(3,8)*sq([p[k]-r[k] for k in range(4)])
        assert -f[0]+f[1]-f[2]+f[3]==0
        nonzero+=int(any(f));count+=1
assert count==64 and nonzero==24
x=list(map(Q,[1,0,0,0]));r=list(map(Q,[1,1,1,0]))
xn,rn,p,s,j,f,h=step(x,r)
assert tuple(h)==(1,1,0,1,0,0)
assert xn==[Q(5,8),Q(7,16),Q(7,16),Q(0)]
assert rn==[Q(7,8),Q(13,16),Q(13,16),Q(0)]
assert f==[Q(0),Q(1,4),Q(1,4),Q(0)]
print("PASS pure Fraction: 64 cases, 24 nonzero face circulation; exact budget")
print("Physical promotion=0; positive-reserve bit NOT established UD closure")
