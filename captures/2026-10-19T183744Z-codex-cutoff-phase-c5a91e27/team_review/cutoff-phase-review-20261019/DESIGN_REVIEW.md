# Retained-factor cutoff and finite returned-phase certificate

Same-team pre-freeze mathematical design review. No new records, fits, projections, estimator runs or numerical phase outcomes are evaluated in this review. The three saved fresh-preparation outputs remain the only candidates. Old source proofs and the PR224 measured-frame certificate are pinned premises, not newly acquired data or an external review.

## 1. Retained-only exact cutoff theorem

Let Z be the exact8191-by-321 projected matrix of one freshly regenerated raw record. Let the actual saved retained factors be U of size8191-by-q, the first q saved nonnegative singular values S, and V of size321-by-q (transpose of the first q saved Vt rows). Require finite arrays, matching custody, q209 and the unchanged cutoff c=2^-24. No discarded columns of U are needed.

Compute the exact dyadic Frobenius residual r=||Z-U S V^T||F. Let etaU and etaV bound the respective Gram defects in Frobenius norm and require both below1. Define p(eta)=eta/(1+sqrt(1-eta)). The polar factors QU=U(U^T U)^(-1/2) and QV=V(V^T V)^(-1/2) are orthonormal. A validated error is

epsilon = r + smax * [p(etaU)*sqrt(1+etaV) + p(etaV)].

This bounds the Frobenius, hence operator, distance between Z and Zhat=QU S QV^T. For example, subtract the two reconstructions by replacing U first and V second, use ||V||2<=sqrt(1+etaV), and ||U-QU||F<=p(etaU), ||V-QV||F<=p(etaV). The latter Frobenius statements follow by summing `(sqrt(lambda)-1)^2=(lambda-1)^2/(sqrt(lambda)+1)^2`; no hidden sqrt(q) factor is omitted.

Zhat has exactly q nonzero singular values equal to the saved retained s values. Weyl therefore gives

sigma_q(Z) >= min(s_retained)-epsilon,
sigma_(q+1)(Z) <= epsilon.

The two strict conditions epsilon<c and min(s_retained)-epsilon>c certify exactly q209 singular values of the actual projected Z above c. Equality or an inconclusive enclosure is HOLD. No discarded reported singular value, discarded U column, opaque LAPACK constant, exact algebraic-rank assertion or future-input robustness theorem is needed.

The saved SVD metadata must still report learned q209 by the original mechanical cutoff count. Verify finite nonnegative descending saved values and count consistency, and never force U to209 columns when the actual retained order differs. This fresh retained-factor proof does not reissue the old full321-column SVD-error engineering gate: its residual includes the actual discarded tail and proves the cutoff/retained approximation only.

For an exact cross-Gram residual, put C=S V^T. Use

r^2=||Z||F^2+tr(C^T(U^T U)C)-2tr(C^T U^T Z).

Every dyadic exponent must be preserved; reject negative exact numerators rather than clipping. Regenerate or hash-bind the new record's complete exact projection N/2^55. The old original-baseline ball/old small integer-delta anchor is inapplicable to the new preparation families. Fresh range guards certify int64 accumulation and exact conversion independently. The projected matrix is small compared with the full Hankel and is not a287-GiB allocation.

## 2. Direct finite observed-phase certificate

The strongest finite shortcut is to compare the actual emitted dyadic angles directly with the pinned complete source target table. For each source label j use target angle theta_j=2*omega_j modulo2pi from PARENT_PHASE.target_matches, not the old table's emitted_index. Ignore those old baseline output indices and form a new assignment by the frozen rule. The factor2 is necessary: these are radians per TWO-STEP sample. Source frequency remains ambiguous modulo pi; this certificate does not create a source lift or SI interpretation.

Let sep>0 be the pinned lower bound on minimum target chord separation. For two unit-circle points, circular angular distance is at least chord distance, so sep is also a conservative angular-separation lower bound. Predetermine the following rule before evaluation: require all209 emitted integer angles, find a unique target for each under validated circular distance, require an injective/bijective assignment, and require every error strictly below sep/2. Equivalently, require a unique nearest target and that same strict error ceiling. Equality, ambiguous enclosure, duplicate assignment, missing target or wrong count is HOLD. The accepted angular neighborhoods cannot overlap. The certified maximum is the outward bound on the actual per-output circular differences; it is not set to an arbitrary post-hoc tolerance.

Each emitted integer must exactly equal ties-to-even rounding at2^-60 of its saved binary64 angle. Independently validate its circular argument error against the exact saved complex-dyadic eigenvalue, with branch wrapping handled modulo2pi. Source targets, labels and minimum-separation proof must be hash-bound to the same pinned parent certificate. Comparing unwrapped angles or reusing the old output permutation is invalid. A robust implementation can use small-angle circular differences or validated complex phases; no accepted angle comparison should cross an unresolved branch.

Fresh eigenpair and inverse checks have a separate role. For saved T,V,Lambda and inverse proposal H, let rho>=||VH-I||2<1, h>=||H||2, and e>=||TV-VLambda||2. Then V is invertible, ||V^-1||2<=h/(1-rho), and Ttilde=V Lambda V^-1 obeys ||T-Ttilde||2<=e*h/(1-rho). Thus the saved Lambda are exact eigenvalues of an explicitly nearby matrix. This binds the finite returned list to a backward-error witness for T. Direct emitted-angle matching alone is not an exact eigenvalue theorem about T; do not describe it as such. Existing engineering maxima may be retained as separate frozen gates, but the observed-angle calculation itself neither needs nor proves the old raw-ball or full321-SVD gates.

## 3. Optional generalized source-to-returned eigenvalue transport

The existing source-frame proof supplies actual retained Gram defect eta, exact r=||U1-U0X||F, source reference residual sigma0, source shift norm M0 and deleted-row margin beta. Set

s = r/sqrt(1-eta),
d = sqrt(2/(1+sqrt(1-s^2)))*s.

Require s<1 and d<beta. Let zeta be an upper bound on the SAME actual raw shift Frobenius residual ||Uplus-Uminus*T||F, either its exact measurement or the validated source-frame returned-shift upper. Use a declared rule consistently; measuring the exact residual is usually tighter. Neither baseline nor actual T is assumed exact least squares. Define

sigma_a = zeta/sqrt(1-eta),
b = [sigma0+sigma_a+d*(1+M0)]/(beta-d).

Then b bounds the aligned difference between actual and source-comparison normalized shift operators. Let eta0 be the pinned baseline Gram defect, k0=sqrt((1+eta0)/(1-eta0)), ka=sqrt((1+eta)/(1-eta)), Delta=e*h/(1-rho). With source reduction D, validated inverse norm hD, reduction norm dD and intertwining residual LJ from PARENT_PHASE.metrics, the correct radius is

R = hD*LJ + k0*hD*dD*(b+ka*Delta),
hD = source_inverse_norm_upper/(1-source_inverse_residual_upper).

The term hD*LJ is not charged an extra k0: if baseline raw T0 satisfies T0D-DJ=L, conjugating by the normalized reduction S0D gives residual D^-1 L. The perturbation between normalized operators does acquire ||S0||2||S0^-1||2<=k0. The actual eigenpair perturbation acquires ka when transported from raw U coordinates to its polar frame. Orthogonal basis alignment adds no condition factor.

The exact source J is normal with unit-circle spectrum. Require R<1,2R<sep and2*(asin(R)+argument_error)<sep. Disjoint disks plus the homotopy eigenvalue-count argument give a bijection to the full209 source targets. The emitted circular phase error is at most asin(R)+argument_error. This route additionally certifies source-to-returned complex-eigenvalue disks, whereas direct observed-phase matching gives the finite angular conclusion directly. Both are recordwise; the new directly measured d avoids the old original-baseline raw-ball premise. No new fit, fullfactor quality assumption or universal solver-admission claim is introduced.

## 4. Controls and custody

Freeze code, source target table, matching rule, cutoff, source separation, retained factor/projection binding and any engineering maxima before this evaluation. Retain all cases and every HOLD. Useful deterministic controls: zero reconstruction factor causes cutoff HOLD; zero right factor fails Gram; cutoff equality is HOLD; zero inverse fails rho<1; emitted-angle integer mismatch is rejected; duplicate or swapped-to-wrong targets cannot pass the strict bijection; source-hash mutation is rejected. Do not substitute a lower target tolerance or retune the source comparison using the new results.

Scope: actual saved synthetic outputs only. No physical acquisition, independent external review, uniform future-solver success, original-baseline ball admission, full-Hankel rank1893, hidden-space reconstruction, or full eight-gate policy transfer is certified by these design notes. Physical Promotion=0; external review pending.
