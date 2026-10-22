# Harmonic source selection on the seven-cell graphite carrier

22 October 2026 · development — no registry entry · exact conditional geometry and source obstruction · physical promotion 0.

## BOOT REPORT

**Question.** Can the native incidence maps source the bilayer relative harmonic port and its passive bath damping? If edge-dependent transport is admitted, what exact part of that source survives harmonic projection?

**Typed carrier.** The oriented 14-vertex, 21-edge, seven-face honeycomb torus K7 has `B1:C1(Q)→C0(Q)`, `B2:C2(Q)→C1(Q)`, `B1B2=0`, rank(B1)=13, rank(B2)=6. With the *chosen unit-edge metric*, the real harmonic 1-cochain plane is `H=ker B1∩ker B2^T`. The exact geometric lateral map `M:R²_direct→H` has 21 rows `d_e^TG`, `G=[[1,1/2],[1/2,1]]`, and `M^TM=(7/2)G`. Direct-coordinate physical lateral `u` has metres when its basis vectors are the dimensionless primitive directions. Each layer's vertex bath coordinate `φ` has 14 components in metres under an assumed unit vertex metric. Boundary conditions are periodic. The map to a physical friction force requires a separate material energy and a dynamical force estimator.

**Algebraic source types.** Exact/coexact edge sources are `s=B1^T φ+B2 ψ`; the terms' amplitudes/units must be supplied separately. A weighted vertex-gradient source is `s_w=W B1^T φ`, where `W=diag(w_e)` is real, dimensionless and invariant under the actual 120° edge permutation. Its seven orbit values are `w=(w0,...,w6)`. An overall physical coupling `g_c` has J m^-2 per top Bravais cell. The original skew Hodge–Dirac generator is closed and has no physical clock; `κ>0` and `d≥0` for a later conditional bath are imported material coefficients (J m^-2 and N s m^-1). No register, clock, factorization, hierarchy, or continuum limit applies (N/A). All coefficient calculations below are exact Q when weights are formal rational indeterminates; bath response is real symbolic.

**Source dependencies.** The preceding planar capture PR #417 supplies K7 and the exact harmonic map; PR #420 supplies the conditional C3 passive E bath. The supplied ledger v0.39 Q169–Q179 concerns internal support flow, but does not specify a graphite `W`, `g_c`, `κ` or `d`; Q22's seam-source zero has a distinct typed scope. The supplied CRL-2 amendment remains a proposal. The Chen *et al.* 2026 PRL public abstract reports paired weak-load-dependent peaks, but its full text and supplement are subscription gated; no weights or friction curves were extracted. All proposed `W` and bath coefficients remain OPEN, without a fit.

## 1. Exact incidence obstruction

Because `B1 M=0` and `B2^T M=0`, every harmonic `h=Mu` satisfies

\[
 h^T(B_1^T\phi+B_2\psi)=0,\qquad M^TB_1^T=0,\quad M^TB_2=0.\tag{1}
\]

The orthogonal projection onto H is `P_H=M(M^TM)^{-1}M^T=(2/7)M G^{-1}M^T`. Thus `P_H s=0` for any exact/coexact source in the declared metric. A polynomial of the closed Hodge–Dirac generator with zero constant term likewise vanishes on this zero sector. This is a **scoped no-go for incidence-only linear sources**, not a no-go for local sources in general. A periodic local edge field can contain a harmonic component. Changed metrics, material weights, nonlinear terms, open-system forcing or boundaries can invalidate Eq. (1)'s hypotheses.

## 2. Minimal weighted-gradient activation

Take a C3-invariant diagonal edge weight W, constant on each of seven 3-edge orbits in the exact K7 graph, and define the dimensionless geometric coupling matrix

\[
 K(w)=M^T W B_1^T=\sum_{r=0}^{6} w_r K_r,\quad
 K_r=M^T P_r B_1^T\in\mathbb Q^{2\times14}.\tag{2}
\]

The deterministic edge indexing of the accompanying verifier gives the C3 orbits

\[
 (0,9,4), (1,6,13), (2,10,18), (3,7,20),
 (5,8,16), (11,14,12), (15,17,19).\tag{3}
\]

The physical Cartesian coupling satisfies `K_cart(w) K_cart(w)^T=α(w)I_2`; in direct coordinates `K(w)K(w)^T=α(w)G`. Exact enumeration gives

\[
 \alpha(w)=w^T Qw,\qquad
 4Q=\begin{pmatrix}
 2&0&-1&-1&0&0&0\\
 0&4&-1&0&-1&-2&0\\
 -1&-1&4&-1&0&-1&0\\
 -1&0&-1&4&-1&0&-1\\
 0&-1&0&-1&4&-1&-1\\
 0&-2&-1&0&-1&4&0\\
 0&0&0&-1&-1&0&2
 \end{pmatrix}.\tag{4}
\]

The integer matrix `4Q` is the Laplacian of a connected seven-vertex weighted graph with edge weights `c_ij=-4Q_ij` for `i≠j` (values 1 or 2). Thus `α(w)=(1/4)Σ_{i<j} c_ij(w_i-w_j)^2`. This independently proves that `Q` is positive semidefinite with exact rank six and `Q·1=0`. Therefore `α(w)=0` **iff all seven weights are equal**. The common shift `w→w+c1` leaves K unchanged. For one orbit selected with unit weight, `α` is 1/2 for orbits 0 and 6, and 1 for orbits 1–5; C3 symmetry alone does not select an amplitude. We have not established a native law choosing any orbit or any `w`. The `1/2` and `1` are geometric consequences of *illustrative* choices, not fitted or physical constants. A scale ambiguity between `g_c` and `w` also remains until the material weights are normalized independently.

## 3. Conditional bilayer and bath map

With the bilayer relative lift `I_Xu=(-Mu/2,+Mu/2)` and independent identically normalized vertex bath variables `(φ_1,φ_2)`, define the bilinear energy as `E_int=g_c (I_Xu)^T diag(WB1^T,WB1^T) (φ_1,φ_2)`. This adds an explicit energy source absent from the closed chain. Its physical Cartesian 2×28 coupling C satisfies

\[
 CC^T=\frac{g_c^2}{2}\alpha(w) I_2.\tag{5}
\]

The factor 1/2 comes from two independent layer contributions of amplitude 1/2 each, not from seven-cell topology alone. A top-layer-only bath instead gives `g_c²α(w)/4`. If each bath coordinate has *assumed* isotropic stiffness κ and damping d, and the clamped curvature excludes this bath, the low-frequency elimination of PR #420 becomes

\[
 \Delta k=\frac{g_c^2\alpha(w)}{2\kappa},\quad
 \gamma_{\rm add}=\frac{d g_c^2\alpha(w)}{2\kappa^2},\quad
 \gamma_{\rm add}/\Delta k=d/\kappa\quad(\alpha>0).\tag{6}
\]

Stability demands `k0 κ>g_c²α(w)/2`. This is a fully typed **conditional candidate source**, not a derived graphite constitutive law. In particular, if an atomistic baseline already includes the same bath relaxation, the softening and damping must not be added again. A uniform W makes this mechanism vanish exactly, while other direct damping mechanisms may remain. Only an independently specified weight law and material bath can turn Eq. (6) into a numerical prediction; merely choosing `w` to match measured friction would be a fit.

## 4. Exact verification and next material gate

`verify_harmonic_source.py` reconstructs B1, B2, M, the C3 edge orbits, seven K_r and Q using stdlib rational arithmetic. It checks Eq. (1), every matrix element of Eq. (4), the rank-six null, C3 isotropy, and the bilayer 1/2. This is constructor verification, not independent review. Next obtain clamped registry energy and force derivatives versus separation, and determine edge-orbit weights from a material interaction without using held-out friction. The still-missing UD-specific ingredient is a source-selection rule for those weights or a dynamical restriction on `g_c,κ,d` beyond conventional mechanics.
