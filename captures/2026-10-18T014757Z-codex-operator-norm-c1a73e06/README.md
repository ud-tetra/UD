# UD floating estimator: frozen operator-bound comparison v0.1

The unchanged actual floating estimator was run on two pinned constructor noise
records. A new exact-Gram verifier compares two sufficient phase-matching
certificates on the same arrays. Physical promotion 0; independent review pending.

| Record | Previous Frobenius certificate | Refined operator bound | Certified phase error, radians/sample |
| --- | --- | --- | --- |
| dense_sign | HOLD | Unique fitted-reference matching | <0.000889144 |
| coherent_dc | HOLD | HOLD | Not certified |

Both original uninstrumented proposals are byte-identical to the instrumented
ones. No estimator, phase, threshold, matching rule, or frozen code was retuned
following these outcomes. Every HOLD is preserved. HOLD means this sufficient
proof cannot certify matching, not that the estimator or true spectral signature
fails. These controls were known before the freeze, not independent or blinded
data. The reference is a fitted model, not physical frequency truth.

The refinement replaces only the reference-model and data-projection residual
Frobenius bounds. For each exact dyadic residual R, a 161-by-161 integer Gram
provides the smaller of its trace and maximum absolute row sum as a bound on
squared operator norm. This is a certified upper bound, not an exact spectral-norm
calculation. Outward interval arithmetic includes the same reference-phase
approximation allowance. See THEOREMS.md and unchanged numeric_math.py.

For dense_sign, the model-residual upper bound falls from about 1.02606e-4 to
1.72588e-5; the projection-residual bound falls from 5.87972e-5 to 2.15578e-5.
This is enough for strict phase separation. For coherent_dc the model-residual
bound remains about 1.04074e-4. The new bound alone does not close this case.
The coherent offset is a useful future same-subspace/amplitude-control test;
that possible refinement has not been proved or substituted here.

## Replay

Extract the core ZIP and all four WITNESS archives listed in WITNESS_INDEX.json
into one directory, then run:

```
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

Recorded runtime: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, python-flint 0.9.0.
The runner verifies hashes and replays both exact saved-sketch/floating-array
residual calculations in a temporary copy. It leaves the original receipts intact.
The exact arrays, original proposals, Gram receipts and both decisions are retained.
It does not regenerate omitted raw records or independently establish their custody.
Fresh raw-source executions projected 37,580,308 scalar readings in total; their
hashes and parent recovery sources are recorded in CAMPAIGN_FREEZE/OMITTED_DATA.

Six checks cover exact PSD Gram formulas, operator/Frobenius distinction, rank-one
and zero cases, dyadic scaling, subnormal float encoding, and a passing reference
versus a corrupted shift-bound refusal. Both portable residual replays agree
with the fresh source-record receipts. Same-constructor verification is not
independent review. No full-Hankel execution is claimed and no dense Hankel was
allocated. Temporal sketch order 105 is certified for dense_sign; the coherent_dc
phase HOLD does not provide the assembled order receipt in this version.

The existing full-Hankel criteria, nominal 747-dimensional dynamical observer
kernel, 62 history channels and separate 189 diagnostic outputs are unchanged.
This return does not certify uniform phase matching throughout the 2^-20 error
ball, optimizer convergence, physical phases, hidden-state recovery, acquisition
or metrology. Review HOLD #177 and independent replay #130 remain open.
O03 tolerances remain protocol controls; no CRL or physical promotion is made.
