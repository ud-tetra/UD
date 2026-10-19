# Exact projected cutoff and two-step phase extraction

**All nine saved outputs pass the finite cutoff/phase checks: three previous outputs and six fresh synthetic preparation/noise fixtures.** The six fresh outputs also pass the unchanged PR224 measured-frame caps. Development — no registry entry. Physical promotion 0; external review PENDING.

## Results and objects

For every one of the nine exact projected sketches (8191×321), exactly 209 singular values exceed the unchanged 2^-24 cutoff. Across all nine, sigma209>0.0026660 and sigma210<1.171276e-12. This is an exact **threshold count**, not a claim that all discarded singular values vanish or that the exact algebraic rank is 209. It is not the native 1893 Hankel rank.

All 209 emitted two-step angles in each output match the pinned learned-model targets bijectively. Across all nine outputs, the largest certified direct circular error is<2.031330e-14 radians per TWO-STEP sample. Measured-frame phase-transport radii are<2.956668e-8, below the unchanged separation test. These are distinct conservative bounds for the same saved outputs, not physical frequency accuracy or removal of the modulo-pi ambiguity.

The six fresh pairs all pass without changing the frame ceiling 2.4895818841068944e-10, Gram cap 2^-43, old finite-run normal cap~3.0785144546764306e-14, or shift allowance~5.563206409135001e-10. Exact dyadic enclosures in the JSON files decide acceptance; displayed decimals are rounded conservatively.

| Fresh preparation/noise pair | Returned-shift upper | Direct emitted circular-error upper | Frozen contract |
|---|---:|---:|---|
| reverse_stationary | 1.5614968e-10 | 2.0313292e-14 | PASS |
| shuffle_cycle | 1.5969225e-10 | 7.6599243e-15 | PASS |
| shuffle_block1024 | 1.5754117e-10 | 1.0463520e-14 | PASS |
| offset_rotation_period2 | 1.7440720e-10 | 6.3215759e-15 | PASS |
| double_rotation_period4 | 1.7698796e-10 | 5.6072422e-15 | PASS |
| transpose_directed | 1.7666108e-10 | 6.1100185e-15 | PASS |

PARENT_NUMERIC_CERTIFICATES.json extends the previous three saved outputs with **zero new estimator calls**. CAMPAIGN_NUMERIC_CERTIFICATES.json covers the six fresh actual runs. CERTIFICATE.json retains their exact frame/Gram/normal/shift results separately. Every primary case remains; primary HOLD count is 0. Twelve declared controls include expected HOLDs and refusals, all retained.

## Why discarded SVD columns are unnecessary

The rank-q polar approximation of the retained Uq,Sq,Vq has exact proposed nonzero singular values and a validated operator-error upper obtained from the exact truncated reconstruction residual and two retained Gram defects. Weyl encloses sigma209 and sigma210. No full 321-column left tail or assumed library error constant is needed. The discarded spectrum is bounded, not declared zero. This retained-factor enclosure must not be substituted for an old full 321-factor gate.

The phase verifier exactly checks eigenpair/inverse/argument metrics against their unchanged relevant caps and verifies ties-even emission. A source-frame transport proof bounds a nearby diagonalizable correction to the returned shift. A separate validated circular calculation matches the actual emitted dyadics to all 209 pinned exp(2iomega) targets with strict uniqueness. THEOREMS.md gives the formulas and limits: no exact spectrum(T) theorem or old all-eight-gate admission is asserted.

## Prospective six-pair campaign

PROTOCOL_FREEZE.json hash baa1b4a59fd65f37a7802b28bdeeca93c2490fb220c8274c6fa2463d73aa190e froze all scientific code, recipes, source inputs and unchanged caps at 2026-10-19T18:25:08UTC before generation, fits or numeric evaluation. The previous saved outputs were already known; no blinding or external preregistration is claimed. All six new raw hashes and complete 112,740,924 scalar noise-difference checks froze together before the first new fit. The six pairs are a declared list, not a 36-case Cartesian product.

Same-clock-parity signed reversals/shuffles and exact rational rotation compositions preserve the pre-rounding unsketched temporal family and aggregate preparation energy. They do not preserve each preparation's norm or guarantee fixed-sketch conditioning. The denominator 25 compositions are formed exactly and rounded once, with scalar rounding error<=12/25 raw quantum and an explicit 49*maxraw+25 int64 guard. Every new 62-vector gets exactly one signed quantum 2^-48 relative to its own new integer nominal. Original-baseline raw-ball membership is expressly not claimed.

All six actual SciPy runs learned 209 at the fixed cutoff without forced rank or loading source phases into the estimator. Lossless retained bases, singular metadata, returned shifts/eigensystems and emitted proposals are included. Auxiliary X coordinate proposals freeze before exact measurement and are untrusted. The library arithmetic is unchanged from the declared estimator core; wrappers are newly frozen and not claimed byte-identical to an entire old program.

## Interruption and continuation

The first three fits completed. The original runner then stopped **before invoking the fourth estimator** because its transient raw filename already existed; the file matched the frozen hash. FIT_AND_FRAME.log and INFRASTRUCTURE_INTERRUPTION.json retain the obstruction. RESUME_FREEZE.json explicitly froze an operational continuation after those three outcomes were known. It binds all three completed RUN/witness hashes, reuses them, and invokes unchanged generation/estimator functions only for the remaining three cases in a new temporary directory. No completed fit was repeated, no numerical rejection was retried, and no recipe, budget, threshold or mathematical code changed. Six fits in total, notnine. CONTINUATION.log and EXECUTION_RECEIPT.json record the distinction.

## Replay and review

Full replay regenerates all nine raw records one at a time from the single pinned original synthetic baseline, checks every nominal/raw hash and scalar perturbation, recomputes exact integer/dyadic projection hashes, recomputes all nine cutoff/phase certificates and all six frame certificates, and repeats the twelve controls. It calls **zero estimators, SVDs or auxiliary alignment proposers**. It may import numerical libraries as dependencies; this is distinct from calling their numerical fitting routines.

With requirements.txt available, run from this capture directory:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python driver.py replay --repo /absolute/path/to/UD --baseline /absolute/path/to/ramp_clock_stress.i64le --work /absolute/path/to/new-temporary-review
```

The new work directory must not exist. FULL_REPLAY.json and its log record the completed PASS:169,111,386 raw scalar checks, nine exact projected/cutoff/phase certificates, six frame certificates and twelve controls; zero new estimator calls. The required original baseline is 150,321,232 bytes, SHA 25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59; it is a declared existing synthetic dependency, not bundled acquisition. All fresh and prior raw files are recoverable from their pinned exact matrices, seeds, recipes and baseline. The pinned parent capture and the two archived source basis members remain repository dependencies. INPUT_PROVENANCE.json, INPUT_INDEX.json and the primary freeze bind them. No dense 287-GiB Hankel matrix is allocated.

Same-team reviews are scoped separately. Their arithmetic expressions and executed scope are included, not represented as outside independence. Review code corrections and operational corrections remain visible. In particular, a same-team diagnostic initially demanded identical outward-rounded endpoints from two formulas; the failed check is preserved, and its correction proves independent direct uppers <=published uppers with no additive tolerance. Exact cutoff, phase and primary frame statuses are not strengthened by the number of dependent claims.

## Remaining boundary

Finite success of these six deterministic fixtures gives no population success rate, worst-case optimality or uniform future-solver theorem. No new full-Hankel/native 1893 certificate, 747-dimensional observer-kernel reduction, empirical data, SI mapping, apparatus qualification or physical correspondence is supplied. Earlier raw-ball/all-policy holds and the generic scalar sufficient-route HOLD stay intact. Gap2_FINAL_Finite_Genesis.png was unavailable and not used. No public-site deployment or new external email is performed this turn.

Next: derive a source-excitation guarantee or counterexample over an explicitly bounded preparation/noise family, and prepare the experimentally testable calibration/model-mismatch contract while independent review remains pending. Promotion requires the stated independent evidence and governance procedure.
