"""Exact controls for the normalized odd oscillator."""

from fractions import Fraction as Q
from itertools import product


def dot(left, right):
    return sum(a*b for a, b in zip(left, right))


def observe(u, v):
    carrier, record = dot(u, u), dot(v, v)
    stock = carrier + record
    return Q(carrier-record, stock), Q(2*dot(u, v), stock), Q(record, stock)


def replay():
    c, s = Q(3, 5), Q(4, 5)
    tested = 0
    for entries in product((-1, 0, 1), repeat=6):
        if not any(entries):
            continue
        u, v = entries[:3], entries[3:]
        d, flux, fraction = observe(u, v)
        assert fraction == (1-d)/2
        assert d*d + flux*flux <= 1
        assert observe(tuple(-2*x for x in u), tuple(-2*x for x in v)) == (d, flux, fraction)
        rotated_u = tuple(c*a-s*b for a, b in zip(u, v))
        rotated_v = tuple(s*a+c*b for a, b in zip(u, v))
        rd, rc, _ = observe(rotated_u, rotated_v)
        assert rd == (c*c-s*s)*d-2*c*s*flux
        assert rc == 2*c*s*d+(c*c-s*s)*flux
        tested += 1
    assert tested == 728
    assert observe((1, 0, 0), (0, 1, 0)) == (0, 0, Q(1, 2))
    assert observe((1,), (0,))[2] == 0 and observe((0,), (1,))[2] == 1
    print("728 exact real-ray and phase-rotation controls, plus both quotient and dephasing witnesses, passed.")


if __name__ == "__main__":
    replay()
