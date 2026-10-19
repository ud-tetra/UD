# Coefficient-weighted leading graph and shift theorem

DERIVED CONDITIONAL. Development — no registry entry. Physical promotion0.
This explanatory theorem records the implemented proof after its numerical
results; the algebraic candidate and primary code were frozen before them.

Let Q0 have orthonormal columns, L0=Q0 D, alpha<=sigma_min(D),
M>=||D||2. Let Btilde=L0+Delta, with e>=||Delta||2,
f>=||Delta^T Q0||F, w>=||Delta D†||F. Define

\[
z=w+ef/\alpha^2,\quad a=(2Me+2e^2)/\alpha^2,\quad
b=e(M+e)/\alpha^2.
\]

If x>0 satisfies

\[
z+ax+bx^2\le x,\quad a+2bx<1,\quad \alpha>2e,\quad
\frac{(\alpha-e)^2-2e(M+e)x}{1+x^2}>e^2,
\]

the leading q-dimensional left singular subspace of Btilde is a graph W
over Q0 with ||W||F<=x. In particular it has a common orthogonal frame
alignment with both Frobenius and operator distances <=x.

Proof: partition H=Btilde Btilde^T relative to Q0 and its orthogonal
complement, and put R=D D^T. The bounds
||H22||2<=e², ||H11-R||2<=2Me+e², ||H12||2<=e(M+e) and
||H21 R^-1||F<=w+ef/alpha² follow by expansion. The invariant-graph equation
has the fixed-point form

\[
\mathcal T(W)=H_{21}R^{-1}+H_{22}WR^{-1}
-W(H_{11}-R)R^{-1}-WH_{12}WR^{-1}.
\]

Its Frobenius ball self-map and contraction constants are bounded by the
first two gates. The final gate bounds every Rayleigh quotient on that
invariant graph above e². Minmax bounds lambda_(q+1)(H)<=e² using the source
orthogonal complement, so this graph is the leading subspace. Principal
angles satisfy tan(theta_i)=s_i(W) and 2(1-cos(theta_i))<=tan²(theta_i).
The common Procrustes frame therefore has both stated norm bounds.

For the parent nonorthogonal factor U0, let G0=U0^T U0 and
Q0=U0 G0^-1/2, D=G0^1/2 C0. With eta0>=||G0-I||2<1, use
alpha=s0-r and M=sqrt(1+eta0)||C0||F from the pinned baseline/order data.
An exact dyadic K=C0^T Maux, with rho>=||C0K-I||2<1, yields
C0†=K(C0K)^-1 and D†=C0†G0^-1/2. Thus baseline/noise weighted norms are
divided by (1-rho)sqrt(1-eta0). The exact row-space construction is required.

Write B for the perturbed encoded sketch, B0 for its baseline, and rK for
||(B0-U0C0)K||F. The full one-quantum lattice ball gives the row-max bound
cK*delta for ||(B-B0)K||F as proved in README.md. A full-factor Frobenius
approximation error epsilonF contributes directly <=epsilonF/alpha to w:
||Delta_helper D†||F<=epsilonF||D†||2. With only an operator error epsilon2,
the valid replacement is sqrt(q)epsilon2/alpha. Correspondingly,

\[
w\le\frac{r_K+c_K\delta}{(1-\rho)\sqrt{1-\eta_0}}
+\frac{\epsilon_F}{\alpha},\quad
e\le r+C\delta+\epsilon_2,\quad f\le r+C\delta+\epsilon_F.
\]

Use sqrt(q)epsilon2 in f and in w's last numerator for the operator-only
lane. Do not upgrade an arbitrary operator certificate to Frobenius.
The actual parent helper's stronger Frobenius semantics were proved in PR217.

For a returned basis with full Gram defect eta, retain the parent's
2p(eta) correction between the full-factor polar columns and the retained
polar basis, p(eta)=eta/(1+sqrt(1-eta)). Put d=x+2p(eta). The exact-LS
shift residual is at most

\[
J=\sqrt{1+\eta}\,[\sigma_{0,F}+(1+M_0)d],\quad
a_{\min}=\sqrt{1-\eta}(\beta-d)>0.
\]

For an actual returned shift with exact normal residual ||A^T E||F<=nu,
the raw residual is <=sqrt(J²+(nu/a_min)²), by exact-LS Pythagoras.
No bound on nu or SVD convergence is attributed to a floating library
without an additional argument. All graph gates are checked with directed
Arb enclosures after rounding the proposed small root upward.

The numerical conclusion concerns the unchanged shift allowance only.
Whole-ball ideal shift sufficiency does not imply the other seven output
gates, uniform floating solver success, or a physical correspondence.
