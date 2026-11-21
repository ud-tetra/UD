# UD Spherical Boundary–Information Inversion Audit v0.1

**Date:** 2026-11-19  
**Status:** `EXACT_CONDITIONAL` finite geometry and topology; `NO-GO_SCOPED` for unqualified inversion correspondence; `OPEN` UD information-to-physical bridge  
**Physical Promotion:** **0**. No empirical test, SI unit map, dynamical selection law, or physical sphere emergence is claimed.  
**Scope:** two authorized workloads: (1) formulate and test a sphere/information inversion square starting from the tetrahedral boundary; (2) independently compare with conventional simplicial duality and a geometrically realized dual tetrahedron.

## 1. Source and assumption register

1. **UD scope lock:** [`UD-SCOPE-001` §Locked scope rules](https://github.com/ud-tetra/UD/blob/cef84ca5c996ec21b67247c74ee85c2c6c5dd995/docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md). The filled 3-simplex is a selected mathematical carrier for observable 3D research; mathematical minimality is not physical uniqueness. The 15-chain-dimensional and 192-exposure-state counts are not spatial dimensions. The frozen bridge boundary is Physical Promotion = 0.
2. **Prior dual-complex audit:** [`UD-Physics experiments/k5-four-cell/README.md` v1.0](https://github.com/ud-tetra/UD-Physics/blob/03722496f5b00e8f3f01b2400e4015eb65fdebc4/experiments/k5-four-cell/README.md), source PR #13 (merged). In particular, the four-cell **3-ball** differs from the closed five-tetrahedron boundary **3-sphere** and filled 4-simplex; graph identity is not topology or metric identity. This audit studies the boundary of one **3-simplex**, a **2-sphere**, not either 3-sphere.
3. **Prior symmetry-selection control:** [`UD-Physics experiments/geometry-s4-selection/README.md`](https://github.com/ud-tetra/UD-Physics/blob/03722496f5b00e8f3f01b2400e4015eb65fdebc4/experiments/geometry-s4-selection/README.md), source PR #241 (merged). Distinguishes full `S4` symmetry from a distinguished-star mapping that only preserves `S3`; geometry and readout choices do not follow from graph connectivity.
4. **Historical conceptual candidate:** `KLEIN_BASIN_INVERSION_DYNAMICS_v0.1`, in historical `Burden Continuity Audit.txt` and the `MASTER_APPEARANCE_EQUATION_KLEIN_BASIN_INVOLUTION_INSERT_v0.1` notes. The notes propose an inversion/refunneling *grammar*, not a verified nonorientable topology, state-to-metric map, or dynamics. Only the **question** is inherited; all explicit inversion and projection maps in the present note are new model definitions.
5. **Mathematical sources:** elementary oriented simplicial boundary, combinatorial duality, Euclidean inversion and polar duality. They are background mathematics—not sourced UD dynamical laws. This report specifies and reproves the relevant finite instances.

**Target exposure:** this is an exploratory construction designed to investigate the proposed sphere/inverse relationship; it is not target-blind discovery or a confirmatory physical test. **Metric:** Euclidean dot product assumed only in §§5–6. **Time, energy and rates:** none. **Normalization:** unit circumradius for regular tetrahedron; dimensionless. **Orientation:** increasing vertex order `0<1<2<3`. **Coefficients:** integers, rationals and exact algebraic `sqrt(3)`; no fitted parameters. **Clock/modular arithmetic:** N/A because no evolution rule or cyclic register is claimed.

## 2. Typed finite carrier and exact boundary topology

Set `V={0,1,2,3}` and let `K=∂Δ³` be the boundary simplicial complex of the filled tetrahedron. Its real chain groups are

\[
C_2(K;\mathbb R)\xrightarrow{B_2}C_1(K;\mathbb R)\xrightarrow{B_1}C_0(K;\mathbb R),\qquad
\dim(C_0,C_1,C_2)=(4,6,4).
\]

The face bases are sorted lexicographically, with increasing orientations. `B1 B2=0` exactly and the oriented boundary of `0123`,

\[
[123]-[023]+[013]-[012],
\]

lies in `ker B2`. Direct exact rational row reduction gives `rank B1=rank B2=3`, and therefore

\[
\chi(K)=4-6+4=2,\quad (b_0,b_1,b_2)=(1,0,1),\quad |K|\cong S^2.
\]

This is the **boundary** of the filled simplex, not an independently derived round metric sphere. The 3-cell itself has `b2=0` when included in the chain complex; changing between solid and shell changes the typed object.

## 3. Exact combinatorial information dual—NOT a 2D metric Hodge star

For a `k`-simplex `σ⊂V`, define the complement `σᶜ=V\σ` and the **signed complement** map

\[
D_k:C_k(K;\mathbb R)\to C_{2-k}(K;\mathbb R),\qquad
D_k[\sigma]=\varepsilon(\sigma,\sigma^c)[\sigma^c],
\]

where `ε` is the sign of the permutation that lists `σ` in increasing order followed by `σᶜ` in increasing order. Thus a vertex maps to its opposite triangle, an edge to its opposite edge, and a face to its omitted vertex. This is a degree-reversing *simplicial complement* map; the induced dual CW-cell construction also reverses incidence. Do not identify `D` with the metric Hodge star on differential forms of `S²`.

The exact matrices satisfy

\[
\boxed{D_0B_1=-B_2^\mathsf TD_1,\qquad D_1B_2=B_1^\mathsf TD_2},
\]

\[
\boxed{D_1^2=I_6,\qquad D_2D_0=-I_4}.
\]

For a permutation `g∈S4` and the induced signed oriented simplex action `T_k(g)`, the full 24-group check gives

\[
\boxed{D_kT_k(g)=\operatorname{sgn}(g)T_{2-k}(g)D_k}\quad(k=0,1,2).
\]

**EXACT:** This is a **sign-twisted** `S4`-covariant duality, not an untwisted same-grade self-involution of the UD carrier. Orientation matters.

**Separate no-go:** A deterministic self-map of the four *bare vertices* that commutes with all `S4` permutations must be the identity. This is proved by noting the stabilizer of any vertex fixes no other vertex, then using transitivity; it was also checked against all 24 candidate permutations. A nontrivial symmetry-preserving inversion must therefore change the type/grade, enlarge the state with an orientation label, or supply distinguishing structure; there is no unique bare-vertex inverse hidden in the `S4` count.

## 4. Conventional dual-complex null control

The dual CW decomposition `K*` of the tetrahedral `S²` has

\[
(f_0^*,f_1^*,f_2^*)=(4,6,4),\qquad
(b_0^*,b_1^*,b_2^*)=(1,0,1).
\]

Dual vertices correspond to primal faces; dual edges cross primal edges; dual faces correspond to primal vertices. The same counts and incidence reversal follow from standard simplicial geometry **without UD burden, phase, `\Theta`, action, or event laws**. This is the required independent control.

The contrast with [`UD-Physics PR #13`](https://github.com/ud-tetra/UD-Physics/pull/13) is important: `∂Δ³ ≅ S²` is not `∂Δ⁴ ≅ S³`. The apparently similar graph or equal face counts do not identify those objects.

## 5. Three genuinely different inversions

### 5.1 Euclidean spherical inversion (ambient 3D)

With supplied radius `R>0` and Euclidean dot product, define for `x≠0`

\[
J_R(x)=\frac{R^2}{\|x\|^2}x.
\]

It is involutive and interchanges `\|x\|<R` with `\|x\|>R`. On the sphere itself it is pointwise the identity:

\[
\boxed{J_R|_{S_R^2}=\mathrm{id}}.
\]

At the center `x=0` it is undefined unless the ambient domain is suitably compactified. Therefore it is **not** a self-map of the entire filled tetrahedron or a nontrivial involution of its `S²` boundary.

### 5.2 Antipodal inversion on the sphere

`N(u)=-u` is a genuine nontrivial involution of `S²`, degree `−1`, and exchanges opposite spherical directions. **It is not `J_R`**. The quotient under `u~−u` is the real projective plane `RP²`, whose Euler characteristic is `1`; it is **not a Klein bottle** (Euler characteristic `0`). Hence neither antipodal identification nor spherical inversion by itself establishes a Klein-basin topology.

### 5.3 Primal-to-dual tetrahedron with explicit Euclidean realization

Place four vertices at

\[
v_0=\frac{(1,1,1)}{\sqrt3},\quad
v_1=\frac{(1,-1,-1)}{\sqrt3},\quad
v_2=\frac{(-1,1,-1)}{\sqrt3},\quad
v_3=\frac{(-1,-1,1)}{\sqrt3}.
\]

Then `\|v_i\|^2=1`, `v_i\cdot v_j=-1/3` for `i≠j`. Let `T=conv{v_i}`. Its opposite-face barycenters are exactly

\[
c_i=\frac13\sum_{j\ne i}v_j=-\frac13v_i.
\]

The face-center dual realization is the different tetrahedron `T*=−T/3`. Note that the affine map in the following paragraph maps *primal vertices to dual vertices* indexed by opposite primal faces, and extends over the triangulated surfaces. It is not identical to the degree-reversing chain map `D_k` in §3.

Define typed affine maps

\[
A: \partial T\to\partial T^*,\ A(x)=-\frac{x}{3},\qquad
B:\partial T^*\to\partial T,\ B(y)=-3y.
\]

Then `B∘A=id_{∂T}` and `A∘B=id_{∂T*}`. The pair defines an involution on the *disjoint union of the primal and dual carriers*, not on the bare primal boundary alone.

Both boundaries are star-shaped about the origin. Their Euclidean radial projections

\[
P_T(x)=\frac{x}{\|x\|},\qquad P_{T^*}(y)=\frac{y}{\|y\|}
\]

are homeomorphisms onto the common unit sphere, under the declared regular realization. For every `x∈∂T`,

\[
\boxed{P_{T^*}(A(x))=-P_T(x)=N(P_T(x)).}
\]

**EXACT / CONDITIONAL:** This is the desired *commuting diagram* with **antipodal**, not ambient spherical inversion. It assumes a specific Euclidean geometry and radial readout. All of its mathematics is reproduced by a conventional tetrahedron and its geometric dual; it is **not UD-specific**.

An additional exact correspondence: the polar dual of `T` (defined by `y·x≤1` for all `x∈T`) has vertices `−3v_i`. Under unit-sphere inversion, `J_1(c_i)=−3v_i`, taking the opposite face centers to the polar vertices. This equality needs the chosen metric and unit-radius normalization. It does not imply an evolution law or hidden information register.

## 6. Commuting-square no-go and counterexamples

**Theorem A (injective boundary projection obstruction).** Let `X` be a finite or continuous candidate information state space, let `P:X→S_R²` be injective, and let `I:X→X` be an involution. If `P∘I=J_R∘P`, then `I=id_X`.

*Proof:* Since `J_R` acts identically on `S_R²`, `P(Ix)=P(x)` for every x. Injectivity of P gives `Ix=x`. QED. This requires no UD dynamics and is valid on the declared domain.

**Theorem B (hidden-fiber null).** When `P` is not injective, a nontrivial involution can permute states entirely within its fibers while obeying the same commuting relation. For example take `X=∂T×{±1}`, `I(x,ε)=(x,−ε)` and `P(x,ε)=P_T(x)`. Then `P∘I=P=J_1∘P`, yet the inversion is **invisible to P**. Thus a commuting relation with ambient sphere inversion alone yields no distinguishing physical measurement.

**Counterexample C (do not swap inversions).** For the primal-dual construction, at an original vertex `v_i`,

\[
P_{T^*}(A(v_i))=-v_i\ne v_i=J_1(P_T(v_i)).
\]

The equation proposed with `J_1` fails; the corrected equation with `N` passes. On the straight edge midpoint `m=(v_0+v_1)/2`, `\|m\|^2=1/3` and `J_1(m)=3m`, which lies **outside** `T`. Hence ambient inversion does not preserve the straight triangulated boundary even though it fixes the round sphere.

**Topological contrast:** `S²/±=RP²`, not a Klein bottle. A nonorientable Klein-type gluing would require an additional, specifically declared identification and proof of its topology; it is not supplied by `S4`, the tetrahedral shell, or the map `A`.

## 7. What a UD-specific bridge would have to produce

1. **State:** an information-side carrier (for instance a typed function of the chain degrees, `S4×Θ` fiber and any supported seam/receipt history), not a relabeling of Euclidean points by fiat.
2. **Operator:** a sourced, admissible, orientation-sensitive map `I_UD` on that carrier; state its domain/codomain, involution or other composition law, symmetry action, and whether it crosses between primal and dual complexes.
3. **Projection:** a *derived* geometry/readout map `P_UD` and the metric/normalization it uses. The present `P_T` was supplied, so this step is open.
4. **Dynamics:** the event generator or transition kernel, initial/boundary conditions, support and work receipts, and any gauge-dressing needed. Present maps are kinematic, not temporal.
5. **Discriminant:** a target-blind prediction distinguishing the proposed internal inversion from (i) plain simplicial duality, (ii) an ordinary tetrahedral polar dual, (iii) an unobservable hidden sign, and (iv) a boundary-condition selection. Candidate readouts could include an orientation-resolved transport/receipt contrast alongside a spherical geometric image, provided the observable and its units are declared and sourced.
6. **Physical promotion:** only after a calibrated map to a measured quantity with uncertainty, baseline/null, independent held-out evidence and explicit acceptance criterion; Physical Promotion remains 0.

**No inference is licensed from the equal number `4` of primal vertices and dual faces, the equal f-vector `(4,6,4)`, or the antipodal map to physical matter, a photon, a black hole, a spacetime dimension, or a Klein-bottle topology.**

## 8. Verification and independent supporting workload

- `verify.py`: generated oriented incidence and ranks, exact complement-duality identities, 24 signed `S4` actions across three grades (72 checks), exhaustive centralizer test, exact regular-tetra dot products, polar vertices, inversion and primal-dual antipodal identities on sixteen test points. All PASS.
- `replay_stdlib.py`: separately implemented standard-library Fraction elimination, generated face incidence and sign-twisted group actions, algebraic coordinate comparisons without SymPy and sixteen paired probes. All PASS. Independent *implementation*, not an independent non-constructor review.
- `results.json` and `replay_results.json`: exact result receipts; logs record execution. `MANIFEST.json`: SHA-256 and byte sizes of frozen files.
- Repository integration tests, fresh-checkout verification, CI status and non-constructor peer review are reported only if actually executed. Any new PR must remain draft until properly reviewed.

## 9. Conclusion and status

**AUTO_LOCK recommended for narrowly scoped mathematics only:** `∂Δ³` is an `S²` shell; the signed complement identifies opposite simplices under an orientation twist; a regular tetrahedron's geometric dual projects antipodally under an **assumed** Euclidean radial readout; on the round sphere ambient inversion is the identity. These are standard mathematical identities, not native UD constitutive laws.

**NO-GO_SCOPED:** Injective sphere-boundary readout plus ambient sphere inversion admits only the identity information involution. Non-injective hidden flips are observationally invisible at that readout. The candidate primal-dual geometry requires an antipodal—not spherical inversion—commuting square.

**OPEN_GATED:** Derived UD information duality, projection to physical spherical geometry, a source-selected event rule, discriminating readout, independent physical measurement. No claim ledger or canonical physical result is changed, and **Physical Promotion = 0**.
