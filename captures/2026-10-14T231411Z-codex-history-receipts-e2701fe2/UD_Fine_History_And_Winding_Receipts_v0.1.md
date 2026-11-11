# Fine histories and the receipts needed to recover winding

14 October 2026. Development - no registry entry. Constructor verification only. Physical promotion: 0.

This package takes the next dependency identified by manuscript v0.10: it declares a fine-history domain, supplies a normalized kernel family, and tests which additive history quantities its receipts determine. It closes a conditional mathematical contract, not the native source of UD events.

The all-open reference graph has eight Boolean vertices and 192 action-distinct edges. Separating nulls gives 44 active receipts plus one null symbol. Every coarse weight-compatible active receipt word can be lifted in this model. Six free coarse probabilities nevertheless permit any positive stationary weight law; symmetry does not select the preference. A general proof and a rank-69 exact certificate show that scalar, frame-composition-consistent increments reduce to three Hamming-shell potential differences, so closed histories have zero increment. A deliberately different graph-cycle functional supplies a concrete receipt collision and an exact supplemental-memory bound: N+1 symbols for a repeated null-distinguished active receipt word, or 2N+1 when nulls are merged into the same code.

These are different hypotheses, not competing conclusions about one undeclared winding. The graph-cycle diagnostic explicitly fails frame-composition consistency and scalar relabeling covariance. It identifies a receipt requirement for a stated functional; it is not promoted as physical winding. The burden coefficient and complete apparatus cost remain unsourced.

## Fine events active receipts and nulls

This development model supplies an explicit graph for the one-pair alphabet of manuscript Appendix D.12; it is not a native admission law (the accompanying exact replay). Let $\theta\in\{0,1\}^3$ and $g\in S_3$ act by permuting the three pair addresses. A primitive action has $\xi=0$ or $e_a$, $a\in\{0,1,2\}$, and updates

\[
\theta'=P_g\theta\oplus\xi.
\]

All these actions are admitted in this reference graph. There are eight vertices and $8\cdot6\cdot4=192$ action-distinct directed edges, including loops and parallel edges. This count is not an identification with the different $S_4\times\Theta$ product counted in manuscript §2.2. Repeated action choices define the fine-history space. Eligibility gates, geometry changes, control sources and resource exhaustion are not supplied by this declaration.

For an edge other than $(g,\xi)=(1,0)$, record

\[
\rho(e)=(w,w',a,\epsilon),\quad
w=|\theta|,\quad w'=|\theta'|,\quad\epsilon=\operatorname{parity}(g),
\]

using $a=\varnothing$ when $\xi=0$. Record the identity/no-flip action as a distinct null symbol $\bot$. This gives 44 active receipt labels plus one null, not 44 total labels. The active receipt fibers have sizes 2, 3, 6 and 9 with multiplicities 2, 26, 14 and 2; the null fiber has eight edges. Counts refer to varying fine initial states as well as controls. They are not probabilities without a measure.

For any fixed $\theta$ of incoming weight $w$, every active receipt with that weight can be realized by some admitted action. For weights 1 and 2, the three even permutations and the three odd permutations each move the exceptional bit to every address. Weights 0 and 3 are fixed by all permutations. Thus every weight-compatible active receipt word lifts to a path from every initial configuration of its first weight in this all-open graph. The 400-pair count in manuscript Appendix D.12 is consequently attained at this coarse level here; more restrictive native gates could reduce it. A null retains the state and does not remove the need for weight compatibility across it.

## Complete kernels and stationary preference

For each weight choose probabilities $b_w,d_w\ge0$ with $b_w+d_w\le1$, $b_3=d_0=0$, and put $h_w=1-b_w-d_w$. Draw $g$ uniformly from $S_3$. With $y=P_g\theta$, define the complete action kernel

\[
K(g,\xi\mid\theta)=\frac16
\begin{cases}
h_w,&\xi=0,\\
b_w/(3-w),&\xi=e_a,\ y_a=0,\\
d_w/w,&\xi=e_a,\ y_a=1.
\end{cases}
\]

Only existing zero or one bits enter the respective branches; the boundary cases have zero total probability and no division by zero. Summing all actions gives one. Each initial state of weight $w$ has the same next-weight law

\[
Q_{w,w+1}=b_w,\quad Q_{w,w-1}=d_w,\quad Q_{w,w}=h_w.
\]

The null probability is $h_w/6$. It differs from the no-flip probability $h_w$ and from the probability that the Boolean endpoint is unchanged: $h_w/\binom3w$. Frame actions can occur without changing that endpoint. One model tick is supplied; no physical waiting-time distribution or clock calibration is derived.

For the reference choice $h_w=1/4$, $b_w=(3-w)/4$ and $d_w=w/4$, all 24 controls have probability $1/24$. The coarse matrix and stationary row vector are

\[
Q=\frac14\begin{pmatrix}1&3&0&0\\1&1&2&0\\0&2&1&1\\0&0&3&1\end{pmatrix},
\qquad \pi=\frac18(1,3,3,1),
\]

with eigenvalues $1,1/2,0,-1/2$. This is a prepared classical stochastic model, distinct from the coherent skew flow.

There is no symmetry-selected stationary preference in this family. Given any strictly positive probability vector $\widetilde\pi$, choose positive adjacent fluxes $J_0,J_1,J_2$ small enough that $J_{w-1}+J_w<\widetilde\pi_w$, with $J_{-1}=J_3=0$, and set

\[
b_w=J_w/\widetilde\pi_w,\qquad
d_w=J_{w-1}/\widetilde\pi_w.
\]

These probabilities give detailed balance $\widetilde\pi_w b_w=\widetilde\pi_{w+1}d_{w+1}$ and positive holding probabilities. The fine stationary distribution is $\widetilde\pi_{|\theta|}/\binom3{|\theta|}$, since the uniform frame draw makes the endpoint uniform within each outgoing weight orbit. Thus the same all-open graph and permutation symmetry admit every positive coarse stationary law. The construction proves nonselection; it does not recommend these freely chosen rates as native UD dynamics.

## A conditional scalar no loop theorem

An additive integer or real edge functional is additional data. A useful restricted class can nevertheless be characterized. Let $f(\theta,g)$ be its increment for a frame move and $t(\theta,a)$ its increment for a single flip. Assume:

1. Frame composition obeys $f(\theta,hg)=f(\theta,g)+f(P_g\theta,h)$.
2. Both increments are scalars invariant under simultaneous relabeling: $f(P_k\theta,kgk^{-1})=f(\theta,g)$ and $t(P_k\theta,k(a))=t(\theta,a)$ for every $k\in S_3$.
3. Flip reversal changes the sign: $t(\theta\oplus e_a,a)=-t(\theta,a)$.
4. A composite frame-then-flip action has increment $f(\theta,g)+t(P_g\theta,a)$; no extra composite increment is introduced.

Then there is a function $F$ of Hamming weight such that every history has total increment

\[
W(\gamma)=F(w_{\mathrm{final}})-F(w_{\mathrm{initial}}).
\]

In particular every closed history has zero increment. These hypotheses define the class being excluded from nontrivial scalar loop winding; they are not established premises for every possible UD winding law.

To prove the frame statement, define $m(\theta)=\frac16\sum_g f(\theta,g)$. The composition identity gives $m(P_h\theta)=m(\theta)-f(\theta,h)$, while scalar relabeling invariance gives $m(P_h\theta)=m(\theta)$. Hence $f=0$. Upward flip edges have three relabeling orbits, indexed by incoming weights 0, 1 and 2. Call their increments $a_0,a_1,a_2$; reversal fixes the downward increments. Set $F(0)=0$ and $F(w)=\sum_{j<w}a_j$. Each elementary increment is the difference of this potential, and the composite rule preserves it. Summing telescopes. There are exactly three free parameters, with integer parameters for integer increments. The finite certificate independently verifies rank 69 for 462 constraints on 72 frame/flip values, leaving precisely this three-dimensional space (the accompanying exact replay).

## A graph cycle diagnostic and finite record size

To test receipt sufficiency outside that restricted class, declare a different edge functional. At $\theta=000$, assign $+1$ to the no-flip frame action $c=(012)$ and $-1$ to $c^{-1}$; assign zero to other edges. This functional is antisymmetric under edge reversal, but deliberately fails the frame-composition identity and full $S_3$ scalar covariance. It is a chosen graph-cycle counter, not a derived physical winding. Treating different frame words as the same group action would invalidate this choice.

Both nonzero actions begin and end at 000 and emit the same active receipt $r=(0,0,\varnothing,0)$. For the word $r^N$, the possible totals are

\[
W_N\in\{-N,-N+2,\ldots,N\}.
\]

All $N+1$ values occur. Even when the initial and final Boolean states, full receipt word and length $N$ are known, exact recovery of total $W_N$ therefore requires a supplement with at least $N+1$ distinct values. A fixed-length binary supplement needs

\[
B_{\min}=\left\lceil\log_2(N+1)\right\rceil
\]

bits; emitting $W_N$ attains the cardinality bound. This is aggregate recovery, not recovery of the full frame history. Under the reference kernel, conditional on this word, the two actions are equiprobable independently, giving binomial probabilities for these totals. The word itself has probability $(1/12)^N$ from initial 000. The support bound is a worst-case exact requirement, not an assertion about average cost.

If a receiver, supplied with the known incoming weight, merges the null action with $r$, the same code word instead hides increments $-1,0,+1$. It then permits every total from $-N$ to $N$, requiring $2N+1$ supplemental values and $\lceil\log_2(2N+1)\rceil$ fixed-length bits. This is a separate 44-code observation that conflates nulls with active events. It is not the 44-active-plus-null contract above. The unflagged word can be reconstructed from the flagged word and initial weight by carrying the weight across nulls; the two standalone symbol maps are not globally ordered because $\bot$ alone omits that weight. Exact winding over unbounded horizons cannot fit into a fixed finite supplemental alphabet under either observation.

For a supplied burden $B(n)=\kappa_B n^2$, known initial counter $n_0$ and recovered total $W_N$ suffice to compute

\[
\Delta B=\kappa_B(2n_0W_N+W_N^2).
\]

This is a sufficient receipt for the signed stock change, not necessarily a minimal one for that change alone; different windings can give the same value. The counter is distinct from the orientation sign called $n_{\mathrm{seam}\to\mathrm{chain}}$ in the source ledger. Neither $\kappa_B$, physical winding, readout acquisition, work, renewal cost nor a boundary-area density is derived. The capacity bounds are conditional on the receipt word and its known length; those side-information resources cannot be omitted from an apparatus ledger. The result identifies what a specified history functional needs recorded before a resource comparison can be completed.


## Source and verification boundaries

The immediate baseline is `UD_Theory_Narrative_Manuscript_v0.10.md`, read at version 2 under its existing manuscript identity. The current source boundary is its conditional update `Theta+ = P_g Theta- xor xi`; restricting xi to zero or one addressed flip and admitting every such action are declared development choices. They are not the native output-selector, hard gate or clock law. The matching action uses S3, the quotient action of S4 on three pair addresses; no claim is made that it retains every vertex-frame distinction.

The supplied coefficient ledger v0.39 retains G05 and physical action normalization as source-open. Its phase quantities Q81-Q84 are conditional transport variables; Q82's orientation sign is not the unbounded history counter defined here. The supplied CRL-2 governance proposal keeps development and registry promotion separate. Its instructions do not convert constructor checking into non-constructor review. The two legacy files named `carrier_definition.md` and `seam_phase_transport.md` contain placeholder text; they were inspected and do not substantiate a new winding law. The unavailable genesis PNG was not used.

Run `python3 verify_history_receipts.py` with Python 3 and SymPy. It constructs the graph and both receipt contracts; verifies support, null fibers, normalized kernels, a second stationary law and all reference coarse eigenvalues; checks edge-reversal antisymmetry of the counterexample; enumerates exact hidden-winding distributions through length 12; and certifies all scalar/frame/flip linear constraints. `SCALAR_WINDING_CERTIFICATE.json` contains the full integer constraint matrix and three-column basis. The proof above, rather than a bounded enumeration alone, establishes the general statements for every finite horizon and every positive target law.

This is not a validation of all historic source results. No imported source script is executed. The prior v0.10 release remains pinned in the source register; the four-paper baseline and all input ledger/governance bytes are unchanged. Physical promotion stays 0.

## What is now closed and what comes next

Closed within the declared model: a composable fine-history graph, complete normalized reference kernel, a symbolic family proving nonselection of stationary preference, the scalar no-loop theorem, explicit receipt collisions outside that theorem's class, and sharp aggregate supplemental-symbol requirements on the specified words. The observed null distinction is part of the receipt, not a free convention that may be forgotten without changing the result.

Open: a native admission mask, source-selected probabilities, actual waiting-time or clock law, a physically justified additive history functional and its covariance/transport rule, the burden scale, and acquisition/renewal/energy costs. The next positive source task is to specify the additional orientation, phase, context or reservoir state and derive its transported increment, rather than assigning an integer counter from a numerical target. An orientation-sensitive quantity must have a consistent transport rule across frame changes; replacing scalar covariance alone does not settle that obligation. The same receipt-fiber test can then be rerun on the enriched state.

This development package is integrated into narrative candidate v0.11, sections 2.4 and 9.5 and Appendix D.13, with a narrowed source-boundary statement in section 13.1. The isolated finite results are review candidates; no independent review or physical correspondence is asserted.
