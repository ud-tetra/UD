# Analytic-predictor allowance and signed-evidence design

Development — no registry entry. Same-team design/adversarial review. Physical Promotion=0. No actual public-key identity authority, physical data, independent calibration evidence or outside reviewer has been supplied. Synthetic signature fixtures can validate cryptographic byte checks; they do not establish measurement truth or physical independence.

## Analytic target and error allowance

Let Yhat be decoded ADC data, Ytrue the unknown noiseless apparatus coordinates, P the exact saved predictor artifact, and Yideal a named analytic prediction in the same coordinate/time grid, channel order, shape and raw Frobenius space. Independent premises are ||Yhat-Ytrue||F<=alpha_acq and ||P-Yideal||F<=beta. Then

alpha_total=alpha_acq+beta,
max(0,||Yhat-P||F-alpha_total)<=||Ytrue-Yideal||F<=||Yhat-P||F+alpha_total.

The sum is deterministic. sqrt(alpha_acq²+beta²) is unjustified without stronger structure and can understate error. Preserve exact acquisition squared norm, separate beta and an outward total-error enclosure; the total square need not be rational. A predata nonnegative rational beta may be an already conservative upper endpoint. Zero beta requires an actual exact-predictor premise, not a default for missing evidence.

The contract must freeze analytic model/target ID and version, model/source coefficients, time schedule/hash and interpolation convention, finite horizon, units, norm, shape, saved-predictor hash and denominator, the beta value and evidence hash before scored validation. A bound for another shape, time schedule, frequency branch, unit or projected space is not transferable. An analytic truncation/discretization bound is distinct from gain/time/processing uncertainty; do not subtract the same source discrepancy twice.

A signature can attest a supplied beta but does not prove it numerically. If the verifier does not implement a proof/envelope checker, return analytic_error_bound=SIGNED_ASSUMPTION_NOT_REDERIVED and make the mismatch conclusion conditional on beta. If it checks a finite interval envelope, report the precise grid/region and premises, not an unrestricted analytic or physical theorem. A larger beta can turn contradiction into HOLD; it cannot create stronger evidence. A beta or cap revised after validation is a new disclosed contract.

Retain the existing frozen saved-predictor-only lane or introduce a new explicit analytic-target version. Missing analytic bound/evidence must HOLD an analytic claim. Neither version grants209-clock membership, old frame/phase gates, native1893 rank, unaliased identification or physical qualification.

## Caller trust boundary

Require an external trust-policy file plus its independently caller-pinned expected SHA, and separately a caller-pinned expected contract SHA and run/challenge. The scored bundle cannot choose its own trusted key, append a public key to become trusted, override key roles or select a replacement policy. A public key included in a signature envelope is informational only unless it equals the policy-authorized key. No fallback to a bundled policy or fixture key is permitted.

The pinned policy declares an allowed signature algorithm/version; unique key IDs and exact key bytes/fingerprints; principal IDs; authorized roles; constructor principals; key validity intervals; revocation; policy validity/verification epoch and receipt-expiry rules. Reject unknown/duplicate key IDs, malformed key bytes, ambiguous principal mappings, wrong role/algorithm, revoked keys and keys outside the required validity window. The external caller is responsible for the policy's identity authority, completeness and freshness. A key ID or principal string is not independently authenticated merely because policy JSON contains it.

Check constructor separation at principal level, not only key inequality: different keys may belong to the same constructor. If the protocol requires independent roles, explicitly freeze which signer principals must differ. Do not infer independent humans from distinct public keys. A caller-pinned policy may assert those mappings, but their physical truth remains an external premise.

## Signed message binding

Choose one specified canonical byte format, or sign exact payload bytes with strict parsing. Reject duplicate JSON keys, nonfinite values, unsupported fields/versions or ambiguous integer/Unicode encodings where cross-implementation interpretation could differ. Use an explicit domain/version prefix and bind role within the signed payload. A suggested context is UD_APPARATUS_EVIDENCE_RECEIPT_v1, followed by the fixed serialization.

Every signed payload includes role, authorized key/principal identity, contract SHA, run/challenge ID, artifact/version references, claimed issuance/expiry and the role's complete scope. Verifier comparisons use the independently pinned expected values, not values copied unchecked from the same receipt.

Calibration/model receipts occur before acquisition under declared chronology: calibration signs its calibration artifact, domain/time coverage and source lineage; model signs saved predictor, analytic target, beta/evidence, model/preparation dependencies and contract. They cannot bind unknown future raw hashes. Acquisition and lineage receipts are postdata: bind the exact scored ADC, timestamps, immutable packet core, preparation/run identifiers, acquisition start/end, declared dependencies and relevant model/calibration receipt references. Artifact/hash/role/domain substitution must invalidate admission.

Avoid circular signing references. Define a packet core that excludes signature envelopes. Contract pins predata predictor/calibration/beta/run context; predata receipts sign that context. Postdata receipts sign the packet core and predata receipt hashes. The outer packet references signatures; a receipt does not sign an outer packet hash that includes itself.

Verify every required role independently and retain the mapping from receipt to trusted key/principal and exact covered artifact hashes. A valid acquisition signature cannot replace calibration/model/lineage roles. A valid signature over the wrong role or unrelated contract is not partial admission.

## Time, revocation and replay

Receipt issuance dates are signer statements, not proof of actual signing time. Enforce supplied chronology and key/receipt validity against an independently selected verification epoch/policy; still report trusted-time authenticity unverified unless a real timestamp authority is implemented. A minimal conservative policy rejects a revoked key even if the receipt claims an earlier issuance. Do not accept backdating to bypass revocation merely because a signed timestamp string is well formed.

Pin policy version/freshness externally. A correctly signed stale policy cannot be recognized as obsolete without an external current-policy premise. Test wrong policy hash, expired policy and revoked keys separately.

Contract/run/challenge/domain/artifact binding prevents cross-context replay. Exact replay of the same bundle is intentionally idempotent for a read-only verifier. At-most-once acquisition freshness needs independently trusted nonce-consumption state or a fresh external challenge; it does not follow from a stateless signature. Do not claim live measurement freshness or replay prevention beyond the implemented context checks.

## Conditional result separation

Report signature_validity=VALID_UNDER_CALLER_PINNED_POLICY only when all checks pass. Separately report principal_identity=POLICY_DECLARED, receipt_claim_truth=NOT_CERTIFIED, calibration_truth=NOT_CERTIFIED, heldout_independence=NOT_CERTIFIED, source_family_membership=NOT_CERTIFIED and physical_verdict=HOLD_UNQUALIFIED. A real-world identity claim requires external evidence beyond this parser. A conditional numeric mismatch result may coexist with these limits; no signature or beta allowance promotes it into a physical result.

Holdout lineage still requires declared disjoint calibration/model-fit and scored validation ancestry, with raw-hash overlap checks. Signed lineage authenticates the policy-authorized signer's statement, not its truth or completeness. Predictor/initial-state fitting on the scored future trace remains contamination even if a signer attests it. Independent calibration cannot be created by signing constructor-generated evidence with another key.

## Prospective adversarial controls

Use explicitly synthetic test keys, clearly labeled non-production, and an externally pinned fixture policy in the frozen test index. The fixture author knowing the test private keys is expected and cannot be called independently authenticated apparatus evidence. Do not expose or capture real private keys or credentials. Freeze recipes/code/expected outcomes before evaluation; no real trust policy/key has been supplied.

| Control | Expected result |
|---|---|
| Valid four-role synthetic envelope, beta0 | Cryptographic/conditional numeric check can pass; physical HOLD |
| Valid analytic beta changes contradiction to overlap | Numeric HOLD with alpha_total=alpha_acq+beta, not an upgraded cap |
| Missing/negative beta, wrong unit/norm/shape/schedule/target | HOLD analytic claim |
| Beta/evidence or saved predictor changed after signing | HOLD binding/signature |
| Missing required role or duplicate receipt substituted for another | HOLD |
| Correct signature under self-supplied/untrusted key or wrong pinned policy | HOLD |
| Valid key signs wrong role/domain/contract/run/challenge | HOLD |
| ADC/timestamps/calibration/model/lineage artifact mutation | HOLD |
| Revoked/expired/not-yet-valid key; receipt outside key or policy window | HOLD |
| Constructor key under another key ID; second key of same constructor principal | HOLD separation |
| Distinct principal/role fixture keys | Only policy-declared separation, no true human-independence claim |
| Raw dependency overlap in otherwise signed lineage | HOLD heldout claim |
| Duplicate JSON key, unsupported algorithm, malformed signature/key | HOLD |
| Same frozen bundle reverified | Same idempotent result; no one-use freshness claim |
| Fresh contract/run with replayed old role signatures | HOLD context binding |
| Synthetic complete envelope labeled apparatus_submission | No physical qualification, actual identity authority still absent |

Useful exact analytic arithmetic fixtures can reuse small frozen saved-predictor data with a separate rational analytic target: one coordinate discrepancy beta, a same-direction acquisition error to show the SUM is necessary, and a cap-boundary/overlap case. Expected residual/error fractions should be derived independently from the saved artifact rather than produced as prediction-plus-random-noise. Existing deterministic processing/sign/timing controls should remain intact.
