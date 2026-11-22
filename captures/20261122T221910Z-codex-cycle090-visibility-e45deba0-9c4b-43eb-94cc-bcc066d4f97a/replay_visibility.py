"""Exact PB3/PB5 memory-pole visibility. Physical Promotion = 0."""

from itertools import combinations

from sympy import Matrix, Poly, Rational, cancel, discriminant, expand, eye, factor, fraction, resultant, symbols, trace, zeros


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


z, g, r = symbols("z g r")
CUBIC = z**3 + g*z**2 + 5*z + 2*g
QUARTIC = z**4 + 2*g*z**3 + (9+g**2)*z**2 + 9*g*z + 19
SEXTIC = (z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
          + (19+4*g**2)*z**2 + 18*g*z + 4*g**2)


def check_trace(rim, linear_scale, collective_constant, factor_slow, expected):
    skew, sink, drive = carrier_operators(rim)
    generator = skew - g*sink
    collective = z**2 + g*z + collective_constant
    annihilator = Poly(collective*factor_slow, z)
    coefficients = annihilator.all_coeffs()
    propagated = drive
    moments = []
    for _ in coefficients[1:]:
        moments.append(expand(trace(drive.T*propagated)))
        propagated = (generator*propagated).applyfunc(expand)
    horner = drive
    for coefficient in coefficients[1:]:
        horner = (generator*horner + coefficient*drive).applyfunc(expand)
    assert horner.is_zero_matrix
    numerator = sum(
        z**(annihilator.degree()-1-i)*sum(coefficients[j]*moments[i-j] for j in range(i+1))
        for i in range(annihilator.degree())
    )
    numerator = expand(linear_scale*numerator)
    assert tuple(factor(resultant(p, numerator, z)) for p in (collective, factor_slow)) == expected
    print(f"PB{rim} trace numerator: {factor(numerator)}")
    print(f"PB{rim} trace denominator: {factor(linear_scale*annihilator.as_expr())}")
    print(f"PB{rim} resultants: {expected}")


def require_positive(expression, variable):
    for part in fraction(cancel(expression)):
        coefficients = Poly(part, variable).all_coeffs()
        assert coefficients[0] > 0 and all(c >= 0 for c in coefficients)


def check_shifted_hurwitz(polynomial, shift, variable):
    coefficients = Poly(polynomial.subs(z, z-shift), z).all_coeffs()
    for k in range(1, len(coefficients)):
        matrix = Matrix(k, k, lambda i, j: coefficients[2*j-i+1]
                        if 0 <= 2*j-i+1 < len(coefficients) else 0)
        require_positive(matrix.det(method="domain-ge"), variable)


def check_hidden_factors():
    # PB3's unique real cubic root is -r, with the complex pair at real part -shift.
    coupling = r*(r**2+5)/(r**2+2)
    shift = 3*r/(2*(r**2+2))
    require_positive(coupling.diff(r), r)
    require_positive(r-shift, r)
    assert cancel(CUBIC.subs({g:coupling, z:-r})) == 0
    assert cancel(coupling-r-2*shift) == 0
    assert expand(discriminant(CUBIC,z)+8*(g**2-Rational(97,16))**2+Rational(6591,32)) == 0
    for constant in (5,Rational(24,5)):
        check_shifted_hurwitz(z**2+coupling*z+constant, shift, r)
    # The independently reviewed PR #605 places a PB5 sextic root to the right
    # of this separator. Both hidden stable factors lie strictly to its left.
    separator = 11*g/(10*(g**2+4))
    for hidden in (z**2+g*z+7, QUARTIC):
        check_shifted_hurwitz(hidden, separator, g)
    print("PASS: hidden stable factors do not determine the PB3 or PB5 gap")


if __name__ == "__main__":
    result3 = 75*g**2+4
    result5 = 213689*g**4+769300*g**2+9680
    require_positive(result3,g)
    require_positive(result5,g)
    check_trace(3,5,Rational(24,5),CUBIC,(
        factor(576*result3/25), factor(1728*g**4*result3),
    ))
    check_trace(5,7,Rational(40,7),SEXTIC,(
        factor(259200*result5/16807), factor(-256000000*g**10*result5),
    ))
    check_hidden_factors()
    print("PASS for g>0: every rightmost stable pole is memory-visible in PB3 and PB5")
