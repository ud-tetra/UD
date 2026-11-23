# Interpacket Junction Constructor — Source Audit and Minimal Exact Control v0.1

**Date:** 2026-11-22 America/Chicago (capture 2026-11-23 UTC).  
**Status:** `EXACT_CONDITIONAL` for declared graph complexes, `NO-GO_SCOPED` for source-free creation and strict support/chain interface; `OPEN_CONSTITUTIVE_SOURCE` for a UD-selected junction.  
**Physical Promotion:** `0`. **No metric, physical clock, energy, SI coupling, or empirical correspondence.**

## 1. Decision and typed source provenance

**Question:** Does the source-defined UD dynamics produce an interpacket junction when two regular tetrahedra's *drawn* edges meet? If not, what is the minimal exact incidence change that permits current transfer, and which independent source rule remains missing?

**Confirmed sources:**

- **UD main**, pinned `6a1fa6aa14624190bae4ed86a8a5db081ecb27e2`, `AGENTS.md` and `docs/governance/UD-SCOPE-001-observable-domain-falsifiability.md` (2026-11-11). Source 3D K4 minimality is not physical uniqueness.
- **Recovered coefficient ledger v0.85** (embedded scientific revision v0.43), `captures/2026-10-21T151000Z-codex-exit03-recovery-98dc7b12/library_LEDGER_v0.85.json`, Git blob `93e2ca31eba625989087275a71c4857848e321c6`. Q165 describes Euclidean chain-amplitude stock; Q166–Q170 its adjacency Hasse current and global generator; Q171–Q173 the existing face/cell interface and hard gating; Q177–Q179 equal-top-star *post-construction* ownership. Q157–Q160 retain open-system source requirements. Q194/Q198/Q200/Q210 address **conditional parity receipt/lineage**, not geometric event incidence. O09 is an accumulated loop-history action, not an independently established spatial junction interaction.
- **UD source audit** `captures/2026-10-13T033829Z-codex-interface-gate-ceaa5a94/UD_INTERFACE_GENERATOR_GATE_v0.1.md`, Git blob `2c7a891c4e89dc78637e3f82cc3cdd5b28ffe733`, §§1–3: fixed-complex A_K need not intertwine through subdivision; contraction + full unit readout has an exact 7>3 no-go under that stricter barycentric-subdivision interface.
- **UD Hasse curl source** `captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/source/hasse-current-curl-v0.1/source/HASSE_CURRENT_CURL_AUDIT.md`, Git blob `f02adccc67fce3c66feeabf847d8e32425badae8`, §§1–3: `dot rho=D j`, signed Hasse-current convention, two face-glued tetrahedral controls. A Hasse square is **not** a original triangular face.
- **UD-Physics** `experiments/pachner-interface-defect/README.md`, Git blob `4a7ee4e2994d8903f9ae4e52e145f198684a5b3a`, §§State/map and receipt, Dynamical obstruction: Q169 is a *fixed-complex* generator; event transfer/memory/stock budget is separately typed; no source event trigger.
- **UD-Physics** `experiments/local-hasse-quarter-event/README.md`, Git blob `f5803bb2f50c26323920c9faf3f8d807746dc42a`, v0.9 Q198-to-Q169 typed lift: parity endpoint and real amplitude flow remain underidentified.
- **UD PR #609** `captures/2026-11-23T020147Z-chatgpt-dualtetra-a83f/REPORT.md`, Git blob `80199d891ad58fb0db0dba48660fdb4fd74049d1`, §§2–6: *conditional Euclidean geometry* has six canonical, zero generic and 30 special edge-pair contacts; six canonical signed radial matches yield `C_signed=D1`. PR is draft and is not accepted native dynamics.
- **External conceptual source:** Dan Echegoyen, *Structure of Existence Video 3.1 narrated*, 2020-04-03, https://youtu.be/UDGeXvDRwgU?t=1096, 18:16 tetrahedral dynamics. The assertion that all orientations have six contacts has an exact counterexample in PR #609; here it is motivation, not a governing law.

**No-go scope:** Claims about *missing source selectors* mean absent from the identified source set, not impossible in every conceivable new theory. No backfitting or empirical target exposure.

## 2. Declared two-level mathematical experiment

### Level I: original disjoint 3D carriers

Let `K_A` and `K_B` be two **abstractly disjoint** filled oriented tetrahedra, each with graded space `C(K_i)=C0⊕C1⊕C2⊕C3` of dimension `15`. For the direct sum, the original simplicial boundary is block diagonal and the sourced skew generator (unit simplex inner product) is

\[
A_{\rm disjoint}=\operatorname{diag}(A_{K_A},A_{K_B}),\qquad A^T=-A.
\]

Because this generator is block diagonal, an initial amplitude supported solely on `K_A` can never acquire a `K_B` coordinate through this fixed-complex evolution. **EXACT / NO-GO_SCOPED:** intersection of their **Euclidean drawings** is not an algebraic incidence update. Neither Q173's gate on **existing** faces nor Q162's burden mixing creates a new shared simplex. A physically oriented `D1` sign or a spatial midpoint is not a transport junction by declaration.

### Level II: explicit, new **graph-only** contact model

Define `G_sep` by subdividing all six edges of *each* of two disjoint K4 graphs at separate midpoints. This has `V=20`, `E=24`, and two connected components. Preserve the two old copies as **labeled graph sectors**, not filled 3D cells. Define `G_J` by **identifying** exactly six corresponding midpoint pairs, pairing A edge `ij` to B's complementary edge `kl` in the canonical dual. This has eight retained corner vertices and six common junction vertices; the 24 oriented half-edges are unchanged as labels. The six identifications are an **inserted candidate contact rule**, not Q169-derived.

For either graph, work on `C0(G;Q)⊕C1(G;Q)` with canonical vertex and directed half-edge bases and orthonormal coefficient metric. Let `B1:C1→C0` be integer incidence, and define

\[
A_G=\begin{pmatrix}0&-B_1\\ B_1^T&0\end{pmatrix},\qquad \dot c=A_G c,
\quad \mathcal S(c)=c^Tc.
\]

These are algebraically the original skew-incidence rule on a **new and lower-dimensional graph**. There are no faces (`C2=0`) or 3-cells (`C3=0`) in this model. **It is not the complete re-triangulation of two interacting filled tetrahedra.**

### Exact combinatorial and spectral receipts

| Typed invariant | Separate subdivided graphs `G_sep` | Six-junction graph `G_J` |
|---|---:|---:|
| `dim C0` | 20 | 14 |
| `dim C1` | 24 | 24 |
| connected components `b0` | 2 | 1 |
| rank `B1` | 18 | 13 |
| graph cycles `b1` | 6 | 11 |
| `tr(B1B1^T)` | 48 | 48 |
| `tr((B1B1^T)^2)` | 168 | 216 |

The exact **vertex graph Laplacian** characteristic polynomials, with indeterminate `λ`, are

\[
\chi_{L_{\rm sep}}(\lambda)=\lambda^2(\lambda-5)^2(\lambda-4)^6(\lambda-2)^4(\lambda-1)^6,
\]

\[
\chi_{L_J}(\lambda)=\lambda(\lambda-7)(\lambda-4)^2(\lambda-3)^4(\lambda^2-7\lambda+8)^3.
\]

The corresponding graph-only **skew** characteristic polynomials, with indeterminate `z`, are

\[
\chi_{A_{\rm sep}}(z)=z^8(z^2+5)^2(z^2+4)^6(z^2+2)^4(z^2+1)^6,
\]

\[
\chi_{A_J}(z)=z^{12}(z^2+7)(z^2+4)^2(z^2+3)^4(z^4+7z^2+8)^3.
\]

**EXACT / CONDITIONAL:** Identifying six vertex pairs changes connectivity and the cycle rank by five, and therefore changes spectra. These are not empirical resonant frequencies and cannot be compared to the previous *full 15+15 filled-chain* action spectrum without first declaring a graded interface.

## 3. The explicit conditional cross-current and its conservation

Use the half-edge `e_A: (A,0)→J_{01}` and the matched B half-edge `e_B:(B,2)→J_{01}`. Their incidence columns overlap at one identified vertex with the same orientation, so

\[
(B_1^TB_1)_{e_B,e_A}=1.
\]

Prepare `c0(0)=0`, `c1(0)=e_{e_A}` (unit amplitude on the first A half-edge; zero elsewhere). The generator yields

\[
\ddot c_{1,e_B}(0)=-(B_1^TB_1)_{e_B,e_A}=-1,
\quad c_{1,e_B}(s)=-\tfrac12s^2+O(s^4),
\]

and hence the target **B-edge** support is `s^4/4+O(s^6)`. In `G_sep`, all A-to-B derivatives and amplitudes vanish identically because the operator is block diagonal.

For every graph initial state, skewness proves

\[
\frac d{ds}\mathcal S(c)=c^T(A_G+A_G^T)c=0.
\]

For an oriented vertex/edge incidence, Q170-like local signed Hasse currents `j_{v,e}=2 B_{v,e}c_vc_e` satisfy a control-volume balance. **Important typing:** a junction-vertex amplitude is a shared register address. Its stock cannot be separately assigned to packet A or B without an additional ownership rule, despite global conservation.

**NO-GO_SCOPED:** This establishes the capability of *a prescribed new incidence graph* to transport amplitude, not an endogenous source-selection event or a physical force.

## 4. New exact interface obstruction on the strict local edge split

Let `B_old` be the edge boundary for two disjoint unsplit K4 graphs (`8×12`). Let `T0:Q^8→Q^14` embed the eight original vertex amplitudes identically into the six-junction graph, and let the **local** edge subdivision map `T1:Q^12→Q^24` send every old oriented edge to the two consecutive half-edges of its own split route with coefficient `1`.

Then direct integer calculation gives

\[
\boxed{B_JT_1=T_0B_{\rm old},\qquad T_1^TT_1=2I_{12}.}
\]

Therefore each old unit edge becomes support `2` instead of `1`. Under the **strict local-path transfer with unchanged endpoint vertex readout**, boundary compatibility forces both half-edge coefficients to `1`; thus it is not a contraction or norm-isometry in the unweighted edge metric.

Choosing `\widetilde T_1=T_1/\sqrt2` instead gives `\widetilde T_1^T\widetilde T_1=I`, but

\[
B_J\widetilde T_1=\frac1{\sqrt2}T_0B_{\rm old}\ne T_0B_{\rm old}.
\]

This is a **scoped** obstruction to simultaneous fixed-vertex readout, strict path-local chain map and unweighted squared-amplitude preservation. It does **not** exclude a nonlocal map, rescaled metric, separately receipted support source, reservoir, or full source-defined three-dimensional refinement. Those constitute changed assumptions with fresh proof obligations. It parallels, but does not overwrite, the independently versioned UD interface-gate no-go cited above.

## 5. Signed duality is not independently observable in this graph spectrum

Any independent reorientation of the 24 graph edges replaces `B_J` by `B_JR` for a diagonal sign matrix `R` satisfying `R^TR=I`. Then

\[
(B_JR)(B_JR)^T=B_JB_J^T.
\]

The graph skew generators are related by orthogonal change of basis `diag(I,R)`. **EXACT / NO-GO_SCOPED:** all graph Laplacian and skew spectra are insensitive to the orientation sign assigned to an edge. In particular, importing the signed radial `D1` contact pattern as mere edge-basis orientation does not produce a distinguishable resonance spectrum. An actual seam phase or holonomy is a different typed variable requiring a sourced cross-packet update and an address-/phase-resolved readout.

## 6. Source-selection ledger and discriminating next gate

| Existing source item | Earned scope | Missing for an interpacket *event* |
|---|---|---|
| Q165 | Squared-amplitude stock on a **declared** simplex carrier | Pre/post event amplitude transfer and normalized metric |
| Q166–Q170 | Signed Hasse current, global skew generator, exact fixed-complex continuity | A source-authenticated rule creating a common simplex or a cross-link |
| Q171–Q173 | Face/cell flow and gates on existing incidences | Signed junction birth, coface closure and support-current debit |
| Q177–Q179 | Equal-top-star ownership *after gluing* | Ownership of new shared junction and receipt for its creation |
| Q194/Q198/Q200/Q210 | Conditional parity event/lineage gates | Intertwiner from parity obligations to actual face/edge support and junction state |
| UD-Physics Pachner interface §Dynamical obstruction | Exact source/stock transfer conditions for **prescribed** topological move | Endogenous event trigger, environmental reservoir and persistent memory law |

**Conclusion / AUTO_FREEZE scoped:** geometric overlap alone creates neither adjacency nor coupling; an unweighted strict local edge split cannot simultaneously satisfy the specified chain and squared-stock contracts; orientation signs alone cannot be identified from the graph spectrum. **Keep the narrower mathematics valid.**

**OPEN_GATED native junction law:** Require a *pre-event* source-defined tuple `r=(K_A,K_B,contact/preparation,integrity,source/stock,orientation,seam,U,history)` and a lawful decision `J(r)` selecting a topology or a generalized link **before observing the event endpoint**. It must specify (i) full 3D complex construction and `B1B2=B2B3=0`, (ii) graded chain/interface `T` with metric, lost-stock or reservoir receipt, (iii) cross-packet signed/gauge-covariant transport and total source continuity, (iv) next-event trigger and HOLD behavior, (v) separate address-/phase-resolved observables, and (vi) ordinary geometric/symmetry null controls. If no such source is recovered, retain the conditional graph control as a benchmark and stop this branch without inserting a fitted coupling.

## 7. Verification, provenance and release policy

- Constructor check `python3 verify.py` using SymPy: integer incidence/rank, two exact characteristic polynomial factorizations, skew generator and conserved support, cross-edge second derivative, strict interface chain/norm obstruction, orientation spectral null. **PASS**.
- Independent *algorithm* `python3 replay_stdlib.py` using only Python stdlib `Fraction` and rational Faddeev–LeVerrier: independent graph construction, component/cycle counts, exact polynomial coefficients, cross-edge incidence. **PASS**. Both programs by same author; **non-constructor mathematical review remains PENDING**.
- No 3D tetrahedral subdivision, physical experiment, SI input, empirical target, continuous clock, or full source-native junction generator is claimed. External source is a comparative hypothesis only. The probability of physical promotion is not estimated; **Physical Promotion = 0**.
- Package includes source register, scripts, logs, exact JSON outputs, this report, a mathematical receipt, and full SHA-256/size manifests. **GitHub repository CI and actual DPR-Coder reviewer verdict are distinct, pending steps; do not mark PASS unless observed.**
