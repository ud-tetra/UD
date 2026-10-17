# Non-constructor review packet: noisy record-only extraction

**Unassigned. Development — no registry entry. Physical promotion: 0.**

This packet is ready for someone other than the constructor to inspect. It records no completed independent review, custodian ruling, apparatus run or CRL advancement. The attached CRL-2 amendment is explicitly a governance proposal; its independence requirement is preserved here without treating constructor checks as promotion evidence.

## What changed

The previous record-only proposer used a relative temporal singular-value cutoff. Several bounded noise records fill its 160-column sketch with small nonzero singular values, so it cannot discover the useful temporal order. A coherent constant offset creates a different failure: the old per-block relative cutoff retains 37 stationary directions, increasing the proposed real rank from 1893 to 1929.

The new version uses two untrusted numerical choices:

1. An absolute temporal cutoff derived from the frozen vector-error budget and a deterministic sketch-norm envelope.
2. A global rank-1893 allocation across modal blocks, respecting the two-real-dimension cost of each positive-frequency complex direction.

Choosing a rank-1893 approximation does **not** establish a rank-1893 signature. The full-record residual, both actual factor Grams, exact Cholesky/SVD residuals and the unchanged acceptance rule still have to pass. Any discarded nonzero mode remains in the temporal-frame bound used for truncation error. A deliberately narrow retained frame cannot hide the discarded temporal content.

## Claim A: uniform temporal separation

Let the time-by-output record matrix be `D`, with 8191 rows and `37·62` output columns. The sketch `W` has 160 columns and entries `±1/64`. Each 62-vector perturbation has norm at most `delta=2^-20`, giving

\[
\|E\|_F\leq\sqrt{37\cdot8191}\,\delta,\quad
\|W\|_2\leq\|W\|_F=\frac{\sqrt{37\cdot62\cdot160}}{64}.
\]

Thus `||(D-D0)W||2 <= eta`, with the exact squared envelope recorded in `DISCOVERY_GAP_CERTIFICATE.json`. The baseline sketch is formed with exact integer products. Its 160-by-160 Gram and eigen-residual certificate show

\[
\sigma_{105}(D_0W)>3\eta,\qquad\sigma_{106}(D_0W)<\eta.
\]

Weyl then implies exactly 105 singular values above `2 eta` for **every** perturbation in this additive vector-error ball. This is a statement about the exact finite sketch spectrum. It does not by itself certify frequency estimates, spatial-rank allocation, optimizer convergence or the full native calibration family. The baseline finite record is not claimed to have exact algebraic temporal rank 105.

## Claim B: full noisy-record certificates

Four predeclared cases receive fresh record-only proposals and complete exact/interval spectral verification: dense signs, coherent DC offset, rational ramp and a single-vector impulse. These are constructed digital controls, not measurements. The single-vector impulse tests the global vector bound alone and exceeds the sufficient per-scalar ceiling; no full acquisition-budget membership is claimed for it. All input readings, hashes and exact per-vector budgets are preserved or reproducible from recipes.

The complete frozen threshold, rank target and condition cap remain unchanged. Inspect `FULL_CERTIFICATE_RESULTS.json` and each `CERTIFICATE.json`; proposal success alone is insufficient. A fifth bounded periodic-clock case is tested at the proposal stage only. Its numeric signature also follows conditionally from the separately established perturbation theorem and its verified vector budget; its fresh proposal has not received a full certificate in this campaign.

The out-of-budget strong central impulse is a negative control. It yields no accepted proposal, and the prior rank-perturbation argument independently proves an actual signature breach. A numerical HOLD on any other input must not be interpreted as physical failure or hidden-kernel leakage.

## Required review actions

- Reconstruct the baseline payload losslessly and verify its SHA-256. Independently regenerate and difference-scan all noise records; check vector norm budgets with exact integers.
- Check the implementation freeze, code hashes and original contract hash. Verify that no acceptance threshold or target was retuned after outcomes.
- Inspect record-only data access. The proposer/verifier must not load nominal operator, preparation, root or modal files. The lossless codec is only an input transport; every integer residual is retained.
- Audit the uniform sketch bound, the exact integer overflow bound, Gram scaling, eigen-residual polar correction and Weyl inequalities.
- Audit global paired rank allocation. Verify zero-rank blocks and inclusion of discarded nonzero temporal modes in the truncation-frame bound.
- Recompute all four complete spectral certificates. Check that they enclose the **encoded finite record**, rather than the underlying physical process or continuous generator.
- Run the regression cases and add an adversarial case chosen by the reviewer. Preserve every HOLD, failure and rejected run.
- Review the limitations: only additive vector-bounded noise is covered by the uniform temporal statement; broader calibration/model-family errors, future prediction, generator identification and physical units require separate evidence.

Record reviewer identity, independence, exact hashes reviewed, reproductions, objections and a PASS/HOLD/REJECT disposition in `REVIEW_TEMPLATE.json`. A custodian ruling, if later authorized, is separate. No messages or invitations have been sent.
