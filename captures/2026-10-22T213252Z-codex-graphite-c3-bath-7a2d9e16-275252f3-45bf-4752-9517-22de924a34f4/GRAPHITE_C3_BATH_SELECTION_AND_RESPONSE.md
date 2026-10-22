# C3 selection and passive bath response for the planar graphite port

22 October 2026 · development — no registry entry · exact conditional theorem and no-go · physical promotion 0.

## BOOT REPORT

**Question.** Which material modes may couple linearly to the two-dimensional lateral harmonic port at a C3-symmetric registry, and what stiffness and damping follow after eliminating one passive bath? Can a scalar normal mode explain a residual load-independent friction signal?

**Typed carrier and domains.** The prior seven-cell honeycomb cellular torus K7 over Q has C1 harmonic dimension two under the declared unit-edge metric. Its geometric relative-translation lift `I_X:R²_x→H¹_layer1⊕H¹_layer2` has `I_X^T I_X=(7/4)I`, with x in metres. The generator of the closed K7 Hodge–Dirac flow is zero on this port, with no physical time calibration. At a stable registry of the conventional first Fourier shell, the physical lateral displacement x carries the real 2D representation E of C3. A scalar height or breathing displacement z carries A1. An optional *material* shear bath y carries another E, with x,y in metres. The normal load L is force per top Bravais cell. We use the same periodic ideal registry and orthonormal physical Cartesian x as the preceding capture. There is no finite-field, parity, clock, prime, hierarchy or continuum-limit calculation here (N/A).

**Energy/metric and physical map.** Let `k0(L)>0` be the *clamped-bath* lateral curvature (J m^-2 per top Bravais cell). It may be set conditionally to the previously derived first-shell `β_s |V_*(z_m)| g_*²` only when the corresponding V_* and vertical relaxation exclude the y degrees of freedom. The bath stiffness κ(L)>0 is J m^-2, mass m_b≥0 is kg, bath damping d(L)≥0 is N s m^-1, and bare lateral damping γ0(L)≥0 is N s m^-1. The bilinear coupling C has J m^-2. Its source and all values are OPEN. Physical time is seconds as an imported laboratory unit; the cellular generator supplies no clock conversion. Friction readout requires separately specified drive, contact and force estimator.

**Provenance.** K7, I_X and first-shell Hessian come from draft PR #419 (corrected manuscript v4). C3 is the actual ideal honeycomb registry symmetry. Chen *et al.*, *PRL* 137, 166201 (2026), DOI 10.1103/ly48-b4l2, public abstract, establishes paired peaks and weak measured load dependence; article and supplement were subscription gated when checked on 22 October 2026. The user-supplied UD mathematical method v1.0 supplies this typed analysis discipline, not a physical value. Coefficient ledger v0.39 Q22's zero applies to its own seam-sector pairing source, **not** to the present graphite E bath. Its Q23–Q26 source variables likewise supply no graphite coupling. The CRL-2 amendment is a governance proposal, not adopted theory.

## 1. Selection theorem at a C3-fixed registry

Let R be physical rotation by 2π/3 on x, with `R^3=I`, `R≠I`, `R^TR=I`. A bilinear scalar-mode energy `x^T c z` is invariant only if `R^T c=c`. The real planar representation E has no nonzero fixed vector, so `c=0`. **A C3-trivial breathing/height coordinate cannot linearly mix with the lateral port at this registry.** This does not forbid nonlinear `z |x|²`, scalar modulation of the lateral stiffness, a direct damping γ0, coupling away from the registry, or symmetry breaking at edges/defects. In the first-shell `E0(z)+2V(z)S(x)` model, this result is also the exact mixed-Hessian equality `E_xz=2V'(z)∇S(x)=0` at a stable stationary registry.

For one bath E doublet transforming by the same R, invariance of `x^T C y` requires `R^T C R=C`, equivalently `CR=RC`. The real commutant is `C=aI+bJ`, with `J=[[0,-1],[1,0]]` and real a,b. Hence `CC^T=(a²+b²)I`. C3 permits *two* linear coefficients; it sets neither to a physical value. Reflection symmetry or a specified orientation convention can further restrict b, but C3 alone does not. A bath with no E component gives no bilinear contribution from this mechanism.

## 2. Exact single-doublet passive elimination

At fixed L, take the quadratic energy and Rayleigh function per top Bravais cell

\[
 E_2=\frac12 k_0|x|^2+\frac12\kappa|y|^2+x^T C y,
 \qquad \mathcal R=\frac12\gamma_0|\dot x|^2+\frac12d|\dot y|^2,\quad C=aI+bJ. \tag{1}
\]

With a lateral mass m_x≥0 and bath mass m_b≥0, equations driven by force f are

\[
 m_x\ddot x+\gamma_0\dot x+k_0x+Cy=f,\quad
 m_b\ddot y+d\dot y+\kappa y+C^Tx=0.\tag{2}
\]

For the Fourier convention `e^{-iωt}` and `ρ²=a²+b²`, eliminating y gives the exact linear response

\[
 \left[k_0-m_x\omega^2-i\omega\gamma_0-
 \frac{\rho^2}{\kappa-m_b\omega^2-i\omega d}\right]x(\omega)=f(\omega).\tag{3}
\]

At low frequency with κ>0 and `|m_b ω²+iω d|<κ`, the clamped-to-relaxed softening and the leading additional damping are

\[
 \Delta k=\frac{\rho^2}{\kappa},\quad
 k_{\rm rel}=k_0-\Delta k,\quad
 \gamma_{\rm add}=\frac{d\rho^2}{\kappa^2}\ge0,\quad
 \gamma_{\rm eff}=\gamma_0+\gamma_{\rm add}.\tag{4}
\]

Mechanical stability in this two-doublet quadratic energy requires `k0 κ>ρ²` (with κ>0), so `0≤Δk<k0`. When `Δk>0`, the conditional, dimensioned relation is

\[
 \boxed{\gamma_{\rm add}/\Delta k=d/\kappa\equiv\tau_b,}\tag{5}
\]

where τ_b has seconds. For n uncoupled E doublets with `ρ_j²=a_j²+b_j²`, `κ_j>0`, `d_j≥0`, the static and low-frequency contributions add. If `Δk_total>0`, `γ_add/Δk_total` is the convex weighted mean of `τ_j=d_j/κ_j`, so `min τ_j≤γ_add/Δk_total≤max τ_j`. The bound is conditional on this bath decomposition, not a universal graphite constant. At `ρ=0`, both additional quantities vanish and the ratio is undefined.

For fixed-sign nonzero a,b and d,κ, the load response is unconstrained without constitutive inputs:

\[
 \partial_L\log\gamma_{\rm add}
 =\partial_L\log d+\partial_L\log(a^2+b^2)-2\partial_L\log\kappa.\tag{6}
\]

An approximately load-independent damping may result from cancellation of these derivatives, but is not a consequence of C3 or the harmonic topology. Static curvature and low-frequency damping jointly test Eq. (5) if the same extra bath is independently identified. Finite-speed friction also depends on forcing, temperature, geometry, and nonequilibrium dynamics; γ_eff is only a local viscous coefficient in the declared linear model.

## 3. Baseline ownership and falsification

The `V_*` in PR #419 defines a *first-shell energy*. If it was extracted from an atomistic potential that already relaxed y, its curvature is `k_rel` and Eq. (4)'s softening **must not** be subtracted a second time. The coupling model is an extension only when `k0` is explicitly clamped and y is omitted from the conventional baseline. Conversely, an ordinary shear phonon bath is a conventional mechanical ingredient even if x is represented by a UD harmonic cochain. Relabeling that bath UD does not create a residual. To get a distinct UD prediction, the theory must derive a source rule fixing `(a,b,κ,d,γ0)` or a restricted relation that a properly matched conventional bath lacks, before inspecting held-out traces.

The strongest present no-go is: a C3-trivial vertical bath cannot supply bilinear lateral damping, and an E bath can supply an arbitrary positive amount together with static softening. This narrows the mechanism without yielding a parameter-free friction value. Obtain clamped and relaxed registry Hessians and a frequency-resolved lateral response at the paired angles, then compare the measured `γ_add/Δk` with an independently sourced E-bath relaxation time, while fitting the conventional baseline separately. If the response has nonlinear stick-slip or rate-independent friction, the low-frequency linear law alone is inapplicable.

## 4. Checks and limits

`verify_c3_bath.py` checks the invariant-coupling null space, E-doublet commutant and Schur/damping coefficients with exact rational arithmetic on a rationally conjugate 120° representation. Its numeric parameter examples are exact algebra checks, not experimental fits. The article's supplement and raw data were inaccessible; no graphite coefficient is determined. Constructor verification only, physical promotion 0.
