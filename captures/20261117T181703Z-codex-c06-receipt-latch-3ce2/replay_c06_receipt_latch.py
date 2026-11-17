"""Exact controls for C06 receipt sufficiency and continuous finite-time hold."""

from fractions import Fraction as Q
from itertools import permutations, product


def replay():
    edges = ({0, 1}, {0, 2}, {0, 3})
    witnesses = [(7, 1), (5, 5), (1, 7)]
    assert all(u*u + v*v == 50 for u, v in witnesses)
    assert [v*v-u*u for u, v in witnesses] == [-48, 0, 48]
    assert [Q(v*v, 50) for u, v in witnesses] == [Q(1, 50), Q(1, 2), Q(49, 50)]
    labels = tuple(product((0, 1), repeat=3))
    cases = 0
    for frame in permutations(range(4)):
        action = tuple(next(i for i, edge in enumerate(edges)
                            if image == edge or image.isdisjoint(edge))
                       for image in ({frame[v] for v in pair} for pair in edges))
        assert sorted(action) == [0, 1, 2]
        for offset in labels:
            outputs = set()
            for before in labels:
                pushed = tuple(before[action.index(i)] for i in range(3))
                after = tuple(a ^ b for a, b in zip(offset, pushed))
                assert tuple(a ^ b for a, b in zip(after, pushed)) == offset
                outputs.add(after)
                assert any(v*v == u*u for u, v in witnesses)
                assert any(v*v != u*u for u, v in witnesses)
                cases += 1
            assert len(outputs) == 8
    assert cases == 1536

    # Same stock and receipt at the event, distinct post-event actuators.
    u = v = 5
    assert [4 * a * u * v for a in (Q(1, 2), Q(0))] == [50, 0]
    for rate, time in product((Q(1, 2), Q(1), Q(3, 2)), (Q(i, 4) for i in range(17))):
        root = max(Q(0), 1-rate*time/2)
        z = 1-root**2
        a = rate*root/(1+z*z)
        assert a*(1+z*z) == rate*root
        assert (z == 1) == (time >= 2/rate)
        assert (a == 0) == (z == 1)
    print("1,536 exact frame/offset/input-label controls; identical receipts admit all three balances.")
    print("Exact switch/continue and continuous non-Lipschitz finite-time controls passed.")


if __name__ == "__main__":
    replay()
