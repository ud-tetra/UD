# Fresh synthetic preparations pass the frozen measured-frame budget

**Three prospective fresh synthetic preparation records pass the unchanged PR224 measured source-frame budget.** All three actual floating runs learn 209 retained columns at the fixed 2^-24 cutoff. Three exact returned-shift upper bounds are below the unchanged 5.563206409135001e-10 allowance. No budget was selected using these outcomes.

Development — no registry entry. Physical promotion 0. External review PENDING.

| Frozen preparation | Measured frame residual upper | Exact normal residual upper | Certified returned-shift upper | Frozen budget |
|---|---:|---:|---:|---|
| signed_cycle | <5.244401e-11 | <2.953029e-14 | <1.581373e-10 | PASS |
| signed_shuffle | <5.186171e-11 | <2.891523e-14 | <1.569574e-10 | PASS |
| rational_pair | <6.132554e-11 | <2.883017e-14 | <1.761333e-10 | PASS |

The same raw frame ceiling is 2.4895818841068944e-10, the same retained Gram cap is 2^-43, and the same normal cap is approximately 3.0785144546764306e-14. The normal cap is an old finite-run measured maximum, not a guarantee for future solvers. No new upper was substituted. The exact dyadic constants and directed enclosures, rather than rounded display numbers, decide acceptance. See CERTIFICATE.json and inputs/FIXED_BUDGET.json.

## What was frozen and executed

PROTOCOL_FREEZE.json hash c87e78f3aa600d8dbdae2a6a896fd031e485a5c67045f19ffbab69fc52865bd4 binds the recipes, policy, source inputs and code at 17:48:36UTC on 2026-10-19, before any new record or fit. It freezes three same-clock-parity orthogonal maps: a signed cycle, a signed shuffle, and disjoint exact3/5,4/5 pair rotations. Each gets independent fixed-seed onehot signed perturbations of one raw quantum 2^-48 per 62-vector. All three raw hashes freeze together in DATA_FREEZE.json before the first estimator fit. Local file times and code-enforced custody record this sequence; no external registration or blinding is claimed.

Generation checks all 56,370,462 scalar differences across the three records. Each record has 37 preparations, 8191 samples and 62 channels. Rational nominal rounding is nearest denominator 5, with exact error at most 2/5 quantum and no ties. Same-parity mixing preserves the unsketched nominal temporal family and aggregate preparation energy before rounding, not each preparation's norm. The fixed sketch need not preserve its conditioning; rank is learned rather than forced.

The arithmetic core uses the same SciPy SVD, lag-two least-squares, eigensystem and angle operations as the pinned prior estimator, with 1-thread runtime. The I/O wrapper is new and explicitly pinned; the whole software is not claimed byte-identical. The estimator loads no source phases. Numerical exceptions would produce retained HOLD receipts without retries or substitutions. None occurred. Saved lossless retained U, singular metadata, returned T/eigensystem/emitted proposals and auxiliary X witnesses are included. Full 321-column U factors are not retained, so no new full-factor SVD proof is claimed.

After the three fits, untrusted auxiliary X coordinates freeze before exact frame, Gram and normal-equation measurement. Exact dyadic arithmetic verifies U1-U0X and all output norms. THEOREMS.md explains why no accuracy or optimality assumption is needed for X. Five predeclared finite controls pass, including refusal above the unchanged normal cap even though that control's diagnostic shift bound passes. All primary cases and all control HOLDs remain in the record.

## Scope of the result

These are new synthetic nominal preparations derived from an existing pinned synthetic baseline, not independent physical acquisitions. The one-quantum radius is relative to each NEW integer nominal. Original-baseline raw-ball eligibility is not asserted. The direct measured source-frame theorem has no old raw-ball premise, and measures the combined preparation/input/numerical displacement. It is not a pure-roundoff estimate.

The observed 209 cutoff decisions are numerical outputs, not newly certified exact SVD rank/order decisions. Emitted phases/eigensystems are retained but not newly phase-certified. The source-frame/returned-shift certificate does not execute the other policy gates, full-Hankel/native 1893 spectral extraction, or observer-kernel proofs. It gives no universal floating convergence, population success probability, physical correspondence or per-preparation stock conservation. Earlier apparatus-contract HOLD, generic scalar full-SVD sufficient-route HOLD, 747-dimensional observer blindness and modulo-pi ambiguity are unchanged. Gap2_FINAL_Finite_Genesis.png was unavailable and not used.

Same-team static and outcome reviews are included with their executed scope; they are not external independence. A previously sent external-review request is not an acceptance receipt and is not resent here.

## Replay

With requirements.txt installed, saved-witness exact replay needs the two pinned source basis members already in the repository:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replay.py --repo /absolute/path/to/UD --work /absolute/path/to/new-review --receipt /absolute/path/to/review-receipt.json
```

For full raw regeneration and exact integer/dyadic projection comparison, add:

```bash
--baseline /absolute/path/to/ramp_clock_stress.i64le
```

The required original baseline SHA is 25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59,150,321,232 bytes. It is a declared pre-existing dependency; raw files are not bundled. Baseline generation/recovery provenance is in the pinned parent captures. records.py reconstructs the three fresh raw records, checks every scalar noise difference and all raw hashes; kernel.project recomputes every exact projected numerator and dyadic digest. No estimator SVD or auxiliary alignment is rerun in replay. Saved numeric witnesses permit portable exact certification without expecting bitwise reproduction of an opaque library run. FULL_REPLAY.json records the completed raw/projection and saved-witness replay separately from the original 3 actual fits.

## Next frontier

Carry the fresh saved outputs through the full-factor/cutoff/eigenpair/inverse/emitted-phase policy with separately frozen supplemental code, retaining any HOLD; this needs additional full-factor evidence from a newly declared run rather than inventing the omitted tails. Separately seek attributable outside review of the current measured-frame theorem and replay. Do not infer hidden bulk information or retune the fixed cap from these three successes.
