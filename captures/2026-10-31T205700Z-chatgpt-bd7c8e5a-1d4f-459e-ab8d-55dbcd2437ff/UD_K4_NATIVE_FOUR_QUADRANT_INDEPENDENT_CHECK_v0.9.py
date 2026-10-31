#!/usr/bin/env python3
"""Independent arithmetic/control check: no symbolic algebra libraries.
Reference realization uses standard 3D signed coordinates, not the 4x4 Laplacian construction.
"""
from fractions import Fraction as F
from itertools import combinations,product
v=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
checks=0
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ok(statement):
 global checks
 assert statement
 checks+=1
for i in range(4):
 for j in range(4):ok(dot(v[i],v[j])==(3 if i==j else -1))
ok(tuple(sum(v[i][k] for i in range(4)) for k in range(3))==(0,0,0))
# Four faces; every tetra edge is in exactly two triangular faces.
faces=list(combinations(range(4),3))
edges=list(combinations(range(4),2))
for ed in edges:ok(sum(set(ed).issubset(set(f)) for f in faces)==2)
for mask in range(16):
 selected=[i for i in range(4) if (mask>>i)&1]
 # Pair of triangular faces i,j shares one edge; coefficients there cancel iff a_i=a_j.
 exposed=sum(((i in selected)!=(j in selected)) for i,j in combinations(range(4),2))
 ok((exposed==0)==(mask in (0,15)))
# The actual support atlas for rational Cartesian sample points.
for p in product(range(-2,3),repeat=3):
 lam=[F(1+dot(vi,p),4) for vi in v]
 ok(sum(lam)==1)
 ok(tuple(sum(lam[i]*v[i][j] for i in range(4)) for j in range(3))==p)
 i=lam.index(min(lam))
 t=[(lam[j]-lam[i],j) for j in range(4) if j!=i]
 ok(all(k>=0 for k,j in t))
 ok(tuple(sum(k*v[j][col] for k,j in t) for col in range(3))==p)
print('INDEPENDENT_FRACTION_CHECKS',checks)
print('CLOSED_MASKS', ['0000','1111'])
print('DIFFERENT_REALIZATION','3D signed tetrahedron with rational arithmetic')
