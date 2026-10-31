# UD PRED-01/PRED-02 v0.3.1 — Typed numerical replay amendment

**Date:** 2026-10-31. **Status:** operational verification repair, no scientific law amended. Physical promotion **0**. Original v0.3 capture and its failed GitHub CI run are preserved.

## Failure record

GitHub PR #477 first replay (Actions run `41233551013`) passed all 36 mathematical test cases but the bytewise comparison `cmp /tmp/ud_pred_v03_replay.json captures/.../RESULTS.json` failed at file byte 34543, line 2379. The corresponding field is `relaxation.final_distance_to_n3`, calculated with platform-sensitive floating linear algebra. Byte-for-byte floating equality across runner platforms is not an appropriate test of a numerical eigensolve, even with pinned Python packages.

This is a verification-contract failure, **not** evidence of either physical confirmation or a mathematical counterexample. Exact rational, combinatorial, topology and response schedule fields remain subject to exact value comparison.

## Typed correction

The new `compare_replay.py` recursively verifies equal JSON types, identical keys, ordered arrays, and exact values for every non-`relaxation` field. Within only the declared `relaxation` subtree, finite floating values are compared using relative tolerance \(10^{-9}\) and absolute tolerance \(10^{-10}\). It rejects extra keys, changed integer Betti numbers, altered response schedules, nonfinite values, and materially changed numerical eigenvalues or residuals. It reports actual maximum absolute and relative drift.

This tolerance is **computational reproducibility**, not a physical error bar or a claim that the model is empirically calibrated. A distinct numerical method or unvalidated platform cannot use it to promote an observable.

## Verification

Eight comparator unit tests check identical replay, controlled small drift, wrong exact topology, altered schedule, type mismatch, nonfinite float, extra field and large numerical drift. The original 36 tests remain unchanged. On GitHub CI the workflow compares saved/recomputed v0.3 data using this standalone comparator rather than rewriting the frozen `RESULTS.json`.

## Source governance

This is an append-only v0.3.1 correction capture with a new event. No v0.3 file content, source theorem, historical negative result or physical promotion changes. Non-constructor review remains deferred, not waived.
