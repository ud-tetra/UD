#!/usr/bin/env python3
"""Exact rational audit of the native tetrahedron generator and sign freedom."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), Q(0)) for col in bt] for row in a]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def negative(a):
    return [[-v for v in row] for row in a]


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def zero(n, m):
    return [[Q(0) for _ in range(m)] for _ in range(n)]


def matvec(a, v):
    return [sum((x*y for x, y in zip(row, v)), Q(0)) for row in a]


def main():
    simplices = [simplex for k in range(1, 5)
                 for simplex in combinations(range(4), k)]
    assert [sum(len(s) == k for s in simplices) for k in range(1, 5)] == [4, 6, 4, 1]
    loc = {simplex: i for i, simplex in enumerate(simplices)}
    n = len(simplices)
    b = zero(n, n)
    for simplex in simplices:
        if len(simplex) == 1:
            continue
        j = loc[simplex]
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k+1:]
            b[loc[face]][j] = Q((-1)**k)
    assert multiply(b, b) == zero(n, n)
    bt = transpose(b)
    a = add(bt, negative(b))
    lap = add(multiply(bt, b), multiply(b, bt))
    assert add(multiply(a, a), lap) == zero(n, n)

    h = [Q(1, 2) if i < 4 else Q(0) for i in range(n)]
    assert matvec(a, h) == [Q(0)]*n
    p = [[h[i]*h[j] for j in range(n)] for i in range(n)]
    assert multiply(p, p) == p
    assert multiply(a, p) == zero(n, n) == multiply(p, a)

    metric_plus = identity(n)
    metric_minus = add(identity(n), [[-2*v for v in row] for row in p])
    for metric in (metric_plus, metric_minus):
        assert add(multiply(transpose(a), metric), multiply(metric, a)) == zero(n, n)

    # S4-invariant 1+3 vertex decomposition: H columns are orthonormal.
    patterns = ((1, 1, 1, 1), (1, 1, -1, -1),
                (1, -1, 1, -1), (1, -1, -1, 1))
    frame = [[Q(patterns[j][i], 2) for j in range(4)] for i in range(4)]
    assert multiply(transpose(frame), frame) == identity(4)
    vertex = [row[:4] for row in metric_minus[:4]]
    for perm in permutations(range(4)):
        r = [[Q(int(i == perm[j])) for j in range(4)] for i in range(4)]
        assert multiply(multiply(transpose(r), vertex), r) == vertex
    assert multiply(multiply(transpose(frame), vertex), frame) == [
        [Q(-1), Q(0), Q(0), Q(0)],
        [Q(0), Q(1), Q(0), Q(0)],
        [Q(0), Q(0), Q(1), Q(0)],
        [Q(0), Q(0), Q(0), Q(1)],
    ]

    l0 = [row[:4] for row in lap[:4]]
    assert l0 == [[Q(4*int(i == j)-1) for j in range(4)] for i in range(4)]
    assert matvec(l0, [Q(1)]*4) == [Q(0)]*4
    for v in patterns[1:]:
        assert matvec(l0, [Q(x) for x in v]) == [Q(4*x) for x in v]
    # Projection from the full first-order flow obeys x''=-L0 x.
    assert [row[4:] for row in lap[:4]] == zero(4, n-4)

    out = {
        'status':'PASS',
        'carrier':'one oriented filled tetrahedron, C0+C1+C2+C3, dimensions 4+6+4+1',
        'boundary_squared_zero':True,
        'generator':'A=B^T-B; A^2=-L',
        'uniform_vertex_mode':'A h=0',
        'preserved_positive_form':'I15',
        'preserved_indefinite_form':'I15-2 h h^T; inertia (1 negative, 14 positive)',
        'vertex_form':'I4-(1/2) J4; rational orthonormal frame gives diag(-1,+1,+1,+1)',
        'vertex_laplacian':'4 I4-J4; spectrum 0,4,4,4',
        'spatial_continuum_or_physical_metric':'NOT_DERIVED',
        'physical_promotion':0,
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
