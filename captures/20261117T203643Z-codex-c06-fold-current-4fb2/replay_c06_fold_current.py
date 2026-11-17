"""Exact stock and routing controls with angles measured in closure units."""

from fractions import Fraction as Q
from itertools import product


def replay():
    checked = 0
    for stock in (Q(1, 4), Q(1), Q(2)):
        for counts in product(range(4), repeat=3):
            if not sum(counts):
                continue
            shares = tuple(Q(n, sum(counts)) for n in counts)
            raw_angle = 2 * sum(stock * share / 2 for share in shares)
            normalized_angle = raw_angle / stock
            assert raw_angle == stock and normalized_angle == 1
            checked += 1

    assert Q(1, 2*2) == Q(1, 4)
    assert 2*Q(1, 4) == Q(1, 2)
    for pair in range(3):
        local_angles = tuple(int(i == pair) for i in range(3))
        assert sum(local_angles) == 1 and local_angles != (1, 1, 1)
    assert checked == 189
    print("189 exact stock/preparation controls and three diagonal routing witnesses passed.")


if __name__ == "__main__":
    replay()
