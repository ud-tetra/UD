# UD native-current address probe and blind-mode audit v0.1

**Date:** 10 October 2026 UTC. **Physical promotion:** 0. Constructor verification only; no independent review.

## Source and proposed observer

Ledger Q167 supplies the gated vertex–edge support current

\[
J_{ie}^{S}=2h_eD_{ie}x_i y_e,
\]

while Q173 supplies the gated directed face–cell current \(J_{f\tau}^{23}=2h_f B_{3,f\tau} f_f u_\tau\). Neither selects a gate transition or a prospective event address. The preceding [symmetry audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-09T231756Z-codex-symmetry-trigger-2f7d5b31) showed why a one-edge event needs a symmetry-breaking input at a symmetric state.

Here we test a **candidate** address observer derived algebraically from Q167's current form. Define the counterfactual ungated value \(J^0_{ie}=2D_{ie}x_i y_e\), even at \(h_e=0\), and the edge score

\[
s_e=\sum_{i\in e}(J^0_{ie})^2=4y_e^2(x_a^2+x_b^2),\quad e=(a,b).
\]

Return the unique edge with positive maximal \(s_e\); return the set of tied maxima; return no address if every score is zero. Squaring and summing endpoint currents makes the score invariant under edge orientation reversal and covariant under simultaneous vertex/edge relabeling. **Evaluating \(J^0\) behind a closed hard gate and using argmax as a trigger are added observer semantics.** They are not Q167's actual gated current or a sourced mask law.

On an asymmetric exact fixture \(x_a=1,x_b=2,y_{ab}=3\), all other edge amplitudes zero, \(s_{ab}=4\cdot9(1+4)=180\) and every other score is zero. All nine target edges and all 12 carrier automorphisms give **108/108** typed-address covariance cases. The candidate can therefore supply an address when the prepared amplitudes distinguish an edge. If the selector instead observes only actual gated current, \(h_e=0\) makes that channel identically zero: reopening from its own gated current is circular unless another input is declared.

## Exact active blind orbit

Use the source-native \(A=B^T-B\) on \(K=\langle0123,0124\rangle\), with both face–cell incidences present. In ascending bases,

\[
B_3^TB_3=\begin{pmatrix}4&1\\1&4\end{pmatrix},\qquad
e=(1,-1)^T,\qquad B_3^TB_3e=3e.
\]

Choose the exact initial state \(x=0,y=0,f=B_3e,u=e\). Since \(B_2B_3=0\), the face–cell subspace \(x=y=0,\ f\in\operatorname{im}B_3\) is invariant under the full native generator. All nine Q167 currents and proposed scores remain **zero for all native evolution time**. The state is active: \(f'=-B_3e\ne0\), \(u'=3e\ne0\). Its cell mode has frequency \(\sqrt3\) in the dimensionless native evolution parameter.

The shared face 012 has \((B_3e)_{012}=0\). At the displayed initial state its two directed Q173 face–cell currents are zero; each of the six private directed currents is exactly \(+2\). Thus the native face readout detects activity, but these six values are tied and do not choose one private face. This is a prepared exact invariant orbit, not a claim that every UD state is blind. Nonuniform face gating can break this subspace and requires its own analysis.

## Disposition

- **EXACT:** the 23-coordinate native chain identities, \(B_2B_3=0\), the active blind invariant subspace, the shared-face zero, and the six private \(+2\) directed currents.
- **EXACT CONDITIONAL:** the score's covariance and unique selection on a supplied asymmetric input.
- **NO-GO for universality:** vertex–edge current activity alone cannot assign a local edge on every active native orbit; gated current alone cannot reopen a closed edge through a rule requiring its own nonzero gated signal.
- **OPEN:** source admission of an ungated probe, any causal detector/threshold, factor updates, face/edge event relation and timing. Physical promotion remains 0.

The next source contract must identify the pre-event observable that carries an address even on active edge-current-blind sectors, or explicitly restrict event eligibility there. A combined vertex–edge and face–cell observer still needs a lawful typed mapping from a detected face set to a particular edge/factor update, with tie handling and relabeling covariance. The current score is a candidate discriminator, not a predictive gate law.

Run `python3 verify.py` in the release directory. Standard-library rational arithmetic records **16 passed assertions** in `results.json`, including all 108 covariance fixtures and the exact chain identities. The all-time blindness follows from invariant-subspace algebra, not sampling a time grid.
