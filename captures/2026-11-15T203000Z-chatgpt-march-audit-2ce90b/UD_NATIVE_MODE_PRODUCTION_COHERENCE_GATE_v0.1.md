# UD Native Face-Mode Production & Coherence Gate — v0.1

**Audit / execution date:** 2026-11-15  
**Research lane:** development — no registry entry; not an amendment to frozen canonical source  
**Status:** `EXACT_CONDITIONAL` (finite algebra), `NO-GO_SCOPED` (minimal event law), `OPEN_GATED` (native event selection, mode-to-observable bridge)  
**Physical promotion:** **0**  
**Supersedes:** no historical file. Extends `UD_GAP2_SIGN_SCALE_AMENDMENT_v0.2` without changing its historical calculation.  
**Purpose:** Execute the high-priority proposed route *derive native mode production and scale-dependent coherence*, beginning with the recovered trion admissibility operator. Do not target-fit an observed scalar index or running.

## 1. Typed source baseline and derivation scope

Historical sources inspected (exact bytes hashed in the companion JSON receipt):

- `triangular_transport_symbol_alphabet.md`, §§2–4: face symbol `A_t` and its binary trion admissibility rule. This is the *sole native input* for the exact face covariance identity below.
- `DistinctionTheory_MasterTheory_v1.md`, §3: same binary distinction `b ∈ C⁰(K,Z₂)` and face admissibility definition; §4: filled tetrahedral packet selected for the 3D model; §12: pre-continuum packet dynamics proposed.
- `packet_modulation_layer.md`, §§1–3: packet state `(ρ,θ,χ)` and **generic**, not fully selected, nonlinear dynamical update law.
- `seam_phase_transport.md`, §§1–5: seam holonomy / framing and additional transport degrees of freedom; not reduced to the face gate `A_f`.
- `Gap2_REVISED_Omega_Convergence.md`, §§2,5,6: historical `Ω(n)` and proposed `P_model ∝ [ΩΦ]⁻¹`; does not derive mode birth or a physical wavenumber map.
- `UD_GAP2_SIGN_SCALE_AMENDMENT_v0.2`, §§2–6: exact conditional positive-running obstruction for fixed Φ and affine `ln k` scale map; change of readout or independent Φ dynamics necessary.
- `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, rows `G05`, `G06`, `Q139`, `C02`: typed bridge/open-source and physical-promotion limits; source- and normalization-selection remain distinct.

**Conventions:** `K` is a *finite, abstract, 2-dimensional simplicial face complex* (or 2-skeleton of a filled tetrahedral 3-complex). It has vertex set `V`, edge set `E`, and face set `F`. No physical length, metric, frequency, energy, cosmic time, or electromagnetic charge is assigned. `A_f` is **face admissibility**, distinct from (i) historical triadic coherence `Φ`, (ii) `η=61/62` reconstruction-retention ratio, and (iii) observable curvature power `𝒫_ℛ(k_phys)`. `H` below is the **unsigned** face–edge incidence matrix; it is *not* the oriented chain-boundary operator `∂₂`.

## 2. EXACT identity: face gate and spectral covariance

Let `b_v∈{0,1}` and `z_v=(-1)^{b_v}`. For a face `f={i,j,k}`, source-bound admissibility is

\[
A_f=1-\delta_{b_i b_j}\delta_{b_j b_k}.
\]

An exact Walsh-character expansion is

\[
\boxed{A_f=\frac34-\frac14(z_i z_j+z_j z_k+z_k z_i).}\tag{1}
\]

Proof: all three bits equal gives three `+1` pair products, so the RHS is 0; in any of the six mixed assignments, two pair products are `−1` and one `+1`, so the RHS is 1.

**Ensemble postulate for this *null baseline*, not a sourced UD law:** independently and uniformly sample each raw `b_v∈Z₂`. Set the centered face readout `X_f=A_f−3/4`. Pair characters `\chi_e=z_i z_j` are mutually orthogonal under this measure: `E[χ_e]=0`, `E[χ_e χ_{e'}]=δ_{e,e'}` for distinct *unordered* edges in a simple graph. Write `H_{fe}=1` exactly when `e⊂f`, and 0 otherwise. Thus

\[
X_f=-\frac14\sum_{e\in E} H_{fe}\chi_e,\qquad
\boxed{C_{fg}:=E[X_f X_g]=\frac1{16}\sum_eH_{fe}H_{ge}
=\frac{|E(f)\cap E(g)|}{16}.}\tag{2}
\]

Equivalently,

\[
\boxed{C=\frac1{16}HH^{\mathsf T}},\qquad C\succeq0.\tag{3}
\]

If `HHᵀu_j=ν_j u_j` and `||u_j||₂=1`, the **native combinatorial face-mode covariance** is

\[
\boxed{S_j^{\rm face}=E[\langle u_j,X\rangle^2]=\frac{\nu_j}{16}.}\tag{4}
\]

This is an exact *mode-index-dependent structural coherence law* under the declared raw-state measure. The eigenvalue `ν_j` is an unsigned incidence-Gram spectral label, **not** automatically a physical `k²` or wavelength. The `1/16` follows from the explicitly normalized binary gate (1), not a tunable coefficient.

For an ordinary abstract simplicial complex, distinct triangles share at most one edge, so `HHᵀ=3I+A_F`, where `A_F` is the adjacency matrix of the **edge-sharing face graph**. This is an unsigned adjacency identity; no Hodge metric was silently used.

### Single filled K4 case

Four faces share edges pairwise. Therefore

\[
C_{K_4}=\frac1{16}(2I_4+J_4),\qquad
\boxed{\operatorname{spec}(C_{K_4})=\big\{\tfrac38,\underbrace{\tfrac18,\tfrac18,\tfrac18}_{3}\big\}}.\tag{5}
\]

The contrast ratio is exactly 3. It is an internal face-covariance ratio, **not** a cosmological tilt or coupling constant.

**Finite growth probe:** two filled tetrahedra `[0123]` and `[0124]`, glued on `[012]`, have 5 vertices, 9 edges and 7 distinct faces. Direct enumeration and Gram-matrix diagonalization independently produce

\[
\boxed{\operatorname{spec}(C_{\mathrm{glued}})=
\left\{\frac{9+\sqrt{33}}{32},\frac14,\frac3{16},\frac3{16},\frac{9-\sqrt{33}}{32},\frac1{16},\frac1{16}\right\}.}\tag{6}
\]

So the topology-dependent *shape* spectrum distinguishes the one-tetra and two-tetra complexes, with **no empirical numbers**. This supplies an exact finite mode readout, not a dynamical preference for one gluing.

## 3. CANDIDATE event law: exact conditional fluctuation production

The face gate does **not** select events by itself. For a clearly segregated minimal **null update**, assume exactly one vertex bit is flipped per integer tick and the selected vertex is uniformly distributed over all `N=|V|` vertices; no other packet degrees of freedom evolve. This is a **new conditional transition postulate**. It is not derived from `Ω₀`, `U_ij`, burden, or source readiness. The uniform choice is relabeling-symmetric, but symmetry does not force one event per tick.

For edge-parity character `χ_{ij}=z_i z_j`, flipping either endpoint reverses its sign. Hence

\[
E[\chi_{ij}(t+1)\mid b(t)]=(1-\tfrac4N)\chi_{ij}(t).
\]

Define `q_N=1−4/N`. Linearity gives the native *conditional face-state evolution*

\[
\boxed{E[X(t+1)\mid b(t)]=q_NX(t),\qquad q_N=1-\frac4N.}\tag{7}
\]

Define **innovation** `\xi(t+1)=X(t+1)−q_NX(t)`. Its conditional mean is zero. If the starting raw-state ensemble is uniform (and hence stationary under this Markov chain), the exact covariances are

\[
\boxed{E[X(t+\ell)X(t)^\mathsf T]=q_N^\ell C},\qquad \ell\in\mathbb N_0,\tag{8}
\]

\[
\boxed{E[\xi(t+1)\xi(t+1)^\mathsf T]=(1-q_N^2)C.}\tag{9}
\]

In face mode `j`:

\[
\boxed{E[|\xi_j|^2]=(1-q_N^2)\frac{\nu_j}{16},\qquad
E[X_j(t+\ell)X_j(t)]=q_N^\ell\frac{\nu_j}{16}.}\tag{10}
\]

**Interpretation:** Equation (10) is an exact **face-gate fluctuation-innovation production law** under the explicitly selected finite Markov update. It does *not* mean creation of electromagnetic field quanta, conserved energy, new physical modes, or a measured primordial signal. The innovations need not be statistically independent/Gaussian; only the first two moments are established.

Numerical-free test cases:

- Single triangle `N=3`: `q_N=−1/3`, a signed alternating conditional response.
- One filled `K4`, `N=4`: `q_N=0`; centered face gate has **zero conditional expectation after one tick**, and all nonzero-lag raw-ensemble covariance vanishes.
- Two face-glued `K4` cells, `N=5`: `q_N=1/5`; the *normalized* lag response is `(1/5)^ℓ` for **every** non-null face mode.

### Exact counterexample: update clock is not intrinsic scale

Add an **isolated vertex** to the filled `K4`, without adding faces or changing `H`. Its equal-time face spectrum remains exactly (5), while uniform-over-all-vertices ticking changes `q_N` from 0 to `1/5`. Thus the apparent memory change is caused solely by the **event-selection population / clock convention**, not by any change to the active face modes. A per-site sweep convention also rescales `q_N` strongly. No physical scale law follows from `N` alone.

## 4. NO-GO: the fully-admissible packet sector is gate-flat

If **all four triangular faces of a filled K4 are required to be admissible**, the allowed binary vertex assignments are exactly those with two zeros and two ones, `C(4,2)=6`. For each such state `A_f=1` on every face, hence

\[
\boxed{X_f\text{ is constant on the strictly admissible sector};\quad
\operatorname{Cov}_{\rm admitted}(A_f,A_g)=0.}\tag{11}
\]

Moreover, a one-vertex bit flip changes the number of ones from two to one or three. The result **always exits the all-face-admissible sector**. So the one-flip null dynamics (7)–(10) **cannot serve as a strictly-admissible K4 update law** without an independent admission/repair rule. A two-bit balanced update can stay admissible, but then the face-admissibility readout remains constant; additional observables (orientation, seam framing, phase, closure branch, burden, holonomy, transport current) are required for nontrivial dynamics.

**NO-GO_SCOPED:** fully-admissible K4 + face gate as the only readout + one-bit changes cannot supply a nontrivial admissible mode-production mechanism. This does not invalidate the raw-state covariance (2)–(6), which is measured on a *different* ensemble, nor does it rule out genuine UD seam/burden dynamics.

## 5. Gap 2 sign implication: what is and is not repaired

Historical `Gap2_REVISED_Omega_Convergence.md` proposed `P_model∝[Ω(n)Φ(n)]⁻¹` with `Ω=Ω∞−Dρ^n` and affine `ln k=n ln(1/r)+const`. Under its **conditional** model and `s=+1`, the existing v0.2 amendment establishes

\[
\alpha_s=-L^{-2}\frac{d^2}{dn^2}\ln[\Omega(n)\Phi(n)],
\quad L=\ln(1/r)>0, \tag{12}
\]

and a necessary and sufficient local condition for negative running

\[
\boxed{\frac{d^2}{dn^2}\ln\Phi(n)
>\frac{\lambda^2 x}{(1-x)^2}},
\quad x=\frac{D\rho^n}{\Omega_\infty},\quad\lambda=-\ln\rho.\tag{13}
\]

**Typed warning:** Here `Φ` is the *historical triadic coherence* and not `C`, `X`, `S_j`, or `q_N`. Equations (2)–(10) do **not** establish `Φ(n)` or the mode-birth map `n↔k`. If, **as a hypothetical extra map**, one took the normalized temporal coherence of the `N>4` one-bit null update to be `Φ(n)=q_N^n` (with `0<q_N<1`), then `d² ln Φ/dn²=0`, and it **cannot satisfy** (13) for a strictly increasing `Ω`. The actual K4 case `q_4=0` has no positive smooth `Φ` to log at positive lags. This is an additional **conditional rejection** of the simplest source-unsupported workaround, not a claimed identification of the historical `Φ`.

**Verdict:** We derived a *native finite covariance spectrum* and a *conditional innovation law*, **not** a native CMB scale-spectrum or the required coherent curvature of `ln Φ(n)`. The earlier red-tilt/negative-running NO-GO remains in force under its exact hypotheses.

## 6. Dependency/claim ledger delta — proposal only, not registry promotion

| ID | Object | Status | Dependencies | Result and boundary | Next gate |
|---|---|---|---|---|---|
| NM01 | `A_f` Walsh decomposition | EXACT | March `A_t` definition | Eq. (1) | None for algebra |
| NM02 | `C=HHᵀ/16` | EXACT_CONDITIONAL | raw iid-fair vertex ensemble | Eqs. (2)–(6) | Derive packet-state sampling measure from native dynamics |
| NM03 | `q_N=1−4/N`, mode innovations | EXACT_CONDITIONAL | one-bit, uniform-vertex Markov update | Eqs. (7)–(10) | Native source authorization and event-rate normalization |
| NM04 | hard-admissibility mode obstruction | NO-GO_SCOPED | all K4 faces admitted; gate-only readout; single-bit update | Eq. (11) | Additional packet variables and source-compatible local moves |
| NM05 | scale-dependent *physical* coherence `Φ(k)` | OPEN_GATED | native dynamics + mode birth + readout bridge | Not supplied | Target-blind native selection/test |
| G05/G06 | master action loop weight / physical action normalization | UNCHANGED | prior distinct source-selection gaps | NM02 is not a loop action coefficient; NM03 is not ℏ | Separate source/action-unit proof |

**Independence/visibility:** All claims remain in development lane. No new physical correspondence, no source-level freeze promotion, no actual cosmological fit, no unique native event selection and no non-constructor review. Original March historical files were not edited.

**Independent verification:** A separate Python standard-library-only implementation enumerated all raw binary assignments and all one-vertex transitions, independently reproduced exact covariance and conditional response for K4, K4-plus-isolated-vertex, and face-glued K4, and rejected every inadmissible one-bit move from the balanced 2+2 sector. Both implementations and their captured stdout are bundled in the release.

## 7. Next highest-value source law and discriminating tests

**Priority 98/100 — Native admissible source kernel:** Identify the actual typed UD state space for adjacent K4 cells (`b,χ,θ,σ,ρ,U`) and supply an *authorized, locally conservative* transition rule `T(X_{t+1}|X_t)` or deterministic generator, including no-event choice, coupling and source/sink receipts. It must not select its rate or output based on `n_s`, `α_s`, or empirical CMB values. Then compute an operator on phase/burden/holonomy fluctuations and verify whether the resulting **mode-specific** covariance/transfer produces nontrivial scale dependence.

**Independent supporting workload — Priority 93/100:** Reproduce the K4 and face-glued cases with a second implementation using enumeration and exact rational arithmetic, then extend to disjoint, edge-glued, and periodic K4 complexes. Include the isolated-vertex and hard-admissibility counterexamples as mandatory null controls. For an eventual physical bridge, preregister a separate dimensional `k_phys`, transfer observable, calibration, uncertainty, held-out mode window and baseline comparisons.

---

### Mission footer

**A. CURRENT MISSION TRAJECTORY** — Derive measurable mode generation from finite admissible packet dynamics rather than a fitted spectrum.  
**B. WHAT WAS DONE** — Proved exact face covariance, finite spectra, conditional update/innovation identities, and two independent no-go controls.  
**C. FINDING** — Structural mode weights exist; strict gate-only K4 dynamics and one-bit null updates cannot supply the missing physical scale/coherence mechanism.  
**D. UD GAP IMPACT** — New finite structural subgate closed; native source selection, Gap 2 physical bridge, G05, and G06 remain open.
