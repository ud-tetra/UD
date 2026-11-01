# UD v1.5.1 — Pareto Explanation Correction

**Date:** 2026-11-01 · **Type:** Versioned non-destructive amendment to v1.5 proof wording · **Physical promotion:** 0.

## Correction

In `UD_COFACE_CROSS_CHANNEL_AND_NEWBORN_SOURCE_AUDIT_v1.5.md`, section 4, replace the sentence:

> Both dominate 023 and 123 by the stated coordinatewise comparison.

with:

> Face **013** dominates faces **023** and **123** (equal seam-mismatch scores but strictly greater burden scores). Face **012** is incomparable with every other face because it has the uniquely highest seam mismatch but a strictly lower burden-current score. Faces **012** and **013** are the complete nondominated (Pareto) set.

The exact diagnostic vectors are

| Face | Burden score | Seam mismatch |
|---|---|---|
| 012 | 3/8 | 1 |
| 013 | 13/8 | 1-sqrt(3)/2 |
| 023 | 3/2 | 1-sqrt(3)/2 |
| 123 | 7/8 | 1-sqrt(3)/2 |

Direct coordinatewise comparison proves Pareto nondominated set `{012,013}`. No formula, theorem verdict, exact assertion count, or experimental interpretation changed. The original source remains immutable. The v1.5 SymPy verifier explicitly checks the result of the Pareto calculation; 920 assertions passed.

**Causality and scope:** Comparing these two scores assumes both are to be maximized (not source-derived); it cannot select the birth event. The weighted score crossover remains `5*sqrt(3)/6` for the declared preparation and is **not** a UD coefficient.

**Status:** Exact correction. Supersedes the *sentence only* in v1.5 section 4, not the prior proofs or underlying records. Nonconstructor review remains pending.