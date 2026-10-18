# UD finite-window phase-stability return v0.1

Development lane; physical promotion 0; constructor work; independent review
pending. This return extends temporal-order separation to a conditional bound
on individual phase recovery about a pinned fitted reference. It does not
identify physical frequencies or certify the floating implementation generally.

## Results and their scopes

| Result | Scope |
| --- | --- |
| Unique phase matching at vector budget 2^-27 | Exact-arithmetic top105-SVD/LS estimator; largest passing radius on frozen dyadic grid |
| Phase error <0.000646029 radians/sample there | Relative to pinned learned reference phases |
| At full 2^-20 vector budget | Only one-sided enclosure; this proof cannot certify unique matching |
| Two new coherent controls | Both fit105 components; intended-parameter discrepancy <=2.776e-15 radians/sample observed |
| New high-budget record's full Hankel certificate | Exactly1893 values above frozen threshold; condition<706.570; tail<1.251e-12 |
| Reference phase-residual computation | All18,790,154 source readings used in exact integer sketch calculation |
| New full certificate | All18,790,154 readings checked; no dense286.75-GiB Hankel allocation |
| Bound tests and portable arithmetic replay | Six tests pass;5460 frame pairs and21 dyadic radii checked |

The previous105-component temporal-order result remains valid throughout2^-20.
This does not imply stable unique phases over that whole ball. Failure of this
sufficient phase-matching bound is not demonstrated failure of the actual fitter.
No claim is made that2^-27 is the optimal or necessary radius.

THEOREMS.md proves the subspace, deleted-row and shift-eigenvalue bounds and
states the sampled-frequency alias and positive-noise identifiability limits.
PHASE_STABILITY_CERTIFICATE.json records all exact dyadic constants and the
frozen grid. CONTROL_RESULTS.json keeps observed fitting discrepancies separate
from exact-arithmetic guarantees and the full Hankel acceptance certificate.

## Source and replay

Python3.12, NumPy2.3.5, SciPy1.17.0, python-flint0.9.0; one BLAS thread.
Run `OPENBLAS_NUM_THREADS=1 python validate_return.py` to replay frame constants,
phase-rounding bounds, dyadic-radius decisions, six tests, input bindings,
observed phase-parameter comparisons and the full-certificate receipt checks.
This portable check does not recompute the omitted raw reference-to-sketch
residual or repeat the large full Hankel proof. Those were executed separately;
their exact outputs, code hashes and input hashes are supplied.

To repeat all raw computations, recover the pinned clean baseline from the
previous record-only/sketch-blind capture recipes, then run in a fresh copy:

```
python certify_phase.py
python make_phase_records.py
python run_controls.py
python summarize_controls.py
python validate_return.py
```

The first commands expect the pinned clean raw record at the sibling path in
CAMPAIGN_FREEZE.json. Every generated output location must be new; no fitting
retry or gate adjustment occurs. Source freeze and existing generated records
are already included as receipts; do not overwrite them in this captured copy.
Raw records and large factor Grams are omitted with size/hash inventories;
proposals and compact proof/receipt files are included. Regeneration hashes
must match before a replay is treated as the same control.

## Remaining work

A validated floating numerical adapter, general optimizer convergence, sharper
full-budget phase matching, independent replay/review and native-family
acquisition/metrology remain open. The proposed next adapter must enclose the
computed singular subspace and shift-solve residual; observed floating output
alone cannot substitute for those bounds. GitHub178/130/136/144 and review
HOLD177 retain these obligations. The747-dimensional nominal observer kernel
is unchanged. O03 tolerances remain protocol controls, not theory constants.
