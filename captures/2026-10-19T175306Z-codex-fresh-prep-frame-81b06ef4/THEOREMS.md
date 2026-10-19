# Measured source-frame theorem and prospective experiment

Development — no registry entry. Physical promotion0. The underlying nominal model and its source comparison bounds are pinned premises from PR224 and its ancestors.

## Exact measurement certificate

Let U0 have209 independent columns and let Q0=U0(U0ᵀU0)^(-1/2). For the actual retained floating basis U1, certify eta>=||U1ᵀU1-I||F with eta<1. Choose any dyadic auxiliary X and exactly measure r=||U1-U0 X||F. X need not be an inverse, minimizer or reliable solve. For Q1=U1(U1ᵀU1)^(-1/2),

s=r/sqrt(1-eta) >= ||(I-Q0 Q0ᵀ)Q1||F.

If s<1, a common orthogonal alignment of the two column frames has Frobenius/operator distance at most

d=sqrt(2/(1+sqrt(1-s²)))s.

Using the pinned source shift comparison sigma0, source shift norm M0 and deleted-row minimum singular bound beta, if d<beta define

J=sqrt(1+eta)[sigma0+(1+M0)d], amin=sqrt(1-eta)(beta-d)>0.

For the returned lag-two shift T, A=U1[:-2], B=U1[2:], E=B-AT, and the exactly measured normal residual nu>=||AᵀE||F,

||E||F <= sqrt(J²+(nu/amin)²).

Proof: source comparison and the common alignment bound the optimal LS residual by J; A has minimum singular value at least amin. Orthogonal decomposition E=(I-AA†)B+A(A†B-T) gives a Pythagorean sum, and the normal residual bounds its second term by nu/amin. All stored binary64 entries are treated as exact dyadics and all displayed enclosures are directed outwards with512-bit Arb arithmetic. Frobenius quantities also bound operator norms.

The measured r includes preparation changes, encoded perturbation and numerical effects. It is not pure roundoff. This theorem has no original-baseline noise-ball premise. Its measured acceptance policy still requires all frozen PR224 caps, including the old finite-run normal cap; a diagnostic direct bound cannot override a failed cap.

## Synthetic preparation construction

For each same clock-parity block, a signed permutation or a disjoint rational orthogonal3/5,4/5 plane transform maps the original nominal preparation series to a fresh synthetic nominal series. Linearity preserves the pre-quantization unsketched temporal family and total preparation energy, but does not preserve each preparation norm or guarantee that the fixed sketch preserves rank/conditioning. The integer rational nominal is rounded once to the nearest raw quantum with exact scalar error <=2/5 quantum. There are no ties for denominator5. Guard7*maxabs(raw)<2^63 before arithmetic. Add exactly one signed quantum per62-vector relative to that fresh integer nominal, checking every scalar difference.

If d0 is the pinned old scalar source error and qraw=2^-48, the signed nominal error is at most d0; the rational nominal error is at most(7/5)d0+(2/5)qraw. After onehot perturbation, each62-vector squared source error is at most62*dnom²+2*dnom*qraw+qraw². These are source-error bookkeeping bounds, not original-baseline raw-ball eligibility or a full SVD certificate.

## Frozen finite policy

Three recipes, all code, inputs and exact old budget are frozen before generation. All three raw hashes freeze before the first estimator run. The actual SciPy estimator learns the retained rank at2^-24 and then uses unchanged lag-two LS/eigenvalue/angle arithmetic. A different learned rank or numerical exception is retained as HOLD without retry or replacement. Auxiliary X witnesses freeze after fitting and before exact measurement. Five finite controls are declared before outcomes. Both all-outcome custody and optional full raw/projection replay are required; replay invokes no new estimator SVD.

Only measured209-column source-frame/shift bounds are newly certified. No full-factor SVD accuracy, cutoff robustness, emitted-phase matching, full-Hankel1893 rank,747-kernel proof, population success probability, physical acquisition or universal future-solver accuracy is claimed here. Same-team reviews do not supply external independence. The protocol is local prospective development work, not blinded or externally registered.
