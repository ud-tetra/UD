# Disposition of the submitted review artifacts

**HOLD — the independent-review gate remains open.** Physical promotion remains **0**. This intake audit was performed by the numerical-package constructor and is not a replacement independent review.

Both submissions are preserved, package by package, as transcriptions of the pasted material. No source package, previous numerical certificate or original reviewer claim has been overwritten.

## Byte binding

| Submitted manifest | Existing target paths | Matching hashes | Mismatching hashes | Additional review files absent from frozen target |
|---|---:|---:|---:|---:|
| Noisy campaign v0.1 | 12 | 0 | 12 | 2 |
| Record-only certificate v0.2 | 12 | 0 | 12 | 2 |

All supplied digest strings have valid SHA-256 syntax. Their values do not match the referenced files in the actual delivered archives. The archive entries also agree with the immutable repository capture bytes. For example, the noisy campaign contract actually hashes to `ba28c60cffd40806d3ecd76bf83db7b2caac71de9173b0de7a471b504e84d20c`, not the submitted value beginning `fe12a8f7`. The record-only spectral certificate hashes to `fd154e00ac7872e09b6e7ea67dcab545d1d25252d798f042a593a6c0d66c9afd`, not the submitted value beginning `19b6bf73`.

These differences prevent binding the claimed review to the named frozen bytes. They do not establish the reason for the differences or prove that no review occurred. A different reviewed revision must be identified explicitly.

The two new review files per submission are naturally absent from an earlier target package. That absence is not itself a review defect. Their submitted hashes cannot be authenticated against original file bytes because only pasted blocks were supplied. The reference inventories in `reference/` are computed by the constructor for resubmission; they are not substituted reviewer attestations.

## Independent reviewer provenance

Neither attestation supplies an attributable reviewer identifier, independence statement, reviewed archive digest/commit, described review method or supporting verification outputs. `runtime_constructor_invoked:false` and role strings named “generator” and “verifier” do not establish that someone other than the constructor performed the audit.

A static mathematical/code review can be useful without executing the constructor. Its scope must say that it was static. If record restoration, numerical reproduction or replay is claimed, the relevant outputs and input/code hashes are needed to assess that claim. A digital signature or legal identity is not imposed here as an additional requirement; a stable reviewer identifier and attributable independence/provenance statement are needed.

A later review cannot retrospectively make these already observed constructed-data runs pre-registered or blinded. The attached amendment explicitly labels itself a governance proposal; under its ladder a non-constructor review, pre-data freeze, later blinded execution and custodian ruling have distinct roles. No rung or registry entry is advanced by this intake audit.

## Noise-campaign corrections

The five listed cases have mathematical evidence about the global additive-vector budget and/or finite numeric signatures. They were not demonstrations of complete apparatus, calibration and model-family compliance.

In particular, the single-vector edit has amplitude `1/1048576 = 2^-20`. It attains the global vector ceiling at equality and is eight times the sufficient coordinate ceiling `1/8388608 = 2^-23`. Exceeding this *sufficient* coordinate criterion alone does not negate the separately proved vector bound; it does prevent describing the test as strictly inside every stated acquisition bound. The original campaign explicitly limited that case to the vector-bound test.

The legacy failure included **over-ranking**, not merely rank deficiency. Coherent DC noise raised its stationary proposal count from1 to37 and its total real proposal count from1893 to1929. The repaired algorithm proposes a shared rank budget and proves the residual afterward. It does not force the observed spectrum to equal the proposal rank.

## Retained count is not algebraic rank

The already certified single-vector record gives a concrete distinction. The central impulse of amplitude `u=2^-20` contributes an embedded4096-by4096 anti-diagonal block with4096 singular values `u/4096=2^-32`. The baseline certificate supplies a rank1893 approximant with error at most `tau`.

A rank1893 perturbation can remove at most1893 of those4096 directions. Weyl therefore gives

\[
\sigma_{2203}(H_{\mathrm{single}})\geq 2^{-32}-\tau
=\frac{146856907921586914997}{633825300114114700748351602688}>0.
\]

Thus this encoded matrix has **algebraic rank at least2203**, while its certified count above the frozen threshold is **1893**. `RANK_COUNTEREXAMPLE.json` binds the result to the same record hash used in both campaigns. This does not establish what the baseline exact rank was or whether its exact rank changed.

## Lossless history is not bulk-state reconstruction

The supported codec result is that a specified dictionary, **every exact integer residual**, and the specified decoder restore the frozen encoded history byte for byte. Its hash round trip was checked. A general bijection over arbitrary record/dictionary pairs was not proved; the codec has a residual-range check and can refuse an input.

For the specified nominal operator and observer, define

\[
N=\bigcap_{k\geq0}\ker(RA^k).
\]

If `n` belongs to `N`, then `R exp(tA)(x+n)=R exp(tA)x` for every time. Any codec or deterministic processing of those observations is identical for both states. A codec therefore cannot distinguish the747 nominal hidden directions, recover them from their absence, or establish a unique continuous generator. In the supplied second evaluation, “state” must be replaced by “encoded observation record.” “Closure without leakage across the projection boundary” is unsupported as a physical or hidden-state claim.

The mathematical mechanism is simple: lossless coding preserves distinguishability already present in the data. It adds no observation channels. Known preparations, a chosen section or extra constraints can select a representative, but those are additional assumptions or inputs.

## Parts supported with scope

- Nominal cell operators and frozen modal inputs are not required by the record-only numerical certificate or by byte-level record restoration. The verifier still constructs/factorizes numerical proposal matrices and checks their residuals; it is not a completely parameter-free procedure.
- The source proof bounds Gram/unitarity defects and applies frame/polar corrections. “Orthogonality verified” must refer to those bounded-defect statements, not unqualified exact orthogonality of the proposed floating/dyadic factors.
- Arithmetic invariant statements do not depend on wall-clock task-completion durations in `PROGRESS.json`. Acquisition times/indexing, pre-data chronology, hashes and review provenance still matter to experimental claims.

## Resubmission requirements

Provide a reviewer identifier and independence declaration, the exact archive SHA-256 or immutable commit reviewed, a freshly computed file manifest, and a report using the corrected scope above. State whether the audit was static, a numerical replay, or partial; supply reproduction outputs for any execution claims. Return the original review files if their own file hashes are to be authenticated.

The supplied material is recorded as **received, package binding failed, review eligibility unestablished**. Previous mathematical/numerical results remain at their existing constructor-verified scope. Independent review, custodian ruling, experimental status advancement and physical identification remain open.
