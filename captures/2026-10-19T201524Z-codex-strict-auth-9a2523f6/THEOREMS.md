# Analytic predictor transfer and receipt authentication

Development — no registry entry. Physical Promotion=0; external review PENDING. The independent-policy assumption is explicit; the verifier cannot establish how a caller obtained its policy hash.

## Deterministic predictor transfer

Let Yhat be decoded acquired coordinates, Ys the frozen saved predictor, and Ya the exact declared analytic model on the SAME finite nominal grid, shape, channel order, metric and units. Suppose ||Yhat−Ytrue||F<=alpha and ||Ys−Ya||F<=beta. For r=||Yhat−Ys||F,

max(0,r−alpha−beta)<=||Ytrue−Ya||F<=r+alpha+beta.

The proof is the triangle inequality and reverse triangle inequality. The deterministic uncertainties ADD: sqrt(alpha²)+beta, not sqrt(alpha²+beta²). A predata cap applies to the new interval with the old strict contradiction versus non-strict consistency conventions. Overlap is HOLD. No uncertainty term may also be charged as the tested model mismatch.

The current extension actually checks beta against the finite harmonic formula Ya_a,k,c=b_a,c+sum_j[u_a,j,c cos(omega_j t_a,k)+v_a,j,c sin(omega_j t_a,k)]. Coefficients, frequencies and nominal time map are exact rationals; unspecified coordinates are zero. Validated512-bit Arb arithmetic encloses every scalar difference from the saved integer/denominator prediction. The finite Frobenius upper must fit the predata beta budget. This is a mathematical formula-to-predictor certificate, not a proof of physical correspondence, an all-time continuum guarantee or hardware-calibration truth. The harmonic target is independently hash/role-bound before scoring raw data; it is not refitted using that raw data.

The unmodified base verifier supplies exact acquired-vs-saved squared residual and deterministic acquired error squared from bytes. Gain/sign/offset and timing semantics remain the corrected model-coordinate convention in the parent v0.2 specification. This extension leaves all old gates/source caps unchanged and never reinstates a2^-49 residual gate or reuses the2^-38 shape gate.

## Authentication under a caller-pinned policy

A caller must independently provide BOTH the policy hash and the admission hash. The policy file must be outside the bundle. Its public-key-to-principal/role bindings, validity intervals, revocation state and synthetic/apparatus scope are the trust premises. A candidate cannot authorize its own key by placing a replacement policy in its bundle. This establishes no global identity directory and does not authenticate a policy that the caller copied blindly from an adversarial candidate.

The four Ed25519 receipts cover calibration, model, acquisition and lineage. Signed canonical payloads include a domain-separated version prefix, role, key ID, run ID,32-byte challenge, admission hash, claimed issue time and role-specific exact artifact hashes. Calibration binds the base contract/calibration; model binds the analytic model, prediction, grid and beta; acquisition binds the packet/raw/timestamps; lineage binds the packet and declared source/raw-dependency closure. Receipt ordering is acyclic because packet/core hashes exclude the separate signature-envelope file. Duplicate JSON keys, floating JSON numbers and invalid hexadecimal fields are refused.

The key policy, not a supplied receipt label, selects the principal and authorized role. Calibration and lineage principals must be distinct from the declared constructor and each other. Reusing the same public key under different principal IDs is rejected. The model receipt may be signed by the constructor to identify its own frozen mathematical model; it is not an independent model-review receipt. These rules enforce declared policy separation; they do not prove that different humans/institutions control different keys or that the declared dependency closure is complete.

A revoked key is refused even if its receipt claims an old signing time. The key must be valid both at its claimed issue time AND at the caller verification time; expired keys are refused even for claimed historical signatures, because no trusted timestamp proof is implemented. Key/receipt times and predata versus postdata role chronology are checked relative to an explicitly supplied verification time or runtime UTC. Claimed timestamps are not a trusted timestamp authority. A policy snapshot is valid only in its declared interval; no live revocation service is consulted. All chronology and identity claims remain conditional on that external trust process.

Cross-run/domain/challenge/contract/artifact reuse is rejected. An exact repeat of the same frozen bundle is deliberately idempotent. Stateless signature checks cannot prove one-use acquisition freshness; that would require an independently maintained trusted nonce-consumption log.

## Boundary

Signature verification establishes that supplied bytes verify under the caller's authorized public keys; it does not prove that the signed experimental statements are true. The analytic formula certificate likewise does not make the formula physical. Thus calibration_truth, heldout_independence and unaliased_identification stay NOT_CERTIFIED, and physical_verdict stays HOLD_UNQUALIFIED for every input.

All included signing keys are ephemeral synthetic fixture keys. Only public keys, signatures and signed payloads are retained. No private key is serialized/logged/captured, and replay neither signs nor generates keys. Fixture issue times are counterfactual test data, not historical preregistration. No real independently trusted apparatus keys, independent calibration receipts or hardware acquisitions were supplied.

The separate strict-family counterexample concerns one actual floating estimator output inside the PR233 input family. It does not falsify the ideal-SVD phase enclosure or establish physical failure. See the captured counterexample's exact lower-witness theorem and independent replay receipts.
