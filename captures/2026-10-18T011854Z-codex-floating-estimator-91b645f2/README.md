# UD actual floating phase-estimator validation v0.1

The actual floating outputs now have a posteriori phase-matching certificates
on three pinned records. This closes the numerical-output gap for these runs;
it does not prove convergence on every input or identify physical frequencies.
Development lane; physical promotion0; independent review pending.

| Captured run | Certified emitted phase error, radians/sample |
| --- | --- |
| Clean | <4.50e-10 |
| Coherent control, declared vector budget2^-28 | <7.06e-8 |
| Coherent control, declared vector budget2^-20 | <1.805e-5 |

Bounds are relative to the pinned fitted reference. Every returned phase has
unique matching there. These are conservative residual bounds, distinct from
the much smaller observed constructor-parameter discrepancies in the prior
campaign. The uniform all-error-pattern2^-20 phase-matching theorem remains open.

## What was validated

The instrumented proposer retains the actual binary64 basis, shift matrix,
returned eigenvalues and angles; auxiliary eigenvector/inverse/reduction
proposals remain untrusted. Its original PROPOSAL.npz must match the old output
bytes exactly. All three do. The verifier converts floating bits to exact dyadic
integers without extra quantization, projects every raw reading into an exact
integer sketch, and encloses the data projection, orthogonality, shift solve,
eigenpair, inverse and emitted-argument residuals. THEOREMS.md proves how these
bounds yield one-to-one phase matching. There is no trust assumption about
BLAS/SVD/least-squares/eigvals/atan2 accuracy.

Each actual record also has exactly105 sketch values above the declared
cutoff, certified by the reference-model rank/error bounds. This is a temporal
sketch count, not a fresh1893-value full-Hankel execution. The full-Hankel
verifier and its existing signature certificates are unchanged. No dense Hankel
is allocated. The nominal747-dimensional dynamical observer kernel is unchanged.

## Portable full residual replay

Download the core ZIP plus the six witness ZIPs listed in WITNESS_INDEX.json.
Extract all seven into the same directory; witness archives populate
`results/CASE/FLOAT_WITNESS.npz` and `results/CASE/EXACT_RECORD_SKETCH.npz`.
Python3.12, NumPy2.3.5, SciPy1.17.0, python-flint0.9.0 are the recorded versions.
Run:

```
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

The runner checks every file hash and replays all actual-array residuals in a
fresh temporary copy. Existing receipts remain intact. No parent workspace or
150-MB raw record is required for this saved-sketch numerical replay. Raw
record-to-sketch identity was checked in the original all-readings executions;
that projection can be repeated separately using the pinned raw-record recipes
and CAMPAIGN_FREEZE.json. The saved exact sketch is a witness, not a substitute
for independent raw-source custody.

Each ZIP is a separate payload to keep individual transfers modest. All actual
floating arrays and exact sketches are retained, not replaced by synthetic
identity matrices or summary-only numbers. Raw parent records are omitted with
hashes and regeneration sources. Core code and the unchanged original proposer
are included. New raw runs require new output paths; the frozen scripts preserve
HOLD and do not retry or retune.

Six tests cover exact encoding including subnormals, a singular-basis gate,
corruption of the actual shift and eigenvalues, an invalid inverse and an invalid
emitted-argument bound. Three fresh source-record runs and three separate
saved-array replays pass. These are same-constructor computations, not an
independent review or blinded apparatus campaign.

Remaining obligations under GitHub178/130/177/136/144 are independent replay,
review, general fitting/error guarantees and acquisition/metrology. Review
HOLD177 is unchanged. No CRL/physical promotion is made. O03 tolerances remain
protocol controls rather than theory constants.
