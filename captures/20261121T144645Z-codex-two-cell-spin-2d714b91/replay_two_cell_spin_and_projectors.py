#!/usr/bin/env python3
"""Exact shared-face spin transition and simplicial projector replay."""

from fractions import Fraction
from itertools import combinations, product

LEFT = (0, 1, 2, 3)
RIGHT = (0, 1, 2, 4)
FACE = (0, 1, 2)
IDENTITY = (2, 0, 0, 0)
CENTER = (-2, 0, 0, 0)


def multiply_spin(left, right):
    # Store twice each quaternion to keep the finite group arithmetic integral.
    a, b, c, d = left
    e, f, g, h = right
    numerators = (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
                  a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)
    assert all(value % 2 == 0 for value in numerators)
    return tuple(value // 2 for value in numerators)


def inverse_spin(q):
    return (q[0], *(-value for value in q[1:]))


def boundary(simplex):
    return {simplex[:i] + simplex[i+1:]: (-1)**i for i in range(len(simplex))}


def check_spin():
    assert {face: n - boundary(RIGHT).get(face, 0)
            for face, n in boundary(LEFT).items()}[FACE] == 0
    units = [tuple(sign*2 if i == axis else 0 for i in range(4))
             for axis in range(4) for sign in (-1, 1)]
    units.extend(product((-1, 1), repeat=4))
    assert len(set(units)) == 24
    for transition, left_frame, right_frame in product(units, repeat=3):
        # A sign-bearing path crosses once. A round trip crosses in both directions.
        round_trip = multiply_spin(inverse_spin(transition), transition)
        assert round_trip == IDENTITY
        with_history = multiply_spin(transition, CENTER)
        assert with_history == tuple(-value for value in transition)
        changed = multiply_spin(right_frame,
                                multiply_spin(transition, inverse_spin(left_frame)))
        changed_history = multiply_spin(right_frame,
                                        multiply_spin(with_history, inverse_spin(left_frame)))
        assert changed_history == multiply_spin(changed, CENTER)
        assert multiply_spin(inverse_spin(transition), with_history) == CENTER
    print("Spin transition gauge and closed-path checks: 13,824 frame triples passed.")


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def multiply(left, right):
    columns = transpose(right)
    return [[sum(a*b for a, b in zip(row, col)) for col in columns] for row in left]


def reduce_rows(matrix):
    result = [list(map(Fraction, row)) for row in matrix]
    pivots = []
    for col in range(len(result[0])):
        row = len(pivots)
        pivot = next((i for i in range(row, len(result)) if result[i][col]), None)
        if pivot is None:
            continue
        result[row], result[pivot] = result[pivot], result[row]
        result[row] = [value / result[row][col] for value in result[row]]
        for i, current in enumerate(result):
            if i != row and current[col]:
                result[i] = [a-current[col]*b for a, b in zip(current, result[row])]
        pivots.append(col)
    return result, pivots


def image_projector(matrix):
    _, pivots = reduce_rows(matrix)
    columns = [[row[i] for i in pivots] for row in matrix]
    adjoint = transpose(columns)
    gram = multiply(adjoint, columns)
    rank = len(pivots)
    identity = [[int(i == j) for j in range(rank)] for i in range(rank)]
    reduced, _ = reduce_rows([a+b for a, b in zip(gram, identity)])
    assert [row[:rank] for row in reduced] == identity
    inverse = [row[rank:] for row in reduced]
    return multiply(multiply(columns, inverse), adjoint), rank


def incidence(edges, faces, signed=False):
    columns = []
    for face in faces:
        incidences = boundary(face)
        columns.append([incidences.get(edge, 0) if signed else int(edge in incidences)
                        for edge in edges])
    return transpose(columns)


def check_projectors():
    left_edges = list(combinations(LEFT, 2))
    left_faces = list(combinations(LEFT, 3))
    edges = sorted(set(left_edges) | set(combinations(RIGHT, 2)))
    faces = sorted(set(left_faces) | set(combinations(RIGHT, 3)))
    single = incidence(left_edges, left_faces)
    assert multiply(transpose(single), single) == [
        [1+2*(i == j) for j in range(4)] for i in range(4)
    ]
    scaled_gram = [[Fraction(value, 3) for value in row]
                   for row in multiply(single, transpose(single))]
    assert multiply(scaled_gram, scaled_gram) != scaled_gram

    fixtures = [
        ("single unsigned", single, 4),
        ("two cells, unique unsigned", incidence(edges, faces), 7),
        ("two cells, copied unsigned", incidence(edges, [*faces, FACE]), 7),
        ("two cells, signed", incidence(edges, faces, signed=True), 5),
    ]
    projectors = []
    for name, matrix, expected_rank in fixtures:
        projector, rank = image_projector(matrix)
        assert projector == transpose(projector)
        assert multiply(projector, projector) == projector
        assert multiply(projector, matrix) == matrix
        diagonal = [row[i] for i, row in enumerate(projector)]
        assert sum(diagonal) == rank == expected_rank
        if matrix is single:
            assert diagonal == [Fraction(2, 3)]*6
        projectors.append(projector)
        print(f"{name}: projector rank {rank}, symmetric and idempotent.")
    assert projectors[1] == projectors[2]
    assert projectors[1] != projectors[3]


if __name__ == "__main__":
    check_spin()
    check_projectors()
