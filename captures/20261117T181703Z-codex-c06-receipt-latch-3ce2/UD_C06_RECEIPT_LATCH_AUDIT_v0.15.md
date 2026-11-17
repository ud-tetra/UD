# C06 receipt latch audit v0.15

**EXACT / CONDITIONAL NO-GO** for inferring an odd half-stock arrival and persistent shutoff from the audited receipt interfaces. **CANDIDATE (agile)** for a continuous, non-Lipschitz finite-time actuator. **OPEN** for a sourced actuator, persistent completion, Stage 2, and deficit allocation. Physical Promotion = 0.

## 1. Typed source audit

| Inspected source | What the receipt fixes | Additional datum required for C06 |
| --- | --- | --- |
| Paper I v1.1.1 §§7.1–7.3, D7.1, T7.2, T7.3, P7.4 | A supplied relative frame \(r\in S_4\) and offset \(a\in\Theta\) give an affine bijection on \(\Theta=\mathbb F_2^3\). A supplied edge map can conditionally identify a frame. | A pre-event coupling of the receipt to the quantitative odd-stock phase, plus a post-event generator rule. |
| C06 v0.7, *Scoped receipt insufficiency*; coefficient ledger v0.39 Q156 and Q166–Q170 | Finite closure and eligibility inputs constrain the declared binary lift. Signed incidence currents give stock accounting on their declared chain carrier. | An interface identifying odd stock in the aligned flag port and making its directed balance event change the active operator. |
| Paper I v1.1.1 §6 and *Pachner Event Darboux Map and Generator Pushforward* v0.1 §§7–9 | Oriented boundary identity for the move and an exact conditional pushforward on a selected signed-Hodge event sector. | A typed alignment and stock-preserving post-event map that nulls both directions of the completed ordinary-edge odd port. |
| Paper I v1.1.1, concluding discussion of winding and event time | Archived winding and journal event counts retain stipulated carrier, clock and source conditions. | A phase relation to the C06 odd exchange. Even a winding count on that oscillator would require a registered subcycle phase to locate its first half-transfer. |

This is a bounded audit of the named source text and the v0.7 declared lift. In particular \(a=\theta^+\oplus P_{\pi(r)}\theta^-\) extracted from endpoints is retrospective when the endpoint is supplied only after the event. The finite alphabet can encode a sign or hold bit if a separate pre-event rule computes it. The issue tested here is whether the audited interfaces entail that rule.

## 2. Exact receipt and stock countermodels

Use aligned Euclidean odd source and record amplitudes \(u,v\) along a shared unit direction in \(T_2\), with conserved initial stock \(N>0\), initially \((u,v)=(\sqrt N,0)\). Set \(B=v^2-u^2\). The even block may continue independently. Before the supplied receipt, the odd exchange is \(\dot u=-\omega v,\ \dot v=\omega u\) in dimensionless time. In the tested product completion the finite receipt history, event time, admission predicates and any winding label from a separate carrier are held fixed. The odd rate or phase law is an auxiliary choice. These stock records do not feed back into the certified receipt fields, which is the v0.7 premise.

At the same prescribed event time, the three admissible auxiliary rotations reaching \((u,v)=(7,1),(5,5),(1,7)\) have \(N=50\) throughout. Their recorded fractions are \(1/50,1/2,49/50\), respectively. Each is reached from the same preparation by the constant positive rate \(\omega=\arctan(v/u)/t_{\rm event}\). Their balances are \(-48,0,+48\); the middle trajectory has positive incoming flux. The phases are all in the first quadrant, with zero completed windings under the usual full-cycle convention. A fixed \((r,a)\), an event index, and even the same full-cycle winding count therefore do not entail a half-transfer guard in this completion. A sourced phase-locking premise would change the comparison.

The hold is independently underdetermined. At the balanced member, keep the pre-event path and receipt fixed. In one completion continue the original generator, so \(\dot B>0\) at the event. In another zero the shared reciprocal coefficient at receipt delivery, so \(\dot B=0\) on the subsequent hold. Both preserve stock and agree at receipt delivery. A finite event identifier or isometric frame update alone supplies no kernel change. The witness tests logical implication from the declared interface, without asserting that any of these extensions is a native retessellation.

## 3. Scope correction and continuous finite-time comparator

The v0.14 locally Lipschitz no-go stands. Finite-time stopping alone does not imply that the feedback coefficient must jump. For a general forward operator \(G_0\) and odd stock difference \(B=\|v\|^2-\|u\|^2\), the reciprocal flow gives \(\dot B=4g(B)\langle v,G_0u\rangle\). For a constant-rate scalar oscillator the incoming derivative of \(B/N\) at first half-transfer is \(2\omega\). A threshold hold reaches the surface with this incoming derivative and then stays on it.

For a continuous feedback comparator in the shared-phase scalar model, define \(b=B/N\) and \(z=\sqrt{(1+b)/(1-b)}\) for \(-1\le b<0\). Set the scalar reciprocal rate

\[
q(b)=
\begin{cases}
\displaystyle \omega\,\frac{\sqrt{1-z}}{1+z^2},& b<0,\\
0,& b\ge 0.
\end{cases}
\]

For \(N=0\) the odd block is inert. For \(N>0\) the feedback is continuous and fails local Lipschitz regularity at balance. On the incoming empty-record orbit \(z=v/u\) and \(\dot z=q(1+z^2)=\omega\sqrt{1-z}\). Consequently

\[
z(t)=1-\bigl(1-\omega t/2\bigr)_+^2,\qquad t\ge0.
\]

The first hit is \(2/\omega\), with both odd exchange directions off and with zero arrival slope. From balance, the local first-quadrant dynamics cannot restart because \(z\) is nondecreasing and the rate is zero at or above the threshold. The even block remains independent and stock is conserved. The comparator is target-informed, uses the declared parity sensing, and does not supply an independently sourced law or perturbation-resistant memory. In particular it cannot provide the strictly positive incoming derivative of the discontinuous switch.

## 4. Reopening test and replay

A source-complete route should give pre-event data and a rule that predicts the first odd half-stock arrival, then specify an update with zero odd coupling in both directions, preservation of stock, continued even exchange, and an explicit release or handoff rule. The same label should be tested at the exact before, at, and after witnesses above. Report source coupling explicitly if it excludes any witness. No Stage 2 rule is assumed here.

Run python3 replay_c06_receipt_latch.py. The replay uses exact rational stocks and derivatives and enumerates the 192 frame/offset receipts over eight input labels. The countermodel and the ODE identities supply the general scoped arguments.
