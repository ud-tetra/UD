"""Rational control of the incomplete diagonal face correction."""
from fractions import Fraction as F
from itertools import combinations, product


def transpose(matrix):
    return tuple(zip(*matrix))


def matmul(left, right):
    return tuple(tuple(sum(a*b for a, b in zip(row, col))
                       for col in transpose(right)) for row in left)


def projection(n):
    return tuple(tuple(F(i == j) - F(1, n) for j in range(n)) for i in range(n))


def diagonal(entries):
    return tuple(tuple(value if i == j else 0 for j in range(len(entries)))
                 for i, value in enumerate(entries))


vertices = range(4)
edges = tuple(combinations(vertices, 2))
faces = tuple(combinations(vertices, 3))
h = tuple(tuple(int(set(edge) <= set(face)) for edge in edges) for face in faces)
hx = matmul(h, projection(6))
u = projection(4)
assert matmul(hx, transpose(hx)) == tuple(tuple(2*v for v in row) for row in u)
assert matmul(transpose(hx), hx) == tuple(
    tuple(int(i == j)-int(j == 5-i) for j in range(6)) for i in range(6))

spectra = [(0, 0, 0), (0, 0, F(3, 4)), (0, F(1, 2), 1), (F(1, 4), 1, 1), (1, 1, 1)]
for mask in product((0, 1), repeat=4):
    residual = matmul(matmul(u, diagonal(mask)), u)
    power = residual
    # The fourth eigenvalue is zero in the ambient face trace direction.
    for degree in range(1, 5):
        assert sum(power[i][i] for i in range(4)) == sum(
            lam**degree for lam in spectra[sum(mask)])
        power = matmul(power, residual)

residual = matmul(matmul(u, diagonal((1, 0, 0, 0))), u)
witness = (3, -1, -1, -1)
assert matmul(residual, tuple((x,) for x in witness)) == tuple(
    (F(3, 4)*x,) for x in witness)
# Constraints from the six face-coordinate difference vectors.
row_pairs = tuple(combinations(range(4), 2))
for i, j in row_pairs:
    d = tuple(int(k == i) - int(k == j) for k in range(4))
    assert matmul(u, tuple((x,) for x in d)) == tuple((x,) for x in d)
    assert tuple(x*x for x in d) == tuple(int(k in (i, j)) for k in range(4))
# The first three pair equations on faces 0, 1, 2 determine them;
# face 3 is then determined by the 0,3 equation.
target = F(2)
first = (target+target-target)/2
gains = (first, target-first, target-first, target-first)
assert gains == (1, 1, 1, 1)
assert all(gains[i]+gains[j] == 2 for i, j in row_pairs)
print("16 diagonal face masks: all five exact residual spectra passed.")
print("One-missing eigenvector and unique diagonal gain equations passed.")
