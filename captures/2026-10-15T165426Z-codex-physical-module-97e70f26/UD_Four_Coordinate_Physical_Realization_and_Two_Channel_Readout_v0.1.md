# UD four-coordinate module: physical state, interaction and two-channel readout

Version 0.1 · 15 October 2026 · Development result · Physical promotion 0

## Result and scope

A passive, linear two-loop LC circuit realizes the previously derived four-coordinate module with its inherited energy metric. Seven face capacitors and two cell inductors generate the interaction matrix directly. The shared-capacitor voltage observes the sum mode; an opposing-winding inductive pickup observes the difference mode. Together they reconstruct all four coordinates. Finite passive probe loads shift or damp these modes, with an explicit apparatus energy balance.

This is a declared physical analogue and a constructor calculation, not experimental evidence for a fundamental tetrahedral substrate. Component values, initial preparation, gains, probe impedances and a physical time calibration are apparatus inputs. Independent review is pending. The missing `Gap2_FINAL_Finite_Genesis.png` was not used. No hardware was built or measured in this work.

## 1. Freeze the module before choosing apparatus

Use tetrahedra 0123 and 0124, with consistently ordered simplex orientations and shared face 012. Let B3 be their seven-by-two signed face incidence matrix. Then

\[
M=B_3^TB_3=\begin{pmatrix}4&1\\1&4\end{pmatrix},\quad
M^{-1}=\frac1{15}\begin{pmatrix}4&-1\\-1&4\end{pmatrix}.
\]

The source module is

\[
q'=v,\qquad v'=-Mq,\qquad
H_4=\frac12(q^Tq+v^TM^{-1}v),
\]

where primes mean differentiation in normalized time. Its embedding in the full two-tetrahedron carrier is c3=q, c2=B3 M^(-1)v, c1=c0=0. Since B2 B3=0, it satisfies the face constraint. The actual integer B3, embedding and generator are supplied in `PHYSICAL_MODULE_DATA.json`.

The inherited energy is not the Euclidean norm of (q,v). Its metric is diag(I2,M^(-1)); using a different metric would change the physical identification.

## 2. Physical state and construction

Use three paths between terminals A and B. Each of the two outer paths has one inductor of inductance L and three capacitors of capacitance C in series. The common middle path contains one capacitor C. These form two loops sharing the middle capacitor. Choose loop and branch signs to reproduce B3; both loop currents contribute with the same sign at the shared capacitor. Assume ideal linear components, matched C and L, and negligible direct mutual inductance between primary inductors. Parasitics must be measured in any implementation.

Let I=(I1,I2) be the loop currents in amperes and X be the seven signed capacitor charges in coulombs. Kirchhoff's equations, with the stated signs, are

\[
\dot X=-B_3I,\qquad L\dot I=\frac1C B_3^TX.
\]

The shared face has B3 row (-1,-1). Set

\[
\omega_0=\frac1{\sqrt{LC}},\quad\tau=\omega_0t,\quad
q=I/I_0,\quad c_2=X/(I_0\sqrt{LC}).
\]

Here I0 is a chosen current scale. With balanced initialization X in im B3, these equations give c2=B3 M^(-1)v and the frozen module exactly. In particular, q is normalized current, and v is its derivative in normalized time; neither is asserted to be mechanical position or velocity.

The SI energy is

\[
E=\frac L2I^TI+\frac1{2C}X^TX
  =L I_0^2 H_4.
\]

Thus the energy mapping preserves the carrier metric, and L I0^2 supplies a measured joule scale. L and C set the seconds scale. These choices do not derive an action quantum, G or universal UD units.

The ideal circuit also permits five constant charge-offset coordinates in ker B3^T. They are absent from the four-coordinate module only when prepared to zero or independently calibrated. Their energy, ||X_perp||^2/(2C), is additional. In particular, the circuit has nine electrical state coordinates, with a four-dimensional dynamic module and five static coordinates. It is not a realization of every sector of the full 23-coordinate simplicial carrier.

## 3. The interaction comes from the shared capacitor

Introduce mesh charges Q with X=-B3 Q and I=dot Q in the balanced subspace. Their canonical momenta are Phi=L I. The physical Hamiltonian is

\[
\mathscr H(Q,\Phi)=\frac{\Phi^T\Phi}{2L}
 +\frac1{2C}\left[3Q_1^2+3Q_2^2+(Q_1+Q_2)^2\right].
\]

The shared capacitor contributes the cross term Q1 Q2/C. Consequently the stiffness is M/C before its spectrum is computed; the interaction has not been fitted retrospectively to two frequencies.

Writing Qplus=(Q1+Q2)/sqrt(2) and Qminus=(Q1-Q2)/sqrt(2) diagonalizes this Hamiltonian. The physical angular frequencies and ordinary frequencies are

\[
\Omega_+=\frac{\sqrt5}{\sqrt{LC}},\quad
\Omega_-=\frac{\sqrt3}{\sqrt{LC}},\qquad
f_\pm=\frac{\Omega_\pm}{2\pi}.
\]

The dimensionless ratio is sqrt(5/3). It is an observable of this matched circuit; reproducing it alone does not distinguish a fundamental UD model from ordinary network theory.

For example, preparing q(0)=(1,0), v(0)=0 gives

\[
q_1(\tau)=\tfrac12[\cos(\sqrt5\tau)+\cos(\sqrt3\tau)],\qquad
q_2(\tau)=\tfrac12[\cos(\sqrt5\tau)-\cos(\sqrt3\tau)].
\]

The initially unexcited second loop acquires current through the common capacitor. The two normal modes interfere to produce the exchange envelope; no stochastic gate or additional interaction has been assumed.

A preparation actuator can supply loop voltages U:

\[
L\dot I=B_3^TX/C+U,\qquad P_{\rm in}=I^TU.
\]

For u=U/(I0 sqrt(L/C)), q'=B3^T c2+u and q''=-Mq+u'. Symmetric and antisymmetric U select the two modes. The input in the second-order equation is u', not u. Arbitrary prepared module states are controllable in this ideal driven network, but this work specifies no manufactured switching actuator or measured preparation efficiency. Preparation energy and actuator losses belong in the resource budget.

## 4. Two complementary voltage channels

### Channel F: shared-face voltage

Let Z0=sqrt(L/C), and measure V_F=X_shared/C. In the ideal unloaded, balanced module,

\[
y_F=\frac{V_F}{I_0Z_0}=-\frac{v_1+v_2}{5},\qquad y_F'=q_1+q_2.
\]

This observes only the sqrt(5) sum mode. A shared-face probe cannot establish whether the hidden difference mode was populated.

### Channel P: opposing-winding pickup

Use a two-lobe secondary pickup with mutuals +mu and -mu to the two primary inductors. Its open-circuit emf is

\[
U_P=-\mu\frac{d(I_1-I_2)}{dt},\qquad
y_P=-\frac{U_P}{\mu I_0\omega_0}=v_1-v_2.
\]

Here mu is a nonzero measured mutual inductance, not an unexplained fit. Two separated transformer lobes can implement opposite secondary winding signs; their actual mutuals and unwanted primary coupling require calibration. Both channels are voltages. The pickup naturally observes the derivative of the current difference.

For z=(q1,q2,v1,v2), the normalized output matrix is

\[
C_4=\begin{pmatrix}0&0&-1/5&-1/5\\0&0&1&-1\end{pmatrix}.
\]

With A4=[[0,I],[-M,0]], rank([C4; C4 A4])=4. Each channel separately has observability rank two. Exact noiseless reconstruction is

\[
q_1=\tfrac12(y_F'-y_P'/3),\quad
q_2=\tfrac12(y_F'+y_P'/3),\qquad
v_1=\tfrac12(-5y_F+y_P),\quad
v_2=\tfrac12(-5y_F-y_P).
\]

## 5. Two-time reconstruction and a deterministic noise bound

Differentiating noisy voltages is unnecessary. Take two samples of each normalized output at tau and tau+h, with h=1/4. Write w5=sqrt(5), w3=sqrt(3), and define s_q=q1+q2, d_q=q1-q2, s_v=v1+v2, d_v=v1-v2. Then

\[
s_q=w_5\frac{y_F(\tau+h)-\cos(w_5h)y_F(\tau)}{\sin(w_5h)},\qquad
 d_q=-\frac{y_P(\tau+h)-\cos(w_3h)y_P(\tau)}{w_3\sin(w_3h)},
\]
\[
s_v=-5y_F(\tau),\qquad d_v=y_P(\tau).
\]

Half the sum and difference reconstruct each q and v. The physical sample separation is sqrt(LC)/4. This is an ideal-module formula; the finite-loaded circuit below has more dynamical coordinates.

Suppose each of the four normalized voltage samples has arbitrary additive error of magnitude at most nu. Taylor's lower bound sin x >= x-x^3/6 gives

\[
\sin(\sqrt5/4)>1/2,\qquad\sin(\sqrt3/4)>2/5.
\]

Hence |delta s_q|<4 sqrt(5) nu<9nu, |delta d_q|<5nu/sqrt(3)<3nu, |delta s_v|<=5nu, |delta d_v|<=nu. Therefore |delta q_i|<6nu, |delta v_i|<=3nu, and in the inherited carrier norm

\[
\|\delta c\|^2=\|\delta q\|^2+\delta v^TM^{-1}\delta v
 <72\nu^2+6\nu^2=78\nu^2,
\qquad \boxed{\|\delta c\|<9\nu}.
\]

This is a conservative deterministic bound, not a statistical claim. Gain, timing, component mismatch, preparation offsets and model errors require separate budgets. Checking all 16 corners of the four-sample noise box corroborates a maximum norm amplification of about 6.03806 for the fixed decoder; the analytic guarantee remains 9.

Weak pickup is not free: physical pickup-voltage error epsilon_P corresponds to normalized error epsilon_P/(|mu| I0 omega0). To meet target nu, one needs |mu|>=epsilon_P/(I0 omega0 nu), while magnetic passivity requires |mu|<sqrt(L Ls/2). Both can hold only if the apparatus has a compatible noise and loading budget.

## 6. Include the apparatus: finite loading and energy cost

Model the face-voltage probe by an added capacitance Cp>=0 and conductance Gp>=0 across the shared capacitor. Let Cs=C+Cp and C_b be diagonal with shared entry Cs and other entries C. Give the pickup secondary inductance Ls>0, load Rs>0, and current J. With d=(1,-1), require

\[
\mathsf L=\begin{pmatrix}L I_2&\mu d\\\mu d^T&L_s\end{pmatrix}>0,
\qquad LL_s>2\mu^2.
\]

The full ten-coordinate electrical system is

\[
\dot X=-B_3I-G_p e_s V_F,\qquad V=C_b^{-1}X,\quad V_F=e_s^TV,
\]
\[
\mathsf L\begin{pmatrix}\dot I\\\dot J\end{pmatrix}
 =\begin{pmatrix}B_3^TV\\-R_sJ\end{pmatrix}.
\]

The measured voltages are V_F and V_R=Rs J. Its stored energy and exact loss identity are

\[
E_{\rm total}=\frac12X^TC_b^{-1}X+
\frac12(I,J)^T\mathsf L(I,J),\qquad
\boxed{\dot E_{\rm total}=-G_pV_F^2-R_sJ^2}.
\]

A write source adds I^T U to the right-hand side. The time integral of the two losses is a real joule cost in this declared circuit, not a normalized bookkeeping stock. Digitizer, recording, controller, bath renewal and reset costs remain outside this electrical submodel; no complete record-formation entropy or Landauer claim follows.

With Gp=0 and no pickup loading, probe capacitance alone gives

\[
\Omega_-^2=3/(LC),\qquad
\Omega_+^2=\frac{3+2C/(C+C_p)}{LC}.
\]

For Cp/C<=1/100, the common-frequency ratio is at least sqrt(503/505)>499/500: its downward shift is less than 1/500. This is a derived tolerance example, not a measured probe specification.

The pickup transfer, for zero initial secondary current, is

\[
J(s)=-\frac{\mu s}{R_s+L_s s} I_d(s),\qquad
V_R(s)=-\frac{\mu R_s s}{R_s+L_s s}I_d(s),\quad I_d=I_1-I_2.
\]

The open-circuit emf is approached as Rs tends to infinity; finite Rs gives both a transfer filter and backreaction. The ideal reconstruction cannot simply be reused without modeling or bounding these effects.

### Both measured modes decay under finite passive loads

The two dynamical characteristic polynomials are

\[
p_+(s)=LC C_s s^3+LCG_p s^2+(3C_s+2C)s+3G_p,
\]
\[
p_-(s)=(LL_s-2\mu^2)s^3+LR_s s^2+(3L_s/C)s+3R_s/C.
\]

For Gp>0, Rs>0, mu nonzero and positive inductance matrix, all coefficients are positive. The cubic Routh margins are respectively 2LC^2 Gp>0 and 6Rs mu^2/C>0. Thus every root of both cubics has negative real part. Finite dissipative readout drains both oscillatory channels. Protection under a separately defined vertex recovery interaction does not imply protection under these face and inductive measurement ports.

There are four remaining static offsets and six dynamical coordinates. For the declared benchmark, rank([C;CA;CA^2])=6 exactly; the two output histories observe all six dynamical coordinates. This is not the assertion that two instantaneous numbers identify a six-coordinate state. The ideal four-sample decoder applies only to the unloaded four-coordinate module.

## 7. Verification and a reproducible benchmark

The replay constructs boundary matrices afresh and checks rational identities using Python Fractions, then uses NumPy/SciPy for numerical corroboration. It does not execute imported research scripts.

The dimensionless constructor benchmark L=C=Ls=1, mu=1/10, Rs=10, Gp=Cp=1/100 is not a hardware component recommendation. Its integer cubic coefficient lists are (101,1,503,3) and (49,500,150,1500). The full characteristic polynomial is s^4 pplus(s) pminus(s)/(101*49). Approximate roots are:

| Channel | Roots in benchmark time units |
|---|---|
| Common | -0.00596424; -0.00196837 +/- 2.23162960 i |
| Difference | -10.19824651; -0.00291756 +/- 1.73254379 i |

All **27 exact checks and 9 numerical checks pass**. They cover the native matrix, physical intertwiner, inherited energy, static offsets, complementary observability, exact derivative reconstruction, sample-noise inequalities, passivity, characteristic factorization, loaded observability, trajectories, decoding, all noise-box corners and integrated dissipation. Exact checks certify finite algebra within the declared model; numerical checks corroborate implementation and examples. Neither category supplies independent review or an empirical correspondence.

The initially coarse dissipation quadrature under-resolved the fast secondary transient. It was replaced by adaptive quadrature without relaxing the energy-loss tolerance; the replay also checks the reported quadrature error. This changed no source equation or analytic bound.

## 8. What is now closed, and what remains open

| Item | Status | Meaning |
|---|---|---|
| Electrical state and SI units | DERIVED | I and X, with explicit L,C,I0 scaling |
| Source of interaction M | DERIVED | Three exclusive C and one shared C per loop |
| Complementary ideal voltage readout | EXACT/DERIVED | Four-coordinate observability and reconstruction |
| Finite-sample conditioning | DERIVED | Inherited norm error <9nu under stated sample model |
| Finite passive apparatus | DERIVED | Ten-state model, loss identity, decaying dynamic modes |
| Numeric replay | NUMERICAL PASS | Specified examples, not experiments |
| Geometry as a fundamental physical cause | OPEN | Circuit topology was chosen to implement the operator |
| Physical action quantum and universal units | OPEN | L,C,I0 are supplied, not predicted (ledger G05/G06) |
| Manufacturing, mismatch and measured noise | OPEN | No apparatus characterization yet |
| Complete write/read/record/reset cost | OPEN | Electronics and renewal costs need an apparatus model |
| Independent review | PENDING | Constructor verification only; physical promotion 0 |

The next defensible mathematical package is a robust loaded-state observer with explicit parameter uncertainty and a finite-duration write/read budget. Freeze its tolerances and a matched ordinary-circuit null before considering empirical discrimination. The present result supplies a concrete analogue bridge and exposes its loading cost; it does not close the source-selection or fundamental-physics bridge.

## Sources and provenance

1. UD, `UD_Bipyramid_Bridge_Exploration_v0.1.md`, PR120, commit 53c96276623fee508f521c6c6a983f0798c1aacd. Source of the frozen module, signed boundary conventions and distinction between four-coordinate module and full carrier. Included as source data in this package.
2. User-supplied local `20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md` and `21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md`. Governance and unresolved physical-unit scope; included unchanged as source data.
3. MIT OpenCourseWare, 8.02T Electricity and Magnetism, Spring 2005, *Chapter 11: Inductance and Magnetic Energy*, sections 11.1, 11.5 and 11.6. Mutual induction, LC storage/oscillation, and resistive loss are established circuit ingredients. https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/5039d9b38e0e96be41771c5455731e34_chap11inductance.pdf
4. Tektronix, *How Oscilloscope Probes Affect Your Measurement*, consulted 15 October 2026. Probe input resistance and capacitance alter the measured circuit. The particular loading equations and tolerances above are derived here. https://www.tek.com/en/documents/application-note/how-oscilloscope-probes-affect-your-measurement

No domain-only citations are used. The particular module/circuit identification, reconstruction bounds and loaded polynomials are this package's derivations, not claims attributed to MIT or Tektronix.
