# C06 hard-edge isolation v0.13

**EXACT / CONDITIONAL NO-GO** for diagonal eligibility applied to the fixed flag port. **CANDIDATE (agile)** for an opposite-pair coupling controlled by sector completion. **OPEN** for the native trigger, a topology-changing handoff, Stage 2 selection and deficit allocation. Physical Promotion = 0. Constructor proof and replay.

## 1. Source and model

C06 v0.12, *Declared switched interaction* and *Exact retention and handoff* (UD #540 and UD-Physics #416), requires a two-direction hold at half transfer. Coefficient Ledger v0.39 Q156 and *UD native gate trigger and recovery* v0.1 §§1–2.1 define the Boolean eligibility product \(h_e=C_{{\rm cl},e}^{\rm hard}T_{{\rm int},e}^{\rm hard}\). Applying those edgewise eligibility bits as a diagonal mask on the v0.12 flag port is the premise tested here.

Use the ordinary six-edge permutation module of the tetrahedron with unordered edges and Euclidean metric. Let \(J\) exchange opposite edges and \(P_0=\mathbf1\mathbf1^\mathsf{T}/6\). The two shear projections on the six coordinates are \(P_E=(I+J)/2-P_0\) and \(P_{T_2}=(I-J)/2\), with sum the projection onto \(X=\mathbf1^\perp\). The flag-copy map \(F:\mathbb R^6\to\mathbb R^{12}\) copies each edge coordinate to its two incident flags. Give the flag records a fixed positive-definite metric \(M\), including the v0.11 unweighted action metric under its flag convention. Let \(H=\operatorname{diag}(h_e)\) and \(G=FH|_X\). The full domain of \(F\) allows masks that create an intermediate trace component.

Evolve \(\dot x=-G^*y,\ \dot y=Gx\) in dimensionless time from zero records and an arbitrary preparation in \(X\). Take the metric adjoint and preserve amplitudes at each mask switch. The exchange preserves \(\|x\|^2+\|y\|_M^2\) on each interval and across switches. Forward isolation of an entire sector \(k\) requires \(GP_k=0\), and reverse isolation requires \(P_kG^*=0\). These equations are adjoints. An instantaneous zero flux is a weaker condition.

## 2. Exact diagonal-mask obstruction

Since \(F^\mathsf{T}F=2I_6\), the flag copy is injective, so \(GP_k=0\) is equivalent to \(HP_k=0\). For a binary mask with \(m=\sum_e h_e\), projector and mask idempotence give

\[
\|HP_E\|_{\rm F}^2=\operatorname{tr}(HP_E)=m/3,\qquad
\|HP_{T_2}\|_{\rm F}^2=\operatorname{tr}(HP_{T_2})=m/2.
\]

The diagonals of the two projections are respectively \(1/3\) and \(1/2\). Each nonzero mask thus retains nonzero coupling on both sectors. The all-closed mask freezes both. A mask can silence a particular vector with zero amplitude on every surviving edge. For a full-support sector vector, even one surviving edge prevents forward isolation. The argument extends to arbitrary real diagonal weights on replacing \(m\) by \(\sum_e h_e^2\).

Even an oracle that chooses the mask at the correct half-stock crossing cannot implement sector isolation through this interface. The replay enumerates all 64 masks and explicitly checks their forward flag maps and weighted reverse maps.

## 3. Pachner transfer and a parity-resolved comparator

The *Pachner Canonical Event Sector Selector* v0.1 §§1–2 and *Pachner Event Darboux Map and Generator Pushforward* v0.1 §§7–9, preserved in UD capture 2026-10-18T201837Z-codex-W-source-coverage-d8374ec5, work with a selected rank-six signed-Hodge event space on the common boundary of a 4-simplex. The generator identification in event coordinates is conditional. A bridge from the ordinary edge-current shear port would need its own typed carrier, record and state maps.

If the only dynamical effect of a move is an isometric port pushforward \(G'=VGU^{-1}\), with source isometry \(U:X\to X'\) and record isometry \(V:Y\to Y'\), then \(\ker G'=U(\ker G)\) and \({G'}^*=UG^*V^{-1}\). An injective open port stays injective. A nonzero overall generator rescaling preserves the kernel as well. A genuine topology-changing handoff can fall outside this premise. Its test requires pre/post sector identifications, stock-preserving state transfer, a post-event completed-sector null equation and nonzero coupling on the live sector. The inspected Pachner sources leave this C06 event law open.

On \(X\), \(P_E=(I+J)/2\) is implemented by comparing the two amplitudes in each opposite pair. The declared candidate \(G=F(P_E+\sigma P_{T_2})|_X\) switches \(\sigma\) from 1 to 0 at the first \(T_2\) balance and holds it there until readiness. Then \(GP_{T_2}=P_{T_2}G^*=0\) and \(G|_E=F|_E\). The v0.11 metric makes \(F(E)\) orthogonal to \(F(T_2)\), so \(G^*\) also annihilates the held record space \(F(T_2)\). The even exchange continues as before. This comparator uses an opposite-pair coupling and assumes a persistent sector completion bit.

## 4. Numerical calibration and reproduction

The v0.12 exact timing formulas stand. On the unit cell the fast and slow first-crossing times are approximately \(0.228854\) and \(0.680175\). If the fast port stays active, its phase at the slow crossing is \((\pi/4)\sqrt{53/6}\approx2.334276\) radians and its recorded fraction is approximately \(0.521912\). The irrational frequency ratio precludes an exact half-stock coincidence. The approximate times are dimensionless.

Run python3 replay_c06_hard_edge_isolation.py. The replay uses rational projectors and action metric entries. No empirical fit enters. The v0.12 ideal staged endpoint and the C06 deficit-allocation question retain their prior scope.
