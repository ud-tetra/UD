#!/usr/bin/env python3
"""Independent standard-library rational check for two-tetra finite generator."""
from itertools import product,combinations,combinations_with_replacement
from fractions import Fraction as F
from collections import defaultdict
from math import factorial,exp
faces=sorted(set(combinations((0,1,2,3),3))|set(combinations((0,1,2,4),3)))
edges=sorted(set(e for f in faces for e in combinations(f,2)))
L={i for i,f in enumerate(faces) if 3 in f};R={i for i,f in enumerate(faces) if 4 in f}
bits=[b for b in product((0,1),repeat=5) if all(len({b[i] for i in f})==2 for f in faces)]
assert len(bits)==6
pairs=[(b,c) for i,b in enumerate(bits) for c in bits[i+1:] if sum(a!=d for a,d in zip(b,c))==2]
assert len(pairs)==6
had={b:0 for b in bits}
for b,c in pairs: had[b]+=1;had[c]+=1
assert all(x==2 for x in had.values())
# raw binary ensemble 5 vertices
C=[]
for f in faces:
    row=[]
    for g in faces:
        brute=sum((F(int(len({state[i] for i in f})==2))-F(3,4))*(F(int(len({state[j] for j in g})==2))-F(3,4)) for state in product((0,1),repeat=5))/32
        formula=F(len(set(combinations(f,2))&set(combinations(g,2))),16)
        assert brute==formula
        row.append(formula)
    C.append(row)
internal=[];interface=[]
for i in range(7):
    for j in range(i+1,7):
        if len(set(faces[i])&set(faces[j]))==2:
            (internal if (i in L and j in L) or (i in R and j in R) else interface).append((i,j))
assert len(internal)==6 and len(interface)==9
v=[0,1,-1,1,-1,1,-1];w=[0,1,-1,-1,1,0,0]
for vec,cc,a,b in ((v,F(1,4),F(0),F(3)),(w,F(1,16),F(3),F(3))):
    assert [sum(C[i][j]*vec[j] for j in range(7)) for i in range(7)]==[cc*z for z in vec]
    for rate in [F(0),F(1,2),F(1)]:
        Lvec=[]
        for i in range(7):
            Lvec.append(sum((F(1) if (i,j) in internal or (j,i) in internal else rate)*(vec[i]-vec[j]) for j in range(7) if (min(i,j),max(i,j)) in internal+interface))
        assert Lvec==[(a+b*rate)*z for z in vec]
# enumerate all stock states in 2-unit register and verify stationary reversibility (fixed b,d)
occ=[]
for pick in combinations_with_replacement(range(7),2):occ.append(tuple(pick.count(i) for i in range(7)))
assert len(occ)==28
P=lambda x:F(factorial(2),7**2*__import__('math').prod(factorial(k) for k in x))
assert sum(map(P,occ))==1
for phase,rate in enumerate((F(1),F(1,2),F(0),F(1,2))):
    for x in occ:
        for i,j in internal+interface:
            coeff=F(1) if (i,j) in internal else rate
            if coeff==0:continue
            for src,dst in ((i,j),(j,i)):
                if x[src]:
                    y=list(x);y[src]-=1;y[dst]+=1;y=tuple(y)
                    assert y in occ and P(x)*x[src]*coeff==P(y)*y[dst]*coeff
# Moments dynamic phase at t=0: constant phase stationary, L_phase sums vanish.
pvals=[F(1),F(1,2),F(0),F(1,2)]
l1=[3*q for q in pvals];l2=[3+3*q for q in pvals]
assert sum(l1,F(0))/4==F(3,2) and sum((q*q for q in l1),F(0))/4==F(27,8)
assert sum(l2,F(0))/4==F(9,2) and sum((q*q for q in l2),F(0))/4==F(171,8)
assert all(l2[i]-l1[i]==3 for i in range(4))
print('PASS independent stdlib: 6 admissible states, 6 min moves; face covariance, two common modes, 2-unit detailed balance, dynamic-phase moments')
