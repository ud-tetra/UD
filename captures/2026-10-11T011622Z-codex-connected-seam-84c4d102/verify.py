#!/usr/bin/env python3
"""Exact K4 finite phase-connection and distinct Theta-lift audit."""
import itertools
import json

V = tuple(range(4))
E = tuple(itertools.combinations(V, 2))
F = tuple(itertools.combinations(V, 3))
PAIRS = ((0, 5), (1, 4), (2, 3))
I2 = ((1, 0), (0, 1))
ROOT = (
    I2, ((0, -1), (1, 0)), ((-1, 0), (0, -1)),
    ((0, 1), (-1, 0)),
)


def tr(A):
    return tuple(zip(*A))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def phase(a, i, j):
    if i < j:
        return a[E.index((i, j))]
    return -a[E.index((j, i))]


def holonomy(a, face):
    i, j, k = face
    return (phase(a, i, j) + phase(a, j, k) + phase(a, k, i)) % 4


def affine(theta, perm, mask):
    return tuple(theta[perm[i]] ^ mask[i] for i in range(3))


def main():
    assert all(mul(tr(R), R) == I2 for R in ROOT)
    assert all(mul(ROOT[i], ROOT[(-i) % 4]) == I2 for i in range(4))
    seen_flat = set()
    total = flat = nonflat = 0
    holonomy_classes = set()
    for a in itertools.product(range(4), repeat=6):
        total += 1
        for k in a:
            assert mul(tr(ROOT[k]), ROOT[k]) == I2
        curv = tuple(holonomy(a, face) for face in F)
        if all(x == 0 for x in curv):
            flat += 1
            seen_flat.add(a)
        else:
            nonflat += 1
        holonomy_classes.add(curv)
        # In exact-isometry specialization, all six integrity gates pass;
        # fully retained closure receipts yield h=(1,...,1).
        assert all(mul(tr(ROOT[k]), ROOT[k]) == I2 for k in a)
    assert (total, flat, nonflat) == (4096, 64, 4032)
    pure_gauges = set()
    for v1, v2, v3 in itertools.product(range(4), repeat=3):
        p = (0, v1, v2, v3)
        pure_gauges.add(tuple((p[j] - p[i]) % 4 for i, j in E))
    assert pure_gauges == seen_flat and len(holonomy_classes) == 64
    assert (0,) * 6 in seen_flat
    # Nonflat holonomy remains fully unitary and integrity-passing.
    witness = (1, 0, 0, 0, 0, 0)
    assert tuple(holonomy(witness, face) for face in F) != (0,) * 4

    # The already sourced affine Theta lift acts on a separate eight-state
    # carrier. Its 48 matrices are permutations, hence always unitary.
    states = tuple(itertools.product((0, 1), repeat=3))
    lifts = []
    for perm, mask in itertools.product(itertools.permutations(range(3)),
                                        states):
        image = tuple(affine(theta, perm, mask) for theta in states)
        assert set(image) == set(states)
        lifts.append(image)
    assert len(lifts) == len(set(lifts)) == 48
    assert any(sum(affine(theta, (0, 1, 2), (1, 0, 0)))
                   != sum(theta) for theta in states)
    print(json.dumps({
        "status": "EXACT finite connection census; topological no-go proved separately",
        "carrier": "fully retained labeled K4; one complex Hermitian dimension per node; six oriented phase links",
        "phase_group_grid": "mu4^6",
        "phase_assignments": total,
        "flat_connections": flat,
        "nonflat_integrity_passing_connections": nonflat,
        "gauge_classes": len(holonomy_classes),
        "pure_gauge_flat_assignments": len(pure_gauges),
        "fixed_K4_null_all_identity": True,
        "distinct_affine_Theta_lifts": len(lifts),
        "independent_Theta_target_scored": False,
        "native_phase_generator_derived": False,
        "physical_promotion": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
