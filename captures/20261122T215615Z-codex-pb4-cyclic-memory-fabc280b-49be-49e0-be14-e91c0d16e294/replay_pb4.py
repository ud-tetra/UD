"""Exact PB4 radial and exterior certificates. Physical Promotion = 0."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import factorial

import sympy as sp


z, g, r = sp.symbols("z g r")
PB3 = (z**2 + g*z + 5, z**2 + g*z + sp.Rational(24, 5), z**3 + g*z**2 + 5*z + 2*g)
PB4_QUADRATICS = tuple(z**2 + g*z + c for c in (4, 6, sp.Rational(16, 3)))
PB4_CUBIC = z**3 + g*z**2 + 4*z + 2*g
PB5_SEXTIC = (
    z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
    + (19+4*g**2)*z**2 + 18*g*z + 4*g**2
)


def build_operators(n):
    poles = (n, n+1)
    cells = [tuple(sorted((j, (j+1) % n, *poles))) for j in range(n)]
    simplices = [
        face for size in range(1, 5)
        for face in sorted({face for cell in cells for face in combinations(cell, size)})
    ]
    indices = {face: i for i, face in enumerate(simplices)}
    size = len(simplices)
    assert tuple(sum(len(face) == k for face in simplices) for k in range(1, 5)) == (
        n+2, 3*n+1, 3*n, n
    )
    boundary = sp.zeros(size)
    for column, face in enumerate(simplices):
        if len(face) > 1:
            for i in range(len(face)):
                boundary[indices[face[:i] + face[i+1:]], column] = (-1)**i
    assert boundary**2 == sp.zeros(size)
    averages = sp.Matrix([
        [int(len(face) == 1 and face[0] in cell) for cell in cells] for face in simplices
    ])
    basis = sp.Matrix.hstack(*averages.columnspace())
    assert basis.cols == n - int(n % 2 == 0)
    if n % 2 == 0:
        assert averages * sp.Matrix([(-1)**i for i in range(n)]) == sp.zeros(size, 1)
    q = sp.eye(size) - basis * (basis.T*basis).inv() * basis.T
    skew = boundary - boundary.T
    radial_edges = {poles} | {(j, pole) for j in range(n) for pole in poles}
    radial = sp.diag(*[int(face in radial_edges) for face in simplices])
    assert radial.rank() == 2*n+1

    orientation = sp.Matrix([1, -1, 1])
    whitney = (6*sp.eye(3) - orientation * orientation.T) / 9
    exterior = sp.zeros(size)
    face_counts = Counter(face for cell in cells for face in combinations(cell, 3))
    for face, count in face_counts.items():
        if count == 1:
            edges = [indices[edge] for edge in combinations(face, 2)]
            for i, row in enumerate(edges):
                for j, column in enumerate(edges):
                    exterior[row, column] += whitney[i, j]
    return q*skew*q, radial, exterior, q*skew*averages


def radial_factors_and_transfer(a, sink, forcing):
    full = (a - g*sink).charpoly(z).as_expr()
    neutral = (z**2+2)**2 * (z**2+4)**2 * (z**2+6)**2
    q4, q6, q_collective = PB4_QUADRATICS
    expected = z**3 * neutral * q4**2 * q6**4 * q_collective * PB4_CUBIC**2
    assert sp.Poly(full-expected, z, g).is_zero

    channels = (sp.ones(4, 1), sp.Matrix([1, 0, -1, 0]), sp.Matrix([0, 1, 0, -1]))
    operator = a - g*sink
    spaces = []
    for channel, expected_transfer in zip(channels, (
        z/q_collective,
        (2*z**2 + g*z + 8)/(2*PB4_CUBIC),
        (2*z**2 + g*z + 8)/(2*PB4_CUBIC),
    )):
        b = forcing*channel
        columns = sp.Matrix.hstack(b, operator*b, operator**2*b)
        basis = sp.Matrix.hstack(*columns.columnspace())
        reduced = (basis.T*basis).inv()*basis.T*operator*basis
        assert (basis*reduced-operator*basis).applyfunc(sp.cancel).is_zero_matrix
        assert all((space.T*basis).applyfunc(sp.cancel).is_zero_matrix for space in spaces)
        spaces.append(basis)
        observed = (b.T*basis*(z*sp.eye(basis.cols)-reduced).inv()[:, 0])[0]/b.dot(b)
        assert sp.cancel(observed-expected_transfer) == 0
    assert sum(basis.cols for basis in spaces) == 8
    assert sp.resultant(2*z**2+g*z+8, PB4_CUBIC, z) == 2*g**4
    assert sp.resultant(z, q_collective, z) == sp.Rational(16, 3)
    print("PB4: carrier 35, resolved rank 3, compressed dimension 32")
    print(f"PB4 radial characteristic on Q: {sp.factor(expected/z**3)}")
    print("PB4 radial transfer: 8 memory-active dimensions, no cancellation for g>0")


def shifted_minor(p, k, coupling, shift):
    coefficients = sp.Poly(p.subs(g, coupling).subs(z, z-shift), z).all_coeffs()
    matrix = sp.Matrix(k, k, lambda i, j: coefficients[2*j-i+1]
                       if 0 <= 2*j-i+1 < len(coefficients) else 0)
    return sp.factor(matrix.det(method="domain-ge"))


def verify_positive(expression):
    for part in sp.fraction(sp.cancel(expression)):
        coefficients = sp.Poly(part, r).all_coeffs()
        assert coefficients[0] > 0 and all(c >= 0 for c in coefficients)


def radial_hierarchy():
    coupling = r*(r**2+4)/(r**2+2)
    shift = r/(r**2+2)
    assert sp.cancel(coupling-r-2*shift) == 0
    assert sp.cancel(PB4_CUBIC.subs({g: coupling, z: -r})) == 0
    verify_positive(sp.diff(coupling, r))
    verify_positive(r-shift)
    assert sp.expand(sp.discriminant(PB4_CUBIC, z)
                     + 8*(g**2-sp.Rational(13, 4))**2 + sp.Rational(343, 2)) == 0
    for p in (*PB3, *PB4_QUADRATICS):
        for k in range(1, sp.degree(p, z)+1):
            verify_positive(shifted_minor(p, k, coupling, shift))
    minor = shifted_minor(PB5_SEXTIC, 5, coupling, shift)
    verify_positive(-minor)
    print(f"PB5 sextic fifth minor at the PB4 gap: {minor}")
    print("PASS for g>0: PB5 stable gap < PB4 stable gap = PB4 memory decay rate < PB3 stable gap")


def exterior_crosscheck(n):
    a, _, sink, forcing = build_operators(n)
    ones = sp.ones(n, 1)
    collective = forcing*ones
    partner = a*collective
    c = sp.Rational(8*n, n+2)
    rank = n-int(n % 2 == 0)
    assert forcing.rank() == rank
    assert partner != sp.zeros(partner.rows, 1)
    assert a*forcing == partner*ones.T/n
    assert a*partner == -c*collective
    assert sink*forcing == sp.Rational(4, 3)*forcing
    assert sink*partner == sp.zeros(partner.rows, 1)
    d = 4*g/3
    block = sp.Matrix([[-d, -c], [1, 0]])
    quadratic = z**2 + d*z + c
    assert sp.expand((z*sp.eye(2)-block).det()-quadratic) == 0
    print(f"PB{n} exterior check: rank {rank}, active determinant {(z+d)**(rank-1)*quadratic}")


def exp_negative_bracket(x):
    partial = sum(x**k/factorial(k) for k in range(31))
    next_term = x**31/factorial(31)
    assert 0 < x < 32
    return 1/(partial+next_term/(1-x/32)), 1/partial


def exterior_settling():
    t = Fraction(29, 10)
    assert Fraction("2.14")**2 > Fraction(32, 7)
    assert 2*Fraction("3.14")/Fraction("2.14") > t
    a, b, d = Fraction(4, 3), Fraction(4), Fraction(16, 3)
    slow_lower, slow_upper = (a/(b-a)*x for x in exp_negative_bracket(a*t))
    fast_lower, fast_upper = (b/(b-a)*x for x in exp_negative_bracket(b*t))
    _, transverse_upper = exp_negative_bracket(d*t)
    assert max(slow_upper, fast_upper, transverse_upper) < Fraction("0.0105") < Fraction(1, 62)
    assert max(fast_upper, transverse_upper) < Fraction("0.000014")
    assert slow_lower-fast_upper > Fraction("0.0104") > Fraction("0.00123")
    assert fast_lower > Fraction("0.000007204")
    print("PB4 exterior at raw g=4, t>=29/10: norm < 0.0105 < 1/62, slow-residue error < 0.000014")
    print("PB4 at t=29/10: norm > 0.0104, slow-residue error > 0.000007204")


if __name__ == "__main__":
    skew, radial, _, b = build_operators(4)
    radial_factors_and_transfer(skew, radial, b)
    radial_hierarchy()
    for rim in (3, 4, 5, 6, 7, 8):
        exterior_crosscheck(rim)
    exterior_settling()
