# Backend conformance: what a finite certificate can establish

Development — no registry entry. Physical Promotion=0. External promotion review PENDING. This analysis uses known earlier outputs but executes no new fit or raw generation.

## Domain and inherited premises

Let D be all encoded perturbation histories of the original nominal record with per-62-vector radius delta0=3*2^-49, quantum qraw=2^-48. There are 7689 pointwise choices and 303067 vector positions. No random law is assigned. The source proof also permits real perturbations in the same ball.

Fix the source comparison rank r=209, observed matrix shape8191×321 and cutoff tau=2^-24. Inherited bounds are sigma209(Z0)>=s0, sigma210(Z0)<=u0 and ||Z-Z0||2<=e=C*delta0. All source constants and proof identities remain explicit hash-bound premises; this work does not rederive source H, full-factor, frame or target certificates.

Define L=s0-e, U=u0+e. Exact arithmetic below shows U<tau<L. C is the same exact rational upper bound used by the original proposed-floor gate. A rounded decimal C is not substituted in a closed-boundary proof.

## Theorem 1: uniform rank and floor, conditional on a backend error bound

For each Z in D, suppose the backend returns 321 finite nonnegative singular-value proposals in descending order, and each indexed value differs from the correspondingly ordered exact singular value of Z by at most epsilon. If

    0 <= epsilon < b := min(L-tau, tau-U),

then exactly209 proposals exceed tau and no proposal equals tau. Weyl's singular-value perturbation inequality gives sigma209(Z)>=L and sigma210(Z)<=U. Hence the first209 proposals are >=L-epsilon>tau, and the rest are <=U+epsilon<tau.

The strictness is material: at epsilon=tau-U the first discarded proposal can equal tau. The numerical strict count can remain209, while the existing exact saved-rank verifier returns HOLD on equality. The stated b is a sufficient bound from inherited enclosures, not the necessary or sharp tolerance of the actual implementation.

The original source-scale floor is s_hat209>=L-d, d=2^-41. The additional sufficient condition epsilon<=d implies this floor. Exact source-bound arithmetic shows d<b, so that condition also implies rank209 and absence of cutoff equality. The largest power-of-two epsilon=2^-k satisfying the strict rank-only budget is2^-25. Its ratio to d is2^16=65536. Rank preservation alone does not imply the stronger floor. No actual uniform epsilon bound for SciPy, LAPACK or any other backend is established here.

## Theorem 2: a sufficient complete-factor route to the singular-value error bound

Suppose COMPLETE thin factors Uf in R^(8191×321), Vf in R^(321×321), and diagonal Sigma with sorted nonnegative proposals s_i satisfy

    ||Z-Uf Sigma Vf^T||2 <= f,
    ||Uf^T Uf-I||2 <= etaL <1,
    ||Vf^T Vf-I||2 <= etaR <1,
    max_i s_i <= m.

Take polar frames QL=Uf(Uf^T Uf)^(-1/2), QR=Vf(Vf^T Vf)^(-1/2). They have orthonormal columns. Define d(eta)=1-sqrt(1-eta), which bounds both deviations of the positive square-root Gram eigenvalues from1. Therefore ||Uf-QL||2<=d(etaL), ||Vf-QR||2<=d(etaR), and ||Vf||2<=sqrt(1+etaR).

The matrix QL Sigma QR^T has singular values s_i. Splitting the product difference on its left and right gives

    max_i |s_i-sigma_i(Z)|
      <= epsilon_eff = f + m[d(etaL)*sqrt(1+etaR)+d(etaR)].

The factor sqrt(1+etaR) cannot generally be dropped. An exact scalar example is Uf=Vf=6/5, s=2, Z=72/25. Reconstruction error is0, both Gram defects are11/25, actual singular-value error is22/25. The displayed bound gives22/25; dropping that factor gives4/5, which is too small.

For exact rational bookkeeping, d(eta)<=eta and sqrt(1+eta)<=1+eta for eta>=0. Thus

    epsilon_eff <= E := f + m[etaL(1+etaR)+etaR].

A proof that E<=2^-41 uniformly over D would supply Theorem1's rank and floor premises. It would still not prove all the retained-vector, lag, eigenpair, inverse, argument and encoding gates. The synthetic54-row budget grid evaluates this implication only; it is not a measurement, a new operational cap or a backend conformance certificate.

PR279 retains209 left columns, not the complete321-column left factor. Its exact retained equation does not provide the complete reconstruction residual or full left Gram premise required above. No missing columns are fabricated or reconstructed here. This is one sufficient route; it is not claimed necessary for all possible backend proofs.

## Theorem 3: accepted-output soundness has a different quantifier

Let P denote the inherited source premises. Let G(Z,w) mean that the ACTUAL raw/projection identities, shapes, exact saved rank, measured singular floor, both retained Gram defects, retained equation, fixed lag-operator bound, inverse/eigenpair/argument/encoding metrics, finite target matching, conditional disks and finite LS conditions for returned tuple w have been validated under the original profile. Metadata assertions, hashes alone, or a claimed PASS string are not G.

The inherited retained-equation/polar/lag/normal-target proof supplies

    P and (Z in D) and G(Z,w)  =>  the certified emitted-phase bound for w.

This is universal over qualifying returned tuples, independently of how w was proposed. It is a conditional mathematical implication, not a claim that every program described as a verifier is correct, terminates, or resists every possible malformed input. Whole-program implementation soundness and numerical library correctness need their own proofs. A runtime exception, missing witness, indeterminate interval or failed validation cannot be counted as certified acceptance.

Backend completeness would require

    for every Z in D: B(Z) terminates and G(Z,B(Z)).

Finite successes do not establish this statement. Even universally correct singular values do not establish G: zero proposed left/right vectors have a zero retained equation but fail the Gram gates. Correct orthonormal vectors aligned to the wrong singular direction can fail the retained equation. An arbitrary shift can fail the lag gate even when the singular factors are exact. The executable small rational examples illustrate invalid inferences; they are not failures of the actual UD records or fixed SciPy implementation.

## Finite-test limitation

For any proper tested subset S of a finite domain and any good black-box map B1, choose an untested input x*. Define B2=B1 on S but return a failing tuple at x*. The two maps have identical tested outputs; only B1 can satisfy the universal success property. This is a logical countermodel to inference from finite black-box observations, not a counterexample to the known frozen estimator source. If full source structure, verified arithmetic, exhaustive coverage or another global theorem is available, it can supply information that this argument does not assume.

No universal implementation failure or impossibility theorem is asserted. No raw, floating fit, experimental evidence, independent physical freshness, exact spectrum(T), native1893/747 recovery or physical six-ratio accuracy is established. Existing finite certificates and HOLD/NO-GO results remain unchanged. Same-team independent implementation review does not replace external promotion review.
