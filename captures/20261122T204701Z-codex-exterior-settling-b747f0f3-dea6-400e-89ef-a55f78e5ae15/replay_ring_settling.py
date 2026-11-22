"""Exact exterior-only PB3/PB5 settling bounds. Physical Promotion = 0."""
from fractions import Fraction
from math import factorial

DAMPING = Fraction(16, 3)
CENTER = DAMPING / 2
TIME_LOWER = Fraction(29, 10)
TOLERANCE = Fraction(1, 62)


def exp_negative_upper(x):
    """Bound e**(-x) by the reciprocal of a positive Taylor partial sum."""
    assert x > 0
    return 1 / sum(x**k / factorial(k) for k in range(31))


def verify_ring(name, omega_squared, a_lower, a_upper, norm_limit, remainder_limit):
    radicand = CENTER**2 - omega_squared
    assert 0 < a_lower < a_upper < CENTER
    assert (CENTER - a_upper)**2 < radicand < (CENTER - a_lower)**2
    b_lower = DAMPING - a_upper
    b_upper = DAMPING - a_lower
    separation_lower = b_lower - a_upper
    assert separation_lower > 0

    slow = a_upper / separation_lower * exp_negative_upper(a_lower * TIME_LOWER)
    fast = b_upper / separation_lower * exp_negative_upper(b_lower * TIME_LOWER)
    transverse = exp_negative_upper(DAMPING * TIME_LOWER)
    assert max(slow, fast, transverse) < norm_limit < TOLERANCE
    assert max(fast, transverse) < remainder_limit
    print(f"{name}: norm < {norm_limit}; slow-residue approximation error < {remainder_limit}")


if __name__ == "__main__":
    # T = 2*pi/sqrt(32/7), pi > 3.14 and sqrt(32/7) < 2.14.
    # Prove the stronger result on the entire interval [29/10, infinity).
    assert Fraction("2.14")**2 > Fraction(32, 7)
    assert 2 * Fraction("3.14") / Fraction("2.14") > TIME_LOWER
    verify_ring("PB3", Fraction(24, 5), Fraction("1.146432766"),
                Fraction("1.146432767"), Fraction("0.0136"), Fraction("0.0000074"))
    verify_ring("PB5", Fraction(40, 7), Fraction("1.484792986"),
                Fraction("1.484792987"), Fraction("0.0085"), Fraction("0.000024"))
