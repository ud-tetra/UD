# UD conditional preparation and clock budgets v0.1

A positive temporal-excitation margin and explicit preparation/timing error
budgets now have source-bound conditional certificates. Physical promotion0;
development — no registry entry; independent review pending.

For the105-by-161 learned sketched coefficient matrix, a validated untrusted
right inverse proves sigma105(C)>0.0012130785174. Its norm bound is<0.107376;
the fixed principal-band derivative factor Omega<8.587783. This is a margin of
the learned temporal model, not physical controllability or spatial rank1893.

Preparation error p<gamma preserves excitation. Common clock-rate error mu and
sample jitter j contribute an exact derivative-norm bound, with no omitted
Taylor remainder. THEOREMS.md states the model, proof and limitations. The
right-inverse witness, exact Gram receipts and all failed/one-sided cases remain
in BUDGET_CERTIFICATE.json.

## Frozen conditional budgets

The following are the largest passing budgets on separately varied frozen
dyadic grids, with preparation error p<=gamma_cert/4 and the declared model floor.
Other timing/additive errors are zero in each individual grid. These maxima are
sufficient, not optimal, and cannot be combined without recalculation.

| Varied control | Largest passing value on grid | Ideal-estimator phase-error bound |
| --- | --- | --- |
| Common sample jitter |2^-22 sample units|<0.000881550 radians/sample|
| Absolute relative clock-rate error |2^-34|<0.001017824 radians/sample|
| Raw62-vector additive error |2^-28|<0.000862413 radians/sample|

A separate frozen JOINT example uses p<=gamma_cert/4, jitter2^-30 sample units,
rate error2^-44 and raw vector error2^-34. It certifies phase error<1.791e-5
radians/sample. Its model singular-value lower bound is>0.0546628. The clean
reference-model fit bound is an explicitly declared model-noise floor here,
not a guarantee for future instruments or changed preparations.

All74 grid rows replay:59 certify,14 give only one-sided enclosures and1 HOLDs
at the conservative excitation margin. The full raw2^-20 error budget does NOT
certify unique matching under this bound. No universal floating convergence or
SI clock accuracy is claimed. The theorem concerns the exact top105 SVD/LS
estimator; actual floating outputs still need PR189's residual/rounding checks.

## Important constraints

- Sampled phases alone cannot bound nonuniform jitter sensitivity: aliased
  interpolations agree on every integer sample but may differ by2 under
  arbitrarily small jitter. The unwrapped principal-band interpolation is
  declared, not inferred as physical truth.
- Clock rate and source frequency scale are confounded without external clock
  calibration. Model-unit numbers here are not SI timing certificates.
- A common constant time origin preserves temporal span and excitation.
  Preparation-specific origins can collapse excitation and require a new check.
- Coefficient preparation bounds need a justified physical state/source map.
  Counting37 preparations alone does not provide excitation or physical control.

Two parallel same-team mathematical reviews checked these formulas and exposed
the alias/clock and preparation-specific-offset limits. They do not satisfy the
independent non-constructor review requirement. TEAM_REVIEW.json records scope.

## Replay

Extract the single core archive and run:

```
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

Python3.12, NumPy2.3.5, SciPy1.17.0 and python-flint0.9.0 are the recorded runtime.
The runner verifies all hashes, re-encodes the saved binary64 right inverse,
recomputes exact small Grams, excitation, frame/separation constants and every
budget. It runs six exact/validated control families and eight tests in a
temporary copy. Existing receipts remain intact. No raw acquisition, new actual
floating phase-estimator run, full-Hankel execution or dense allocation occurs.

ACQUISITION_REQUIREMENTS.json lists the missing source, clock, preparation,
noise and excitation inputs. Independent review/replay and task144 metrology
obligations remain open. The nominal747-dimensional observer kernel,62 history
channels and separate189 diagnostic outputs are unchanged. O03 parameters remain
protocol controls. No CRL or physical promotion is made.
