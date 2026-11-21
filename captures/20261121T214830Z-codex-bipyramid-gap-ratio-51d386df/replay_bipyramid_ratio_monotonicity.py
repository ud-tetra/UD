#!/usr/bin/env python3
"""Certify the strong-coupling upturn for the PB3 and PB5 fixtures."""

from itertools import combinations

from sympy import I, Matrix, Poly, Rational, eye, expand, re, simplify, sqrt, symbols, zeros


def carrier_operators(rim):
    poles = (rim, rim + 1)
    cells = [tuple(sorted((i, (i + 1) % rim, *poles))) for i in range(rim)]
    simplices = [
        simplex for size in range(1, 5)
        for simplex in sorted({s for cell in cells for s in combinations(cell, size)})
    ]
    index = {simplex: i for i, simplex in enumerate(simplices)}
    dimension = len(simplices)
    boundary = zeros(dimension)
    for simplex, column in index.items():
        if len(simplex) > 1:
            for i in range(len(simplex)):
                boundary[index[simplex[:i] + simplex[i + 1:]], column] = (-1)**i
    assert boundary**2 == zeros(dimension)
    skew = boundary - boundary.T
    averages = Matrix([
        [int(len(simplex) == 1 and simplex[0] in cell) for cell in cells]
        for simplex in simplices
    ])
    gram = averages.T * averages
    identity = eye(dimension)
    complement = identity - averages * gram.inv() * averages.T
    edges = [poles] + [(i, pole) for i in range(rim) for pole in poles]
    selector = identity[[index[edge] for edge in edges], :]
    sink = selector.T * selector
    assert sink.rank() == 2 * rim + 1 and sink * averages == zeros(dimension, rim)
    return complement * skew * complement, sink


def main():
    z, g, h, w = symbols("z g h w")
    cubic = z**3 + g*z**2 + 5*z + 2*g
    quartic = z**4 + 2*g*z**3 + (9+g**2)*z**2 + 9*g*z + 19
    sextic = (z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
              + (19+4*g**2)*z**2 + 18*g*z + 4*g**2)
    dark = {
        3: (z**2 + 2)**2 * (z**2 + 5)**2,
        5: (z**2 + 2)**2 * (z**4 + 9*z**2 + 19)**2,
    }
    stable = {
        3: (z**2+g*z+5)**4 * (z**2+g*z+Rational(24, 5)) * cubic**2,
        5: (z**2+g*z+7)**2 * (z**2+g*z+Rational(40, 7)) * quartic**2 * sextic**2,
    }

    for rim in (3, 5):
        skew, sink = carrier_operators(rim)
        full = Poly((skew - g*sink).charpoly(z).as_expr(), z, g)
        assert (full - Poly(z**rim * dark[rim] * stable[rim], z, g)).is_zero

    inverse_gap_coefficients = {}
    for rim, factor, w0 in (
        (3, cubic, -Rational(3, 2)),
        (5, sextic, -(5-sqrt(5))/4),
    ):
        scaled = expand(factor.subs({z: I*sqrt(2)+h*w, g: 1/h}, simultaneous=True))
        f0, f1, f2 = (scaled.coeff(h, k) for k in range(3))
        derivative = f0.diff(w).subs(w, w0)
        assert f0.subs(w, w0).simplify() == 0 and derivative.simplify() != 0
        w1 = simplify(-f1.subs(w, w0) / derivative)
        correction = f2 + f1.diff(w)*w1 + f0.diff(w, 2)*w1**2/2
        w2 = simplify(-correction.subs(w, w0) / derivative)
        assert re(w1) == 0
        inverse_gap_coefficients[rim] = (-w0, simplify(-re(w2)))
        print(f"PB{rim}: coefficients of gamma^-1 and gamma^-3: {inverse_gap_coefficients[rim]}")

    a3, b3 = inverse_gap_coefficients[3]
    a5, b5 = inverse_gap_coefficients[5]
    limit = simplify(a5/a3)
    quadratic = simplify((b5*a3-a5*b3)/a3**2)
    assert simplify(quadratic + sqrt(5)/3) == 0
    print(f"Ratio limit: {limit}")
    print(f"Ratio coefficient of gamma^-2: {quadratic}")
    print(f"Ratio derivative coefficient of gamma^-3: {-2*quadratic}")

    def gap_interval(rim, coupling):
        intervals = []
        polynomial = Poly(stable[rim].subs(g, coupling), z)
        for factor, _ in polynomial.factor_list()[1]:
            real_roots, complex_roots = factor.intervals(all=True, eps=Rational(1, 10**7))
            assert sum(count for _, count in real_roots + complex_roots) == factor.degree()
            intervals.extend((re(lo), re(hi)) for (lo, hi), _ in real_roots + complex_roots)
        return -max(hi for _, hi in intervals), -max(lo for lo, _ in intervals)

    for coupling, lower, upper in ((10, 4532, 4533), (100, 4605, 4607)):
        pb3_min, pb3_max = gap_interval(3, coupling)
        pb5_min, pb5_max = gap_interval(5, coupling)
        assert pb3_min > 0 and pb5_min > 0
        assert Rational(lower, 10000) < pb5_min/pb3_max
        assert pb5_max/pb3_min < Rational(upper, 10000)
        print(f"At gamma={coupling}: {lower}/10000 < PB5/PB3 < {upper}/10000")


if __name__ == "__main__":
    main()
