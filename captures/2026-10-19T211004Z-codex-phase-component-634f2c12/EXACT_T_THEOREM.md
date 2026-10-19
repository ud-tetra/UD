# Post-known-outcome exact transition spectrum extension

Development — no registry entry; external review PENDING; Physical Promotion=0. This additive lemma is separate from the original frozen finite-emission lane, whose scope and bytes remain unchanged. Its finite emitted/quality results were known before this extension was written. No new estimator, SVD, inverse, alignment or target proposal is used.

Let T,V,H,Lambda be the exact dyadic saved matrices, with Lambda diagonal. Suppose verified upper bounds are

||VH-I||F<=rho<1, ||H||2<=h, ||TV-VLambda||F<=e.

The inverse premise implies V is invertible and ||V^-1||2<=h/(1-rho). Therefore

V^-1 T V = Lambda+F, F=V^-1(TV-VLambda), ||F||2<=R=e*h/(1-rho).

It is **Lambda in this similarity basis** that is normal. Neither T nor VLambdaV^-1 is assumed normal. The diagonal-normal resolvent argument places every exact eigenvalue of T within a closed radiusR disk around some saved lambda_i.

Compute exact squared distances between all saved dyadic centers. If their minimum s^2 satisfies s^2>4R^2, choose R<r0<s/2. The continuous family Lambda+tF,0<=t<=1 has spectrum inside the radiusR union for everyt, so no eigenvalue crosses any radiusr0 boundary. The algebraic count in each r0 disk stays one from t=0. Its eigenvalue must then belong to the radiusR disk at the same center. Thus every exact T eigenvalue is simple and uniquely assigned to a saved center.

Compute m^2=min_i|lambda_i|^2 exactly. If m^2>R^2, every exact T eigenvalue is nonzero and its circular argument differs from its assigned center by at mostasin(R/m). Add the separately verified saved-center argument-to-emission uppera and emission-to-fixed-source upperb:

phase_error_exact_T_to_source <= asin(R/m)+a+b.

If this total is strictly less than half the unchanged source minimum chord lower bound, the exact T eigenphases are uniquely assigned to the SAME bijective source targets as the saved emissions. Chord length is a lower bound on circular angular separation. All arithmetic predicates use exact rationals; only the final arcsine is enclosed with directed Arb arithmetic.

These conclusions apply only to these four exact saved dyadic T matrices and their proved residual/inverse premises. They do not promote the original phase lane into a universal floating-solver, noise-ball, ideal-SVD, full eight-gate or physical-frequency theorem. In particular source frequencies remain model targets and primitive clocks retain their modulo-pi ambiguity. The strict frame failures at amplitudes2/4 remain failures; this different spectral certificate does not rewrite that policy.

The extension's source hashes/code/rules are frozen before its new predicate evaluation. Its proof is algebraic and was separately reviewed; synthetic boundary controls test refusal implementation rather than prove this theorem.
