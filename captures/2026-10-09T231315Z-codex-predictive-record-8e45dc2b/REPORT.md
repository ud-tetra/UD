# UD predictive mask record: quotient and factor-memory audit v0.1

**Date:** 9 October 2026 UTC. **Physical promotion:** 0. **Review:** constructor checks only; independent review pending.

## Source boundary

The admitted hard edge decision is \(h_e=C_eT_e\), with \(C_e\) the conjunction of the closure receipts required by a declared context and \(T_e\) the lawful transport predicate (ledger Q156). Q167 supplies an edge-mask support current and Q173 supplies a face-mask support current. Their mask states/effects do not constitute primitive event laws for \(C_e,T_e\) or for independent Q173 face masks. This distinction is explicit in `UD_HARD_GATE_UPDATE_LAW_SOURCE_DERIVATION_v0.1.md` and `HARD_GATE_TRANSITION_TRIGGER_AND_SOFT_MARGIN_SOURCE_AUDIT_v0.1.md`, inspected in the previous capture. The preceding [hard-mask decision audit](https://github.com/ud-tetra/UD/tree/main/captures/2026-10-09T183221Z-codex-hard-mask-72ae8f01) verifies the structural selector, with its chosen context and candidate face lift labeled separately.

This continuation asks a narrower question: **what must a compact record retain if a future event law is supplied?** It does not assert such a law has been sourced.

## Exact amplitude quotient

On the two-tetrahedron carrier \(\langle0123,0124\rangle\), let \(c\in\mathbb R^{23}\) contain 5 vertices, 9 edges, 7 faces and 2 cells. Let \(n\) be 1 on all five vertices and 0 elsewhere. Define

\[
z=Pc=(c_0-c_4,c_1-c_4,c_2-c_4,c_3-c_4;\ c_E,c_F,c_T)\in\mathbb R^{22}.
\]

For every whole-edge vertex–edge mask and every per-face face–cell mask, retain the fixed edge–face incidences and use the skew incidence generator \(A_{e,f}\). The two endpoint signs of a masked edge cancel on \(n\). All other incidence blocks leave \(n\) untouched. Hence \(A_{e,f}n=0\), and \(\ker P=\operatorname{span}\{n\}\). Therefore there exists a unique \(22\times22\) matrix \(H_{e,f}\) satisfying

\[
\boxed{PA_{e,f}=H_{e,f}P.}
\]

One explicit construction is \(H_{e,f}=PA_{e,f}L\), where \(L\) sets the vertex-4 gauge coordinate to zero and \(PL=I_{22}\). Thus, **given a mask history**, \(\dot z=H_{e,f}z\) on each fixed-mode interval; a pure mask change with continuous amplitude retains \(z^+=z^-\). A separate amplitude impulse would require its own sourced reset. This is algebraic closure under prescribed switches, without a prediction of event times. The prior typed-mask capture established the 22-dimensional minimum for its selected observations and mask family; this audit supplies a simple coordinate chart for the same one-dimensional quotient.

The replay tests all 512 edge masks paired with a declared complete-boundary face lift, checks 16 independent mask generators (nine edge, seven face), verifies a right inverse for \(P\), and checks an exact intertwining witness. The generator proof, rather than a 65,536-case enumeration, covers all independent binary edge and face assignments by linearity. The Boolean factor test below is separate.

## Conditional minimum factor memory

The hard edge bit \(h=CT\) has four possible underlying Boolean states:

| \((C,T)\) | \(h\) | Interpretation |
| --- | ---: | --- |
| \((1,1)\) | 1 | Both predicates pass |
| \((0,1)\) | 0 | Closure fails |
| \((1,0)\) | 0 | Transport fails |
| \((0,0)\) | 0 | Both fail |

For a **declared diagnostic event alphabet** `repair_C`, `repair_T`, `fail_C`, `fail_T`, each event sets only its named factor and preserves the other. These are hypothetical typed updates, not admitted primitive UD events. The four factor states have distinct output signatures under the current gate observation and one such event. For example, starting from the same closed \(h=0\), `repair_C` opens \((0,1)\) but leaves \((0,0)\) closed. Consequently any deterministic event-response record valid for this whole alphabet must distinguish four states: at least **two binary state bits per independently repairable edge**, or an equivalent four-state symbol. This is conditional on that event alphabet. It does not establish a universal UD state dimension or independence among nine edges.

At the same \(z\), the same pre-event mask and the same `repair_C` event, take the two pre-factor states \((0,1)\) and \((0,0)\) on edge 01. With the candidate AND face lift, the next edge mask is respectively 1 or 0; at the test amplitude \(e_0+e_{01}+e_{012}+e_{0123}\), the next edge-01 derivative is respectively \(-2\) or \(-1\). Thus \((z,h)\) is not a deterministic predictive record for that declared update grammar. Even \((z,C,T)\) only becomes predictive when an update law supplies the next factors; if \(C\) is an AND of multiple receipts, primitive receipt updates may require more underlying state.

Q173's seven face masks can be independently prescribed in its verification family. A face decision from three edge gates was used only as a **candidate** in the explicit two-branch witness. It must not be counted as a sourced face-event law. The SER vertex–cell scheduling graph likewise has a different type from these geometric edge/face gates; identifying them requires a separate typed bridge.

## Replay and disposition

Run `python3 verify.py` in this release directory. Standard-library rational arithmetic produces `results.json`. **15 named assertions pass.** They are constructor verification, not independent replication.

- **EXACT / CONDITIONAL:** \(22\)-coordinate amplitude quotient under supplied whole-edge and face masks; four factor states distinguishable under the declared independent repair/failure event alphabet.
- **NO-GO for the declared grammar:** gate bit \(h\) alone cannot predict all one-event responses.
- **OPEN in UD source:** event carrier, update order and laws for closure receipts and transport maps, independent Q173 face decisions, switch eligibility/timing, and any amplitude reset.

The next source-complete contract must specify a typed primitive event \(E_n\), an explicit update \((r_n^{\rm cl},U_n,E_n)\mapsto(r_{n+1}^{\rm cl},U_{n+1})\) or an equivalent factor law, and its relation to face masks. It should prove relabeling covariance and null behavior, issue pre/post cause receipts, and then test whether the augmented record closes and what its actual minimum size is. Event index is not physical time.
