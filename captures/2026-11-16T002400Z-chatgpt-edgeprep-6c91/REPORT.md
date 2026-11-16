# UD edge-resolved amplitude preparation and source-selection gate v0.6

**Execution date:** 2026-11-15.  **Research lane:** source-bound mathematical development and Discovery; draft review only.  
**Status:** `EXACT_CONDITIONAL` (finite orbit theorem), `NO-GO_SCOPED` (unique native source selection), `OPEN_GATED` (packet preparation, stock mapping and clock).  **Physical Promotion = 0.**

## 1. Mission and sources

Question: Can the preceding v0.5.1 two-channel formula, combined with recovered March packet preparation, trion closure and seam geometry, **select the edge-resolved input norm** `mu_e=|a_e|²+|b_e|²`, and thereby select the reversible phase-cycle conductance `c_e=mu_e/2`, without selecting it from the known higher-derivative correlation result?

Source and scope:

- Recovered March `packet_modulation_layer.md`, §§1–3, defines packet `(rho_i,theta_i,chi_i)` and a **schematic** nonlinear burden update; neither site preparation nor edge-resolved mobility is given.
- Recovered March `seam_phase_transport.md`, §§1,4–5, defines seam transport operators and an abelian `U_ij=e^{iq phi_ij}` reduction; it does **not** fix a coherent two-port mixer or edge coupling.
- Recovered March `triangular_transport_symbol_alphabet.md`, §§2–4, supplies the face-admissibility predicate and framing/closure labels, not a weight rule.
- `UD_TWO_CHANNEL_MICRO_READOUT_GATE_v0.5.1/REPORT.md` §§2–5 and `ADDENDUM_v0.5.1.md`: conditional unitary two-port readout, exact A/B equal-budget counterexample. Reference in `ud-tetra/UD` draft PR #517 / `ud-tetra/UD-Physics` draft PR #391, not canonical acceptance.
- Integrated Discovery G05/G06 source gates (UD-Physics `main@2ab32f5f28d0461dc4d35a389e814e8415cb58e8`, `experiments/g0506-packet-hodge-sourcegate/README.md`) still block native packet-to-Hodge source/absolute action normalization. No new result overrides them.

**Typed provenance:** `rho_i` is an assumed packet burden/amplitude; `pi_d` is a stationary **probability** assigned to a *four-state phase register*. They are not equal objects. Interpreting `pi_d` as the squared input amplitude of a source channel requires an additional preparation map `P:(b,rho,theta,chi,U)->(a_e,b_e)_e`, currently OPEN. The register's nearest-neighbor *phase edges* are not simplicial edges of the two-glued-K4 geometry. `mu_e` is a pre-event dimensionless two-port norm, `c_e` a reversible generator conductance, `Q_{de}=c_e/pi_d` a dimensionless event-rate generator, and event parameter `s` is not physical time. All these identifications must remain separate.

**Target exposure:** The historical A/B conductance profiles are already known, as is the fourth-derivative discriminant from v0.4. This audit treats A/B as exposed internal controls. It selects no formula by matching their fourth derivative, uses no CMB target, and claims no blind confirmation.

## 2. What follows from a direct two-port packet preparation

On an oriented phase edge `(d,e)`, assume raw coherent incident input states `a=sqrt(r_d)`, `b=sqrt(r_e)`, with phase transported by `U=e^{i phi}` and a receiving-frame convention that makes `a,b` real and nonnegative before the seam rotation. For rational input loads `r_d,r_e>0`, the **postulated** balanced mixer gives

`I_+(phi) = (r_d+r_e)/2 + sqrt(r_d r_e) cos(phi)`,  
`I_-(phi) = (r_d+r_e)/2 - sqrt(r_d r_e) cos(phi)`.

**EXACT:** `I_++I_-=r_d+r_e = mu_raw`. The visibility is `V=2 sqrt(r_d r_e)/(r_d+r_e)` and the normalized destructive-bright intensity at `phi=pi` equals

`p_+(pi) = (sqrt(r_d)-sqrt(r_e))^2 / [2(r_d+r_e)]`.

It vanishes **iff** `r_d=r_e`. Under unequal loads, the direct two-port interpretation conflicts with the v0.5.1 *perfect seam-off* axiom `p(pi)=0`. At the four-phase benchmark's adjacent load ratio 4:1, `V=4/5` and `p_+(pi)=1/10`, all four edges. On a 16:1 edge, `V=8/17` and `p_+(pi)=9/34`. These are exact combinatorial readout checks, not physical leakage measurements.

A norm-preserving real rotation can equalize the two incident amplitudes to `|a'_e|²=|b'_e|²=(r_d+r_e)/2`, restoring the perfect gate `(1+cos phi)/2` without changing the **sum** `mu_raw=r_d+r_e`. However, **the prep rotation and any transfer of stock between packet inputs are not supplied by the March source**. Such balancing is a *candidate source-preparation operation*, not a theorem of the substrate. An alternative matched geometric, harmonic, or passive-minimum preparation changes the total input norm and requires an explicit allocation/sink budget. The bright-port intensity is not automatically an event rate.

## 3. Exact restricted orbit theorem: why A appears without fitting R''''

Use the *assumed*, previously exposed four-phase equilibrium weights `pi=(16,4,1,4)/25` (the v0.4 Gibbs sample at inverse noise `beta=ln4`). On its cycle `E=(01,12,23,30)`, assume a local **symmetric degree-one homogeneous** function `f:(R_{>0})²->R_{>0}` chooses incident norm `mu_{de}=f(pi_d,pi_e)` (hence adds a yet-unproved identification of phase probability with source load).

Let `h=f(4/25,1/25)>0`. The 01 and 30 edge loads are, up to permutation, `4*(4/25,1/25)`, whereas edges 12 and 23 are `(4/25,1/25)` up to permutation. Symmetry and one-homogeneity give the **exact** edge profile

`mu = (4h,h,h,4h)`.

Fixing the benchmark `sum_e mu_e = 8/5` (an **imposed comparison-clock normalization**, not a native prediction) yields `10h=8/5` and `h=4/25`. Therefore, **for every such f**, one obtains

`mu=(16,4,4,16)/25`,  `c_e = mu_e/2=(8,2,2,8)/25` (**Generator A**).

This is **EXACT_CONDITIONAL**, including a previously unrecognized positive but narrow restriction of the A/B family: Generator B with `mu_e=2/5` constant is not realizable by one common positive symmetric one-homogeneous local f acting on these four-phase loads. The proof does **not** select f, pi, source-preparation map, source/burden identification, absolute event clock, or the native physical generator. The prior entire family `mu^lambda=(1-lambda)mu^A+lambda mu^B`, `0<=lambda<=1` remains admissible **without** the new homogeneity postulate.

For direct demonstration, all four symmetric one-homogeneous choices below normalize to A on the four phase edges:

- Raw unitary input norm: `f_sum(x,y)=x+y`.
- Matched geometric input norm: `f_geo(x,y)=2 sqrt(xy)`.
- Matched harmonic input norm: `f_harm(x,y)=4xy/(x+y)`.
- Passive minimum input norm: `f_min(x,y)=2 min(x,y)`.

The fact these distinct **functions** agree after four-edge normalization is *not* evidence they are physically the same operator. Their pre-normalized total norms differ and require different source receipts. Uniform per-edge `f_const=1` instead produces B at the same aggregate budget. Its lack of degree-one homogeneity is precisely why the stronger conditional premise excludes it.

## 4. Adversarial stress: six-phase cosine sample breaks the degeneracy

Choose a different, clearly **assumed** six-state phase alphabet `d in Z6` with `V_d=1-cos(2pi d/6)` and inverse noise scale `beta=2 ln4`. The exact rational Gibbs weights are

`pi6=(256,64,4,1,4,64)/393`.

This is a structural stress test of phase-resolution/phase-noise dependence, not a new physical clock or new observed dataset. Normalize each edge-preparation law to `sum mu=1` for shape comparison. Exact profiles, ordered by the six cyclic phase edges, are:

| Preparation function | Normalized 6-edge norm profile |
|---|---|
| `x+y` | `(160/393, 34/393, 5/786, 5/786, 34/393, 160/393)` |
| `2 sqrt(xy)` | `(32/73, 4/73, 1/146, 1/146, 4/73, 32/73)` |
| `4xy/(x+y)` | `(544/1185, 8/237, 17/2370, 17/2370, 8/237, 544/1185)` |
| `2 min(x,y)` | `(32/69, 2/69, 1/138, 1/138, 2/69, 32/69)` |
| constant | `(1/6,...,1/6)` |

The first/second edge norm ratio for the raw-sum law is `80/17`; for the geometric law it is `8`. Since these are different **exact** rationals, no global choice of event-clock scaling can identify the two allocations. Uniform phase-load control `pi6=(1/6,...,1/6)` makes all five normalized profiles equal, confirming that nonuniform loads (not arbitrary numerology) distinguish them.

The choice `beta=2ln4` creates rational square roots and was made for exact arithmetic, not from the source or empirical data. Selection of the alphabet, noise, and phase potential remains OPEN. This six-phase exercise does not contradict the four-phase orbit theorem: that theorem assumes the specific orbit structure with all successive load ratios exactly 4 or 1/4.

## 5. Boundary and empty-channel counterexample

For a donor load `x>0` and empty receiving channel `y=0`, the raw-sum preparation has `f_sum(x,0)=x`, permitting a nonzero incident norm, whereas geometric, harmonic and passive-minimum functions all give zero. Thus they prescribe opposite source-admission behavior at the empty-channel boundary. Whether growth into an empty packet is allowed, and where remaining norm goes on a blocked seam, are independent source/sink and closure questions that the 4-phase normalized ratios cannot answer. A complete pre-event law must include source/sink receipts and actual boundary/closure status, not just an edge norm function.

## 6. Verification and exact limits

- `verify.py` (standard library `Fraction`) independently constructs positive symmetric homogeneous preparations and normalizes them, checks all rational 4-state and 6-state profiles, conservation `I_++I_-`, direct-unequal seam-dark residual, a norm-conserving matching input, the continuum of A/B reversible conductance interpolants, uniform-load control and zero-load boundary.
- `replay_independent.py` uses orbit arithmetic and two-edge ratios, **not** the five-function enumeration, to check the same central theorem and six-phase obstruction; its results are preserved in `replay_results.json`.
- The **unchanged** original v0.5.1 `verify.py` was rerun in `baseline_v0.5.1/` and again passed the complete 672-state exact nonnegative-conservation/detailed-balance and historical A/B counterexample checks, with `replay_portable.py` independently passing. This baseline includes the already exposed fourth-derivative values but **none were used to select the v0.6 functions**.
- Verification is constructor-executed and an independent mathematical implementation, not independent non-constructor review. No raw SI calibration, external dataset, G05/G06 or CMB observable was introduced.

## 7. Decision and reopening gate

**DERIVED_CONDITIONAL:** Given the *new* phase-probability-to-source-load identification, a common symmetric positive degree-one local preparation functional, the special 4-state Gibbs orbit and imposed total event input norm, **relative** edge intensities uniquely collapse to A. This is useful but narrow mathematical closure, not native source selection.

**NO-GO_SCOPED:** The recovered March sources provide no such preparation map, no unique homogeneous f, no source/phase probability identification, no unique phase noise or alphabet, no unforced stock balance at the empty channel, and no physical event clock. Even a direct coherent two-port source fails perfect seam-off for unequal loads unless a new balancing operation is imposed. An alternative six-phase admissible stress distinguishes four functions that coincide on the four-state test.

**Priority next dependency:** Source a packet-level preparation/edge-port coupling and stock/closure receipt with a declared boundary, and separately derive the event-scale normalization. Demand transfer success on inequivalent phase-load orbits, zero-receiver controls, and a finite source/sink accounting law *before* any claim of a unique generator. Freeze the new rule before exposure to held-out physical targets. Current G05/G06 obstructions and Physical Promotion=0 remain unchanged.
