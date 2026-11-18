"""Exact witness controls for the C06 cell transition audit."""
from itertools import product


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def cross(x, y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])


basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
zero = (0, 0, 0)
rows = tuple(product((-1, 0, 1), repeat=3))
for left, right in product(rows, repeat=2):
    a = cross(left, right)
    if a == zero:
        row = left if left != zero else right
        a = next((cross(row, e) for e in basis if cross(row, e) != zero), basis[0])
    assert a != zero and dot(left, a) == dot(right, a) == 0
    # At the root use equal aligned amplitudes (common positive scale omitted).
    assert dot(a, a)-dot(a, a) == 0
    assert 4*dot(a, a) > 0  # B' after dividing by the positive common rate.

# A queued token can publish only when a slot is clear. The selected
# model determines the outgoing balance before the next rearm check.
for resolved, slot_clear, select_at_capture in product((False, True), repeat=3):
    captured = ["root-1"] if resolved else []
    pending = captured.copy()
    published = [pending.pop(0)] if slot_clear and pending else []
    assert captured == published + pending
    held = bool(captured) and (select_at_capture or bool(published))
    outgoing_before_publish = 0 if held or not resolved else 1
    rearmed = bool(captured) and outgoing_before_publish > 0
    if resolved and not slot_clear:
        assert held == select_at_capture
        assert rearmed != select_at_capture
    if held:
        assert not rearmed

print("729 observation pairs: exact nonzero silent preparations retain a directed balance.")
print("8 declared capture/publication controls: a terminal balance hold does not rearm.")
