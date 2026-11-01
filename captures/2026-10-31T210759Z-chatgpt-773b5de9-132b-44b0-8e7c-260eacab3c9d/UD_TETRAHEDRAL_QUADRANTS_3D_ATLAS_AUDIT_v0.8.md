# Unified Dynamics — Tetrahedral Quadrants as a Complete Three-Dimensional Coordinate Partition

**Artifact:** `UD_TETRAHEDRAL_QUADRANTS_3D_ATLAS_AUDIT_v0.8`  
**Date:** 2026-10-31  
**Status:** DEVELOPMENT — NO REGISTRY ENTRY. Mathematical claims are exact only under their specified geometric assumptions.  
**Physical promotion:** **0**. No primitive spacetime, energy, physical isotropy, temporal metric, or native Ω₀ growth dynamics are inferred.

## 0. Mission and source control

**Question:** Can the full three-dimensional coordinate carrier be constructed using **four tetrahedral quadrants**, rather than eight Cartesian octants, without dropping spatial degrees of freedom or conserved integrals?

**Controlling source:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (2026-08-22), rows P01–P09 (primitive K₄ counts and candidate adjacency), F01–F05 (dimension-typed ratios, including the exact `R₃^(tet-face)=4/3` under its declared dyad definition), G05 (unfixed native action coefficient), Q153–Q154 (source/sink bookkeeping), and Q165–Q179 (fixed-carrier support and global support gluing). **Development dependency:** `UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_AUDIT_v0.7.md` (2026-10-31) and `UD_SIMPLEX_FILL_LADDER_AND_VOLUME_CLOSURE_AUDIT_v0.6.md` (2026-10-31). The live designated portal continues to list physical promotion zero. Historical results are not independent proof of the present construction.

**Types:** `T⊂R³` is a geometric filled tetrahedron; `O` is its barycenter; `F_i⊂∂T` is a triangular face; `T_i⊂T` is a bounded child tetrahedron; `Q_i⊂R³` is an *unbounded trihedral cone* (a spatial quadrant); `λ_i` are affine scalar barycentric coordinates with sum one; `t_j` are **three local conical coordinates** in a chosen quadrant; `g_i` is a metric pullback; `E_i` is a declared mathematical density integral, **not** native UD burden `B_i`. The quadrant **index** `i` is a chart label, not a fourth continuous coordinate or physical time.

## 1. EXACT — Four tetrahedral quadrants cover R³

Set

\[
\begin{aligned}
v_0&=(1,1,1),&v_1&=(1,-1,-1),\\
v_2&=(-1,1,-1),&v_3&=(-1,-1,1),
\end{aligned}
\qquad O=(0,0,0).
\]

The vectors are the vertices of a regular tetrahedron centered at `O`; they satisfy

\[
\sum_{i=0}^{3}v_i=0,\qquad v_i\cdot v_j=\begin{cases}3&i=j\\-1&i\ne j.\end{cases}
\]

Let `F_i=conv({v_j:j≠i})` be the face opposite `v_i`. Define the **tetrahedral quadrant**

\[
\boxed{Q_i:=\operatorname{cone}(F_i)
=\left\{\sum_{j\ne i}t_jv_j:\ t_j\ge0\right\}.}
\]

This is an unbounded, closed, convex **three-dimensional trihedral cone**. It is not a bounded regular tetrahedron.

### Theorem 1: No-gap four-quadrant covering

\[
\boxed{\mathbb R^3=\bigcup_{i=0}^{3}Q_i,\quad
\operatorname{int}(Q_i)\cap\operatorname{int}(Q_j)=\varnothing\ \ (i\ne j).}
\]

**Proof A (ray geometry):** `O` lies strictly inside the convex tetrahedron `T=conv(v₀,v₁,v₂,v₃)`. Every ray from `O` exits this tetrahedron through at least one of its four triangular faces. The directions of the four faces exhaust all possible rays, and distinct face interiors have disjoint ray directions. Therefore their cones cover all `R³` with only boundary overlaps.

**Proof B (explicit inverse coordinates):** For any `X∈R³`, define the global affine coordinate functions

\[
\lambda_i(X):=\frac{1+v_i\cdot X}{4},\quad
\sum_i\lambda_i=1,\quad
X=\sum_i\lambda_iv_i.
\]

Choose any index `i` attaining `min_j λ_j`. Then

\[
X=\sum_{j\ne i}(\lambda_j-\lambda_i)v_j,
\quad t_j:=\lambda_j-\lambda_i\ge0.
\]

This exhibits `X∈Q_i`. For a strict minimum, the sector index and local coordinates are unique. When the minimum is tied, `X` lies on a sector interface and the duplicated chart representations agree geometrically. QED.

### Exact incidence of the quadrant fan

- **4** three-dimensional quadrants, one per face;
- **6** two-dimensional pairwise interfaces: `Q_i∩Q_j=cone(v_k,v_l)` for the complementary indices `k,l`;
- **4** one-dimensional triple intersections, each a ray along one `v_i`;
- **1** fourfold intersection, the origin `O`.

This is a complete **three-dimensional** charting scheme. It does **not** claim the global topology of physical space must be `R³` or require an additional spatial coordinate.

## 2. EXACT — Equal solid angles: tetrahedral quadrants versus Cartesian octants

The regular tetrahedron's rotational group acts transitively on its four triangular faces and preserves solid angle. The quadrants cover all directions on `S²` with only measure-zero boundary overlaps. Since the sphere subtends `4π` steradians, each of the four congruent sectors subtends

\[
\boxed{\Omega_i=\pi\ \mathrm{sr},\qquad\sum_i\Omega_i=4\pi\ \mathrm{sr}.}
\]

Independent exact check: for the three **unit** generators `a,b,c` of any sector, pairwise dot products equal `−1/3`, so the denominator of the standard trihedral-angle formula is

\[
1+a\!\cdot\!b+b\!\cdot\!c+c\!\cdot\!a=0,
\]

and the absolute triple product is `4√3/9>0`. Therefore

\[
\Omega=2\operatorname{atan2}\bigl(|\det(a,b,c)|,0\bigr)=\pi.
\]

The four regions are **not** standard Cartesian quadrants (2D) or octants (3D). “Tetrahedral quadrant” is the defined name for this four-way 3D conical partition.

## 3. EXACT — Local coordinates and metric: three dimensions, four sectors

Let `M_i=[v_j]_{j≠i}∈R^{3×3}` (columns ordered by increasing index). Every `M_i` is invertible with `|det M_i|=4`. Thus in sector `Q_i`,

\[
X=M_it,\quad t\in\mathbb R^3_{\ge0},\quad
\boxed{g_i=M_i^TM_i=4I_3-\mathbf1_3\mathbf1_3^T.}
\]

The metric has eigenvalues `{1,4,4}`; it is positive definite. The Jacobian/volume form is

\[
\boxed{dV=4\,dt_1dt_2dt_3.}
\]

When two sectors share a face, both parameterizations produce the same physical coordinates and hence the same restricted Euclidean metric. The chart label is not a new physical degree of freedom.

**Typed relation to `4/3`:** Rescale the tetrahedral generators to unit circumradius `n_i=v_i/√3`. Then

\[
\sum_{i=0}^{3}n_in_i^T=\frac43 I_3,\qquad
\boxed{d\ell^2=\frac43\sum_{i=0}^{3}(d\lambda_i)^2,\quad\sum_i d\lambda_i=0.}
\]

This is an EXACT geometric tight-frame identity, but **not** an automatic identification with the prior ledger's coframe dyad `F03`, nor with a physical `4/3` spacetime or dynamical coefficient.

## 4. EXACT — Restrict each infinite quadrant to a finite tetrahedral volume

For the finite parent tetrahedron `T=conv(v₀,…,v₃)`, define

\[
T_i=T\cap Q_i=\operatorname{conv}\bigl(O,F_i\bigr).
\]

With the conical coordinates from §3, the bounded region is exactly

\[
t_j\ge0,\qquad \sum_{j\ne i}t_j\le1.
\]

The four children have disjoint interiors and preserve the original outer boundary:

\[
\boxed{T=\bigcup_{i=0}^{3}T_i},\quad
\boxed{V(T)=\frac83},\quad
\boxed{V(T_i)=\frac{2}{3}=\frac14V(T)}.
\]

The oriented chain-level identity is

\[
\boxed{\partial\left(\sum_{i=0}^{3}(-1)^i[O,v_0,\ldots,\widehat{v_i},\ldots,v_3]\right)
=\partial[v_0,v_1,v_2,v_3].}
\]

All six internal triangular faces cancel pairwise; no volume hole or extra outer boundary is introduced.

The same barycentric 1→4 volume result holds for any **nondegenerate, nonregular** tetrahedron if `O` denotes its vertex barycenter, even though the angular sectors may have unequal solid angles. Hence local tetrahedral quadrants do not require globally tiling with congruent regular tetrahedra.

### A useful graph/filled-cell distinction

If the center `O` is promoted from a **derived geometric point** to an actual mesh vertex, the subdivision contains five vertices, ten edges, ten triangular faces and **four** filled tetrahedra (`f=(5,10,10,4)`). The graph is `K₅`, but the geometric complex remains **three-dimensional**. It is neither the five-tetrahedron shell of a four-simplex nor its filled four-dimensional interior.

## 5. EXACT energy accounting for a declared density; dynamics still OPEN

For any integrable scalar density `ε` on a measurable domain `D⊂R³`, the quadrant partition gives

\[
\boxed{\int_D\epsilon\,dV
=\sum_{i=0}^3\int_{D\cap Q_i}\epsilon\,dV.}
\]

This is countably additive volume integration; it does not assert a physical conservation law.

**Exact test:** Set `ε(x,y,z)=8+x+2y+3z`, strictly positive on the parent tetrahedron. Affine-simplex integration yields

\[
E(T)=\frac{64}{3},\qquad
(E(T_0),E(T_1),E(T_2),E(T_3))
=\left(\frac{13}{3},6,\frac{17}{3},\frac{16}{3}\right),
\]

\[
\boxed{\sum_{i=0}^3E(T_i)=\frac{64}{3}.}
\]

Equal-volume quadrants therefore **need not** carry equal energy when the density is anisotropic.

If a UD update eventually assigns per-quadrant source `S_i` and antisymmetric transfer current `J_{ij}=-J_{ji}`, a possible accounting contract is

\[
\dot E_i=S_i-\sum_{j\ne i}J_{ij}-F_i^{\mathrm{ext}},\qquad
\frac{d}{dt}\sum_iE_i=\sum_i S_i-\sum_iF_i^{\mathrm{ext}}.
\]

This is a conditional discrete balance **definition**, not a derived UD transport law. Source normalization, conversion of burden to physical energy, and physical time remain OPEN.

## 6. NO-GO — Four-way barycentric refinement alone is not fractal contraction

A central counterexample is essential. Starting from `T=conv(v₀,v₁,v₂,v₃)`, at each 1→4 split select the child retaining the fixed face `F₀=conv(v₁,v₂,v₃)`. Denote the selected child’s apex by `p_n` and the fixed face centroid by `c_F=(v₁+v₂+v₃)/3`.

\[
\boxed{p_n=c_F+4^{-n}(v_0-c_F)}.
\]

The nested child volumes decay as

\[
\boxed{\operatorname{Vol}(T_n)=4^{-n}\operatorname{Vol}(T_0),}
\]

but the entire original triangular face remains in every descendant. Its longest edge length stays `2√2`; since all descendants lie inside the original tetrahedron, the diameter remains exactly

\[
\boxed{\operatorname{diam}(T_n)=2\sqrt2\quad\forall n.}
\]

Consequently the 1→4 barycentric rule does **not** guarantee mesh-diameter contraction, shape regularity, or self-similar fractal dynamics. A true fractal or spatial-refinement theorem requires a separate, native contraction/selection rule. This no-go leaves intact the exact four-quadrant partition result.

## 7. Program implications and explicit gap gates

**EXACT mathematical representation:** Any local Euclidean 3D region can be described by tetrahedral quadrants about an interior tetrahedral point, and globally `R³` admits a four-sector conical atlas for the regular symmetric reference tetrahedron. Quadrants do not imply 4 spatial dimensions.

**CANDIDATE UD spatial grammar:** use `Q_i` as an S₄-related local sector/readout, attach compatible tetrahedral volumes through oriented triangular faces, and preserve an independent burden/current ledger. Allow nonregular cells so arbitrary 3D regions can be meshed.

**OPEN / GATED:** `Ω₀` has not selected the center, the tetrahedron's orientation, quadrant birth, refinement or gluing. The factor `4/3` is not a physical coupling. A single `R³` conical chart does not prove global manifold topology, local isotropy under dynamic transport, emergent Lorentzian signature, physical time, native energy conservation, or the physical reality of the four-sector partition.

**Next discriminating test:** derive or reject a native S₄-equivariant local quadrant-admission selector under the *same initial support and boundary conditions*, with degenerate/nonregular tetrahedron controls, a genuine current balance and observables that distinguish four-sector angular partition from conventional tetrahedral meshes and Cartesian octants.

## 8. Reproducibility

- Verification: `UD_TETRAHEDRAL_QUADRANTS_VERIFY_v0.8.py` (SymPy exact rational geometry and chain incidence), locally executed with **109** exact assertion groups plus exhaustive coverage of 125 rational lattice points and 7 nested counterexample levels.
- Visualization: `UD_TETRAHEDRAL_QUADRANTS_VISUAL_v0.8.py` produces `UD_TETRAHEDRAL_QUADRANTS_VISUAL_v0.8.png`; it is a schematic computed from the stated vertices.
- Result ledger: `UD_TETRAHEDRAL_QUADRANTS_RESULTS_v0.8.json`.
- Constructor verification is not independent review. Any repository capture requires an append-only manifest and separate event, plus review before a claim promotion. Physical promotion remains **0**.
