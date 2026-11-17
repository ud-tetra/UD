"""Exact controls for the C06 pair-balance observable and exchange law."""

from fractions import Fraction as Q
from itertools import product


def pair_product(a, b, c, d):
    return a * b - c * d


def sector_balances(x, y):
    pairs = zip(x[::2], x[1::2], y[::2], y[1::2])
    even = odd = 0
    for a, b, c, d in pairs:
        even += Q((a + b)**2 - (c + d)**2, 2)
        odd += Q((c - d)**2 - (a - b)**2, 2)
    return even, odd


def replay():
    coefficients = [Q(-2), Q(-1, 2), Q(0), Q(1, 2), Q(2)]
    for a, b, c, d in product(coefficients, repeat=4):
        j = pair_product(a, b, c, d)
        assert j == pair_product(b, a, d, c)
        assert 2*j == sum(sector_balances((a, b), (c, d)))

    empty = (0,) * 6
    mixed = (2, 0, Q(-1, 2), Q(-1, 2), Q(-1, 2), Q(-1, 2))
    assert sum(mixed) == 0 and pair_product(*mixed[:2], 0, 0) == 0
    assert sector_balances(mixed, empty)[1] == -2
    aggregate_control = (6, 0, 0, -6, 0, 0)
    even, odd = sector_balances(aggregate_control, empty)
    assert (even, odd) == (36, -36)
    assert sum(pair_product(*aggregate_control[i:i + 2], 0, 0)
               for i in range(0, 6, 2)) == 0

    pure_odd = (1, -1, 0, 0, 0, 0)
    assert sector_balances(pure_odd, pure_odd) == (0, 0)
    stock = 4  # squared norms of these two blocks at the half-stock point
    for speed in (Q(2, 3), Q(0)):
        record_flux = 2 * speed * sum(a*b for a,b in zip(pure_odd, pure_odd))
        carrier_flux = -record_flux
        assert record_flux == speed*stock and record_flux + carrier_flux == 0

    for z in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        f = z*z/(1 + z*z)
        detuning = 1 - 2*f
        assert (1 + z*z)*detuning == 1 - z*z
        assert (1 if detuning > 0 else 0) == (1 if z < 1 else 0)
    print("625 exact pair-product and symmetry cases")
    print("Exact local and aggregate false triggers on mixed inputs")
    print("Pure odd balance, reciprocal flux, smooth Riccati and threshold controls passed")


if __name__ == "__main__":
    replay()
