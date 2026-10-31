# UD PRED-01 — Local K4 defect selector and bounded distributed source, v0.4

**Date:** 2026-10-31  
**Lane:** D0 DEVELOPMENT / P0 CANDIDATE; non-constructor review deferred.  
**Claims:** EXACT_CONDITIONAL topology and bounded-work theorem; NUMERICAL finite realizations and relaxation; NO-GO within specified premises; physical promotion **0**.

## 1. Authority, sources and what is being added

Authoritative antecedents inspected: `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md` Part A (§§A.1–A.5; source blob `c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b`), `docs/UD_PACKET_v1.1_ERRATA.md` E.1–E.2 (`6961b917f4f1ca470127aa0b7d3c1b59693f4373`), `docs/UD_EXTERNAL_REVIEW_BRIEF.md` (`c1ec2adc2e257e06d9681d1a13c6e11b15b7d750`), and v0.3 K4-decorated annulus paper in open UD PR #477 (head `43e198eaf95da5fe2f1a8ec5a4b5c8a87d1ca571`). `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` remains a proposal; program governance PR #473 was not assumed merged.

The v0.3 annulus was inserted in the initial carrier. Here the *initial complex is a full simplicial 3-ball*, and topology changes under an explicitly declared **local defect-excision operation**. This removes the particular pre-inserted-annulus assumption but does **not** derive a unique selector or constitutive action from K4 parity alone.

## 2. Typed finite carrier, state, update and boundary

For even integer grid resolution \(N\ge4\), let \(Q_N\) be a closed square disk triangulated by the diagonal of each unit square. Extrude to the interval \([0,2]\) in two slabs, decomposing each triangular prism into three tetrahedra in a globally consistent vertex order. The initial K4-packet complex is

\[
 X_N^{\rm full}=Q_N\times[0,2],\quad |K_3|=12N^2,
 \quad H_i(X_N^{\rm full};\mathbb Z)=\begin{cases}\mathbb Z&i=0\\0&i>0.\end{cases}
\]

**Assumptions L1–L4 (new source mechanism):**

- **L1:** An externally initialized, conserved unit token \(b\in\{0,1\}\) occupies one interior bottom-boundary vertex; a trail-memory mark is separately writable. Neither localization nor the distinguished \(+z\) contact is derived from K4 packet symmetry.
- **L2:** A deterministic nearest-neighbor transfer \(b(v)=1\to b(v')=1\) advances along a declared \(+z\) edge. Each transfer preserves \(\sum b=1\) and marks the visited vertex. Two transfers produce the boundary-to-boundary path \(\Gamma\) through three layers; transfers are **algorithmic events**, not seconds.
- **L3:** Locally suppress all filled K4 tetrahedra incident to a trail vertex. Remove unsupported faces/edges and retain all faces of the surviving tetrahedra. This *pruning of unsupported subfaces* is part of the assumed rule, not automatic in a simplicial subcomplex. Retain the trail-memory mark in the separate source state; it is not identified with an extant vertex after excision.
- **L4:** Winding is represented by a lifted real 1-cochain with integral period; the \(\mathbb Z_2^3\) packet parity fiber alone has not been proved to select this integer lift or the excision trigger.

**Boundary conditions:** finite square boundary and the two slab endcaps; the defect path intersects both endcaps and remains otherwise interior. The intact disk mesh has no tunnel. At full trail completion the tetrahedron/face incidence agrees with \((Q_N\setminus\operatorname{ost}(v_\star))\times[0,2]\), triangulated by tetrahedra, where \(\operatorname{ost}\) is the open planar star of the selected interior base vertex. The source creates the tunnel by changing cell occupancy; there was no annular spatial domain before the update.

### Theorem 1 — Integer winding support is conditionally generated

The base complex after excision is a triangulated disk with one central polygonal hole. It deformation retracts to \(S^1\). Product with an interval does not change homotopy type, so

\[
 H_0(X_N^{\rm cut};\mathbb Z)\cong\mathbb Z,\quad
 H_1(X_N^{\rm cut};\mathbb Z)\cong\mathbb Z,\quad H_i=0\;(i\ge2).
\]

This is an **EXACT_CONDITIONAL** topological statement; the finite computation also verified \(\partial_1\partial_2=0\), \(\partial_2\partial_3=0\), and the Betti numbers over \(\mathbb F_2\) independently at \(N=4,6,8\). Over \(\mathbb Z\), the product/deformation-retraction proof excludes hidden torsion; equality of mod-2 ranks alone would not.

| N | Full K4 tetrahedra | Selected K4 tetrahedra | \(\beta_1\) before → after | Defect source transfers |
|---:|---:|---:|---:|---:|
| 4 | 192 | 156 | 0 → 1 | 2 |
| 6 | 432 | 396 | 0 → 1 | 2 |
| 8 | 768 | 732 | 0 → 1 | 2 |

An independent check enumerates the planar disk Euler characteristic changing from \(1\) to \(0\), with exactly six source-adjacent planar triangles excluded. No observed physical core, tear or boundary migration is claimed.

## 2.1 Candidate parity/transport trigger and its exact obstruction

The conserved token in L1 is not automatically the UD opposite-edge parity fiber. A more native-looking **CANDIDATE**, not used to claim that the finite test mesh was selected autonomously, is to equip each face-adjacent K4 pair with an explicitly typed \(\mathbb Z_2\) transport sign \(U_{tt'}\). For a closed dual packet-link cycle \(C_e\) around an interior edge, define

\[
H_e:=\prod_{(t,t')\in C_e}U_{tt'}\in\{+1,-1\}.
\]

If local frame changes act by \(U_{tt'}\mapsto g_t U_{tt'}g_{t'}\), the product is gauge-invariant because each internal \(g_t\) occurs twice. A *proposed* trigger is \(H_e=-1\) together with a positive, source-retained burden stock threshold and a direction/contact rule. This is an admissible way to pose a local gate, **but neither \(U\), the stock threshold nor the direction rule is uniquely imported from the frozen K4 fiber here**. Boundary-spanning propagation and excision remain a separate assumption.

**EXACT NO-GO for a trivial transport:** if \(U_{tt'}=g_tg_{t'}\) on every neighbor link (a pure-gauge sign), \(H_e=+1\) on every closed dual cycle. Merely assigning local tetrahedral \(\mathbb Z_2^3\) labels without a nonflat transport/frustration rule cannot produce this selector. Further, even a nontrivial \(\mathbb Z_2\) holonomy specifies only parity and does not supply the integral winding lift needed to distinguish arbitrarily many integer \(n\) sectors. These are explicit **OPEN_GATED** native-interface dependencies, not an implicit permission to insert them by notation.

## 3. Winding states and a local harmonic-construction algorithm

Let \(B_1: C_1\to C_0\) and \(B_2:C_2\to C_1\) be signed simplicial boundaries, with Euclidean unit-edge inner product. An exact integer cocycle \(z\in C^1(X_N^{\rm cut};\mathbb Z)\) was constructed by angular-branch crossing of the planar defect, giving \(B_2^{\mathsf T}z=0\) and \(\oint_\gamma z=1\). Its support comprises 15, 25 and 35 oriented edges at the tested resolutions.

The unique harmonic representative with that period and this metric is

\[
 h=z-B_1^{\mathsf T}\phi_\star,\qquad
 B_1B_1^{\mathsf T}\phi_\star=B_1z,
 \qquad B_1h=B_2^{\mathsf T}h=0.
\]

For every integer \(n\), \(a_n=nh\) is a mathematically available fixed-sector state; in particular \(n=2,3\) exist in the constructed cochain model. With quadratic action \(S_{\lambda_N}(a)=\lambda_N\|a\|^2/2\), \(a_n\) uniquely minimizes the action in its cohomology class. It does not prove matter persistence in the native §7.13 sense.

**Local solver:** the update \(\phi_{r+1}=\phi_r+\eta\big(B_1z-B_1B_1^{\mathsf T}\phi_r\big)\) reads only adjacent vertices/edges. With \(\eta=1/(2d_{\max})=1/28\) and a fixed gauge, it converges to \(\phi_\star\) on a connected mesh. Its inputs still require the selected integer cut \(z\); computing the cut and choosing the starting seed are open native gates. At 2,500 iterations, numerical divergence residuals were at most \(1.82\times10^{-9}\) for the three tested sizes. Neither an iteration nor a local transfer is calibrated physical time.

## 4. Refinement theorem: what changes the original obstruction

The v0.3 no-go proved that a **fixed three-edge, unit-slip cut** cannot provide *both* a nonzero finite retained gap and bounded injected work while refining the earlier annulus with the declared stiffness scaling. That result remains valid **under those hypotheses**.

**New assumptions R1–R4:** Permit all nonzero edges of \(h\) to receive a local staged increment, permit temporary nonzero \(B_2^{\mathsf T}a\), use a positive curvature penalty, and *choose* \(\lambda_N\) by unit-gap calibration (an inverse normalization, **not** derived native coefficient):

\[
 \mathcal A_N(a)=\frac{\lambda_N}{2}\|a\|^2+\frac{\mu_N}{2}\|B_2^{\mathsf T}a\|^2,
 \quad \mu_N=\lambda_N,
 \quad \lambda_N\|h\|^2=\frac25.
\]

For \(n=2\to3\), the retained difference between flat harmonic endpoints is
\[
 \varepsilon_2^{\rm retain}=\mathcal A_N(3h)-\mathcal A_N(2h)
 =\frac52\lambda_N\|h\|^2=1.
\]

Update **one edge at a time**, by adding its \(h_e\) component, using a locally traversable front. The endpoint again has zero curvature. Intermediate states are usually **not closed** and therefore are not claimed to remain in a fixed cohomology sector. Let \(W_N^+=\sum_t\max\{\mathcal A_N(a_{t+1})-\mathcal A_N(a_t),0\}\) count **all positive action input** including temporary curvature. By a triangle inequality for each face, with maximum number \(d_F\) of triangle incidences per edge,

\[
 W_N^+\le \varepsilon_2^{\rm retain}
 +\mu_N\sum_{f}\Big(\sum_{e\subset\partial f}|h_e|\Big)^2
 \le1+3\mu_Nd_F\|h\|^2.
\]

Here \(d_F\le6\) on the constructed meshes. Thus, **EXACT_CONDITIONAL**,

\[
 \boxed{W_N^+\le 1+3\cdot6\cdot\frac25=\frac{41}{5}}.
\]

The proven upper bound is uniform in \(N\) for this family and normalization. The total **number** of sequential edge updates grows with the mesh: 298, 666 and 1,170. It is not bounded physical duration or power. This is a mathematically valid **new branch** under distributed support, intermediate curvature, and calibrated \(\lambda_N\), not a refutation of the previous fixed-support no-go.

Numerical source receipts:

| N | \(\|h\|^2\) | Gross fixed-cut work (retained gap = 1) | Staged positive injected work | Universal upper bound |
|---:|---:|---:|---:|---:|
| 4 | 1.5795034477 | 2.6993310869 | 1.0000996098 | 8.2 |
| 6 | 2.0170151434 | 3.2789104912 | 1.0008246847 | 8.2 |
| 8 | 2.3335419204 | 3.7997318406 | 1.0013816221 | 8.2 |

**Additional scoped no-go:** No nonzero *single-edge* update of these meshes can preserve \(B_2^{\mathsf T}a=0\) at every intermediate step because each edge belongs to at least one triangular face. A local sequential transport path needs temporary curvature, extra simultaneous compensating updates, or a changed rule. Merely keeping all states flat is not an available shortcut under this one-edge contract.

## 5. Source-action scope and zero-promotion decision

- The purely quadratic action yields \(\varepsilon_k=\lambda_N\|h\|^2(2k+1)/2\), hence \(R_B=3\) and \(D_2=0\) even when winding topology is present. **A generated tunnel does not itself derive WBX1 autocatalysis.** A nonquadratic or stock-dependent law is an *additional* candidate, to be compared with PLB1 leakage and quartic alternatives.
- The integer lift \(\oint a=n\) is a selected state variable; \(e^{2\pi i n}=1\) for all integer sectors. A Wilson-loop measurement alone cannot identify \(n=2\) or \(n=3\). A \(\mathbb Z_2\) loop readout cannot resolve general integer winding either.
- **Symmetry obstruction:** On a transitive homogeneous packet graph, no deterministic automorphism-equivariant rule with fully invariant initial data can select exactly one defect among equivalent sites. A localized burden seed, boundary asymmetry, stochastic transition or other symmetry-breaking source is essential. Our seed and \(+z\) contact are admitted input data, **not** a native selection derivation.
- Removing occupied cells changes the complex; to maintain a topological defect, an actual restoration prohibition or burden-memory dynamics must be supplied. Reloading the original K4 cells restores \(H_1=0\).
- Source sign, orientation, SI energy, instrument, noise covariance, radiative losses and calibrated physical clock remain **OPEN_GATED**. Non-constructor review **DEFERRED**, not waived.

## 6. Next source-bound gate

Derive or experimentally constrain the local burden/parity trigger and winding lift from the UD source connection and packet readiness equations. Then check whether this selector survives K4 face moves, nuisance dynamics and finite boundary perturbations. A future *confirmatory* bridge must also specify what apparatus measures the retained action, positive injected work, integer winding or a leakage proxy, and how it calibrates the native dimensionless values.
