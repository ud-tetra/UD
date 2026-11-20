# UD — Native Constitutive Action Selection Gate v0.4

**Date:** 2026-11-15. **Status:** `DERIVED_CONDITIONAL` (March phase-gradient primitive), `EXACT_CONDITIONAL` (finite Markov/Onsager theorem and 672-state checks), `NO-GO_SCOPED` (constitutive generator selection), `OPEN_GATED` (source selection, physical time, G05/G06). **Physical promotion: 0.**

## 1. Sources, provenance, and question

Question: Can the recovered March packet action, seam phase, burden and closure rules, together with a least-action or entropy-dissipation criterion, **uniquely** determine the transition generator for two glued filled K4 packets, without empirical fitting?

Sources checked:
- Recovered `triangular_transport_symbol_alphabet.md`, §§2–4, defines the face trion gate `A_[ijk]=1−δ_bi,bj δ_bj,bk` and symbol tuple. It defines kinematic admissibility, not event rates.
- Recovered `seam_phase_transport.md`, §§1–4, defines framed seam transport and the abelian limit `U=e^{iqφ}`, not a native positive-stochastic readout or phase noise law.
- Recovered `packet_modulation_layer.md`, §§1–3, specifies the **stylized** phase update with `κΣ sin(θ_j−θ_i)` alongside phenomenological coefficients, not a coefficient-free microscopic phase generator.
- Recovered `master_action.md`, §§2–3, gives a **coarse-grained effective field action** with free sector coefficients, not a finite microscopic Markov action or an absolute action/clock selection.
- `ud-tetra/UD-Physics`, `state/CURRENT.md` (main revision `2ab32f5f28d0461dc4d35a389e814e8415cb58e8`) and `experiments/g0506-packet-hodge-sourcegate/README.md` (2026-11-05) retain absent packet-to-Hodge maps, signed obstruction source and absolute unit. The recovered coefficient ledger v0.85 mentioned in these source-bound audits supersedes historical v0.39 for G05/G06 status. This audit neither verifies nor changes its canonical registry.
- Immediate predecessor `UD_NATIVE_SOURCE_ADVERSARIAL_v0.3`, reviewed in `ud-tetra/UD` PR #514 and `ud-tetra/UD-Physics` PR #388, establishes the `p=(1,q,0,q)` family and nonunique donor kinetics. Both PRs are unmerged development records.

The recovered sources are **historical evidence**; the source documents' timestamps alone are not independent line-level proof of composition date. This v0.4 report is a newly generated mathematical audit, not a historical March source file.

## 2. Typed finite state, allowed transitions, and conservation

Let `K=[0123]∪[0124]` have 5 vertices, 7 distinct triangular faces and 2 filled 3-simplices. `B` is the set of six `b∈(Z2)^5` satisfying `A_f(b)=1` for every face. The smallest nontrivial admitted bit moves have Hamming distance 2 and split `B` into two triangular components.

A **candidate** finite Markov state is `s=(b,d,x)` with `b∈B`, gauge-compensated relative seam phase `d∈Z4`, and face-stock vector `x∈N_0^7`, `Σ_f x_f=2`. Thus the full state space has `6·4·C(8,6)=672` states. A face-stock transition is `x→x−e_f+e_g` across an edge-adjacent face pair and only if `x_f>0`. The uniform/raw bit phase and stock sectors of previous v0.3 are not asserted as native source facts. Face stocks are not automatically native Hodge support or measured mass. The update parameter `s` is an uncalibrated Markov event parameter. No continuum metric, SI unit, or empirical `k`-map is supplied.

Every tested finite generator obeys the **closed-budget continuity identity** `Σ_f Δx_f=0`, and imposes zero exogenous source `s_B=0`; a nonzero external source would require additional tagged receipts. The general modern project source uses `Δρ=Bj_B+s_B` (historical ledger source type Q153), but does not provide `j_B` constitutive coefficients. This experiment makes only a conservative *conditional* identification with finite face-stock transfers.

## 3. The maximal phase action derivable from the March update **ansatz**

For two symmetric packet phases, and retaining only the March `κ sin` neighbor coupling, assume continuous limit with common `κ_θ>0` and no frame/forcing/memory terms:

`dθ_L/ds=κ_θ sin(θ_R−θ_L)`, `dθ_R/ds=−κ_θ sin(θ_R−θ_L)`.

Setting `φ=θ_R−θ_L`, this **exactly** implies `dφ/ds=−2κ_θ sinφ`. It is a two-coordinate gradient system for

`E_θ(θ_L,θ_R)=κ_θ[1−cos(θ_R−θ_L)]`, up to additive constant.

**DERIVED_CONDITIONAL:** The first-cosine-harmonic *potential shape* is fixed by the explicitly assumed sine phase force. Neither the primitive trion gate nor the seam link operator proves that the phase force must be that sine. Nor is a potential itself a jump propensity. A transition weight `p=(1+cosφ)/2` would additionally assume the affine readout `p=1−E_θ/(2κ_θ)`, or a coherent equal-amplitude two-channel intensity `p=|1+U|²/4`; the March source defines neither of those readouts. The competing admissible `p^2` and strict-match kernels from v0.3 remain legitimate under their own assumptions.

In particular, the v0.3 **symmetric phase diffusion** with uniform phase stationary law does not implement a nonzero deterministic sine gradient drift. Replacing it with a sampled Gibbs law requires a **new noise/temperature choice**, discretization convention and phase-event mobility.

## 4. Finite reversible-generator / Onsager action theorem

Let `S` be a finite admitted state graph and `π_s>0` a prescribed stationary measure. Each undirected allowed transition `{s,t}` can be assigned a **symmetric conductance** `c_st=c_ts≥0`, with `c_st=0` on forbidden edges. Define rates

`Q_st=c_st/π_s` (`t≠s`), `Q_ss=−Σ_{t≠s}Q_st`.

**EXACT theorem:** These rates satisfy detailed balance `π_s Q_st=π_t Q_ts` and every reversible generator on that support has this form. The admissibility graph, equilibrium measure, gauge/reversal constraints, and conservation laws select the *support and equalities*, **not** its positive conductance amplitudes.

For any evolving probability distribution `μ_s` define `r_s=μ_s/π_s`, the oriented current `J_st=c_st(r_s−r_t)`, and the quadratic deviation functional

`F(μ)=1/2 Σ_s π_s(r_s−1)^2`.

Under the master equation `dμ/ds=Qᵀμ`, exact differentiation and detailed balance yield

`dF/ds = −Σ_{ {s,t} } c_st(r_s−r_t)^2 ≤ 0`.

Thus **every** nonnegative admissible conductance family produces a valid Lyapunov/entropy-dissipation law. Even fixing the same equilibrium and requiring monotone entropy does not select the conductances.

The conditional Onsager current functional

`A_c(J;r)=Σ_{ {s,t} }[J_st²/(2c_st)−J_st(r_s−r_t)]`

has the unique minimizer `J_st=c_st(r_s−r_t)` for each **already selected** positive `c_st`. The minimal value depends on `c`, but its stationarity equations do not fix `c`. Here `A_c` is a **constructed quadratic transport action**, not the recovered UD master action, a microscopic path integral or G05's loop coefficient. Its choice of mobility metric is precisely the unresolved constitutive input. In particular, “minimize action” without a sourced mobility/traffic constraint cannot select a nontrivial unique stochastic generator. At equilibrium `r=1`, every candidate has zero currents and zero value of this functional.

## 5. Strong two-generator counterexample with equal phase equilibrium and clock traffic

For a reproducible **rational test only**, discretize phase to `d=0,1,2,3` and take the sampled potential `V_d=1−cos(πd/2)=(0,1,2,1)`. Assume inverse noise scale `β=ln 4` and therefore `π_d∝exp(−βV_d)=(16,4,1,4)/25`. This scale is **not derived from the March sources** and is not a fitted cosmological constant; it was chosen for exact rational arithmetic.

Two distinct reversible phase generators on the `Z4` nearest-neighbor cycle both preserve that `π_d`, phase reversal `d↔−d`, and the identical stationary *undirected phase traffic* `4/5` per native time unit:

- **A (square-root Gibbs):** `Q^A_{d,e}=2^{V_d−V_e}` on neighboring phase states. Its edge conductances around the four-cycle are `(8/25,2/25,2/25,8/25)`.
- **B (uniform conductance):** `Q^B_{d,e}=(1/5)/π_d` on neighboring phase states. Its four conductances are `(1/5,1/5,1/5,1/5)`.

They are **not** related by an overall clock rescaling, because their edge-conductance ratios differ even though their total traffic is exactly equal. The 672-state system additionally uses reversible Hamming-two admitted bit transitions and conservative face-stock rates `q_{f→g}=x_f w_fg(d)`, with internal `w=1` and interfacial `w=p(d)=(1,1/2,0,1/2)`. These bit and stock rules are prior explicit candidates, not sourced.

For the normalized intercell face-burden difference `Z_v`, both A and B have exactly the same first four Taylor coefficients (orders 0 through 3), but **different fourth derivatives**:

| Order at `s=0` | A | B |
|---|---:|---:|
| `R(0)` | `1` | `1` |
| `R'(0)` | `−12/5` | `−12/5` |
| `R''(0)` | `162/25` | `162/25` |
| `R'''(0)` | `−504/25` | `−504/25` |
| `R''''(0)` | `72` | `29529/400` |

Difference: `R_B''''(0)−R_A''''(0)=729/400` (**EXACT**). The independent 4-state computation reproduces the 672-state full generator result through order four. Thus matching equilibrium, total phase traffic and even three temporal derivatives does **not** determine the event kinetics.

For the deliberately nonstationary `μ_s=π_s[1+(1/4)Z_v(s)]` (nonnegative since `|Z_v|≤2`), the quadratic entropy begins at `F(μ)=3/56` and decreases with `dF/ds=−9/35` for both A and B. Both satisfy the same directional entropy law, again showing why entropy monotonicity is insufficient. Their phase part has the same Dirichlet `〈p,−Q_phase p〉_π=1/5`.

Changing the donor mobility to the conservative nonlinear candidate `q_{f→g}=x_f w_fg[1+(x_f+x_g−1)]` also preserves the stationary measure and positivity but changes the initial slope from `−12/5` to `−108/35`. This is a separate open constitutive direction even after the phase equilibrium and total phase traffic have been prescribed.

## 6. Reproduction and controls

`verify.py` independently enumerates all `672` states and reversible transitions; checks exact rationals, allowed endpoints, nonnegative rates, conserved stock, stationary measure and detailed balance for three phase laws and a nonlinear donor control; computes normalized moments to fourth order; computes the quadratic-entropy identity and phase traffic.

`replay_independent.py` uses a **different four-phase-only derivation**. For the cell-antisymmetric mode the face-stock generator obeys `Q_stock(d) Z_v = −3p(d)Z_v`, so the full correlation reduces exactly to the `4×4` effective matrix `Q_eff=Q_phase−3 diag(p)`, with `R^(n)(0)=π_phaseᵀQ_eff^n 1`. The scripts use the Python standard library and `Fraction`; no empirical target is supplied.

The first attempted third-derivative discriminant failed: both models also share the third derivative under this exact equal-traffic, `p(0:3)=(1,1/2,0,1/2)` control. That failed discrimination is retained; the fourth derivative is the first discriminant in this branch. This is a **constructor-independent mathematical implementation**, not an independent human or non-constructor review.

## 7. Disposition and reopening conditions

**NO-GO_SCOPED:** Given March sine phase ansatz, trion admission, U(1) seam labels, state conservation, specified stationary measure, reversal symmetry, positivity and even a fixed total phase-event traffic, **there remains no unique generator**. A gradient/Onsager variational principle is not sufficient without a source-selected mobility metric, phase-noise rule, two-channel detector/readout law, donor-stock response, and clock.

**Positive narrowing:** A conditional phase energy shape follows from the old sine update, and an exact finite transport-gradient action can be written once conductances are stipulated. Exact counterexamples isolate the missing selection function and give a fourth-order discriminant.

Reopen the native-selection claim only upon a source-derived local measure of transition conductance (or equivalent pre-event two-channel transport and readout), a defined microscopic phase-energy/noise law, a donor response, and a nonconventional event clock. The new rule must survive the A/B equal-equilibrium/equal-traffic control and the `κ=1` donor alternative, as well as altered shared-face boundary ownership. G05/G06, the native packet-to-Hodge map and physical correspondence remain OPEN_GATED. **Physical promotion remains 0.**

No original artifacts are overwritten. This v0.4 development result does not promote historical physical claims or contradict prior narrower NO-GO theorems.
