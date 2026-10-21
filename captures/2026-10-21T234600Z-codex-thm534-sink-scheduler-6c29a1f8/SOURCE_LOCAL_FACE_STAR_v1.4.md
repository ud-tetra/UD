# THM-534 local face-star events and event-order audit, v1.4

October 21, 2026. EXACT CONDITIONAL local support events; CANDIDATE event granularity; native admission and scheduling OPEN. Development, no registry entry. Physical promotion 0. Outside peer review pending. Local propositions L1–L5 are not new global theorem numbers.

## Source reconciliation

Main checked at `f0a2ee841cb0feed3ec5e700bfc0a6521cbda2f4`. The research branch advanced to `ce9a482979c09469baa1c549fd48a073d6f4492b`, with `THM534_GLUED_FACE_CONTACT_RESET_v1.2.md`. That document supplies an explicit two-cell face/core candidate, exact midpoint receipts, and a conditional reset witness while leaving native contact admission open.

Its gate family has **eight individual face–cell incidence contacts** on Kminus, rather than the previous seven global face bits that shared the same permission on both sides. These are different declared families. The new incidence family does not falsify the preceding diagonal shared-face permission and locality theorems. It changes a hypothesis. No claim is made that Q173 uniquely selects incidence-specific gating.

This audit uses the admitted support bilinear and ownership definitions in ledger Q169–Q173/Q177–Q179, and investigates exact local restrictions of the research branch's declared generator. It does not require transport-masked operators themselves to remain a chain complex. The fixed topological boundary identities remain intact.

## Coordinates and contact convention

Use cells tau0=[0123] and tau1=−[0124], with unique face order 012,013,014,023,024,123,124. Write z for the seven real face amplitudes and t for the two real cell amplitudes. Let D=B3 in those signed cell bases. Its shared-face row is

\[
D_{012,:}=(-1,+1).
\]

For contact mask H, put M=D elementwise-multiplied by H. The face/core support generator is

\[
A_H=\begin{pmatrix}0&-M\\M^{\mathsf T}&0\end{pmatrix}.
\]

Use the existing dimensionless protocol step epsilon=1/4. It is an integration/event convention, not physical time or a source-derived universal coefficient. Contact updates, joint face-star updates, and global masked updates are distinct choices of primitive event unless their equivalence is established.

## L1 — Exact local face-star update

Fix one face f. During one event, hold all contacts on other faces off. Write c_tau=D_(f,tau) h_(f,tau), where a zero coefficient also represents a cell not incident to f. Put

\[
m=\sum_\tau c_\tau^2,\qquad s=\epsilon/2.
\]

The Cayley event has the explicit form

\[
z_f'=\frac{(1-ms^2)z_f-2s\sum_\tau c_\tau t_\tau}{1+ms^2},
\]

\[
t_\tau'=t_\tau+s c_\tau(z_f+z_f').
\]

Every other coordinate is unchanged. Thus the event is local to this face and its admitted incident cells, and preserves

\[
z_f^2+\sum_\tau t_\tau^2.
\]

**Proof.** The midpoint equations are z_f'−z_f=−epsilon sum(c_tau t_tau^mid), and t_tau'−t_tau=epsilon c_tau z_f^mid. Eliminate the cell midpoints to obtain the first formula and then the second. Equivalently this is the Cayley transform of the restricted real skew matrix, so it is orthogonal. Since \(1+m s^2>0\), the update is defined for every finite real epsilon. QED.

No global inverse is needed beyond this local scalar denominator. When m=0 the update is the identity. For m>0, only the cell-amplitude direction parallel to c couples to the face; every perpendicular cell direction is fixed. The nonzero skew frequencies are plus/minus i sqrt(m), entirely determined by the retained unit incidences. No physical frequency or mass follows.

This formula is an exact restriction of the declared generator. An arbitrary product of such events is not thereby identical to one global Cayley step containing every face contact simultaneously.

## L2 — Local receipts, shared ownership, and symmetry

For this completed event define

\[
J_{f\tau}=2\epsilon c_\tau z_f^{\mathrm{mid}}t_\tau^{\mathrm{mid}}.
\]

Then

\[
\Delta z_f^2=-\sum_\tau J_{f\tau},\qquad
\Delta t_\tau^2=J_{f\tau}.
\]

With frozen equal-top-star ownership w_(f,tau), the owned cell support changes by

\[
\Delta S_\tau^{\mathrm{owned}}
=J_{f\tau}-w_{f\tau}\sum_{\tau'}J_{f\tau'}.
\]

**Proof.** Apply the squared-amplitude midpoint identity to L1, then distribute the face stock through its declared ownership weights. The weights sum to one, so the sum of owned changes is zero. QED.

On a shared face w=1/2 in each cell. An owned-support change at a cell with disabled contact is accounting for a change in a jointly owned interface; it is not transport through that disabled contact.

The star generator and update are covariant under signed relabeling of the oriented face and cell bases, with their masks relabeled. A shared face with both contacts equally admitted has an update invariant under the exchange of its two cells after the cell-basis signs are handled. This does not select which star is admitted next.

The verifier independently checks all 256 masks of the full nine-coordinate declared face/core model for support conservation and every face, core and owned-support receipt. It checks 28 sparse-form controls and all 12 signed automorphisms of Kminus on the symmetric joint-star event. Finite controls support the algebraic proofs; they do not establish a native scheduling law.

## L3 — Exact event-order witness

Use a new symmetric preparation: only shared face 012 has amplitude 1, and every cell and private-face amplitude is zero. Its total support is 1. This is **not** the asymmetric support-2 reset preparation in research-branch S52.

For readable comparison use the signed chart

\[
(f,u,v)=(z_{012},-t_{\tau_0},+t_{\tau_1}).
\]

Squared support and ownership do not change under this chart transformation. For one contact and epsilon=1/4, the active plane Cayley rotation has cosine 63/65 and sine 16/65.

Two consecutive single-contact events and one simultaneous two-contact star event give:

| Event definition | f | u | v |
|---|---|---|---|
| Contact tau0, then contact tau1 | 3969/4225 | 1040/4225 | 1008/4225 |
| Contact tau1, then contact tau0 | 3969/4225 | 1008/4225 | 1040/4225 |
| Joint shared-face star | 31/33 | 8/33 | 8/33 |

All three results have squared norm 1 and satisfy the local receipts. The ordered pair-event result has the owned-support contrast

\[
S_{\tau_0}^{\mathrm{owned}}-S_{\tau_1}^{\mathrm{owned}}
=\frac{65536}{17850625},
\]

whereas the reversed order changes its sign and the simultaneous star leaves it zero. The shared-face contribution cancels from this contrast because each cell owns one half.

**Proof.** Multiply the two active-plane rotations in their specified order. For the joint event substitute m=2 and s=1/8 into L1. In the first ordered result the contrast is (1040 squared−1008 squared)/4225 squared, giving the displayed fraction. QED.

The comparison keeps the same per-contact step but changes event grouping and the number of primitive events: it is not a claim that the schedules represent equal calibrated physical durations. Its purpose is to demonstrate that conservation, ownership and unit incidence coefficients alone do not determine the final allocation.

## L4 — Source-selected order is still missing

The initial preparation and equal shared-contact admissions in L3 are invariant under cell exchange. A deterministic, single-valued equivariant selector that chooses exactly one of the two otherwise identical contacts as first cannot be computed from those symmetric inputs alone: exchanging the cells fixes the input but exchanges the two possible outputs.

An ordered contact schedule is therefore an additional input or rule. It can be covariant when relabeled together with the state, as in the seeded research-branch witness, but that is not a derivation of the schedule from symmetric support. Extra memory, a previous asymmetric receipt, boundary data, a stochastic rule, or a joint event can change the hypotheses. No particular choice is established here.

The joint star is one admissible symmetric local event. Symmetry and norm preservation do not uniquely establish Cayley discretization, its step, or joint grouping as the native packet grammar. A different declared norm-preserving symmetric event family could meet those properties.

For distinct face stars with disjoint active coordinate sets, their updates commute exactly, since they act in independent coordinate blocks. Stars sharing a cell need not commute. On Kminus, private faces 013 and 014 give a commuting control, while shared face 012 and private face 013 give a noncommuting control. Thus grouping all contacts of one face removes the within-face order choice but does not eliminate scheduling between overlapping faces.

This identifies a concrete next interface: specify which local face stars may be admitted together and how an overlapping set is resolved. Merely imposing a lexicographic order would be a label convention, not an invariant physical selection.

## L5 — Reconcile the newer source reset and retain its sign

The checker independently reconstructs research-branch S52 without executing its verifier. From z_012=z_013=1 and zero cores, admit only contact (013,tau0) for the first event. This gives t_tau0=16/65. On the next event retain that contact and additionally admit (012,tau0), leaving its neighboring shared contact disabled. Exact midpoint evaluation reproduces

\[
J_{012,\tau_0}=-\frac{61824}{511225},\quad J_{012,\tau_1}=0,
\]

\[
(\Delta S_{\tau_0}^{\mathrm{owned}},\Delta S_{\tau_1}^{\mathrm{owned}})
=\left(-\frac{30912}{511225},+\frac{30912}{511225}\right).
\]

The negative current is cell-to-face under the source convention; reopening does not mean positive ingress. The source correctly labels both the independently admitted seed and the subsequent reset predicate as additional candidate choices. The local-star construction supplies exact arithmetic and accounting for admitted events; it does not provide their native permission source.

## Disposition

Closed mathematically within the declared model: sparse local star formula, norm and midpoint receipts, equal-share ownership, contact-order noncommutativity, signed shared-face symmetry, disjoint-star commutation, and the exact source S52 replay.

Still open: the admission/reset predicate, native event grouping and scheduling of overlapping stars, integration step and physical action/time map, open-system capacity, nondecaying burden transport and matter correspondence. The receipt-only all-contact-dead obstruction remains: no admitted event means no generated receipt to trigger that same receipt-only rule.

This is a local conservative construction with explicit remaining event semantics, not a claim of physical recovery or a new chain-flatness postulate. Original sources and earlier proofs remain unchanged. Physical promotion 0.
