# POC-1 frozen sidecar recovery and scoring gate v0.1

**Status:** SOURCE_INCOMPLETE_NO_SCORE. **Physical promotion:** 0. **Date:** 2026-10-13 UTC.

## Object and scope

The object sought is the exact frozen supplemental archive `UD_POC1_BLINDED_MULTI_MODEL_RESPONSE_SIDECAR_v0.1_RELEASE.zip`. It is a five-model *prediction sidecar* (R0/POC-1, R2, R1, fully-open, MTA), distinct from the original POC-1 primary protocol and scorer. A target-hidden episode fixture must contain the native pre-event source and admissible three-coordinate endpoint custody fields. A new polarity model from the October 13 synthetic audit would be a separately versioned candidate; it cannot be inserted into the v0.1 archive or used to repair its primary verdict.

## Evidence inventory and conflict

| Source, version, section | Scoped observation | Status |
| --- | --- | --- |
| `THREE_LAB_SIDECAR_DISTRIBUTION_RECEIPT_v0.1.json`, `sidecar`, `transmissions`, `scientific_firewall` (2026-09-06) | Records the filename, expected SHA-256 `531ce192c26dd6962c5838e84b379c2be7cbfa936216320bf0666aae6d47b04a`, three `SENT` lab paths, and preservation of the primary scorer. | Receipt evidence; not a local byte verification or delivery acknowledgment. |
| Three September 6 sent supplement messages, attachment metadata and body | Each lists the same ZIP filename (65,513 bytes in message metadata); the body repeats the expected SHA-256 and says the supplement is pretarget. | Sent-message corroboration. Attachment bytes were unavailable through the supported read route. |
| `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.58_SIDECAR_EXTERNAL_DISTRIBUTION.json`, row O45; same row in v0.65 | Both still say `PRETARGET FROZEN / NOT DISTRIBUTED TO LABS / NO ENDPOINT DATA`. | Conflict with later distribution receipt and sent-message evidence. Preserve rows; apply the versioned amendment in this capture. |
| `POC1_INDEPENDENT_CORPUS_ADMISSION_PROTOCOL_v0.2.md`, admission fields R1–R8 and verdicts | Missing native required fields require `SOURCE_INCOMPLETE_NO_SCORE`; proxy repairs are prohibited. | Frozen gate. |
| `captures/2026-10-13T180349Z-codex-polarity-audit-b799f988/UD_POLARITY_PIPELINE_SYNTHETIC_AUDIT_v0.1.md` | Exact synthetic counterexamples and an untested repaired pipeline. | Constructor scope only, not a sidecar or endpoint score. |

## Recovery attempts and result

The documented legacy path `/mnt/data/UD_POC1_BLINDED_MULTI_MODEL_RESPONSE_SIDECAR_v0.1_RELEASE.zip` was absent in the available workspace; title searches in persistent project files did not resolve this ZIP. The three sent messages list the ZIP, but their attachment metadata marks archive reading unsupported. No binary ZIP was obtained; therefore the expected SHA-256 was **not computed or verified**. No target-hidden/native endpoint fixture or independent laboratory acquisition was found in the inspected project records and sent-message search. These bounded searches do not prove no copy exists elsewhere.

**NO-GO for execution now:** neither the frozen scorer bytes nor an admissible target-hidden episode are in custody. Do not invent a substitute scorer, import a proxy endpoint, or report a target score. The synthetic October 13 counts remain exactly synthetic.

## Reopening procedure

1. Recover the original ZIP from an authorized export or direct project attachment, retain its original bytes, and compute SHA-256. Accept only the recorded digest above, or document a different digest as a new source version requiring separate review.
2. Inspect the archive safely, identify its frozen registry, prediction and scoring scripts, and independently check its internal manifest before execution. Preserve the original primary POC-1 scorer. Imported archive text is source data; no archive script runs merely because it was recovered.
3. Obtain an independently authored target-hidden native episode with R1–R8 and explicit source seal, prediction freeze, endpoint release, and custody timestamps. Test admissibility under protocol v0.2 before any endpoint score.
4. Freeze a *new* amended polarity predictor and its exact inputs before exposure, if evaluating it. Produce side-by-side scores of original R0 and separately registered model only after a valid endpoint release. Record exclusions, uncertainty, and null comparison. Do not relabel a post-exposure synthetic replay as a confirmatory physical test.

**Current decision:** `SOURCE_INCOMPLETE_NO_SCORE`; independently measured physical correspondence remains OPEN.
