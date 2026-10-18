# Preparation-specific clock and excitation certificate

Development lane; physical promotion **0**; independent review pending.

This extends PR193 from one common clock to 37 preparation-specific origins,
rate errors and jitter sequences. Each preparation's clock is common across its
62 channels. Errors may be arbitrarily correlated across preparations.

## Results

- All four frozen declared-origin profiles certify positive temporal excitation:
  zero, common one-sample shift, alternating quarter-sample shifts, and a ramp
  from minus one-half to plus one-half sample.
- The conservative unknown-origin bound certifies excitation for deviations up
  to **2^-14 sample units** from a common origin, without other preparation error.
  The failed bound at 2^-13 is inconclusive about actual rank.
- The joint unknown-origin example uses offset box 2^-16, one-quarter excitation
  allocation for preparation error, jitter 2^-34, rate error 2^-48, raw vector
  error 2^-36 and the declared parent model floor. It certifies ideal-estimator
  phase error **<4.492e-5 radians/sample**.
- All 80 frozen budget cases, four profile witnesses, five control families and
  ten tests replay. Outcomes include 52 conditional matching certificates,
  19 one-sided enclosures and nine HOLDs; every outcome is retained.

Different preparation origins can destroy rank and amplify a global preparation
operator norm. The proof uses per-preparation modal-block error bounds and exact
right-inverse/Gram certificates, including validated rotation approximation error.
A common origin preserves true singular values exactly; coordinate-dependent
certificate lower bounds may differ without contradicting that fact.

The separate largest passing jitter and rate budgets in RESULT_SUMMARY.json
must not be combined. Known-profile certificates apply to the exact declared
origins; unknown deviations need their own error charge.

## Replay

Install requirements.txt in an isolated Python environment, extract the complete
ZIP into an empty directory, then run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_package.py
```

Replay checks every package file hash, regenerates the validated profile
rotations, verifies exact right-inverse/Gram witnesses and all budget cases,
and runs controls and ten tests in a temporary copy. No full Hankel allocation
or new actual floating phase-estimator execution is required by this replay.

THEOREMS.md supplies assumptions and proof; CERTIFICATE.json contains rational
bounds; RESULT_SUMMARY.json presents results; ACQUISITION_REQUIREMENTS.json
lists outstanding source and metrology inputs. Profile witnesses are untrusted
proposals until their exact residual and norm checks pass.

These are conditional results for the pinned learned real modal model and
principal-band interpolation. They are not SI timing specifications, future
instrument-noise guarantees, full-Hankel certificates or independent review.
Actual floating outputs retain PR189's residual/rounding requirements. Issues
144, 178 and the independent review intake remain open.
