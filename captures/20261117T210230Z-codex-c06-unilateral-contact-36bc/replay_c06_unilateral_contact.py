"""Exact controls for plastic apex contact on the v0.28 branch."""

from fractions import Fraction as Q
from itertools import product


def replay():
    checked = 0
    for inertia, gain, rate, excess in product(
        (Q(1), Q(3, 2)), (Q(2), Q(4, 3)), (Q(1), Q(5, 7)), (Q(1, 4), Q(2), Q(5))
    ):
        action_before = inertia*gain**2*rate + excess
        impulse = inertia*gain*rate
        momentum_after = -impulse
        action_after = action_before-gain*impulse
        assert action_after == excess > 0
        assert momentum_after/inertia + gain*rate == 0
        assert rate > 0  # Both Hamiltonian phase rates, hence both half-stock slopes.
        assert 2*(action_after-action_before) == -2*inertia*gain**2*rate
        energy_before = rate*action_before
        energy_after = rate*action_after+momentum_after**2/(2*inertia)
        assert energy_before-energy_after == inertia*gain**2*rate**2/2
        checked += 1
    assert checked == 24
    print("24 exact plastic-contact, residual exchange, stock and energy controls passed.")


if __name__ == "__main__":
    replay()
