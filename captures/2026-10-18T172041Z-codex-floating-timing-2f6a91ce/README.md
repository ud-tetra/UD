# Actual floating-estimator timing campaign

Development — no registry entry. Physical promotion **0**; independent review pending.

This campaign constructs four fresh complete records from the pinned learned
real modal model, then runs the unchanged original and instrumented floating
estimators on each. All source recipes and code were frozen before generation;
all raw hashes were frozen before fitting. The actual output certificates are
in VALIDATION.json; every pass and HOLD is retained.

| Record | Preparation origins | Rate magnitude | Alternating jitter magnitude |
| --- | --- | --- | --- |
| modal_zero | zero | 0 | 0 |
| origin_alternating | alternating +1/4 and -1/4 sample | 0 | 0 |
| ramp_joint_clocks | (a-18)/36 sample | 2^-48 | 2^-34 sample |
| ramp_clock_stress | (a-18)/36 sample | 2^-20 | 1/16 sample |

Rate signs alternate with preparation; jitter signs alternate with preparation
and sample. Each preparation has one clock across 62 channels, with prescribed
cross-preparation dependence. These are finite synthetic constructor fixtures,
not independently obtained observations. The source uses exactly the fitted
reference model against which phase discrepancy is checked.

## Actual results

| Record | Floating sketch count | Certified emitted phase-error upper bound |
| --- | --- | --- |
| modal_zero | 105 | <4.835e-12 radians/sample |
| origin_alternating | 105 | <4.659e-12 radians/sample |
| ramp_joint_clocks | 105 | <6.645e-9 radians/sample |
| ramp_clock_stress | 161 (full sketch width) | Proposer model/order HOLD |

All three available original proposals are byte-identical to the instrumented
ones. Both stress executions have identical HOLD receipts. The stress count is
a floating threshold count in a 161-column sketch, not its exact temporal rank
or a full-Hankel spectral failure. All three complete saved-array certificate
replays and 14 tests pass. Raw regeneration is reported separately.

## Three checks with distinct meanings

1. Validated Arb anchors, a proved 96-bit integer recurrence error bound and exact
   coefficient contraction give a uniform waveform-evaluation/encoding error.
   DATA_FREEZE.json binds all 75,160,616 encoded readings by range/layout/hash.
   DIRECT_SOURCE_AUDIT.json separately reports 45,880 direct Arb spot checks.
2. Original and instrumented proposals are compared byte-for-byte. The actual
   computed basis, shift, eigenvalues, eigenvectors, inverse, angles and emitted
   phases are saved. No reference phase is supplied to the floating proposer.
3. The unchanged PR189 mathematical proof verifies saved-array residuals and
   rounding against the pinned reference frame. It does not trust floating
   SVD, least squares, eigensolver or atan2 merely because they were computed.

Constant preparation origins retain the reference frame while changing its
coefficients. Rates/jitter can leave that span and introduce additional modes.
A pass certifies bounded discrepancy from the original fitted reference;
it does not certify exact identification of clock-distorted native modes.
Orders outside 105 and all proof HOLDs are retained without forced truncation.
No old clean residual or additive-to-old-clean acquisition gate is inherited.

## Portable saved-output replay

Extract the core ZIP and every witness ZIP named by WITNESS_INDEX.json into one
empty folder. With the pinned requirements installed, run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

This checks hashes and replays all applicable complete saved-array phase proofs,
HOLD receipts and 14 tests in a temporary copy. It does not rerun the original
proposer or regenerate raw records. Every available floating witness and original
proposal is retained. The raw generation recipe and complete hashes are supplied
instead of duplicating the large int64 source arrays.

## Optional complete raw regeneration

From the extracted package, run:

```bash
OPENBLAS_NUM_THREADS=1 python make_records.py --destination /new/empty/path
```

The destination must not exist. This regenerates all four raw records and
requires byte-identical SHA256 hashes and identical generation-bound receipts.
It needs no parent codec or external dataset. RAW_REGENERATION_RECEIPT.json,
when present, records the separate complete execution performed for this return.
Normal portable replay makes no silent claim to regenerate those bytes.

THEOREMS.md states the timing/evaluation argument; PARENT_FRAME_THEOREMS.md
states the output-residual theorem. SOURCE_IDENTITY.json and adapter patches
show the unchanged mathematical helper and estimator lineage. O03 tolerances
remain protocol controls. SI calibration, general fitting convergence,
independent review/data, physical source/metric mapping, full-Hankel validation
and acquisition admission remain open. No dense Hankel array is allocated;
the nominal 747-dimensional observer kernel is unchanged.
