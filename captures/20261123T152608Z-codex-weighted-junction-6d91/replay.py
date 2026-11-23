"""Exact junction transfer and first-return replay. Requires SymPy."""
from collections import defaultdict
from itertools import combinations

from sympy import Rational, SparseMatrix, eye, zeros


def chain(terms):
    result = defaultdict(int)
    for simplex, coefficient in terms:
        inversions = sum(a > b for a, b in combinations(simplex, 2))
        result[tuple(sorted(simplex))] += (-1)**inversions * coefficient
    return {simplex: c for simplex, c in result.items() if c}


def boundary(vector):
    return chain(
        (simplex[:i] + simplex[i+1:], c * (-1)**i)
        for simplex, c in vector.items() if len(simplex) > 1
        for i in range(len(simplex))
    )


def cone(vertex, vector):
    return chain(((vertex,) + simplex, c) for simplex, c in vector.items())


def transfer(vector, columns):
    return chain(
        (target, c * d)
        for source, c in vector.items()
        for target, d in columns[source].items()
    )


def closure(cells):
    return sorted({
        s for cell in cells for size in range(1, len(cell)+1)
        for s in combinations(cell, size)
    }, key=lambda s: (len(s), s))


def boundary_matrix(simplices):
    index = {s: i for i, s in enumerate(simplices)}
    return SparseMatrix(len(index), len(index), {
        (index[t], j): value
        for j, s in enumerate(simplices)
        for t, value in boundary({s: 1}).items()
    })


def selector(a, b, pairs):
    scores = [a.get(edge, 0)**2 * b.get(opposite, 0)**2 for edge, opposite in pairs]
    winners = [pair for pair, score in zip(pairs, scores) if score == max(scores) > 0]
    return winners[0] if len(winners) == 1 else None


def main():
    xyz = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
    edges = list(combinations(range(4), 2))
    pairs = [(e, tuple(i for i in range(4) if i not in e)) for e in edges]
    for e, opposite in pairs:
        assert all(sum(xyz[i][j] for i in e) == -sum(xyz[i][j] for i in opposite)
                   for j in range(3))
    fixtures = [
        ({(0,1):1}, {(2,3):1}, pairs[0]),
        ({(0,2):1}, {(1,3):-1}, pairs[1]),
        ({(0,1):1,(0,2):1}, {(2,3):1,(1,3):1}, None),
        ({(0,1):1}, {(0,2):1}, None),
    ]
    for a, b, expected in fixtures:
        assert selector(a, b, pairs) == expected
        assert selector({e:-c for e,c in a.items()}, b, pairs) == expected
    print("TEST-PRE-AUTH-01: six midpoint contacts, four control outcomes PASS")

    cells = [tuple(range(4*p, 4*p+4)) for p in range(2)]
    source = closure(cells)
    columns = {}
    for p, vertices in enumerate(cells):
        columns.update({(v,): {(v,): 1} for v in vertices})
        for i, (u, v) in enumerate(combinations(vertices, 2)):
            m = 8 + (i if p == 0 else 5-i)
            columns[(u,v)] = chain([((u,m),1), ((m,v),1)])
        for i, face in enumerate(combinations(vertices, 3)):
            columns[face] = cone(14+4*p+i, transfer(boundary({face:1}), columns))
        columns[vertices] = cone(22+p, transfer(boundary({vertices:1}), columns))
    target = closure([s for cell in cells for s in columns[cell]])
    index = {s: i for i, s in enumerate(target)}
    weights = {}
    entries = {}
    for j, simplex in enumerate(source):
        column = columns[simplex]
        assert len(column) == (1, 2, 6, 24)[len(simplex)-1]
        for s, c in column.items():
            i = index[s]
            assert i not in weights
            weights[i] = Rational(1, len(column))
            entries[i, j] = c

    n, m = len(target), len(source)
    phi = SparseMatrix(n, m, entries)
    w = SparseMatrix(n, n, {(i,i):weights.get(i,1) for i in range(n)})
    b = boundary_matrix(target)
    assert b*b == zeros(n)
    assert b*phi == phi*boundary_matrix(source)
    assert phi.T*w*phi == eye(m)
    q = SparseMatrix(eye(n)) - phi*phi.T*w
    assert q*q == q and q.T*w == w*q
    a = b - w.inv()*b.T*w
    assert a.T*w + w*a == zeros(n)
    d = q*a*q
    assert d.T*w + w*d == zeros(n)
    g = q*a*phi
    assert phi.T*w*a*q == -g.T*w
    first_return = -g.T*w*g
    old_vertex = source.index((0,))
    assert first_return[old_vertex,old_vertex] < 0

    ranks = [b.extract([i for i,s in enumerate(target) if len(s)==size-1],
                       [i for i,s in enumerate(target) if len(s)==size]).rank()
             for size in (2,3,4)]
    counts = [sum(len(s)==size for s in target) for size in range(1,5)]
    betti = [counts[i] - ([0]+ranks)[i] - (ranks+[0])[i] for i in range(4)]
    assert betti == [1,5,0,0]
    print(f"Transfer: {m} source coordinates, {n} target coordinates, {n-m} transverse coordinates")
    print(f"Target counts: {counts}; Betti: {betti}")
    print(f"Weighted chain map, Gram, projections and skew-adjointness: PASS")
    print(f"First-return coefficient at old vertex 0: {first_return[old_vertex,old_vertex]}")


if __name__ == "__main__":
    main()
