# Identifiability of the seven-orbit graphite source

22 October 2026 · development — no registry entry · exact conditional inverse-analysis result · physical promotion 0.

## BOOT REPORT

**Question.** Given the seven-orbit geometric source from draft PR #421, can measured static softening, low-frequency damping, or even the full linear-response spectrum determine its material orbit weights? What extra readout would suffice, and what controlled contrast scaling follows?

**Typed objects and metric.** K7 is the exact periodic honeycomb carrier with unit-edge metric and two-dimensional harmonic edge plane. The physical lateral x has metres and Euclidean Cartesian metric; the vertex-bath displacement φ has 14 components in metres under the *assumed* unit vertex metric. The seven C3 orbit projectors `P_i` and rational matrices `K_i=M^T P_i B1^T` are fixed by PR #421. Orbit weights `w∈R^7` are dimensionless; `Q∈Q^(7×7)` is the exact rank-six positive-semidefinite matrix with `K_cart(w)K_cart(w)^T=α(w)I` and `α=w^TQw`. Coupling `g_c` has J/m² per top Bravais cell; clamped curvature k0 and bath κ,d,m_b,γ0 are external material inputs with units in the preceding receipt. The Fourier convention is `e^{-iωt}`, and the full response is per top Bravais cell. This analysis assumes one *degenerate isotropic* 14-site bath per layer and equal-layer relative lift; distinguish a different bath or readout explicitly. No native UD clock, prime, modular, hierarchy or factorization calculation is used (N/A).

**Status and sources.** PRs #419–#421 establish the geometry and conditional bath algebra, not a graphite material source. The supplied coefficient ledger v0.39 Q22–Q26 leaves its edge-source variables open or in a distinct seam sector. The supplied CRL-2 amendment is a proposal. The APS abstract of Chen *et al.*, *PRL* 137, 166201 (2026), DOI 10.1103/ly48-b4l2, reports the paired friction peaks and weak load dependence, but its full text/supplement remain unavailable here. No response or force trace was fitted.

## 1. Exact observational factorization

Write the mean-zero orbit contrast `w_perp=w-(1^Tw/7)1`. Since `Q1=0`, `α(w)=α(w_perp)` and a uniform shift is unobservable to *this mechanism*. Under the preceding independent, identical bilayer bath assumption,

\[
 D_{\mathrm{eff}}(\omega;w)=k_0-m_x\omega^2-i\omega\gamma_0-
 \frac{g_c^2\alpha(w)/2}{\kappa-m_b\omega^2-i\omega d}.\tag{1}
\]

Consequently the entire complex isotropic linear response at **all accessible frequencies** factors through the single scalar `α(w)`, even if `g_c,κ,d,m_b,k0,γ0` are independently known. Its static reduction and low-frequency damping are two multiples of that same scalar. The Jacobian of the pair `(Δk,γ_add)` with respect to the seven weights is

\[
 \mathrm{D}_w(\Delta k,\gamma_{\rm add})=
 \begin{pmatrix}g_c^2/\kappa\\ d g_c^2/\kappa^2\end{pmatrix}
 (Qw)^T,\tag{2}
\]

which has rank one for nonuniform w and zero at uniform w, assuming `g_c≠0`. (The bilayer factor 1/2 cancels against `∇α=2Qw`.) An independently fixed mean and Euclidean norm leave a five-dimensional sphere of possible contrasts; a generic α level within it is at least four-dimensional. Without those normalizations or with unknown material coefficients, ambiguity increases. In particular `w=e_1` and `w=e_2` (indices 1 and 2 in PR #421's orbit order) both give `α=1`, equal sum and norm, yet they cannot be related by an automorphism of `4Q`: vertex 1 touches a weight-2 orbit-graph edge while vertex 2 does not. All responses in Eq. (1) are identical for these distinct sources. Thus a friction fit cannot identify the weights in this assumed bath.

The conclusion applies to this isotropic degenerate bath and isotropic lateral readout. Nondegenerate vertex stiffnesses, site-resolved forcing, additional modes, defects and higher-order response can expose further combinations, but their own parameters and observables must be declared; they do not rescue identifiability retroactively.

## 2. What would identify the contrasts conditionally

Suppose a simulation or apparatus can impose *labeled, calibrated* unit vertex-bath displacements and measure both Cartesian lateral force components, with the physical vertex-to-bath map fixed. This determines the full 2×14 matrix `g_c K_cart(w)` for a single layer (or the corresponding signed bilayer blocks), not merely its isotropic Gram. If `g_c` is independently known, it determines `w` modulo the uniform shift. In direct coordinates define

\[
 b_i=\frac12\operatorname{tr}\!\left[G^{-1}K_i K(w)^T\right]
 =\sum_{j=0}^6Q_{ij}w_j,\qquad i=0,\ldots,6.\tag{3}
\]

Then solve `Qw=b` with the explicit gauge `1^Tw=0`. Since rank Q=6 and ker Q=span(1), the solution is unique in that gauge. Unknown `g_c` leaves an overall scale ambiguity. If the postulated vertex displacement lacks a physical map to actual atomic or phonon coordinates, this is a **computational identification protocol**, not an immediately executable experiment. It would also test the weighted-gradient ansatz itself: a measured cross Hessian outside the six-dimensional span of the K_i falsifies that ansatz under its declared metric and carrier.

## 3. A frozen contrast intervention

For a planned C3-preserving perturbation with independently fixed orbit-direction v and magnitude ε, let `w(ε)=w0·1+εv`; the quadratic form gives the *exact conditional* law

\[
 \alpha(w(\epsilon))=\epsilon^2 v^TQv,
 \quad \Delta k(\epsilon)=\frac{g_c^2}{2\kappa}\epsilon^2v^TQv,
 \quad \gamma_{\rm add}(\epsilon)=\frac{d g_c^2}{2\kappa^2}\epsilon^2v^TQv.\tag{4}
\]

For the declared orbit contrast `v=e_1-e_2`, `v^TQv=5/2`, hence `Δk=5g_c² ε²/(4κ)` and `γ_add=5d g_c² ε²/(4κ²)`. The response is even under `ε↦-ε` and vanishes quadratically near uniform weights. This is an intervention prediction **for the stated candidate bath with fixed material coefficients**, not a statement that ordinary graphite friction is quadratic in strain. A perturbation that also changes `g_c,κ,d`, breaks C3, or activates other friction channels changes the test. Freeze those rules and fit the conventional atomistic baseline before consulting held-out friction/load data.

## 4. Interpretation

The seven-orbit source construction is an exact parameterization, but a single scalar α cannot select a six-dimensional contrast vector. Further model fitting to the paired angles would make the inverse problem look resolved while leaving many inequivalent material sources. A UD-specific prediction requires a source rule fixing w and a bath law independently of graphite friction, or a restricted relation surviving a conventional atomistic baseline. The present intervention and site-resolved cross-Hessian tests are concrete gates for that development lane. `verify_weight_identifiability.py` checks the rank, explicit collision, inverse Gram relation, and quadratic intervention using exact rational arithmetic. Constructor verification only; physical promotion 0.
