#!/usr/bin/env python3
"""Finite counterexample audit for contrast as a universal event-ready gate."""
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, file):
    import sys
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


selector = load("historical_selector", "historical_selector_source.py")
event = load("phase23_event", "phase23_receipt_source.py")


def contrast_square(W):
    # The ledger Q20 delta_i = W_i - mean(W); scale by 9 for integers.
    total = sum(W)
    return sum((3 * x - total) ** 2 for x in W)


def main():
    bits = tuple(itertools.product((0, 1), repeat=3))
    signed = tuple(itertools.product((-1, 0, 1), repeat=3))
    weights = tuple(itertools.product((0, 1, 2), repeat=3))
    counts = Counter()
    for theta, T, G, W in itertools.product(bits, bits, signed, weights):
        after, branch, _ = selector.select(theta, T, G, W)
        counts["cases"] += 1
        if after != theta:
            counts["candidate_events"] += 1
        if contrast_square(W) == 0:
            assert W[0] == W[1] == W[2]
            counts["zero_contrast_cases"] += 1
            if after != theta:
                counts["candidate_events_vetoed_by_contrast"] += 1
                if sum(G) != 0:
                    counts["nonzero_source_events_vetoed_by_contrast"] += 1
    assert counts["cases"] == 46656
    assert counts["zero_contrast_cases"] == 8 * 8 * 27 * 3

    # Q20's equal-W static null: the signed source candidate selects A,
    # while the declared frozen structural state gives no gate transition.
    theta = (0, 0, 0)
    T = (1, 1, 1)
    W = (0, 0, 0)
    G = (Fraction(-1), Fraction(-1, 2), Fraction(-1, 2))
    after, branch, _ = selector.select(theta, T, G, W)
    assert contrast_square(W) == 0 and branch == "closure" and after == (1, 0, 0)
    frozen_structural_after = theta
    assert after != frozen_structural_after

    # A provenance-bound EXTERNAL receipt is admissible algebraically at the
    # same zero-contrast current values. This asserts no dynamical reachability.
    receipt = event.make_receipt(provider_id="synthetic_model_completion",
                                 event_id="zero_contrast_probe",
                                 theta_prev=theta, flip_mask=(1, 0, 0),
                                 provenance_note="formal interface only")
    applied = event.apply_receipt(receipt, theta_prev=theta)
    assert applied.status == "APPLIED" and applied.theta_next == (1, 0, 0)

    # Three-valued, source-safe *decision status*; it does not predict events.
    def scope_status(fixed_structure_certificate):
        return "VETO" if fixed_structure_certificate else "UNRESOLVED"

    assert scope_status(True) == "VETO"
    assert scope_status(False) == "UNRESOLVED"
    print(json.dumps({
        "status": "EXACT fixed-structure veto / contrast-positive trigger NO-GO as a universal rule",
        "counts": dict(counts),
        "static_null_excluded_by_contrast": True,
        "zero_contrast_external_receipt_algebraically_admitted": True,
        "positive_source_eligibility_derived": False,
        "independent_same_carrier_event_histories_scored": 0,
        "physical_promotion": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
