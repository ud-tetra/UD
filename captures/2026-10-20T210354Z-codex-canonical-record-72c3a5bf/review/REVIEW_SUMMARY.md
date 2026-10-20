# Independent C21 canonical-identity review

The exact canonical-byte theorem and the finite implementation checks pass within the supplied-input identity scope. No mathematical correction or source change was required.

For Z=N/2^b, Python-integer gcd cancellation gives the unique least nonnegative power-of-two common denominator. Fixed-width shape/exponent fields and C-order little-endian int64 numerators then give identical canonical bytes exactly when shape and rational entries agree. The frozen proof handles zero matrices, denominator saturation at exponent zero, signed values and INT64_MIN. The independent oracle uses Fraction/gcd arithmetic rather than the implementation's signed OR and right shifts. SHA256 remains a cryptographic fingerprint; hash injectivity is not claimed.

Finite evidence:

| Review | Result |
| --- | --- |
| Fraction-versus-gcd oracle controls | 170 passed |
| Frozen CLI fixtures | 47 passed: 22 valid screens, 25 negative cases; 383 checks |
| Supplied original/alias/synthetic screens | 8 passed; 194 checks |
| Exact canonical-entry comparisons | Fortran/scaled aliases agree; each synthetic variant changes exactly one entry |
| Original SCREEN replays | Both byte-identical |

The fixture suite covers C/Fortran layout, scaling/reduction aliases, changed denominator, shape, signs, zero exponents up to 256, INT64_MIN, duplicate fingerprints under distinct catalog IDs, empty catalogs, invalid types/shapes/headers/catalogs, symlinks, missing input and output-overlap/no-overwrite behavior. Invalid cases exited 2 with no new output; the malformed command-line integer was rejected by argparse. Existing sentinel/input bytes were preserved. These are finite tests, not a universal program or race-safety proof.

The eight existing 8191-by-321 arrays were read in blocks without writing another large matrix. Both original fingerprints agree with the two-entry frozen inventory. Six screens are listed (two originals plus four layout/scaling aliases); two deliberately computed one-entry changes are unlisted. These synthetic changes are not acquisitions. All eight keep independent_acquisition and fresh_preparation NOT_ESTABLISHED, provenance HOLD, and numerical_spectral_certificate NOT_EVALUATED.

Numerical identity cannot establish acquisition independence. Conditional on two admissible histories with the same Z but different provenance labels, any function of Z, its canonical bytes or fingerprint gives the same output and cannot classify both correctly. This is an alternative-history impossibility argument, not evidence that any actual independent replicate exists. A match cannot prove replay, and an unlisted computed perturbation cannot prove freshness. A legitimately independent replicate might have the same projected matrix, including when hidden states differ invisibly.

The format identifies only numerical shape and exact rational entries. It does not encode physical units, basis/channel semantics, projection definition, raw acquisition, factors, preparation, hidden state or history. Equal numerical arrays across different physical settings are not thereby the same physical object; a catalog match must not merge their evidence. Coordinate-basis/unit/projection receipts in a development checklist are not part of the executable schema and were not validated here.

The code's before/after hashes check endpoint stability. The review assumes stable inputs during each run; it does not establish an immutable snapshot against concurrent mutation. The source-seal and input hashes bind the observed finite executions. No new acquisition, model construction, estimator call, numerical spectral certificate, physical promotion or universal backend guarantee follows.

Development — no registry entry. Same-team independent review; external promotion review PENDING. All-input/backend conformance and acquisition authenticity remain OPEN. Physical Promotion = 0.
