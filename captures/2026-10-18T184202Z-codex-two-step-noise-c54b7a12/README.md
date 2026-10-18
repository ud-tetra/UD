# Two-step noise tolerance on the frozen PR195 stress trajectory

The arbitrary-noise order guarantee is **δ≤2^-37 per62-channel vector** (about7.276×10^-12). This guarantees209 singular values above the unchanged source cutoff2^-24. The certified open radius is approximately8.0513436013×10^-12. It is an order guarantee, not a uniform actual-floating phase guarantee.

All six noisy records were frozen before fitting. Both noise Grams and all six raw hashes were reproduced in a separate generation pass. There were12 original/instrumented adapter runs, with byte-identical emitted outputs for applicable209-order cases; five full saved-array phase replays and six tests. Every raw record satisfies the per-vector2^-20 gate relative to the encoded PR195 stress record.

| Noise case | Per-vector noise norm (approx.) | Floating order | Exact order bound | Primary phase certificate | Primary phase upper, rad/2 steps | Supplemental actual error upper |
|---|---:|---:|---|---|---:|---:|
| dense_a0 | 2.797410e-14 | 209 | PASS | PASS | 9.102014e-10 | 1.387841e-14 |
| dense_a8 | 7.161368e-12 | 209 | PASS | PASS | 1.356559e-09 | 3.881896e-12 |
| dense_a12 | 1.145819e-10 | 209 | PASS | PASS | 7.563575e-09 | 6.193718e-11 |
| dense_a16 | 1.833310e-09 | 209 | PASS | PASS | 1.081649e-07 | 9.897332e-10 |
| dense_a25 | 9.386549e-07 | 321 | HOLD | HOLD | — | — |
| dc_a25 | 9.386549e-07 | 209 | PASS | PASS | 9.686394e-10 | 1.198662e-14 |

RESULT_SUMMARY.json and the per-case dyadic receipts are authoritative; displayed decimal values are rounded for reading. The supplemental source-aware assigned-error bounds never replace a primary HOLD. Its uniqueness result is recorded separately.

The dense cases reuse a single frozen sign tensor at five amplitudes; they are not independent replicates. Coherent DC has a different temporal geometry: it remains in the stationary source column, so its comparison-model tail can stay at the parent generation bound. Dense noise must be charged in the tail. Tested passing amplitudes do not imply every intermediate amplitude or noise pattern passes.

The uniform ideal-subspace phase sufficient bound returns **HOLD even atδ=0**. This is a conservative proof limitation. It does not prove actual failure or zero noise tolerance. A new proof would be needed for an arbitrary-noise actual-floating phase guarantee. The full frozen acquisition noise ball2^-20 is not certified by the much smaller uniform order guarantee.

## Frozen rules and correction

NOISE_FREEZE.json pins recipes, seeds, inputs and code before generation/fitting; DATA_FREEZE.json pins all raw hashes before fitting. The original frozen files remain unchanged. The estimator and primary acceptance gates were never retuned. The first supplemental direct_error.py attempt failed because an outward-rounded interval touched exactzero. direct_error_v2.py conservatively bounds its validated upper endpoint first. The failure log, initial code, correction receipt and resume log are retained; this is explicitly a postexecution diagnostic correction. Use replay_package_v2.py for the completed diagnostic replay.

## Replay

Extract the CORE ZIP and every WITNESS ZIP into the same empty folder. Install requirements.txt using Python3.12, then run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_package_v2.py
```

This checks package and witness hashes, rederives uniform bounds, replays all six order receipts and all applicable actual phase certificates, reruns supplemental source-target diagnostics and six tests. It uses saved arrays and does not invoke a dynamical constructor, regenerate raw records, rerun the floating adapter or allocate the full Hankel matrix. Independent external replay is still pending.

For a fresh adapter run, first recover the exact PR195 baseline record using its capture recipe and SHA256 in NOISE_FREEZE.json. Stage it at the sibling path floating-timing-work/records/ramp_clock_stress.i64le. In a separate campaign copy remove only its generated receipts/results/logs, preserve the frozen sources and inputs, and run make_records.py then the adapter commands listed in RUN_EXECUTIONS.json (using direct_error_v2.py for the supplemental diagnostic). Raw verification can be reproduced without removing the recorded evidence using `python make_records.py --destination /new/empty/path`; it checks all six raw hashes and exact Grams against DATA_FREEZE.json. The included RAW_REGENERATION_RECEIPT.json records the completed reproduction. Each noisy raw record is150321232 bytes; reproducible raw records are omitted from the GitHub payload.

## Interpretation

All phase errors are circular radians per TWO-STEP sample, conditional on the pinned learned source model; the original frequency remains moduloπ. These synthetic records are not apparatus measurements. The former204/205 noise-cutoff HOLD, nominal747-dimensional unobservable space and observer-mapping questions remain open. A right sketch kernel also makes phase output insensitive to some large raw perturbations, so raw error gates are verified separately.

Physical promotion=0. Development — no registry entry. Same-team review only; independent review and empirical provenance remain pending. See THEOREMS.md, CLAIM_LEDGER.json, SOURCE_IDENTITY.json and DIAGNOSTIC_CORRECTION.json.
