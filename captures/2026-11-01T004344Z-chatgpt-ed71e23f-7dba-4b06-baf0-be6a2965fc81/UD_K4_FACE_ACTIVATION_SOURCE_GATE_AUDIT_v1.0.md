# Unified Dynamics — K4 Face Activation, Cooperative Filling, and Ω₀ Source-Selection Audit

**Artifact:** `UD_K4_FACE_ACTIVATION_SOURCE_GATE_AUDIT_v1.0`  
**Research date:** 2026-10-31 (America/Chicago)  
**Status:** `EXACT_READINESS_DIAGNOSTIC__NO_GO_UNIQUE_NATIVE_BIRTH_FROM_PRESENT_SOURCE`  
**Lane:** `DEVELOPMENT — NO REGISTRY ENTRY`  
**Physical promotion:** **0**  
**Author/constructor:** ChatGPT (GPT-6); independent adversarial reviewer **not yet engaged**.  
**Requested work:** Derive a predictive source-backed face-activation and tetrahedral-filling rule from current UD seam transport, framing, burden continuity; compare with hold, automatic clique-completion, and partially closed controls. No target/back-fit.

## 1. Source and version constraints

| Source | Version and part used | Applicable status |
|---|---|---|
| `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` | 2026-08-22, P01–P09; G05; Q153–Q164; Q165–Q179 | Current attached typed baseline. The `K4` count is exact. G05 action weight and open-system source/sink laws remain OPEN. |
| `UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_AUDIT_v0.9.md` | 2026-10-31, §§1–7 | Four `K4`-derived quadrants, cooperative four-face closure, and no Ω₀ birth mechanism; development only. |
| `UD_SIMPLEX_FILL_LADDER_AND_VOLUME_CLOSURE_AUDIT_v0.6.md` | 2026-10-31, shell/fill and conservation sections | Boundary closure differs from cell interior admission and physical energy accounting. |
| `UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_AUDIT_v0.7.md` | 2026-10-31, barycentric 4/3 frame | Geometric coordinate convention, not a derived physical metric. |
| `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` | Governance proposal, §§1–6 | Nonconstructor review required for promotion; this work remains in development lane. |
| `https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/` | Current site checked 2026-10-31 | Public physical promotion remains 0; no source on this page resolves Ω₀ cell-birth selection. |
| `ud-tetra/UD` repository `AGENTS.md`, `CONTRIBUTING.md` | main SHA recorded in capture manifest | Append-only captures, distinct review and publication states. |

**Source limits:** The ledger gives conditional `j_{B,e}^{mix}=-(1/4)h_e(B^T b)_e` (Q162), a hard-gated existing face→3-cell flux `J_{23}^{h}=2h_f B_{3,fτ}c_{2,f}c_{3,τ}` (Q173), and an open constitutive source `s_B` in `Δρ=Bj_B+s_B` (Q153). These statements do **not** supply an event rule deciding when absent face/cell carriers are created. In particular, `B_3` is not a pre-birth operator on an unoccupied 3-cell: its use is conditional on admitting the cell as a candidate or as actual occupied support. The autonomous Ω₀ rule is not reconstructed here.

## 2. Types, domains, conventions

- `G=K4` is the fixed **four-vertex, six-edge abstract graph**. A graph clique does not automatically contain a filled 2- or 3-simplex.
- `E={01,02,03,12,13,23}`, `F={012,013,023,123}` are **possible oriented simplex labels**. Defining these *comparison slots* is a mathematical probe; it does not assert that a physical UD state has admitted the corresponding faces.
- `C_1^{candidate}=ℝ^6`, `C_2^{candidate}=ℝ^4` use the **counting inner product** and standard increasing-index orientations.
- `B_2:C_2^{candidate}→C_1^{candidate}` is the face→edge boundary matrix. A potential 3-cell `τ=[0123]` has oriented boundary `u=(-1,1,-1,1)^T`.
- `a∈{0,1}^4` records **face occupancy**; `b_3∈{0,1}` records separately **tetrahedral interior occupancy**. The real vector `c∈ℝ^4` records **oriented support amplitude** and is zero in any unoccupied comparison face slot. The statement `c≠0` is an extra observed/seeded preparation, not implied by the graph.
- `U_{ij}` are independent group-valued **seam transports**, allowed to have nontrivial triangular holonomy. They do not equal face occupancy or metric length.
- `ρ∈ℝ^4`, `j_B∈ℝ^6`, `s_B∈ℝ^4` are a **burden ledger**, with source and physical units unspecified. `S_μ=∑c_σ²` is a distinct **quadratic support**. No equality between energy, burden, and support is assumed.
- `P=uu^T/4` is an orthogonal projector under the declared counting metric, not a physical coframe, GR tensor, probability, or action coefficient.
- The equations involve a finite comparison state and mathematical update models, **not** a physical event clock or a source-derived new simplex selection.

## 3. EXACT — K4 face-closure spectral identity

With `B_2` as the standard simplicial boundary map and `u=(-1,1,-1,1)^T`, direct incidence calculation gives

\[
B_2 u=0,\qquad \operatorname{rank} B_2=3,\qquad
\boxed{B_2^{\mathsf T}B_2=4I_4-uu^{\mathsf T}}.
\]

Thus `ker B₂=span(u)` and `P=uuᵀ/4` is the unique rank-one **orthogonal projector onto the closed shell mode** for this declared metric. Writing `c=Pc+(I-P)c` gives the exact support identity

\[
\boxed{\|c\|^2=\frac{(u^{\mathsf T}c)^2}{4}+\frac{\|B_2c\|^2}{4}}.
\]

For **nonzero** `c`, define

\[
C_{\rm cl}(c)=\frac{(u^{\mathsf T}c)^2}{4\,c^{\mathsf T}c},\quad
D_{\partial}(c)=\frac{\|B_2c\|^2}{4\,c^{\mathsf T}c}.
\]

Then `C_cl+D_∂=1`, `0≤C_cl,D_∂≤1`, and `D_∂=0` iff `B₂ c=0`. The zero vector is intentionally **UNSCORED**; its zero boundary is not evidence of completed face support. The normalized diagnostics are mathematical ratios of **amplitude norms**, not material energy, probability or physical time.

For unit-amplitude occupied faces with inherited orientation, `c_i=u_i a_i` and `m=∑a_i`. For `m>0`,

\[
\boxed{C_{\rm cl}=\frac m4,\qquad D_\partial=\frac{4-m}{4},\qquad\|B_2c\|^2=m(4-m).}
\]

The **raw** boundary-defect norm follows `(3,4,3,0)` for `m=(1,2,3,4)`; only the **normalized** defect decreases monotonically in this equal-amplitude control. No inference of a monotone physical energy gradient is permitted. Exactly two binary masks have closed boundary, `0000` and `1111`; only `1111` is **nonempty closed**. Closed shell occupancy does not determine the 3-cell occupancy bit.

## 4. EXACT — Symmetry, orientation, and transport controls

For all 24 `S4` vertex relabelings `σ`, the induced **signed** maps on oriented faces and edges satisfy

\[
B_2 R_2(σ)=R_1(σ)B_2,\qquad R_2(σ)u=\operatorname{sgn}(σ)u,
\]

and `R₂ P= P R₂`. Therefore `C_cl` and `D_∂` are relabeling-invariant and the oriented 3-cell amplitude transforms as a **pseudoscalar** under an odd permutation. If the initial data are completely `S4`-invariant *unoriented* occupancy and scalar burden only, an equivariant deterministic transition cannot produce a **signed nonzero** 3-cell amplitude without an orientation precursor; this does not prohibit un-oriented cell occupancy. An oriented closed shell itself supplies a pseudoscalar sign.

The non-Abelian `S3` transport control has nontrivial triangular holonomy on several faces while `B₂u=0` and `C_cl(u)=1` still hold. **NO-GO:** Requiring flat holonomy on all faces would falsely reject this admissible *combinatorial* closed-shell preparation. Seam holonomy, homological closure, and physical curvature are different typed observables.

For a binary vertex distinction field `b`, choosing edge bits **only** as `e=δb` guarantees `δe=δ²b=0` for every one of the 16 vertex masks. A `δe=0` criterion alone is therefore vacuous and cannot select face birth. An independent seam/framing/edge state may be nontrivial, but its actual influence on occupancy has to be supplied by a constitutive rule.

## 5. EXACT scoped no-go — conservation and readiness do not identify Ω₀

**Input:** a fully admitted 2-shell, unfilled tetrahedral interior, `a=1111`, `b₃=0`, and coherent unit support `c=u/2`; choose an otherwise arbitrary fixed curved or flat `U` and fixed burden state `ρ`. The quadratic face support is `||c||²=1`. Both the following source-independent extensions are possible:

1. **HOLD:** Preserve 2-shell occupancy, support and all transports; leave `b₃=0`.
2. **BIRTH(α,β):** Declare the same occupied 2-shell plus a newly admitted filled `τ` with `b₃'=1`, replace `c` by `αc` and set signed new interior amplitude `c₃'=β(uᵀc/2)`, where `α²+β²=1`, `0<α,β<1`.

Both obey exact **quadratic support** conservation

\[
\|c'\|^2+(c'_3)^2=\|c\|^2,
\]

both preserve closed boundary and all pre-existing seam holonomies, and both are equivariant under `S4` when oriented signs are tracked. For example, the independent rational controls `(α,β)=(3/5,4/5)` and `(5/13,12/13)` produce different nonzero 3-cell amplitudes from identical inputs. These are *witnesses of nonuniqueness*, not recovered UD couplings or natural time steps. Thus even exact incidence + coherence + symmetry + preserved pre-existing transport + conserved quadratic support do not identify whether or how `Ω₀` fills the cell.

**More general isometry:** For any `c` in the candidate face-coordinate space,

\[
F_{\alpha,\beta}(c)=\left((I-P)c+\alpha Pc,\ \beta\frac{u^{\mathsf T}c}{2}\right)
\]

is norm-preserving when `α²+β²=1`. This is an isometric **comparison map between different carriers**, not an established native birth process. The post-admission skew generator `A=[[0,-u],[uᵀ,0]]`, spectrum `{0,0,0,±2i}`, likewise transfers support conservatively **after** `C₃` exists as a carrier. Neither map creates absent face labels or decides event timing from original UD inputs.

**Energy/source no-go with exact hypotheses:** If all original **positive quadratic support**, external reserves, and boundary fluxes are held unchanged, creating a new cell with `c₃²>0` strictly increases total quadratic support and violates this declared conservation. This theorem is about the support functional, **not** physical energy unless a separate source-dependent map identifies the two. Redistribution or a sourced reserve can fund new support, but the native `Ω₀` selection and cost law are OPEN.

## 6. Source-dependent constitutive limits and null controls

Current Ledger v0.39: `Δρ=B j_B+s_B` (Q153), `j_{B,e}^{mix}=-(1/4)h_e(Bᵀ b)_e` in the restricted relaxational regime (Q162), and `J_{23}^h=2h_f B_{3,fτ}c_{2,f}c_{3,τ}` (Q173). A 64-mask exact check of the Q162 **conditional** control conserves `∑ρ` when `s_B=0`; no face occupancy bit changes because the formula supplies none. The Q173 face-to-bulk **support stock-rate** vanishes instantaneously when `c₃=0`, even though an amplitude-level post-admission generator may subsequently produce nonzero amplitude. It cannot be used on an *absent* 3-cell without adding it to the domain.

| Control | Initial conditions | Result under declared mathematics | Scientific scope |
|---|---|---|---|
| HOLD | closed `1111`, `b₃=0` | Shell survives; interior unfilled | Admissible comparison |
| AUTO CLIQUE | only `K4` graph, empty `a` | Auto-filling fails the separate face-readiness and source obligation | Rejected as **native proof**, not as a graph-theory convention |
| PARTIAL masks | `0001,0011,0111`, inherited oriented support | `C_cl={1/4,1/2,3/4}`; `D_∂>0` | Not closed under zero-exposed-boundary rule |
| FULL SHELL | `1111`, coherent oriented support | `C_cl=1`, `D_∂=0` | Readiness PASS; cell occupancy still OPEN |
| CURVED transport | full shell, nonflat `S3` links | Readiness PASS despite curved holonomy | No flatness as necessary criterion |
| Scalar coboundary | any 4-vertex bit mask, `e=δb` | Every `δe=0` | FAIL as discriminating readiness selector |
| TWO conservative lifts | identical full-shell input | Both preserve support yet produce different bulk amplitudes | NO-GO uniqueness |

## 7. Proposed interface (CANDIDATE only)

A source-backed, versioned future update would require the following **independently derived** ingredients, not selected after observing the desired output:

- `Ω_face`: local rule on previous-step `(ρ,θ,χ,U,J,...)` that predicts a face occupancy change `a_f(t)→a_f(t+1)` without assuming the destination face has already appeared. It must distinguish HOLD and AUTO CLIQUE on held-out inputs.
- `Ω_bulk`: a separate interior-occupancy rule that observes nonempty closed shell `B₂c=0` and **source-matched** cost/receipt before setting `b₃=1`. Its structure must be valid for curved and nonuniform controls; no inferred physical energy from counting alone.
- `J_birth`: an incoming/outgoing **typed support or burden** current specified before cell activation, with continuity on the changing carrier, including any external reservoir or conversion into outgoing channels. `Q153` and `Q173` are accounting constraints, not this constitutive map.
- State/clock rule specifying initial/boundary conditions, one-step locality, symmetry/orientation signs, and stability under perturbation and recursion. An event count convention does not determine measured time.
- Independent binary outcomes/retention tests with frozen thresholds and nulls; `C_cl=1` is a necessary shell-closure test under the proposed nonzero support preparation, not a sufficient physical selector.

No parameter-free, source-derived `Ω_face` or `Ω_bulk` has been established in this audit. The unidentifiability witness is a genuine **NO-GO with hypotheses stated**, while the mathematical diagnostic remains a reusable EXACT tool.

## 8. Execution and governance verdict

- Primary exact SymPy implementation: **4,946** assertion groups PASS; `5^4=625` rational face-amplitude vectors (including the zero UNSCORED control), all 16 face masks, all 24 `S4` relabelings, 64 hard-gate burden configurations, full curved-`S3` control, and two distinct conservative birth witnesses.
- Independent Python `fractions.Fraction` implementation: **658** exact checks PASS, with no imports from the main implementation. This is implementation independence, *not* nonconstructor peer review.
- Neither codebase performs physical simulations of native UD `Ω₀`, nor predicts energy, physical spacetime, or an empirical measurement.
- **AUTO_LOCK (mathematical development scope only):** the incidence spectral identity and exact closure-coherence decomposition with zero-vector UNSCORED convention.
- **AUTO_FREEZE:** claiming native face/bulk birth, a derived energy threshold, or unique conservative lifting from current ledger Q153/Q173; retain narrower support mathematics.
- **Required reopening:** retrieve a complete pre-birth move generator with predicted face bits and independent source/sink law, an orientation/sign convention for new cells, an explicit comparison observable and target-blind, independent test. Do not promote any inferred physical geometry or energy until its own bridge passes.

**Bottom line:** The tetrahedral four-face shell has an exact, symmetry-compatible readiness observable. The presently frozen source determines **what closure means** and how support is accounted for on admitted carriers, but does not determine **when a new spatial 3-cell is born**.
