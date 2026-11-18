"""Exact controls for the C06 v0.47 collective reservation candidate."""

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import permutations, product


FACES = tuple(range(4))
RELABELINGS = tuple(permutations(FACES))
PASS = (True, True)


@dataclass(frozen=True)
class Operation:
    cell: str
    epoch: int
    donor: str
    archive: str
    cut_map: tuple[tuple[int, ...], ...]
    guard: str
    metric_binding: str = "canonical"


@dataclass(frozen=True)
class Receipt:
    operation: Operation
    revision: int
    face: int
    closure: bool
    integrity: bool


@dataclass(frozen=True)
class Decision:
    mode: str
    vetoes: frozenset[tuple[int, str]] = frozenset()


def evaluate(operation, revision, roster, receipts, first_root):
    """Evaluate an authoritative common snapshot for one frozen roster."""
    if not roster:
        return Decision("pending")
    accepted = {}
    for receipt in receipts:
        if (
            receipt.operation != operation
            or receipt.revision != revision
            or receipt.face not in roster
        ):
            return Decision("pending")
        if accepted.setdefault(receipt.face, receipt) != receipt:
            return Decision("pending")
    if accepted.keys() != roster:
        return Decision("pending")

    vetoes = frozenset(
        (face, cause)
        for face, receipt in accepted.items()
        for cause, passed in (
            ("closure", receipt.closure),
            ("integrity", receipt.integrity),
        )
        if not passed
    )
    if vetoes:
        return Decision("abort", vetoes)
    return Decision("held" if first_root else "continue")


def commit(reservation, decision):
    """Model one atomic token update. False in both slots means reciprocal cut."""
    if reservation != ("armed", True, True):
        return reservation
    if decision.mode in ("abort", "held"):
        return decision.mode, False, False
    return reservation


def joint_target(roster, bindings):
    if not roster:
        return None
    targets = {bindings[face] for face in roster}
    return next(iter(targets)) if len(targets) == 1 else None


def run():
    operation = Operation("k4", 3, "donor-A", "archive-A", ((0, -1), (1, 0)), "first-directed")
    revision = 17
    roster = frozenset(FACES)
    armed = ("armed", True, True)
    states = tuple(product((False, True), repeat=2))
    typed_words = set()
    equivariance_count = 0
    order_count = 0
    idempotence_count = 0
    for flags in product(states, repeat=len(FACES)):
        receipts = tuple(
            Receipt(operation, revision, face, closure, integrity)
            for face, (closure, integrity) in zip(FACES, flags)
        )
        result = evaluate(operation, revision, roster, receipts, True)
        typed_words.add(result.vetoes)
        assert all(closure and integrity for closure, integrity in flags) == (not result.vetoes)
        # The only way to reach Held is that all factors pass at the root.
        assert result.mode == ("abort" if result.vetoes else "held")
        for at_root in (False, True):
            expected = evaluate(operation, revision, roster, receipts, at_root)
            assert expected.mode == ("abort" if result.vetoes else ("held" if at_root else "continue"))
            terminal = commit(armed, expected)
            if expected.mode in ("abort", "held"):
                assert terminal == (expected.mode, False, False)
                for new_decision in (Decision("held"), Decision("abort")):
                    assert commit(terminal, new_decision) == terminal
                    idempotence_count += 1
            else:
                assert terminal == armed
            for ordering in RELABELINGS:
                permuted = tuple(receipts[i] for i in ordering)
                assert evaluate(operation, revision, roster, permuted, at_root) == expected
                assert evaluate(operation, revision, roster, permuted + (permuted[0],), at_root) == expected
                order_count += 2
                renamed = tuple(replace(receipt, face=ordering[receipt.face]) for receipt in receipts)
                renamed_vetoes = frozenset((ordering[face], cause) for face, cause in expected.vetoes)
                assert evaluate(operation, revision, roster, renamed, at_root) == Decision(expected.mode, renamed_vetoes)
                equivariance_count += 1
    assert len(typed_words) == 4 ** len(FACES)

    all_clear = tuple(Receipt(operation, revision, face, *PASS) for face in FACES)
    changed_epoch = replace(operation, epoch=4)
    changed_register = replace(operation, donor="donor-B")
    changed_metric = replace(operation, metric_binding="rescaled joint metric")
    distinct_operations = (changed_epoch, changed_register, changed_metric)
    assert all(operation.cut_map == other.cut_map for other in distinct_operations)
    assert joint_target(roster, dict.fromkeys(roster, operation)) == operation
    for incompatible in distinct_operations:
        bindings = dict.fromkeys(roster, operation)
        bindings[0] = incompatible
        assert joint_target(roster, bindings) is None
    bad_receipt = replace(all_clear[0], closure=False)
    rejected_batches = (
        all_clear[1:],
        (replace(all_clear[0], revision=revision - 1),) + all_clear[1:],
        (replace(all_clear[0], revision=revision + 1),) + all_clear[1:],
        (replace(all_clear[0], operation=changed_epoch),) + all_clear[1:],
        (replace(all_clear[0], operation=changed_register),) + all_clear[1:],
        (replace(all_clear[0], operation=changed_metric),) + all_clear[1:],
        (replace(all_clear[0], face=4),) + all_clear[1:],
        all_clear + (bad_receipt,),
    )
    for rejected in rejected_batches:
        assert evaluate(operation, revision, roster, rejected, True) == Decision("pending")
    assert evaluate(operation, revision, roster, all_clear, True).mode == "held"
    assert evaluate(operation, revision, roster, (bad_receipt,) + all_clear[1:], True) == Decision(
        "abort", frozenset({(0, "closure")})
    )
    two_vetoes = (replace(bad_receipt, integrity=False),) + all_clear[1:]
    assert evaluate(operation, revision, roster, two_vetoes, True) == Decision(
        "abort", frozenset({(0, "closure"), (0, "integrity")})
    )

    # Faces are indexed by omitted vertex. The signed witness fixes no face.
    potential = (1, 1, -1, -1)
    negative = tuple(-value for value in potential)
    signed = [g for g in RELABELINGS if tuple(potential[g[v]] for v in FACES) == potential]
    ray = [g for g in RELABELINGS if tuple(potential[g[v]] for v in FACES) in (potential, negative)]
    for group, order, orbit_size in ((signed, 4, 2), (ray, 8, 4)):
        assert len(group) == order
        assert all(len({g[face] for g in group}) == orbit_size for face in FACES)

    # Freeze identity is checked in exact rational coordinates.
    stock_cases = 0
    for donor, archive in ((1, 0), (Fraction(4, 5), Fraction(3, 5)), (Fraction(3, 5), Fraction(4, 5)), (0, 1)):
        for scale in (1, 2, 3):
            before = (scale * donor, scale * archive)
            assert sum(value * value for value in before) == scale * scale
            cut = commit(armed, Decision("abort", frozenset({(0, "closure")})))
            assert cut == ("abort", False, False)
            for post_cut_phase in (Fraction(0), Fraction(1, 4), Fraction(9, 7)):
                _, forward, reverse = cut
                after = (
                    before[0] - reverse * post_cut_phase * before[1],
                    before[1] + forward * post_cut_phase * before[0],
                )
                assert after == before
                assert sum(value * value for value in after) == scale * scale
                stock_cases += 1
    # If history is hidden until after the root, identical visible inputs can
    # conceal a same-revision veto. This is a model-level witness only.
    visible = all_clear[1:]
    assert evaluate(operation, revision, roster, visible, True).mode == "pending"
    assert evaluate(operation, revision, roster, visible + (all_clear[0],), True).mode == "held"
    assert evaluate(operation, revision, roster, visible + (bad_receipt,), True).mode == "abort"

    print(f"{len(typed_words)} distinct typed factor states and {equivariance_count} relabeling comparisons passed.")
    print(f"{order_count} receipt order and duplicate controls and {idempotence_count} terminal retry controls passed.")
    print(f"{len(rejected_batches)} incomplete, stale, foreign or conflicting batches withheld. {len(distinct_operations)} equal-matrix distinct-operation controls passed.")
    print(f"{stock_cases} exact reciprocal abort stock controls passed. Signed and ray stabilizer orders 4 and 8 verified.")
    print("The delayed same-root veto witness distinguishes a complete all-pass snapshot from an incomplete root prefix.")


if __name__ == "__main__":
    run()
