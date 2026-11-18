"""Exact controls for C06 shared-vertex loading."""
from fractions import Fraction as F
from itertools import combinations, product


edges = tuple(combinations(range(4), 2))
grid = tuple(product((-1, 0, 1), repeat=3))


def grad(p):
    return tuple(p[j] - p[i] for i, j in edges)


def boundary(h):
    return tuple(sum(a * (int(k == j) - int(k == i))
                     for a, (i, j) in zip(h, edges)) for k in range(4))


def norm(x):
    return sum(a*a for a in x)


def scaled(w, a):
    return tuple(a*x for x in w)


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


# Rational endpoint coordinates are the actual archive (La,-La), represented
# here by scaled gradient coordinates; the common metric identity is homogeneous.
angles = ((1, 0), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (0, 1), (-1, 0))
for w in grid:
    p = (*w, -sum(w))
    h = grad(p)
    assert add(boundary(h), boundary(scaled(h, -1))) == (0, 0, 0, 0)
    for q in grid:
        vertex = (*q, -sum(q))
        common = grad(vertex)
        assert add(add(h, common), scaled(add(scaled(h, -1), common), -1)) == scaled(h, 2)
        # The loader outputs opposing gradients, so vertex derivative is untouched.
        assert boundary(add(add(common, h), add(common, scaled(h, -1)))) == boundary(scaled(common, 2))
    for cosine, sine in angles:
        donor_stock = 2*norm(scaled(h, cosine))
        archived_stock = norm(scaled(h, sine)) + norm(scaled(h, -sine))
        assert donor_stock + archived_stock == 2*norm(h)
        assert F(archived_stock, 2) == sine*sine*norm(h)
        if cosine == 0:
            assert donor_stock == 0
            assert F(archived_stock, 2) == norm(h)
print("729 exact common-channel and cancellation cases passed.")
print("135 exact rotation and stock-readback cases passed.")
