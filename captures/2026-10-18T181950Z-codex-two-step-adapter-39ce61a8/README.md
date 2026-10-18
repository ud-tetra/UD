# Actual two-step phase adapter: source-precision audit

Development — no registry entry. Physical promotion **0**; independent review pending.

The new record-only adapter learns 105 baseline modes and 209 stress modes at a
separately frozen encoding-precision cutoff **2^-24**. Its actual saved outputs
pass the direct similarity, inverse, eigenpair and emitted-angle checks:

| Existing synthetic record | Certified source-precision order | Circular two-step phase error |
| --- | ---: | ---: |
| Modal baseline | 105 | **<1.373e-13 radians** |
| Larger preparation-clock control | 209 | **<8.961e-10 radians** |

The stress minimum target chord separation is >7.285423493e-7. Its exact encoded
sketch has sigma209>0.0028804 and sigma210<1.034e-10, so the comparison model's
previous rank interval [205,209] closes at 209. Encoded algebraic rank can still
be larger because of tiny rounding directions.

**The earlier instrument-noise counts 205/204 and original stress HOLD remain
unchanged.** The new cutoff audits these known synthetic records at their
proved generation/encoding precision; it does not qualify them under the old
instrument-noise contract. No target rank was forced: the adapter's floating
count and independent source-aware encoded-sketch count agree.

## What was checked

- Four fresh original/instrumented adapter runs; both phase proposals are
  byte-identical. The adapter receives no numerical source phases, clock rates,
  jitter or coefficients. A verifier-only source reduction is proposed later.
- Exact source projections read 37,580,308 existing encoded readings. Source-order
  Gram replays and complete actual-output residual replays agree on both cases.
- Six tests and two frozen actual-array corruption controls pass: a zero source
  inverse and a changed emitted phase are refused. Original witnesses remain
  unchanged. These controls are finite fault checks, not stochastic coverage.
- All available bases, shifts, eigenvalues/eigenvectors, inverse witnesses,
  actual angles, emitted phases, source reductions and exact Grams are retained.

The phase theorem uses normal two-step rotation blocks and directly validates
TD-DJ. It does not multiply by a guessed reference conditioning constant or
assume floating SVD, least-squares, inverse, eigensolver or atan2 accuracy.
THEOREMS.md gives the finite proof and the strict separation gates.

## Aliasing contract

Primary errors are circular **two-step phases**. They identify original phase
only modulo **pi**. The per-target lift integers and divided-by-two bounds in
certificates are conditional on the explicitly declared source labels. They
are not unrestricted one-step generator identification or physical frequencies.
All 209 source targets, including folded signed branches, are checked for
pairwise unit-circle separation and explicit unique returned-value assignment.

## Portable saved-output replay

Extract the core and every WITNESS ZIP listed in WITNESS_INDEX.json into one
empty folder. Install requirements.txt and run:

```bash
python verify_structure.py
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

The structural guard checks exact Gram symmetry, dimensions and descending
witness eigenvalues. It was added after execution as a packaging check; it
changes no estimator arithmetic, threshold, fitted output or numerical bound.
The estimator, mathematical core and corruption recipes retain their initial
ADAPTER_FREEZE.json hashes.

Portable replay verifies all file/array hashes, repeats both exact source-order
and actual two-step phase certificates from saved witnesses, preserves HOLDs
and runs six tests in a temporary copy. It does not regenerate raw records,
reproject them, rerun the adapter or rerun the actual-array corruption campaign;
CONTROL_RESULTS.json retains that separate executed campaign.

For full raw recovery, use PR195's frozen generation package and
make_records.py --destination /new/empty/path; raw hashes must match the current
ADAPTER_FREEZE.json. OMISSION details and source lineage are in OMITTED_DATA.json.
Original/instrumented adapter and source-projection execution receipts are
retained in RUN_EXECUTIONS.json and per-case receipts/logs.

## Remaining scope

These are same-constructor known-model fixtures, not independent/blinded data
or review. The comparison source itself is fitted and declared. No uniform
whole-instrument-noise-ball result, general convergence, original-contract
admission, full-Hankel spectrum, native observer/metric selection, SI clock
qualification, physical identification or hidden-state recovery is asserted.
No full Hankel is allocated; the nominal 747-dimensional observer kernel is
unchanged. O03 cutoffs remain protocol controls. Independent replay/review and
source/band/preparation/clock/noise metrology remain open.
