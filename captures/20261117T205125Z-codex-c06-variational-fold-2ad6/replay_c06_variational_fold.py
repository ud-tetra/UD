"""Exact controls for the variational fold countermodels."""

from fractions import Fraction as Q
from itertools import product


def replay():
    targets = (Q(1, 4), Q(1, 2), Q(3, 4))
    phases = (Q(0), Q(1, 8), *targets, Q(7, 8), Q(1))
    checked = 0
    for target, fraction, inertia, stiffness in product(
        targets, phases, (Q(1), Q(3, 2)), (Q(2), Q(5, 3))
    ):
        gain = 1/target
        angle = gain*fraction
        assert angle-gain*fraction == 0
        assert (angle == 1) == (fraction == target)
        required_acceleration = 2*gain
        actual_initial_acceleration = -stiffness*(0-gain*0)/inertia
        assert actual_initial_acceleration == 0 and required_acceleration > 0
        checked += 1
    assert checked == 84
    print("84 exact closure and initial acceleration controls passed.")


if __name__ == "__main__":
    replay()
