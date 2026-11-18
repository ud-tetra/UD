"""Exact tests for gradient isolation on the regular tetrahedron."""
from itertools import combinations, product

vertices = range(4)
edges = tuple(combinations(vertices, 2))


def grad(p):
    return tuple(p[j] - p[i] for i, j in edges)


def boundary(h):
    return tuple(sum(a * (int(k == j) - int(k == i))
                     for a, (i, j) in zip(h, edges)) for k in vertices)


def scale(left, right):
    return tuple(a * b for a, b in zip(left, right))


zero = (0, 0, 0, 0)
basis = tuple(tuple(int(i == j) for i in vertices) for j in vertices)
potentials = tuple(product((-1, 0, 1), repeat=4)) + ((-3, -1, 1, 3),)
for mask in product((0, 1), repeat=6):
    columns = tuple(boundary(scale(mask, grad(p))) for p in basis)
    assert (all(column == zero for column in columns)) == (not any(mask))
    for a, (i, j) in zip(mask, edges):
        assert columns[i][j] == columns[j][i] == -a
    for p in potentials:
        gated_gradient = scale(mask, grad(p))
        assert (boundary(gated_gradient) == zero) == (not any(gated_gradient))
    assert (boundary(scale(mask, grad(potentials[-1]))) == zero) == (not any(mask))

for p in potentials:
    h = grad(p)
    left, right = boundary(h), boundary(tuple(-t for t in h))
    assert tuple(a + b for a, b in zip(left, right)) == zero
    # K K^T = 2 B B^T. Apply it to the centered input scaled by four.
    centered4 = tuple(4*t - sum(p) for t in p)
    assert tuple(2*t for t in boundary(grad(centered4))) == tuple(8*t for t in centered4)
print("64 masks and 5248 pointwise potential controls passed.")
print("82 stationary and live two-copy sector controls passed.")
