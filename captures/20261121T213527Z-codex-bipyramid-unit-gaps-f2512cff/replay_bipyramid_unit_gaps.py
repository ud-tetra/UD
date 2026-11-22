#!/usr/bin/env python3
"""Derive exact unit-sink polynomials and estimate their spectral gaps."""

from itertools import combinations

from sympy import Matrix, Poly, eye, symbols, zeros


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
    return complement * skew * complement - sink, complement * skew * averages


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


def slowest_real_part(polynomial):
    roots = [
        complex(root)
        for factor, _ in polynomial.factor_list()[1]
        for root in factor.nroots(n=30, maxsteps=250)
    ]
    return max(root.real for root in roots)


def main():
    z = symbols("z")
    dark = {
        3: (z**2 + 2)**2 * (z**2 + 5)**2,
        5: (z**2 + 2)**2 * (z**4 + 9*z**2 + 19)**2,
    }
    results = []
    for rim in (3, 5):
        generator, drive = carrier_operators(rim)
        full = Poly(generator.charpoly(z).as_expr(), z)
        stable = full.exquo(Poly(z**rim * dark[rim], z))
        observable = memory_denominator(generator, drive, full)
        assert stable.rem(observable).is_zero
        gap = -slowest_real_part(stable)
        memory_rate = -slowest_real_part(observable)
        assert gap > 0 and memory_rate > 0
        print(f"PB{rim} stable polynomial: {stable.as_expr().factor()}")
        print(f"PB{rim} memory denominator: {observable.as_expr().factor()}")
        print(f"PB{rim} spectral gap {gap:.12f}; memory pole rate {memory_rate:.12f}")
        results.append((gap, memory_rate))
    print(f"PB5/PB3 spectral gap ratio: {results[1][0] / results[0][0]:.12f}")
    print(f"PB5/PB3 memory rate ratio: {results[1][1] / results[0][1]:.12f}")


if __name__ == "__main__":
    main()
