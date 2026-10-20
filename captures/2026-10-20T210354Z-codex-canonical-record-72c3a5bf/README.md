# Canonical numerical matrix identity and independent-record handoff

Development — no registry entry. Ledger v0.39 / CRL-2. External promotion review PENDING. Physical Promotion=0.

The next step after PR291 is ready for supplied records: a sealed canonical dyadic-matrix identity screen and an explicit source/preparation handoff checklist. No new independent acquisition record was supplied. All actual exercises use the two old projected matrices or declared synthetic variants; all provenance verdicts remain HOLD.

## Exact identity and its limit

For Z=N/2^b, remove common numerator powers of two up to b; normalize the zero matrix to denominator exponent0. The byte format binds a domain tag, shape, normalized denominator and C-order little-endian int64 normalized entries. Equal bytes are equivalent to equal shapes and exact rational matrices. SHA256 is a cryptographic fingerprint of those bytes, not an injective mathematical code. The supplied profile is finite, with protocol limits in identity_screen/PROTOCOL.json.

The screen compares only numerical matrices, not units, basis/channel meaning, the projection map, raw records, hidden states or histories. Equal numbers do not imply equal typed physical objects. The known catalog contains only two PR291 reference matrices; UNLISTED means unlisted relative to that exact finite catalog, not globally novel or independently acquired.

Two conditional counterexamples close the interpretation gap. A replay and an independent replicate may give exactly the same Z, so a matrix-only test cannot distinguish their histories when both are admissible. Conversely, a synthetic one-entry change can create an unlisted Z with no acquisition at all. Neither a listed nor unlisted fingerprint establishes preparation or acquisition independence. No actual independent replicate is asserted by this hypothetical-history proof.

## Exercised records

| Input class | Screens | Identity result | Provenance |
|---|---:|---|---|
| Original PR291 projections |2|Listed|HOLD|
| C/Fortran layout and equivalent(2N,b+1) aliases |4|Listed|HOLD|
| Controlled one-entry changes |2|Unlisted|HOLD|

The two original screens replay byte-for-byte; timing RESOURCE files are excluded. The distinct reviewer freezes proof/fixtures, uses Python gcd/division and Fraction arithmetic rather than signed OR/right-shift, checks the actual reference/alias identities, and tests intake/failure boundaries. All47 frozen fixtures pass383 checks;170 Fraction/gcd oracle controls and194 actual-case checks pass. Direct canonical entry comparisons independently confirm alias equality and one-entry mutations. Exact bindings are in review/FINAL_REVIEW_RECEIPT.json. This is same-team independent review, not external promotion authority. Finite tests do not establish all-input/backend/library/whole-program or race correctness.

## Handoff

identity_screen/README.md defines the format, CLI, finite catalog schema and all status meanings. A valid screen exits0 even though provenance stays HOLD; this is successful identity screening, not numerical or physical acceptance. Malformed intake exits2 without creating output. Inputs must remain stable during computation; before/after hashes are endpoint checks, not an atomic snapshot guarantee.

identity_screen/SUBMISSION_TEMPLATE.json is a development checklist, not an executable validator or registered protocol. It calls for actual raw/preparation/projection/coordinate-unit receipts, the complete PR291 numerical manifest, subsequent product/scalar audit and external provenance review. Missing evidence must remain explicitly unavailable; declarations and matching numbers are no substitutes.

The PR291 v1.1 spectral verifier remains unchanged. Its earlier two numerical certificates do not transfer to a newly supplied matrix or different saved factors. A new supplied manifest must pass that verifier and its own distinct per-record product/scalar audit. A catalog match is no numerical rejection: an independently documented replicate could legitimately have the same projection.

## Inputs and reproduction

Run screen_record.py using explicit --record, --denominator-bits, --known and a new external --out. Its source/protocol/two-record catalog seal is in identity_screen/SEAL.json. Existing N inputs and generated alias files are not duplicated into git; root/CASE_RECEIPT.json records exact identities, origins and temporary execution paths. root/run_cases.py and build_known.py document construction and execution against the pre-existing PR291 projected inputs. Their original workspace paths are historical execution provenance and need explicit relocation for a different workspace; the CLI itself has no repository/case/model dependency. review/ contains safe standalone source/receipts; generated fixture/execution trees and symlinks are excluded.

No estimator calls, new numerical spectral certificates, raw/projection reconstruction, fresh preparation, physical acquisition, outreach or full-Hankel allocation occur. Prior HOLD/NO-GO decisions, native1893/747 interpretations, SI/six-ratio accuracy and exact shift-spectrum obligations are unchanged/open. No Project-board/public-site update is asserted.

Governance inputs are the exact supplied Ledger v0.39 and CRL-2 bytes. Numerical representation/resource choices are O03 controls, not theory constants. No new mathematical retraction; a session-wide retraction ratio is not computable from a scoped capture. Gap2_FINAL_Finite_Genesis.png remains unavailable/unused; re-upload if it should be included. Notes/ASTER are available but unused. Publication, CI, merge and tracking results are reported after completion.
