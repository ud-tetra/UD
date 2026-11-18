"""Exact tests of one-face stock, alignment and mixed-sector ambiguity."""
from fractions import Fraction as F
from itertools import combinations, product

edges = tuple(combinations(range(4), 2))
grid = tuple(product((-1, 0, 1), repeat=3))


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def lift(face_ids, values, sign):
    result = [0] * 6
    for i, value in zip(face_ids, values):
        result[i], result[5-i] = value, sign*value
    return tuple(result)


seam_cases = 0
supplement_cases = 0
for face in combinations(range(4), 3):
    ids = tuple(i for i, e in enumerate(edges) if set(e) <= set(face))
    assert {min(i, 5-i) for i in ids} == {0, 1, 2}
    apex = next(i for i in range(4) if i not in face)
    p = tuple(-3 if i == apex else 1 for i in range(4))
    g = tuple(p[j]-p[i] for i, j in edges)
    assert any(g) and not any(g[i] for i in ids)
    for u, v in product(grid, repeat=2):
        s, d = lift(ids, u, -1), lift(ids, v, -1)
        assert dot(s, s) == 2*dot(u, u) and dot(s, d) == 2*dot(u, v)
        minors = sum((u[i]*v[j]-u[j]*v[i])**2 for i,j in combinations(range(3), 2))
        assert dot(s,s)*dot(d,d)-dot(s,d)**2 == 4*minors
        seam_cases += 1
    for u in grid:
        mixtures = [(i, j, -i-j) for i, j in product((-1, 0, 1), repeat=2)]
        for w in mixtures:
            x = tuple(a+b for a,b in zip(lift(ids,u,-1), lift(ids,w,1)))
            for extra in combinations((5-i for i in ids), 2):
                observed = {i: x[i] for i in (*ids, *extra)}
                missing = next(i for i in range(6) if i not in observed)
                observed[missing] = -sum(observed.values())
                assert tuple(observed[i] for i in range(6)) == x
                supplement_cases += 1
    s = lift(ids, (1,-1,0), -1)
    e = lift(ids, (-1,1,0), 1)
    d = lift(ids, (1,1,1), -1)
    assert all(s[i]+e[i] == 0 for i in ids)
    assert dot(s,d) == 0 and dot(s,s) < dot(d,d)
    assert F(dot(s,s), dot(s,s)+dot(d,d)) == F(2,5)
print(f"{seam_cases} exact face Gram checks and {supplement_cases} exact recovery checks passed.")
print("4 signed-gradient blind witnesses and 4 mixed-sector false-completion witnesses passed.")
