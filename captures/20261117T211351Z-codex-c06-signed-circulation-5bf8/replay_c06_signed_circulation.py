"""Exact signed circulation and reciprocal hold controls."""
from collections import Counter
from itertools import combinations, product


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def apply(matrix, x):
    return tuple(dot(row, x) for row in matrix)


def det3(rows):
    a, b, c = rows
    return (a[0] * (b[1]*c[2] - b[2]*c[1])
            - a[1] * (b[0]*c[2] - b[2]*c[0])
            + a[2] * (b[0]*c[1] - b[1]*c[0]))


edges = tuple(combinations(range(4), 2))
faces = tuple(combinations(range(4), 3))
circulation = tuple(tuple(
    int(e == (i, j)) + int(e == (j, k)) - int(e == (i, k))
    for e in edges) for i, j, k in faces)
odd = tuple(tuple(int(i == j) - int(i == 5-j) for i in range(6))
            for j in range(3))
even = tuple(tuple(int(i == j) + int(i == 5-j) - int(i in (2, 3))
                   for i in range(6)) for j in range(2))
blind = (1, 1, 0, 0, -1, -1)
assert apply(circulation, blind) == (0, 0, 0, 0)
assert apply(circulation, even[0]) == (0, 2, 2, 0)

ranks = Counter()
for signs in product((-1, 1), repeat=6):
    signed = tuple(tuple(a*s for a, s in zip(row, signs))
                   for row in circulation)
    restricted = tuple(tuple(dot(row, x) for x in odd) for row in signed)
    assert any(any(apply(signed, x)) for x in even)
    if any(det3(rows) for rows in combinations(restricted, 3)):
        ranks[3] += 1
    else:
        assert any(a[i]*b[j] != a[j]*b[i]
                   for a, b in combinations(restricted, 2)
                   for i, j in combinations(range(3), 2))
        ranks[2] += 1
assert ranks == {2: 48, 3: 16}, ranks

# Coordinates are orthonormal and ordered (E:2, T2:3) on each port.
# G=diag(2,3,5,7,11) before cut and diag(2,3,0,0,0) after cut.
hold = (2, 3, 0, 0, 0)
for x, y in product(product((-1, 0, 1), repeat=5), repeat=2):
    dx = tuple(-g * v for g, v in zip(hold, y))
    dy = tuple(g * u for g, u in zip(hold, x))
    assert dot(x, dx) + dot(y, dy) == 0
    assert dx[2:] == dy[2:] == (0, 0, 0)
print('Signed edge gauges: 64 exact controls. Odd ranks: 48 rank-2, 16 rank-3.')
print('Even leakage: all 64. Canonical blind witness and explicit even leakage verified.')
print('Reciprocal hybrid hold: 59049 integer state controls.')
