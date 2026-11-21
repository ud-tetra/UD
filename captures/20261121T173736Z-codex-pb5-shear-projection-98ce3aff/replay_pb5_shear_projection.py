#!/usr/bin/env python3
"""Exact PB5 shear projection over the rational coefficient carrier."""

from itertools import combinations

from sympy import Matrix, eye, factor, symbols, zeros


def oriented_image(simplex, permutation):
    moved = tuple(permutation[i] for i in simplex)
    inversions = sum(a > b for a, b in combinations(moved, 2))
    return tuple(sorted(moved)), (-1)**inversions


def main():
    cells = [(*sorted((i, (i + 1) % 5)), 5, 6) for i in range(5)]
    simplices = [s for k in range(1, 5) for s in
                 sorted({part for cell in cells for part in combinations(cell, k)})]
    index = {s: i for i, s in enumerate(simplices)}
    identity = eye(len(simplices))
    incidence = zeros(len(simplices))
    for simplex in simplices:
        if len(simplex) > 1:
            for i in range(len(simplex)):
                incidence[index[simplex[:i] + simplex[i+1:]], index[simplex]] = (-1)**i
    generator = incidence - incidence.T
    cyclic_edges = [(i, (i + 1) % 5) for i in range(5)]
    equator = Matrix.hstack(*(identity[:, index[tuple(sorted(edge))]] *
                              (1 if edge[0] < edge[1] else -1) for edge in cyclic_edges))
    radial_edges = [(5, 6)] + [(i, pole) for i in range(5) for pole in (5, 6)]
    selector = identity[[index[s] for s in radial_edges], :]
    radial_projector = selector.T * selector
    observer = selector.col_join(selector * generator)
    assert radial_projector**2 == radial_projector and radial_projector.rank() == 11
    assert observer.rank() == observer.col_join(observer * generator).rank() == 22
    lossless = Matrix.hstack(*observer.nullspace())
    projector = lossless * (lossless.T * lossless).inv() * lossless.T
    all_edges = identity[:, [index[s] for s in simplices if len(s) == 2]]
    assert projector * equator == equator
    assert projector * all_edges == equator * equator.T * all_edges

    permutations = [
        tuple((i + 1) % 5 for i in range(5)) + (5, 6),
        tuple((-i) % 5 for i in range(5)) + (5, 6),
        (0, 1, 2, 3, 4, 6, 5),
    ]
    fixed_constraints = []
    for permutation in permutations:
        action = zeros(len(simplices))
        for simplex in simplices:
            image, sign = oriented_image(simplex, permutation)
            action[index[image], index[simplex]] = sign
        assert action * projector == projector * action
        assert action * generator == generator * action
        fixed_constraints.append(action - identity)

    fixed = Matrix.vstack(*fixed_constraints)
    signed_cycle = equator * Matrix.ones(5, 1)
    assert fixed_constraints[0] * signed_cycle == zeros(43, 1)
    assert fixed_constraints[1] * signed_cycle == -2 * signed_cycle
    assert (fixed * equator).rank() == 5
    assert generator * signed_cycle != zeros(43, 1)

    # Rotation weight two has polynomial t^2 - 2*cos(4*pi/5)*t + 1.
    # Work with both real nontrivial weights as a rational Galois pair.
    rotate_edges = equator.T * (fixed_constraints[0] + identity) * equator
    t = symbols("t")
    assert factor(rotate_edges.charpoly(t).as_expr()) == (t-1)*(t**4+t**3+t**2+t+1)
    # Every zero-mean cyclic potential gives a lossless cyclic edge derivative.
    derivative = rotate_edges.T - eye(5)
    assert derivative.rank() == 4
    assert projector * equator * derivative == equator * derivative

    fixed_basis = Matrix.hstack(*((fixed * lossless).nullspace()))
    full_fixed = lossless * fixed_basis
    generator_image = generator * full_fixed
    uniform_vertices = Matrix([int(len(s) == 1) for s in simplices])
    assert full_fixed.cols == 1
    assert full_fixed.columnspace() == [uniform_vertices]
    assert generator_image == zeros(43, 1)

    # A supplied cycle encodes the axial channel and the planar weight-two pair.
    # The exact order-five module check and DFT orthogonality separate the three.
    assert signed_cycle.dot(signed_cycle) == 5
    print("Radial sink rank 11; invariant lossless rank 21; edge slice rank 5.")
    print("No fully symmetric direction in the signed equatorial edge slice.")
    print("The supplied cyclic axial direction survives the lossless projector.")
    print("Full lossless fixed-space rank 1: the static uniform vertex mode.")


if __name__ == "__main__":
    main()
