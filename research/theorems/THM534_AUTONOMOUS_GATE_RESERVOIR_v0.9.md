# THM-534 v0.9 — Autonomous positive-stock gate and reservoir candidate: exact conservation and passive no-persistence

**Date:** 2026-10-21 | **Classification:** EXACT CONSTRUCTION / EXACT CONDITIONAL / NO-GO / CANDIDATE native-selection law | **Proof lane:** development, constructor-verified; **Physical promotion:** 0.  
**Previous:** [THM-534 v0.8 S23–S28](THM534_GATE_SELECTION_AND_CIRCULATION_BUDGET_v0.8.md), [v0.7 Q162 burden/current](THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md). **Underlying source:** \`UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md\`, Q153, Q155, Q156, Q158, Q161, Q162, Q163 and Q169–Q173. These coefficients and support receipts are distinct mathematical carriers; nothing below identifies them with physical energy/time or the historical THM-534 transition weights. Historical original THM-534 derivation remains unrecovered. Known target exposure; **not** target-blind confirmatory work.

## 1. Explicit carrier and candidate state rule

Let \(\Delta^3\) be the fixed **filled** tetrahedron on vertices \(0,1,2,3\), with edge order \(01,02,03,12,13,23\). Take signed \(B_1:\mathbb R^6\to\mathbb R^4\), \(B_2:\mathbb R^4\to\mathbb R^6\) with \(B_1B_2=0\), the unit simplex metric, and normalized Q162 attempt coefficient \(1/4\).

Define the **extended candidate state** \((\rho_n,r_n,\beta_n,\tau_n)\), where vertex burden \(\rho_n\in\mathbb R_{\ge0}^4\), **distinct** local vertex reservoir \(r_n\in\mathbb R_{\ge0}^4\), binary boundary admissibility \(\beta_{v,n}\in\{0,1\}\), and binary transport integrity \(\tau_{e,n}\in\{0,1\}\). This is a newly constructed finite candidate; \(r_v\) is **not** the face reservoir \(S_f^{iface}\) of Q172 or a physical bath. For the present minimal branch set \(\beta_{n+1}=\beta_n\) and \(\tau_{n+1}=\tau_n\), treating these flags as supplied boundary controls; dynamic repair of those flags is **not** derived.

Define a **stock-availability bit**, explicitly not the canonically admitted UD geometric closure gate,
\[
\chi^{avail}_{v,n}:=\mathbf1[r_{v,n}>0],
\quad C^{cand}_{cl,e,n}:=\chi^{avail}_{u,n}\chi^{avail}_{v,n},
\quad T^{cand}_{int,e,n}:=\beta_{u,n}\beta_{v,n}\tau_{e,n},
\quad h_{e,n}=C^{cand}_{cl,e,n}T^{cand}_{int,e,n}.
\]
This matches the *formal factorization* Q156 but does **not** prove equivalence with its true \(C_{cl}^{hard}\), \(T_{int}^{hard}\) or the native packet closure rule. The gate is selected from the state, **not prescribed anew each tick**.

**Autonomous single-attempt update:**
\[
H_n=\operatorname{diag}(h_{e,n}),\quad
j_n=-\tfrac14H_nB_1^\mathsf T\rho_n,\quad
p_n=\rho_n+B_1j_n,\quad
F_n=B_2^\mathsf Tj_n,
\]
\[
\boxed{s_n=\tfrac14(r_n-p_n),\quad
\rho_{n+1}=p_n+s_n=\tfrac34p_n+\tfrac14r_n,\quad
r_{n+1}=r_n-s_n=\tfrac14p_n+\tfrac34r_n.}
\]
Here \(s_n\) is a **balanced local reservoir-to-vertex transfer** after the Q162 relaxation. It is not an externally backsolved return to any target state. The exchange coefficient \(1/4\) is a declared modeling reuse of the Q161 attempt convention; Q161 does not establish a universal reciprocal reservoir coupling. This reuse is conditional and cannot be promoted without an independent constitutive proof. Update index is event count, not physical seconds.

## THM-534-S29 — Well-defined dynamic gate and positive stocks [EXACT CONDITIONAL]

For arbitrary finite nonnegative \(\rho,r\), any \(\beta,\tau\in\{0,1\}\), and the stated selection rule, the update is single-valued, preserves \(\rho',r'\ge0\), and obeys
\[
\boxed{\mathbf1^\mathsf T(\rho'+r')=\mathbf1^\mathsf T(\rho+r).}
\]
**Proof.** With \(0\le h_e\le1\), \(P_H=I-\frac14B_1H B_1^\mathsf T\) is symmetric nonnegative row-stochastic: its off-diagonal entry on edge uv is \(h_{uv}/4\ge0\); its diagonal entry is \(1-\sum_{u\sim v}h_{uv}/4\ge1/4\) because K4 degree is three. Thus \(p=P_H\rho\ge0\) and \(\mathbf1^\mathsf Tp=\mathbf1^\mathsf T\rho\). Each pair \((p_v,r_v)\) is multiplied by the positive symmetric doubly-stochastic \(2\times2\) matrix \(\frac14\begin{psmallmatrix}3&1\\1&3\end{psmallmatrix}\), proving positivity and total-stock conservation. QED.

The marked gate is equivariant under **simultaneous** vertex relabeling of \(\rho,r,\beta\) and the induced edge relabeling of \(\tau,H\). This is \(S_4\) covariance of a declared candidate rule, not proof of UD-admissible closure.

## THM-534-S30 — Paired reservoir source receipt [EXACT CONDITIONAL]

For the two-stage attempt, the vertex stock changes by \(B_1j+s\) and the reservoir changes by \(-s\). Thus, componentwise and globally:
\[
\Delta\rho=B_1j+s,\quad\Delta r=-s,\quad
\Delta(\rho+r)=B_1j,\qquad
\mathbf1^\mathsf T\Delta(\rho+r)=0.
\]
The balanced reservoir exchange does **not** eliminate Q162's burden flow; it supplies a typed compensation when reservoir stock differs from the post-relaxation stock. The reservoir holds a finite, explicitly accounted quantity. This is a **conservative stock accounting identity**, not a theorem about physical mass-energy, radiation or source energetics.

## THM-534-S31 — Passive replenishment finite-circulation budget [EXACT / NO-GO]

Write the conserved total \(M=\mathbf1^\mathsf T(\rho_n+r_n)\), mean \(\mu=M/8\), and eight-slot variance
\[
E_n=\|\rho_n-\mu\mathbf1\|^2+\|r_n-\mu\mathbf1\|^2.
\]
For every state-dependent gate history and every admissible boundary/integrity control history, provided the above positive-stock/reciprocal-exchange dynamics are used,
\[
\boxed{E_n-E_{n+1}\ge\|F_n\|^2+\frac38\|p_n-r_n\|^2.}
\]
Consequently
\[
\sum_{n=0}^{N-1}\left(\|F_n\|^2+\tfrac38\|p_n-r_n\|^2\right)\le E_0-E_N\le E_0
\quad\Rightarrow\quad F_n\to0.
\]
**Proof.** Separate the relaxation \((\rho,r)\mapsto(p,r)\) from exchange \((p,r)\mapsto(\rho',r')\). As \(P_H\) is a symmetric contraction preserving \(\mathbf1\), the relaxation decreases the first squared deviation by \(\|\rho-\mu\mathbf1\|^2-\|p-\mu\mathbf1\|^2\). The v0.8 S25 estimate bounds \(\|F\|^2\) by that decrease. The \(2\times2\) exchange has difference eigenvalue \(1/2\), hence decreases the paired squared norm by **exactly** \(\frac38\|p-r\|^2\). Sum, telescope and use nonnegative \(E_N\). QED.

**NO-GO (exact hypotheses):** A finite passive reservoir can temporarily replenish the vertex field, but cannot sustain asymptotically nonzero \(F\), regardless of gate switching. This does *not* preclude independently sourced reversible transport, directional pumps, driven boundaries or different generators; it also does *not* prove any physical energy loss.

## THM-534-S32 — State-selected nonuniform gate witness and its exact decay [EXACT CONDITIONAL]

Let \(\beta=\mathbf1,\ \tau=\mathbf1\), \(\rho_0=(1,0,0,0)^\mathsf T\), \(r_0=(1,1,1,0)^\mathsf T\). The state rule, not a per-tick hand-selected mask, gives
\[
h_0=(1,1,0,1,0,0),\quad j_0=(\tfrac14,\tfrac14,0,0,0,0),\quad
F_0=(0,\tfrac14,\tfrac14,0).
\]
The complete first attempt is
\[
p_0=(\tfrac12,\tfrac14,\tfrac14,0),\quad
s_0=(\tfrac18,\tfrac3{16},\tfrac3{16},0),
\]
\[
\boxed{\rho_1=(\tfrac58,\tfrac7{16},\tfrac7{16},0),\quad
r_1=(\tfrac78,\tfrac{13}{16},\tfrac{13}{16},0).}
\]
Both stocks stay positive at vertices 0,1,2 and zero at vertex 3 for every finite step, so **the selected nonuniform mask persists**. On the 3-vertex active triangle, the Q162 vertex matrix has eigenvalues \(1,(1/4)^{[2]}\). The active contrast \(a_n=\rho_{0,n}-\rho_{1,n}\) and reservoir contrast \(b_n=r_{0,n}-r_{1,n}\) satisfy
\[
\binom{a_{n+1}}{b_{n+1}}=
\begin{pmatrix}3/16&1/4\\1/16&3/4\end{pmatrix}
\binom{a_n}{b_n},\qquad(a_0,b_0)=(1,0).
\]
The eigenvalues are \(\lambda_\pm=(15\pm\sqrt{97})/32\), both strictly between 0 and 1. In exact closed form,
\[
a_n=\frac{\sqrt{97}-9}{2\sqrt{97}}\lambda_+^n+
\frac{\sqrt{97}+9}{2\sqrt{97}}\lambda_-^n,\quad
F_n=\tfrac14a_n(0,1,1,0),\quad\|F_n\|^2=a_n^2/8.
\]
This is an **autonomous positive-stock replenishment witness with nonzero transient curvature** but **no persistent circulation**, consistent with S31.

## THM-534-S33 — Availability is not admissibility; closure and repair remain underdetermined [EXACT / OPEN]

Within the candidate rule, \(r'_v=\frac14p_v+\frac34r_v\) and \(p_v\ge0\), so \(r_v>0\Rightarrow r'_v>0\). Therefore the availability bits are monotone:
\[
\chi^{avail}_{v,n+1}\ge\chi^{avail}_{v,n}.
\]
**NO-GO:** This rule **cannot close a gate that has once opened**, and therefore is not a general closure-fracture/recovery mechanism. It cannot be identified with the desired full \(\chi_i\) law without a new closure-specific source. With initial \(\chi^{avail}=(1,1,1,0)\), a different \(\prod_v\chi^{avail}_v\) complete-cell selector—also compatible with Q156's *formal factorization*—would give all gates off. Thus the actual hard-gate predicate remains structurally nonunique (S23), and this v0.9 rule is merely one **explicit candidate**. No independent UD source has established \(\chi^{avail}=C_{\mathrm{cl}}^{hard}\).

## THM-534-S34 — Conservative reversible rotor control (EXACT CONDITIONAL / NO-GO SCOPE)

As an independent negative control against overgeneralizing S31, enlarge the *routing* input with an explicitly supplied oriented three-cycle register \(\sigma=(u,v,w)\) on an open triangle and define the signed edge current that moves the **entire** vertex stock cyclically:
\[
k_{u\to v}=\rho_u,\quad k_{v\to w}=\rho_v,\quad k_{w\to u}=\rho_w,\quad
\rho'=\rho+B_1k.
\]
Signed orientations are converted to the fixed canonical edge basis. For \(\sigma=(0,1,2)\) and the fourth vertex isolated this is exactly
\[
(\rho_0,\rho_1,\rho_2,\rho_3)\mapsto(\rho_2,\rho_0,\rho_1,\rho_3).
\]
The map is a permutation, preserves total stock, nonnegativity and \(\|\rho\|^2\), and the **oriented triangle face circulation** is
\[
(B_2^\mathsf Tk)_{012}=\rho_0+\rho_1+\rho_2,
\]
which is unchanged at every step and positive whenever that triangle contains stock. **Proof:** direct oriented incidence substitution and permutation. Relabeling \(\sigma\) together with the vertices is equivariant.

This is a conditional **source-complete finite mathematical rotor** but **not** the frozen Q162 gradient-current generator. Its signed orientation \(\sigma\), event scheduling, admissibility, and action/physical work receipt are not native-source-derived. Its existence proves S31's no-persistence result cannot be claimed for arbitrary conservative dynamics.

## Exact and numerical execution

[Exact/finite verifier v0.9](verify_thm534_autonomous_reservoir_v0_9.py) includes: 4,096 exact initial control states across availability patterns, boundary masks and selected integrity controls; 24 \(S_4\) relabelings; exact 12-tick positive-stock receipt; exact eigenvalue and contrast-decay proof controls; 9 reversible rotor events; and **32×256 = 8,192** numerical passive updates with finite/mixed masks. All pass, constructor only. Finite runs are supportive checks, not independent proof.

Frozen observed numerical outputs: **4,096** nonuniform mask steps; **1,574** face-circulation values with norm above \(10^{-12}\); maximum total-stock drift \(1.7763568394002505\times10^{-15}\); maximum apparent Lyapunov-bound shortfall \(1.1401454618356886\times10^{-16}\) (floating-point roundoff; exact theorem not dependent on this); oriented cochain closure residual exactly zero in tested floating stencil.

**Claim boundary:** The full multi-reservoir update is a new **candidate** proposed within the existing Q153/Q156/Q162 accounting interface. It is not the unique/native UD packet closure, is not physical energy conservation, and does not recover THM-534 six-edge Markov hop probabilities, quark/lepton physics, time units, gauge fields or GR. Physical promotion **0**. Independent review pending.

## Next gate
Derive from upstream UD \(\chi,b,\tau\) source receipts a *true* dynamic closure/transport gate and a separately sourced directed circulation or active reservoir work protocol. Freeze signed orientation and its evolution rule without importing a target spectrum. Require admissible state/metric/units, a boundary-reservoir ledger, source-route uniqueness or controlled gauge equivalence, testable observations and independent nonconstructor review before any claim promotion.
