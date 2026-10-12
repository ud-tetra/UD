# Bounded K4 pre-event pair-and-edge comparison law v0.1

**12 October 2026 UTC. CANDIDATE axiomatic comparison model; no native UD source law or physical correspondence. Physical promotion 0.** Constructor-only verification. This file adds a deliberately explicit finite source clock and finite fuel to see what a complete pre-event law must contain. These additions are **new premises**, not results derived from UD chains, cochains or geometry.

## Source question and provenance

The current [Paper I v1.1.1 §§7.4, 8.4](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/browse/dist/papers/UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) leaves the native event receipt and active contact admission open and gives an exclusive symmetric-selection no-go. The admitted [direct-Theta interface, Phase 23, as audited 10 October](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-10T170752Z-codex-theta-closure-245626d6/REPORT.md) takes an external `xi`; it does not derive it. [Mask source readiness v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-10T163105Z-codex-source-readiness-3c72f65b/REPORT.md) requires a pre-event typed factor update; [pair-to-edge obstruction v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-10T161720Z-codex-pair-edge-22aece15/REPORT.md) proves pair-only equivariance cannot make all six-edge masks. [Local transport boundary v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-10T225355Z-codex-transport-boundary-6666de3f/REPORT.md) proves no exact isometry reopening under pure contractive composition. [OP03 independent producer handoff v0.1](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-11T020241Z-codex-op03-producer-handoff-23f7e091/PROVIDER_HANDOFF_v0.1.md) reports zero independent full endpoints.

The supplied `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` (22 August 2026, SHA-256 `1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63`, Q156/Q167/Q173) gives typed masks and conditional currents, not a clock/fuel source. The supplied `UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md` is a proposed review ladder, not independent review. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not read.

## Declared objects, domain and conventions

Fix one *labeled* K4. Edges are ordered `(01,02,03,12,13,23)`; pair seats are `A=(01,23)`, `B=(02,13)`, `C=(03,12)`. The state at integer step `n` is

\[
x_n=(\theta\in\mathbb F_2^3,\; C,T\in\mathbb F_2^6,\;
b^\theta\in\{0,1\}^3,\;b^C,b^F,b^R\in\{0,1\}^6,\;z\in\mathbb Z/2).
\]

Here `C` is an **edge closure predicate**, `T` an **edge transport-integrity predicate**, `h_e=C_e T_e` the hard-mask readout, `b` one-use *prepared source fuel*, and `z` an event-count phase. `F` and `R` mean transport failure and reset. The `b` registers and `z` are **new axioms**; they must be fixed or independently produced before the attempted interval. They are not observed endpoints, action, energy, seconds, or a source-derived UD field. There is no cochain dynamics in this deliberately bounded model. The pair `theta` is a different typed object from the six edge predicates: in particular `C_e=1-theta_{p(e)}` is **not** assumed.

Admissible states obey the **new constitutive bridge**

\[
\theta_p=0\quad\Longrightarrow\quad T_e=T_f=1\quad\text{for }\{e,f\}=M_p.
\]

The pair-open integrity implication is not a historical identification of pair-level integrity with edge-level integrity. It is a test axiom. Arbitrary admissible initial values, including every fuel bit and phase, must be declared before prediction; K4 is closed with no external boundary inflow. No hidden post-state variable enters the update.

## One simultaneous pre-event step

Set `on=1-z` and calculate **all** pulses from the *same pre-state*. For edge `e` in pair `p(e)`, define

\[
f_e=on\,b^F_e T_e\theta_{p(e)},\qquad
r_e=on\,b^R_e(1-T_e),\qquad
c_e=on\,b^C_e T_e(1-f_e).
\]

For pair `p` with edges `e,f`, define

\[
a_p=on\,b^\theta_p T_eT_f(1-f_e)(1-f_f).
\]

All quantities are bits; products are Boolean conjunctions. A failure takes precedence over a simultaneous closure change at its edge and holds a same-pair toggle. A reset requires failed pre-integrity and cannot occur simultaneously with a failure at that edge. Symmetry-equivalent pair toggles are **both** admitted as a batch; there is no exclusive priority.

The unique post-state is

\[
\begin{aligned}
\theta'_p&=\theta_p\oplus a_p, & C'_e&=C_e\oplus c_e,& T'_e&=T_e-f_e+r_e,\\
(b^\theta_p)'&=b^\theta_p-a_p,& (b^C_e)'&=b^C_e-c_e,&
(b^F_e)'&=b^F_e-f_e,& (b^R_e)'&=b^R_e-r_e,\\
z'&=1-z, & h'_e&=C'_eT'_e.
\end{aligned}
\]

Domain and codomain are the admissible states above. Step number is an integer index, not physical time. With no fired pulse, structural `(theta,C,T)` stays fixed although `z` advances. This distinguishes a null window from a zero-bit supplied Theta receipt. A finite prefix is specified by its initial state; no exogenous schedule is supplied after initialization.

## Exact conditional proofs and limiting cases

1. **Well-posedness and invariant:** The displayed Boolean formulas return exactly one next state. If `theta_p=0`, both edges have `T=1`, so their `f=0`; both `r=0`. A possible pair toggle can close `theta` but does not corrupt `T`. If `theta_p=1` and its toggle fires, both pre-`T` equal 1 and neither edge fails, so the newly open pair has intact post-`T`. Hence the admissible domain is forward invariant. All fuel subtractions are by bits no larger than their stock.
2. **Finite budget:** Let `B=sum b` over the four fuel classes. Then exactly
   \[B_n-B_{n+1}=\sum_p a_p+\sum_e(c_e+f_e+r_e)\ge0.\]
   Thus at most `B_0` structural pulses can ever occur, even though the phase continues. Once no pulse is possible, structural state persists. This is not an inexhaustible formation mechanism.
3. **Covariance:** A vertex permutation permutes edges, opposite-edge pairs, and their respective bits, leaving `z` fixed. Every formula uses only pairing incidence and matching indexed fields; therefore `F(gx)=gF(x)` for all `g in S4`. Exact enumerated checks include all 24 permutations on the declared fixtures.
4. **Static null:** With all source fuel zero, any signed current or burden value considered as an unmodeled spectator cannot fire a pulse; `(theta,C,T)` is fixed. This avoids the unqualified negative-source false trigger in [the fixed-structure audit](https://github.com/ud-tetra/UD/blob/main/captures/2026-10-10T182115Z-codex-structural-veto-ef5beee2/REPORT.md).
5. **Independent edge resolution:** From `theta=(1,1,1)`, `C=T=1` on all six edges, and `z=0`, each chosen six-bit `b^C` yields `h'=1 XOR b^C`; all 64 binary masks are possible. This is only representational capacity under prepared edge fuel, not evidence that UD generates those fuels or that all masks occur physically.
6. **Conditional information lower bound:** At a fixed visible pre-state, a deterministic source that can select all 64 distinct next six-edge masks must admit at least 64 distinguishable source states, equivalently at least six binary bits if encoded without redundancy. More generally, `k` distinct required outputs need at least `k` distinguishable inputs. The six `b^C` bits saturate this *capacity* bound for the displayed initial state. This is no proof that all 64 patterns are physically admissible or that a UD source provides the bits. Pair-only states fixed under the matching-action kernel cannot evade the separate equivariance obstruction by adding more pair-only bits.

## Adversarial results and actual decision

The standalone `verify.py` checks **5,120 exhaustive local admissible cases** (five pair-theta/transport combinations, four closure combinations, 128 seven-bit fuel combinations, two phases), including multistep stabilization checks, plus **12,000 full K4 S4 covariance comparisons** (125 pair-theta/transport combinations, four prepared fuel/closure patterns, 24 permutations). It also tests all 64 edge-mask outputs from one prepared base, an all-fuel-zero null, symmetric simultaneous pair firing, failure followed by reset, and same-pair failure/toggle collision. Exact integer assertions pass; `results.json` records the counts. The written factorization and invariant arguments establish the scoped general claims; finite full-K4 fixtures alone are not a universal proof.

**NO-GO as a sourced UD law:** Two states with identical visible `(theta,C,T)` and different *precommitted* `b^theta_A` yield different next `theta`. The new hidden source registers make the automaton mathematically complete by assumption; no current UD source derives their initial values, replenishment, their event-count phase, or the pair-open/edge-integrity bridge from primitive packets and native action. Encoding the desired endpoint into `b` after exposure would be circular. An initial bit choice that predetermines a future switch is a lawful toy axiom, not a physical mechanism or an independent predictive success.

**Scoped collision result:** The batch rule evades Paper I's deterministic *exclusive* symmetric-selection no-go by abandoning exclusivity; it does not solve physical admission or simultaneous contact interactions. The reset pulse is a fresh, explicit source operation and therefore does not contradict the pure-contractivity transport no-reopening theorem. The candidate permits local masks outside the pair-constant image because it carries edge-indexed input; it does not identify pair-Theta closure with all edge closure predicates.

**OPEN_GATED:** To make this a UD-derived law, provide a source-bound map from oriented pre-event packet/cochain/defect state to the clock and local resource/register dynamics, justify the pair/edge integrity bridge and allowed mask family, and define physical readout and units. A source-independent endpoint producer with all null windows must then test the frozen law; no such target was scored. Physical promotion remains **0** and nonconstructor review is pending.
