# Supplied projected-record verifier v1.0

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

This package computes every numerical premise anew from a supplied projected integer matrix and saved binary64 SVD factors. It has no model, generator, estimator, prior-certificate, nominal-tail, sector, repository or case dependency. It verifies finite supplied bytes, not acquisition authenticity, projection derivation, physical correspondence or all-input backend correctness.

## Invocation

Requires Python3, NumPy and python-flint. No floating SVD, fitting or matrix-exponential call occurs. To avoid writing Python caches, set PYTHONDONTWRITEBYTECODE=1.

```sh
python verifier.py --manifest /absolute/path/INPUT.json --out /absolute/path/new-output
```

The manifest root is its parent directory. Input file paths are relative to that root. The output must be a new directory, disjoint from each input and from the package. Existing output is never overwritten. Symlink components, absolute input paths and parent traversal are rejected. Do not put output under the package; an output sibling is acceptable.

```json
{
  "schema_version": "1.0",
  "record": {
    "path": "N.npy",
    "sha256": "64 lowercase hex characters",
    "payload_sha256": "64 lowercase hex characters",
    "dyadic_exponent": 55
  },
  "svd": {
    "path": "SVD_META.npz",
    "sha256": "64 lowercase hex characters"
  },
  "left_chunks": [
    {"path": "U_0.npz", "sha256": "64 lowercase hex characters", "start": 0, "stop": 2731},
    {"path": "U_1.npz", "sha256": "64 lowercase hex characters", "start": 2731, "stop": 5462},
    {"path": "U_2.npz", "sha256": "64 lowercase hex characters", "start": 5462, "stop": 8191}
  ]
}
```

The displayed hashes are placeholders, not a runnable record. Unknown/duplicate JSON fields are rejected. N.npy contains exactly one m×n little-endian int64 matrix N; its payload hash is SHA256 of canonical C-order little-endian int64 values, distinct from the entire NPY file hash. The real supplied matrix is Z=N/2^dyadic_exponent. SVD_META.npz has exactly singular.npy (n float64 values) and right_transpose.npy (n×n float64). Each left chunk has exactly basis.npy; declared intervals cover all m rows exactly once, in order. C-order and Fortran-order NPY arrays are supported; object/pickle arrays are forbidden. All full-file hashes and payload identity are checked, including after computation.

The record is memory-mapped read-only by this process. Before/after hash equality is not a universal snapshot or concurrent-mutation guarantee: another process could theoretically alter and restore bytes between checks. The mathematical result assumes stable supplied input bytes during execution, or an exact witness audit against the intended fixed record. The two exercised records have distinct per-run CRT audits; this does not turn the interface into a universal race-free intake mechanism.

## Frozen finite profile

PROTOCOL.json fixes the cutoff2^-24, full-list absolute-error gate2^-41, 180-bit outward dyadic root grid and resource profile before actual record recomputation. These are O03 protocol controls, not theory constants. The order q is inferred by counting saved singular values strictly above the cutoff; exact equality and q=0 or q=n are outside this verifier profile. The complete list must be finite, nonnegative and sorted. The leading-q condition enclosure is reported, with no generic1888 acceptance cap.

The supported profile has m>=n, m<=8191, n<=321, int64 record values, finite float64 factors, dyadic exponents<=256 and common encoded factor integers<=512bits. Some binary64 values, including sufficiently small subnormals, are intentionally outside this finite profile. Header/ZIP member counts, sizes, dtypes, shapes and uncompressed payload lengths are checked before materializing arrays. Per-entry/file caps are64MiB, total on-disk inputs128MiB and header16KiB. These checks are finite intake/resource guards, not a proof against every hostile platform input or a universal termination guarantee.

## Arithmetic and outputs

Every float is interpreted as its exact dyadic value. FLINT computes six integer sufficient-statistic matrices: M=NᵀN, K=NᵀUi, A=UiᵀUi, B=ViᵀVi, E=DiᵀDi−2^(2bD)I and H=DiᵀMDi. Exact trace identities give both forward and adjoint Frobenius squares without storing their large residual matrices. Packed symmetric witness entries count off-diagonal terms twice when summing squared norms. The discarded-output norm uses the fourth root of its output-Gram Frobenius square, not a square root. No negative exact squared norm is clamped.

The returned gate uses fresh left/right Gram defects, fresh forward and adjoint residuals, and a fresh discarded-span minmax tail. It checks strict leading-block matching and the actual cutoff count separately. See the accompanying proof and trace-identity review for definitions. No prior norm scalar or PASS metadata is accepted as arithmetic authority. A hash establishes byte identity, not a matrix-product proof; the separate per-run all-entry CRT audit supplies independent finite product evidence for the two exercised records.

CERTIFICATE.json contains exact rational pairs and readable approximations. WITNESS.json.gz deterministically stores exact integer matrices, norm squares and enclosures. RESOURCE.json reports host-dependent elapsed time and peak RSS; it is excluded from byte-identical scientific replay comparisons. The package allocates small projected matrices and sufficient statistics; it never constructs the full287GiB Hankel array. This is not an end-to-end acquisition/Hankel benchmark.

Exit0 and CERTIFIED_FINITE_SUPPLIED_RECORD require every numerical gate and input-unchanged check. Valid intake with failed numerical gates produces HOLD_NUMERICAL, exit2, with witness/certificate. Intake/schema/hash/resource/path failures return HOLD_INTAKE_OR_INPUT_IO, exit2, before numerical output creation. Unexpected execution failures return HOLD_EXECUTION, exit3; partial output may remain as failure evidence and must never be interpreted as a certificate. No alternate norm route, precision retry, cutoff relaxation or replacement case is selected on failure.

## Scope

Finite fixture/replay and independent matrix checks are evidence about exercised inputs, not a theorem of whole-program/library correctness or all-input backend conformance. The generic mathematical accepted-output theorem is conditional on the exact sufficient-statistic identities and scalar calculations. The certificate proves a cutoff count and ordered singular-value accuracy, not algebraic rankq, the full n×n condition, native1893/747 claims, SI/six-ratio accuracy, exact shift spectrum, or physical calibration. Same-team independent review is not external promotion authority. Existing HOLD/NO-GO decisions remain unchanged.
