# Direct measured source-frame numerical budget

Same-team review; physical promotion 0. This is a finite-output sufficient
certificate, not uniform convergence of a numerical library.

Let U0 span the pinned baseline and Q0=polar(U0). Let U1 be an actual returned
retained basis with eta1>=||U1^T U1-I||_F<1, Q1=polar(U1). Any dyadic X is an
untrusted proposal; no inverse or fitting accuracy of X is required. If
ell>=||U1-U0 X||_F, projection annihilates U0 X, hence

    ||(I-Q0Q0^T)Q1||_F <= ell/sqrt(1-eta1) =: sF.

For sF<1, the common principal-angle Procrustes alignment has BOTH operator
and Frobenius distance at most

    d(sF)=sqrt(2-2sqrt(1-sF^2)).

This uses normalized actual retained spaces directly; the global full-factor
polar allowance is not added to irrelevant directions.

With pinned baseline beta, sigma0,F and M0 bounds, define

    J=h[sigma0,F+(1+M0)d],  amin=g(beta-d),
    h=sqrt(1+eta1), g=sqrt(1-eta1).

J bounds the exact-LS residual on the actual U1 basis in Frobenius norm.
For the actual saved shift T, if nu bounds
||U1minus^T(U1plus-U1minus T)||_F, exact orthogonal least-squares decomposition
gives the returned residual bound sqrt(J^2+(nu/amin)^2). No exact-LS status
of the actual binary64 T is assumed.

## A priori monotone ceiling

Use eta1<=eta_cap and verified/declared nu<=nu_cap. Let A be the unchanged
published strict allowance, g=sqrt(1-eta_cap), h=sqrt(1+eta_cap), and

    B=sqrt(A^2-[2nu_cap/(g beta)]^2),
    D=(B/h-sigma0,F)/(1+M0).

Require B>h sigma0,F and 0<D<min(beta/2,sqrt(2)). Then

    S=D sqrt(1-D^2/4)

is a sufficient strict ceiling on sF. Indeed sF<S implies d<D<beta/2,
J<B, amin>g beta/2, and therefore the returned residual is strictly below A.
The squared returned bound is monotone increasing in sF on this interval.
The raw residual sufficient ceiling is S*sqrt(1-eta_cap).

derive.py was frozen before evaluating this numerical ceiling. The archived
maximum normal residual is used only for its three named finite cases. It is
not asserted as a guarantee for future solves. The resulting conservative
sinTheta_F ceiling is about 2.489581884107036e-10. No actual X, alignment
residual, new SVD, or new estimator output was computed in this review.

Full input eligibility and all other policy gates remain separate. A source-
frame or shift-budget HOLD is a limitation of this sufficient contract, not a
proof of a failed physical model or an unrestricted algorithm no-go.
