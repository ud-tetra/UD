# UD Lorentzian signature emergence gate v0.1

**13 October 2026 UTC · development, no registry entry · physical promotion 0.** Target: derive, from a declared UD state and dynamics, a four-dimensional *spacetime* metric of Lorentzian inertia, conventionally `(-,+,+,+)`. A chosen sign matrix on the four vertex amplitudes is a conditional internal form; it is not that target.

## 1. Source and type control

| Source | Current usable statement | Scope limit |
|---|---|---|
| [UD Paper I review v1.1.1, §§3–5, 7.4 and 8](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) | An oriented filled tetrahedron has graded real chain carrier `C0⊕C1⊕C2⊕C3`, dimensions `(4,6,4,1)`, unit Euclidean pairing and skew generator `A=B^T−B`. The uniform C0 mode is harmonic. | Chain amplitudes are not spacetime tangent vectors; update parameter has no physical unit. |
| `UD_NATIVE_TENSOR_METRIC_FLUX_MAP_v0.1.md`, 28 September 2026, §§2–5 (Library `libfile_9b89d4f98d888191a216cfced6b05d52`) | On C0, S4-invariant forms are `G=alpha P0+beta Pperp`; the example `alpha=-1,beta=1` is a rational `(-,+,+,+)` form. | Source calls the sign choice *conditional*, with no clock, causal propagation or physical worldline. |
| Supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q101, Q139, Q169–Q170 | Context covariance inverse is distinct from spacetime metric; native global skew operator and exact cut balance are internal; action scale not identified by present geometry/second moments. | No native spacetime tangent bundle, coarse metric, physical clock or Einstein dynamics is supplied. |
| Supplied `recursive_gr_companion.docx`, §interpretive bridge, and historical `Unified Dynamics (Distinction Theory) v2.2_ Master Manuscript.pdf` | Time as phase advance and space as adjacency are interpretive proposals. | No derived Lorentzian principal symbol or normalization in the inspected passages. |
| [Current project portal](https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/) | Papers I–III v1.1.1 and IV v0.1, independent review pending, physical promotion 0. | Publication is not a signature or GR bridge receipt. |

An external methodological comparison is Barceló, Liberati and Visser, [*Analog gravity from field theory normal modes?*](https://arxiv.org/abs/gr-qc/0104001), 2001: linearized fields can produce an effective Lorentzian propagation metric. Their [*Refringence, field theory, and normal modes*](https://arxiv.org/abs/gr-qc/0111059) stresses that multiple modes need not share one metric. Neither paper supplies a UD result.

**Distinct objects:** the positive inner product on `C•(K)`, an indefinite quadratic form on `C0`, an effective inverse metric read from a continuum PDE's principal symbol on `T*M`, a calibrated physical spacetime metric on `TM`, and a GR metric satisfying a sourced gravitational field equation. Equal `4×4` matrices do not identify these carriers.

## 2. EXACT native sign non-selection on one filled tetrahedron

Let `B:C_k→C_{k−1}` be the signed simplicial boundary on the 15-dimensional real graded carrier, with `B²=0`, and define `A=B^T−B`. Let `h=(1,1,1,1)/2` on `C0` and zero on higher grades; `P=hh^T`. Then `B^T h=0`, `B h=0`, and hence `Ah=0`, `AP=PA=0`. For any real `alpha != 0`, put

\[
G_\alpha=I_{15}+(\alpha-1)P.
\]

Because `A^T=-A` and `AP=PA=0`, both terms in `A^T G_alpha+G_alpha A` vanish. Therefore the *same source generator* preserves `c^T G_alpha c` for every `alpha`. In particular `G_1=I15` has inertia `(0 negative,15 positive)`, whereas `G_{-1}=I15−2P` has inertia `(1 negative,14 positive)`. Its vertex block is `I4−(1/2)J4`, diagonalized by the rational orthonormal Hadamard frame into `diag(-1,+1,+1,+1)`. The negative mode `h` is stationary; it is not a derived time direction.

**NO-GO under the stated native premises:** skew-flow conservation and S4 symmetry alone do not select the sign of the uniform mode. This does not prohibit an effective Lorentzian metric on a separately derived continuum spacetime carrier. The exact checker builds every incidence block using rational arithmetic; it verifies `B²=0`, `A²=−L`, both metric conservation identities, the frame, and `L0=4I4−J4` with spectrum `{0,4,4,4}`.

## 3. EXACT inertia barrier for transported metrics

Let `V` be a fixed finite-dimensional real carrier, `F'(s)=A(s)F(s)`, `F(0)=I`, with invertible fundamental solution `F`, and let a symmetric nondegenerate metric `G(s)` satisfy the metric-compatibility evolution

\[
G'(s)+A(s)^T G(s)+G(s)A(s)=0.
\]

Differentiating `F^T G F` makes it constant, so `G(s)=F(s)^{-T}G(0)F(s)^{-1}`. Sylvester's law of inertia then preserves the numbers of positive and negative eigenvalues. Thus a positive initial form cannot evolve into a Lorentzian form through an invertible metric-compatible flow on that same carrier. More generally, any continuous symmetric nondegenerate path has constant inertia; a sign change needs a zero eigenvalue, a discontinuity, or a change of effective carrier/metric definition. This is an **exact conditional obstruction**, not a claim that UD begins with a spacetime metric.

## 4. CONDITIONAL route through a dynamical propagation cone

`A²=−L` holds exactly on the finite chain space because `B²=0`. In particular a vertex-amplitude trajectory `x(s)` under the native first-order flow satisfies

\[
x''(s)+L_0x(s)=0,\qquad L_0=B_1B_1^T=4I_4-J_4
\]

on the single tetrahedron. This is an exact graph oscillator identity, **not** a local `3+1` wave equation: four vertex amplitudes and three contrast modes do not furnish a three-dimensional continuum of spatial wavevectors, a null cone or a physical clock.

**Candidate bridge with explicit assumptions.** Supply a family of increasingly fine *spatial* 3-complexes `K_a`, a source-derived generator `A_a(z)` and a fixed source-authored reconstruction `W_a` into scalar fields on a three-manifold `Sigma`. Linearize around a declared stationary prepared background `z0`, or prove that derivatives of a varying generator contribute only lower-order terms to the principal symbol. Without this step, differentiating a state-dependent first-order equation produces an additional `A'(z)z'` term and the displayed wave principal part does not follow. On the reconstruction image, prove a controlled continuum limit on an open background-state domain, with one common evolution parameter `s`,

\[
a^{-2}W_aL_{0,a}(z_0)W_a^{-1}u
\longrightarrow -\partial_i\big(C^{ij}(z_0,x)\partial_j u\big)+\text{lower-order terms},
\qquad C^{ij}=C^{ji}>0.
\]

The resulting scalar equation has principal part `u_ss−∂_i(C^{ij}∂_j u)=0` and characteristic polynomial

\[
p_{z_0}(\omega,k)=-\omega^2+C^{ij}(z_0,x)k_i k_j.
\]

**DERIVED conditional on the stated convergence and positivity:** this *co-metric* has inertia `(1 negative,3 positive)`, selecting a Lorentzian cone in the declared `(s,x)` chart. An overall sign flip of the metric is a convention; the invariant target is one timelike direction and a consistent null cone. The coefficient `C`, spatial embedding, continuity domain and clock map must come from source dynamics, not a chosen target metric. The symbol fixes a causal conformal structure for that mode; its scale, metric volume, physical seconds, and universal gravitational coupling are additional data.

For multiple modes `m`, verify that their principal polynomials share the same cone (up to positive scalar factors) in a declared low-energy regime. Otherwise UD may yield several effective cones, which does not establish one GR spacetime metric. A hyperbolic scalar sector also does not prove Einstein field dynamics, equivalence-principle behavior or physical correspondence.

## 5. Acceptance and falsification gates

| Gate | Required calculation or evidence | Present status |
|---|---|---|
| S1 — source | Versioned `K_a,z,A_a,W_a`, update/renewal law, preparation and boundary data, with units and carrier maps | **OPEN** |
| S2 — continuum | Consistent refinement, local second-order principal symbol, `C^{ij}>0` with an eigenvalue gap on a declared open domain; source-independent rerun | **OPEN**; K4 alone has no spatial continuum |
| S3 — causality | Hyperbolic well-posedness, oriented cone, stable propagation, shared cone across declared sectors; test for birefringence and degeneracy | **OPEN** |
| S4 — metric | Derive conformal factor/volume and state-dependent metric response; calibrate event parameter to a physical clock and lengths without backsolving | **OPEN** |
| S5 — GR correspondence | Derive or independently test the metric's dynamics and matter coupling against a declared GR limit, observables, units, uncertainties and baseline | **OPEN** |

An observed positive definite/degenerate symbol in the claimed regime, incompatible mode cones, or failure under refinement falsifies the respective universal signature claim. A signature crossing within a continuous fixed carrier must expose its degeneracy rather than hide it through rescaling. A physical bridge needs target-blind calibration and independent comparison; no result here raises physical promotion.

## 6. Disposition

**EXACT:** native generator supports both sign choices; metric-compatible invertible transport preserves inertia; the finite graph oscillator identity. **DERIVED CONDITIONAL:** Lorentzian characteristic co-metric if an independently derived continuum positive spatial principal coefficient exists. **NO-GO:** claiming the current tetrahedral `1+3` amplitude split or preserved `G_{-1}` as a dynamically emerged GR metric. **OPEN:** the spatial scaling family, source response, common causal cone, physical normalization and Einstein dynamics. No AUTO_LOCK of a UD-to-GR metric or physical promotion. Independent review pending.

`Gap2_FINAL_Finite_Genesis.png` could not be made available this turn; no statement relies on it.
