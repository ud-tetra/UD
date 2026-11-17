"""Exact finite-loading and hard-constraint controls."""

from fractions import Fraction as Q
from itertools import combinations, product


def replay():
    levels = (Q(0), Q(1, 48), Q(1, 2), Q(1), Q(10), Q(10**6))
    tested = 0
    for total, odd in product(range(-2, 3), repeat=2):
        x = (total + odd, total - odd)
        for weight in levels:
            residual = Q(odd)/(1+2*weight)
            drive = (total + residual, total - residual)
            assert tuple(d + weight*k for d, k in zip(drive, (2*residual, -2*residual))) == x
            assert (drive[0]-drive[1] != 0) == (odd != 0)
            tested += 1
        assert sum(x)/Q(2) == total

    indices = set(range(4))
    tested_subsets = 0
    for size in range(5):
        for observed in combinations(range(4), size):
            hidden = sorted(indices - set(observed))
            if size < 3:
                witness = [int(i == hidden[0])-int(i == hidden[1]) for i in range(4)]
                assert sum(witness) == 0 and any(witness)
                assert all(witness[i] == 0 for i in observed)
            else:
                assert len(hidden) <= 1
            tested_subsets += 1
    assert (tested, tested_subsets) == (150, 16)
    print("150 exact loading controls and all 16 constraint subsets passed.")


if __name__ == "__main__":
    replay()
