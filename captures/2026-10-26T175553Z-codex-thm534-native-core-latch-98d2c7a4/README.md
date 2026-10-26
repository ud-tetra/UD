# Native core isolation and stopping audit

Read THM534_NATIVE_CORE_ISOLATION_AND_STOPPING_AUDIT_v2.21.md for the four theorems and proofs.

Run, in this capture directory:

    PYTHONDONTWRITEBYTECODE=1 python3 verify_parking.py
    PYTHONDONTWRITEBYTECODE=1 python3 verify_native_latch.py

The first regenerates RESULTS.json and SIGNED_RECEIPTS.json; the second regenerates LATCH_RESULTS.json. All checks use the Python standard library. parking_stdout.txt and latch_stdout.txt capture constructor runs.

SCHEDULE_CERTIFICATE.json contains the original 192-step v2.20 prefix, bound by its exact SHA-256, plus 64 parking steps. Rational trace vectors certify approximate execution; no checkpoint reset is applied. The original real metric and all native lower incidence contacts remain present.

The isolation theorem fixes four gates incident to the chosen existing output core, leaving eight possible full masks. It preserves that core under arbitrary subsequent positive Cayley steps and arbitrary other fields. It does not freeze the restored worker. Holding the chosen gate pattern and selecting its activation time are supplied controls. The theorem derives no core-role selection, readiness predicate, clock, latch record or physical gate hardware.

Construction-only files: search_parking.py, parking_search.json, build_parking_trace.py (NumPy 2.3.5, SciPy 1.17.0). The builder uses the first 192 trace entries already present in SCHEDULE_CERTIFICATE.json and recreates only its appended stage. Search reruns may differ across numerical environments; correctness rests on the fixed rational witness.

Negative controls: the old face-output checkpoint moves even with all gates off; opening any one isolation face can change the stored core; latching on first nonzero core occupancy fires prematurely. Start/end aliasing applies to a controller restricted to the first tetrahedron's field observation, not to every possible controller.

No imported historical scripts executed. Source snapshots and hashes are inventoried. Development only; independent review pending; physical promotion: 0.
