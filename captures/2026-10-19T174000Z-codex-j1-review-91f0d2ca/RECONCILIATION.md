# Supplied J1 review reconciliation and inexact-output allowance v0.1

Development — no registry entry. DERIVED / EXACT CONDITIONAL. Physical promotion0. Refs #218,#136 and PR223. The supplied review arrived as user text; its author's identity, methods beyond the shown snippets, and nonconstructor independence are not established. Record it as supplied review evidence, not independent human review, blanket verification or CRL promotion. The attached governance amendment remains a proposal. Earlier capture bytes are unchanged.

## 1. Accepted scoped checks

The supplied algebra agrees with the target's rotation cancellation, monotonicity of beta in positive damping, conservative continuum lambda*=4, source dual norm bound sqrt5, flux-norm expansion47/42, completed-square gain bound, and conditional Galerkin/residual identities. A fresh constructor replay of the target verify_continuum.py reproduced its85-check JSON exactly, including actual RT1 coefficient constraints and norms. New exact Fraction arithmetic confirms the flux expansion; the floating difference of about4e-16 in the supplied note is arithmetic rounding, not a mathematical discrepancy.

The supplied scalar algebra alone does not reconstruct the entire flux or independently establish functional-analytic hypotheses. No independent-review status is inferred from the title 'Independent Premise & Mathematical Verification' in the supplied text.

## 2. Corrections to the supplied review

| Supplied assertion | Correct scoped statement |
|---|---|
| lambda1=(pi/diameter)^2 | Payne-Weinberger gives lambda1>=pi²/2 for this domain. It does not identify the actual first eigenvalue. |
| Prior5-node gap lambda_h=10 |10 was a certified lower bound for the14-node refined mesh. The original5-node J1 model has positive squared eigenvalues20,20,40,80. Neither discrete statement identifies the continuum gap. |
| gamma_UD is a topological invariant derived from connectivity | gamma is a declared external damping parameter of the scalar-wave benchmark. No native derivation or topological selection was supplied. |
| Scalar-wave acoustic benchmark / UD–GR–QFT counterpart table | The contract is a declared scalar-wave benchmark, without an acoustic-field identification or a sourced GR/QFT correspondence. The proposed table is not accepted into the claim lineage. |
| alpha=min(pi/dihedral) determines the3D shift and interpolation constant | Edge-wedge ratios alone do not determine vertex/conical regularity or a global numerical interpolation/elliptic constant. |
| Envelope 'diverges' on the fixed positive-damping band | It becomes large but stays finite on the declared compact band with gamma>=1/10. True divergence concerns the zero-damping/resonance limit, not a pole on that fixed band. |
| A solver tolerance O(h^r) universally preserves the quadratic output rate | This can balance state error; a raw output generally has a first-order algebraic contribution. An output-specific residual rule or corrected output is needed. |

Primary regularity reference: Monique Dauge, 'Regularity and singularities in polyhedral domains',2008, slides13–19 distinguish3D vertex solid-angle Laplace-Beltrami spectra from edge wedge conditions. https://dauge.pages.math.cnrs.fr/publis/Talk_Karlsruhe08.pdf . A regularity theorem may apply to this convex Neumann domain, but it still does not compute the requested numerical C_app from a minimum dihedral ratio. This receipt does not settle that constant.

## 3. Inexact Galerkin allowance

Use the same fixed volume port and zero-mean complex H1 space as PR223. Let u be the continuum solution, uh the exact Galerkin solution and v the actually computed, conforming, zero-mean finite-element field. Keep the mesh/forms/load exact for this algebraic error analysis; geometry, quadrature, rounding of the residual evaluation and nonconforming/gauge errors need separate bounds if present.

Define the restricted algebraic residual

    r_h(w_h)=ell(conj(w_h))-a_z(v,w_h),
    epsilon_alg=||r_h||_(Vh'),

with the equivalent coefficient convention r_h(w_h)=rho^T conj(w_h), rho=g-Aq. In a verified mean-free basis whose gradient Gram K_V is positive definite,

    epsilon_alg² = rho* K_V^(-1) rho.

Here * is conjugate transpose. An unscaled Euclidean residual norm or a software tolerance is not automatically this dual norm. A singular full Neumann stiffness matrix cannot simply be inverted without fixing the gauge/basis.

The same rotated coercivity implies

    ||uh-v||V <= epsilon_alg/beta,
    |ell(uh)-ell(v)| <= sqrt5 epsilon_alg/beta.

Hence an available discretization-output bound D_h yields a raw total bound

    |H-ell(v)| <= D_h + sqrt5 epsilon_alg/beta.

For a prescribed algebraic output budget delta_alg, the sufficient rule is epsilon_alg<=beta delta_alg/sqrt5, or beta_* on the whole band. This is a derived norm-aware stopping rule, not a tested floating-point solver implementation.

## 4. Residual-corrected output restores the quadratic identity

Use the complex symmetric BILINEAR form b_z from PR223 and define

    r_b(v)=ell(v)-b_z(v,v),
    J_corr(v)=ell(v)+r_b(v)=2ell(v)-b_z(v,v).

In coordinates, J_corr=2g^T q-q^T A q. These transposes are NOT conjugate transposes: this is an analytic complex transfer, not the Hermitian energy norm. The residual dual norm in Section3 is Hermitian, so the two conventions must stay distinct.

For any admissible v (even without exact Galerkin orthogonality), set e=u-v. Symmetry gives

    H-ell(v)=b_z(e,e)+r_b(v),
    H-J_corr(v)=b_z(e,e).

Proof: ell(e)=b_z(u,e)=b_z(e,e)+b_z(v,e), while b_z(v,e)=ell(v)-b_z(v,v). Thus the correction removes the first-order algebraic term exactly when the forms/residual are evaluated exactly. A flux estimate eta for v, with R=F-zv+div tau retained, gives

    |H-J_corr(v)| <= B eta²/beta²,
    |H-ell(v)| <= B eta²/beta² + |r_b(v)|.

This extends the continuum certificate to inexact solves without pretending orthogonality still holds. Any finite-precision error in J_corr, eta, forms or residual must be added conservatively. No actual IEEE solver or rounding-error certificate is supplied here.

If discretization state error is O(h^r), epsilon_alg=O(h^r) is sufficient for total state error O(h^r) and consequently for a quadratically bounded corrected output, assuming the needed certified evaluations. For the uncorrected raw output, the displayed general bound instead needs epsilon_alg=O(h^(2r)) to guarantee the same output order. These are sufficient worst-case conditions, not necessary universal Krylov tolerances.

## 5. Exact check scope and next work

57 new Gaussian-rational assertions PASS on the original J1 port subspace at omega in{0,1,4,6}, gamma=1/10 and real/complex perturbations. They check the corrected identity, raw first-order term, dual-norm bounds and first-versus-second-order error scaling exactly. They are finite algebra witnesses, not independent review, refined-mesh equilibration or floating-solver validation. The prior85-check replay is reported separately.

The next implementation return should combine refined H(div) flux equilibration with a verified algebraic dual-residual budget, using a declared numeric backend. Quantitative regularity/interpolation constants remain a separate theorem/computation. Preserve the native UD action/state/units gap and physical promotion0.
