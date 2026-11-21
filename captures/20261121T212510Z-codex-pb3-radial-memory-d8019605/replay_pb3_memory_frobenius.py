#!/usr/bin/env python3
"""Exact PB3 compressed dark-space check and diagnostic Frobenius samples."""

from itertools import combinations

import numpy as np
from scipy.linalg import expm, null_space
from sympy import Matrix, Rational, eye, factor, symbols, zeros


def main():
    cells = [tuple(sorted((i, (i+1) % 3, 3, 4))) for i in range(3)]
    simplices = [part for degree in range(1, 5)
                 for part in sorted({s for cell in cells for s in combinations(cell, degree)})]
    assert len(simplices) == 27
    identity = eye(27)
    index = {simplex: i for i, simplex in enumerate(simplices)}
    boundary = zeros(27)
    for simplex, column in index.items():
        if len(simplex) > 1:
            for k in range(len(simplex)):
                boundary[index[simplex[:k] + simplex[k+1:]], column] = (-1)**k
    assert boundary**2 == zeros(27)
    generator = boundary - boundary.T
    averages = Matrix([[int(len(s) == 1 and s[0] in cell) for cell in cells] for s in simplices])
    gram = averages.T * averages
    assert gram.rank() == 3
    complement = identity - averages * gram.inv() * averages.T
    skew = complement * generator * complement
    drive = complement * generator * averages

    radial = [(3, 4)] + [(i, pole) for i in range(3) for pole in (3, 4)]
    selector = identity[[index[s] for s in radial], :]
    damping = selector.T * selector
    assert damping**2 == damping and damping.rank() == 7
    assert damping * averages == zeros(27, 3)

    rows = selector.col_join(averages.T)
    ranks = []
    for _ in range(4):
        rows = rows[list(rows.T.rref()[1]), :]
        ranks.append(rows.rows)
        rows = rows.col_join(rows * skew)
    assert ranks == [10, 17, 19, 19]
    dark = Matrix.hstack(*rows.nullspace())
    assert dark.cols == 8 and dark.T * drive == zeros(8, 3)
    dark_generator = (dark.T * dark).inv() * dark.T * skew * dark
    assert skew * dark == dark * dark_generator
    z = symbols('z')
    assert factor(dark_generator.charpoly(z).as_expr()) == (z*z+2)**2*(z*z+5)**2

    initial_in_cell_basis = -gram.inv() * drive.T * drive
    assert (initial_in_cell_basis**2).trace() == Rational(1251, 25)
    print(f'Observation ranks {ranks}; dark dimension 8; exact dark input rank 0.')
    print(f'Initial squared Frobenius norm: {(initial_in_cell_basis**2).trace()}.')
    print('Time      gamma=0         gamma=1')
    q = null_space(np.asarray(averages.T, dtype=float))
    cholesky = np.linalg.cholesky(np.asarray(gram, dtype=float))
    f = q.T @ np.asarray(drive, dtype=float) @ np.linalg.inv(cholesky.T)
    operators = [q.T @ np.asarray(skew - g*damping, dtype=float) @ q for g in (0, 1)]
    for t in (0, 5, 10, 20, 40, 80):
        norms = [np.linalg.norm(f.T @ expm(t * operator) @ f, ord='fro') for operator in operators]
        print(f'{t:>4}   {norms[0]:.9e}     {norms[1]:.9e}')


if __name__ == '__main__':
    main()
