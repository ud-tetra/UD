# Executable supplied-record handoff v1.0

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

This runner connects the unchanged PR294 identity screen, PR291 v1.1 exact numerical verifier, and PR291 distinct CRT/product auditor. It accepts a full numerical manifest and verifies the same supplied record through all three stages. It does not accept an externally supplied PASS certificate as an executable input and does not adjudicate acquisition independence.

```sh
python run_submission.py --repo /path/to/UD \
  --manifest /path/to/numerical/INPUT.json --out /path/to/new-output
```

Requires Python3, NumPy and python-flint, as required by the pinned child tools. The repository argument locates the exact capture-relative dependency paths in DEPENDENCIES.json. It may be an equivalent directory tree with those same source bytes; no Git operation or network access occurs inside the runner. The runner's source/protocol/dependency seal and all13 dependency-file hashes must match. A changed dependency requires an explicit versioned update, not an automatic branch/source substitution.

## Intake and execution

Before output creation the runner checks source pins, paths and the complete supplied numerical manifest through the pinned verifier's intake. That validates source file hashes, payload identity, numerical shapes/dtypes/profile, cutoff order and chunk coverage. This preflight performs no estimator call, SVD or fit. Its temporary arrays are discarded before subprocess execution. Bytecode writes are disabled for pinned imports and child processes.

Output must be a new directory outside the supplied repository, source package and enclosing immutable capture, and must not cover any input. Existing output and symlink components are rejected. No source or input is rewritten. The finite resource profile is inherited from the pinned numerical verifier; the600-second per-child timeout is an O03 execution control, not a theory constant.

Execution order is fixed:

1. `identity/SCREEN.json`: bind the original record bytes, denominator, dimensions, numerical payload and fixed catalog/source identities. Check fingerprint/class/matching-ID consistency against that catalog. Both listed and unlisted identities are permitted; neither is provenance approval.
2. `numerical/CERTIFICATE.json` and `WITNESS.json.gz`: recompute fresh exact Gram, forward, adjoint and tail premises from the supplied record and saved factors. Require the certified finite status, all eight strict boolean gates, exact source/input identities and the witness hash. A numerical HOLD stops execution before the auditor; there is no retry, alternate precision, fit or replacement record.
3. `audit/CERTIFICATE.json`: execute the distinct implementation's exact per-record products and scalar checks. The auditor may exit0 while reporting HOLD, so its exit code alone is insufficient. Require actual six-matrix CRT PASS, full entry coverage, adequate bound/product checks, matching scalar gates/metrics/bounds and exact producer-certificate/witness/source/input bindings.

Endpoint source/input and stage-artifact hashes are rechecked. `ROLLUP.json` records invoked stages, source/input identities and artifact hashes. `*_PROCESS.json` and RESOURCE files retain process results/timings. Status validators check result consistency and bindings; they are not standalone mathematical verifiers for arbitrarily fabricated reports. Their authority in this workflow depends on execution of the pinned child sources against the same stable inputs.

## Terminal states

| Condition | Workflow status | Exit | Provenance |
|---|---|---:|---|
| Intake/source/path failure before output | HOLD_INTAKE_OR_SETUP on stdout |2|HOLD|
| Identity step fails or its report is inconsistent | HOLD_IDENTITY_STEP |2|HOLD|
| Numerical step fails, holds or has invalid bindings/gates | HOLD_NUMERICAL_STEP |2|HOLD|
| Distinct audit fails, holds or has invalid product/scalar bindings | HOLD_AUDIT_STEP |2|HOLD|
| Endpoint source/input/artifact check fails | HOLD_BINDING_CHANGE |2|HOLD|
| Every numerical and binding condition succeeds | NUMERICAL_PASS_PROVENANCE_HOLD |0|HOLD|

Unexpected I/O failures can leave partial output as failure evidence; never infer whole-workflow success from the existence of one child certificate. Only the complete successful rollup describes numerical handoff success, and it still retains HOLD_PROVENANCE_NOT_ESTABLISHED, independent_acquisition=NOT_ESTABLISHED and fresh_preparation=NOT_ESTABLISHED.

The rollup declares no automatic registry/physical promotion. Same-team independent development review is not external promotion authority. The numerical result is finite supplied-record evidence, with stable inputs and stage artifacts assumed. Before/after hashes do not provide atomic snapshots or exclude modification-and-restoration races. All-input/backend/library/whole-program correctness remains OPEN.

## Data and provenance obligations

Numerical identity omits physical units, basis/channel meaning, the projection map and acquisition history. Matching numbers do not merge those typed objects. A listed projection can be an independent replicate; an unlisted projection can be synthetic. Consult PR294's conditional nonidentifiability proof and submission checklist for the external source/preparation/raw/projection/coordinate-unit receipts required separately.

The exercised large records are the same two PR291 computational projections with their original saved factors. Their successful runs are repeated numerical verifications, not new record identities, new estimator fits, blinded acquisitions or physical calibration. The small fixtures are explicitly synthetic. Original numerical/identity/audit sources remain unchanged, including prior error gates and HOLD/NO-GO findings. No full Hankel matrix is constructed, and this is not a benchmark of raw acquisition, projection or SVD proposal generation.
