from fractions import Fraction as F
from itertools import combinations

def grad(i,j):
    return 2*(F(i==j)-F(1,3))

def moment(i,j):
    return F(1,6) if i==j else F(1,12)

def terms(edge):
    i,j=edge
    return [(i,j,1),(j,i,-1)]

cycle=[(0,1),(1,2),(2,0)]
for a,e in enumerate(cycle):
    i,j=e
    for b,f in enumerate(cycle):
        k,l=f
        mass=sum(s*t*moment(d,h)*grad(g,m)
                 for d,g,s in terms(e) for h,m,t in terms(f))
        curl=4*(grad(i,k)*grad(j,l)-grad(i,l)*grad(j,k))
        assert mass==F(6*(a==b)-1,9)
        assert curl==F(16,3)
assert F(3,16)*F(16,3)==1
assert F(16,3)/F(1,9)==48

edges=list(combinations(range(4),2))
faces=list(combinations(range(4),3))
pairs=[(i,j) for i,j in combinations(range(6),2)
       if not set(edges[i]) & set(edges[j])]
assert len(pairs)==3
for c,expected in [(F(0),F(10,9)),(F(1,48),F(4,3)),(F(1),F(106,9))]:
    gram=[[sum(F(6*(i==j)-1,9)+c*F(16,3)
               for face in faces if set(e+f)<=set(face))
           for j,f in enumerate(edges)] for i,e in enumerate(edges)]
    for parity,weights in [(1,(1,-1,0)),(1,(1,1,-2)),
                           (-1,(1,0,0)),(-1,(0,1,0)),(-1,(0,0,1))]:
        x=[0]*6
        for (i,j),v in zip(pairs,weights):
            x[i],x[j]=v,parity*v
        rate=F(4,3) if parity==1 else expected
        assert [sum(a*b for a,b in zip(row,x)) for row in gram]==[rate*v for v in x]
assert F(4,3)/F(106,9)==F(6,53)
print('PASS_EXACT · nine local mass and curl entries, Stokes coefficient, five sector modes at three action weights')
