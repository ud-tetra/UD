# UD-PM-PRED04-TOPO-001 v1.0 — Conditional K4 star-column excision and integral winding

**Proof kind:** THEOREM + scoped bistellar-move NO-GO  
**Evidence:** EXACT_CONDITIONAL, independent finite-chain corroboration  
**Review:** DEFERRED — author-side independent rederivation, not independent peer review  
**Physical promotion:** 0  
**Source audited:** `ud-tetra/UD`, PR #479, head `b5c8146ae4b956279e6f399553e02cffbc42c7ea`; `docs/UD_PRED01_LOCAL_DEFECT_SELECTION_AND_BOUNDED_SOURCE_v0.4.md`, §§2–3, 5 (Git blob `abefbc821bd7897e9c469b2ff12bd7cccab56c99`).

## A. Typed objects and assumptions

Let `N` be an even integer at least 4. Let `Q_N` be the square disk `[0,N]^2` triangulated by the same southwest-to-northeast diagonal in every unit square. Set `I=[0,2]`, with vertex levels `z=0,1,2`. Let `X_N` be the Freudenthal tetrahedralization of `Q_N × I`: each cube is subdivided into six tetrahedra, each with four vertices and six edges (`K4` as a simplicial 3-cell). Coefficients for the main homology assertion are the **integers**; mod-2 boundary matrices are auxiliary finite checks. No physical metric, clock or energy is required.

Choose the interior planar vertex `v=(N/2,N/2)`. **New stipulated rule EX:** mark the three vertices `(v,z)` for `z=0,1,2`, remove every 3-simplex containing at least one marked vertex, then retain *only* the subfaces supported by remaining 3-simplices. This is a topology-changing occupancy rule; the mark's generation, choice of `v`, preferred vertical direction and restoration prohibition are *not derived* from the native UD action.

## B. Theorem and proof

**Theorem T:** The intact realization `|X_N|` is a 3-ball and the fully excised realization `|X_N^{EX}|` deformation retracts to `S^1`. Consequently

\[
H_i(X_N;\mathbb Z)\cong\begin{cases}\mathbb Z&i=0\\0&i>0,\end{cases}
\quad
H_i(X_N^{EX};\mathbb Z)\cong\begin{cases}\mathbb Z&i=0,1\\0&i\ge 2.\end{cases}
\]

*Proof.* `Q_N` is a disk, and the stated tetrahedralization is a compatible subdivision of `Q_N×I`, so `|X_N|` is a 3-ball. In the planar grid, the interior vertex `v` has exactly six incident triangles; their closed star is a planar disk whose link is a simple six-edge cycle. Removing the triangles containing `v` and pruning unsupported subfaces leaves the square disk with a polygonal inner boundary: an annulus `A_N`.

Every tetrahedron in the prism over a base triangle containing `v` contains the bottom or top copy of `v` in its slab, and no tetrahedron over another triangle contains a marked vertex. Thus EX removes precisely the tetrahedra over `star(v)×I`, and the surviving subdivision has geometric realization `A_N×I`. Because `A_N` deformation retracts to its inner circle and `I` is contractible, `A_N×I` deformation retracts to `S^1`. This proves the stated **integral** homology, including the absence of torsion. ∎

**Exact combinatorial check:** For the declared two-slab triangulation,

\[
(V,E,F,T)_{\mathrm{full}}=(3(N+1)^2,\ 17N^2+14N+2,\ 26N^2+8N,\ 12N^2),
\]

and EX deletes `(ΔV,ΔE,ΔF,ΔT)=(3,32,66,36)`; hence `χ_full=1` and `χ_EX=0`. The integer homology theorem follows from the geometric proof, **not** from the Euler characteristic alone. An independently coded Freudenthal construction and full mod-2 boundary-rank calculation at `N=4,6,8` returned `(β_0,β_1,β_2,β_3)=(1,0,0,0)` before and `(1,1,0,0)` after excision, with both consecutive boundary compositions equal to zero.

## C. Legal face moves and a precise no-go

**Corollary (NO-GO, scoped):** No finite sequence of legal topology-preserving simplicial bistellar moves, including interior `2↔3` Pachner moves, can change the intact ball's first integral homology from `0` to `Z`. Such moves preserve the PL-homeomorphism type. The topology change in T is supplied by **EX**, not by ordinary face moves.

Conversely, legal bistellar moves *after* excision preserve `H_1≅Z`, but they do **not** automatically preserve a particular harmonic cochain, preferred vertex selector, local action, numerical energy or the permanence of the removed defect. The transport and constitutive laws for those quantities remain OPEN.

A separate exact finite 2→3 replacement of two tetrahedra about an interior face by three about the new edge preserved the full mod-2 Betti vector on both the original and the cut `N=4` complexes. This is a test witness, not the general topological proof.

## D. Counterexamples, degeneracies and native-selection gaps

- **Not every local defect creates winding.** At `N=4,6,8`, excision of just the single bottom-boundary seed vertex (with the same pruning rule) leaves `H_1(-;F_2)=0`, so cannot have `H_1(-;Z)≅Z`. A boundary-spanning or otherwise nontrivial geometric removal is essential.
- **Not a native selected defect.** The initial seed, `+z` contact and EX are independently stipulated. An automorphism-equivariant deterministic rule with fully symmetric data cannot choose one vertex from a transitive `K4` vertex orbit: equivariance would require a vertex fixed by all of `S4`, which does not exist.
- **Pure-gauge obstruction.** If every `Z_2` transport link is `U_{tt'}=g_t g_{t'}`, closed dual holonomy products are `+1`; a proposed `H=-1` selector does not activate. A `Z_2` phase also does not, by itself, specify arbitrary integer winding `n`.
- **Not persistence.** Re-inserting the removed tetrahedra returns the intact 3-ball and trivializes `H_1`; an actual restoration prohibition or burden memory rule is required for dynamical persistence.
- **Not metric invariance.** A triangulation change can preserve integral homology without preserving an edgewise Euclidean norm or a chosen harmonic representative.

## E. Verification, status and dependencies

Independent source-free executable: `independent_topology_work_audit.py`; output `INDEPENDENT_AUDIT.json`. The program derives its tetrahedra from six monotone coordinate permutations per cube rather than importing the antecedent source. It verifies boundary composition, ranks, exact simplex counts, legal face-move examples, and partial-defect counterexamples. The integral result is proved above, not inferred from mod-2 ranks.

**Proof status:** `VERIFIED_SCOPED / EXACT_CONDITIONAL`, review deferred. **Physical promotion:** 0. **Next gate:** derive the seed, preferred local transport/excision event and restoration constraint from admitted native packet variables, with a well-posed generator and surviving-graph rule.
