"""Certify the unique PB5/PB3 minimum inside the previously localized window."""

from fractions import Fraction
from math import comb

import numpy as np
from mpmath import iv


iv.dps = 35


def interval(low, high=None):
    high = low if high is None else high
    return iv.mpf([iv.mpf(low.numerator)/low.denominator,
                   iv.mpf(high.numerator)/high.denominator])


def coefficients(g, rim):
    if rim == 3:
        return [1, g, 5, 2*g], [0, 1, 0, 2], [0]*4
    return ([1, 2*g, 9+g*g, 13*g, 19+4*g*g, 18*g, 4*g*g],
            [0, 2, 2*g, 13, 8*g, 18, 8*g], [0, 0, 2, 0, 8, 0, 8])


def horner(coeffs, z):
    value = 0
    for coefficient in coeffs:
        value = value*z + coefficient
    return value


def derivative(coeffs):
    degree = len(coeffs)-1
    return [(degree-i)*coefficient for i, coefficient in enumerate(coeffs[:-1])]


def taylor(coeffs, center, order):
    degree = len(coeffs)-1
    return horner([comb(degree-i, order)*c for i, c in enumerate(coeffs[:degree-order+1])], center)


def stable_to_left(coeffs, margin):
    degree = len(coeffs)-1
    shifted = [taylor(coeffs, -margin, order) for order in range(degree, -1, -1)]
    if not all(a > 0 for a in shifted):
        return False
    if degree < 3:
        return True
    a0, a1, a2, a3, a4 = shifted
    return a3*(a1*a2-a0*a3) > a1*a1*a4


def root_box(low, high, rim):
    working = (low+high)/2
    guess = max((z for z in np.roots(coefficients(float(working), rim)[0]) if z.imag > 0),
                key=lambda z: z.real)
    center = iv.mpc(iv.mpf(str(guess.real)), iv.mpf(str(guess.imag)))
    g = interval(low, high)
    p = coefficients(g, rim)[0]
    midpoint_p, midpoint_pg, pgg = coefficients(interval(working), rim)
    centered = [
        [taylor(coeffs, center, order) for order in range(len(p))]
        for coeffs in (midpoint_p, midpoint_pg, pgg)
    ]
    delta = interval(low-working, high-working)
    center_p, center_pg, center_pgg = centered
    linear = center_p[1]
    if not abs(linear) > 0:
        return None
    radius = max(high-low, Fraction(1, 10**11))
    rad = interval(radius)
    p_local = [a+b*delta+c*delta**2/2 for a,b,c in zip(*centered)]
    uncertainty = abs(p_local[0]) + abs(center_pg[1]*delta+center_pgg[1]*delta**2/2)*rad
    for order in range(2, len(p)):
        uncertainty += abs(p_local[order])*rad**order
    if not abs(linear)*rad > uncertainty:
        return None
    error = interval(-radius, radius)
    offset = iv.mpc(error, error)
    z = center+offset
    margin = iv.mpf(3)/5 if rim == 3 else iv.mpf(1)/3
    if not (z.imag > 0 and z.real > -margin):
        return None

    # Divide out the certified conjugate pair to bound all competing roots.
    linear_coeff = -2*z.real
    constant_coeff = z.real**2+z.imag**2
    quotient = [1]
    for j in range(1, len(p)-2):
        previous = quotient[j-2] if j > 1 else 0
        quotient.append(p[j]-linear_coeff*quotient[-1]-constant_coeff*previous)
    others = ([1, g, 5], [1, g, iv.mpf(24)/5]) if rim == 3 else (
        [1, g, 7], [1, g, iv.mpf(40)/7], [1, 2*g, 9+g*g, 9*g, 19]
    )
    if not all(stable_to_left(q, margin) for q in (*others, quotient)):
        return None

    pg_local = [b+c*delta for b,c in zip(center_pg, center_pgg)]
    p_desc, pg_desc, pgg_desc = p_local[::-1], pg_local[::-1], center_pgg[::-1]
    pz = horner(derivative(p_desc), offset)
    if not abs(pz) > 0:
        return None
    first = -horner(pg_desc, offset)/pz
    second = -(horner(pgg_desc, offset)+2*horner(derivative(pg_desc), offset)*first
               +horner(derivative(derivative(p_desc)), offset)*first**2)/pz
    return -z.real, -first.real, -second.real


def numerator(low, high):
    pb3 = root_box(low, high, 3)
    pb5 = root_box(low, high, 5)
    if pb3 is None or pb5 is None:
        return None
    a, ap, app = pb3
    b, bp, bpp = pb5
    return bp*a-b*ap, bpp*a-b*app


def certify(low, high, index, sign):
    queue = [(low, high, 0)]
    leaves = 0
    while queue:
        left, right, depth = queue.pop()
        result = numerator(left, right)
        if result is not None and sign*result[index] > 0:
            leaves += 1
            continue
        if depth == 22:
            raise RuntimeError(f"Could not certify interval [{left}, {right}]")
        middle = (left+right)/2
        queue.extend(((left, middle, depth+1), (middle, right, depth+1)))
    return leaves


def main():
    lower, upper = Fraction(316, 100), Fraction(318, 100)
    for left, right, index, sign, label in (
        (Fraction(3, 2), lower, 0, -1, "N < 0"),
        (lower, upper, 1, 1, "N' > 0"),
        (upper, Fraction(4), 0, 1, "N > 0"),
    ):
        count = certify(left, right, index, sign)
        print(f"[{left}, {right}]: {label} ({count} certified intervals)")
    assert numerator(lower, lower)[0] < 0 and numerator(upper, upper)[0] > 0
    while upper-lower > Fraction(1, 10**8):
        middle = (lower+upper)/2
        enclosure = numerator(middle, middle)
        assert enclosure is not None
        sign = enclosure[0]
        if sign < 0:
            lower = middle
        elif sign > 0:
            upper = middle
        else:
            raise RuntimeError("Bisection requires a certified sign")
    print(f"Unique minimizer in ({lower}, {upper})")
    print(f"Decimal guide: {float(lower):.10f} < g* < {float(upper):.10f}")


if __name__ == "__main__":
    main()
