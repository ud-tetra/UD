# C06 face balance coverage v0.22

**EXACT / CONDITIONAL** on the declared Whitney port and common-phase preparation. **CANDIDATE** for a face receipt with shared actuation. **Physical Promotion = 0.**

Let \(H\) be the unsigned face-by-edge incidence on the regular tetrahedron. For mean-zero edge data, v0.21 gives \(H^\mathsf TH=2P_-\) on that space. Hence each face sum annihilates mean-zero even data. Also \(HH^\mathsf T=2I+J_4\), since distinct faces share one edge. On the three-dimensional odd subspace, \(H\) maps onto the sum-zero face space and multiplies squared Euclidean norm by two.

For an empty initial Whitney record under closed exchange, write primal flags \(y=Sz\) and aligned odd record \(v_-=\omega_-P_-z\). The source odd coordinate is \(u_-=P_-x\). A face \(f\) reads the three carrier entries of that face and the three primal flags on it. Put \(a_f=(Hx)_f\), \(r_f=\omega_-(Hz)_f\) and \(B_f=r_f^2-a_f^2\). These use only the selected face data. The rate is from the declared v0.11 metric. The balance identity and its derivative are
\[
\sum_f B_f=2(\|v_-\|^2-\|u_-\|^2),\qquad
\sum_f\dot B_f=2\dot B .
\]
This aggregate identity needs neither common phase nor a phase-based OR rule. Its readout still assumes the copied range. Three face values per register reconstruct the fourth by the sum-zero relation.

Under the v0.19 common-phase preparation, \(a_f=s_f\cos\theta,\ r_f=s_f\sin\theta\) with \(s=Hu_0\). Every face with \(s_f\ne0\) detects first upward balance at \(\theta=\pi/4\). A single face can therefore detect this event for preparations it sees, even though v0.21 shows one face cannot reconstruct a prescribed opposite-edge difference. For universal detection over nonzero odd preparations, any fixed three faces suffice and any two fail: on the sum-zero face space the vector supported with values \(+1,-1\) on the omitted faces is invisible to the two selected faces. Within any selected three, \(\max_f |s_f|^2\ge \|u_0\|^2/6\). Indeed if the three selected entries are bounded by \(m\) in magnitude, the fourth is bounded by \(3m\), so \(2\|u_0\|^2\le 12m^2\). This bound is attained by selected entries proportional to \((1,1,1)\) and omitted entry \(-3\).

A shared atomic commit may accept the first qualifying face receipt under the same assumptions as v0.20. Face-local detection itself supplies neither synchronized aggregation nor lockout or actuation authority. The v0.21 record-only and record-and-cut extensions still separate those possibilities. For dephased states, use the full summed balance and its derivative, since a single populated face need not track global balance. Physical implementation and Stage 2 remain open.

Run python3 replay_c06_face_balance.py for exact reduction, coverage, sharp bound and blind-pair witnesses. The replay uses unnormalized integer phase witnesses with the same stock.
