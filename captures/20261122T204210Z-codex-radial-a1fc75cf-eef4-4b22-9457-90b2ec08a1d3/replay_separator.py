"""Exact global spectral separator for the pinned PB3 and PB5 radial pencils."""
import sympy as sp

z, g = sp.symbols("z g")
pb3 = (
    z**2 + g*z + 5,
    z**2 + g*z + sp.Rational(24, 5),
    z**3 + g*z**2 + 5*z + 2*g,
)
pb5_sextic = (
    z**6 + 2*g*z**5 + (9+g**2)*z**4 + 13*g*z**3
    + (19+4*g**2)*z**2 + 18*g*z + 4*g**2
)


def hurwitz_minor(polynomial, shift, k):
    coefficients = sp.Poly(polynomial.subs(z, z-shift), z).all_coeffs()
    return sp.factor(sp.Matrix(k, k, lambda row, col:
        coefficients[2*col-row+1]
        if 0 <= 2*col-row+1 < len(coefficients) else 0
    ).det(method="domain-ge"))


def verify_sign(expression, sign):
    # Verify each primitive factor on the open positive half-line.
    # Remove any power of g so the root count at zero is unambiguous.
    numerator, denominator = sp.fraction(expression)
    for part in (numerator, denominator):
        leading, factors = sp.factor_list(part, g)
        assert leading != 0
        for factor, multiplicity in factors:
            if factor != g:
                poly = sp.Poly(factor, g, domain=sp.QQ)
                assert poly.eval(0) != 0 and poly.count_roots(0, sp.oo) == 0
    assert expression.subs(g, 1)*sign > 0


def radial_certificate():
    shift = 11*g/(10*(g**2+4))
    for p in pb3:
        for k in range(1, sp.degree(p, z)+1):
            minor = hurwitz_minor(p, shift, k)
            verify_sign(minor, 1)
            print(f"PB3 degree {sp.degree(p,z)}, minor {k}: {minor}")
    minor = hurwitz_minor(pb5_sextic, shift, 5)
    verify_sign(minor, -1)
    print(f"PB5 sextic, minor 5: {minor}")
    # Eliminate s = omega² to check that this minor is the same
    # nonreal collision polynomial, with the convention E then O.
    w, s = sp.symbols("w s", real=True)
    translated = sp.Poly(sp.expand(pb5_sextic.subs(z,z-shift).subs(z,sp.I*w)), w)
    even = sum(c*s**(j//2) for (j,),c in translated.terms() if j%2==0)
    odd = sum(c/sp.I*s**(j//2) for (j,),c in translated.terms() if j%2==1)
    result = sp.factor(sp.resultant(even,odd,s))
    ratio = sp.cancel(result/minor)
    assert ratio in (-1, 1), ratio
    print(f"PB5 sextic reduced resultant / minor 5 = {ratio}")
    print("PASS for every g>0: Delta_PB5 < 11*g/(10*(g**2+4)) < Delta_PB3")



if __name__ == "__main__":
    radial_certificate()
