# Unified Dynamics — Native Four-Quadrant Admission and Symmetry Obstruction Audit

**Version:** v0.9  
**Date:** 2026-10-31  
**Claim lane:** `DEVELOPMENT — NO REGISTRY ENTRY`  
**Physical promotion:** **0**  
**Decision:** `STRUCTURAL_PASS / OMEGA0_DYNAMICAL_ADMISSION_SOURCE_BLOCKED`  
**Scope:** Theorems concerning a finite `K4` graph, its simplicial 2-shell and conditional filled 3-cell, intrinsic counting-metric coordinate sectors, and bounded controls. Nothing here identifies the mathematical coordinates with measured spacetime or extracts a physical energy, time or gravitational constant.

## 0. Source control and exact objects

**Read together:**

1. `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, dated 2026-08-22: P01–P09 (`K4` counts, `S4` automorphisms, four-contact *candidate* adjacency), F01–F05 (dimension-typed geometric ratios), G05 (physical action source still open), Q153–Q158 (burden/source bookkeeping and missing constitutive law), Q165–Q179 (support conservation on a fixed chain complex).
2. `UD_TETRAHEDRAL_QUADRANTS_3D_ATLAS_AUDIT_v0.8`, 2026-10-31: a **given** regular tetrahedron has four trihedral cones covering its ambient Euclidean 3-space.
3. `UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_AUDIT_v0.7`, 2026-10-31: four constrained barycentric weights provide three coordinates; regular `4/3` metric identity is geometric and typed separately from ledger F03.
4. `UD_SIMPLEX_FILL_LADDER_AND_VOLUME_CLOSURE_AUDIT_v0.6`, 2026-10-31: shell formation and filled-cell admission differ, with separate energy/source requirements.
5. Designated portal `https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/`, observed 2026-10-31: Papers I–III v1.1.1 / IV v0.1, independent review pending and physical promotion 0.
6. `ud-tetra/UD` repository `AGENTS.md`, read on `main` at `a78193d420f3bac957be081aed0525fbc1457825`: immutable development capture, independent reviewer needed for any promotion, existing frozen claims unchanged.

### Object types

- `G=K4=(V,E)` is the **unweighted abstract graph**, with vertices `V={0,1,2,3}` and six undirected edges. Its Laplacian `L:C^0(G;R)->C^0(G;R)` has nonnegative real spectrum.
- `R^V` has the **declared counting inner product**. Its three-dimensional zero-sum subspace `H=1^⊥` is a derived, *dimensionless coordinate carrier*; it is not already a physical spatial tangent space.
- `v_i∈H` are **embedded graph vertex vectors**; their scale follows a declared, unweighted normalization.
- `F_i` are **oriented triangular face chains** of the tetrahedral 2-skeleton, not the cones.
- `a=(a_0,...,a_3)∈{0,1}^4` is a **face occupancy mask**. `b_3∈{0,1}` is a separate **filled 3-cell occupancy flag**; valid simplicial states with `b_3=1` must have all four faces.
- `Q_i⊂H` is an **unbounded three-dimensional conical coordinate sector**. The quadrant index is a finite chart label, not a continuous fourth spatial coordinate.
- `U_ij∈G_\mathrm{tr}` is a link transport group element, **independent** of `v_i` and triangle occupancy. Scalar burden/current receipts belong to a separate ledger and do not equal coordinate norms or energy without a new map.
- `Ω0` is the project's **source-level native evolution/admission rule**, whose transition law for face bits and new cell occupancy is not supplied by the frozen sources consulted here. `A_quad` below is an explicitly proposed *readout predicate*, not that evolution rule.

## 1. EXACT — Graph-derived regular tetrahedron without external XYZ axes

The combinatorial Laplacian for `K4` is

\[
L = 4I_4 - J_4,\qquad J_4=\mathbf 1\mathbf 1^{\mathsf T}.
\]

Its eigenspaces are `ker L = span(1)` and `H=im L=1^⊥`, with

\[
\operatorname{spec}(L)=\{0,4,4,4\},\quad \dim H=3.
\]

Define the intrinsic graph vertex vectors

\[
\boxed{v_i=\tfrac12 Le_i=2(e_i-\tfrac14\mathbf1)\in H.}
\]

Then

\[
\sum_{i=0}^3v_i=0,\qquad
\boxed{\langle v_i,v_j\rangle=4\delta_{ij}-1},\qquad
\|v_i-v_j\|^2=8\ (i\ne j).
\]

The four vectors form a centered regular tetrahedron *in the abstract three-dimensional Euclidean space `H`*. No orthonormal basis or external xyz axes has been chosen; any orthonormal basis of `H` gives the same geometric object up to `O(3)`. The counting inner product and the factor `1/2` are mathematical conventions. `rank L = 3` alone is **not** proof that the physical substrate is three-dimensional or that a 3-cell is filled.

**Tetrahedral 4/3 identity (same number, distinct type).** With unit-radius directions `n_i=v_i/√3`,

\[
\boxed{\sum_{i=0}^3 n_i n_i^{\mathsf T}=\tfrac43 P_H},\qquad P_H=I_4-\tfrac14J_4.
\]

Restricted to `H`, `P_H` is the identity, giving exactly `4/3 I_H`. This is a new exact graph-induced **tight-frame identity**, not automatically the historical `F03` coframe dyad in Ledger v0.39, nor a dynamical 4-to-3 spacetime reduction.

**Permutation equivariance.** For any vertex relabeling `σ∈S4`, with permutation matrix `P_σ`, `P_σ L P_σ^T=L` and `P_σv_i=v_{σ(i)}`. The induced action on `H` has determinant `sgn σ`; twelve relabelings preserve orientation, twelve reverse it. An unoriented `K4` cannot by itself select an absolute handedness.

**Uniqueness scope.** Under the declared equal-weight counting inner product, centering, and identical pairwise distances, the Gram matrix is fixed up to a common positive scale. Other edge-weight/metric conventions remain admissible and are not ruled out by topology.

## 2. EXACT — The complete tetrahedral fan, derived from `K4`

For the four graph-derived vectors define

\[
\boxed{Q_i=\operatorname{cone}(v_j:j\ne i)
=\left\{\sum_{j\ne i}t_jv_j:\ t_j\ge0\right\}\subset H.}
\]

Because the vectors are affinely independent and sum to zero, `0` is strictly inside their convex hull. Each ray from `0` meets an outer triangular face; hence

\[
\boxed{H=\bigcup_{i=0}^3 Q_i,\qquad
\operatorname{int}Q_i\cap\operatorname{int}Q_j=\varnothing\ (i\ne j).}
\]

Every quadrant has three independent local coordinates. For `x∈H`, set

\[
\lambda_i(x)=\frac{1+\langle v_i,x\rangle}{4},\quad
\sum_i\lambda_i=1,\quad x=\sum_i\lambda_i v_i.
\]

Choose any index `i` attaining `min_j λ_j` and set `t_j=λ_j−λ_i≥0` for `j≠i`. Then `x=Σ_{j≠i}t_j v_j`. The chart is unique off interfaces and compatible on interfaces.

With the regular counting metric, tetrahedral symmetry implies **solid angle** `Ω_i=π` steradians per cone, exactly 1/4 of the unit sphere area. This is not four equal densities or a prediction of any physical isotropic state. It also does not imply that bounded congruent regular tetrahedra tile all of flat `R³`.

### Exact impossibility of choosing one quadrant without state asymmetry

`S4` acts transitively on the four faces/vertex indices. Any subset invariant under **every** `S4` relabeling must be either the empty set or all four. Therefore a deterministic, fully `S4`-invariant selector acting on a completely symmetric `K4` cannot mark exactly one quadrant as privileged. A chirality, asymmetry or oriented frame would require additional input/selection, whose source remains OPEN.

## 3. EXACT — Cooperative four-face closure

Equip the triangle faces `F_i` with the orientation inherited from `τ=[0123]`. The boundary of `τ` is

\[
\partial_3\tau=[123]-[023]+[013]-[012].
\]

Given a binary occupancy mask `a`, form the signed chain

\[
c(a)=\sum_{i=0}^3(-1)^i a_i\,[0,\ldots,\widehat{i},\ldots,3].
\]

**Theorem.** `∂₂c(a)=0` iff `a=0000` or `a=1111`. Every edge is contained in precisely two of the four tetrahedral faces; their signed boundary contributions cancel only when the two corresponding face bits agree. Since every pair of tetrahedral faces shares one edge, all bits must agree. Over `F2` the same result holds. There are exactly two solutions among 16 occupancy masks.

**Cooperative necessity, conditional.** If every admissible intermediate state is required to have **zero exposed boundary** and each basic move toggles one face bit, `0000→1111` has no admissible one-face path. A cooperative four-face event or a rule allowing explicit temporary boundary/source receipts is required. If open partial boundaries are allowed, sequential construction is not obstructed by the theorem.

**Shell is not filled bulk.** `a=1111` defines a closed 2-shell even when `b_3=0`. Only `b_3=1` admits the filled 3-simplex. The chain complex, its homology, and its support operator change when `b_3` switches on. A derived metric, a closed shell, and physical bulk occupancy are three separate assertions.

## 4. CANDIDATE — Minimal *atlas* admission predicate, not native evolution

Let `State(K4)` contain `a`, `b_3`, declared counting metric and independent `U_ij` and source/burden records. For valid simplicial states define

\[
\mathcal A_{\rm quad}(\mathrm{State})=\begin{cases}
\{Q_0,Q_1,Q_2,Q_3\}, & a=1111\text{ and }b_3=1,\\
\bot, &\text{otherwise}.
\end{cases}
\]

Here `⊥` means that a **filled-cell spatial atlas has not been admitted**; the algebraic fan can still be constructed for a graph-only state. The map has domain `State(K4)` and codomain `Fan4(H) ⊔ {⊥}`. It commutes with `S4` relabeling and does not require flat holonomy.

To promote this predicate into a true **source-backed Ω₀ transition**, the program must supply a separate evolution

\[
\Omega_0:(K,a,b_3,\rho,\theta,\chi,U,J,\ldots)_n
\longmapsto (K',a',b'_3,\rho',\theta',\chi',U',J',\ldots)_{n+1}
\]

and a conserved typed source/stock receipt when a cell or face occupancy changes. The current frozen ledger specifies `C0⊕C1⊕C2⊕C3` support continuity for a **fixed carrier**, while the `Ω₀` cell-birth trigger, constitutive burden source, and physical-time map remain OPEN.

### NO-GO — Static geometry does not identify a birth evolution

On an unfilled `K4` graph, both `Ω_hold(a)=a` and `Ω_complete(a)=1111` are deterministic, idempotent, `S4`-equivariant maps respecting graph incidence. They disagree on whether any face cells arise. Static graph symmetry and incidence cannot decide which evolution is realized, much less what funds it. This proves a **source-identification obstruction**, not that a native Ω₀ law is impossible to derive once additional dynamics are provided.

## 5. NO-GO — The bare binary vertex coboundary is a vacuous trigger

The primitive substrate permits a distinction cochain `b∈C⁰(K4;F₂)`. If the edge bits are *only* its coboundary `e=δb`, then for every triangular face

\[
\boxed{\delta e=\delta^2b=0.}
\]

Thus requiring all triangles to have zero binary parity does **not** distinguish between any two vertex distinction states. All 16 vertex states pass. There are eight distinct edge-gradient states (because global vertex complementation does not change differences). Among all 64 independent six-edge bit assignments, only eight are flat; the others produce an even-parity face syndrome. These 8/64 are exact counts, **not physical probabilities**, and their numerical equality to any other eight-state UD fiber does not establish object identity.

Consequently, a nontrivial face-ready selection mechanism needs an independent edge/transport state, constitutive source, or occupancy dynamics beyond `δ²=0`. Flatness is not imposed as a requirement on the general non-Abelian transport branch.

## 6. EXACT mathematical robustness tests, not physical validations

**Metric deformation:** For positive rational edge weights `w_ij`, define `L_w=Σw_ij(e_i−e_j)(e_i−e_j)^T`. Its pseudoinverse gives a candidate *resistance-squared* distance `R_ij=(e_i−e_j)^TL_w^+(e_i−e_j)`. This construction is canonical relative to declared `w`, is `S4`-equivariant under simultaneous relabeling of weights, and yields rank-three Euclidean vertex geometry for a connected weighted `K4` graph. Unequal weights generally break equal solid angles. Neither weights nor electrical-resistance distance are yet shown to be native UD physical metrics.

**Curved seam transport:** An explicit non-Abelian `S3` connection was assigned to six graph edges, producing nonidentity holonomy on three of four triangular loops. Under all `6^4=1296` vertex gauge transformations, the holonomies conjugate as expected and the nonflat-face count is invariant. The combinatorial four-face cycle and geometric fan remain valid. A condition requiring every triangle to have trivial holonomy would be too restrictive for this curved control and is not part of the candidate selector.

**Independent check:** A separate pure-`fractions.Fraction` program uses the three-dimensional signed tetrahedron `(±1,±1,±1)` rather than the graph-Laplacian embedding. It independently verifies pairwise Gram entries, 16 face masks and the four-cone inversion on 125 integer points. This is an independent *implementation*, not independent scientific peer review.

## 7. Execution record and falsifiable acceptance boundary

- `UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_VERIFY_v0.9.py`: **4,119** exact assertion groups passed, including 343 rational coordinate points, all 24 `S4` relabelings, all 16 face masks, all 64 independent edge-bit fields, and all 1,296 local `S3` gauge transformations.
- `UD_K4_NATIVE_FOUR_QUADRANT_INDEPENDENT_CHECK_v0.9.py`: **539** checks passed using only exact Python fractions and distinct 3D coordinates.
- `UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_RESULTS_v0.9.json`: full assertion and control ledger.

**Scoped structural pass:** canonical intrinsic four-sector geometry; `S4` covariance; cooperative all-or-none closed shell; metric deformation tolerance; curved group transport compatibility.

**NO-GO / source blocker:** no observed or sourced Ω₀ cell-birth dynamics, energy trigger, physical metric or measured time; a vertex-only exact-coboundary gate is vacuous; no guaranteed individual quadrant direction from a symmetric K4.

**Reopening conditions:** Recover or derive the actual `Ω₀` primitive move family including **initial conditions**, allowed partial-boundary states, constitutive source/sink laws, and a graph/metric coframe readout. Pre-register distinct alternatives before observing any downstream physical targets. Test fresh growth/retention evidence against `hold`, `automatic clique-completion`, and random/sequential face-admission controls. Physical promotion remains **0**.
