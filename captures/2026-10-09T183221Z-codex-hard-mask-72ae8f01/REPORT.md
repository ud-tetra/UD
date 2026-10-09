# UD hard-mask decision: two-tetrahedron source audit v0.1

**Date:** 9 October 2026 UTC. **Class:** exact conditional mathematics plus a source gap. **Physical promotion:** 0. Constructor audit; no independent review or hardware evidence.

## Sourced decision

UD's edge formation gate is the Boolean product

\[
h_e=C_{{\rm cl},e}^{\rm hard}T_{{\rm int},e}^{\rm hard},\qquad
C_{{\rm cl},e}^{\rm hard}=\prod_{\alpha\in\operatorname{Req}_{\rm cl}(e)}r_\alpha^{\rm cl}.
\]

The closure receipts and the required set are typed by the context of use. Transport integrity means a lawful local transition on the declared state fiber, with required domain, overlap, and reverse-map conditions. Nontrivial loop holonomy alone does not fail this predicate. The hard gate is a veto, not a smooth coefficient. The source also gives an exact cause classification for a supplied pre/post pair of Boolean factors. It explicitly does **not** supply their primitive event update laws. Sources inspected in the user's Library:

- `UD_EDGE_CLOSURE_AND_TRANSPORT_INTEGRITY_HARD_GATE_DERIVATION_v0.1.md`, 21 August 2026, sections II–IV; Library identity `libfile_e9d5b0d7a4bc81918822ae403d527626`.
- `UD_HARD_GATE_UPDATE_LAW_SOURCE_DERIVATION_v0.1.md`, 23 August 2026; `libfile_a80bf50559c88191a8b3b411cb38d93c`.
- `UD_HARD_GATE_BOOLEAN_FACTOR_UPDATE_THEOREM_v0.1.md`, 23 August 2026; `libfile_10b3069a88a48191bd7190f02f91807b`.
- `HARD_GATE_TRANSITION_TRIGGER_AND_SOFT_MARGIN_SOURCE_AUDIT_v0.1.md`, 28 August 2026; `libfile_92f3e465e4008191a62746ef92d52a4c`.
- `UD_DELTA4_FACET_FRAME_EDGE_GATE_TRANSITION_AND_GLOBAL_FACE_VIABILITY_v0.1.md`, 14 September 2026; `libfile_ea2d159c1ba08191b73b4e2473c3004b`. Its complete-boundary face viability is a **candidate** context, not an unconditional Q173 face mask decision.
- `UD_PHASE_AWARE_GATE_TRANSITION_AUDIT_v0.1.md`, 2 October 2026 UTC; `libfile_818d0cf540f881919f9fdb3b326779ea`. Its zero-crossing observer is **candidate** event semantics and is not an admitted hard-mask update.

## Frozen test context

On \(\langle0123,0124\rangle\) there are 5 vertices, 9 edges, 7 faces and 2 cells. We declare \(\operatorname{Req}_{\rm cl}(e)\) to be **all incident triangular face closure receipts** on this carrier. This choice is not universally forced by UD; the source leaves the requirement set to the context. We use real one-dimensional state fibers, and let each edge map be \(U_e\in\{-1,0,1\}\). For this declared reversible/isometric sector, \(T_e=1\) exactly when \(U_e=\pm1\); zero is invalid. The alternative \(U=-1\) is legitimate even when it produces nontrivial loop holonomy.

For a separate face-mask test we propose the complete-boundary lift \(h_f=\prod_{e\subset f}h_e\), motivated by the source's candidate AND face viability. **This is a new conditional bridge to Q173, not a sourced Q173 switch law.** Edge masks act on both vertex–edge incidences (Q167 extension); face masks act on both face–cell incidences at the shared face (Q173). The intermediate edge–face incidences stay unmasked. All generator entries use exact integer/rational arithmetic and \(A=B^T-B\).

## Replay result

Run `python3 verify.py` from this directory. It writes `results.json`. The constructor ran 14 named checks, including all \(2^7 2^9=65,536\) face-receipt/transport-bit assignments, the 16 Boolean factor transitions, and 12 carrier relabeling automorphisms. All 512 edge masks are reachable because the all-closed-receipt state allows any integrity pattern. Under the **candidate face lift**, 62 of the 128 independent Q173 face masks are reachable, and each face mask is determined by its edge mask. This restriction is an implication of the declared lift, not a restriction supplied by Q173 itself.

| Exact fixture | Result |
| --- | --- |
| All required receipts present, \(U_e=1\) | All edge and face gates open; no structural switch along the fixed-topology amplitude orbit |
| \(U_{01}=-1\), other maps identity | All edges open although the 012 loop has holonomy \(-1\) |
| \(U_{01}:1\to0\), receipts unchanged | Edge 01 closes; candidate face lift closes 012, 013, 014 |
| At the same amplitude \(c=e_0+e_{01}+e_{012}+e_{0123}\) | \(\dot c_{0123}=-1\) with \(U_{01}=1\), and \(0\) with \(U_{01}=0\) |
| At the same amplitude, edge 01 component | \(\dot c_{01}=-2\) and \(-1\), respectively |

The two configurations in the last rows have the **same full chain amplitude**, hence exactly the same 22-dimensional compact record \(R_{22}c\), but different supplied transport maps and different derivatives. If the transport map is omitted, even the full amplitude does not identify which derivative to use. This is a direct nonidentifiability witness for an autonomous switch predictor based only on the existing compact amplitude record. The test does not assert both maps arise on one admitted UD trajectory; the missing transition law is precisely what would decide that.

## Decision and next source gate

**PASS:** the sourced Boolean rule decides the current hard edge mask from complete closure and transport predicate inputs and exactly tags a supplied transition. **CONDITIONAL:** the declared incident-face context and face AND lift can propagate a supplied edge switch through this two-tetrahedron generator. **NO-GO for autonomous prediction:** no sourced map currently updates \(r_\alpha^{\rm cl}\) and \(U_e\), or directly updates \(C_e,T_e\), from the primitive packet state and event. The all-open static carrier provides no amplitude-triggered switches. A postulated amplitude threshold would change the model and cannot be counted as sourced.

The smallest concrete next source contract is an event map \(\mathcal E:(c_n,\text{typed closure/transport state},E_n)\mapsto(r_{n+1}^{\rm cl},U_{n+1})\), or a factor-level equivalent, with exact domain and update order, typed face relation, relabeling covariance, null behavior and receipts. Then replay candidate switch times against the fixed generator and the 22-coordinate record. If the selector needs additional state, include that state in the predictive record and recompute its closure/minimal size. Physical time remains distinct from event index.

No claim of physical force unification, hardware validation or threshold theorem follows from this audit.
