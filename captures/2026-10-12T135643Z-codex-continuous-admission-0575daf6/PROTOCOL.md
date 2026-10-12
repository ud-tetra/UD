# UD continuous contrast-zero admission candidate v0.2 and no-go

**12 October 2026 UTC. Development lane, target-blind frozen comparator; no registry entry. CANDIDATE event axiom, EXACT conditional closed-K4 dynamics and recurrence obstruction, OPEN packet source/physical clock. Physical promotion 0.** This is an append-only new branch alongside the [frozen endpoint candidate v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-12T133647Z-codex-cochain-contrast-fc1f7596/PROTOCOL.md); it does not alter its calculation.

## Sources and the inference boundary

[Paper I review draft v1.1.1 §§4.1–4.2,7.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) defines the filled K4 oriented unit-weight chain carrier and `A=d-d^T`, with `A²=-4(I-P0)` and a dimensionless closed evolution parameter `s`; event receipt admission remains open. The supplied coefficient ledger v0.39(2) (22 August 2026, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q156/Q165–169/Q173) supplies conditional mask and current formulae, no cochain-to-event trigger. [The exact clock audit v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-12T134736Z-codex-native-clock-audit-cfb6e43b/CLOCK_AUDIT.md) proves the endpoint-rule alias and `Q_h=exp(arctan(h)A)` **on this carrier**. The [OP03 independent producer handoff v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-11T020241Z-codex-op03-producer-handoff-23f7e091/PROVIDER_HANDOFF_v0.1.md) reports no independent same-carrier full endpoint sequence. Attached packet/seam equation files are placeholders, and the unavailable `Gap2_FINAL_Finite_Genesis.png` was not read.

The new assertion “a contrast zero with sign change causes a pair flip” is **not** in Paper I or the ledger. It is a constitutive **candidate**. The contrast is a newly defined cochain-energy proxy, not the ledger's distinct signed readiness `G_p^{S±}`, a physical defect, or an observed event source.

## Declared carrier, state, boundary and evolution

One filled labeled K4 has oriented vertices `(0,1,2,3)`, edges `(01,02,03,12,13,23)`, faces `(012,013,023,123)`, cell `(0123)`. The real chain state `c(0)∈C0⊕C1⊕C2⊕C3` has these 15 unit-weight coordinates and evolves for `s≥0` by `c(s)=exp(sA)c(0)`, with **no external boundary flow, nonlinear source, feedback, damping, or topology change**. The initial pair state `Theta(0)∈F2³` is separately typed. The three unordered opposite-edge pairs are `A=(01,23)`, `B=(02,13)`, `C=(03,12)`. Set

\[
 E_p(s)=\sum_{e\in p}c_{1,e}(s)^2,\qquad
 d_p(s)=3E_p(s)-\sum_{q=A,B,C}E_q(s).
\]

The full real chain state and its orientation are pre-event inputs. The generator/metric and threshold zero are fixed conventions; nothing is fitted to an endpoint. Norm `||c(s)||²` is conserved by skewness, but no energy, physical seconds or measured defect unit is asserted. The binary state does **not** feed back into `c(s)`.

Because `P0` has no edge component, let `u=c1(0)` and `v=(Ac(0))_1/2`. Then `c1(s)=u cos(2s)+v sin(2s)`. With `U_p=3 sum_{e∈p}u_e²-sum_e u_e²`, `V_p` analogously for `v`, and `W_p=3 sum_{e∈p}u_ev_e-sum_e u_ev_e`,

\[
\boxed{d_p(s)=\alpha_p+\beta_p\cos(4s)+\gamma_p\sin(4s),\quad
\alpha_p=\tfrac{U_p+V_p}{2},\quad\beta_p=\tfrac{U_p-V_p}{2},\quad\gamma_p=W_p.}
\]

Coefficients are determined by `c(0)` before any pair endpoint. They satisfy `sum_p alpha_p=sum_p beta_p=sum_p gamma_p=0`. This is exact kinematics of the **chosen proxy** under Paper I's closed flow, not a dynamics theorem for physical events.

## Candidate admission and simultaneous event protocol

**CANDIDATE RULE v0.2.** For each pair `p`, mark every isolated `s>0` at which `d_p` changes sign. At that instant toggle `Theta_p` once. At coincident roots, toggle all affected pairs in a single batch. `Theta(s)` is right-continuous; a root at `s=0` is part of the declared initial condition and is not counted. A window `(a,b]` reports the ordered event instants, every pair address, total pulse count, binary parity receipt `xi_p(a,b)=N_p(a,b) mod 2`, and `Theta(b)=Theta(a) XOR xi(a,b)`. A **null window** has no sign-changing root in `(a,b]`, not merely an unchanged endpoint. The event parameter is `s`, not a physical clock.

Let `r_p²=beta_p²+gamma_p²`. If `r_p=0=alpha_p`, the contrast is identically zero: label `DEGENERATE_HOLD`, with no event for that pair. If `alpha_p²>r_p²`, no root; if `alpha_p²=r_p²>0`, roots only touch zero and produce no toggle; if `alpha_p²<r_p²`, there are **exactly two simple sign-changing roots per contrast period `π/2`**. Roots may be computed from `alpha_p+r_p cos(4s-phi_p)=0`, `phi_p=atan2(gamma_p,beta_p)`, then sorted in the declared half-open window. Source inputs or orientation missing at the pre-event seal yield `SOURCE_DEFERRED`, not a correct null. `DEGENERATE_HOLD` is a mathematical rule convention, not a claim that nature suppresses degenerate contacts.

For a typed edge readout, only if a *separately predeclared* fixed-transport certificate covers `(a,b]` use the specific pair lift `C_e=1-Theta_{p(e)}`, hold `T_e` fixed, and calculate `h_e=C_e T_e`. If the local edge integrity map changes or is unknown, `EDGE_MASK_DEFERRED`. The rule does not create independent six-edge patterns or local `U_e` dynamics. It also does not generate new tetrahedra or a physical spacetime metric.

## Exact consequences, counterexamples and scope of the no-go

**Well-posedness and covariance (conditional).** A non-identically-zero trigonometric contrast has isolated zeros, at most two sign changes per `π/2` period. Finite windows therefore have finitely many batch event instants: no Zeno accumulation. Signed vertex permutations commute with `A`; squared edge amplitudes send the three pair contrasts through the `S4→S3` pair action. Root sets, batch receipts, and the Theta update are accordingly equivariant. For the zero chain all pairs are `DEGENERATE_HOLD` and no events occur. A single-edge basis initial chain gives a tangential A contrast and no A toggle; zero/tangent cases are explicitly tested.

**Alias witness.** In the frozen 15-coordinate order set `c0=(2,-2,2,1 | 2,2,0,0,-2,2 | 0,2,1,2 | 1)`. Exact coefficients `(alpha,beta,gamma)` are `A=(59/4,-27/4,-16)`, `B=(-1,9,2)`, `C=(-55/4,-9/4,14)`. Over `(0,π/4]`, the continuous candidate gives pulse counts `(2,1,2)` and net receipt `(0,1,0)`. The frozen v0.1 endpoint rule also gives `(0,1,0)` but cannot report the four additional pair pulses or their instants. This is an exact counterexample to **equating a net endpoint delta with an event-count or timing record**, not a refutation of v0.1's stated endpoint definition. `verify.py` independently computes exact coefficients and checks 2,472 `S4` coefficient comparisons.

**Recurrence NO-GO under this closed rule.** If any pair has `alpha²<r²`, its two sign-changing zeros recur every `π/2` units of internal `s`. That `Theta` bit toggles forever, and the corresponding pair-lift closure factor also toggles; a hard edge bit follows it only where its fixed `T_e=1`. Pair parity returns after each full contrast period. If none qualifies, this candidate produces no sign-change events at all. Therefore the no-feedback, closed filled-K4 candidate **cannot** supply a finite terminal stabilization of its affected `Theta`/pair-closure readouts after a nonzero switching history. This says nothing about separately defined geometry or hard edges with `T_e=0`. Changing boundary/source, chain generator, feedback, or event grammar defines a new branch; it does not negate this scoped obstruction.

**No unique source from closed chain algebra.** The same native `c(s)` admits two formal `S4`-equivariant binary completions: `Theta(s)=Theta(0)` for all `s`, or the candidate toggles at each sign-changing proxy zero. Both preserve the same chain flow and its norm, and the current direct-Theta conditional interface accepts a supplied receipt; neither completion is authenticated as a physical UD history. Therefore `A`, symmetry and norm conservation alone do not entail the candidate admission law. The new axiom is necessary if it is to be used at all. This is a logical source-gap result, not a theorem forbidding any future packet/defect source mechanism.

**Separate AI review.** `REVIEW.md` and `independent_check.py` were produced by a separate agent that did not construct the earlier verifiers. They confirm the clock and root-count identities by a quadratic `tan(2s)` substitution. They also establish `Q_1²=2P0-I`: under frozen v0.1, any nonzero endpoint receipt repeats at every step in the closed no-feedback model. An exact tie input gives `000` but arbitrarily small edge perturbation gives `111`, exposing a measurement-tolerance dependency. These are conditional mathematical checks, **not** independent human review or physical evidence.

## Target-blind test contract and disposition

Freeze v0.2's metric, carrier, coefficient formula, root/tie convention, initial boundary, all candidate/null windows, simultaneous batch semantics and scoring before target exposure. An independent provider must seal oriented same-carrier pre-states, a chronology and complete null/positive windows separately from hidden full pair endpoints and event instants; target code must not derive outcomes from this candidate. Score **event count, timing in a calibrated parameter, pair address, parity endpoint, and null coverage separately** against constant/no-event baselines. An in-domain ideal exact counterexample is `NO-GO` for the corresponding universal candidate claim; absence of a provider or physical clock is `NOT_RUN`. Physical comparison additionally needs units, uncertainty, calibration and a predeclared acceptance tolerance. No such independent submission is present here; nothing empirical is inferred from the constructed alias witness.

**Disposition:** The continuous rule is a precisely defined target-blind comparator, **not** an accepted UD law. The exact finite checks support its conditional algebra; its nonsettling and source-gap limitations prevent AUTO_LOCK as an event mechanism. Independent nonconstructor review is being recorded separately. Physical promotion remains **0**.
