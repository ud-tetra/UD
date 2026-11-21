#!/usr/bin/env python3
"""Derive strong-coupling damping slopes for the PB3 and PB5 fixtures."""

from itertools import combinations

from numpy import geomspace, roots
from sympy import I, Matrix, Poly, Rational, eye, expand, lambdify, sqrt, symbols, zeros


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

    def scaled(factor, power, center):
        return expand(h**power * factor.subs({g: 1/h, z: center+h*w}, simultaneous=True))

    assert expand(scaled(cubic, 1, I*sqrt(2)).coeff(h) - I*sqrt(2)*(2*w+3)) == 0
    assert scaled(quartic, 2, 0).coeff(h, 2) == w**2+9*w+19
    assert scaled(sextic, 2, I*sqrt(2)).coeff(h, 2) == -8*w**2-20*w-10
    slope3 = min(5, Rational(24, 5), Rational(3, 2))
    slope5 = min(7, Rational(40, 7), (9-sqrt(5))/2, (5-sqrt(5))/4)
    ratio = (5-sqrt(5))/6
    assert expand(slope5/slope3 - ratio) == 0
    print(f"PB3 inverse-coupling coefficient: {slope3}")
    print(f"PB5 inverse-coupling coefficient: {slope5}")
    print(f"Strong-coupling ratio: {ratio} = {float(ratio):.12f}")

    polynomials = {}
    for rim, expression in stable.items():
        polynomials[rim] = [
            lambdify(g, Poly(factor, z).all_coeffs(), "numpy") for factor, _ in Poly(expression, z, g).factor_list()[1]
        ]

    def gap(rim, gamma):
        return -max(
            root.real
            for coefficients in polynomials[rim]
            for root in roots(coefficients(gamma))
        )

    for gamma in (10, 100, 1000):
        print(f"gamma={gamma}: gamma*PB3={gamma*gap(3,gamma):.9f}; "
              f"gamma*PB5={gamma*gap(5,gamma):.9f}; ratio={gap(5,gamma)/gap(3,gamma):.9f}")
    grid = geomspace(1e-4, 1e4, 801)
    maximum = max((gap(5,x)/gap(3,x), x) for x in grid)
    print(f"Grid maximum ratio: {maximum[0]:.9f} at gamma={maximum[1]:.4g}")


if __name__ == "__main__":
    main()
