"""Exact rational controls for C06's detector and selective hold."""

from fractions import Fraction as F


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def projected_odd(vector):
    return (0, vector[1])


def apply(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def replay():
    stocks = [(49, 1), (25, 25), (1, 49)]
    assert [F(x, y) for x, y in stocks] == [49, 1, F(1, 49)]
    assert [y - x for x, y in stocks] == [-48, 0, 48]
    assert [u*v > 0 for u, v in [(5, 5), (-5, 5), (-5, -5), (5, -5)]] == [True, False, True, False]
    rate_squared = F(106, 9)
    f = 1/(1 + rate_squared)
    assert f == F(9, 115) and 1-f == rate_squared*f
    z = F(3, 4)
    assert (z*z-1)/(z*z+1) == F(-7, 25) != F(-1, 4)

    # Rational direct-sum port control in an orthonormal record chart.
    g_hold = ((2, 0), (0, 0))
    for x, y in [((3, 5), (7, 11)), ((-1, 5), (0, -2)), ((0, 0), (1, 0))]:
        dy = apply(g_hold, x)
        dx = tuple(-v for v in apply(tuple(zip(*g_hold)), y))
        assert projected_odd(dx) == projected_odd(dy) == (0, 0)
        assert (dx[0], dy[0]) == (-2*y[0], 2*x[0])
        assert dot(x, dx) + dot(y, dy) == 0

    # One record shared by two modes, even coupling drives the odd record range.
    g_mixed = ((1, 1),)
    mixed_hold = ((1, 0),)
    assert apply(g_mixed, (0, 1)) == apply(mixed_hold, (1, 0)) == (1,)
    print("Exact ratios 49, 1, 1/49; direction, 9/115 metric bias and v0.15 comparator distinction passed.")
    print("Selective two-way hold and stock conservation passed; shared-record leakage control reproduced.")


if __name__ == "__main__":
    replay()
