"""Exact controls for odd-stock event authorization."""

from itertools import product


def transition(mode, origin, carrier, record):
    """Test the declared Ready/Hold contract on scalar aligned odd states."""
    balance = record**2 - carrier**2
    inward = 2 * carrier * record
    if mode == "Ready" and origin == "direct guard" and balance == 0 and inward > 0:
        return "Hold", True, (carrier, record)
    return mode, False, (carrier, record)


def replay():
    witnesses = [(7, 1), (5, 5), (1, 7)]
    assert [v**2-u**2 for u, v in witnesses] == [-48, 0, 48]
    assert [2*u*v for u, v in witnesses] == [14, 50, 14]
    assert all(u*u+v*v == 50 for u, v in witnesses)
    for u, v in product(range(-7, 8), repeat=2):
        assert u*u + v*v - 2*u*v == (u-v)**2
    assert 2 * 0 * 5 == 0 and 5**2 - 0**2 == 25

    states = witnesses + [(5, -5), (0, 0), (0, 5)]
    tested = 0
    for mode, origin, (u, v) in product(
        ("Ready", "Hold"), ("direct guard", "unrelated", "supplied tag"), states
    ):
        after, fired, amplitudes = transition(mode, origin, u, v)
        expected = (mode, origin, u, v) == ("Ready", "direct guard", 5, 5)
        assert fired == expected
        assert after == ("Hold" if expected else mode)
        assert amplitudes == (u, v)
        if fired:
            assert not transition(after, origin, *amplitudes)[1]
        tested += 1
    assert tested == 36
    print("Exact balances and fluxes; 225 maximum-flux controls; 36 authorization cases passed.")


if __name__ == "__main__":
    replay()
