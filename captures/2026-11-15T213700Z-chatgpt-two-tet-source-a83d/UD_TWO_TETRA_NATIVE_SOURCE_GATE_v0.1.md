# UD two-tetrahedron seam/burden/closure source-gate audit — v0.1

**Date:** 2026-11-15. **Lane:** development — no registry entry. **Classification:** EXACT_CONDITIONAL / NO-GO_SCOPED / CANDIDATE / OPEN_GATED. **Physical promotion:** 0. **Target exposure:** March historical CMB values were known; *none were used to select parameters in this audit*. No GR, EM, physical time, mass, quantum transition, or cosmology inference.

## 1. Source versions, dependencies, and statement of the question

Native *historical source-stratum* inputs: `triangular_transport_symbol_alphabet.md` §§2–4 defines the binary face-admission gate and symbolic tuple; `seam_phase_transport.md` §§1–5 defines a two-component lifted seam framing, SU(2)-like exponent, its U(1) reduction, and loop holonomy; `packet_modulation_layer.md` §§1–3 specifies `X_i=(ρ_i,θ_i,χ_i)` and a **generic** update with unspecified α,β,γ,κ and environmental/memory terms; `packet_field_equation.md` §§1–4 gives a *coarse ansatz* but no source-selected finite microscopic generator. `UD_NATIVE_MODE_PRODUCTION_COHERENCE_GATE_v0.1` §§2–4 proves the *raw independent-bit ensemble* face covariance `C_raw=HHᵀ/16` and flags source selection open.

Current mainline comparison: UD-Physics `state/CURRENT.md` (integrated 2026-11-05) and `experiments/g0506-packet-hodge-sourcegate/README.md` (v0.1) explicitly leave packet-to-Hodge source selection, phase/temporal rule, G05/G06 normalization, full sectors and physical readout open. This work neither replaces nor relaxes those obstructions. Historic `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` is **not** substituted for the recovered newer v0.85 summary. Related ongoing review: UD PR #511; UD-Physics PR #385 (both draft).

Question: can face admission + seam phase + closure and positive retained burden **uniquely derive** a local source/transition rule, and if not, what is the smallest explicit source-gated conservative candidate and its observable coherence on a face-glued tetrahedron pair?

## 2. Declared objects and no-go for literal bit flips

Use the abstract filled simplicial complex `K=[0123]∪[0124]`, glued on the face `[012]`; `|V|=5`, `|E|=9`, `|F|=7`, `|K_3|=2`. Binary distinction `b∈{0,1}^5`; for face `f=[ijk]`, `A_f=1−δ_{b_i b_j}δ_{b_j b_k}`. Let `χ_t=∏_{f⊂t}A_f∈{0,1}` be a **defined** closure indicator. This is a modeling choice equating all-face admission to packet closure; the March `χ` branch may carry additional information.

**EXACT:** A tetrahedron has all four faces admitted iff its four vertex labels split 2+2. For the glued pair the shared triple splits 2+1 and each apex must equal the singleton label, producing `3×2=6` globally admitted binary configurations. No one-vertex flip preserves global admission (exhaustive verification and elementary case argument). Therefore the earlier raw-bit flip generator has no nontrivial admissible single-flip restriction on this complex. A different admissible multi-vertex move or additional packet variables are necessary. We **hold b fixed** during the packet-stock test; this is a finite, specified submodel, not a derivation of event genesis.

## 3. A family of admissible conservative candidate generators

Define a state `(n,d)∈{0,…,M}×ℤ₄`, with `M≥1` total retained *stock count*, `B_L=n`, `B_R=M−n` and seam relative phase `d=θ_R−θ_L+a_{LR} mod 4`. The oriented seam operator is `U_{LR}=i^d`, with `U_{RL}=U_{LR}^{−1}`. Under compensated local changes of `θ_L,θ_R,a_{LR}`, `d` is invariant. The dual graph of two cells has no nontrivial plaquette; `U_{LR}U_{RL}=1` does not determine physical curvature. Unit stock, phase quadrants, and the event-time/phase-diffusion rate are **CANDIDATE conventions**; nothing in March selects them.

Take `a∈[-1,1]`, `γ≥0` and `g_a(d)=χ_Lχ_R[1+a Re(i^d)]/2≥0`. A donor-proportional, unit-stock **candidate** continuous-time Markov generator on functions `f(n,d)` is

```
Q_{a,γ} f(n,d)
 = n g_a(d)[f(n−1,d)−f(n,d)]
 + (M−n) g_a(d)[f(n+1,d)−f(n,d)]
 + γ/2 [f(n,d+1)+f(n,d−1)−2f(n,d)].
```

Out-of-domain jump terms have zero rates. Here the two stock moves represent `L→R` and `R→L` transfers; no external production occurs. If the initial packet is inadmissible, `χ_Lχ_R=0` blocks stock exchange. The phase-jump term is imposed, not sourced from holonomy. This generator respects positivity of available stocks, seam reversal symmetry, phase-gauge covariance of the specified U(1) branch, nonnegative rates, and exact conservation of `B_L+B_R=M` **per individual transfer**. It does not give a sourced physical birth/sink law or a unique unit clock.

**NO-GO_SCOPED — uniqueness:** Every `a∈[-1,1]` and `γ≥0` satisfies those structural conditions; in particular `a=0` (phase-blind transfer) and `a=1` (phase-sensitive interference gate) are distinct. Symmetry, positive stock, admission, U(1) seam and exact conservation do not select `a`, `γ`, or the donor-proportional form. Claiming this specific `Q` as a *native UD-derived transition law* would be unsupported. The correct characterization is a **source-admissible candidate family**, useful for falsifying additional selection rules.

## 4. Exact finite test, controls and conservation

Test `M=3`, `γ=1` (each phase-neighbor jump has rate `1/2`). **These are native demonstration settings only**, not physical mass, color, clock or measured energy. The state space has `4(M+1)=16` states. With `χ_L=χ_R=1`, both `a=0` and `a=1` have the exact stationary probability `π(n,d)=binom(3,n)/(2^3·4)` and satisfy `Q1=0`, `πQ=0`, nonnegative off-diagonal entries and detailed balance. Tests cover every state and every transition, and verify `ΔB_L+ΔB_R=0` at each stock move. The complementary sham (`χ_R=0`) has zero stock flux; `M=0` has no stock flux; `a=0` is the phase-blind control; `a=1` is the phase-sensitive test. Empty `M=0` is an analytic boundary control (not a 16-state numerical run).

For `D=B_L−B_R=2n−3`, the Markov generator restricts exactly on the four-dimensional subspace of `D·f(d)` to `B=L_phase−2 diag(g_a)`. The phase Laplacian has diagonal `−1`, nearest-cycle entries `1/2`; for `a=1`, `g_1=(1,1/2,0,1/2)` and

```
B = [−3,  1/2, 0,   1/2;
      1/2,−2,   1/2, 0;
      0,  1/2, −1,  1/2;
      1/2, 0,   1/2,−2].
```

**EXACT:** `spec(B)={−2 (multiplicity 2), −2−√2, −2+√2}`. At equilibrium `C_D(s)=E[D(s)D(0)]`, normalized `R_a(s)=C_D(s)/3`; the phase-sensitive exact formula is

```
R_1(s) = (1/4)e^(−2s)
       + (3/8−√2/4)e^((−2−√2)s)
       + (3/8+√2/4)e^((−2+√2)s).
```

`R_1(0)=1`, `R'_1(0)=−1`, `R''_1(0)=3/2`. Phase-blind `a=0` gives `R_0(s)=e^(−s)` with `R''_0(0)=1`; the sham transfer-block gives `R_sham(s)=1`. More generally **EXACT** `R''_a(0)=1+a²/2` for this phase-grid convention: nonzero `|a|` breaks the single-exponential response, while the burden autocorrelation cannot identify the sign of `a` by this second moment alone.

**NUMERICAL (SciPy matrix exponential):** `R_1(1)=0.4401017526359883`, `R_0(1)=0.3678794411714423`, sham `R(1)=1`; difference `0.072222311464546`. The independently derived three-exponential closed form agrees with the 16-state matrix exponential to below `10⁻¹²`. The values are dimensionless candidate Markov responses, not measured physical coherence. A pure standard-library `Fraction` implementation independently confirms stationary/detailed-balance identities and exact derivatives, without using SciPy/SymPy.

## 5. Seven-face readout and mode-specific coherence

Define a **separate candidate readout** assigning the same burden to each cell's three exclusive faces and half of each cell's burden to the shared face. At equilibrium the centered seven-face burden vector is `Y=(D/2)v` with sorted face list `[(012),(013),(014),(023),(024),(123),(124)]` and `v=(0,1,−1,1,−1,1,−1)^T`. The *raw-bit face-gate* structural covariance `C_raw=HHᵀ/16` from the prior gate obeys **EXACT** `C_raw v=(1/4)v`; this equality uses a common combinatorial face basis but **does not identify raw gate variance with burden dynamics**.

For the stock readout, `Cov(Y)=(M/4)vvᵀ`, which has **rank one** and nonzero eigenvalue `3M/2=9/2` at `M=3`. Its only active spatial face direction is `v`. The normalized time correlation of its unique active face mode is `R_1(s)` above. A distinct seam-phase observable `cos(πd/2)` relaxes with `e^(−s)` under the assumed phase diffusion and does not require burden transfer. Thus **mode-selective face readout exists conditionally** (one antisymmetric face eigenmode, with another phase-channel observable having different time behavior), but **NO multiple independently populated face spatial modes with distinct source-derived relaxation rates** have been established. A claimed primordial power `P_ℛ(k)` would require a separately sourced mode `k`, amplitudes, geometry, physical time and independent readout bridge.

## 6. Test verdicts, falsifiers, and dependency impact

| Gate | Verdict | Scope |
| --- | --- | --- |
| Filled K4-pair admissible vertex flips | NO-GO_SCOPED | No single-bit admissible moves among six all-face-admitted states |
| Positive and conservative seam transfer | EXACT_CONDITIONAL PASS | For the explicitly chosen family `Q_{a,γ}` |
| Detailed balance / stationary measure | EXACT_CONDITIONAL PASS | `M=3`, `γ=1`, admitted `χ` |
| Closed seam/sham, empty stock, constant-gate controls | PASS | Zero transfer or phase-independent reference as declared |
| Conditional phase-sensitive temporal response | EXACT / NUMERICAL PASS | Exact derivative separation and matrix exponential |
| Unique native source/transition law | **NO-GO_SCOPED** | Constraints admit infinitely many `a,γ` and alternative donor laws |
| Excitation of ≥2 independent face modes with distinct sourced rates | OPEN / NOT SHOWN | Only one face-burden mode populated in this readout |
| G05/G06 or cosmological bridge | OPEN_GATED | No packet-to-Hodge map, native action/phase normalization or physical readout |

**Required native repair to progress:** source the phase/closure/burden coupling or event authorization *before* an event; fix its kinetic selection, positivity, detailed balance/non-equilibrium conditions, rate normalization and possible independent source/sink reservoirs without using exposed physical targets. Then test a two-or-more-channel face operator that excites distinct face modes, with phase-reversal, inactive-face, donor-zero, seam-off, isolated-vertex, boundary, and energy/stock controls. An alternative admissible move family creates a new branch; it does not invalidate the all-admitted one-bit no-go.

## 7. Reproduction and limitations

- `python UD_TWO_TETRA_NATIVE_SOURCE_GATE_v0.1_check.py` — SymPy exact Gram/spectrum/stationarity and SciPy matrix exponential, JSON results.
- `python UD_TWO_TETRA_NATIVE_SOURCE_GATE_v0.1_independent.py` — separate pure Python/Fraction enumeration of all states, detailed balance, mode identity and short-time moments; no SciPy or SymPy.
- One early run failed due to JSON serialization of a SymPy integer; it was repaired before the passing receipts. This was an output-format error, not a failed mathematical assertion. Subsequent runs complete and produce the attached receipts.
- `UD_TWO_TETRA_NATIVE_SOURCE_GATE_v0.1_results.json` contains exact scopes plus numerical comparisons; all decimals are modeling outputs, not measurements.
- Data generation is explicitly synthetic/conditional; no independent apparatus, non-constructor review, calibrated clock or held-out physical prediction.

**Governance:** Development — no registry entry; do not overwrite March files, the v0.1 face gate, G05/G06 frozen records, or UD accepted claims. Physical promotion = **0**.
