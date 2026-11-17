from fractions import Fraction as F
from itertools import combinations

edges = list(combinations(range(4), 2))
faces = list(combinations(range(4), 3))
adjacent = [[int(len(set(e) & set(f)) == 1) for f in edges] for e in edges]
face_rows = [[int(set(e) <= set(face)) for e in edges] for face in faces]
b2t = [[sum((-1)**i for i in range(3) if face[:i]+face[i+1:] == e)
        for e in edges] for face in faces]
b1 = [[int(j == v)-int(i == v) for i,j in edges] for v in range(4)]
pairs = [(i,j) for i,j in combinations(range(6),2)
         if not set(edges[i]) & set(edges[j])]
assert len(pairs) == 3

def gram(rows):
    return [[sum(a*b for a,b in zip(x,y)) for y in zip(*rows)] for x in zip(*rows)]

def apply(matrix,x):
    return [sum(a*b for a,b in zip(row,x)) for row in matrix]

unsigned, cut, cycle = map(gram, (face_rows,b1,b2t))
for i in range(6):
    for j in range(6):
        assert unsigned[i][j] == 2*(i==j)+adjacent[i][j]
        assert cut[i][j]+cycle[i][j] == 4*(i==j)
assert sum(cut[i][i] for i in range(6)) == sum(cycle[i][i] for i in range(6)) == 12
assert all(v == 0 for row in cut for v in apply(cycle,row))

def modes(weights,parity):
    vector = [0]*6
    for (i,j),q in zip(pairs,weights):
        vector[i],vector[j] = q,parity*q
    return vector

even = [modes(w,1) for w in [(1,-1,0),(1,1,-2)]]
odd = [modes(w,-1) for w in [(1,0,0),(0,1,0),(0,0,1)]]
for basis,eigen in [(even,-2),(odd,0)]:
    for x in basis:
        assert apply(adjacent,x) == [eigen*a for a in x]
        for u,v in [(F(1),F(0)),(F(1),F(1,2)),(F(1),F(-1,4))]:
            gem = [[2*u*(i==j)+v*adjacent[i][j] for j in range(6)] for i in range(6)]
            assert apply(gem,x) == [(2*u+v*eigen)*a for a in x]
print('PASS_EXACT · three flag metrics on five shear modes; unsigned coherent face spectrum; signed cut/cycle and joint Grams')
