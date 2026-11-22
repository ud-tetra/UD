# UD Whitney Matching-Coframe and Signed-Dual S4 Audit — v0.1

**Executed:** 2026-11-20 UTC. **Research mode:** exact mathematical development; two authorized workloads.  
**Status:** `EXACT_CONDITIONAL` rank/orbit/duality statements; `NO-GO_SCOPED` native magnitude-only selection and direct Hodge identification; `OPEN_CONSTITUTIVE_SOURCE` geometry/dynamics.  
**Physical Promotion = 0.** Nothing here reconstructs a measured sphere, a physical metric, a spacetime coframe, matter, or gravity.

## 1. Sources, scope, and typed provenance

- **Governance:** UD `AGENTS.md`, `CONTRIBUTING.md`, `docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md`, pinned UD `main` `cef84ca5c996ec21b67247c74ee85c2c6c5dd995` (UD-SCOPE-001, November 11, 2026, locked research scope). No physical carrier uniqueness claimed.
- **Immediate predecessor:** [UD PR #578](https://github.com/ud-tetra/UD/pull/578), captured v0.1 `REPORT.md` §2–6 at `captures/2026-11-20T031100Z-chatgpt-sphere-inversion-6b72/REPORT.md`, pinned commit `fc86bd07e6da88ece4125fda6cba95f975c8c636`; and [UD-Physics PR #454](https://github.com/ud-tetra/UD-Physics/pull/454), head `8d298d8353f95fd951e0da69b93fd06700a08b72`. These PRs are draft/unmerged research snapshots, **not automatically accepted canon**.
- **UD source transport and support:** manuscript `TETRAHEDRAL_PACKET_COMPLEXES_JOP_LEAN_MANUSCRIPT_v2.5_POC1_LAB_IMPLEMENTATION_READY.md`, §§2.2, 3.1–3.3, 4.1 and 4.5, Library file `libfile_eb315486c110819199861a466b40fc3c`. §4.5 explicitly defines pre-gate latent support `Λ_e^S=2|c_{1,e}|(|c_{0,i}|+|c_{0,j}|)` and `ω_p^lat=T_p 1[Λ_p^pair>0]`; POC-1 is a **candidate constitutive hypothesis**. The historical algebraic source is not an operational event generator.
- **Source-direction constraint:** `EDGE_STRAIN_TO_SUPPORT_AMPLITUDE_CONSTITUTIVE_SOURCE_AUDIT_v0.1.md`, §§2–4, 8–9, Library `libfile_2ee214edca088191a0456621df881b4a`; support-to-parent-shape is defined but reverse strain-to-support constitutive law remains absent. Do not insert stiffness or phase sign rules by analogy.
- **Independent ordinary-mathematics nulls:** merged [UD-Physics PR #13](https://github.com/ud-tetra/UD-Physics/pull/13), `experiments/k5-four-cell/README.md` v1.0, and merged [UD-Physics PR #241](https://github.com/ud-tetra/UD-Physics/pull/241), `experiments/geometry-s4-selection/README.md`, both pinned UD-Physics main `03722496f5b00e8f3f01b2400e4015eb65fdebc4`. Graph identity does not fix topology, metric or projection selection.

**Question 1:** Which signed Whitney matching triads are rank-three at the barycenter, and which make a globally nondegenerate interior coframe? Classify all 64 binary sign assignments under the complete signed `S4` action. Determine whether recovered source receipts select a class.

**Question 2:** Compare the Whitney construction and its covariance to PR #578's **signed complementary simplex map** `D1`; test whether it can be identified with a metric Hodge star or whether an ordinary simplicial/Euclidean null explains the result.

**Coefficient domain** `Q` for tested finite maps; `R` for arbitrary amplitude theorem and smooth affine interpolation. **Geometry:** a *supplied* reference affine tetrahedron with barycentric coordinates and dimensionless Euclidean chart. **Time:** no dynamical update; the spatial coordinates are *not* model event time. **Units:** dimensionless only. **Orientation:** vertex order `0<1<2<3`, every simplex oriented increasingly. **Target exposure:** hypothesis-led mathematical exploration; no empirical measurement or fitted parameter. The binary alphabet `{−1,+1}` is a **test preparation**, not a source-derived UD admissible sign law.

## 2. Exact construction

Let `K=Δ³` include its filled top cell and let `C¹(K;R)=R⁶` use the ordered edge basis

`(01,02,03,12,13,23)`.

On the reference tetrahedral interior define

\[
(\lambda_0,\lambda_1,\lambda_2,\lambda_3)=(1-x-y-z,x,y,z),\qquad \lambda_i\ge0,\quad\sum_i\lambda_i=1.
\]

A Whitney edge form is

\[
W_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i.
\]

Three opposite-edge matchings are `M1=(01,23)`, `M2=(02,13)`, `M3=(03,12)`. For real edge cochain `c` define **candidate** Whitney forms and row-coefficient matrix

\[
e^a(c)=\sum_{ij\in M_a}c_{ij}W_{ij},\qquad E_c(x)\in \operatorname{Mat}_{3\times3}(\mathbb R),\quad e^a=\sum_{\alpha=x,y,z}E_{a\alpha}(x)\,dx^\alpha.
\]

The word *coframe* is justified only where `det E_c(x)≠0`. The matrix `g_c=E_c^T E_c` is a **conditional dimensionless Gram metric under the supplied chart and Euclidean pairing**, not a UD-recovered physical metric. On the boundary surface `∂Δ³≅S²`, a tangent coframe has rank at most two; the rank-three claim is strictly for the **filled three-dimensional interior**.

Let `T1(g)` be the *signed* action on oriented edge coordinates for `g∈S4`; let `R(g)` be the induced permutation of the three matchings; and `Φ_g` the affine vertex permutation with Jacobian `J_g`. A direct Whitney calculation gives

\[
\boxed{E_{T_1(g)c}(\Phi_g x)=R(g)E_c(x)J_g^{-1}.}
\]

This is an **exact typed affine covariance**, not geometric metric emergence. Since `det R(g)=det J_g=sgn(g)`, `det E` is `S4`-invariant when the cochain is correctly transported. The induced conditional Gram metric transforms covariantly by `J_g^{-T}g_cJ_g^{-1}`. Verified for all 24 permutations, including off-center rational coordinates and an arbitrary unequal-amplitude cochain.

## 3. Binary sign classification across complete S4

Restrict **for this calculation only** to `c∈{−1,+1}⁶`. At the barycenter `λ_i=1/4`, exhaustive exact rank and orbit enumeration gives:

| Representative `c` in `(01,02,03,12,13,23)` order | Orbit size | Rank at barycenter | Barycenter determinant |
|---|---:|---:|---:|
| `(-1,-1,-1,-1,-1,-1)` | 24 | 2 | 0 |
| `(-1,-1,+1,-1,-1,-1)` | 24 | 2 | 0 |
| `(-1,-1,-1,-1,+1,-1)` | 8 | 3 | `−1/4` |
| `(-1,-1,+1,-1,-1,+1)` | 8 | 3 | `+1/4` |

**EXACT:** `48` sign assignments are rank-deficient at the barycenter, while exactly `16` are rank-three there. The latter are *globally nondegenerate* on the filled tetrahedron (proof next). These four orbits exhaust `24+24+8+8=64`; counting representatives or swapping orientations without the signed action gives the wrong classification.

Equivalently, for these binary sign vectors,

\[
\boxed{\operatorname{rank}E_c(\lambda_*)=3\quad\Longleftrightarrow\quad c_{01}c_{23}=c_{03}c_{12}=-c_{02}c_{13}=\pm1.}
\]

## 4. Signed dual eigensector theorem — main new result

From the preceding [sphere audit PR #578](https://github.com/ud-tetra/UD/pull/578) §3, the *metric-free* signed complement map is

\[
D_1[e]=\varepsilon(e,e^c)[e^c]\colon C_1(\partial\Delta^3;\mathbb R)\to C_1(\partial\Delta^3;\mathbb R).
\]

In the ordered edge basis `D1` swaps `01↔23` with sign `+`, `02↔13` with sign `−`, and `03↔12` with sign `+`. It satisfies exactly

\[
D_1^2=I_6,\qquad\boxed{D_1T_1(g)=\operatorname{sgn}(g)T_1(g)D_1},\qquad g\in S_4.
\]

**THEOREM (EXACT / CONDITIONAL):** Choose either sign `ε=±1`, and take a real cochain in its eigenspace `D1 c=ε c`. Write `a=c01`, `b=c02`, `d=c03`. Necessarily

\[
c_{23}=\varepsilon a,\qquad c_{13}=-\varepsilon b,\qquad c_{12}=\varepsilon d.
\]

Then, *identically throughout the affine tetrahedron*,

\[
\boxed{\det E_c(x)=abd\left(\lambda_0^2+\lambda_1^2+\lambda_2^2+\lambda_3^2\right).}
\]

Because `(Σλ_i)²≤4Σλ_i²` and `Σλ_i=1`,

\[
\sum_i\lambda_i^2\ge\frac14,
\]

with equality at the barycenter. Thus `abd≠0` is **necessary and sufficient for a globally rank-three Whitney matching triad within the declared eigensector**. For `c∈{±1}⁶`, the eigensector condition is additionally necessary for barycenter rank three, hence exactly explains the `16` sign states.

**Scope caution:** `D1 c=±c` is not *necessary* for global nondegeneracy among unrestricted real cochains. Starting from `(c01,c02,c03,c12,c13,c23)=(1,1,1,1,-1,1)`, change only `c13` to `−9/10`. This new cochain is in neither `D1` eigenspace, but

\[
\det E_c=\sum_i\lambda_i^2-\frac1{10}(x^2+z^2)\ge\frac9{10}\sum_i\lambda_i^2\ge\frac9{40}>0.
\]

That explicit counterexample prevents an unwarranted universal selector claim.

**Symmetry obstruction:** The `+` and `−` duality eigenspaces are exchanged by each odd vertex permutation. Consequently neither *fixed* eigensector is independently stable under the full signed `S4` action. The **union** is invariant. A fully `S4`-fixed oriented edge 1-cochain must be zero: swapping the endpoints of any edge reverses that edge and forces its coefficient to equal its negative. A nonzero coframe needs sign/orientation information in the preparation, a covariant frame-valued law, or a source-induced symmetry-breaking mechanism. Merely enumerating `S4×Θ` does not provide one.

## 5. Source-admission gate: support and seam do not yet select a coframe

Take `c0,i=1` at all four vertices, six edge magnitudes `|c1,e|=1`, and all hard integrity gates `T_e=1` (the latter are supplied test controls, not sourced dynamics). For all `64` sign assignments,

\[
\nu_e=c_{1,e}^2=1,\qquad \Lambda_e^S=2|c_{1,e}|(|c_{0,i}|+|c_{0,j}|)=4,
\qquad \Lambda_p^{\rm pair}=8,\quad\omega_p^{\rm lat}=1.
\]

Thus a *magnitude-only* support, positive-latent-obligation and integrity-readout selector cannot distinguish the `48` barycenter-degenerate from the `16` globally nondegenerate sign choices. In particular, the all-positive cochain and the dual-`+` cochain `(1,1,1,1,-1,1)` have identical such receipts but different coframe rank at the barycenter.

**Important limitation:** Full signed Hasse currents (`J_{ση}=2 B_{ση}c_σc_η`) can distinguish those prepared signs. Their **availability as a readout** does not supply a source-defined pre-event selection law forcing `D1 c=±c`. Likewise a *supplied* seam `U_ij` may carry phase/orientation information, but the recovered POC-1 §4.5 support law neither maps `U_ij` to these Whitney edge signs nor selects one of the two duality eigensectors. No seam-gauge identification was assumed; no `Z2` or `U(1)` gauge equivalence of these cochains has been proved.

**NO-GO_SCOPED:** `(|c|²,Λ,T,ω)` alone cannot choose a nondegenerate Whitney sign preparation uniquely. This is a failure of the named input family, not a proof that richer signed-current/connection/history dynamics cannot ever select a coframe. Source-selected native coframe and metric remain **OPEN_GATED**.

## 6. Whitney versus combinatorial duality versus metric Hodge star

1. **Incidence-to-forms compatibility (EXACT):** for any vertex cochain `u∈C⁰(Δ³;R)`, its Whitney 0-interpolant is `W0(u)=Σu_i λ_i`, and its simplicial coboundary is `(δ0u)ij=u_j−u_i`. Then

   \[
   \boxed{dW_0(u)=W_1(\delta_0u).}
   \]

   This is a genuine *metric-free* commuting differential identity for the **assumed affine realization**; it says nothing about a physical metric.
2. **Signed complement `D1` (EXACT):** a 6×6 involution on same-grade oriented *boundary* edge chains satisfying `D1²=+I`; it reverses simplex-complement incidence with the relations in PR #578 §3. Identifying `C1` and `C¹` uses the declared coefficient pairing, not a physical energy metric.
3. **Smooth interior Hodge star (type obstruction):** with a supplied oriented Euclidean/Riemannian metric in three dimensions, `*₃:Ω¹→Ω²`, so it cannot literally equal the **1-form** output of `W1∘D1` without an additional primal-to-dual identification. DEC uses `*_h:C^1(K)→C^{2}(K^*)` (convention-dependent chain/cochain notation), where `K^*` is a **distinct dual-cell complex** and weights depend on primal/dual geometry. That object is not `D1`.
4. **Boundary Hodge star (square obstruction):** for a positively oriented Riemannian `S²`, the tangent `*_2:Ω¹(S²)→Ω¹(S²)` obeys `*_2²=−I`. If one claimed `W1∘D1=*₂∘W1` on all real Whitney 1-cochains with faithful Whitney edge interpolation, composing twice would yield `W1=−W1`, contradiction. Therefore **no exact full-space identification** of the real involution `D1` with the real metric surface Hodge star exists under these hypotheses. Restrictions, complex structures, an explicit dual complex or a modified operator require a new branch.
5. **No sourced conformal sphere:** the tetrahedral `S²` shell is topological; its geometry is piecewise flat, and any map to a round `S²`, Whitney chart, `R`, or physical scale needs a declared embedding and eventually empirical correspondence. The conventional Whitney/FEM construction reproduces the positive coframe identities. No UD-specific excess has appeared.

The first two items are exact finite algebra and interpolation; the latter two are carefully typed no-go results. They do not invalidate a properly normalized discrete Hodge star built on **additional dual metric data**.

## 7. Reproduction, controls, and release criteria

- `python verify.py` — generated symbolic Whitney forms and `D1`, 24 affine permutation/covariance checks at off-centre rational coordinates with unequal edge loads, `D1` sign-twist, all 64 signed preparations, 4 orbit classifications, eigensector determinant polynomial in arbitrary `a,b,d`, positive-simplex bound, explicit non-eigen positive coframe, Whitney coboundary identity, source readout indistinguishability, and zero invariant signed-edge subspace.
- `python replay_stdlib.py` — separate author implementation using Python `Fraction` and direct determinants; 64 signs, 24 permutations, two eigensectors at boundary and interior rational points, sign-twisted duality, Whitney coboundary and source-indicator null. This is an **independent algorithm** but **the same constructor**, not non-constructor adversarial review.
- The null is **ordinary Whitney finite-element interpolation on a conventional tetrahedron**; zero novel physical consequences follow. A label match is not a physical bridge.
- No empirical target was used and no fitted coefficient selected. The `±1` alphabet, affine realization and unit-coefficient pairing are **model assumptions**. A coframe's existence is not growth, persistence or physical calibration.
- Full-UD and UD-Physics repository CI/validation are **NOT_RUN** until verified fresh checkout/CI. This report remains `development / draft / no registry entry`; physical promotion `0`.

## 8. Decision and reopening

**AUTO_LOCK candidate (scoped proof, subject to review):** exact signed-`S4` coframe classification and the `D1`-eigensubspace determinant theorem for a *supplied* reference simplex.

**AUTO_FREEZE scoped:** (i) claim that arbitrary unsigned pair Whitney sums always furnish a coframe, (ii) claim that `D1` is the real metric Hodge star on `S²`, (iii) any claim that magnitude-only POC-1 receipts select a duality eigen preparation, and (iv) claim that a finite sign class determines a physical sphere.

**OPEN_CONSTITUTIVE_SOURCE:** deriving a pre-event signed edge/connection preparation that produces the dual-sector relation and an admissible clock/update/support or gauge-readout map without fitting. The next discriminant is whether *fully sourced*, target-blind, signed Hasse-current plus seam-holonomy histories select an `S4`-covariant nonzero coframe orbit under authenticated event admission, as opposed to simply being able to measure or impose it.
