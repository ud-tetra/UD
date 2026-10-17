# Channel-response law and native closure boundary v0.1

**Classification:** source-derived moment identities and EXACT CONDITIONAL response-family theorems. Development — no registry entry. Constructor checked; independent review pending. Physical promotion 0. No numerical target evaluated.

## Scope and source

The frozen v2.3 tetrahedral manuscript supplies the real chain generator A with adjacent blocks -B_k, B_k^T on C0+C1+C2+C3 of dimensions 4+6+4+1. Ledger v0.39 Q165–Q173 supplies norm support and bilinear Hasse-current receipts. Q153/Q158 retain constitutive/open-system source gaps. H03 prevents unqualified reuse of historical F_IFS. Supplied master_action.md, coherence_equation.md and packet_field_equation.md contain placeholder text, not a constitutive selector.

Three objects below are distinct: (i) the 15D native chain state, (ii) an explicitly declared seven paired-stock observation map, and (iii) a conditional unsigned seven-state mixing model. The proposed sensor map and mixing assumptions are not asserted to be admitted native WBS variables. The real signed chain action is not replaced by the unsigned action.

## R1 — Exact response with correlations retained

For a real chain state c evolving under c'=Ac, define its second moment M=cc^T, or any positive ensemble second moment on the same register. Then

\[
M'=AM+MA^T,\qquad M\succeq0.
\]

For the frozen skew A, the solution is

\[
M(s)=e^{sA}M(0)e^{sA^T},\qquad \operatorname{tr}M(s)=\operatorname{tr}M(0).
\]

These are exact consequences of the source generator and matrix product rule. M is a real uncentered second moment; quantum density, energy, entropy and physical-time interpretations do not follow.

Keep update index n primitive. If an internal step h is independently declared, U_h=e^{hA} gives the exact discrete law M_{n+1}=U_h M_n U_h^T. No h or conversion to physical seconds is selected here. For this single-cell source, the active identity A^2=-4(I-P_H0) also gives

\[
U_h=P_{H0}+\cos(2h)(I-P_{H0})+\tfrac12\sin(2h)A.
\]

This exact internal propagator does not determine an event schedule or an irreversible coarse-graining rule.

## R2 — Explicit paired-stock response map

Declare four VF sensors y_i=M_{v_i,v_i}+M_{f_{opposite\ i},f_{opposite\ i}} and three EE sensors z_m=M_{e,e}+M_{e',e'} for opposite-edge pairs. These are nonnegative observed support stocks, not seven native amplitudes. All fourteen vertex/edge/face coordinates are covered once; the fifteenth body coordinate is excluded. Let w_a be each sensor's 0/1 indicator vector.

For ordered native incidences i<j define

\[
J_{ij}(M)=2A_{ij}M_{ij},\qquad
D_{a,ij}=w_{a,i}-w_{a,j}.
\]

Then the exact response law is

\[
\boxed{\dot{\mathbf y}=D_7\mathbf J(M).}
\]

**Proof:** y_a=sum_i w_ai M_ii, and M'_ii=2 sum_j A_ij M_ij. Pairing the i,j terms using A_ji=-A_ij and M_ji=M_ij gives D_a,ij J_ij. QED.

There are 28 native Hasse incidence currents. Appending the body stock b=M_tau,tau supplies D8 with column sums zero:

\[
\binom{\dot{\mathbf y}}{\dot b}=D_8\mathbf J(M),
\qquad \mathbf1_8^TD_8=0.
\]

Both D7 and D8 have exact rank 7; their current kernel has dimension 28-7=21. This is an aggregation/graph kernel, not the chain homology or PSR code. The seven paired stocks obey sum_a y_a=tr M-b, so

\[
\sum_a\dot y_a=-\dot b.
\]

Therefore even their aggregate is not generally conserved when the body exchanges support. OPERATORS.json records the basis, A, all sensors, incidences, and both exact aggregation matrices.

## R3 — Stocks alone do not close native response

Use sorted orientations and choose c_+=v0+e01 and c_-=v0-e01. Both give

\[
\mathbf y=(1,0,0,0,1,0,0).
\]

But their derivatives are respectively

\[
(2,0,0,0,-2,0,0),\qquad(-2,0,0,0,2,0,0).
\]

Thus no autonomous function of these seven stocks alone can reproduce the native instantaneous response for all admitted chain states. Relative signs/correlations are necessary. This is not a no-go for a stochastic, averaged, reservoir-coupled, memory-bearing or enlarged model under additional assumptions. Nor does it exclude special sampled steps where the flow happens to return to identity.

For arbitrary declared quadratic sensors C_a, a closed **linear** sampled response exists on all PSD moments iff their span is invariant under C_a -> U_h^T C_a U_h. The necessity follows because PSD matrices span real symmetric matrices; sufficiency follows by expanding each transported sensor in the declared span. The infinitesimal counterpart requires C_a A + A^T C_a in that span. The paired diagonal sensors fail that infinitesimal test for nonzero incidence coupling.

## R4 — Complete conditional discrete seven-state mixing law

Separately assume: nonnegative seven-channel mass; a fixed linear time-homogeneous update; total mass conservation; covariance under the unsigned S4 action on four VF labels and three opposite-edge matchings; and uniform detailed balance (T=T^T). These are additional mixing axioms, not a native consequence of R1–R3.

The full admissible response family is

\[
\mathbf x_{n+1}=T(q,r,t)\mathbf x_n,
\]

\[
T=\begin{pmatrix}
(1-4q-3r)I_4+qJ_4&rJ_{4,3}\\
rJ_{3,4}&(1-3t-4r)I_3+tJ_3
\end{pmatrix},
\]

with exact conditions

\[
q,r,t\ge0,\quad3q+3r\le1,\quad2t+4r\le1.
\]

Here q is within-VF transfer per distinct pair, t within-EE transfer, and r cross-family transfer. They are source variables, not selected constants. The symbol t here is a transfer weight, not time.

**Completeness proof:** the unsigned group action is transitive on each diagonal class and on each of the three unordered off-diagonal classes (VF/VF, EE/EE, cross). Symmetry and self-adjointness therefore leave five entries; row normalization fixes the two diagonal entries. Entrywise positivity gives exactly the displayed inequalities. Conversely those inequalities produce a symmetric, nonnegative, row/column-normalized, equivariant matrix. QED.

No continuity in physical time or amplitude-to-probability identification is assumed. A prescribed source term j_n gives x_{n+1}=Tx_n+j_n and the usual finite sum of propagated sources; positivity and source/sink balance then require their own gates.

## R5 — Exact multi-round channel responses

Let P0=J7/7. Let PV=diag(I4-J4/4,0), PE=diag(0,I3-J3/3), and PM=I7-P0-PV-PE. Their ranks are 1,3,2,1. Direct substitution gives

\[
T=P0+\lambda_VPV+\lambda_EPE+\lambda_MPM,
\]

\[
\lambda_V=1-4q-3r,\quad
\lambda_E=1-3t-4r,\quad
\lambda_M=1-7r.
\]

Orthogonal projector multiplication yields, for all integer n>=0,

\[
\boxed{T^n=P0+\lambda_V^nPV+\lambda_E^nPE+\lambda_M^nPM.}
\]

The full determinant is lambda_V^3 lambda_E^2 lambda_M. Values can be negative in the admissible stochastic family; attenuation, energy decay and determinant-as-observable must not be conflated. The exact replay checks the identity coefficient-wise in q,r,t and tests finite powers using declared rational control fixtures. Those fixture values are not native coefficients or numerical targets.

Uniform active response requires lambda_V=lambda_E=lambda_M, which gives q=r=t=w. Then

\[
T=P0+f(I-P0),\qquad f=1-7w,\quad0\le w\le1/6,
\]

and det T=f^6 because the conserved mean has eigenvalue one. A positive active screen additionally requires w<=1/7. A full scalar response fI7 preserves total mass only if f=1. The WBS expression F_IFS^7 may concern a different, nonconservative operator or different carrier; these results do not replace that source by changing its exponent. They identify an object/assumption distinction.

## Derived result and remaining source gates

Derived: exact moment/current response under the frozen generator; explicit paired-stock observation response; phase/correlation closure obstruction; complete conditional discrete mixing family; exact sector and multi-round response law.

Not selected: the physical channel map, stochastic closure, q/r/t source law, internal step, metric/time conversion, thermodynamic output functional, cascade depth, or numerical target. The master-action placeholders cannot select these. No IPS/IFS alias, burden-mixing rate or Hodge-Dirac frequency is imported into q/r/t.

Next useful source work is to retain the native signed current receipts (and body exchange) in a supplied channel packet, then test a declared closure/averaging or memory rule. A target number cannot decide that rule.

**Missing source:** Gap2_FINAL_Finite_Genesis.png was unavailable and not used.
