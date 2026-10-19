# Zero-fit phase replay

The new result directory contains no copied four-case U, SVD, raw baseline or
phase-factor bundles. SOURCE_INDEX.json points directly to immutable PR240
repository phase META/PROPOSAL/RUN bytes, plus the prior frame/run/data receipts.
The parent capture manifest and every used source file are hash-pinned in the
pre-score protocol. The input target list and old phase-quality caps are small
verbatim PR231 data copies.

From this directory or a captured copy, run:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python replay.py --repo /absolute/path/to/UD --out /absolute/path/to/new-phase-replay
```

The supplied repository must contain the pinned PR240 capture with its source
manifest and saved phase NPZ/JSON files. No original baseline is required for
this saved-output phase proof. The replay stages only small frozen code/input
files and a read-only reference to the supplied repository; it never copies or
rewrites the original numerical arrays. It checks all source hashes before and
after execution, repeats all836 emitted-angle and numerical-quality checks and
all ten controls, and requires exact JSON equality with the original results.
It invokes no estimator, SVD, alignment fit or inverse proposal. Imported
legacy helper modules define other routines; those routines are not called.

One additional post-known-outcome control appends a newline to an ISOLATED
copied target-source JSON and requires the frozen input-hash assertion to reject
it. Original source/capture bytes are never changed. The four original frame
verdicts and nested-ball exclusion remain unchanged and are not rerun or
superseded by this finite emitted-phase check.
