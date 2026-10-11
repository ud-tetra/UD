#!/usr/bin/env python3
"""Exact bit-mask audit of the v0.2.1 guard's frame-alignment dependency."""
import itertools
import json

PAIRS = range(3)
PERMS = tuple(itertools.permutations(PAIRS))


def permute(mask, permutation):
    return sum(((mask >> p) & 1) << permutation[p] for p in PAIRS)


def endpoint(seat):
    return seat ^ 7


def main():
    totals = {"admitted": 0, "identity_admitted": 0,
              "nonidentity_admitted": 0, "naive_event_mismatch": 0,
              "correct_no_change": 0, "correct_switch": 0,
              "zero_index_switch": 0, "covariance_failures": 0}
    witness = None
    for permutation in PERMS:
        for raw_theta in range(8):
            aligned_theta = permute(raw_theta, permutation)
            for seat in range(8):
                for integrity in range(8):
                    if seat & (~integrity & 7):
                        continue
                    totals["admitted"] += 1
                    totals["identity_admitted" if permutation == (0, 1, 2)
                           else "nonidentity_admitted"] += 1
                    theta_plus = endpoint(seat)
                    correct_toggle = aligned_theta ^ theta_plus
                    naive_toggle = raw_theta ^ theta_plus
                    correct_switch = correct_toggle != 0
                    naive_switch = naive_toggle != 0
                    totals["correct_switch" if correct_switch else "correct_no_change"] += 1
                    mu = theta_plus.bit_count() - aligned_theta.bit_count()
                    if correct_switch and mu == 0:
                        totals["zero_index_switch"] += 1
                    if correct_switch != naive_switch:
                        totals["naive_event_mismatch"] += 1
                        if witness is None:
                            witness = {"permutation": permutation,
                                       "raw_theta_minus": raw_theta,
                                       "aligned_theta_minus": aligned_theta,
                                       "output_seat_mask": seat,
                                       "integrity_mask": integrity,
                                       "theta_plus": theta_plus,
                                       "correct_toggle": correct_toggle,
                                       "naive_toggle": naive_toggle,
                                       "mu": mu}
                    # Rebase the entire typed packet into another output frame.
                    for relabel in PERMS:
                        lhs = permute(correct_toggle, relabel)
                        rhs = permute(aligned_theta, relabel) ^ endpoint(
                            permute(seat, relabel))
                        if lhs != rhs:
                            totals["covariance_failures"] += 1
    assert totals["admitted"] == 6 * 8 * 27
    assert totals["identity_admitted"] == 8 * 27
    assert totals["naive_event_mismatch"] > 0
    assert totals["covariance_failures"] == 0
    # A minimal frame-only window that should not become a Theta event.
    raw_theta, frame, seat, integrity = 1, (1, 0, 2), 5, 7
    aligned = permute(raw_theta, frame)
    assert aligned == 2 and endpoint(seat) == 2
    assert aligned ^ endpoint(seat) == 0
    assert raw_theta ^ endpoint(seat) == 3
    print(json.dumps({"scope": "six S3 pair-frame actions, all raw three-bit states,"
                               " all coordinate seats and integrity masks",
                      "totals": totals, "first_mismatch_witness": witness,
                      "explicit_frame_only_witness": {
                          "raw_theta_minus": raw_theta,
                          "frame_permutation": frame,
                          "aligned_theta_minus": aligned,
                          "theta_plus": endpoint(seat),
                          "correct_event": False,
                          "naive_raw_comparison_event": True}}, indent=2))


if __name__ == "__main__":
    main()
