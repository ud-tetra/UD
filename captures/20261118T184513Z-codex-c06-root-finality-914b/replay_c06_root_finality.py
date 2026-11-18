"""Exact controls for C06 root-time veto finality and its conditional comparator."""

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import permutations, product


FACES = tuple(range(4))
CAUSES = ("closure", "integrity")
PREDICATES = tuple(product(FACES, CAUSES))
FULL_MASK = (1 << len(PREDICATES)) - 1


def verify_observation_fibers():
    """A visible pass/fail word is a partial function on the predicate roster."""
    fibers = {}
    for visible_mask in range(FULL_MASK + 1):
        for world in range(FULL_MASK + 1):
            observation = visible_mask, world & visible_mask
            fibers.setdefault(observation, set()).add(world)

    coarse_ambiguous = 0
    typed_ambiguous = 0
    for (visible_mask, failures), worlds in fibers.items():
        modes = {"abort" if world else "held" for world in worlds}
        can_complete = len(modes) == 1
        complete_typed_record = len(worlds) == 1

        # This characterization is for the unrestricted independent-bit model.
        assert can_complete == (bool(failures) or visible_mask == FULL_MASK)
        assert complete_typed_record == (visible_mask == FULL_MASK)
        coarse_ambiguous += not can_complete
        typed_ambiguous += not complete_typed_record

    assert len(fibers) == 3 ** len(PREDICATES)
    assert coarse_ambiguous == FULL_MASK
    assert typed_ambiguous == len(fibers) - (FULL_MASK + 1)

    # Restricted admissibility can determine an unobserved predicate.
    correlated_fibers = {}
    for world in (0b00, 0b11):
        correlated_fibers.setdefault(world & 0b01, set()).add(world)
    assert all(len(worlds) == 1 for worlds in correlated_fibers.values())
    return len(fibers), coarse_ambiguous, typed_ambiguous


@dataclass(frozen=True)
class Operation:
    cell: str
    epoch: int
    loader: str
    metric: str


@dataclass(frozen=True)
class Root:
    operation: Operation
    revision: int
    first_directed: bool


@dataclass(frozen=True)
class RootSeal:
    """Reference marker for a source-authoritative immutable pre-cut read."""

    root: Root
    failures: frozenset[tuple[int, str]]
    roster: frozenset[tuple[int, str]]


@dataclass(frozen=True)
class Reservation:
    operation: Operation
    mode: str = "ready"
    forward: bool = True
    reverse: bool = True
    failures: frozenset[tuple[int, str]] = frozenset()


def cut(reservation, root, seal, authority):
    """A declared atomic transaction using the live, sealed decision state."""
    if (
        not authority
        or reservation.mode != "ready"
        or reservation.operation != root.operation
        or seal is None
        or seal.root != root
        or not root.first_directed
        or seal.roster != frozenset(PREDICATES)
        or not seal.failures <= seal.roster
    ):
        return reservation
    return Reservation(
        root.operation,
        "abort" if seal.failures else "held",
        False,
        False,
        seal.failures,
    )


def verify_root_controls():
    operation = Operation("K4", 5, "reciprocal-A", "metric-A")
    root = Root(operation, 17, True)
    roster = frozenset(PREDICATES)
    ready = Reservation(operation)
    clear = RootSeal(root, frozenset(), roster)

    relabelings = tuple(permutations(FACES))
    raw_read_collisions = 0
    for labels in relabelings:
        gathered = tuple((face, cause) for face in labels for cause in CAUSES)
        visible = tuple((key, True, root.revision) for key in gathered)
        for failed_key in gathered:
            # The two histories share labels. One failure becomes live
            # immediately after that predicate's read, before the root commit.
            root_truth_fail = dict.fromkeys(gathered, True)
            failed_history = []
            for key in gathered:
                failed_history.append((key, root_truth_fail[key], root.revision))
                if key == failed_key:
                    root_truth_fail[key] = False
            assert tuple(failed_history) == visible
            assert not root_truth_fail[failed_key]
            assert cut(ready, root, None, True) == ready
            assert cut(ready, root, clear, True).mode == "held"
            failed_seal = RootSeal(root, frozenset({failed_key}), roster)
            aborted = cut(ready, root, failed_seal, True)
            assert (aborted.mode, aborted.failures) == ("abort", frozenset({failed_key}))
            assert not aborted.forward and not aborted.reverse
            raw_read_collisions += 1

    complete_modes = set()
    for word in range(FULL_MASK + 1):
        failures = frozenset(key for i, key in enumerate(PREDICATES) if word & (1 << i))
        seal = RootSeal(root, failures, roster)
        terminal = cut(ready, root, seal, True)
        assert terminal.mode == ("abort" if failures else "held")
        assert terminal.failures == failures
        assert not terminal.forward and not terminal.reverse
        assert cut(terminal, root, clear, True) == terminal
        complete_modes.add((terminal.mode, terminal.failures))
    assert len(complete_modes) == FULL_MASK + 1

    other_epoch = replace(root, operation=replace(operation, epoch=6))
    other_loader = replace(root, operation=replace(operation, loader="reciprocal-B"))
    other_metric = replace(root, operation=replace(operation, metric="metric-B"))
    wrong_root_direction = replace(root, first_directed=False)
    invalid = (
        (root, clear, False),
        (root, replace(clear, root=replace(root, revision=16)), True),
        (root, replace(clear, root=replace(root, revision=18)), True),
        (root, replace(clear, root=other_epoch), True),
        (root, replace(clear, root=other_loader), True),
        (root, replace(clear, root=other_metric), True),
        (wrong_root_direction, replace(clear, root=wrong_root_direction), True),
        (root, replace(clear, roster=roster - {(2, "closure")}), True),
        (root, replace(clear, failures=frozenset({(4, "closure")})), True),
    )
    for observed_root, observed_seal, authority in invalid:
        assert cut(ready, observed_root, observed_seal, authority) == ready

    # Two independent failures on one contact are retained. Abort-first
    # precedence at the requested root is a declared model convention.
    simultaneous = frozenset({(2, "closure"), (2, "integrity")})
    tied = cut(ready, root, replace(clear, failures=simultaneous), True)
    assert tied.mode == "abort" and tied.failures == simultaneous
    return raw_read_collisions, len(complete_modes), len(invalid)


def verify_drift_controls():
    # Exact rational rotations. The named pair is (sin(delay), cos(delay)).
    rotations = (
        (Fraction(0), Fraction(1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(4, 5), Fraction(3, 5)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    count = 0
    for scale, (sine, cosine) in product((1, 2, 3), rotations):
        root = (0, scale)
        paused = root
        active = (-scale * sine, scale * cosine)
        initial_stock = scale * scale
        assert sum(x * x for x in active) == initial_stock
        assert sum(x * x for x in paused) == initial_stock
        assert active[0] ** 2 / initial_stock == sine ** 2
        assert paused[0] ** 2 == 0
        count += 1
    assert rotations[-1][0] == 0 and rotations[-1][1] < 0
    return count


if __name__ == "__main__":
    fibers, coarse, typed = verify_observation_fibers()
    collisions, sealed, withheld = verify_root_controls()
    drift = verify_drift_controls()
    print(f"{fibers} observation fibers checked: {coarse} ambiguous for Held/Abort, {typed} for the full typed record.")
    print(f"{collisions} raw-read collisions distinguished using a final common snapshot; {sealed} sealed terminal states passed.")
    print(f"{withheld} invalid authority, scope, revision, root or roster controls withheld the cut; same-root typed tie and duplicate cut controls passed.")
    print(f"{drift} exact active-delay and guarded-pause stock controls passed, including a nonzero phase delay with donor recurrence.")
