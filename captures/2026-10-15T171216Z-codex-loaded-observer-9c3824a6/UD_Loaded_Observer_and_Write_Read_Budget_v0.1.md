# UD loaded observer and finite write/read budget

Version 0.1 · 15 October 2026 · Development — no registry entry

Physical promotion 0 · Constructor verification only · Non-constructor review pending

## Result

The physical analogue of the four-coordinate module now has an exact six-state loaded reduction, a sampled observer with a rational conditioning certificate, and a finite-duration write pulse whose electrical work and heat can be audited. For one declared benchmark, three samples from each voltage channel reconstruct all six dynamic coordinates. A specified eight-parameter uncertainty box preserves observability, bounds write error, and guarantees greater than 19/20 energy retention over the read window for the stated preparation class.

A concrete binary write/read construction is also obtained. At a chosen signal amplitude of six normalized sample-noise units, its two output histories remain distinguishable under the declared uncertainty bounds, while gross positive work at the electrical source ports is less than (144/5) Eref nu^2. This is a sufficient budget for this construction, not a universal minimum cost of a bit, an entropy law, or a fundamental-physics correspondence.

## 1. Freeze apparatus, units and uncertainty family

Start with PR121's passive two-loop circuit: seven equal face capacitors C before probing, two equal primary inductors L, a shared-face probe with Cs=C+Cp and Gp, and an opposing pickup with mutuals +mu and -mu, secondary inductance Ls and load Rs. Add a declared series drive resistance r in each primary loop. The same resistance remains connected during writing and reading. The source emfs are set to zero during readout; no zero-cost topology change or current-breaking switch is assumed.

Assume linear lumped elements, matched primary inductors, three matched exclusive capacitors per loop, exactly opposite pickup mutuals, and negligible direct mutual inductance between the primaries. The eight uncertain parameters are L,C,Cs,Ls,mu,Rs,Gp,r. Their values are constant during a run. The uncertainty box preserves this matching structure; it does not cover arbitrary individual-component mismatch, parasitic primary coupling, drift terms, timing error, voltage-source error or ADC gain error. Those need additional budgets.

The symbolic equations below are SI equations. The constructor benchmark is dimensionless, using independently chosen L0,C0,I0 and

\[
t_0=\sqrt{L_0C_0},\quad Z_0=\sqrt{L_0/C_0},\quad E_{\rm ref}=L_0I_0^2.
\]

Charges are scaled by I0 t0, currents by I0, voltages by I0 Z0, inductances by L0, capacitances by C0, resistances by Z0 and conductances by 1/Z0. The benchmark is

\[
L=C=L_s=1,\quad C_s=101/100,\quad \mu=1/10,\quad
R_s=10,\quad G_p=r=1/100.
\]

These are design/calibration inputs, not UD-derived universal constants or hardware recommendations. Ledger G05/G06 remain open.

## 2. Exact six-coordinate dynamic reduction

Let x be the signed shared-capacitor charge. For the exclusive faces of loop i, define a_i=sum_f B_fi X_f, using the signed B3 of tetrahedra 0123 and 0124. Define

\[
z=a_1+a_2,\quad w=a_1-a_2,\quad
S=I_1+I_2,\quad D=I_1-I_2,
\qquad \xi=(z,x,S,w,D,J)^T.
\]

Here z,x,w are charges; S,D,J are currents. The common and difference systems obey

\[
\dot z=-3S,\qquad \dot x=S-gx,\qquad
L\dot S=z/C-2x/C_s-rS+U_\Sigma,\quad g=G_p/C_s,
\]
\[
\dot w=-3D,\qquad
L\dot D+2\mu\dot J=w/C-rD+U_\Delta,\qquad
\mu\dot D+L_s\dot J=-R_sJ,
\]

where U_Sigma=U1+U2 and U_Delta=U1-U2. Write these as dot xi=A6 xi+B6 u. All matrix entries are supplied in `LOADED_OBSERVER_DATA.json`.

The four residual exclusive-face charge offsets are constant and orthogonal to the dynamic face distributions. Preparing them to zero gives the exact ten-state embedding; nonzero values carry additional constant energy and are not identified by this observer. The replay verifies P R=I6, P A10=A6 P, A10 R=R A6 and R^T G10 R=G6. This is an exact reduction, not a numerical mode fit.

The dynamic electrical energy is

\[
E_6=\frac{z^2+w^2}{12C}+\frac{x^2}{2C_s}
+\frac L4(S^2+D^2)+\mu DJ+\frac{L_s}{2}J^2
=\frac12\xi^TG_6\xi.
\]

G6 is positive if L Ls>2mu^2. The exact energy balance is

\[
\boxed{\dot E_6=\frac{S U_\Sigma+D U_\Delta}{2}
-\frac{G_p x^2}{C_s^2}-R_sJ^2-\frac r2(S^2+D^2)}.
\]

Thus the source resistance is charged in both phases, alongside probe leakage and pickup dissipation. The static offsets, when present, add a constant to stored energy and do not improve the observable signal.

## 3. Three samples per channel observe six dynamic coordinates

The physical outputs are V_F=x/Cs and V_R=Rs J. Work in a fixed nominal energy coordinate e=G0^(1/2) xi and fixed scaled outputs

\[
b=W_0(V_F,V_R)^T,\qquad
W_0=\operatorname{diag}(\sqrt{C_{s,0}},\sqrt{L_{s,0}}/R_{s,0}).
\]

In SI, both e and b have units sqrt(joule); in the benchmark they are normalized by sqrt(Eref). This prevents adding charge errors to current errors without a declared metric. All gains and coordinates remain fixed at their nominal values when bounding uncertainty.

During a source-free read, take samples at t/t0=0,1,2 relative to the write endpoint. Define

\[
\mathcal O_0=\begin{pmatrix}
W_0C_0\\W_0C_0e^{A_0}\\W_0C_0e^{2A_0}
\end{pmatrix}G_0^{-1/2},\qquad
\widehat e_0=\mathcal O_0^{\dagger}\mathbf b.
\]

No output derivative is required. For the frozen benchmark,

\[
\boxed{\sigma_{\min}(\mathcal O_0)>1/50}.
\]

Numerically sigma_min is about 0.0218701 and the condition number about 61.3108. These decimals are corroboration, not the certificate.

### Rational certificate

Passivity implies ||exp(Abar0 t)||<=1 in the energy norm. Exact rational traces show ||Abar0||<11; the two energy-scaled output rows are orthogonal and ||Cbar0||<11/10. Form the degree-100 Taylor polynomials at times 0,1,2, and stack them into O_N in physical coordinates. Exact rational elimination verifies

\[
O_N^T\operatorname{diag}(W_0^2,W_0^2,W_0^2)O_N
-(21/1000)^2G_0>0.
\]

The integral Taylor remainder, using the contractive semigroup, satisfies

\[
\|e^{\bar A t}-P_{100}(\bar A t)\|
\le \frac{(11t)^{101}}{101!}.
\]

The stacked output remainder is less than 1/1000 by an exact rational inequality. Singular-value perturbation therefore yields sigma_min>(21-1)/1000=1/50. The proof does not depend on a floating-point exponential or singular-value computation.

## 4. Parameter uncertainty, noise and reconstruction

Permit every one of the eight matched-family parameters to vary independently within relative error 1/100000 of nominal. Interval arithmetic over the whole box, not just its corners, proves in the fixed energy/output coordinates

\[
\|\Delta\bar A\|<1/2000,\quad
\|\Delta\bar C\|<1/50000,\quad
\|G_0^{-1/2}(G-G_0)G_0^{-1/2}\|<1/30000,
\]
\[
\|G_0^{1/2}(B-B_0)\|<1/10000.
\]

The last bound uses the declared sum/difference voltage-input coordinates. It is used for write uncertainty, not for source-free read dynamics. The box also preserves positive inductance and Cs>C.

For delta_A=1/2000, delta_C=1/50000 and c=11/10, Duhamel's identity gives, at read time t,

\[
\|\Delta\mathcal O(t)\|\le
c(e^{\delta_A t}-1)+\delta_C e^{\delta_A t}.
\]

Using exp(2delta_A)<=1/(1-2delta_A), the stacked error over the three times is less than

\[
\boxed{\rho=1/500}.
\]

Thus the true sampled operator has sigma_min>1/50-1/500=9/500. If the six normalized sample errors are each bounded in magnitude by nu and ||e0||<=R, nominal least-squares decoding obeys

\[
\boxed{\|\widehat e_0-e_0\|<50\sqrt6\,\nu+R/10
<125\nu+R/10}.
\]

This is a conservative absolute error certificate. It does not promise small relative error for a nearly zero state, nor silently absorb unknown timing/gain/mismatch effects into the eight-parameter box. All 256 parameter-box corners additionally corroborate the enclosure; the interval proof supplies coverage between them.

## 5. An explicit finite-duration write

Keep probes and resistance connected. Start at xi=0 and apply a finite voltage waveform over 0<=s=t/t0<=1. The target is

\[
\xi_*=(0,0,1,0,1,0),
\]

meaning I1=1, I2=0, zero dynamic capacitor charge and zero secondary current at the write endpoint. Four static offsets remain zero. In the benchmark its target energy is 1/2.

Choose the shared charge and secondary current polynomials

\[
x(s)=\tfrac32s^2-4s^3+\tfrac52s^4,\qquad
J(s)=\tfrac3{10}s-\tfrac{51}{50}s^2+\tfrac{18}{25}s^3.
\]

Define the remaining coordinates and required source emfs by

\[
S=x'+gx,\quad z=-3x-3g\int_0^s x(u)du,
\]
\[
D=-\frac{L_sJ+R_s\int_0^sJ(u)du}{\mu},\qquad
w=-3\int_0^sD(u)du,
\]
\[
U_\Sigma=LS'+rS-z/C+2x/C_s,
\]
\[
U_\Delta=-\frac{LL_s-2\mu^2}{\mu}J'-w/C
-\frac{LR_s}{\mu}J+rD.
\]

These are explicit polynomial voltages. The pulse construction enforces both endpoint states and the integral constraints imposed by the loaded secondary and shared leakage. Actual loop emfs are (U_Sigma+U_Delta)/2 and (U_Sigma-U_Delta)/2. Setting them to zero after s=1 changes derivatives but causes no state or stored-energy jump in this lumped model.

The replay verifies all six ODEs coefficient by coefficient, not just their endpoint values. The construction is feasible for the declared ideal actuator; it is not an optimized waveform or a manufactured source specification.

### Exact nominal write budget

Every entry below is in Eref units; multiplying the pulse by amplitude a multiplies every energy/work quantity by a^2.

| Quantity | Exact value | Approximate value |
|---|---|---|
| Target stored energy | 1/2 | 0.5 |
| Probe leakage heat | 10/642663 | 0.00001556 |
| Pickup-load heat | 129/17500 | 0.00737143 |
| Drive-resistance heat | 87585811/32133150000 | 0.00272572 |
| Net source-port work | 5463842677/10711050000 | 0.51011270 |
| Gross positive source-port work | Numerical integration over polynomial sign intervals | 0.57682999 |
| Work returned to actuator | Numerical integration over negative-power intervals | 0.06671729 |

The exact identity is Wnet=Etarget+Hprobe+Hpickup+Hdrive. Returned work is reported separately; it is not presumed to be recovered with unit efficiency. With P the source-power polynomial,

\[
W_+=\tfrac12\left(\int|P|+W_{\rm net}\right)
\le\tfrac12\left(\sqrt{T_w\int P^2}+W_{\rm net}\right)
<\frac{16174892677}{21422100000}.
\]

The upper fraction is a conservative rational bound, rather than the numerical positive-work estimate.

### Write error and actual source-work bound

For the same fixed nominal pulse and parameters anywhere in the box, variation of constants gives a uniform write-trajectory error bounded by

\[
e^{\delta_A T_w}\left[
\delta_A\sqrt{T_w\int\|e_{\rm nominal}(s)\|^2ds}
+\delta_B\sqrt{T_w\int\|u(s)\|^2ds}\right]<1/1000.
\]

The integrals are exact polynomial integrals; rational square-root upper bounds supply the certificate. Consequently the actual endpoint is within a/1000 of the nominal amplitude-a target in the fixed energy norm, assuming the voltage waveform itself is accurate.

The nominal source-power operator has norm less than 3/4. Bounding the change in its positive-power integral with this uniform trajectory error yields

\[
\boxed{W_{+,\rm actual}<\frac45a^2E_{\rm ref}}.
\]

This charges all specified passive circuit losses and gross positive work through the source ports. It excludes waveform-generator electronics, digitization, durable memory, controller computation, bath renewal and reset. No complete apparatus or thermodynamic lower-bound claim is made.

## 6. Retention during a two-unit read

The original four-coordinate preparation class is embedded as

\[
\xi=P_4(q_1,q_2,v_1,v_2)^T
=\left(\tfrac35(v_1+v_2),-\tfrac15(v_1+v_2),q_1+q_2,
 v_1-v_2,q_1-q_2,0\right)^T.
\]

The shared probe is already connected when this state is prepared. Its energy metric is P4^T G6 P4; it must not be silently replaced by the unloaded metric.

At read duration T=2, another exact rational Taylor/positive-definiteness certificate proves nominal energy retention greater than 24/25 for every nonzero state in this preparation class. The nominal numerical retention eigenvalues range from about 0.968064 to 0.975075. This result does not apply to an arbitrary six-state initial condition containing a large fast-secondary transient.

For the declared uncertainty box, the state-propagator perturbation is less than 1/999 and metric variation less than 1/30000. Combining these with the write error cone proves

\[
\boxed{E_{\rm actual}(T)/E_{\rm actual}(0)>19/20}
\]

for the specified written target and its nonzero amplitude multiples. The same bound holds for exact P4 preparations; the finite-write error-cone extension here is certified for this pulse family. For the nominal unit-amplitude target, read heat is approximately 0.01498954 and energy after read approximately 0.48501046, separately corroborated by integrating the loss rate.

Energy retention and distinguishability are different statements. The following section supplies a separate signal-distance bound.

## 7. One retained binary symbol with a declared electrical budget

Encode the two symbols with the pulses +a u(s) and -a u(s). Their nominal written states are +/-a xi*. The target has unit energy-coordinate norm. Exact rational sample-Gram evaluation, with its remainder bound, gives a direction-specific signal gain greater than 1/2. This is stronger for this particular binary direction than the worst-direction six-state observer bound of 1/50; it does not improve that full-state bound.

Combining write error with read-model uncertainty bounds each noiseless sample vector's deviation from its nominal code center by less than a/200. Six scalar errors of magnitude at most nu have stacked norm at most sqrt(6)nu<(5/2)nu. The two uncertainty/noise balls are disjoint if

\[
a\left(\frac12-\frac1{200}\right)>\frac52\nu.
\]

Thus **a=6nu suffices** for any positive declared nu. A nearest-nominal-center decoder then distinguishes the symbols under all stated errors. The noiseless case permits any a>0. No probability distribution or Gaussian-noise assumption is used.

For this sufficient choice,

\[
E_{\rm target,nominal}=18E_{\rm ref}\nu^2,\qquad
\boxed{W_{+,\rm actual}<\frac{144}{5}E_{\rm ref}\nu^2}.
\]

Greater than 19/20 of the actual post-write electrical energy remains at the end of the read window. This is a retained binary label in an analog electrical state. It is not yet an irreversible receipt, a complete memory cycle, a channel-capacity theorem, or information per boundary area. An assigned apparatus area and all recording/renewal costs remain necessary for the latter comparisons.

## 8. Verification, corrections and next closure

**46 exact checks and 10 numerical checks pass.** Exact checks cover reduction, energy, input power, rational observer and retention certificates, whole-box uncertainty envelopes, the six write ODEs, endpoint, heat/work identities, write uncertainty, binary separation and source-work bounds. Numerical checks corroborate singular values, sampled reconstruction, all 256 parameter corners, finite write trajectories, polynomial power splitting and read dissipation. Neither category is empirical validation or non-constructor review.

A constructor implementation initially allowed integer zero entries divided by two to become floating-point zeros in a polynomial energy expression. The exact net-work assertion detected the resulting floating coefficients. All model matrix entries, including zeros, are now normalized to Fractions before algebra. The equations and intended claim were unchanged. A clean-directory replay reproduces the two output JSON files byte for byte. This correction is recorded as a local pre-release implementation repair, not a retraction of PR121.

The strongest next mathematical closure is **symmetry-breaking component mismatch**: independent primary/exclusive-capacitor/mutual errors, resulting cross-channel mixing and offset leakage, followed by a robust observer that tests its own model residual. Then specify actuator bandwidth/saturation, ADC and durable-record/reset costs. A fundamental UD source-selection or action-unit theorem remains a separate task. This development result promotes none of those gaps.

## Sources

- PR121, *Four-coordinate physical analogue and two-channel readout*, remote commit e7f3ee66485a9d3dcd76724cf9e42fcfc3a28a59: https://github.com/ud-tetra/UD/pull/121 . Report and finite matrices are preserved as source data in this package. PR120 supplied the earlier frozen module.
- User-supplied local coefficient ledger v0.39(2), especially G05/G06 and Q174, and governance CRL-2 subdivision v1.0; copied unchanged. Development lane; no registry promotion or physical identification.
- MIT OpenCourseWare, 8.02T Spring 2005, *Chapter 11: Inductance and Magnetic Energy*, sections 11.1, 11.5 and 11.6: https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2005/5039d9b38e0e96be41771c5455731e34_chap11inductance.pdf . Supports standard inductive/capacitive storage, mutual induction and resistive loss; not the particular observer or budget derived here.
- Tektronix, *How Oscilloscope Probes Affect Your Measurement*: https://www.tek.com/en/documents/application-note/how-oscilloscope-probes-affect-your-measurement . Supports inclusion of probe resistance/capacitance; the present six-state equations and certificates are our derivations. Consulted 15 October 2026.

`Gap2_FINAL_Finite_Genesis.png` remains unavailable and was not used. No domain-only citation, unexamined archive or historical numerical target supplied a missing physical normalization.
