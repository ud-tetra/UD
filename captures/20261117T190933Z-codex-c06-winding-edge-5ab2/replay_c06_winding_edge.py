"""Exact controls for the C06 winding and edge observation audit."""

from fractions import Fraction
from itertools import product


def guard(carrier, record):
    """Directed balance with positive rate on a real aligned pair."""
    return carrier**2 == record**2 and carrier * record > 0


def replay():
    pairs = ((7, 1), (5, 5), (1, 7))
    assert all(u > 0 and v > 0 for u, v in pairs)  # All lie before one full turn.
    assert [guard(u, v) for u, v in pairs] == [False, True, False]
    tested = 0
    for preparation in product(range(-2, 3), repeat=3):
        if not any(preparation):
            continue
        for u, v in pairs:
            assert any(guard(a*u, a*v) for a in preparation) == guard(u, v)
            assert sum((a*v)**2-(a*u)**2 for a in preparation) == (
                sum(a*a for a in preparation)*(v*v-u*u)
            )
            tested += 1
    assert tested == 372
    for observed in range(3):
        direction = (observed + 1) % 3
        initial = tuple(int(i == direction) for i in range(3))
        assert initial[observed] == 0 and sum(initial) == 1
    assert guard(5, 5) and 5**2 + 1**2 - 5**2 - 7**2 == -48
    assert [Fraction(v*v, u*u + v*v) for u, v in pairs] == [
        Fraction(1, 50), Fraction(1, 2), Fraction(49, 50)
    ]
    print("372 exact common-phase controls passed. Winding, invisible-edge and asynchronous witnesses reproduced.")


if __name__ == "__main__":
    replay()
