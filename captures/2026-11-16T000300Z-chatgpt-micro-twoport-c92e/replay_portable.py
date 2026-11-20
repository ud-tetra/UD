#!/usr/bin/env python3
"""Portable exact replay: balanced two-port and equal-budget A/B kinetics.
No NumPy/SymPy; phase law, channel norms, equilibrium are conditional inputs.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import factorial, prod

pi = tuple(map(F, ('16/25', '4/25', '1/25', '4/25')))
norm = {'A':tuple(map(F,('16/25','4/25','4/25','16/25'))),
        'B':tuple(map(F,('10/25','10/25','10/25','10/25')))}
p = (F(1),F(1,2),F(0),F(1,2))
assert sum(norm['A']) == sum(norm['B']) == F(8,5)
faces = sorted(set(combinations(range(4),3))|set(combinations((0,1,2,4),3)))
accepted = [b for b in product(range(2),repeat=5) if all(len({b[v] for v in face})>1 for face in faces)]
assert len(accepted)==6
stock = [tuple(e.count(k) for k in range(7)) for e in combinations_with_replacement(range(7),2)]
assert len(stock)==28
edges = [(i,j,'intra' if (3 in faces[i] and 3 in faces[j]) or (4 in faces[i] and 4 in faces[j]) else 'inter') for i in range(7) for j in range(i+1,7) if len(set(faces[i])&set(faces[j]))==2]
assert len(edges)==15
Z = (0,1,-1,1,-1,1,-1)
for label, nn in norm.items():
    c=tuple(x/2 for x in nn) # equal channels, quarter-turn U=i: bright intensity = n/2
    assert sum(c)==F(4,5)
    mat=[[F(0) for j in range(4)] for i in range(4)]
    for (i,j),v in zip(((0,1),(1,2),(2,3),(3,0)),c):
        mat[i][j]+=v/pi[i];mat[i][i]-=v/pi[i]
        mat[j][i]+=v/pi[j];mat[j][j]-=v/pi[j]
    vec=[F(1) for i in range(4)]; moments=[]
    for n in range(5):
        moments.append(sum((pi[i]*vec[i] for i in range(4)),F(0)))
        vec=[sum((mat[i][j]*vec[j] for j in range(4)),F(0))-3*p[i]*vec[i] for i in range(4)]
    expected = [F(1),F(-12,5),F(162,25),F(-504,25), F(72) if label=='A' else F(29529,400)]
    assert moments==expected,(label,moments)
    # All 672 states: require each allowed stock transfer to conserve stock,
    # obey positive donor capacity and satisfy multinomial detailed balance.
    count=0
    for b in accepted:
        assert sum(sum(a!=q for a,q in zip(b,z))==2 for z in accepted)==2
        for phase in range(4):
            for x in stock:
                px=F(2,49*prod(factorial(t) for t in x))
                for i,j,cat in edges:
                    weight=F(1) if cat=='intra' else p[phase]
                    for donor,recv in ((i,j),(j,i)):
                        if not x[donor] or weight==0:continue
                        y=list(x);y[donor]-=1;y[recv]+=1
                        py=F(2,49*prod(factorial(t) for t in y))
                        assert sum(y)==2 and px*x[donor]*weight==py*y[recv]*weight
                        count+=1
    assert count>0
    print(label, 'moments',list(map(str,moments)), 'stock_transitions',count)
assert F(29529,400)-F(72)==F(729,400)
assert (F(3,5)+F(4,5))**2/2==F(49,50)
assert (F(3,5)-F(4,5))**2/2==F(1,50)
print('PORTABLE REPLAY PASS')
