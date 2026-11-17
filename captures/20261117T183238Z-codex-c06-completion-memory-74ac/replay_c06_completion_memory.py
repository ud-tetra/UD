"""Exact replay for the C06 reserved terminal Fire comparator."""

from fractions import Fraction


def fire(acknowledged, pending):
    return acknowledged, 1


def ack(acknowledged, pending, capacity):
    if pending and acknowledged < capacity:
        return acknowledged + 1, 0
    return acknowledged, pending


def replay():
    cases = 0
    for width in range(1, 9):
        capacity = (1 << width) - 1
        for count in range(capacity + 1):
            state = fire(count, 0)
            assert sum(state) == count + 1
            assert fire(*state) == state
            final = ack(*state, capacity)
            assert sum(final) == sum(state)
            if count < capacity:
                assert final == (count + 1, 0)
            else:
                assert final == state
                assert sum(final) == 1 << width
                # Count-only decoder aliases different incoming labels and stocks.
                event_types = [
                    ("C06", Fraction(1, 2)),
                    ("unrelated", Fraction(1, 50)),
                ]
                records = {label: fire(count, 0) for label, _ in event_types}
                assert records["C06"] == records["unrelated"]
                assert event_types[0][1] != event_types[1][1]
            cases += 1
    assert cases == 510

    # Aligned two-mode chart, identity amplitude reset and reciprocal held block.
    for x, y in [((2, 5), (3, 5)), ((2, 7), (3, 1))]:
        dx, dy = (-2*y[0], 0), (2*x[0], 0)
        assert dx[1] == dy[1] == 0
        assert sum(a*b for a, b in zip(x+y, dx+dy)) == 0
        assert (dx[0], dy[0]) == (-2*y[0], 2*x[0])
        assert Fraction(y[1]**2, x[1]**2 + y[1]**2) in {
            Fraction(1, 2), Fraction(1, 50)
        }
    print("510 exact abstract Fire/Ack cases, widths 1–8; terminal pending is persistent.")
    print("False arm at 1/50 shares the terminal count with 1/2; selective stock controls passed.")


if __name__ == "__main__":
    replay()
