# Measured source-frame error budget for returned floating outputs

DERIVED CONDITIONAL. Development — no registry entry. Physical promotion0.
Budgets are derived certificate inequalities, not new theory constants or replacements for frozen policy gates.

## Direct source witness

Let U0 be the pinned8191-by209 baseline basis, Q0=U0(U0^T U0)^-1/2, and U1 the actual returned retained basis. Let eta1>=||U1^T U1-I||F<1. For ANY dyadic209-by209 X, compute r²=||U1-U0X||F² exactly. No inverse, exact least-squares, or orthogonality property of X is required. With Q1=U1(U1^T U1)^-1/2 and P0=Q0Q0^T,

\[
\|(I-P_0)Q_1\|_F\le s=r/\sqrt{1-\eta_1}.
\]

The projection annihilates U0X and the normalizing inverse has operator norm<=1/sqrt(1-eta1). The same s bounds the operator norm. For s<1, common principal frames have an orthogonal alignment with both distances bounded by

\[
d(s)=\sqrt{\frac{2}{1+\sqrt{1-s^2}}}\,s.
\]

The actual209-column Gram is normalized directly, so no full321-column polar triangle term is added. Displacement combines input perturbation and numerical effects; it is not floating roundoff alone.

## Actual returned shift

The pinned normalized reference has Frobenius shift defect sigma0, shift norm upper M0 and two-row-deleted singular lower beta. For d<beta,

\[
J=\sqrt{1+\eta_1}[\sigma_0+(1+M_0)d],\qquad
 a_{\min}=\sqrt{1-\eta_1}(\beta-d)>0.
\]

For the actual same-output T, set A=U1[:-2], B=U1[2:], E=B-AT, N=A^T E. Exact-LS orthogonality gives

\[
\|E\|_F\le\sqrt{J^2+(\nu/a_{\min})^2},\qquad \nu\ge\|N\|_F.
\]

This does not assume an exact floating LS solve. Exact N² and E² fractions are recomputed and matched to PR217. The source bound is derived without using E²; that value is only a consistency check.

## Explicit sufficient frame ceiling

Let A0 be the unchanged strict shift allowance lower, eta_cap the unchanged Gram cap, nu_cap a declared/verified normal upper, g=sqrt(1-eta_cap), h=sqrt(1+eta_cap). Define

\[
B_0=\sqrt{A_0^2-[2\nu_{\rm cap}/(g\beta)]^2},\quad
D=\frac{B_0/h-\sigma_0}{1+M_0},\quad
S=D\sqrt{1-D^2/4},\quad R=gS.
\]

Require B0>h sigma0 and0<D<min(beta/2,sqrt2); take successive directed lower endpoints for D,S,R. If eta1<=eta_cap, nu<=nu_cap, r<R, then s<S, d(s)<D, amin>=g beta/2 and the returned shift is strictly below A0. The normal cap is the maximum verified upper for the three named archived outputs, not a future solver guarantee. Equality is conservatively refused by this sufficient budget; it is not an estimator failure.

## Generic scalar Frobenius-helper contour

In PR222 notation, alpha=s0-r0, t=r0+C delta, and w0 is the closed weighted baseline/noise forcing. Fix the exact dyadic graph radius x below D-2p(eta_cap), p(eta)=eta/(1+sqrt(1-eta)). The source graph self-map condition is

\[
\Phi(\epsilon)=w_0+\epsilon/\alpha+
\frac{(1+x)^2(t+\epsilon)^2+Mx(2+x)(t+\epsilon)}{\alpha^2}<x.
\]

Its coefficients are nonnegative. The stable positive quadratic root is enclosed. The lower endpoint has a strict self-map; contraction, separation and leading-subspace gates hold at the upper endpoint. Every smaller nonnegative helper F error therefore satisfies this fixed-radius proof under its Gram/normal premises. The upper endpoint bounds this conservative proof contour, not a necessary quality limit on an actual estimator.

The sufficient scalar budget is about1.73686299125739e-13. All three archived full-factor upper bounds are larger, so that route remains HOLD. The direct source-frame route can still certify these outputs.

## Provenance and limits

Auxiliary X proposals were frozen before exact residual evaluation; prior results and the same-team source ceiling were already known. An unexecuted draft's graph-radius display issue was caught during review. budget_v2.py fixes the precise dyadic radius BEFORE deriving and verifying the quadratic. Draft bytes and correction record are preserved; no published result or gate changed. Replay/controls froze after outcomes.

This is a conditional quality theorem and record-wise verification of three actual saved basis/shift pairs. It is not a library-wide forward-error bound, future normal-residual guarantee, new raw eligibility or other-seven-gate execution, physical correspondence, or external independence.
