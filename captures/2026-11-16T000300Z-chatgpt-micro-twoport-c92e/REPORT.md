# UD — Two-Channel Microscopic Readout and Conductance Source Gate v0.5

**Prepared:** 2026-11-15. **Lane:** development / Discovery. **Status:** `DERIVED_CONDITIONAL`, `EXACT_CONDITIONAL`, `NO-GO_SCOPED`, `OPEN_GATED`. **Physical promotion:** 0. **Provenance:** v0.5 new calculations following v0.4, not a March document or an adopted canonical rule.

## 1. Question and exact source dependency

**Question:** Can the recovered packet seam `U=e^{i\phi}`, framing doublet, burden, and admissibility rules determine a two-channel microscopic transport readout **and thereby uniquely select** the pre-event reversible conductances of the v0.4 two-K4 counterexample without fitting a physical target?

Inspected sources:

1. Recovered **March** `seam_phase_transport.md` §§1–5: `U_ij=exp(i/2 A^a_ij sigma_a)`, its Abelian reduction `U=e^{iq\phi}`, and a lifted two-state framing space. **This does not define a two-output measurement device, amplitude mixing, phase jump rate, or source-to-Hodge map.**
2. Recovered `packet_modulation_layer.md` §§1–3: packet state `(rho,theta,chi)`, generic local update, schematic sine-coupled dynamics. Its kinetic coefficients and environment/memory terms are not fixed by its primitives.
3. Recovered `triangular_transport_symbol_alphabet.md` §§2–4: closed-face binary admissibility and symbolic seam labels, not microscopic stock kinetics.
4. `UD_NATIVE_VARIATIONAL_SELECTION_GATE_v0.4/REPORT.md` §§2–6, retained in the current input bundle: 672-state reversible Markov family and two distinct phase generators A/B with the same positive stationary law, equal traffic, and distinct fourth-order correlations. Mainline source archive [UD draft PR #515](https://github.com/ud-tetra/UD/pull/515) and Discovery [UD-Physics draft PR #389](https://github.com/ud-tetra/UD-Physics/pull/389) (unmerged as inspected). Their artifact status is **development**, not proof authority.
5. `ud-tetra/UD-Physics` `state/CURRENT.md` and `experiments/g0506-packet-hodge-sourcegate/README.md` at `2ab32f5f28d0461dc4d35a389e814e8415cb58e8`: source-selected packet-to-Hodge map and absolute action unit remain OPEN; recovered v0.85 ledger supersedes v0.39 for G05/G06 governance. None is overridden here.

**Target exposure:** The old cosmological spectrum and the A/B fourth-derivative target were already exposed. This is a structural **adversarial re-realization**, not a preregistered independent prediction. No measured dataset, physical frequency, coupling or clock calibration is used.

## 2. Typed object and two-channel construction

For an oriented seam `(s,t)`, use a one-dimensional complex incoming channel fiber `\mathbb C\oplus\mathbb C` with input `z=(a,b)`, `a,b\in\mathbb C`. Its Abelian transport `U_{st}\in U(1)` maps the second input into the first input's receiving frame, with `U_{ts}=U_{st}^{-1}`. Let the input norm be `n=|a|²+|b|²\ge0`. **Assume** a balanced, coherent two-port mixer

\[
\binom{y_+}{y_-}=\frac1{\sqrt2}\begin{pmatrix}1&U_{st}\\1&-U_{st}\end{pmatrix}\binom a b,
\quad I_\pm=|y_\pm|².
\]

This matrix is unitary because `|U|=1`; accordingly

\[
I_++I_-=n,\quad I_+=\frac n2+\operatorname{Re}(\bar a U b),\quad I_-=\frac n2-\operatorname{Re}(\bar a U b).
\]

Both intensities are nonnegative. Under simultaneous receiving-frame rephasing `a\mapsto e^{i\lambda}a`, `Ub\mapsto e^{i\lambda}Ub`, each output rephases by the same factor and both intensities are invariant. The `SU(2)` framing expression in the March text motivates considering a lifted doublet but **does not select this balanced detector**; it is a declared candidate.

For `n>0` and `a=|a|e^{i\alpha}, b=|b|e^{i\beta}`, the normalized bright-port fraction is

\[
p_+(\phi)=\frac12\left[1+\mathcal V\cos(\phi+\beta-\alpha)\right],\quad
\mathcal V=\frac{2|a||b|}{|a|²+|b|²}\in[0,1].
\]

`p_- =1-p_+`. The zero-input case `n=0` defines zero event flux, **not a normalized probability**. The physical interpretation of these mathematical intensities is OPEN.

### Exact conditional phase-gate theorem

If we **add** the assumptions of (i) coherent balanced two-port readout above, (ii) `U=e^{i\phi}` and (iii) full constructive bright-port transmission at `\phi=0`, then `p_+(0)=1` forces `\operatorname{Re}(\bar a b)=n/2`. By `\operatorname{Re}(\bar a b)\le |a||b|\le n/2`, both inequalities are equalities, hence `|a|=|b|` and their relative phase is zero. Therefore

\[
\boxed{p_+(\phi)=\frac{1+\cos\phi}{2}},\quad
(p_+(0),p_+(\pi/2),p_+(\pi),p_+(3\pi/2))=(1,\tfrac12,0,\tfrac12).
\]

This **conditionally** singles out the prior four-phase `q=1/2` among the v0.3 symmetric endpoint-constrained family `p=(1,q,0,q)`. It does **not** prove that a balanced mixer or perfect bright-port anchor is native to the packet substrate. A rational unbalanced example `(a,b)=(3/5,4/5)` has `p_+(0)=49/50` and `p_+(\pi)=1/50`. Independent incoherent channels erase the cross term and give `p_+=1/2`, demonstrating the additional coherence assumption's necessity.

## 3. From two-port intensity to a pre-event transition — explicit extra assumptions

The finite carrier remains `K=[0123]\cup[0124]`, with five binary vertices, seven distinct faces and two filled tetrahedral cells. The six fully admitted bit assignments have Hamming-two component moves and no single-bit admitted move. **Candidate** event state `(b,d,x)` consists of one admitted bit assignment `b`, relative seam phase `d\in\mathbb Z_4`, and seven nonnegative face stocks with `\sum_f x_f=2`: `6\cdot4\cdot28=672` states. Here `d` is a discrete label, **not** physical time and not automatically the full continuous SU(2) link.

A **postulate**, not a source derivation, maps the coherent bright intensity to a jump propensity per native event parameter `s`. For an allowed face transfer `f\to g` at phase `d`, choose balanced input channels with `n=x_f`; then

\[
q_{f\to g}(b,d,x)=x_f\,p_+(d\pi/2)\,w_{fg},
\]

where `w=1` on the historical internal face-pair edges and the earlier interfacial model uses `w=p_+(d\pi/2)` once (not twice). Equivalently, for a single interfacial transfer use `q=x_f p_+`, with internal `q=x_f`. Reversal symmetry and the multinomial invariant face-stock measure then establish detailed balance. The assumption `n=x_f`, the Poisson-intensity interpretation, and the division between intra/interfacial faces are not derived from the March source. A symmetric donor mobility `h(x_f+x_g)` yields further admissible kinetics (e.g. `h=1+\kappa(x_f+x_g-1)`), reproducing the v0.4 donor nonuniqueness.

For reversible **phase** jumps `d\leftrightarrow e=d+1`, write the edge symmetric conductance as

\[
c_{de}=\mu_{de}\,p_+(\pi/2)=\frac{\mu_{de}}2,\qquad Q_{de}=\frac{c_{de}}{\pi_d},
\]

with `\mu_{de}=|a_{de}|²+|b_{de}|²` the per-edge input channel norm and `\pi_d>0` a separately assumed phase equilibrium. On the reverse edge `U_{ed}=U_{de}^{-1}` and conjugate inputs yield the same intensity. This constructs symmetric `c_{de}`, but the source **does not** supply `\mu`, `\pi`, the microscopic phase-noise generator, or the absolute event duration. Equal phase-port total input `\sum_e\mu_e` does not specify the distribution among edges.

## 4. Equal-input-budget A/B counterexample survives the two-channel construction

Choose for rational exact testing only `\pi=(16,4,1,4)/25`, imported unchanged from v0.4's **assumed** `\beta=\ln4` Gibbs scale. For the four phase-cycle edges `(01,12,23,30)` use the same quarter-turn seam transport `U=i` and balanced channel inputs at every edge. These two **distinct** normalized input allocations have the same total:

| model | per-edge source norm `\mu_e` | bright-port conductance `c_e=\mu_e/2` |
|:--|:--|:--|
| A | `(16,4,4,16)/25` | `(8,2,2,8)/25` |
| B | `(10,10,10,10)/25` | `(5,5,5,5)/25` |
| Both | `\sum\mu_e=8/5` | `\sum c_e=4/5` |

Both fulfill identical two-port unitarity, same seam quarter-turn `U`, exchange/reversal pairing, fixed total input norm, phase-reversal symmetry, stationary phase distribution, event traffic, all local stock conservation, and the same detailed balance law. Yet `\mu_e` profiles and phase jump generators differ. The phase reversal/equal-traffic family has one continuous free degree: writing `c_{01}=c_{30}=a`, `c_{12}=c_{23}=b`, the prescribed traffic gives `2(a+b)=4/5`, or `a+b=2/5`. A has `(a,b)=(8/25,2/25)` and B has `(1/5,1/5)`.

With the existing conditional stock-generator and interfacial bright-port gate `p=(1,1/2,0,1/2)`, 672-state exact enumeration and the independent four-phase operator both yield the normalized intercell burden readout `R(s)`:

| derivative | A | B |
|:--|:--|:--|
| `R(0)` | `1` | `1` |
| `R'(0)` | `-12/5` | `-12/5` |
| `R''(0)` | `162/25` | `162/25` |
| `R'''(0)` | `-504/25` | `-504/25` |
| `R''''(0)` | `72` | `29529/400` |

**EXACT:** `R_B''''(0)-R_A''''(0)=729/400`. The phase-blind control `p=1` gives the same `R^{(n)}(0)=(-3)^n` for both. A nonlinear donor alternative at fixed A source norm and phase port has `R'(0)=-108/35` instead of `-12/5`. Thus microscopic two-port interference **realizes both counterexamples**; it does not settle the phase mobility or donor mobility.

## 5. Decision and required source-closure gate

**DERIVED_CONDITIONAL:** A conservative gauge-covariant two-port amplitude identity exists, and a *balanced coherent bright-port plus perfect-transmission assumption* forces `p(\phi)=(1+\cos\phi)/2` in that detector. This is stronger than merely postulating the same number as an arbitrary readout, but the added optical/interference postulates are still assumptions.

**NO-GO_SCOPED:** Given only the March seam U, trion-admissibility, packet burden/phase/closure variables, two-port norm conservation, reversal covariance, per-event budget positivity, prescribed aggregate channel intensity and equilibrium phase traffic, there are distinct `\mu_{de}` allocations and reversible phase generators. No unique `c_{st}` follows. Equal A/B input **totals** are insufficient. A source law must fix the **edge-resolved channel amplitudes/norms**, their relative preparation phase and coherence, the output-to-event map, donor response and event clock. Declaring `\mu_e=\text{constant}` across edges would select B, but that is a new homogeneity **axiom** rather than a derivation from geometric incidence or seam framing. The A/B test is precisely designed to distinguish such a choice from a physically sourced law.

**OPEN_GATED:** Validity of complex two-channel amplitude superposition at the packet level, source-prepared balanced states, dynamical phase-noise law, source channel-norm budget allocation, atomically authorized event map, nonconstructive readout, G05/G06 native action and SI clock, physical wavevector/cosmology bridge, and independent non-constructor review. The construction does not invalidate existing narrower no-go results; a new premise opens a new conditional branch. **Physical promotion 0.**

## 6. Verification and provenance

- `verify.py`: standard-library exact rational 672-state enumeration, two-port trigonometric sector at rational quadrature phases, A/B equal-budget test, conserved stock, stationary phase balance, fourth derivative, phase-blind and nonlinear-donor controls.
- `replay_sympy.py`: independent SymPy complex-matrix and 4-state moment replay, including gauge-covariance and unequal-amplitude limits.
- `results.json`, `replay_results.json`, run logs, and SHA-256 `MANIFEST.json` are in the release package; `inputs/` retains selected source bytes. `python verify.py` and `python replay_sympy.py` ran successfully on 2026-11-15. These are two constructor-directed implementations, **not** an independent external review.
- Neither source PDF nor physical instrument trace is needed for this finite mathematical gate. No code or source bytes are overwritten in previous v0.4 release or accepted current repository.

**Next discriminant:** Derive **locally** from the packet action and preparation rule the source-resolved norms `\mu_{de}`, not just the aggregate input budget or phase gate. Require a fixed pre-event preparation predicting either A or B (or a third quantitatively specified law), then test held-out phase-dependent fourth derivatives and donor perturbations. An independent non-constructor review is needed before registry consideration.
