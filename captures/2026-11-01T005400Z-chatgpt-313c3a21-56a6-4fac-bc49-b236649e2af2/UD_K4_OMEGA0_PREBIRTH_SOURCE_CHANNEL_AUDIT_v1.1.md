# Unified Dynamics — Primitive Pre-Birth Source Channel and Native Tetrahedral Admission

**Version:** v1.1  
**Research date:** 2026-10-31  
**Lane / status:** `DEVELOPMENT — NO REGISTRY ENTRY` · `STRUCTURAL_PASS__NATIVE_BIRTH_SOURCE_BLOCKED`  
**Claim types:** `EXACT` (conditional finite mathematics), `DERIVED` (source implications), `NO-GO` (stated hypotheses), `CANDIDATE` (source interface), `OPEN` (constitutive dynamics)  
**Physical promotion:** **0**  
**Construction/testing:** ChatGPT GPT-6; executable independent *implementation*, no nonconstructor adversarial peer review.

## 1. Mandate and frozen source precedence

**Requested task:** Execute the highest-value step from `UD_K4_FACE_ACTIVATION_SOURCE_GATE_AUDIT_v1.0`: derive, if possible, a source-backed one-step update for face activation and three-cell filling from admitted native UD variables, not a shape-matching ansatz. Avoid fitting a trigger, rate, cost, or metric. If blocked, derive the strongest source-independent result and identify the exact missing input.

Relevant current source strata and types:

| Source | Exact version/location | Source claim and limitation |
|---|---|---|
| `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63` | 2026-08-22, P01–P09; G05; Q153–Q179 | The K4 incidence and support accounting are typed; G05 loop action normalization, Q153/Q158 predictive source/sink constitutive laws, and Q157 open-system support connection remain OPEN. Q162 is a conditional relaxational burden flux. Q169–Q173 act on already admitted chain spaces. |
| `UD_K4_FACE_ACTIVATION_SOURCE_GATE_AUDIT_v1.0`, SHA-256 `3c404bdf0d1df82e61cb1c8556e60e2109c29d35476b9f30781a4ffd62354c38` | 2026-10-31, §§2–8 | The closed-shell readiness observable and same-input HOLD-versus-BIRTH no-go are exact within the candidate-carrier model. This v1.1 audit tightens the representation-theoretic direction of an admissible source channel. |
| `UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_AUDIT_v0.9`, SHA-256 `49acf83807b0fe6b057d48b3e57880e7817f6b53ca698708091eaf9d47600cd5` | 2026-10-31, intrinsic quadrant construction | The four mathematical spatial quadrant cones follow from K4 symmetry; they do not supply the native occupancy event. |
| `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`, SHA-256 `8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4` | Governance proposal §§1–4 | This is constructor-checked development, not CRL-2b or physical promotion. |
| UD site `https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/` | Home, Papers I–III 1.1.1 / IV 0.1, retrieved 2026-10-31 | Physical promotion 0, independent review pending. No exhibited update source deriving the birth predicate. |

**Source collision guard:** The mathematical `4/3` tight-frame factor and the orientation-sign channel below are different typed operators; neither inherits physical meaning from the numerical value of frozen F03. `Ω0` symbolic grammar is not a complete physical generator.

## 2. Formal objects and assumptions

- **Fixed comparison graph:** `K4` on vertices `0,1,2,3`, six oriented edges. This graph does **not** force triangular faces or an interior tetrahedron to be occupied.
- **Comparison face space:** `C₂^cand = ℝ⁴`, with oriented face basis `f_i=[0,...,\hat i,...,3]` and standard counting inner product. Binary occupancy `a∈{0,1}⁴` is distinct from amplitudes `c∈C₂^cand`.
- **Candidate interior:** `C₃^cand=ℝ` with oriented generator `τ=[0123]`; actual occupancy is a separate binary variable `b₃∈{0,1}`. Before the event, actual `C₃` may be absent; the comparison slot is not a declaration that it exists.
- **Boundary:** `B₂:C₂^cand→C₁^cand`, `B₃:C₃^cand→C₂^cand`. Choose `u=(-1,1,-1,1)^T=-B₃τ`. This sign is a declared orientation convention; changing it does not change the projectors or conclusions.
- **Group action:** `S₄` permutes vertices and induces signed orthogonal face matrices `R₂(σ)`; the oriented interior transforms by `sgn(σ)`.
- **Support:** `S₂(c)=cᵀc` (counting norm), **not** physical energy or burden. `ρ` is a separate vertex burden ledger, and `U_ij` are separately typed seam/group transports.
- **Conservation test:** An optional *comparison* after-admission map preserves `S₂+S₃` in an enlarged carrier, with `S₃=z²`; this is not a native dynamic admission.
- **Clock:** None. A model rotation angle is an algebraic transfer control, not event count or measured duration.

## 3. EXACT — Unique S4-equivariant linear oriented shell-to-interior map

**Theorem 1.** For the above face representation `R₂` and oriented 3-cell sign representation `sgn`, the space of equivariant real linear maps

\[
\mathrm{Hom}_{S_4}(C_2^{\mathrm{cand}},C_3^{\mathrm{sign}})
\]

has dimension exactly **one**. Every such map has the form

\[
\boxed{\ell(c)=\gamma u^{\mathsf T}c,\qquad \gamma\in\mathbb R.}
\]

If the target is instead an orientation-**even** scalar carrying the trivial `S₄` representation, then

\[
\boxed{\mathrm{Hom}_{S_4}(C_2^{\mathrm{cand}},\mathbb R_{\mathrm{triv}})=\{0\}.}
\]

**Proof.** Map face `i` to its complementary tetrahedral vertex `i`, retaining the orientation sign. This identifies the signed face representation with `sgn⊗ℝ⁴_perm`. The four-dimensional permutation representation decomposes into the one-dimensional constant-vector sector and the irreducible three-dimensional zero-sum sector. Hence the signed face space decomposes into one `sgn` line, generated by `u`, plus a three-dimensional summand containing no trivial or `sgn` line. The only linear equivariant map to the oriented interior is projection onto `u`, up to scalar. A map into the untwisted scalar target must vanish. ∎

**Independent matrix verification:** For all 24 `σ`, the constraints `R₂(σ)ᵀ a=sgn(σ)a` have rank `3` on `ℝ⁴`, giving `ker=span(u)`; the constraints `R₂(σ)ᵀa=a` have rank `4`, giving `ker={0}`. Tested in SymPy and independently in `fractions.Fraction` with a separate Gaussian elimination implementation.

**Physical limitation:** This determines *the allowed linear direction of coupling*, not whether a 3-cell exists, the sign of an external source, a rate, magnitude, physical handedness, or physical energy. An orientation-even quadratic scalar such as `(uᵀc)²` is invariant, but discards the orientation sign. A nonzero source in a scalar lane could also be nonlinear or carry extra symmetry-breaking state; the zero statement is limited to **linear** maps from this face representation alone.

## 4. EXACT — All-or-none fully symmetric binary hard face gates

For a hard gate vector `h∈{0,1}⁴` transformed by the **unsigned** face permutation, full `S₄` invariance is equivalent to

\[
\boxed{h=(0,0,0,0)\quad\text{or}\quad h=(1,1,1,1).}
\]

This is because the induced action is transitive on the four faces. All 16 masks were exhaustively tested under all 24 permutations. If independent vertex or transport data break that symmetry, partially active masks can be permitted **as transient states** but they cannot be mistaken for closed tetrahedral shells. As proven in v1.0, the only nonempty binary closed-shell mask is `1111`.

**NO-GO:** Symmetry restricts the gate to two options but cannot decide between **HOLD** and **ALL-ON**. Requiring full closure from the outset would rule out gradual intermediate masks, but still cannot select when a cooperative event occurs.

## 5. EXACT — Unique normalized channel, nonunique amplitude

The boundary matrix identity is

\[
B_2^\mathsf{T}B_2=4I_4-uu^\mathsf{T},\qquad
P=\frac{uu^\mathsf{T}}4,\qquad
Q=I-P.
\]

The normalized oriented closed-shell coordinate is

\[
q(c)=\frac{u^\mathsf{T}c}{2},\qquad
\|c\|^2=\|Qc\|^2+q(c)^2.
\]

Any rational or real pair `(α,β)` with `α²+β²=1` defines a *comparison* isometric embedding

\[
\boxed{F_{\alpha,\beta}(c)=\left(Qc+\alpha Pc,\;\beta q(c)\right)}
\]

satisfying

\[
\|Qc+\alpha Pc\|^2+\beta^2 q(c)^2=\|c\|^2.
\]

For an initially fully coherent shell `c=u/2`, the following outcomes have identical input support and exact output support `1`:

| Comparison output | Interior occupancy | Face-support amplitude | Interior amplitude | `S₂+S₃` |
|---|---:|---:|---:|---:|
| HOLD | 0 | `1` | `0` | `1` |
| BIRTH A | 1 | `3/5` | `4/5` | `1` |
| BIRTH B | 1 | `5/13` | `12/13` | `1` |

The fractions above are **counterexample witnesses**, not derived UD coefficients, physical energy fractions, probabilities, or a preferred mixing angle.

**NO-GO under stated constraints:** Symmetry, closed-shell readiness, the preserved preexisting seam connection, and conserved quadratic support do not identify the birth event or transfer fraction. This is not a universal impossibility theorem for future source-enriched dynamics.

### 5.1 Minimal skew exchange *after* the candidate cell is admitted

With normalized direction `w=u/2`, consider the block generator on `C₂⊕C₃`:

\[
A_\lambda=\lambda\begin{pmatrix}0&-w\\w^\mathsf{T}&0\end{pmatrix},\qquad
A_\lambda^\mathsf{T}=-A_\lambda.
\]

Its spectrum is `\{0,0,0,+i\lambda,-i\lambda\}`, and for `\lambda=1` the exact matrix has `A³=-A`. It rotates only the closed-shell support and the oriented cell amplitude, preserving quadratic stock. **But the matrix is not defined as a native birth event on an absent `C₃`**; it is a post-admission comparison generator. The scalar `λ`, event clock and admission condition remain source-open.

## 6. EXACT — Sharp support-funding constraint, not a physical cost law

If `Qc` is preserved and the only support receiving transfer is the newly admitted interior, then, with no external support reserve,

\[
\boxed{0\le z_{\mathrm{new}}^2\le q(c)^2,\qquad
\Delta S_2=-z_{\mathrm{new}}^2.}
\]

For the isometric family, `z_new²=β²q²`. The sharp upper bound is reached at `β²=1`, which leaves the closed-shell face amplitude zero; an independent *face-retention* requirement might forbid this endpoint, but such a requirement is not supplied by current source laws.

If a measured or native support reserve `R` is admitted, the balance becomes `\Delta S_2+\Delta S_3+\Delta R+J_{\partial}=0` under one declared sign convention. This is an accounting equation, not a prediction for `R`, `β`, or physical energy. A free-standing positive-energy cell with no stock transfer, source, or boundary receipt would violate conservation; do **not** identify `S_μ` with physical energy without an independent unit and observables bridge.

## 7. Source-constrained nulls: why presently frozen laws cannot choose

### 7.1 Q153, Q158: continuity is a receipt, not the source constitutive law

The ledger specifies

\[
\Delta\rho=B_1j_B+s_B,\qquad s_B:=\Delta\rho-B_1j_B.
\]

The first is a typed continuity requirement, and the second a residual identity. Neither predicts `s_B` from previous admissible state. They therefore cannot determine whether and when the previously absent face/interior occupancy bits toggle. This conclusion is scoped to the **presently retrievable** source records.

### 7.2 Q162 restricted relaxational flux does not determine birth

For the declared source regime,

\[
j_{B,e}^{\rm mix}=-\frac14 h_e(B_1^\mathsf{T}\rho)_e.
\]

For spatially uniform `ρ` on `K4`, `B₁ᵀρ=0`; this yields `j_B^mix=0` for **every** binary edge-hard-gate mask. All 64 masks were checked. Both HOLD and an internally stock-transferring comparison BIRTH are consistent with this restricted zero burden flux because burden stock and quadratic support are **not identified**. Other native currents or internal nonuniform states could select birth if explicitly sourced.

### 7.3 Q173 vanishes at c₃=0 but does not disprove later propagation

\[
J_{23}^{(f,\tau)}=2h_fB_{3,f\tau}c_{2,f}c_{3,\tau}
\]

vanishes for `c₃,τ=0`, even if the candidate faces are coherent (16 face-hard-gate controls verified). This **does not** establish that the derivative of `c₃` must be zero if a candidate cell space and its **linear** skew generator have already been installed: early-time amplitudes could grow while `c₃²` starts only at quadratic order. But that would presuppose the destination carrier. Q173 is not an operator that **creates** the destination's incidence labels or occupancy bit.

### 7.4 The automatic coboundary condition is not selective

For any vertex distinction field `b∈C⁰(K4,𝔽₂)`, `e=δb` satisfies `δe=0` automatically. All `2⁴=16` vertex masks were checked. Therefore `δe=0` alone cannot be a face-birth selector. It also does not identify actual matter/energy sources or introduce an independent seam twist.

## 8. CANDIDATE — Minimum source-complete Ω₀ admission interface

An implementable *future* source-complete rule must define, independently of target output, at least the following typed maps:

1. **Face pre-birth source:** `\Gamma_f : X_t^{\rm admitted}→\{0,1\}` (or a proved event intensity/probability model) determining face *occupancy* before the destination slot is declared; distinguish source data, orientation and support amplitude.
2. **Interior event source:** `\Gamma_\tau : X_t^{\rm admitted}→\{0,1\}` selecting HOLD versus BIRTH when the nonempty full shell is ready. The source may use transported frame and burden **only if** a native law specifies how.
3. **Signed transfer magnitude/source:** `\beta_\tau : X_t^{\rm admitted}→[-1,1]` or equivalently a sourced exchange generator. Full `S₄` symmetry fixes the **linear shell direction**, not this magnitude.
4. **Stock and burden receipt:** a source-derived typed `j_B,s_B,J_{\rm birth}` plus source-volume ownership rule on the changing simplicial complex. No residual post hoc source is admissible as a prediction.
5. **Evolution/time and readout:** admissible initial/boundary conditions, orientation convention, event ordering, conserved quantities, metric choice, physical time map and observational bridge.

One exact future mathematical update could use `F_{α,β}` *after* `\Gamma_\tau=1`; it must remain a `CANDIDATE` until both `\Gamma_\tau` and `β` are calculated from source-native inputs. The two outcomes at identical inputs prove these missing data are not forced by current closure/conservation alone. A new pre-birth axiom is an amendment, not a discovery from frozen rules.

## 9. Execution record / independent check

- Primary `sympy` exact verifier: **5,377** passed assertions in **27** test groups, including the full `S₄` signed representation, linear intertwiner dimensions, all binary occupancy/gate masks, bounded isometric transfers, uniform burden controls, and source-nonuniqueness witnesses.
- Separate `fractions.Fraction` verifier with hand-implemented rational Gaussian elimination: **4,760** passed assertions in **12** test groups. It imports **no** primary script or SymPy.
- Source snapshots: v0.39 ledger and v1.0 face-activation audit, both SHA-256 identified above; no source rewrites.
- The two mathematical implementations are *implementation-independent* but **not** a nonconstructor adversarial peer review; full-source `Ω₀` code and empirical data not supplied.
- `AUTO_LOCK` **within exact mathematical scope**: the one-dimensional signed intertwiner, no nonzero even linear intertwiner, all-or-none invariant hard gate, and norm-preserving family.
- `AUTO_FREEZE`: any assertion that these establish unique native cell birth, source cost, measured time, physical energy, or a completed spacetime theory.

### Reopening conditions

Recover a source-complete generator deriving `\Gamma_f`, `\Gamma_\tau`, and transfer source from previous-step state. Freeze input/output, normalization, sign, null cases, and acceptance criteria *before* new target exposure; then test independent same-stock HOLD/BIRTH controls and curved/nonuniform cases, with an adversarial reviewer not responsible for constructing the model. Only a separately calibrated physical observable bridge can change physical promotion from 0.

**Research verdict:** A unique symmetry-compatible **oriented linear face-to-volume channel** exists. The existing source still **does not select a unique event or rate**, and conserved support cannot be silently retyped as physical energy.
