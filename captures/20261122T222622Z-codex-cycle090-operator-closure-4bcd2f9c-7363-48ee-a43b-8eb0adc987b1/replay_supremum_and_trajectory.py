"""Exact ratio-supremum and prepared exterior trajectory bounds."""

from fractions import Fraction
from itertools import permutations

import sympy as sp


z, g, r = sp.symbols("z g r")
radical = sp.sqrt(5)
ratio_limit = 5*(10-radical)/57
cubic = z**3 + g*z**2 + 5*z + 2*g
sextic = (z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
          + (19+4*g**2)*z**2 + 18*g*z + 4*g**2)


def require_positive_coefficients(expression):
    for part in sp.fraction(sp.cancel(expression)):
        coefficients = sp.Poly(part, r).all_coeffs()
        assert coefficients[0] > 0 and all(c >= 0 for c in coefficients)


def certify_pb3_gap():
    coupling = r*(r**2+5)/(r**2+2)
    gap = 3*r/(2*(r**2+2))
    assert sp.expand(sp.discriminant(cubic, z)
                     + 8*(g**2-sp.Rational(97,16))**2 + sp.Rational(6591,32)) == 0
    assert sp.cancel(cubic.subs({z:-r, g:coupling})) == 0
    assert sp.cancel(coupling-r-2*gap) == 0
    require_positive_coefficients(sp.diff(coupling, r))
    require_positive_coefficients(r-gap)
    for c in (5, sp.Rational(24,5)):
        require_positive_coefficients(coupling-2*gap)
        require_positive_coefficients(gap**2-coupling*gap+c)
    return coupling, gap


def determinant_polynomial(coefficients, size):
    domain = {"extension":radical}
    result = sp.Poly(0, r, **domain)
    for permutation in permutations(range(size)):
        indices = [2*j-i+1 for i,j in enumerate(permutation)]
        if all(0 <= k < len(coefficients) for k in indices):
            inversions = sum(permutation[i] > permutation[j]
                             for i in range(size) for j in range(i+1,size))
            term = sp.prod((coefficients[k] for k in indices),start=sp.Poly(1,r,**domain))
            result += (-1)**inversions*term
    return result


def positive_in_quadratic_field(value):
    b = value.expand().coeff(radical)
    a = sp.expand(value-b*radical)
    assert a.is_Rational and b.is_Rational
    return (a >= 0 and b >= 0 and a+b > 0
            or a > 0 > b and a*a > 5*b*b
            or b > 0 > a and 5*b*b > a*a)


def certify_supremum():
    coupling, gap = certify_pb3_gap()
    shift = ratio_limit*gap
    denominator = r**2+2
    translated = sp.Poly(sextic.subs(g,coupling).subs(z,z-shift),z)
    scaled = [
        sp.Poly(sp.cancel(coefficient*denominator**k, extension=radical),
                r, extension=radical)
        for k,coefficient in enumerate(translated.all_coeffs())
    ]
    # This is the monic polynomial obtained by multiplying the translated
    # roots by r**2+2. The sign of each Hurwitz minor is preserved.
    negative_minor = -determinant_polynomial(scaled,5)
    assert [degree for (degree,),_ in negative_minor.terms()] == list(range(35,4,-2))
    assert all(positive_in_quadratic_field(value) for value in negative_minor.coeffs())
    assert sp.simplify(((10-radical)/38)/sp.Rational(3,10)-ratio_limit) == 0
    print("PB5: negative fifth shifted Hurwitz minor certified by 16 positive coefficients")
    print(f"Strict ratio bound for g>0; supremum = {ratio_limit} by the weak limit")


def certify_trajectory():
    d = sp.Rational(16,3)
    stiffness_cap = d**2*sp.Rational(3,8)/(1+sp.Rational(3,8))**2
    # Largest transverse Fourier stiffness of PB3, PB4, or PB5 is (9+sqrt(5))/2.
    assert positive_in_quadratic_field(stiffness_cap-(9+radical)/2)
    assert sp.Rational(7) < d*d/4
    assert Fraction(3,8)**8 < Fraction(21,100)**5
    assert Fraction(3,16) < Fraction(21,100)
    assert Fraction(9,49) < Fraction(21,100)
    for n in (3,4,5):
        c = sp.Rational(8*n,n+2)
        k = sp.Rational((n-2)**2,n+2)
        # The Schur complement of the unresolved collective two-state block
        # gives the prepared resolved transfer from its initial coordinate.
        block = sp.Matrix([[0,-k,0],[1,-d,-c],[0,1,0]])
        response = (z*sp.eye(3)-block).inv()[0,0]
        assert sp.cancel(response-1/z+k/(z*(z**2+d*z+n+2))) == 0
        assert k/(n+2) <= sp.Rational(9,49)
    k = sp.symbols("k", positive=True)
    transverse = (z*sp.eye(2)-sp.Matrix([[0,-k],[1,-d]])).inv()[0,0]
    assert sp.cancel(transverse-(z+d)/(z**2+d*z+k)) == 0
    print("PB3, PB4, PB5: prepared exterior trajectory error < 21/100 in relative operator norm for all t>=0")


if __name__ == "__main__":
    certify_supremum()
    certify_trajectory()
