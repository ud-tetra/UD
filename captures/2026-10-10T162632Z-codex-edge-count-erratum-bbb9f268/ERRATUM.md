# UD edge receipt replay-count erratum v0.1.1

**10 October 2026 UTC · append-only correction to [v0.1](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-10T162352Z-codex-edge-receipt-9061c3ae).**

The v0.1 report and PR description incorrectly called the `results.json` value `checks: 1551` a count of executed **assertions**. It is a manually incremented count of selected check groups in `verify.py`; it omits assertions inside `decode` and several assertion sites in loops. The original files and result remain preserved as evidence of the reporting error.

An AST instrumentation pass replacing each `assert expression` with a counted check, while preserving failure behavior, reports **1,837 evaluated assertion expressions** when running the frozen v0.1 verifier. This number is an implementation execution count, not independent experiments or evidence of a physical law. Run `python3 count_assertions.py /path/to/v0.1/verify.py` to reproduce; its SHA-256 input guard identifies the exact frozen source. The 64 masks, 24 relabelings, 28 kernel orbits, and one conditional close/hold disagreement are unchanged. No mathematical or physical promotion follows from either count.

**Disposition:** `1551 assertions` is AUTO_FREEZE as a misdescription; `1551` remains the old program's manually maintained `checks` field. Reopen only with a correctly defined and reproducible count. Physical promotion 0; non-constructor review pending.
