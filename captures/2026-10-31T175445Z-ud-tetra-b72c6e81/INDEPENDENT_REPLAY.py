#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from fractions import Fraction
import sympy as s
# Independent fixed 3+1 slab verification, zero assumptions about physical time.
S=[(0,4,5,6,7),(0,1,5,6,7),(0,1,2,6,7),(0,1,2,3,7)]
c=Counter()
for i,sig in enumerate(S):
    for j in range(5):c[sig[:j]+sig[j+1:]]+=(-1)**(i+j)
c={k:v for k,v in c.items() if v}
assert len(c)==14 and c[(0,1,2,3)]==-1 and c[(4,5,6,7)]==1
d=Counter()
for sig,v in c.items():
    for j in range(4):d[sig[:j]+sig[j+1:]]+=v*(-1)**j
assert all(x==0 for x in d.values())
# Exact achromatic-redshift / additive detector-bias null.
a=Fraction(7,4);offset=Fraction(1,20)
lines=[Fraction(i) for i in (400,500,600)]
assert all(a*lam/lam-1==Fraction(3,4) for lam in lines)
zs=[(a*lam+offset)/lam-1 for lam in lines]
assert zs[0]-zs[2]==Fraction(1,24000)
# Exact 2x2 spectral mixing identity.
g,D,w=s.symbols("g D w",real=True)
H=s.Matrix([[0,g],[g,D]])
assert s.simplify((w*s.eye(2)-H).det()-(w*(w-D)-g*g))==0
print("PASS: four pentachora, 14 boundary tetrahedra, d^2=0, spectral and instrument null")
