"""Exact incidence and coordinate controls for the tetrahedron."""

from fractions import Fraction as Q
from itertools import combinations, product


def replay():
    vertices = set(range(4))
    edges = tuple(combinations(range(4), 2))
    faces = tuple(combinations(range(4), 3))
    opposite = {edge: tuple(sorted(vertices - set(edge))) for edge in edges}

    checked = 0
    for free in product(range(-1, 2), repeat=5):
        for total in (0, 1):
            z = dict(zip(edges, (*free, total - sum(free))))
            face_sums = {face: sum(z[e] for e in combinations(face, 2)) for face in faces}
            for edge in edges:
                adjacent_sum = sum(value for face, value in face_sums.items() if set(edge) <= set(face))
                assert adjacent_sum == z[edge] - z[opposite[edge]] + total
                checked += 1
    assert checked == 2916

    z = {edge: 0 for edge in edges}
    z[(2, 3)], z[(0, 3)] = 1, -1
    assert sum(z.values()) == 0 and all(z[e] == 0 for e in combinations((0, 1, 2), 2))
    assert z[(0, 1)] - z[(2, 3)] == -1
    metric_mix = Q(47, 9)
    face_012 = sum(z[e] for e in combinations((0, 1, 2), 2))
    face_013 = sum(z[e] for e in combinations((0, 1, 3), 2))
    assert metric_mix * (face_012 - face_013) == Q(47, 9)
    print("2916 exact incidence checks passed. Single-face and dual-flag witnesses reproduced.")


if __name__ == "__main__":
    replay()
