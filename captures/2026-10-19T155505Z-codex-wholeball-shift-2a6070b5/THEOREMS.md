# A priori shift-residual bounds over the encoded ball

DERIVED CONDITIONAL. Development — no registry entry. Physical promotion0.
All quantities are in the frozen numerical model units. No gate is changed.

## 1. Norm-typed premises and Frobenius certificate

Let q=209, n=8191 and B have321 columns. Each encoded62-vector differs from
the pinned PR195 baseline by norm<=delta<=2^-48; arbitrary correlations are
allowed. Flattening the37 preparations gives raw error Frobenius norm
<=sqrt(37*8191)*delta. Multiplication by the fixed sketch/128 therefore gives
||B-B0||F and ||B-B0||2 <=C*delta, with the pinned C<707.294. This covers the
entire declared ball, not only tested patterns.

The baseline has a rankq approximation L0 with spanQ0 and **Frobenius** error
<=r. Its exact squared residual is a source dependency derived by integer
cross-Grams and sum-of-entry-squares; the retained scalar r is checked against
that exact fraction. Put alpha=s0-r, where s0 is a baseline sigmaq lower bound.

For returned factors, the old abstract operator approximation premise is
||Btilde-B||2<=epsilon2. It does NOT alone give the same Frobenius bound.
However, the actual pinned full-factor helper computes Frobenius reconstruction
and Gram-defect norms. If eta=||U^T U-I||F<1, diagonalizing its Gram shows

\[
 ||U-\operatorname{polar}U||_F
 \le p(\eta)=\frac{\eta}{1+\sqrt{1-\eta}}.
\]

Indeed each singular value difference is (s_i^2-1)/(s_i+1), with denominator
>=1+sqrt(1-eta). Summing squared terms proves the formula. The same holds
for the right factor. Thus the helper's exact Frobenius reconstruction error
plus smax*[p(etaU)*sqrt(1+etaV)+p(etaV)], including Frobenius projection error,
is ALSO a Frobenius approximation bound epsilonF. This explicitly proves the
stronger norm semantics for that helper; an arbitrary operator-only witness
is not upgraded by assertion. All numerical maxima remain O03 controls.

## 2. Simultaneous subspace alignment

Set e2=r+C*delta+epsilon2, t2=e2/(alpha-e2), and assume alpha>2e2. For the
topq singular equations, the off-reference part has operator bound e2 and
Frobenius bound ef. Use ef=r+C*delta+epsilonF with the verified F certificate;
with only epsilon2, use ef=r+C*delta+sqrt(q)*epsilon2 for the projected error.
The retained singular denominator is >=alpha-e2, so tf=ef/(alpha-e2) bounds
the Frobenius norm of principal-angle sines. The ideal exact-SVD lane has
epsilon2=epsilonF=eta=0.

Let c=sqrt(2/(1+sqrt(1-t2^2))). Principal angles give a **common orthogonal O**
aligning the returned polar retained basis Q with Q0O, with

\[
 d_2=c t_2+2p(\eta),\qquad d_F=c t_F+2p(\eta).
\]

The identity 2(1-cos(theta))=2sin(theta)^2/(1+cos(theta)) proves both bounds
using cos(theta)>=sqrt(1-t2^2). The2p term is the triangle between the full
factor's firstq polar columns and the separately normalized retainedq basis;
both Gram defects are bounded in Frobenius norm. No missing sqrt(q) is hidden
in that term. Q0 and the normalized comparison shift T0bar have source bounds
sigma0F for the Frobenius shift residual, M0 for ||T0bar||2, and beta for the
two-row-deleted singular margin. Parent sigma0 is Frobenius-derived, not an
unqualified operator bound.

## 3. Uniform exact least-squares residual bound

Write returned U=Q S, S=(U^T U)^(1/2), and take
Tcmp=S^-1 O^T T0bar O S. Then

\[
 J=\sqrt{1+\eta}\,[\sigma_{0,F}+d_F(1+M_0)]
\]

bounds ||Uplus-Uminus*Tcmp||F. Consequently the exact least-squares minimizer
T* on this returned basis satisfies ||E*||F<=J. With

\[
 a_{\min}=\sqrt{1-\eta}\,(\beta-d_2)>0,
\]

the deleted returned basis A=Uminus has sigma_min(A)>=a_min. These are a
priori bounds for every ball input satisfying the stated SVD-quality premises;
they do not assume every floating SVD returns that quality.

## 4. Actual floating shift solve and fixed-basis lower bound

For any finite real returned T let E=Uplus-A*T and N=A^T E. Since A has full
column rank, exact least squares gives A^T E*=0 and

\[
 E=E_*+(A^\dagger)^T N,\qquad
 ||E||_F^2=||E_*||_F^2+||(A^\dagger)^T N||_F^2.
\]

Therefore a declared/verified ceiling ||N||F<=nu yields the uniform conditional
returned-solve bound

\[
 ||E||_F\le\sqrt{J^2+(\nu/a_{\min})^2}.
\]

No uniform normal-equation residual guarantee is attributed to a floating
library without proof. For a saved output with **exact** s_squared=||E||F^2,
the same identity supplies a lower enclosure for the optimal residual:

\[
 \min_T||U_+-AT||_F
 \ge\sqrt{\max(0,s_{\rm squared}-(\nu/a_{\min})^2)}.
\]

This lower bound uses exact residual squared, an upper normal residual and a
positive lower singular margin. A strict lower>2^-34 proves no replacement
shift T can pass the OLD gate on THAT saved basis. It does not prohibit a new
basis, different algorithm or new policy. The max with0 only weakens a lower
bound; an inconsistent negative exact residual numerator is rejected first.

## 5. Limits and refusal

Without any shift/normal-residual constraint, projection and SVD quality
alone cannot bound arbitrary returned T: taking T=tI makes the residual
unbounded as |t| grows for full-rank A. This is a logical missing-premise
obstruction, not a claim about the outputs of a particular numerical library.

Comparing a conservative J or returned upper with the published v2 allowance
only tests sufficiency of THIS proof. If it exceeds the allowance, uniform
admission remains HOLD; that is not a witnessed failure or a lower bound on
the true worst-case residual. No gate or source radius is tuned to obtain PASS.
Prior finite-pattern v2 certificates and v1 HOLDs remain unchanged. No new
SVD/proposer/raw generation, physical/SI identification or full-Hankel claim.
An email request being sent does not constitute nonconstructor review.
