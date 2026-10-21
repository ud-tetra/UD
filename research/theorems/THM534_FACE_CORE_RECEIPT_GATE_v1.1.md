# THM-534 v1.1 — Face–Cell Receipt-Driven Boundary Events and Edge-Gate Recovery

**Date:** 2026-10-21 · **State:** EXACT source-bound continuity / EXACT CONDITIONAL finite state model / scoped NO-GO / native closure selection OPEN · **Lane:** development; no registry promotion · **Physical promotion: 0**.  
**Parent:** `THM534_SUPPORT_READINESS_GATE_v1.0.md` (S35–S41), `THM534_AUTONOMOUS_GATE_RESERVOIR_v0.9.md` (S29–S34). **Authoritative source-stratum:** `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md`, specifically Q156, Q162, Q169–Q173 and Q177–Q179. **Historical THM-534 six-edge Markov probabilities remain SOURCE-BLOCKED.** This is target-exposed mathematical exploration, not a target-blind confirmation.

## Typed carrier, dependencies, source limitations

Let \(K=\Delta^3\), with oriented vertices 0,1,2,3; unoriented edge readout order \((01,02,03,12,13,23)\); oriented face order \((012,013,023,123)\); and positively oriented cell \([0123]\). Signed boundary \(B_1:\mathbb R^6\to\mathbb R^4\), \(B_2:\mathbb R^4\to\mathbb R^6\), and \(B_3:\mathbb R\to\mathbb R^4\) obey \(B_1B_2=B_2B_3=0\). Set \(d=B_3=(-1,1,-1,1)^\mathsf T\).

**Distinct dynamical carriers:** \(z_n\in C_2=\mathbb R^4\) is *face support amplitude*, \(t_n\in C_3=\mathbb R\) is *cell support amplitude*. Their squared amplitudes \(S_{f,n}=z_{f,n}^2\) and \(S_{\tau,n}=t_n^2\) are the frozen Q172 and Q171 support stock definitions. Separately, \(\rho_n\in\mathbb R_{\ge0}^4\) is dimensionless **vertex burden** and \(r_n\in\mathbb R_{\ge0}^4\) is the distinct v0.9 candidate vertex reservoir; neither is identified with a Q172 face interface reservoir, physical mass-energy, or the v1.0 \(C_0\oplus C_1\) reversible support norm.

**Upstream earned facts:** Q171 fixes \(J_{23,f}=2(B_3)_f z_ft\) as an infinitesimal support throughput and \(\dot S_\tau=\sum_fJ_{23,f}\). Q172 fixes the face continuity \(\dot S_f=\sum_eJ_{12,e f}-J_{23,f}\). Q173 permits a separate hard face-to-cell gate \(h_f^{23}\) multiplying that throughput. The source **does not specify** a unique rule identifying face current sign with \(\chi\) geometric closure or \(b\) boundary permission; it also does not force the two degrees' gates to be equal.

**Declared source-first candidate branch:** keep face-to-cell contacts admissible, \(h_f^{23}=1\), while suppressing edge-to-face support ingress, \(J_{12}=0\), in this isolated finite subsystem. This is an independent higher-degree transport path even if *all six edge burden gates are off*. Apply the real skew generator and fixed dimensionless Cayley step \(\varepsilon=1/4\):

\[
A_{23}=\begin{pmatrix}0_{4\times4}&-d\\d^\mathsf T&0\end{pmatrix},\quad
\binom{z_{n+1}}{t_{n+1}}=
\left(I-\tfrac{\varepsilon}{2}A_{23}\right)^{-1}
\left(I+\tfrac{\varepsilon}{2}A_{23}\right)\binom{z_n}{t_n}.
\]

Here \(\varepsilon=1/4\) is an explicit internal event-step convention, not physical time or a unique action coefficient. This is an exact finite model **conditioned** on the choice of an unmasked higher-degree support channel.

## THM-534-S42 — Exact finite face/cell transfer and support conservation (EXACT CONDITIONAL)

Let \(m_n=(z_n+z_{n+1})/2\), \(u_n=(t_n+t_{n+1})/2\), and define the **actual finite-event** face-to-cell receipt
\[
\mathcal J^{23}_{f,n}=2\varepsilon\,d_f(m_n)_f u_n.
\]
Then, at every finite step,
\[
\boxed{S_{f,n+1}-S_{f,n}=-\mathcal J^{23}_{f,n},\qquad
S_{\tau,n+1}-S_{\tau,n}=\sum_f\mathcal J^{23}_{f,n}.}
\]
Hence \(\sum_f S_{f,n}+S_{\tau,n}=\|z_n\|^2+t_n^2\) is exactly conserved. **Proof.** Cayley is orthogonal for real skew \(A_{23}\), and the midpoint identity \(b^2-a^2=2\tfrac{a+b}{2}(b-a)\), with \(\Delta z=-\varepsilon d\,u_n\), \(\Delta t=\varepsilon d^\mathsf Tm_n\), gives each local receipt. No unaccounted face sink or core source is introduced. QED.

**Timing/firewall:** The pre-event bilinear \(2d_fz_{f,n}t_n\) need *not* have the same sign as the finite-step net receipt; a valid binary **event** readout must use \(\mathcal J^{23}_{f,n}\) or explicitly be labeled prospective, not silently equated to the executed update.

## THM-534-S43 — Exact source-driven binary projection is a candidate, not a uniqueness result (EXACT CONDITIONAL / OPEN)

Given the completed step's typed receipts, propose binary **readouts for the next event**:
\[
\chi^{\mathrm{in}}_{n+1}:=\mathbf1\!\left[\sum_f\mathcal J^{23}_{f,n}>0\right],\quad
b^{\mathrm{in}}_{f,n+1}:=\mathbf1[\mathcal J^{23}_{f,n}>0],
\]
\[
\boxed{h^{01}_{e,n+1}=\tau_e^{\rm ctl}\,\chi^{\mathrm{in}}_{n+1}
\prod_{f\supset e} b^{\mathrm{in}}_{f,n+1},\qquad \tau_e^{\rm ctl}=1.}
\]
Each tetrahedron edge is incident to exactly two triangular faces. The strict positive tie rule and the logical **AND** across both incident faces are **explicit candidate constitutive choices**. The source equations alone also allow the opposite sign, a non-strict tie or an **OR** incident-face rule; these select different masks while preserving S42. For the first actual positive-transfer event, the face-status vector is `0111`: the declared **AND** projection gives edge mask `001011` and nonzero Q162 face circulation, while the equally permutation-equivariant **OR** of the two incident-face bits opens all six edges and produces zero Q162 circulation from a pure burden gradient. Thus Q171–Q173 + Q156 do **not** uniquely derive actual \(\chi^{\mathrm{geom}}\) closure or \(b\) boundary admissibility. These readout bits denote **positive ingress-event status**, not the existence or topological closure of the cell itself. QED as a nonuniqueness countermodel.

**Event order:** start with a declared initial edge mask \(h^{01}_0=0\). During event n, compute the Q162 burden attempt using \(h^{01}_n\); independently execute the higher face–cell Cayley attempt, record **actual midpoint** face/core transfers, then select \(h^{01}_{n+1}\). There is a one-event delay from face receipt to next edge permission. Higher-degree contact \(h_f^{23}=1\) is not \(b^{\mathrm{in}}_{f}\); the latter gates subsequent **edge burden** access only.

## THM-534-S44 — Exact all-edge-off opening, closing and re-entry witness (EXACT CONDITIONAL)

Fix the initial state (all dimensionless)
\[
z_0=(\tfrac12,\tfrac32,-\tfrac12,\tfrac12)^\mathsf T,
\quad t_0=0,\quad h^{01}_{e,0}=0,\quad
\rho_0=(1,0,0,0)^\mathsf T,\quad r_0=(1,1,1,1)^\mathsf T.
\]
Write \(z_0=w+\tfrac12d\) with dark face mode \(w=(1,1,0,0)\), \(d^\mathsf Tw=0\). The exact Cayley evolution has
\[
z_n=w+\tfrac12d\cos(n\vartheta),\quad t_n=\sin(n\vartheta),\quad
\cos\vartheta=\frac{15}{17},\quad\sin\vartheta=\frac8{17}.
\]
The first actual **finite** face-to-cell receipt is
\[
(\mathcal J^{23}_{f,0})_f=\frac1{289}(-18,50,16,16),\quad
\Delta S_{\tau,0}=\frac{64}{289}.
\]
All 14 exact steps in the declared model pass, with the selected edge gate chronology:

| Event n | \(\chi^{\mathrm{in}}_n\) | next-edge boundary status \(b_n^{\mathrm{in}}\) | \(h^{01}_n\) | Meaning (within model only) |
|---|---:|---|---|---|
| 0 | 0 (initial) | 0000 | 000000 | all **edge** gates closed |
| 1 | 1 | 0111 | 001011 | nonuniform reopening from higher-degree support transfer |
| 3 | 1 | 0111 | 001011 | same branch retained |
| 4 | 0 | 0100 | 000000 | closed after negative core net transfer |
| 6 | 0 | 0100 | 000000 | remains edge-off |
| 7 | 1 | 1011 | 010101 | second nonuniform reopening |
| 10 | 1 | 1011 | 010101 | still on under finite-event receipt, unlike instantaneous pre-readout |
| 11 | 0 | 1000 | 000000 | closed again |

At event 1, Q162 edge mixing gives the exact distinct **vertex-burden face circulation**
\[
F^{B}_{1}=B_2^\mathsf Tj^B_1=(0,-3/16,-3/16,0)^\mathsf T\ne0.
\]
At event 7 the new mask \(010101\) also gives nonzero \(F^B_7\). This demonstrates **edge-gate recovery from all edge gates off**, not a geometric tetrahedron disappearance/reappearance, nor recovery from a completely inactive global packet. The dark face mode \(w\) is an intentionally asymmetric initial support input, not spontaneous breaking from an \(S_4\)-invariant state. QED by the exact recurrence/receipts and executable fraction arithmetic.

## THM-534-S45 — Signed \(S_4\) transport covariance (EXACT)

Under any vertex relabeling \(g\in S_4\), let \(Q_2(g)\) act with the **oriented face signs**, and \(Q_3(g)=\operatorname{sgn}(g)\) on the oriented tetrahedral cell. Then \(Q_2d=dQ_3\), so \(A_{23}\) and the Cayley map intertwine with the block-diagonal signed action. The actual face-to-core **support** transfers \(\mathcal J^{23}_f\) transform as *unoriented scalars* under the induced face permutation; therefore the candidate sign predicates and resulting edge masks commute with vertex relabeling. This is an equivariant **conditional** event rule, not spontaneous or physically preferred selection. QED. All 24 permutations, four representative epochs and exact intertwiners passed.

## THM-534-S46 — Two distinct no-recovery obstructions and a nonuniformity control (EXACT / NO-GO)

1. **Global zero support:** if \(z=t=0\) and no independent face/boundary source acts, the skew evolution fixes zero; no bilinear face-to-core current can begin. The candidate cannot recover from the entirely empty face/core support state.
2. **All face gates disabled:** if Q173 hard gates are \(h_f^{23}=0\) for all f, then \(A_{23,H}=0\). Even for \(z\ne0\) and \(t=0\), no support moves, so initially zero candidate event flags cannot create their own opening. In particular, if one **identifies** the face-to-core gate \(h_f^{23}\) with \(\mathbf1[J^{23,\mathrm{pre}}_f>0]\), then \(t_0=0\) makes all face gates off and they remain off. A separate face-to-cell admission, prospective signal, reset/memory or external source is required.
3. **No asymmetry source:** with \(w=0\), every face transfer has the same sign at each event. The sign-and-AND selection generates only **uniform** edge masks, hence \(F^B=B_2^\mathsf T H B_1^\mathsf T\rho/(-4)=0\). Nonuniform circulation requires an independently present face asymmetry or changed rule/carrier.

These no-go statements apply **only under their respective exact hypotheses** and do not obstruct an admitted higher-degree support flux, an asymmetric boundary condition or a different dynamical coupling.

## THM-534-S47 — Dual ledger compatibility and dissipative circulation ceiling (EXACT CONDITIONAL)

For each selected binary \(h_n^{01}\), apply the existing v0.9 **conditional** burden/reservoir update:
\[
j^B_n=-\tfrac14H_nB_1^\mathsf T\rho_n,
\quad p_n=\rho_n+B_1j_n^B,
\quad s_n=(r_n-p_n)/4,
\quad \rho_{n+1}=p_n+s_n,
\quad r_{n+1}=r_n-s_n.
\]
Then \(\rho_n,r_n\ge0\) and \(\mathbf1^\mathsf T(\rho_n+r_n)=5\) in the S44 witness. Independently \(\sum_f z_{f,n}^2+t_n^2=3\). These are **different typed conserved contents** with **no** established conversion to one physical stress-energy. For every state-selected sequence of masks, the exact passive-reservoir no-go v0.9 S31 still applies:
\[
\sum_{n\ge0}\|F^B_n\|^2\le E_0<\infty,\qquad F^B_n\to0.
\]
The periodic higher-degree support *can repeatedly reopen edge gates*, but **does not** sustain asymptotically nonzero Q162 face circulation under the passive burden model. A distinct source-bearing/reversible transport law is still required for persistence. QED.

## THM-534-S48 — Instantaneous/current sign is not the finite-event receipt (EXACT / NO-GO)

For the explicit S44 witness at n=3, the prospective Q171 **instantaneous** total current is
\[
\sum_f 2d_f z_{f,3}t_3=\frac{9\,678\,240}{24\,137\,569}>0,
\]
but the actual core support change under event 3 is
\[
S_{\tau,4}-S_{\tau,3}=\frac{-932\,746\,816}{6\,975\,757\,441}<0.
\]
Therefore identifying the prospective current sign with the **completed** finite event contradicts exact dynamics near a turning point. S43's delayed midpoint-current receipt avoids that error. This is a specific counterexample, not a universal sign reversal statement. QED.

## Verification, correction and scientific boundary

- [`verify_thm534_face_boundary_receipt_v1_1.py`](verify_thm534_face_boundary_receipt_v1_1.py): exact signed boundary; 14 face/core + burden/reservoir steps; actual midpoint flux and next-event selectors; recurrence and face/core norm; all 24 oriented S4 rebasings × four states; source-free and symmetric controls. Constructor **PASS_SCOPED**.
- [`verify_thm534_face_boundary_receipt_fraction_v1_1.py`](verify_thm534_face_boundary_receipt_fraction_v1_1.py): distinct pure-Python Fraction recurrence and 14-event midpoint receipt/stock test. Same constructor, not external independent review. **PASS_SCOPED**.
- **Audit correction:** an earlier exploratory provisional rule set the edge mask from \(2d_fz_{f,n}t_n\) at the **beginning** of event n. S48 falsifies its interpretation as executed finite receipt. The current v1.1 explicitly replaces it with a next-event bit selected from exact midpoint flux. The earlier prospective rule remains separately valid only as a *prospective diagnostic*, not a finite-event closure law. No historical frozen result is overwritten.
- **No physical promotion:** candidate \(\chi^{\rm in}\) is not intrinsic geometric \(\chi\), and \(b^{\rm in}\) is not uniquely selected boundary admissibility. All topological faces and cell remain present in the carrier throughout; edge gates affect **burden transport**, face/core couplings remain continuously admitted. No physical time, action, conserved stress-energy, Born weighting, THM-534 six-edge transition matrix, gauge field or spacetime metric is derived.
- **OPEN_GATED:** source of the sign/AND selection from the frozen packet action; actual dynamic face hard gate \(h_f^{23}\) and boundary exception/repair rules; automatic phase/framing/edge-channel selection; independent physical observable; source/energy reservoir for nondecaying circulation; non-constructor adversarial review.

**Next recommended test:** rigorously derive a face-contact admission/reset mechanism (rather than assume \(h_f^{23}=1\)), and test its compatibility with the frozen multi-cell Q169–Q179 gluing, shared-face reservoirs and hard gating. A fully disabled higher-degree sector cannot bootstrap from this bilinear alone, and an independent source/boundary event must be identified or the branch stopped under its no-go.