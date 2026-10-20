# Posterior admission integration and fixed-basis LS error allowance

Development — no registry entry. Physical Promotion=0; external promotion review PENDING. This continues PR263. It contains a new exact source-selected least-squares error allowance and a small historical-only admission reducer. It performs zero estimator calls, raw generation, factor copies, Gram/normal matrix recomputations or full Hankel allocations.

## New quantitative result

For fixed saved A=U[:-2], B=U[2:] and exact Tstar=A†B, inherit saved operator-lag upper d, saved LS-distance upper e0 and U Gram-defect upper eta. Row deletion gives ||A||2<=sqrt(1+eta)<=a=1+eta/2. Every replacement Tprime with ||Tprime-Tstar||2<=epsilon satisfies

 ||A Tprime-B||2 <= d+a(e0+epsilon).

Therefore epsilon_star=(2^-34-d)/a-e0, when positive, is a sufficient CLOSED LS-centered radius for the unchanged operator-lag cap. This is a budget around exact fixed-basis least squares, not the saved T, raw input or a physical parameter. It proves no replacement phase/eigenpair quality and no numerical backend guarantee.

| Saved basis | Sufficient LS-centered radius (approximate) | Largest qualifying frozen dyadic |
|---|---:|---:|
| Top1 alternating | 1.9557855412317577e-11 | 2^-36 |
| Top2 alternating | 1.4484347641443424e-11 | 2^-37 |

Thus2^-37 suffices for both fixed bases for this operator-lag gate alone. Exact rational radii and all162 grid rows (k20..100 per basis) are retained. A larger grid value failing this sufficient envelope is not a counterexample or sharp stability boundary. Equality at epsilon_star is allowed because the lag cap is nonstrict. The known historical source values were disclosed; core/grid were frozen before these new quotient evaluations. This is not blinded experimental evidence.

The source d is PR258's preselected Gram-Frobenius operator upper; e0 and positive Gram floor come from PR263's exact saved normal certificates. Norm matrices/factor truth are inherited and hash-bound, not recomputed. The old Top2 fixed-U Frobenius obstruction and original campaign HOLD remain unchanged; the operator bound has a different scope.

## Executable historical admission profile

OPERATOR_POSTERIOR_ADMISSION_v0.1, implementation revision0.2, checks a conjunction of exact rational original caps, source/projection identity, SAME actual saved witness tuple, positive singular/rank premises, strict eigenvalue disks and finite209-target phase qualification, plus finite saved LS posterior accuracy. It invents no new LS threshold and performs no adaptive norm-route search. It consumes hash-pinned previously reviewed exact proof receipts; it is not a new independent matrix proof or a new phase theorem.

Record SHA alone is insufficient to bind a fit. The registry cross-checks PR256 data, protocol, projection comparison, execution and complete manifest; PR258's frozen bindings point to that same saved execution; PR263 also pins each U/T and RUN byte hash. The original statuses and gates are copied unchanged. Input hash/schema/identity/gate failures are HOLD.

Both registered historical cases return HISTORICAL_FINITE_OPERATOR_PROFILE_ADMISSIBLE under this new integration profile. Top2's original HOLD_ACTUAL_ESTIMATOR_EQ_OR_PHASE remains explicitly present. The earlier separate operator-route result was already known from PR258: this is integration, not a newly discovered phase success.

The explicit foreign/fresh mode returns HOLD_FOREIGN_OR_UNVERIFIED_FRESH_BUNDLE without admitting any row. The executable is intentionally historical-only and cannot validate fresh record arithmetic from claimed pass flags or metadata. A fresh numerical admission implementation remains absent. Primary/replay outputs are byte-identical; the root foreign-mode receipt is retained.

## Pre-execution correction and review

The first frozen implementation draft was never run on the historical reductions. Separate review found two promised contract checks missing: explicit strict eigenvalue-disk checks and exact expected phase/route gate-key sets to avoid vacuous all(values). The complete first draft/freeze/16 pure controls remain preserved. Revision0.2 adds those checks,29 pure rejection controls, supersession provenance and a new pre-run freeze/review/release before any historical reduction. No source cap, selected norm route or historical outcome was tuned.

Separate same-team review checked all162 budget rows with10 independent budget controls,20 synthetic gate controls and14 metadata-mutant rejection tests. The budget also has8 root controls; corrected producer admission controls number29 (the first draft retains16). Root deterministic replay covers both the new rational budget and logical reducer. Their receipts identify synthetic controls, post-release metadata mutant tests, all162 budget comparisons, exact source pins, strict boundaries, same-fit binding and the unchanged old verdicts. Historical exact matrix checks remain inherited. Same-team review does not supply external promotion authority, independent experimental replication or a registry advancement.

## Fresh execution frontier

FRESH_RUN_PROTOCOL.md is a frozen requirements document with status INCOMPLETE_UNEXECUTED, not a completed concrete run registration or an execution release. It requires a specific eligible source/model/baseline and preparation set; concrete code/data/noise/projection freezes; independent prospective review/root release; exclusive one-shot unchanged numerical invocation; complete saved witness tuple; fresh exact eligibility/equation/Gram/lag/complex/encoding/LS-normal recomputation; source/fit identity; and independent review/root replay. A specific fresh candidate and its complete eligibility chain are still unresolved. A new computational preparation would not itself establish independent physical fresh lineage.

No new evidence-return search was performed this turn. The prior bounded R01–R14 status remains the stated older snapshot:128 paths unresolved, request UNSENT. Actual source-specific acquisition/calibration/model/fresh-lineage evidence and separate scientific/authority/custody review plus custodian ruling remain required for their corresponding claims. No outreach, physical acquisition, site deployment or Project-board change is claimed. Genesis PNG unavailable/unused.

## Provenance and publication

All new payloads, original/corrected freezes, source pins, exact rational results, controls, reviews and root replay receipts are inventoried by SHA256/size/provenance in MANIFEST.json, with a unique event and contributor PR. Canonical supplied ledger v0.39 and CRL2 governance bytes are preserved. Protocol controls are not theory constants; equal values do not identify different typed objects. Source/model dependence remains conditional and cannot gain authority by citation.

Next1: identify one eligible computational fresh candidate, check prior exposure, then complete concrete source/code/data/verification freezes and review before a one-shot run. Next2: actual independent evidence returns and promotion review/custodian ruling; historical logical admission is no substitute.
