#!/usr/bin/env python3
"""Exact standard-library verifier for THM-534-R1/R2; development capture v0.1."""
from fractions import Fraction as Q

N = 6
opposite = [(0, 1), (2, 3), (4, 5)]
cross_matchings = [
    [(0, 2), (1, 4), (3, 5)],
    [(0, 3), (1, 5), (2, 4)],
    [(0, 4), (1, 3), (2, 5)],
    [(0, 5), (1, 2), (3, 4)],
]
def permutation(matching):
    p = list(range(N))
    for a, b in matching:
        p[a], p[b] = b, a
    return p

P = [list(range(N)), permutation(opposite)] + [permutation(m) for m in cross_matchings]
weights = [Q(1, 2), Q(1, 6)] + [Q(1, 12)] * 4
T = [[Q(0) for _ in range(N)] for _ in range(N)]
for w, p in zip(weights, P):
    for i, j in enumerate(p):
        T[i][j] += w

opp = {tuple(sorted(edge)) for edge in opposite}
assert sum(weights) == 1
assert all(sum(row) == 1 for row in T)
assert all(sum(T[i][j] for i in range(N)) == 1 for j in range(N))
assert all(T[i][j] == T[j][i] for i in range(N) for j in range(N))
for i in range(N):
    for j in range(N):
        expected = Q(1, 2) if i == j else Q(1, 6) if tuple(sorted((i, j))) in opp else Q(1, 12)
        assert T[i][j] == expected
assert all(p[p[i]] == i for p in P for i in range(N))
assert all(sum(T[i][k] * T[k][i] for k in range(N)) == Q(11, 36) for i in range(N))

# Exact eigenvector verification (three antisymmetric, one constant,
# two independent symmetric zero-sum pair vectors).
def apply(v):
    return [sum(T[i][j] * v[j] for j in range(N)) for i in range(N)]
vecs = [
    ([1, 1, 1, 1, 1, 1], Q(1)),
    ([1, 1, -1, -1, 0, 0], Q(1, 2)),
    ([1, 1, 0, 0, -1, -1], Q(1, 2)),
    ([1, -1, 0, 0, 0, 0], Q(1, 3)),
    ([0, 0, 1, -1, 0, 0], Q(1, 3)),
    ([0, 0, 0, 0, 1, -1], Q(1, 3)),
]
for v, lam in vecs:
    assert apply(v) == [lam * x for x in v]
print("PASS: THM-534-R1 exact spectrum 1,1/2×2,1/3×3")
print("PASS: THM-534-R2 iid two-step return 11/36; quenched involution return 1")
print("Physical promotion: 0; source derivation of weights: OPEN")
