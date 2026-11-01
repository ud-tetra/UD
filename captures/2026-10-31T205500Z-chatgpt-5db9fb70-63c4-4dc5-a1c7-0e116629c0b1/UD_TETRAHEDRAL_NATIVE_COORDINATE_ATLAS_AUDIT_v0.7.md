# Unified Dynamics — Tetrahedral Native Spatial Coordinate Atlas

**Artifact:** `UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_AUDIT_v0.7`  
**Date:** 2026-10-31  
**Status:** DEVELOPMENT — NO REGISTRY ENTRY; mathematical model and scoped exact proofs only.  
**Physical promotion:** 0. No native metric/clock/energy selection theorem or empirical bridge has been established.

## 0. Purpose, sources and typed provenance

**User instruction:** Reformulate the UD 3D picture around tetrahedral spatial cells *with coordinates*, replacing cube-centered intuition. Preserve complete cell filling, reversible coordinate readout, gluing, and typed energy bookkeeping. Do not equate an abstract tetrahedron with all of physical space.

**Sources and precedence:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), especially P01–P09 (K4 incidence, selection), F01–F05 (dimension-typed ratio family), G05 (native action coefficient OPEN), Q153–Q154 (source/sink semantics) and Q165–Q179 (fixed-chain-carrier support). Development dependencies: `UD_TETRAHEDRAL_SPACETIME_4_OVER_3_FOLD_AND_ENERGY_AUDIT_v0.5.md` and `UD_SIMPLEX_FILL_LADDER_AND_VOLUME_CLOSURE_AUDIT_v0.6.md`, 2026-10-31. UD GitHub `ud-tetra/UD` AGENTS.md and CONTRIBUTING.md require immutable capture and constructor/independent review separation. External comparison: Conway and Torquato, *Packing, tiling, and covering with tetrahedra*, PNAS (2006) DOI 10.1073/pnas.0601389103, and the standard Freudenthal partition literature. Neither literature source is a native UD dynamics law.

**Object types:** An abstract graph `K4` is not a filled 3-simplex `Δ³`. `V_i∈R³` are geometric vertices; `λ_i∈R` are **affine barycentric spatial coordinates**, not physical amplitudes, independent dimensions, elapsed time or burden. `n_i` are unit frame vectors, `N` is a 4×3 analysis matrix, `g` a positive-definite local spatial metric (when specified), `E_T` an integral of a declared test energy density, `B_T` native UD burden (a different object), `U_{ij}` native transport (not a coordinate scalar), `τ` an independent candidate temporal coordinate only after a causal clock bridge. `R_3=4/3` appears in several *different typed equations*: equality of values is not proof of equality of objects.

## 1. EXACT — Point → line → triangle → volume are the barycentric support strata

Given a nondegenerate tetrahedron with affine vertices `V_0,...,V_3∈R³`, assign

\[
P=\sum_{i=0}^3\lambda_iV_i,\qquad \sum_{i=0}^3\lambda_i=1.
\]

The interior is exactly the region `λ_i>0` for every i, while the closed cell is `λ_i≥0`. Within the cell, the **minimal face containing** `P` has geometric dimension

\[
\boxed{\dim\operatorname{face}(P)=|\{i:\lambda_i>0\}|-1.}
\]

The support sequence is therefore

| Positivity pattern of barycentric weights | Minimal occupied geometric stratum |
|---|---|
| `(1,0,0,0)` | point, 0-simplex |
| `(1/2,1/2,0,0)` | segment interior, 1-simplex |
| `(1/3,1/3,1/3,0)` | triangle interior, 2-simplex |
| `(1/4,1/4,1/4,1/4)` | tetrahedral interior, 3-simplex |

**Proof:** Faces of a simplex are exactly convex hulls of subsets of its vertices. Convex combinations with strictly positive weights in an index set are in the relative interior of that subset's face. A nondegenerate simplex has affinely independent vertices, giving uniqueness. The formal *addition of a filled face/cell* remains a separate simplicial occupancy event. This is a coordinate classification of an admitted simplex, not a physical birth law.

## 2. EXACT — Regular tetrahedron: four scalar weights, precisely three spatial coordinates

Define unit vectors

\[
\begin{aligned}
n_0&=(1,1,1)/\sqrt3,\\
n_1&=(1,-1,-1)/\sqrt3,\\
n_2&=(-1,1,-1)/\sqrt3,\\
n_3&=(-1,-1,1)/\sqrt3.
\end{aligned}
\]

Let `N∈R^{4×3}` have rows `n_i^T`. Then

\[
N^T\mathbf1=0,\qquad N^TN=\frac43 I_3.
\]

For a position `x∈R³` measured from the unit-circumradius tetrahedron's centroid, the exact forward and inverse maps are

\[
\boxed{\lambda(x)=\frac14\mathbf1+\frac34Nx,\qquad
x=N^T\lambda,\qquad \mathbf1^T\lambda=1.}
\]

**Proof:** The first equation sums to one since `N^T1=0`. Substituting into `N^Tλ` yields `3/4(4/3) x=x`. Conversely, the linear operator `3/4 NN^T` is the orthogonal projector onto the three-dimensional sum-zero hyperplane. It follows that the map is bijective between `R³` and the affine hyperplane `1^Tλ=1` (with the nonnegative quadrant selecting the tetrahedral cell).

**Exact metric pullback:**

\[
\boxed{d\ell^2=dx^Tdx=\frac43\sum_{i=0}^3(d\lambda_i)^2,\quad\sum_i d\lambda_i=0.}
\]

This equality follows from `dλ=(3/4)Ndx` and `N^TN=(4/3)I`. If circumradius is `R`, the coefficient is `4R²/3`. If edge length is `a`, since `a²=8R²/3`, it is `a²/2` instead. **These are metric units, not inferred native energy units.**

**Crucial separation:** The four barycentric weights form only **three independent spatial coordinates**; their sum-one direction is fixed. In particular their redundant fourth component is **not the variable singlet** `q=u^Tz` in the earlier v0.5 four-*unconstrained-channel* decomposition. Neither one is automatically a physical time coordinate. A 3+1 chart requires a separately admitted temporal coordinate `τ` and physical signature/causal laws.

**Symmetry:** Every permutation `P∈S4` of the four vertices induces an orthogonal map `O_P=(3/4)N^TPN`. These 24 maps preserve the three-dimensional metric; their determinants are the permutation parities. The result is verified exactly for all 24 permutations.

## 3. EXACT — Nonregular tetrahedra are admissible metric charts

Let `A=[V_1−V_0\;V_2−V_0\;V_3−V_0]`. With independent chart coordinates `μ=(λ_1,λ_2,λ_3)` and `λ_0=1−λ_1−λ_2−λ_3`, define

\[
 x(\mu)=V_0+A\mu,\qquad g^{(T)}_{ab}=\partial_a x\cdot\partial_b x=(A^TA)_{ab},
\]

\[
\boxed{V_3(T)=\frac{|\det A|}{6}.}
\]

When `det A != 0`, `g` is positive definite. This construction does not assume regular (equilateral) cells. **Gluing condition:** For tetrahedra meeting along a common face, the two face-coordinate maps must identify the same physical point; the induced metric on the shared face must match (possibly after an explicit affine transition map). Orientation and flux are recorded with opposite incidence signs across the shared internal face.

**Independent exact benchmark:** For vertices `[(0,0,0),(2,0,0),(1,3,0),(0,1,4)]`, `det A=24`, volume `4`, and the pullback metric is `A^TA`. Exact SymPy verification shows positive definiteness and metric/coordinate consistency.

## 4. NO-GO — Regular tetrahedra alone do not face-to-face tile flat Euclidean 3-space

The internal dihedral angle `θ` of a regular Euclidean tetrahedron satisfies `cos θ=1/3`. In a face-to-face tiling by congruent regular tetrahedra, `k θ=2π` around every interior edge, with integer `k`. Then `2cos(2π/k)=2/3`. But `2cos(2π/k)` is an algebraic integer (the sum of a root of unity and its inverse); a rational algebraic integer is an integer. `2/3` is not an integer. Contradiction.

Thus **NO-GO under the stated flat, regular, face-to-face assumptions**. This is not an obstruction to tetrahedra as native 3D coordinate cells: nonregular tetrahedra can mesh Euclidean 3D, or a piecewise geometrical manifold can have curvature/defects; an explicit metric/gluing rule is still required. The familiar six-tetrahedra-per-cube triangulation is one **comparison**, not UD's primitive ontology.

## 5. EXACT — Tetrahedral metric gluing and energy-preserving refinement

Use an affine test density `ε(x,y,z)=4+x+2y+z`, with test-energy observable

\[
E_T:=\int_T\epsilon\,dV.
\]

For an affine `ε`, exact simplex quadrature gives

\[
E_T=\frac{V_T}{4}\sum_{i=0}^3\epsilon(V_i).
\]

For the nonregular tetrahedron in §3, `E_T=31`. Its barycenter subdivides it into four tetrahedra with volumes `(1,1,1,1)` and exact energies

\[
\boxed{(139,131,111,115)/16,\qquad\sum E_{T_i}=31.}
\]

The partition is exact—no volume or test energy is created by a coordinate change/remeshing.

**Two-tetrahedron, noncubic local mesh:** Glue upper and lower tetrahedra along the common triangle with vertices `(0,0,0),(1,0,0),(0,1,0)` and opposite apices `(0,0,±1)`. Their face restrictions agree exactly and have identical induced face metrics. With the same test density:

\[
 E_\text{upper}=\frac56,\quad E_\text{lower}=\frac34,\quad E_\text{total}=\frac{19}{12}.
\]

A signed internal face transfer `J` updates `(E_1,E_2)→(E_1−J,E_2+J)`, preserving the sum. The oriented incidence signs of the shared triangle cancel. This proves **defined mathematical conservation under a declared mesh/ledger model**, not a physical energy law or a native source/sink mechanism.

A field-consistent computational rule must use `E_T=∫_T ε√det(g)d³μ`, with a correct Jacobian and no double counting of boundaries. Without suitable spacetime symmetry, local GR stress-energy continuity is not a general globally conserved scalar-energy theorem.

## 6. CANDIDATE — UD native coordinate grammar, not a physical derivation

**Proposed state:** `X_n=(K_n^3, {V_i}, {g_T}, {U_e}, {B_T}, {E_T}, {J_{T,f}},\text{receipts},n)` where `K_n^3` is a spatial simplicial complex assembled from tetrahedra; `n` is an event ordering index, not measured time; `E_T` and `B_T` are distinct typed quantities until a bridge identifies them. Coordinates in each tetrahedron are `λ^T∈R^4` with `Σλ^T=1`.

**Proposed admission gates, not a sourced Ω0 evolution law:** (i) valid K4 graph / independently admitted triangular faces and 3-cell; (ii) compatible shared-face barycentric charts; (iii) nondegenerate local metric and declared orientation; (iv) signed conservation receipt `E_T^{n+1}−E_T^n+Σ_{f⊂∂T}J_{T,f}=S_T`, without equating native burden to physical energy; (v) separately specified causality/clock and optional holonomy/twist. A source-free closed mesh has `Σ_T ΔE_T=0` by internal-face cancellation. This is a *test contract*, not an autonomous cell creation proof.

For spacetime, a candidate chart is `(λ_0,λ_1,λ_2,λ_3;τ)` with `Σλ_i=1`: **four independent degrees of freedom = 3 spatial + 1 temporal**. A tetrahedron × update-interval admits a triangulation into four 4-simplices, as proved in v0.5. The simplicial 4-cell can model history, but does not automatically furnish Lorentzian signature, measured duration or persistence dynamics. Orientation/twist information remains in the transport representation rather than being encoded by spatial barycentric weights alone.

## 7. Distinct numerical 4/3 appearances — typed identity firewall

| Expression | Object | Status |
|---|---|---|
| `Σ_i n_i n_i^T=(4/3)I_3` | tetrahedral tight-frame operator | EXACT, regular metric frame |
| `dℓ²=(4/3)Σ_i dλ_i²` | Euclidean spatial metric on unit-circumradius barycentric chart | EXACT, constrained weights |
| `V_3/(A_\mathrm{facet}r_3)=4/3` | regular tetrahedron facet-volume/inradius identity | EXACT, geometric scalar |
| ledger `F03 R_3^(tet-face)=4/3` | frozen UD dyad/coframe shape factor | SOURCE-BOUND EXACT; distinct domain/normalization |

Same rational does not imply same operator, physical interpretation or coupling. A typed intertwiner and source-bound normalization audit are required before any identification of these four objects. No existing frozen coefficients are modified.

## 8. Verification, no-go, and next independent bridge test

`UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_VERIFY_v0.7.py` runs exact SymPy checks and emits `UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_RESULTS_v0.7.json`. **121 assertion groups passed** (including 72 exact S4 equivariance/parity checks, four barycentric support-stratum checks, an affine nonregular metric example, four-child conservative refinement, two-tetra face gluing and a separate 3+1 chart rank check). The full global-flat regular-tetrahedral tiling no-go is proved above independently of sampled computations.

**Decisive next physical/source gates:**
1. Derive native positive edge-length/metric functional from packet transport and burden without importing Euclidean lengths.
2. Derive Ω0 occupancy/refinement/birth selection: how four closed triangular faces become a filled tetrahedral cell under an admitted local move.
3. Derive native evolution/clock and Lorentzian signature, independently of the redundant fourth barycentric coordinate.
4. Define native source/current conservation and a calibrated physical energy bridge, including nonconservative open/boundary conditions.
5. Run a target-blind comparative test of tetrahedral atlas transport, alternative cubic-coordinate representation, and twisted/curved controls at matched observable budgets.

**Classification:** EXACT for scoped coordinate and partition constructions; NO-GO for regular-tetra tiling under flat Euclidean face-to-face hypotheses; CANDIDATE for native UD identification; OPEN for physical promotion. No external physical dimensions, energy law, or gravitational/quantum measurement is claimed.
