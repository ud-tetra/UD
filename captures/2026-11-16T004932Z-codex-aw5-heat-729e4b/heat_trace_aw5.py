"""Exact AW5 face heat-trace identities and a 2-to-3 control (SymPy)."""
from collections import Counter
from itertools import combinations

from sympy import Matrix, exp, factor, series, symbols, zeros

HUB = (0, 1, 2, 3)
LEAVES = [tuple(v for v in HUB if v != i)+(4+i,) for i in HUB]


def face_laplacian(cells):
    simplices = [sorted({s for tet in cells for s in combinations(tet, size)})
                 for size in range(1, 5)]
    boundaries = []
    for lower, upper in zip(simplices[1:], simplices[2:]):
        indices = {s: i for i, s in enumerate(lower)}
        matrix = zeros(len(lower), len(upper))
        for j, s in enumerate(upper):
            for k in range(len(s)):
                matrix[indices[s[:k]+s[k+1:]], j] = (-1)**k
        boundaries.append(matrix)
    B2, B3 = boundaries
    assert B2*B3 == zeros(B2.rows, B3.cols)
    return simplices, B2, B3, B2.T*B2+B3*B3.T


def boundary(cells):
    occurrence = Counter(s for tet in cells for s in combinations(tet, 3))
    assert max(occurrence.values()) <= 2
    return {face for face, count in occurrence.items() if count == 1}


filled = [HUB]+LEAVES
hollow = LEAVES
old_ball = [HUB, LEAVES[0]]
new_ball = [(0, *edge, 4) for edge in combinations((1, 2, 3), 2)]
flipped = LEAVES[1:]+new_ball
assert all(not {0, 4}.issubset(tet) for tet in filled)
assert boundary(old_ball) == boundary(new_ball)
assert boundary(filled) == boundary(flipped)

_, B2f, B3f, Lf = face_laplacian(filled)
_, B2h, B3h, Lh = face_laplacian(hollow)
assert B2f == B2h
assert (B3f.T*B3f).eigenvals() == {2: 1, 4: 3, 6: 1}
assert B3h.T*B3h == 4*Matrix.eye(4)
t, x = symbols("t x")
delta = (1+4*exp(-4*t))-(exp(-2*t)+3*exp(-4*t)+exp(-6*t))
assert (delta-(1-exp(-2*t))*(1+exp(-4*t))).expand() == 0
assert series(delta, t, 0, 3).removeO() == 4*t-12*t**2
assert Lf.trace()-Lh.trace() == 4

for name, cells, b2, trace in (("filled",filled,0,68), ("hollow",hollow,1,64),
                               ("flipped",flipped,0,78)):
    basis, _, _, L = face_laplacian(cells)
    assert L.rows-L.rank() == b2 and L.trace() == trace
    print(name, tuple(map(len,basis)), "b2=", b2, "trace=", trace)
    print(factor(L.charpoly(x).as_expr()))
print("PASS: common boundary and zero long-time face trace difference for 2-to-3")
