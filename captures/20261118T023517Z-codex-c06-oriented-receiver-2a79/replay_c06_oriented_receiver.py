"""Exact incidence, signed action and archive readback controls."""
from fractions import Fraction
from itertools import combinations, permutations, product

edges = tuple(combinations(range(4), 2))
states = tuple(product((-1, 0, 1), repeat=3))


def norm(x):
    return sum(a * a for a in x)


def endpoint(x, signed=False):
    return tuple(sum(val * (int(k == j) + (-1 if signed else 1) * int(k == i))
                     for val, (i, j) in zip(x, edges)) for k in range(4))


def gradient(v):
    return tuple(v[j] - v[i] for i, j in edges)


def action(x, p, signed=False):
    out = [0] * 6
    for val, (i, j) in zip(x, edges):
        a, b = p[i], p[j]
        out[edges.index(tuple(sorted((a, b))))] = -val if signed and a > b else val
    return tuple(out)


for w in states:
    x = (*w, *(-a for a in reversed(w)))
    r = gradient(endpoint(x))
    assert norm(r) == 8 * norm(x)
    assert endpoint(r, signed=True) == tuple(4*a for a in endpoint(x))
    assert bool(norm(endpoint(r, signed=True))) == bool(norm(x))
    for i, j, k in combinations(range(4), 3):
        assert r[edges.index((i, j))] + r[edges.index((j, k))] == r[edges.index((i, k))]
    # Archived h= L(sqrt(2)*x) = r/2. Readback contributes half its norm.
    archive = tuple(Fraction(t, 2) for t in r)
    assert norm(archive) / 2 == norm(x)
    divergence = endpoint(archive, signed=True)
    assert tuple((divergence[i] + divergence[j]) / 4 for i, j in edges) == x
    for p in permutations(range(4)):
        assert gradient(endpoint(action(x, p))) == action(r, p, signed=True)

p = (1, 0, 2, 3)
signed_trace = sum(action(tuple(int(i == j) for i in range(6)), p, signed=True)[j]
                   for j in range(6))
vertex_contrast_trace = sum(i == j for i, j in enumerate(p)) - 1
assert (signed_trace, vertex_contrast_trace, signed_trace - vertex_contrast_trace) == (0, 1, -1)
print("648 exact signed and unsigned intertwining checks passed.")
print("27 exact norm, half-readout and boundary controls passed. Transposition traces +1/-1 confirmed.")
