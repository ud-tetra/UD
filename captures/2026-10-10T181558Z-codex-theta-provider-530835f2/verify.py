#!/usr/bin/env python3
"""Exact finite compatibility audit; the historical selector stays a candidate."""
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


old = load("historical_selector", "historical_selector_source.py")
new = load("phase23_receipt", "phase23_receipt_source.py")


def inverse(perm):
    return tuple(perm.index(i) for i in range(3))


def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def main():
    binary = tuple(itertools.product((0, 1), repeat=3))
    signed = tuple(itertools.product((-1, 0, 1), repeat=3))
    burdens = tuple(itertools.product((0, 1, 2), repeat=3))
    perms = tuple(itertools.permutations(range(3)))
    counts = Counter()
    witnesses = {}
    cases = 0
    source_receipt_checks = 0
    for theta, integrity, G, W in itertools.product(binary, binary, signed, burdens):
        for pi in perms:
            # The historical implementation sends source coordinate i to pi[i].
            # Phase 23 reads output coordinate j from input coordinate p[j].
            p = inverse(pi)
            y = old.permute(theta, pi)
            assert new._permute(theta, p) == y
            data = tuple(old.permute(x, pi) for x in (integrity, G, W))
            after, branch, addresses = old.select(y, *data)
            xi = xor(y, after)
            assert xor(new._permute(theta, p), xi) == after
            weight = sum(xi)
            assert weight == (1 if branch in ("closure", "reopen") else
                              2 if branch == "swap" else 0)
            if branch == "closure":
                assert sum(after) - sum(y) == 1
            if branch == "reopen":
                assert sum(after) - sum(y) == -1
            if branch == "swap":
                assert sum(after) == sum(y) and addresses is not None
            if branch.endswith("hold"):
                assert xi == (0, 0, 0) and after == y
                # A missing event receipt preserves the *local* Theta.
                if y != theta:
                    counts["hold_relabel_mismatch"] += 1
                    witnesses.setdefault("hold_relabel", {
                        "theta": theta, "historical_perm": pi,
                        "phase23_perm": p, "y": y, "branch": branch})
            counts[branch] += 1
            cases += 1
            # The sourced receipt code is checked on a fixture from each
            # branch and each permutation; these are synthetic candidate
            # outputs, NOT provenance-bound native event observations.
            key = (branch, pi)
            if key not in witnesses:
                receipt = new.make_receipt(
                    provider_id="synthetic_candidate_probe", event_id=str(cases),
                    theta_prev=theta, pair_permutation=p, flip_mask=xi,
                    context_note="compatibility_only")
                out = new.apply_receipt(receipt, theta_prev=theta,
                                        pair_permutation=p,
                                        context_note="compatibility_only")
                assert out.status == "APPLIED" and out.theta_next == after
                assert out.pair_closures - out.pair_reopenings == sum(after) - sum(y)
                assert out.pair_closures + out.pair_reopenings == weight
                if weight == 0:
                    absent = new.apply_optional_receipt(None, theta_prev=theta,
                                                        pair_permutation=p)
                    assert absent.status == "THETA_UPDATE_DEFERRED"
                    assert absent.theta_next == theta
                witnesses[key] = True
                source_receipt_checks += 1
    assert cases == 8 * 8 * 27 * 27 * 6 == 279936
    assert sum(counts[x] for x in ("closure", "reopen", "swap",
                                   "closure_hold", "reopen_hold", "swap_hold")) == cases
    assert counts["hold_relabel_mismatch"] > 0
    assert source_receipt_checks == 6 * 6
    # A 3-cycle makes the two conventions genuinely unequal.
    pi = (1, 2, 0)
    theta = (1, 0, 0)
    assert old.permute(theta, pi) == new._permute(theta, inverse(pi))
    assert old.permute(theta, pi) != new._permute(theta, pi)
    # Exact fixed-structure null from the prior K4 native-flow capture:
    # source stock drains but no closure receipt or local edge map changes.
    static_G = (Fraction(-1), Fraction(-1, 2), Fraction(-1, 2))
    static_theta = (0, 0, 0)
    proposed, static_branch, _ = old.select(static_theta, (1, 1, 1),
                                             static_G, (0, 0, 0))
    assert static_branch == "closure" and proposed == (1, 0, 0)
    structural_theta_after = static_theta
    assert proposed != structural_theta_after
    print(json.dumps({
        "status": "EXACT conditional interface compatibility / no endogenous xi source",
        "synthetic_candidate_frame_cases": cases,
        "source_receipt_fixtures": source_receipt_checks,
        "branch_counts": {x: counts[x] for x in ("closure", "reopen", "swap",
                            "closure_hold", "reopen_hold", "swap_hold")},
        "hold_cases_where_missing_receipt_differs_from_zero_flip_relabel":
            counts["hold_relabel_mismatch"],
        "hold_relabel_witness": witnesses["hold_relabel"],
        "fixed_structure_native_null_candidate_disagrees": True,
        "independent_event_histories_scored": 0,
        "physical_promotion": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
