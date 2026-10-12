# Separate AI review of the frozen UD cochain contrast and clock audits

**12 October 2026. Nonconstructor AI review of mathematical scope only. No independent human review, same-carrier outcome corpus, physical evidence, CRL promotion, or edit to either capture.**

## Materials and method

I inspected the [frozen contrast protocol v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-12T133647Z-codex-cochain-contrast-fc1f7596/PROTOCOL.md), [clock audit v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-12T134736Z-codex-native-clock-audit-cfb6e43b/CLOCK_AUDIT.md), [Paper I v1.1.1 §§4.1–4.2, 7.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md), and the supplied `project_sources/20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md` (especially Q156 and Q165–Q173). Paper I §4.3 also contains the filled-cell identity used in the clock audit. I subsequently checked the separate local `ud_continuous_admission/PROTOCOL.md` v0.2 branch as an additional conditional comparator, without editing it.

The accompanying [independent_check.py](independent_check.py) constructs all 15 nonaugmented oriented simplex coordinates from subsets, inserts alternating boundary signs, and works over rational numbers. It neither imports the earlier verifiers nor reads their result files. It checks the Cayley equation against an independently evaluated polynomial in the generator, exact witness scores, positive roots of a new quadratic substitution, a clock-dependent input, a tie perturbation, and signed vertex relabelings. Run `python3 independent_check.py` from this directory. Finite executions check the implementation; the arguments below state which conclusions hold for every real input.

## Findings

### 1. The clock identity is exact on the declared carrier, with a narrower interpretation

The independently constructed boundary has `A² = −4(I−P0)` and `AP0=0`, where `P0` projects onto the uniform vertex coordinate. Hence on the complement of `P0`, `A/2` is a complex structure. Direct multiplication of the Cayley equation gives

\[
Q_h=P_0+\frac{1-h^2}{1+h^2}(I-P_0)+\frac{h}{1+h^2}A
=e^{(\arctan h)A}\quad(h\in\mathbb R),
\]

with principal `arctan`. In particular, `Q_1=P0+A/2` samples the native continuous flow at `s=π/4`, and `Q_{1/2}` at `s=arctan(1/2)`. This **confirms** the clock audit. The protocol's description of Cayley as a discretization is correct as a chosen update convention, but on this filled unit-weight K4 the map has no integration error relative to the flow at its mapped parameter. It is **not** the native flow at `s=h` in general. The special one-frequency reduction is not established for weighted or glued carriers. No physical duration or event interval follows from this identity.

At the frozen `h=1`, there is a further exact consequence:

\[
Q_1^2=2P_0-I,\quad Q_1^4=I,\quad
d_p(Q_1^{n+2}c)=d_p(Q_1^n c).
\]

The last equality follows because `P0` has no edge component and each contrast is quadratic in edges. Thus `xi_{n+1,p}=xi_{n,p}` for **every** initial cochain, including endpoint ties, under the protocol's no-feedback closed update. If any pair flips once, it flips on every subsequent step; `Theta` toggles periodically and that pair closure cannot settle. This strengthens the protocol's observed 32-step example into a universal conditional nonsettling theorem. A fixed transport bit `T_e=0` can hide a pair closure toggle from the product `h_e=C_eT_e`; the conclusion is about `xi`, `Theta`, and `C`, not every possible geometric observable or physical history.

### 2. The alias witness guarantees sign-changing zeros, and the endpoint rule omits them by definition

For the clock audit's 15-coordinate witness, independently computed `d(0)=(8,8,−16)`, `d(π/8)=(−5/4,1,1/4)`, and `d(π/4)=(43/2,−10,−23/2)`. Continuity alone forces one strict sign-changing zero of A and C in each of `(0,π/8)` and `(π/8,π/4)`. The frozen endpoint receipt is `(0,1,0)`, exactly as stated. The intermediate signs make the two zeros **distinct for each pair**, not merely an inference from equal endpoint signs.

The exact form `d_p(s)=α_p+β_p cos(4s)+γ_p sin(4s)` gives a sharper count. On `0<s<π/4`, set `t=tan(2s)>0`. The sign of `d_p` is the sign of `(α_p−β_p)t²+2γ_pt+(α_p+β_p)`. For this witness the numerators are:

| Pair | Exact numerator | Positive roots in the interval |
|---|---|---:|
| A | `(43/2)t²−32t+8` | 2 |
| B | `−10t²+4t+8` | 1 |
| C | `−(23/2)t²+28t−16` | 2 |

Each discriminant is positive; the product and sum of roots establish the displayed positive-root counts. The three endpoint scores are nonzero, so `(0,π/4]` has exactly `(2,1,2)` strict pair-root pulses. Distinct pairs might cross at one common instant; `(2,1,2)` counts pair pulses, not necessarily five distinct batch instants. This confirms the separate continuous candidate v0.2's witness and its parity `(0,1,0)`. It does not contradict v0.1: that protocol explicitly defines a **single endpoint sign comparison**, rather than a count of continuous zeros.

For any nonconstant scalar contrast, `r²=β²+γ²`: `α²<r²` gives exactly two simple sign-changing roots per `π/2` contrast period; `α²=r²>0` gives tangencies with no sign change; `α²>r²` gives none. The `α=β=γ=0` case is identically zero and needs a separate hold convention. Thus v0.2's classification is correct. Its no-feedback recurrence proves nonsettling of its active `Theta` bits and pair closure after a nonzero event history. A claim about *all* geometry would require an explicit geometric readout and nonzero integrity on an affected edge.

### 3. The tie convention is covariant but discontinuous

For `c=(−2,−2,−1,0 | 0,0,0,0,0,0 | 0,0,0,0 | 0)`, all initial contrasts are zero while the `Q1` endpoint has `d=(−2,1,1)`. The stipulated tie rule yields `xi=000`. Adding any nonzero `ε` to edge `01` leaves the `Q1` edge endpoint unchanged (at `h=1`, `Q1` sends edge input into other chain degrees), while the initial contrasts become `(2ε²,−ε²,−ε²)`. The receipt is then `111` for arbitrarily small `ε`. This is an exact boundary discontinuity, not a defect in a binary strict-threshold rule. It matters for any proposed measured application: score uncertainty near zero and equality handling would require a separately frozen tolerance/uncertainty contract; an exact rational tie cannot be presumed measurable.

For all 24 vertex permutations, the signed chain action conjugates the boundary and generator, and opposite-edge squares permute in the `S4→S3` action. The independent checker confirms this on the alias, tie and clock witnesses, including receipt covariance. Algebraically it holds for all states. Permuting the pre-`Theta` bits and fixed edge integrity bits with their corresponding seats yields covariance of the conditional lift. A fixed `T` certificate is still an extra premise; covariance cannot supply it. Batch flipping all tied qualifying pairs avoids the exclusive-selection obstruction discussed in Paper I, but supplies no independent admission authority.

### 4. Source and event-time nonidentification are properly scoped

The same initial chain `c=(−2,−2,0,0 | −2,0,0,0,0,0 | 0,0,0,0 | 0)` gives `xi=111` under `h=1` and `xi=000` under `h=1/2`, using the same contrast predicate and exact native flow. This is an independent clock-choice witness. More fundamentally, for a fixed native `c(s)` the identically zero receipt law and the contrast-trigger law are both deterministic and `S4`-equivariant; skewness, norm conservation and equivariance cannot distinguish them. The nonidentification is **relative to those premises**, not a proof that a richer packet source could never derive an event rule.

Paper I §7.4 expressly leaves the pre-event offset/source outside its conditional affine map. The ledger's Q165–Q169 supply support and incidence dynamics, while Q156/Q167/Q173 give conditional hard gating and currents; they do not equate this squared-edge contrast with the signed `G_p^{S±}` readiness or make a zero crossing a switch. The candidate therefore adds a constitutive proxy and an event/admission axiom. It can be a target-blind comparator, but its mathematical receipts are not independent observations. Continuous `s`, frozen step count `n`, source event count and measured seconds remain distinct clocks. A first-crossing or every-crossing rule is a new candidate with different null and timing semantics, as the v0.2 branch acknowledges.

## Disposition and limits

**Confirmed exact mathematics:** the filled-K4 Cayley/flow identity; the alias witness's two A and two C sign-changing zeros and exact `(2,1,2)` continuous pair counts; signed covariance; the closed `h=1` repetition theorem. **Additional edge case:** the `000` tie receipt jumps to `111` under arbitrarily small edge perturbations. **Not established:** native source/admission, physical clock, local transport update, geometric creation or stabilization, independent same-carrier endpoint accuracy, and empirical null performance. No result here promotes either candidate or supplies an independent human review.
