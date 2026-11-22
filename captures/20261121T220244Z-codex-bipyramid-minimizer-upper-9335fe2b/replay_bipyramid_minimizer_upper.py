#!/usr/bin/env python3
"""Certify a strong-coupling exclusion interval for the PB3 and PB5 fixtures."""

from itertools import combinations

from sympy import Matrix, Poly, Rational, eye, expand, re, symbols, zeros


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
    z, g, t = symbols("z g t")
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

    start = 4
    pb5_coefficient = Rational(13, 20)
    pb3_coefficient = Rational(157, 100)

    for factor in (z**2+g*z+7, z**2+g*z+Rational(40, 7), quartic, sextic):
        shifted = Poly(factor.subs(z, z-pb5_coefficient/g), z)
        degree = shifted.degree()
        coefficients = [expand(g**degree*c) for c in shifted.all_coeffs()]
        hurwitz = Matrix(degree, degree, lambda i, j: (
            coefficients[2*j-i+1] if 0 <= 2*j-i+1 <= degree else 0
        ))
        for size in range(1, degree+1):
            minor = hurwitz[:size, :size].det(method="domain-ge")
            shifted_minor = Poly(minor.subs(g, t+start), t)
            assert shifted_minor.TC() > 0
            assert all(c > 0 for c in shifted_minor.coeffs())
        print(f"PB5 shifted degree {degree}: {degree} Hurwitz minors positive for g >= 4")

    cubic_test = Poly(expand(g**3*cubic.subs(z, -g+2*pb3_coefficient/g)), g)
    shifted_test = Poly(cubic_test.as_expr().subs(g, t+start), t)
    assert shifted_test.TC() > 0 and all(c > 0 for c in shifted_test.coeffs())

    def gap_interval(expression):
        intervals = []
        for factor, _ in Poly(expression, z).factor_list()[1]:
            real, complex_pairs = factor.intervals(all=True, eps=Rational(1, 10**7))
            assert sum(count for _, count in real+complex_pairs) == factor.degree()
            intervals.extend((re(lo), re(hi)) for (lo, hi), _ in real+complex_pairs)
        return -max(hi for _, hi in intervals), -max(lo for lo, _ in intervals)

    pb3_min, pb3_max = gap_interval(stable[3].subs(g, 3))
    pb5_min, pb5_max = gap_interval(stable[5].subs(g, 3))
    assert pb3_min > 0 and pb5_min > 0
    assert Rational(411, 1000) < pb5_min/pb3_max
    assert pb5_max/pb3_min < Rational(412, 1000) < pb5_coefficient/pb3_coefficient
    print("PB3 cubic test positive for g >= 4")
    print("411/1000 < R(3) < 412/1000 < 65/157 < R(g) for g >= 4")
    print("Combined with #599: every global minimizer satisfies 3/2 < g < 4")


if __name__ == "__main__":
    main()
