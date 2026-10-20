# Canonical projected-record identity screen v1.0

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

This screen identifies a supplied real dyadic matrix Z=N/2^b relative to an explicit finite fingerprint catalog. It prevents file repackaging or equivalent dyadic encodings from being mistaken for new projected matrices. It does not determine whether a physical acquisition or preparation is independent, whether a hidden bulk state differs, or whether saved spectral factors are accurate.

Identity here means equality of numerical matrices in declared coordinates. The byte format does not encode physical units, basis semantics, channel meaning, the projection map or acquisition history. Equal numbers in different typed settings are not the same physical object. Bind those coordinate/unit/source receipts separately; a fingerprint match must not merge their evidence or provenance.

## Canonical identity

For nonzero integer N, let t be the smaller of b and the minimum power of two dividing every nonzero entry. Define Nbar=N/2^t and bbar=b−t. For zero N, use Nbar=0,bbar=0. Serialize the following exact bytes:

1. ASCII `UD_DYADIC_MATRIX_V1` followed by one zero byte;
2. shape m,n as little-endian unsigned32 integers and bbar as a little-endian unsigned16 integer (`<IIH`);
3. Nbar in C-order signed little-endian int64.

Equal canonical bytes are equivalent to equal shapes and exactly equal rational matrices. SHA256 of these bytes is a cryptographic fingerprint; the mathematical theorem does not assert that a finite hash is injective. The signed-OR/right-shift implementation avoids `abs(INT64_MIN)` overflow. Independent review uses Python integer gcd/division rather than the producer algorithm.

A C-order or Fortran-order NPY containing the same values gives the same fingerprint. Replacing (N,b) by (2N,b+1), when the new numerator fits int64, also preserves it. Changing b without a compensating numerator change generally changes Z and its identity. Matrix dimensions remain part of the identity even for zero matrices.

## Invocation

Requires Python3 and NumPy. Set PYTHONDONTWRITEBYTECODE=1 to avoid caches when invoking archived source. Use a new external output directory.

```sh
python screen_record.py --record /path/N.npy --denominator-bits 55 \
  --known /path/KNOWN_RECORDS.json --out /path/new-screen
```

The record is a two-dimensional little-endian int64 NPY. C and Fortran layout are accepted. Shapes satisfy1<=m<=8191,1<=n<=321;0<=b<=256. This identity profile does not itself check the additional m>=n or factor requirements of the numerical verifier. Header<=16KiB and file<=64MiB limits are checked before memory mapping. Paths with symlink components, output overlap, existing output and output under this source package or an enclosing immutable capture are rejected. The finite profile and resource caps are O03 controls, not theory constants.

Catalog schema:

```json
{
  "schema_version": "1.0",
  "identity_format": "UD_DYADIC_MATRIX_V1",
  "coverage": "An explicit statement of this finite catalog's coverage",
  "records": [
    {"record_id": "label", "fingerprint_sha256": "64 lowercase hex characters", "source_reference": "source reference"}
  ]
}
```

The shown hash is a placeholder. Unknown/duplicate JSON fields and duplicate record IDs are rejected. Different record IDs may legitimately share a fingerprint, for example separate acquisitions of the same projected matrix. The included KNOWN_RECORDS.json covers only the two PR291 matrices. A custom catalog changes the comparison scope; its SHA256 and coverage are reported. Catalog statements and source references are metadata, not executable instructions or independent evidence.

SCREEN.json reports LISTED_FINGERPRINT or UNLISTED_FINGERPRINT, matching catalog IDs, source file/payload identities and the canonical fingerprint. Both valid classifications exit0. This means the screen completed, not that provenance passed. Both retain HOLD_PROVENANCE_NOT_ESTABLISHED, independent_acquisition=NOT_ESTABLISHED, fresh_preparation=NOT_ESTABLISHED and numerical_spectral_certificate=NOT_EVALUATED. Malformed intake exits2 without creating output; unexpected execution failure exits3. RESOURCE.json is timing metadata, excluded from deterministic replay comparison.

The input payload hash records the original numerator values in canonical C-order, before dyadic normalization. It is deliberately distinct from the normalized matrix fingerprint and entire NPY file hash. Before/after digests are endpoint checks; stable input bytes during execution are assumed. They do not prove atomic snapshots or exclude concurrent modification and restoration. Finite tests do not establish universal intake/backend/program correctness.

## Submission and review sequence

SUBMISSION_TEMPLATE.json is a development checklist, not an executable schema or registered protocol. Complete it from actual source receipts; do not infer timestamps, operator identities, raw-data provenance, units or independence from numerical agreement.

1. Bind supplied raw/preparation/projection evidence and its declared source to the exact numerical manifest. Preserve original inputs.
2. Run this identity screen against the declared catalog. An unlisted fingerprint establishes no independent acquisition. A listed fingerprint is compatible with either a replay or an independent replicate giving the same projection; it is no numerical rejection.
3. Run the unchanged PR291 v1.1 numerical verifier on the full manifest and saved factors. The identity screen supplies none of its Gram/residual/tail premises.
4. Have a separate implementation audit the exact products and scalar bounds for that supplied record. The prior two audits do not automatically transfer.
5. Adjudicate acquisition/preparation independence, instrument-to-model mapping, protocol pre-registration and any physical claim separately through non-constructor review and custodian ruling. Numerical acceptance alone advances none of them.

No new estimator call, physical acquisition, fresh preparation, SI/six-ratio result, algebraic rank claim or native1893/747 interpretation follows. Prior HOLD/NO-GO decisions remain unchanged.
