# Frozen independent canonical-identity test plan

Before implementation exercise, freeze a Python-int/Fraction oracle and the following expected mathematical outcomes. Inventory-schema adapters may be written after the CLI schema is supplied. No fit, new acquisition or large duplicate record is created.

Use a controlled known catalog containing the canonical fingerprint of Z=[[1,-2],[0,3]] and a zero1x3 matrix. Valid tests include:

- N=[[2,-4],[0,6]], b1, both C-order and Fortran-order NPY layouts: same typed bytes and LISTED fingerprint; wrapper file hashes may differ.
- N doubled with b increased1; N halved with b reduced1: same typed bytes and listed class.
- b changed without matching N: changed rational matrix and unlisted class for these nonzero fixtures.
- The original entirely even N at b0: exponent stays0 and numerators remain even; no negative canonical exponent.
- One changed entry, negative matrix, same flattened values in a different shape: different typed bytes and unlisted fingerprints in the finite examples. The shape1x4 case is valid despite m<n.
- Zero1x3 at b0 and b256: identical typed bytes and listed class; zero2x2 is a different typed object.
- INT64_MIN1x1 at b63 equals[-1],b0; at b256 yields canonical[-1],b193; at b64 yields[-1],b1. Mixed INT64_MIN plus odd1 prevents any cancellation.
- Mixed negative entries[-8,-4] at b4 and positive[8,4] at b4: exact Fraction/gcd results, no signed-OR valuation error.
- A duplicate known fingerprint under distinct IDs is valid; duplicate IDs reject.

For every valid listed or unlisted case, require independent_acquisition=NOT_ESTABLISHED, fresh_preparation=NOT_ESTABLISHED, provenance_status=HOLD_PROVENANCE_NOT_ESTABLISHED, numerical_spectral_certificate=NOT_EVALUATED and physical promotion0. A changed matrix must never promote physical freshness. A match must never declare acquisition reuse or reject an independent repetition.

Negative intake tests cover float/int32/object dtype, nonmatrix/empty/out-of-profile/truncated headers, negative or above-profile denominator bits, invalid CLI integer syntax, invalid catalog IDs/digests/schema, missing inputs, symlink file/ancestor and existing output or input/output overlap. Require no output creation or overwrite for invalid intake; preserve input/sentinel bytes. Record structured rejection versus argument errors or crashes distinctly.

Finite oracle controls will compare the gcd and individual-Fraction/least-common-denominator routes, including small scalar grids and the fixed matrix cases. Optional direct helper tests depend on the implementation's callable interface; CLI tests remain authoritative for recorded intake behavior. Canonical byte equality is the exact theorem; no universal SHA injectivity claim is tested or assumed.

Capture only standalone reviewer sources, expected-case/index records and receipts. Generated NPY fixtures/symlinks/execution trees remain transient; no large existing N record is duplicated. Actual known-record inventory fingerprints may be independently recomputed by streaming the existing files, without storing another full numerator/canonical matrix.
