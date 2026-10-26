# Finite native Cayley checkpoint certificate

Read THM534_FINITE_NATIVE_CAYLEY_CHECKPOINT_CERTIFICATE_v2.20.md for definitions, four theorems and proofs.

Verify the fixed witness from this directory:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_schedule.py
    PYTHONDONTWRITEBYTECODE=1 python3 verify_mutation_controls.py

The first command regenerates RESULTS.json and SIGNED_RECEIPTS.json exactly using the standard library. certificate_stdout.txt captures its constructor output. The second rejects three corrupted witnesses; it is an integrity control, not independent review.

SCHEDULE_CERTIFICATE.json specifies the complete ordered mask word and rational positive Cayley parameters. Rational q vectors certify errors; they are not reset states or alternative exact dynamics. SIGNED_RECEIPTS.json records exact q-trace signed ownership changes, cut defects and rigorous bounds for actual receipts.

Construction-only files: search_schedule.py (NumPy 2.3.5/SciPy 1.17.0), schedule_search.json and build_trace.py. To reconstruct a trace proposal from saved search results, run build_trace.py, then the exact verifier. To rerun the search, run search_schedule.py first. Floating search reruns may differ between environments; correctness rests on the fixed rational certificate, not optimizer reproducibility. Search termination and solver output are not trusted by the verifier.

No negative steps, isolated shared contacts, external algebraic reset or intermediate state replacement occur in the specified sequence. Full masked Cayley-map availability and an external mask/step programme are assumed. The map is implicit on the full two-cell carrier; no bounded-radius implementation theorem is claimed. The prepared feed and empty output roles are supplied. The result is target-dependent, one-preparation, approximate discrete-model transfer; it is not a target-blind native selector, continuous-flow word or action-unit derivation.

Development only. Independent review pending. Physical promotion: 0.
