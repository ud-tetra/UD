# C06 unweighted Whitney trace variation

**EXACT / CONDITIONAL / NO-GO** for the declared lowest-order trace lifts on a regular Euclidean tetrahedron. **Physical Promotion = 0.**

Use oriented unit-integral Whitney edge basis functions. Let \(T\) be their tangential trace from a solid tetrahedron to its boundary, with boundary data represented by one common coefficient per edge. Each of the six bulk edge degrees of freedom is already a boundary edge integral. A tangential trace preserves these integrals, so \(T\) is the identity on the common coefficient space. If separate face flags are used, \(T\) is the rank-six duplication map into compatible flag data.

Let \(P_g,P_c\) be the Euclidean coefficient projections onto cuts and cycles. With tetrahedral side length \(\ell\), volume-averaged bulk mass \(M_v\) and the **average of the four individually area-averaged** face masses \(M_b\) are
\[
M_v=\ell^{-2}(\tfrac12P_g+\tfrac15P_c),\qquad
M_b=\ell^{-2}(\tfrac13P_g+\tfrac29P_c).
\]
The face-sum convention equals \(4M_b\). These forms follow from the [regular-simplex spectrum](https://github.com/ud-tetra/UD-Physics/pull/406) and the [Whitney boundary assembly](https://github.com/ud-tetra/UD-Physics/pull/404). Positive changes of domain normalization simply rescale either form.

## Hard trace and soft variation

For prescribed compatible boundary cochain \(x\), the constrained problem \(\min_{Tu=x}u^\mathsf TM_vu\) has exactly one feasible bulk cochain, \(u=x\). The effective energy is \(x^\mathsf TM_vx\). If the bulk is instead inferred from arbitrary face flags by unweighted Euclidean residual minimization, its coefficient on each edge is the mean of the two copies. For compatible input this returns \(x\). These lifts leave the bulk mass unchanged.

A soft version minimizes
\[
E_a(u;x)=u^\mathsf TM_vu+a(x-u)^\mathsf TM_b(x-u),\qquad a>0.
\]
Stationarity gives \((M_v+aM_b)u=aM_bx\). Substitution gives the effective symmetric form
\[
M_{\rm eff}=\big(M_v^{-1}+a^{-1}M_b^{-1}\big)^{-1}.
\]
For the equal-weight case \(a=1\) its cut eigenvalue is \(1/(5\ell^2)\) and its cycle eigenvalue is \(2/(19\ell^2)\). In general their ratio is \((5+9/(2a))/(2+3/a)>1\). A positive sum \(rM_v+sM_b\), for \(r,s\ge0\) and at least one positive, also strictly favors cuts. These positive quadratic constructions cannot supply the correction needed to equalize the bulk mass.

## Codifferential and added derivative energy

On the volume-averaged tetrahedron the Whitney vertex mass is \(M_{0v}=(I_4+\mathbf1\mathbf1^\mathsf T)/20\). The degree-one codifferential \(\delta_1=M_{0v}^{-1}D_0^\mathsf T M_v\) contributes energy \(Q_{\rm down}=(20/\ell^4)P_g\). This follows from \(D_0D_0^\mathsf T=4P_g\) and the eigenvalue \(1/20\) of \(M_{0v}\) on mean-zero vertex data. The exterior derivative contributes the bulk form \(Q_v=(16/\ell^4)P_c\). A common nonnegative coefficient on both Hodge terms widens the bulk mass gap. This refers to the volume-averaged tetrahedron; the averaged boundary has a different degree-zero mass.

The displayed action with \(\|w\|^2+\kappa\|dw\|^2\) uses the exterior derivative and contributes \(\delta_2d\) to its bulk Euler–Lagrange operator. The coefficient that achieves bulk equalization is \(\kappa=3\ell^2/160\) under these norms and a fixed cut target. None of the unweighted lifts tested fixes this coefficient. Higher-order spaces can have interior degrees of freedom, so a different lift in such a space would require its own variational analysis.

The rational replay assembles the coefficient Gram matrices from signed edge incidence and simplex moments and checks the hard and soft energies, codifferential sector, and conditional up weight. The proof and replay concern mathematical selection only.

**Claim boundary footer:** Physical Promotion = 0.
