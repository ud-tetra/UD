#!/usr/bin/env python3
"""Derive weak-coupling damping slopes for the PB3 and PB5 fixtures."""

from itertools import combinations

from numpy import asarray, linalg
from sympy import Matrix, Poly, Rational, eye, simplify, sqrt, symbols, zeros


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
    return complement * skew * complement, sink, complement * skew * averages


def memory_denominator(generator, drive, characteristic):
    # Multiply the Laurent expansion at infinity by the characteristic
    # polynomial. Cayley-Hamilton makes the polynomial part the numerator.
    degree = characteristic.degree()
    coefficients = characteristic.all_coeffs()
    moments = []
    propagated = drive
    for _ in range(degree):
        moments.append(drive.T * propagated)
        propagated = generator * propagated
    numerator = [
        sum((coefficients[j] * moments[i - j] for j in range(i + 1)), zeros(drive.cols))
        for i in range(degree)
    ]
    common = characteristic
    for row in range(drive.cols):
        for column in range(drive.cols):
            entry = Poly.from_list([block[row, column] for block in numerator], characteristic.gen)
            common = common.gcd(entry)
    return characteristic.exquo(common).monic()


def main():
    z, g, w = symbols("z g w")
    dark = {
        3: (z**2 + 2)**2 * (z**2 + 5)**2,
        5: (z**2 + 2)**2 * (z**4 + 9*z**2 + 19)**2,
    }
    slow_factor = {
        3: z**3 + g*z**2 + 5*z + 2*g,
        5: z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
           + (19+4*g**2)*z**2 + 18*g*z + 4*g**2,
    }
    rates = []
    operators = []
    for rim in (3, 5):
        skew, sink, drive = carrier_operators(rim)
        operator = skew - g*sink
        characteristic = Poly(operator.charpoly(z).as_expr(), z, g)
        stable = characteristic.exquo(Poly(z**rim * dark[rim], z, g))
        factors = [(p.monic(), count) for p, count in stable.factor_list()[1]]
        leading = Poly(slow_factor[rim], z, g)
        assert (leading.as_expr(), 2) in [(p.as_expr(), count) for p, count in factors]
        print(f"PB{rim} stable characteristic polynomial: {stable.as_expr().factor()}")

        unit = skew - sink
        unit_full = Poly(unit.charpoly(z).as_expr(), z)
        unit_leading = Poly(leading.as_expr().subs(g, 1), z)
        remaining = unit_full.exquo(unit_leading**2)
        assert unit_leading.gcd(remaining).degree() == 0
        assert memory_denominator(unit, drive, unit_full).rem(unit_leading).is_zero

        if rim == 3:
            slopes = [Rational(1, 2), Rational(2, 5), Rational(3, 10)]
        else:
            blown_up = slow_factor[rim].subs(z, g*w).expand().coeff(g, 2)
            assert blown_up == 19*w**2 + 18*w + 4
            slopes = [Rational(1, 2), (9-sqrt(5))/19, (9+sqrt(5))/19]
            for x in ((-9+sqrt(5))/2, (-9-sqrt(5))/2):
                slopes.append(simplify((2*x*x+13*x+18)/(2*x*(2*x+9))))
            assert slopes[-2] == (10-sqrt(5))/38
        rate = min(slopes)
        rates.append(rate)
        print(f"PB{rim} distinct damping slopes: {slopes}")
        print(f"PB{rim} smallest slope: {rate} = {float(rate):.12f}")
        operators.append((asarray(skew, dtype=float), asarray(sink, dtype=float)))

    ratio = simplify(rates[1] / rates[0])
    assert simplify(ratio - 5*(10-sqrt(5))/57) == 0
    print(f"Limiting gap ratio: {ratio} = {float(ratio):.12f}")
    print("gamma       PB3 gap/gamma   PB5 gap/gamma   PB5/PB3")
    for gamma in (1e-1, 1e-2, 1e-3, 1e-4):
        slopes = []
        for skew, sink in operators:
            eigenvalues = linalg.eigvals(skew - gamma*sink)
            slopes.append(-max(v.real for v in eigenvalues if v.real < -1e-9) / gamma)
        print(f"{gamma:.0e}       {slopes[0]:.9f}     {slopes[1]:.9f}     {slopes[1]/slopes[0]:.9f}")


if __name__ == "__main__":
    main()
