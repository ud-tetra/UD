# Direct discarded-right-subspace bound

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

Fix a real matrix Z of shape8191×321 and q=209. Let Vd be the321×112 saved discarded right-factor matrix, and suppose

    ||VdᵀVd−I||₂≤eta<1.

This supplies full column rank112 and ||Vd c||≥sqrt(1−eta)||c||. No relation to the retained columns or invariant-subspace assumption is required. Courant–Fischer gives

    sigma210(Z)=min over dim(W)=112 of max_{x∈W,x≠0} ||Zx||/||x||
               ≤||ZVd||₂/sqrt(1−eta).

Write G=(ZVd)ᵀ(ZVd). Since ||ZVd||₂⁴=||G||₂²≤||G||F², a fourth-root upper r≥(sum_ij Gij²)^(1/4) gives the conservative rational bound

    sigma210(Z)≤tnew=r/(1−eta).

The preselected computation uses a Frobenius square upper for the Vd Gram defect and the fourth root of the output Gram Frobenius square. Both scalar roots are enclosed on the fixed2^-180 grid. No eigenvalue estimation, alternate norm route or precision retry is selected after seeing a target result.

## Exact witnesses

With Z=N/2^55 and Vd=Vi/2^b, compute the integer matrices

    E=ViᵀVi−2^(2b)I,
    H=(NVi)ᵀ(NVi).

Their denominator exponents are2b and2(55+b). Then

    eta ≥ sqrt(sum Eij² /2^(4b)),
    r ≥ fourthroot(sum Hij² /2^(4(55+b))).

The integer identities must be verified, not inferred from a PASS label or hashes. A distinct modular/CRT audit verifies every E,H entry against independently encoded saved Vd and the original hash-bound projected N, with full difference bounds and proved primes. These are finite exact computational statements; raw/projection lineage remains inherited from PR279/286.

## Reanchor the retained block proof to the new tail

PR286 supplies retained Gram bounds a,b, forward f and exact adjoint g for the same saved tuple. Recompute

    c={s1[a/(2−a)+b/(2−b)]+f}/(1−b),
    e=max(f/(1−b),g/(1−a)).

The separate polar-frame block proof shows that when sq−c>tnew+e, the leading209 singular block matches the retained compression, giving |sigma_j(Z)−sj|≤epsilon=c+e for j≤209. These c/e bounds themselves do not require the earlier nominal source-tail enclosure. Rechecking the matching gap with the directly computed tnew removes that old nominal-tail dependency from this finite retained/full321 accuracy proof. Original retained Gram/forward norms and PR286 adjoint remain inherited premises; they are not newly recomputed here.

For j>209, both actual and saved singular values are nonnegative, sigma_j(Z)≤tnew and sj≤saved_s210, so

    |sigma_j(Z)−sj|≤max(tnew,saved_s210).

Thus every ordered singular-value error in the full321 list is bounded by max(epsilon,tnew,saved_s210). A strict upper below2^-41 closes that finite per-record numerical target, not actual all-input backend conformance. If a bound fails, preserve the target HOLD; do not tune the method/caps or replace the case.

If also sq−epsilon>tau>tnew for tau=2^-24, the actual cutoff count is209 with no equality. This is not algebraic rank209: the discarded singular values may be small and nonzero. No lower bound for sigma321 or full-matrix condition number is established. The prior ambient leading209 condition remains a distinct supported object.

## Scope and dependencies

The theorem concerns two unchanged PR279 computational records. The stored N inputs are reused with their original integer projection hashes and current before/after identity checks. No estimator, new record identity, raw replay, projection reconstruction or stored factor copy is created. Both fresh Gram matrices and their scalar consequences are computed and independently audited. Existing retained-norm/source-lineage premises remain explicit. The nominal source-tail upper is not a premise of the new finite full321 bound after reanchoring, but original physical/model/frame/target premises are not thereby validated.

All-input backend/library/whole-program guarantees, native1893/747 interpretation, exact spectrum(T), primitive-frequency unaliasing, physical freshness, acquisition/calibration and SI/six-ratio accuracy remain OPEN. Protocol accuracy targets are O03 controls, not theory constants. No previous HOLD/NO-GO verdict is changed. Same-team reviews are not external promotion authority.
