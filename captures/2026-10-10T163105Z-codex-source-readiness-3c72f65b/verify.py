#!/usr/bin/env python3
"""Exact reduced-input ambiguity fixtures; no hidden physical trajectory claim."""
import itertools
import json
from pathlib import Path


def main():
    protocol = json.loads(Path(__file__).with_name("PROTOCOL.json").read_text())
    assert protocol["physical_promotion"] == 0
    factors = tuple(itertools.product((0, 1), repeat=2))
    assert len(factors) == 4
    assert {c * t for c, t in factors} == {0, 1}
    edge_pre = (1, 1)
    edge_completions = ((1, 1), (0, 1))
    edge_targets = {c * t for c, t in edge_completions}
    assert edge_targets == {0, 1}
    assert all(sum(pred != target for target in edge_targets) >= 1 for pred in (0, 1))

    pair_pre = (1, 1, 1)
    pair_endpoint_source = (1, 0)
    T, L = pair_endpoint_source
    pair_targets = {0, 1}
    assert pair_pre == (1, 1, 1) and T == 1 and L == 0
    assert all(T * L <= q <= T for q in pair_targets)
    assert all(sum(pred != target for target in pair_targets) >= 1 for pred in (0, 1))
    close = T * L
    hold = T * int(bool(pair_pre[2] or T * L))
    assert (close, hold) == (0, 1)

    result = {
        "status": "SOURCE_BLOCKED",
        "edge_reduced_input": {"C_prev": 1, "T_prev": 1, "event_descriptor": "unresolved primitive event"},
        "edge_admissible_completions": [list(x) for x in edge_completions],
        "edge_next_masks": sorted(edge_targets),
        "pair_reduced_input": {"pre": pair_pre, "source_endpoint": pair_endpoint_source, "receipt": "intact terminal sink"},
        "pair_admissible_responses": sorted(pair_targets),
        "pair_close_hold": [close, hold],
        "candidate_edge_constructor": None,
        "candidate_pair_response": None,
        "held_out_target_scored": False,
        "physical_promotion": 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
