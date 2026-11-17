from fractions import Fraction as F
from itertools import combinations

def diagonal(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def multiply(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def combine(a,b,scale=1):
    return [[x+scale*y for x,y in zip(row_a,row_b)] for row_a,row_b in zip(a,b)]

def scale(a,factor):
    return [[factor*x for x in row] for row in a]

edges = list(combinations(range(4),2))
pairs = [(i,j) for i,j in combinations(range(6),2)
         if not set(edges[i]) & set(edges[j])]
assert len(pairs) == 3
I = diagonal(6)
P = [[F(0) for _ in edges] for _ in edges]
for i,j in pairs:
    for k,l in ((i,i),(i,j),(j,i),(j,j)):
        P[k][l] = F(1,2)
assert multiply(P,P) == P
odd = combine(I,P,-1)

# One orthonormal even and odd block has source, direct and (even only)
# matching ports. Integer unit rates suffice to check both Taylor series.
def record_taylor(g):
    n = len(g)
    assert combine(g,transpose(g)) == scale(g,0)
    initial = [[1]]+[[0] for _ in range(n-1)]
    derivative = multiply(g,initial)
    third = multiply(g,multiply(g,derivative))
    quadratic = sum(v[0]**2 for v in derivative[1:])
    quartic = sum(F(2,6)*a[0]*b[0] for a,b in zip(derivative[1:],third[1:]))
    return quadratic,quartic

even = record_taylor([[0,-1,-1],[1,0,0],[1,0,0]])
odd_taylor = record_taylor([[0,-1],[1,0]])
assert even == (2,F(-4,3)) and odd_taylor == (1,F(-1,3))
assert F(1,2)*even[1]-odd_taylor[1] == F(-1,3)
records = scale(combine(I,P),F(1,2))
assert combine(records,scale(odd,F(1,2))) == I
assert multiply(records,P) == P
assert multiply(records,odd) == scale(odd,F(1,2))
print('PASS_EXACT · projector, skew blocks, t^4 contrast -1/3, finite-stage isometry, record gains 2:1')
