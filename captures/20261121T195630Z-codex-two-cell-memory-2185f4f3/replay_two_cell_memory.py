#!/usr/bin/env python3
"""Exact projected-memory transfer functions on the 23-coordinate two-cell carrier."""

from itertools import combinations

from sympy import Matrix, eye, factor, symbols, zeros


def main():
    cells = [(0, 1, 2, 3), (0, 1, 2, 4)]
    simplices = [a for degree in range(1, 5)
                 for a in sorted({s for c in cells for s in combinations(c, degree)})]
    assert len(simplices) == 23
    index = {simplex: n for n, simplex in enumerate(simplices)}
    identity = eye(23)
    boundary = zeros(23)
    for simplex, column in index.items():
        if len(simplex) > 1:
            for i in range(len(simplex)):
                boundary[index[simplex[:i] + simplex[i+1:]], column] = (-1)**i
    assert boundary**2 == zeros(23)
    generator = boundary - boundary.T
    even = Matrix([2 if s in ((0,), (1,), (2,)) else int(s in ((3,), (4,)))
                   for s in simplices])
    odd = identity[:, index[(3,)]] - identity[:, index[(4,)]]
    modes = Matrix.hstack(even, odd)
    gram = modes.T * modes
    assert gram == Matrix.diag(14, 2)
    complement = identity - modes * gram.inv() * modes.T

    b = Matrix([1, -1, 1])
    metric = (6*eye(3) - b*b.T)/9
    losses = {}
    for face in (s for s in simplices if len(s) == 3):
        restrict = identity[[index[e] for e in combinations(face, 2)], :]
        losses[face] = restrict.T * metric * restrict
    seam = 2 * losses.pop((0, 1, 2))
    exterior = sum(losses.values(), zeros(23))

    s, gamma = symbols('s gamma', positive=True)
    compressed = complement * generator * complement
    active_bases = []
    for i, mode in enumerate((even, odd)):
        drive = complement * generator * mode
        seed_columns = [drive] if i == 1 else [drive, compressed*drive]
        active = Matrix.hstack(*seed_columns)
        active_bases.append(active)
        assert active.rank() == len(seed_columns)
        assert seam * active == zeros(23, active.cols)
        inverse_basis = (active.T*active).inv()*active.T
        assert exterior * drive == 4*drive/3
        if i == 0:
            assert exterior * compressed * drive == zeros(23, 1)
        for label, sink in [('seam', seam), ('exterior', exterior), ('combined', seam+exterior)]:
            operator = complement*(generator-gamma*sink)*complement
            reduced = inverse_basis*operator*active
            assert operator*active == active*reduced
            transfer = factor((mode.T*generator*active*(s*eye(active.cols)-reduced).inv()
                               *inverse_basis*drive)[0]/gram[i, i])
            d = 0 if label == 'seam' else 4*gamma/3
            expected = -3/(s+d) if i else -3*s/(7*(s**2+d*s)+32)
            assert factor(transfer-expected) == 0
            if label != 'combined':
                print(f'{label}, {"odd" if i else "even"}: {transfer}')
    assert active_bases[0].T * active_bases[1] == zeros(2, 1)
    assert even.T * generator * active_bases[1] == zeros(1, 1)
    assert odd.T * generator * active_bases[0] == zeros(1, 2)
    print('Internal seam memory decay rate: 0 at every nonnegative sink strength.')


if __name__ == '__main__':
    main()
