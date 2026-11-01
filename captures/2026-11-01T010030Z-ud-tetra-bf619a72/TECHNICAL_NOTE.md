# Unified Dynamics — Protected Circulation, Glued-Complex Homology and 3+1 History

**Artifact:** `UD_PROTECTED_CIRCULATION_GLUED_COMPLEX_AUDIT_v0.1`  
**Date:** 2026-10-31  
**Claim status:** `EXACT` (chain algebra, scoped Hodge and topology theorems), `NUMERICAL` (eigenvalue diagnostics), `CANDIDATE` (transient-to-protected-mode transfer), `NO-GO` (unmodified discrete Q162 transfer, source identification), `OPEN` (current O09 phase source and physical mapping).  
**Physical promotion:** **0**. Independent non-constructor scientific review pending.

## 1. Mission and immutable source boundary

Two tasks were executed: (1) search the current O09/Hodge mathematics for a reversible or topologically persistent edge mode and determine whether it is locally selected; (2) compare single K4 with glued tetrahedral complexes, including fully face-glued complexes supporting nontrivial first homology. All calculations are **target-blind**; no observed fine-structure, lepton, optical, or cosmological value was used in constructing a matrix, a source, or a threshold.

**S1.** The source register is `library_LEDGER_v0.85.json`, retrieved from [UD Ledger Recovery v0.1](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/) on 2026-10-31. Its *filename version* is v0.85 while its *inherited scientific revision* is v0.43. Entries: `O09` (`I_lift = 1/2 sum_{omega>0} a_omega Delta phi_tilde_omega`), `G05` (universal scalar retired), `Q140` (dimensionless holonomy cost), `Q153` (burden continuity), and `Q162` (scoped relaxational current `j_e=-(1/4)h_e(B1^T b)_e`). O09 does **not** define a local modal-to-link-phase intertwiner, a Hamiltonian, or a photon. Its displayed sum excludes zero-frequency modes.

**S2.** Uploaded `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, 2026-08-22; SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, historical typed source, not silently preferred over v0.85.

**S3.** Previously generated `UD_O09_BURDEN_PHASE_SOURCE_AUDIT_v0.1.zip`, SHA-256 `34ebaa245def6059424a7f1d1bda935c4d28d5456134bc20150d0f970b61af15`, draft [GitHub PR #478](https://github.com/ud-tetra/UD/pull/478). Its K4 persistence bounds are retained, not overridden. **S4.** `UD_O09_CUBIC_CURRENT_GATE_v0.1.zip`, SHA-256 `7def5fd8a7e9fee1addf09f8ee9bf74a3af946f98df85823485cbefc808c4ce7`, [PR #472](https://github.com/ud-tetra/UD/pull/472): eligible cubic current shape on one scalar K4 vertex carrier, not a native coupling.

## 2. Defined mathematical carriers and dynamics

Let `K` be a connected finite 3D simplicial complex obtained as a union of oriented **filled tetrahedra** with unique shared simplices, and work over **real** graded chain spaces `C_k(K;R)` in the declared **unit oriented-simplex Euclidean metric**. Incidence maps `B_k:C_k -> C_(k-1)` have signs from increasing vertex order; `B_(k-1) B_k=0` exactly. On edges, define

\[
L_1=B_1^{\mathsf T}B_1+B_2B_2^{\mathsf T},\qquad
\mathcal H^1=\ker B_1\cap\ker B_2^{\mathsf T}.
\]

The exact orthogonal decomposition is

\[
C_1=\operatorname{im}B_1^{\mathsf T}\oplus\operatorname{im}B_2\oplus\mathcal H^1,
\quad\dim\mathcal H^1=\beta_1(K)=\dim C_1-\operatorname{rank}B_1-\operatorname{rank}B_2.
\]

Define the **separately supplied** closed skew Hodge generator `A = B^T - B` on `C_0 ⊕ C_1 ⊕ C_2 ⊕ C_3`, where `B` is the graded incidence-lowering operator. Evolution `x'(s)=A x(s)` preserves the full unit norm; `s` is **not physical time**. These declarations do **not** import an O09 Hamiltonian or physical photon field.

### Theorem 1 — harmonic persistence and the K4 obstruction (`EXACT`, scoped)

For every `h in H^1` embedded in edge degree, `A h=0` and `L_1 h=0`. Hence `x(s)=h` is stationary, and `<h,x_1(s)>` is constant for every solution of the unforced closed skew system. Proof: `B1 h=0` and `B2^T h=0`; these are precisely the adjacent degree components of `A h`. Skew-adjointness gives `d<h,x>/ds=-<Ah,x>=0`.

For the **filled** K4, `rank B1=3`, `rank B2=3`, `dim C1=6`, so `beta1=0`. Thus there is no nonzero stationary **harmonic edge-current mode** on this carrier. There are nevertheless coexact face-boundary cycles. For `z=B2 e_f`, `A^2 z=-4 z` and the edge component evolves as `z cos(2s)` with a face component `(B2^T z/2) sin(2s)`. This is reversible **oscillation**, nonvanishing amplitude, and exactly zero mean edge response per full period—not a static current and not a physical-frequency prediction.

### Theorem 2 — no source or excitation from geometry alone (`NO-GO`, scoped)

Neither `beta1>0` nor a stationary `h` implies that the initial coefficient `<h,x_1(0)>` is nonzero. A closed Hodge evolution preserves an already prepared coefficient; it does not create it. A frequency/metric normalization, source excitation, physical clock and observable require independent admission. The current O09 positive-frequency history sum contains no explicit `omega=0` term, so **as written** it supplies no harmonic zero-mode action or excitation law. A different O09 source extension could change this branch but has not been derived.

## 3. Exact glued-complex comparison (`EXACT`, fixed carriers)

| Complex | Tetrahedra | `f=(V,E,F,T)` | `(rank B1,B2,B3)` | `(beta0,beta1,beta2,beta3)` | Face-adjacent tet connectivity |
|---|---:|---|---|---|---|
| Filled K4 | 1 | `(4,6,4,1)` | `(3,3,1)` | `(1,0,0,0)` | yes |
| Two tetrahedra, one common face | 2 | `(5,9,7,2)` | `(4,5,2)` | `(1,0,0,0)` | yes |
| Four tetrahedra, face-glued ball | 4 | `(7,15,13,4)` | `(6,9,4)` | `(1,0,0,0)` | yes |
| Four tetrahedra in a vertex-glued necklace | 4 | `(12,24,16,4)` | `(11,12,4)` | `(1,1,0,0)` | **no** |
| 24-tetrahedron face-glued solid torus | 24 | `(16,56,64,24)` | `(15,40,24)` | `(1,1,0,0)` | **yes** |
| Same solid torus, reversed annulus diagonals | 24 | `(16,56,64,24)` | `(15,40,24)` | `(1,1,0,0)` | **yes** |

The solid torus is explicitly the simplicial product of a triangulated annulus of four quadrilateral sectors with a finite interval; every triangular prism has three tetrahedra. Its 24 tetrahedra are connected by common 2-faces; this is stronger geometrically than a loop of tetrahedra attached only at points. The alternate triangulation flips each annulus quadrilateral diagonal and again gives `beta1=1`.

**Verification:** `reproduce.py` computes oriented incidence and **exact rational** ranks via SymPy DomainMatrix/Q; it checks both boundary compositions and exact Hodge nullity. `independent_check.py` separately reconstructs complexes and obtains the same ranks over `F_2`, `F_101` and `F_1009`, plus independent floating eigen/nullity diagnostics. Modular agreement corroborates but is not substituted for the exact rational ranks.

### Theorem 3 — global flat holonomy without local face curvature (`EXACT`, U(1) kinematics)

Label each annulus sector by `0,1,2,3`; duplicate it through the interval. Give each oriented edge one integer step `c_e = +1` if it advances one sector, `-1` for a reverse step, and `0` within a sector. Every tetrahedron connects at most neighboring sectors. Exactly

\[
B_2^{\mathsf T}c=0,\qquad \oint_{\gamma}c=4
\]

around the central four-edge circle `gamma=(0,1,2,3,0)`. It is therefore **closed but not exact**. For any symbolic global angle `theta`, the compact link connection

\[
\alpha=\frac{\theta}{4}c \pmod {2\pi}
\]

has `B2^T alpha=0` on every triangular face but global Wilson loop `W_gamma=exp(i theta)`. Its **local face** mismatch `delta_U(U_f)=1-cos(B2^T alpha)_f` is identically zero, although its **global loop** mismatch `1-cos(theta)` can be nonzero if that noncontractible loop is admitted as an observable. **No local face action alone selects theta**, and the Wilson phase is not in itself a transport current. Local U(1) face holonomy, global Wilson-loop phase, Hodge harmonic *real edge vector*, and measured electromagnetic response are typed different objects.

The unique harmonic representative of the cohomology class in the chosen Euclidean metric is `h=c−B1^T v`, with `B1B1^T v=B1c` and gauge `v_0=0`. Exact calculations verify `B1 h=0`, `B2^T h=0`, and `∮h=4`. Its squared norm on the first triangulation is **`7971126/278293`**. After flipping the annulus diagonals, it becomes **`2576374/89887`**. These are different exact mathematical norms under two *different* unit-simplex metric realizations of the same topological loop: the **mode count** is robust; the amplitude/metric-dependent quantity is **not** topologically selected. No numerical match to laboratory discrepancies is inferred.

## 4. Extension of the prior Q162 source-free no-go to any glued graph

**Separate conditional extension of Q162**, not a frozen global update: For a connected K graph with edge incidence `B1`, choose a scalar vertex burden `b(s)`, edge gates `0<=h_e(s)<=1`, and normalized continuous flow

\[
j_B=-\tfrac14D_hB_1^{\mathsf T}b,\qquad b'=B_1j_B,\qquad
E_B=\tfrac12\|b-\bar b\mathbf1\|^2.
\]

Then, for any piecewise measurable gate history,

\[
-E_B'=\frac14\sum_e h_e\bigl[(B_1^{\mathsf T}b)_e\bigr]^2
\ge 4\|j_B\|^2\ge4\|P_{\mathcal H}j_B\|^2.
\]

Thus

\[
\boxed{\int_0^T\|P_{\mathcal H}j_B(s)\|^2ds\le\frac{E_B(0)}4.}
\]

**NO-GO (specified model):** Source-free *burden flux* cannot sustain a positive asymptotic time-averaged squared harmonic projection on **any** finite glued complex, including one with `beta1=1`. The statement is about the Q162 flux, **not** the already populated, separately retained harmonic Hodge state. It does not imply pointwise current decay under arbitrary switching and does not prohibit a source-funded transfer.

**Exact K4 to glued-complex discrete-clock obstruction.** If one naively applies the K4 **discrete** event map `b_(n+1)=(I−L0/4)b_n` with **all gates open** to the 24-tet solid torus, some graph vertices have degree **9**. The Rayleigh quotient gives `lambda_max(L0)>=9`; the event operator therefore has eigenvalue `<=1−9/4=−5/4` and spectral radius `>=5/4>1`. This discrete extension is **linearly unstable**. This is a rigorous no-go for using the unmodified `1/4` step as a universal discrete update, not an obstruction to the continuous Q162 equation or to an independently smaller event step. The same issue holds in the alternate triangulation. Node degree is a graph property; a physical clock remains uncalibrated.

## 5. Explicit source-funded harmonic pump: conditional existence only

The previous L2 no-go does not forbid a transient pump into a **different** protected state. To demonstrate the distinction, supply an extra, unselected source law

\[
x_1'(s)=Ax(s)|_{C_1}+F(s),\qquad F(s)=P_{\mathcal H}j_B(s),
\]

on the 24-tet torus. **This is not supplied by O09**, and the choice of unit transfer coefficient is a declared test convention, not a native physical coupling. For a single open edge `01`, initial `b_1=1` and all other vertices zero, the normalized burden difference is `d(s)=exp(-s/2)` and `j_B(s)=−d(s)e_{01}/4`. The exact harmonic projection is

\[
P_{\mathcal H}j_B(s)=-\frac{h_{01}}{4\langle h,h\rangle}e^{-s/2}h.
\]

With zero initial protected state and h normalized by `∮h=4`,

\[
x_1(s)=a(s)h,\quad a(s)=-\frac{h_{01}}{2\langle h,h\rangle}(1-e^{-s/2}),\quad
\boxed{a(\infty)=-\frac{52403}{2657042}\ne0.}
\]

This exact **one-shot transfer countermodel** shows how a source that subsequently vanishes can create a persistent harmonic amplitude *if* a distinct transfer interface is supplied. Its retention is due to `A h=0` after injection, not to perpetually circulating Q162 burden flux. One cannot infer this coupling from a zero-mode existence theorem.

For a fully declared shared unit quadratic-energy convention, `E_B(s)=7/32+e^{-s}/4`, `E_h(s)=A_*(1-e^{-s/2})^2` with **`A_*=8238223227/1478872378612 < 1/4`**. Define a **reversible work bank** (not an entropy sink)

\[
E_{\rm bank}(s)=\frac{15}{32}-E_B(s)-E_h(s)
=\frac14(1-e^{-s})-A_*(1-e^{-s/2})^2\ge0.
\]

Then `E_B+E_h+E_bank=15/32` exactly. The bank need not be monotone, because late-time mode loading can draw on previously stored work. This is **a postulated common energy convention**, not a UD physical energy/clock normalization; the transfer mechanism and donor implementation remain OPEN.

## 6. 3+1 product slab of the solid-torus spatial carrier

Under global orientable tet signs, the standard staircase product of each tetrahedron with an indexed interval has four pentachora. For **24 spatial tetrahedra**, this gives **96 pentachora** and **32 vertices**. The oriented 4-chain boundary contains exactly **24 past tetrahedra** (opposite orientation), **24 future tetrahedra** (matching orientation), and **96 lateral tetrahedra**. All internal 3-faces cancel; the boundary of the boundary vanishes. The spatial boundary has 32 triangular faces. `slab_check.py` independently establishes every coefficient and orientation cancellation.

**EXACT:** The slab is a consistent combinatorial 3+1 history of a nontrivial spatial carrier. **OPEN:** There is no selected map transporting a *physical* harmonic current between slices, proper duration, causal lapse, spacetime metric, cosmological scale factor or measured optical phase. An isometric identity transfer can be *declared* but does not follow from triangulation.

## 7. Decision and next falsification gates

1. **AUTO_LOCK candidate for scoped mathematics (constructor verification only):** explicit glued-complex Betti counts, exact harmonic representative, non-exact flat holonomy, and 96-pentachoron boundary identity. A formal accepted theorem milestone remains subject to non-constructor review.
2. **NO-GO under declared hypotheses:** isolated filled K4 has no harmonic edge modes; an unchanged Q162 discrete `1/4` event rule is unstable on the 24-tet face-glued carrier; source-free continuous Q162 cannot sustain positive long-time mean-square projected flux; current O09 formula does not explicitly include harmonic zero modes.
3. **CANDIDATE:** a one-time flux-to-harmonic transfer and common-unit work bank are internally consistent for the given fixture, but **not** source-derived. Do not promote its coefficient or use laboratory residuals to determine it.
4. **OPEN_GATED:** a source-native modal/edge intertwiner and global-loop observable, Hamiltonian/zero-mode phase dynamics, phase and burden carrier coupling, action units, physical clock and causal metric, photon two-polarization and detector readout.

**Priority next action (98/100):** obtain a current-source rule for the O09 zero/harmonic sector with explicit phase/current carriers, generator, source normalization and donor work. Test it on both face-glued triangulations without changing the source law. Use *a separate earlier/later source-blind test* to decide whether a spectrum survives topology and calibration changes. No physical promotion without the independent bridge.

### Reproducible execution

- `python reproduce.py` — independently constructs exact oriented complexes, rational ranks, harmonic representatives, unit-cycle and flat-holonomy checks, K4 reversible oscillator.
- `python independent_check.py` — freshly builds all carriers; tests boundaries, ranks over three finite fields and numerical Hodge eigen/nullities; provides independent support but does not pretend modular rank is itself a rational proof.
- `python slab_check.py` — oriented 96-pentachoron slab, internal face cancellation, 144 exterior tetrahedra and `boundary^2=0`.
- `python pump_check.py` — exact conditional transient harmonic injection and reversible work-bank identity.
- Outputs: `exact_receipt.json`, `independent_receipt.json`, `slab_receipt.json`, `pump_receipt.json`.

**Source publication state:** all code, checks and manuscript are local; GitHub capture will be a draft PR pending verification. Nothing is merged or posted to public UD sites by this analysis. **Physical promotion 0.**
