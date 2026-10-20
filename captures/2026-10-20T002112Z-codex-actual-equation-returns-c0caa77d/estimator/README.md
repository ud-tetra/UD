# Two adversarial records: actual floating estimator and exact output review

Development research; Physical Promotion = 0. Two frozen original-nominal recipes were evaluated exactly once each by the unchanged PR250 estimator. Both executions completed with learned order 209. Neither was retried or replaced. All two raw/noise/overflow/projection receipts and source/protocol hashes were frozen before either fit and independently reviewed.

| Fixed case | All fixed output gates | Raw lag Frobenius upper | Direct finite emitted phase error upper |
| --- | --- | ---: | ---: |
| null_top1_alternating | PASS | 5.567150984689772e-11 | 9.658324838923563e-15 |
| null_top2_alternating | HOLD: raw-lag cap | 6.157846432372804e-11 | 1.002893298768725e-14 |

The frozen raw-lag gate is 2^-34 = 5.820766091346741e-11. Top2's exact dyadic Frobenius bound exceeds that gate and its admission remains HOLD. This is a conservative Frobenius-to-operator qualification failure, not a proof that the actual operator norm exceeds the cap or that its finite phases failed. No gate, norm route, sample, rank, precision, sketch or target was changed to recover the record.

Both records have independently gate-qualified retained singular equation residuals: xi <=4.725162482378356e-14 (top1) and <=4.666267993740219e-14 (top2). Both retained Gram defects and measured s209 floors pass. Saved complex inverse/eigenpair/argument/encoding gates pass, and each finite list matches all 209 pinned two-step source targets bijectively modulo 2pi. The exact saved output target errors above are separate from the conditional theorem's conservative propagated phase bounds.

For transparency, the source equation theorem evaluated pointwise with each measured tuple returns disjoint phase disks: bounds 3.260339674130404e-7 and 3.266292200713908e-7, respectively. That pointwise mathematical result does not waive top2's failed mandatory raw-lag gate. It also does not assert uniform success of the numerical backend over a ball. The primitive-frequency ambiguity modulo pi remains.

The old PR254 strict rank-209 reconstruction-cap NO-GO proofs for both raw recipes are inherited and unchanged. The retained equation concerns `Z V - U Sigma`; it does not claim a full rank-209 reconstruction residual, full SVD certificate or exact-spectrum(T) forward bound. The old cyclic-one-quantum example is inherited control evidence only; there was no new control fit.

## Reproduction and storage

`PROTOCOL_FREEZE.json` binds all core sources, copied inputs and source equation contracts before outcomes. `DATA_FREEZE.json` and `DATA_INDEPENDENT_COMPARISON.json` bind both exact raw/projection hashes. `ROOT_RELEASE.json` links root release and independent pre-fit review. `RUN_EXECUTIONS.json` and `results/*/RUN.json` retain each one-time execution and hashes of all numerical witnesses. `EXECUTION_STORAGE.json` records exact file bytes and estimator-reported elapsed times.

There are 30,295,263 bytes of retained numerical NPZ witnesses in total, 30,297,939 bytes including both RUN.json files. No new raw record is retained. At most one 150,321,232-byte reproducible raw file exists transiently. No full Hankel matrix is allocated. The primary exact verifier took 40.874 seconds with measured process peak RSS 781,096 KiB; actual estimator peak RSS was not instrumented. Estimator-reported times were 7.421 and 8.753 seconds. These are host-specific measurements, not guaranteed performance bounds.

The exact verifier is replayed without calling `estimate`:

```
PYTHONDONTWRITEBYTECODE=1 python certify.py --repo /ABS/PATH/ud-repo --baseline /ABS/PATH/ramp_clock_stress.i64le --out /ABS/NEW/OUTPUT
```

Output must be a new path outside this package and any MANIFEST-bearing ancestor; lexical, resolved and ancestor destinations are guarded. Replay regenerates and hashes the same raw recipes, performs unchanged exact integer projection, and verifies saved factors only. Never rerun `driver.py fit`. Root owns capture/publication and independent final review receipts.
