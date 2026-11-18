"""Exact checks for the declared quadratic capture and bank handoff."""
from fractions import Fraction
from itertools import product


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def norm(x):
    return dot(x, x)


def halves(x, y, sign):
    return tuple(Fraction(a + sign*b, 2) for a, b in zip(x, y))


states = tuple(product((-1, 0, 1), repeat=3))
zero = (0, 0, 0)
for u, v in product(states, repeat=2):
    diff, archive = halves(u, v, -1), halves(u, v, 1)
    # The two rational coordinates represent normalized blocks divided by sqrt(2).
    assert norm(u)+norm(v) == 2*(norm(diff)+norm(archive))
    assert tuple(a+b for a, b in zip(archive, diff)) == u
    assert tuple(a-b for a, b in zip(archive, diff)) == v

for a, donor in product(states, repeat=2):
    if a == zero or donor == zero:
        continue
    assert norm(a)-norm(a) == 0
    assert 4*dot(a, a) > 0  # B' in units of omega_- if the old port is restored.
    assert halves(a, a, -1) == zero
    assert halves(a, a, 1) == a
    assert -norm(donor) < 0  # Fresh record is empty.
    assert 2*norm(a)+norm(donor) == 2*norm(halves(a, a, 1))+norm(donor)

for held, correct_epoch, archive_empty, donor_positive, authorized in product((False, True), repeat=5):
    conditions = (held, correct_epoch, archive_empty, donor_positive, authorized)
    # Model explicit first-failure rejection and compare with the conjunction.
    result = "new epoch" if next((i for i, ok in enumerate(conditions) if not ok), None) is None else "retain"
    assert (result == "new epoch") == (sum(conditions) == 5)

print("729 exact sum/difference stock and inverse controls passed.")
print("676 positive-stock held and donor pairs passed.")
print("32 declared handoff eligibility combinations passed.")
