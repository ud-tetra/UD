#!/usr/bin/env python3
"""Certify a lower bound on the turning point for the PB3 and PB5 fixtures."""

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
    z, g, t, x = symbols("z g t x")
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

    # Via g = (3/2)t/(1+t), test all Hurwitz minors for the shifted PB5 factors.
    upper_coupling = Rational(3, 2)
    lower_slope = Rational(7, 50)
    for factor in (z**2+g*z+7, z**2+g*z+Rational(40, 7), quartic, sextic):
        coefficients = Poly(factor.subs(z, z-lower_slope*g), z).all_coeffs()
        degree = len(coefficients) - 1
        hurwitz = Matrix(degree, degree, lambda i, j: (
            coefficients[2*j-i+1] if 0 <= 2*j-i+1 <= degree else 0
        ))
        for size in range(1, degree+1):
            minor = Poly(hurwitz[:size, :size].det(method="domain-ge"), g)
            cleared = Poly(sum(
                coefficient*(upper_coupling*t)**power*(1+t)**(minor.degree()-power)
                for (power,), coefficient in minor.terms()
            ), t)
            assert all(coefficient > 0 for coefficient in cleared.coeffs())
            assert cleared.degree() == minor.degree()
        print(f"Shifted PB5 degree {degree}: all {degree} Hurwitz minors positive")

    def gap_interval(expression):
        intervals = []
        for factor, _ in Poly(expression, z).factor_list()[1]:
            real, complex_pairs = factor.intervals(all=True, eps=Rational(1, 10**7))
            assert sum(count for _, count in real+complex_pairs) == factor.degree()
            intervals.extend((re(lo), re(hi)) for (lo, hi), _ in real+complex_pairs)
        return -max(hi for _, hi in intervals), -max(lo for lo, _ in intervals)

    pb3_min, _ = gap_interval(stable[3].subs(g, 10))
    _, pb5_max = gap_interval(stable[5].subs(g, 10))
    assert pb3_min > 0 and pb5_max/pb3_min < Rational(4533, 10000)
    assert Rational(4533, 10000) < lower_slope/Rational(3, 10)
    print("R(g) > 7/15 for 0 < g <= 3/2; R(10) < 4533/10000")

    def weak_coefficients(factor, center):
        def derivative(j, k):
            return simplify(factor.diff(z, j, g, k).subs({z: center, g: 0}))

        a = simplify(-derivative(0, 1)/derivative(1, 0))
        b = simplify(-(derivative(2, 0)*a*a/2+derivative(1, 1)*a
                       +derivative(0, 2)/2)/derivative(1, 0))
        c = simplify(-(derivative(2, 0)*a*b+derivative(1, 1)*b+derivative(3, 0)*a**3/6
                       +derivative(2, 1)*a*a/2+derivative(1, 2)*a/2
                       +derivative(0, 3)/6)/derivative(1, 0))
        return -re(a), -re(c)

    a3, b3 = weak_coefficients(cubic, I*sqrt(5))
    a5, b5 = weak_coefficients(sextic, I*sqrt((9-sqrt(5))/2))
    weak_limit = simplify(a5/a3)
    weak_linear = simplify((b5-b3*weak_limit)/a3)
    strong_limit = (5-sqrt(5))/6
    strong_inverse = -sqrt(5)/3
    beta = simplify(weak_linear/strong_inverse)
    assert weak_linear < 0 and beta > 0 and weak_limit > strong_limit
    pade = (weak_limit+weak_linear*x+strong_limit*beta*x**2)/(1+beta*x**2)
    derivative = weak_linear+2*beta*(strong_limit-weak_limit)*x-beta*weak_linear*x**2
    assert simplify(pade.diff(x)-derivative/(1+beta*x**2)**2) == 0
    g_min = sqrt(max(root for root in Poly(derivative, x).nroots()))
    print(f"Weak g^2 coefficient: {weak_linear}")
    print(f"Pade minimum at g={float(g_min):.9f}, ratio={float(pade.subs(x, g_min**2)):.9f}")


if __name__ == "__main__":
    main()
