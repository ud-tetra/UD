#!/usr/bin/env python3
"""Replay the PB5 sink replacement with exact rational SymPy arithmetic."""

from itertools import combinations

from sympy import Matrix, eye, factor, symbols, zeros


def image_projector(operator):
    _, pivots = operator.rref()
    basis = operator[:, list(pivots)]
    return basis * (basis.T * basis).inv() * basis.T


def observation(generator, sink):
    rows = sink.T
    previous_rank = -1
    while True:
        independent_rows = list(rows.T.rref()[1])
        rows = rows[independent_rows, :]
        if rows.rows == previous_rank:
            return rows
        previous_rank = rows.rows
        rows = rows.col_join(rows * generator)


def main():
    cells = [tuple(sorted((i, (i + 1) % 5, 5, 6))) for i in range(5)]
    by_degree = [sorted({s for cell in cells for s in combinations(cell, k)})
                 for k in range(1, 5)]
    assert list(map(len, by_degree)) == [7, 16, 15, 5]
    index = {s: i for i, s in enumerate(sum(by_degree, []))}
    size = len(index)
    identity = eye(size)
    boundary = zeros(size)
    for simplex, column in index.items():
        if len(simplex) > 1:
            for k in range(len(simplex)):
                boundary[index[simplex[:k] + simplex[k+1:]], column] = (-1)**k
    assert boundary**2 == zeros(size)
    generator = boundary - boundary.T

    radial = [(i, 5, 6) for i in range(5)]
    assert all(sum(set(face) <= set(cell) for cell in cells) == 2 for face in radial)
    restrictions = [identity[[index[edge] for edge in combinations(face, 2)], :]
                    for face in radial]
    trace = Matrix.vstack(*restrictions)
    injection = trace.T
    copied_injection = Matrix.hstack(injection, injection)
    projector = image_projector(injection)
    assert projector == image_projector(copied_injection)
    assert projector == projector.T == projector**2
    assert projector * injection == injection
    touched_edges = {edge for face in radial for edge in combinations(face, 2)}
    assert projector == Matrix.diag(*(int(s in touched_edges) for s in index))
    assert [injection.rank(), copied_injection.rank(), projector.rank()] == [11]*3

    signed_face = Matrix([1, -1, 1])
    whitney_mass = (6 * eye(3) - signed_face * signed_face.T) / 9
    assert whitney_mass.is_positive_definite
    loss = sum((2 * restriction.T * whitney_mass * restriction for restriction in restrictions),
               zeros(size))
    assert loss.rank() == 11 and projector * loss == loss

    stack = trace.col_join(trace * generator)
    stack_next = stack.col_join(trace * generator**2)
    assert [trace.rank(), stack.rank(), stack_next.rank()] == [11, 22, 22]
    sink_stack = projector.col_join(projector * generator)
    assert sink_stack.rref()[0][:22, :] == stack.rref()[0][:22, :]
    lossless = Matrix.hstack(*stack.nullspace())
    lossless_projector = identity - image_projector(stack.T)
    assert lossless_projector == lossless_projector.T == lossless_projector**2
    assert lossless_projector.rank() == lossless.cols == 21
    assert generator * lossless_projector == lossless_projector * generator
    assert projector * lossless_projector == loss * lossless_projector == zeros(size)
    reduced = (lossless.T * lossless).inv() * lossless.T * generator * lossless
    z = symbols("z")
    polynomial = factor(reduced.charpoly(z).as_expr())
    assert polynomial == z * (z**2 + 2)**2 * (z**4 + 9*z**2 + 19)**4

    # One unsigned incidence column per face sums three edges into one observation.
    summed = zeros(size, len(radial))
    for column, face in enumerate(radial):
        for edge in combinations(face, 2):
            summed[index[edge], column] = 1
    summed_projector = image_projector(summed)
    assert summed_projector.rank() == 5
    summed_dim = size - observation(generator, summed_projector).rows
    assert summed_dim != 21

    print("PB5 dimensions by degree: 7, 16, 15, 5")
    print("Radial trace projector: rank 11 with 15 or 30 flag columns")
    print("Observation stack ranks: 11, 22, 22")
    print(f"Lossless projector: rank 21; damped complement: rank 22; spectrum: {polynomial}")
    print(f"Unsigned face-sum control: sink rank 5; lossless rank {summed_dim}")


if __name__ == "__main__":
    main()
