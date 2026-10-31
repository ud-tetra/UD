# Unified Dynamics — Point-to-Tetrahedron Filling Ladder and Volume Closure

**Version:** v0.6  
**Date:** 2026-10-31  
**Status:** DEVELOPMENT — NO REGISTRY ENTRY  
**Physical promotion:** **0**  
**Method:** exact chain complexes, integer homology, F2 facet enumeration, metric determinant checks, tetrahedral facet-volume and energy-receipt controls.  
**Scope:** a reproducible *mathematical* filling grammar; not native UD growth, a physical energy-generation law, a physical clock, or a proof of fractal emergence.

## 0. Sources, nomenclature, and dependency boundaries

Authoritative context: `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22): P01–P09 (K4 structure and face-sharing selector), F01–F05 (dimension-typed ratios, especially `R_d=(d+1)/d` and F03's `4/3` under an independently declared dyad), G05 (native action normalization/source still OPEN), Q153–Q154 (typed source/sink), Q169–Q179 (finite support gluing on fixed chain carrier; open-system semantics still OPEN). Existing development: `UD_K4_K5_NATIVE_BIRTH_J34_CURVED_METRIC_AUDIT_v0.3.md` and `UD_TETRAHEDRAL_SPACETIME_4_OVER_3_FOLD_AND_ENERGY_AUDIT_v0.5.md`, both 2026-10-31. Designated UD portal (retrieved 2026-10-31): Papers I–III v1.1.1 / IV v0.1; physical promotion 0. External comparison: discrete exterior calculus (MathWorld) and the Vietoris–Rips / flag construction (Scientific Reports 2021); not imported as a native selection law.

**Typed objects:** `K_n` is the abstract complete graph on *n vertices*; `K_0` is empty, `K_1` has a single vertex; `Δ^d` is a **filled** d-simplex; `∂Δ^d` is its (d−1)-dimensional **boundary shell**; `skel_k Δ^d` is the subcomplex of simplices through degree k; `C_k` is the oriented chain space, `∂_k` its incidence/boundary map; `f_k` counts admitted k-simplices. `V_d` is metric d-dimensional volume; `E` is integrated test energy; `S` is native support stock; `B` is native burden. These are not synonymous. `d` denotes dimension, not event count or time.

## 1. EXACT — One interior cell is different from a closed boundary

For a simplex with ordered vertices `v_0,...,v_d`, oriented boundary is

\[
\partial_d[v_0,\ldots,v_d]=\sum_{i=0}^d(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_d],
\qquad \partial_{d-1}\partial_d=0.
\]

For a triangle and tetrahedron,

\[
\partial_2[012]=[12]-[02]+[01],
\qquad
\partial_3[0123]=[123]-[023]+[013]-[012].
\]

`∂z=0` proves that `z` has no exposed boundary **as a chain**. It does **not** prove that an interior cell with boundary `z` is already present. Conversely, an arbitrary closed polygonal loop is not necessarily a single simplex boundary; the required facet/vertex incidence must be present (or a lawful triangulation added).

**Shell-first gate** (purely kinematic construction): given a filled `(d−1)`-simplex `c=[0,...,d−1]`, create a new apex `a=d`. The cone operator `h_a` prefixes `a` to each oriented simplex. Under augmented chains for `d=1`,

\[
\partial h_a+h_a\partial=\mathrm{id},\qquad
z_{d-1}:=c-h_a(\partial c)=\partial[a,0,\ldots,d-1].
\]

The two admissible **construction** steps are

\[
K_{\rm shell}=\Delta^{d-1}\cup(a*\partial\Delta^{d-1})=\partial\Delta^d,
\qquad
K_{\rm filled}=K_{\rm shell}\cup\{[a,0,\ldots,d-1]\}=\Delta^d.
\]

Both are exact valid simplicial complexes; no native UD update has been proven to select or fund either step. The first stage leaves a closed topological shell, the second adds the higher-dimensional interior.

### 1.1 EXACT — Pascal simplex-increment theorem

A filled d-simplex has `f_k(Δ^d)=C(d+1,k+1)` k-cells. Consequently, extending a filled `(d−1)`-simplex to a filled d-simplex introduces

\[
\boxed{\Delta f_k=\binom{d}{k},\quad k=0,\ldots,d.}
\]

| Lift | New vertices/edges/faces/cells | Shell stage before final fill |
|---|---|---|
| point → segment | `(1,1)` | two endpoints |
| segment → triangle | `(1,2,1)` | three-edge loop |
| triangle → tetrahedron | `(1,3,3,1)` | four-face 2-sphere |
| tetrahedron → 4-simplex | `(1,4,6,4,1)` | five-tetrahedron 3-sphere |

This is an exact **inventory** recurrence, not an energy spectrum, growth frequency, or fractal theorem. In particular, `K_4` (graph) has `f=(4,6)`; admitting its four triangular faces produces `f=(4,6,4)`; admitting its tetrahedral interior produces `f=(4,6,4,1)`.

### 1.2 EXACT — Filling kills a specific topological cavity

For d≥2, `∂Δ^d≃S^{d−1}`. Its top homology has rank one. Admitting the unique top d-cell makes the filled simplex contractible:

\[
\boxed{H_{d-1}(\partial\Delta^d;\mathbb Z)\cong\mathbb Z,
\quad H_{d-1}(\Delta^d;\mathbb Z)=0.}
\]

For d=1, the two endpoints have reduced `\tilde H_0≅Z`, while the filled segment is connected. The top-boundary vector spans `ker ∂_{d−1}` within the complete shell when d≥2. Its homology class becomes a boundary only after `C_d` is introduced. This is a strict topological distinction between **geometric enclosure** and **cell occupancy**.

The exact rational-rank audit gives:

| Fixed graph / complex | Betti signature of nontrivial positive-degree holes |
|---|---|
| `K3` graph (3 edges) | `β1=1` |
| `skel_2 Δ²` (filled triangle) | no positive-degree holes |
| `K4` graph (6 edges) | `β1=3` |
| `skel_2 Δ³` (four triangular faces, unfilled bulk) | `β2=1` |
| `Δ³` (filled tetrahedron) | no positive-degree holes |
| `K5` graph (10 edges) | `β1=6` |
| `skel_2 Δ⁴` (10 triangles) | `β2=4` |
| `skel_3 Δ⁴` (5 tetrahedra, unfilled 4-cell) | `β3=1` |
| `Δ⁴` (filled 4-cell) | no positive-degree holes |

More generally, for `0≤k<n`, the k-skeleton of the n-simplex has reduced homology concentrated in degree k with rank `C(n,k+1)`. This follows from exactness of the augmented full-simplex chain complex, and the rank formula `rank ∂_k=C(n,k)` in its full chain groups. The finite cases above were recomputed with exact matrices.

### 1.3 EXACT — Cooperative closure is all-or-none on a minimal simplex shell

For a complete minimal `(d−1)`-faceted shell `∂Δ^d`, encode each of its `d+1` facets as a binary occupancy bit. Requiring **zero exposed codimension-two incidence modulo 2** permits only the empty set or all facets: every pair of facets meets on one distinct shared codimension-two face, hence their binary occupancies must agree. An independent exhaustive GF(2) enumeration tested the full sets of `2²,2³,2⁴,2⁵` facet masks for d=1,2,3,4 and found exactly those two zero-boundary configurations in every case.

This is a finite combinatorial **cooperative closure selection**; it does not establish energetic cooperation, dynamics or spontaneous birth. Nor does `∂²=0` imply flat group holonomy `U_C=I`: curvature may remain on a filled triangle. Flatness is an extra transport hypothesis.

### 1.4 NO-GO — Strict flag-complex completion removes independent fill events

In the **flag/clique complex** `Flag(G)`, every complete `(k+1)`-vertex subgraph is automatically declared a filled k-simplex. For `K4`, this includes its four triangles **and** the filled tetrahedron immediately. Consequently, any model that adopts this completion as an instantaneous identity has **no distinct observable time window** in which the same complete `K4` graph has an unfilled tetrahedral shell. If UD intends a dynamically admitted `F_3` event, it must retain separate incidence/occupancy or admission data beyond the graph. The flag construction is an external mathematical comparator, not a derived UD fill rule. See https://www.nature.com/articles/s41598-021-84486-1 and https://mathworld.wolfram.com/DiscreteExteriorCalculus.html.

## 2. EXACT — How triangular faces determine enclosed 3D geometric volume

For an oriented nondegenerate tetrahedral boundary with outward unit normals `n_f`, triangular areas `A_f` and face centroids `c_f`, the divergence theorem with vector field `X(x)=x` gives

\[
\boxed{V_3^{\rm enclosed}=\frac13\sum_{f=1}^{4}A_f\,c_f\cdot n_f.}
\]

The origin is arbitrary because the oriented area vectors close: `Σ_f A_fn_f=0`. On the coordinate unit tetrahedron `0,e1,e2,e3`, the three coordinate-plane triangles contribute zero to the volume moment and the inclined triangle contributes `1/2`, yielding `V=1/6` exactly. An independent determinant gives `V=|det(e1,e2,e3)|/6=1/6`.

**Essential scope:** The boundary formula computes the *geometric volume enclosed by a positioned and oriented shell*, even if `C_3` is absent. It is not an occupancy sensor: the same four triangles can bound an empty tetrahedral cavity in the abstract complex. A native fill witness must still establish top-cell admission.

### 2.1 EXACT — General dimension-typed facet-to-volume factor

Let `Δ^d` be a **regular**, nondegenerate Euclidean simplex with edge length `a`, common facet `(d−1)`-volume `A_{d−1}`, and inradius `r_d`. The incenter partitions the simplex into `d+1` disjoint facet-cone pyramids, each of d-volume `A_{d−1}r_d/d`. Therefore

\[
\boxed{V_d=\frac{d+1}{d}\,A_{d-1}r_d,
\qquad R_d^{\rm volume}=\frac{d+1}{d}.}
\]

Exact formulas (`d≥1`, `V_0=1` as zero-dimensional measure convention) are

\[
 r_d=\frac{a}{\sqrt{2d(d+1)}},\qquad
 V_d=\frac{\sqrt{d+1}}{d!\sqrt{2^d}}a^d.
\]

Consequently

\[
R_1=2,\quad R_2=\frac32,\quad R_3=\frac43,\quad R_4=\frac54,
\]

and specifically for a regular tetrahedron (`A=√3a²/4`, `r=√6a/12`),

\[
\boxed{V_{\rm tetra}=4\bigl(\tfrac13Ar\bigr)=\tfrac43Ar=\tfrac{\sqrt2}{12}a^3.}
\]

**Provenance lock:** The numerical ratios match the frozen ledger's dimension-typed family `F01`, including `F03=4/3` and `F05=5/4`. The new volume ratio is typed `R_d^(volume)`; the frozen `F03` is a coframe-shape factor under a separately declared dyad and `F05` is a 5-state address-frame identity. **Do not identify their operators, domains, observables, or normalization solely from numeric equality.** This is a testable structural correspondence candidate, not a new physical coefficient.

### 2.2 EXACT — Why metric rank and cell fill remain independent

All four vertices of an abstract filled `Δ³` can be sent to coplanar Euclidean coordinates: then the Euclidean Gram determinant is zero despite the **abstract** top cell being present. Conversely, the four triangles may have positive enclosed geometric volume even when the 3-cell is absent. Thus positive Gram rank and top-cell occupancy are independent predicates. A nondegenerate Euclidean 3D realization requires `det G>0` for the 3×3 displacement Gram matrix.

## 3. EXACT — Conservative *refinement* versus unsourced *volumetric birth*

**Refinement:** Choose the barycenter `b=(v0+v1+v2+v3)/4` of an existing tetrahedron and replace it with four children `conv(b, F_i)`, one for each outer face. Barycentric coordinates ensure each child has exactly `V_parent/4`; their interiors are disjoint and their union is the parent. For any integrable test energy density `ε`, partition additivity gives

\[
E_{\rm old}=\int_{\Delta^3}\epsilon\,d^3x
=\sum_{i=1}^{4}\int_{\Delta_i^3}\epsilon\,d^3x
=E_{\rm refined}.
\]

An exact affine-density control `ε=1+x+2y+3z` on the coordinate unit tetrahedron gives `E_parent=5/12`, and child energies `(23/192,7/64,19/192,17/192)`, summing to `5/12`. The parent energy was verified independently by direct threefold integration. Iterating such four-way refinement for `n` uniform generations creates `4^n` occupied tetrahedral cells each of volume `V/4^n`: the total region and total geometric volume remain unchanged. This is **not** an emergent higher spatial dimension or a proof of a noninteger fractal dimension.

**Genuine birth:** If the initial object supports only a triangular face with energy per area `σ` and a newly admitted tetra volume has energy per volume `ρ`, the two quantities are typed and cannot be equated as densities. Conservation requires an explicit receipt, e.g.

\[
E_{\rm surface}^{\rm before}+E_{\rm reserve}^{\rm before}
=E_{\rm surface}^{\rm after}+E_{\rm bulk}^{\rm after}+E_{\rm emitted},
\quad E_{\rm bulk}=\int_{\Delta^3}\rho\,d^3x.
\]

**NO-GO (closed, unchanged-old-stock, positive-new-energy):** When the face and all pre-existing energy reserves remain unchanged and there is no incoming source, a strictly positive newly admitted bulk energy violates conservation. This holds irrespective of the geometric `4/3` or Pascal coefficients. For a conserved reserve `R`, every choice `E_bulk=αR`, `E_reserve_after=(1−α)R`, `0≤α≤1` is algebraically conservative; conservation alone does **not** select `α`. Tests `α=0,1/3,1` all satisfy the same receipt.

**Temporal dimension firewall:** A completed **spatial** 3-cell and a physical spacetime evolution event are distinct. The v0.5 model triangulates a tetrahedral spatial prism over an event interval into four 4-simplices; that is a kinematic decomposition with no physical clock. A point → edge → triangle → tetrahedron filling ladder does not create metric time or imply Lorentzian signature.

**Fractal control:** A geometric subdivision filling an unchanged tetrahedral region maintains a 3D support. A corner-only four-child half-scale rule yields declining occupied volume and a limiting Hausdorff dimension 2 under the standard self-similarity hypotheses. Identical four-way branching counts do not discriminate the two. Finite Pascal increments therefore establish neither fractal growth nor physical energy levels.

## 4. CANDIDATE — UD fill-admission gate, typed and falsifiable

Define a pre-event source state `Z_n=(K_n,X_n,U_n,B_n,S_n,...)`, where geometry, burden, and support have separately declared carriers, units, metrics and ledger norms. A candidate operation `F_d` may admit one new d-cell only after:

1. **Incidence:** its complete proper face set is present; an oriented shell `z=∂σ` is explicitly identified and `∂z=0` verified. A general cycle that cannot be the boundary of a *single* simplex does not qualify without additional subdivision.
2. **Independent occupancy gate:** the top cell is absent before the move, and the native source law produces a new occupancy witness after. Do not infer occupancy from complete graph adjacency or metric enclosed volume.
3. **Transport:** edge/face holonomy is computed in its proper group/fiber. Nonzero holonomy is not automatically illegal; any flatness condition needs an independent native proof.
4. **Geometry:** if physical Euclidean volume is claimed, require positive Gram determinant and a length assignment derived from the source dynamics. A 4D Lorentzian claim needs a separately derived signature/causal structure.
5. **Conservation:** identify all debit and credit terms for native support and (separately) physical energy; record boundary/radiative/latent exchanges. Do not reuse `4/3`, `7/192`, or `G1=4` as a new action weight.
6. **Selection:** compare filled and unfilled states with the same skeleton, same initial support, and identical available source; measure whether the native update selects one without post-hoc tuning.

The source ledger has a fixed-chain support program, a scoped face-sharing default `G1=4`, and unresolved higher-cell/open-system source laws. No native `Ω_0` trigger, 2→3 filling cost, 3→4 filling cost, physical time map, or energy allocation has been derived from those rows in this artifact. The mathematical geometry is ready for an independent dynamical selection test; `F_d` remains a **CANDIDATE**, not a native dynamical theorem.

**Null/falsification gates:** (i) same `K4` graph, face-only versus filled tetra; (ii) same oriented face shell, no cell versus occupied cell; (iii) nonflat transport (allowed/forbidden only by declared rule); (iv) coplanar geometric degeneration; (v) source-free positive-bulk creation; (vi) fixed-volume four-way refinement versus volume-deleting corner fractal; (vii) non-simplex closed cycles. A gate fails if its proposed native output cannot distinguish the required test or violates the ledger.

## 5. Reproduction and decision

Run `python3 UD_SIMPLEX_FILL_LADDER_VERIFY_v0.6.py` with Python 3.11+ and SymPy. It regenerates `UD_SIMPLEX_FILL_LADDER_RESULTS_v0.6.json` and prints an exact verification transcript. Verified scope: **110 exact assertion groups**, including ∂²=0, shell/filled integer-rank Betti numbers, exhaustive GF(2) facet cycles, Pascal increments, cone identities, regular-simplex Gram determinants, general `R_d^(volume)` incenter volume reconstruction, oriented boundary flux, and conservation via independent direct integration. This is a constructor verification, **not independent peer review**.

**Decision:** `EXACT` geometry and topology of the filling ladder; `DERIVED CONDITIONAL` conservation for an unchanged integration domain; `NO-GO` unsourced positive-energy bulk formation under stated hypotheses; `OPEN` native filling/admission, energy source, time and observed physical geometry. No frozen ledger amendment or physical promotion. The result may be captured as a new immutable development artifact, not merged into a completed spacetime or energy claim.
