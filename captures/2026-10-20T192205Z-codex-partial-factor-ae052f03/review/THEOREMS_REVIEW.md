# Independent partial-factor proof review

Development — no registry entry. Physical Promotion = 0. External promotion review remains PENDING. This is a same-team independent mathematical derivation and implementation, not an independent physical experiment or external promotion decision.

## Premises and object

Let Z be real m by n, 1 <= q <= min(m,n), U and V be retained m by q and n by q factors, and S have descending nonnegative diagonal entries s1,...,sq. Assume actual operator-norm bounds

\[
\|U^TU-I\|\le a<1,\quad \|V^TV-I\|\le b<1,\quad \|ZV-US\|\le r,
\]

where a,b,r are nonnegative. Existing exact Frobenius norm certificates can imply these bounds. In this review those existing matrix norm statements are **inherited premises**. Their rational upper wrappers are checked against their saved exact squared enclosures, but the large matrix norm computations and raw projection are not independently repeated. Hash identity binds bytes; it does not prove the inherited inequalities. Only the singular array is read from each saved SVD metadata file; no vector factor is loaded or copied.

## Proof of the retained lower and upper bounds

The Gram assumptions give, for each coefficient vector c,

\[
\sqrt{1-a}\|c\|\le\|Uc\|\le\sqrt{1+a}\|c\|,
\quad
\sqrt{1-b}\|c\|\le\|Vc\|\le\sqrt{1+b}\|c\|.
\]

Thus V is injective and W=range(V) is q dimensional. Writing E=ZV-US and using the triangle inequality yields

\[
(\sqrt{1-a}s_q-r)\|c\|\le\|ZVc\|
\le(\sqrt{1+a}s_1+r)\|c\|.
\]

If the lower numerator is positive, division by the appropriate bounds on ||Vc|| gives the lower and upper gains of the map Z restricted to W, with W carrying its induced Euclidean norm. Courant–Fischer, in the form

\[
\sigma_q(Z)=\max_{\dim W'=q}\min_{x\in W'\setminus\{0\}}\frac{\|Zx\|}{\|x\|},
\]

then gives the proposed lower bound for the actual ambient qth singular value. W need not be an invariant subspace or exact singular subspace.

For 0 <= a,b < 1, the elementary inequalities sqrt(1-a)>=1-a, sqrt(1+b)<=1+b, sqrt(1+a)<=1+a and sqrt(1-b)>=1-b give the conservative rational bounds

\[
\ell=\frac{(1-a)s_q-r}{1+b},\qquad
h=\frac{(1+a)s_1+r}{1-b}.
\]

The rational numerator must be positive for these inverse and conditioning conclusions:

\[
\sigma_q(Z)\ge\ell>0,\quad
\|(Z|_W)^\dagger\|\le1/\ell,\quad
\kappa(Z|_W)\le h/\ell.
\]

The exact algebraic identity

\[
d_q=s_q-\ell=\frac{s_q(a+b)+r}{1+b}
\]

therefore bounds the proposal's **overstatement**: s_q-sigma_q(Z)<=d_q. It does not bound sigma_q(Z)-s_q or absolute error. The map pseudoinverse here is for W to Z(W). The h bound is not an ambient sigma1 bound, so h/ell does not bound ambient sigma1(Z)/sigma_q(Z).

## Prefix extension and all ordered proposals

Let J_j select the first j coefficient coordinates. Its operator norm is one. The prefix Gram defects are J_j^T(U^TU-I)J_j and J_j^T(V^TV-I)J_j, and the prefix equation residual is EJ_j. Their norms therefore remain at most a,b,r. Since the smallest retained rational numerator is positive, applying the same minmax proof to every prefix j <= q gives

\[
\sigma_j(Z)\ge\ell_j=\frac{(1-a)s_j-r}{1+b},\qquad
s_j-\sigma_j(Z)\le d_j=\frac{s_j(a+b)+r}{1+b}\le d_1.
\]

For the remaining saved descending nonnegative proposals j > q, actual singular values are nonnegative, so s_j-sigma_j(Z)<=s_j<=s_(q+1). Consequently all 321 saved ordered proposals satisfy

\[
s_j-\sigma_j(Z)\le\max(d_1,s_{q+1}).
\]

This one-sided conclusion does **not** require the inherited source tail bound. The tail term is a saved proposal, not a certified actual singular value. It does not control underestimation, discharge PR281's two-sided indexed-error condition, prove automatic proposal-floor admission on other records, or prove uniform backend conformance.

## Exact cutoff count

A separately justified actual-tail upper bound t satisfying t<tau<ell ensures that exactly q actual singular values strictly exceed tau and none equals tau. This is a **cutoff count**, not algebraic rank: nonzero singular values smaller than tau may remain. The retained bound alone cannot exclude additional singular values above tau. Strict inequalities are essential.

## Countermodels

The exact controls include Z=diag(5/3,0), U=e1, V=(3/5,4/5), S=[1]. Both Gram defects and equation residual vanish, and the actual matrix has algebraic and cutoff rank one. Nevertheless sigma1=5/3 while the saved proposal is1. Thus zero one-sided debit does not imply zero absolute error, even with the correct actual rank.

A stronger conditioning family uses q=2,

\[
Z=\operatorname{diag}(M,2,0),\quad U=[e_2,e_1],\quad
V=[e_2,(c,0,h)^T],\quad S=\operatorname{diag}(2,1),
\]

with c=2n/(n^2+1), h=(n^2-1)/(n^2+1), M=1/c and integer n>=4. The Grams are identities, ZV=US, ell=1, h_bound=2, and the restricted condition number equals2. At tau=1/2 the actual cutoff count and algebraic rank are both2, with actual tail zero. Yet ambient leading condition sigma1/sigma2=(n^2+1)/(4n) is unbounded. The case n=100 is checked exactly. This also exhibits ordered underestimation despite zero one-sided debit. These are logical rational matrix examples, not actual saved data or a floating-backend bug.

## Active V3 source review

The root V3 proof, domain restrictions, saved-array checks, source bindings and statements agree with this independent derivation. Its source multiplier is compared directly with the pinned prior certificate and, independently here, with the earlier source certificate. Its actual source lower/tail fields agree exactly with those earlier enclosures. Every per-case rational bound, all six new prefix scalar pairs, and the unchanged V2 partial bounds agree. Root V3 certificate and control files are byte-identical to its replay. No mathematical error was found in the stated partial-factor or prefix formulas. V2 hardened source binding; V3 adds the valid prefix extension. Neither version change is a correction of a demonstrated backend bug.

The result establishes finite, conditional postconditions for two existing computational records. All-input actual backend conformance, independent physical acquisition/calibration, primitive-frequency unaliasing, native 1893/747 claims, and physical six-ratio accuracy remain outside the review.
