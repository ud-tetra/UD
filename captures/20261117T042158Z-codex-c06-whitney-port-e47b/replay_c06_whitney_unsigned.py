from fractions import Fraction as F
from itertools import combinations

def moment(i,j):
    return F(1,6) if i==j else F(1,12)

def grad(i,j):
    return 2*(F(i==j)-F(1,3))

def terms(edge):
    i,j=edge
    return [(i,j,1),(j,i,-1)]

cycle=[(0,1),(1,2),(2,0)]
for i,e in enumerate(cycle):
    for j,f in enumerate(cycle):
        mass=sum(s*t*moment(a,c)*grad(b,d)
                 for a,b,s in terms(e) for c,d,t in terms(f))
        assert mass == F(6*(i==j)-1,9)
assert F(1,48)*F(16,3) == F(1,9)

edges=list(combinations(range(4),2))
faces=list(combinations(range(4),3))
pairs=[(i,j) for i,j in combinations(range(6),2)
       if not set(edges[i]) & set(edges[j])]

def mode(weights, sign):
    result=[0]*6
    for (i,j),weight in zip(pairs,weights):
        result[i],result[j]=weight,sign*weight
    return result

for i,e in enumerate(edges):
    for j,f in enumerate(edges):
        assert sum(set(e+f)<=set(face) for face in faces)==2*(i==j)+int(len(set(e)&set(f))==1)
for ell in [F(0),F(1),F(3,2)]:
    gab=[[sum(F(6*(i==j)+ell-1,9) for face in faces if set(e+f)<=set(face))
          for j,f in enumerate(edges)] for i,e in enumerate(edges)]
    for sign,weights in [(1,(1,-1,0)),(1,(1,1,-2)),
                         (-1,(1,0,0)),(-1,(0,1,0)),(-1,(0,0,1))]:
        x=mode(weights,sign)
        rate=F(4,3) if sign==1 else 2*(5+ell)/9
        assert [sum(a*b for a,b in zip(row,x)) for row in gab]==[rate*v for v in x]
assert F(4,3)/F(10,9)==F(6,5)
print('PASS_EXACT · nine Whitney mass entries, all flag incidence counts, and five modes at three rotational weights')
