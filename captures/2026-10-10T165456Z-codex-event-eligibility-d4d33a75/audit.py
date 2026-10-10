#!/usr/bin/env python3
"""Retrospective qualification of a generated UD history archive for OP03 polarity."""
import hashlib
import json
import sys
import zipfile
from fractions import Fraction

EXPECTED_ARCHIVE_SHA256 = "85d41c897e2f846387eb59c36641b796d1be44f77a246aae67025d7003d18da7"
EXPECTED_FILES = {
    "UD_GENERATED_HISTORY_RESULTS_v0.1.json",
    "verify_generated_history_v0_1.py",
    "UD_GENERATED_HISTORY_PERSISTENCE_AUDIT_v0.1.md",
}


def score(b):
    pairs = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
    return tuple(sum((b[i] - b[j]) ** 2 for i, j in pair) for pair in pairs)


def qualify(path):
    blob = open(path, "rb").read()
    archive_sha = hashlib.sha256(blob).hexdigest()
    assert archive_sha == EXPECTED_ARCHIVE_SHA256, "different archive/version: requalify explicitly"
    with zipfile.ZipFile(path) as z:
        assert EXPECTED_FILES <= set(z.namelist())
        data = json.loads(z.read("UD_GENERATED_HISTORY_RESULTS_v0.1.json"))
        program = z.read("verify_generated_history_v0_1.py").decode()
    assert data["run_count"] == 2052 and data["step_count"] == 65664
    assert data["counts"]["SWAP"] == 12171
    assert len(data["representative_traces"]) == 6
    # The target label is assigned by the generator's own selector. This is
    # retrospective code provenance, not a blind check of an independent target.
    assert "after,event,gain=select(state,theta,history=selected)" in program
    assert "'theta_after':after[:]" in program
    assert "state,theta=ns,after" in program
    assert "W=score(b)if history is None" in program
    assert "def select(b,theta,integrity=True,history=None):" in program
    assert "signed_pair_source" not in program and "G_Sigma" not in program
    audited = swaps = 0
    for rep in data["representative_traces"]:
        trace = rep["trace"]
        assert len(trace) == 32
        for i, rec in enumerate(trace):
            audited += 1
            before, after = rec["theta_before"], rec["theta_after"]
            assert sum(before) == sum(after) == 1
            assert "G_Sigma" not in rec and "signed_pair_source" not in rec
            burden = tuple(Fraction(x) for x in rec["burden_before"])
            current_scores = score(burden)
            assert tuple(Fraction(x) for x in rec["current_scores"]) == current_scores
            assert after == before or (
                sum(a != b for a, b in zip(after, before)) == 2
                and rec["event"] == "SWAP")
            swaps += rec["event"] == "SWAP"
            if i:
                prev = trace[i - 1]
                assert prev["theta_after"] == before
                assert prev["burden_after"] == rec["burden_before"]
    return {
        "status": "INELIGIBLE_FOR_OP03_POLARITY_TARGET_BLIND_TEST",
        "archive_sha256": archive_sha,
        "source_archive": "UD_GENERATED_HISTORY_v0.1_RELEASE.zip",
        "generator_runs_reported": data["run_count"],
        "generator_steps_reported": data["step_count"],
        "generator_swaps_reported": data["counts"]["SWAP"],
        "available_full_representative_traces": len(data["representative_traces"]),
        "representative_steps_rechecked": audited,
        "representative_swaps": swaps,
        "all_representatives_fixed_hamming_one": True,
        "signed_G_Sigma_present": False,
        "target_generated_by_own_selector": True,
        "independent_primitive_receipt_outcome_present": False,
        "discriminating_polarity_target_scored": False,
        "physical_promotion": 0,
    }


if __name__ == "__main__":
    print(json.dumps(qualify(sys.argv[1]), indent=2, sort_keys=True))
