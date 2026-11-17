"""Exact signed incidence and unsigned face projection controls."""

from fractions import Fraction as Q
from itertools import combinations, product


def boundary(simplex):
    return {simplex[:i] + simplex[i+1:]: (-1)**i for i in range(len(simplex))}


def replay():
    tetra = tuple(range(4))
    faces = tuple(combinations(tetra, 3))
    edges = tuple(combinations(tetra, 2))
    signs = boundary(tetra)
    assert all(sum(signs[f]*boundary(f).get(e, 0) for f in faces) == 0 for e in edges)

    for left, right in product(faces, repeat=2):
        assert len(set(combinations(left, 2)) & set(combinations(right, 2))) == 1 + 2*(left == right)

    zero = tuple(Q(0) for _ in edges)
    tested = 0
    for free in product((-1, 0, 1), repeat=5):
        edge_data = dict(zip(edges, (*free, -sum(free))))
        face_data = {f: sum(edge_data[e] for e in combinations(f, 2)) for f in faces}
        mean = Q(sum(face_data.values()), 4)
        bulk_pullback = tuple(sum(mean for f in faces if set(e) <= set(f)) for e in edges)
        assert bulk_pullback == zero
        correction = tuple(Q(sum(face_data[f]-mean for f in faces if set(e) <= set(f)), 2)
                           for e in edges)
        expected = tuple(Q(edge_data[e]-edge_data[tuple(v for v in tetra if v not in e)], 2)
                         for e in edges)
        assert correction == expected
        tested += 1
    assert tested == 243
    print("Signed boundary-of-boundary, 16 face Gram entries, and 243 exact pullbacks passed.")


if __name__ == "__main__":
    replay()
