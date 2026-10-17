# UD retained distinguishability for the stock-controlled writer v0.1

15 October 2026 UTC. Development — no registry entry. Conditional mathematics; constructor verification only. Independent review pending. Physical promotion 0.

**Result.** The positive-stock writer admits a six-symbol real-amplitude code with an exact retained-distance certificate. For the declared uniform finite mechanism, the six writes are symmetry-related and share one response kernel. With the explicit controller refinement below, their common restoration time lies in [1/3,1/2], and the protected output distance is at least 25/256. Nearest-template decoding tolerates total protected-amplitude error strictly below 25/512. A finite post-restoration contact-error bound and the normalized export receipt accompany the certificate.

This is a candidate encoding and readout contract. The controller receives the symbol through its chosen write edge. No native source selection, physical measurement rule, quantum discrimination, entropy law or information-per-physical-area claim is made.

## 1. Source and protocol disposition

The source mechanism is `UD_Positive_Stock_Balanced_Recovery_and_Predictive_Switching_v0.1.md`, PR117, commit `85fd18bfb224733234f1b5cd8e8ecd2e149ed344`. It declares signed transport z, positive load m, export w and finite buffer b=m+z^2/2. The finite 600-cell input and current constructor helper are preserved with hashes. No historical uploaded code is executed.

The attached ledger v0.39(2), C03/Q153/Q156/Q158/Q162/Q178, continues to leave physical capacity, predictive primitive sourcing and renewal identification open. The attached CRL-2 proposal distinguishes constructor checks from independent review. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used. The repository base inspected was `d833aae4837672b433712894475e1a6962334672`.

The six representative edges and exact leading geometry come from `ROBUST_RETENTION_DATA.json`, preserved from the prior development package. Their Gram matrix is independently reconstructed here from the incidence matrices and rational vertex pseudoinverse. The earlier small-cut dynamical certificate is not reused as a certificate for this writer.

**Explicit protocol revision:** shorten the maximum write duration from the PR117 control 1 to **49/100**, retaining the full **1/100** actuation delay. All rates, capacities, high/low guards, initial state and edge representatives remain unchanged. The numerical load guard still fires before this new deadline. The purpose is to put every admitted guard-or-timeout write inside a provable spectral window. This is a design choice, not a new UD constant. A timeout remains a timeout, not a certified load event.

## 2. Declared code and mechanism

Use the unit-metric 600-cell chain generator A, protected projector P and vertex source u=119. There are six frozen symbol representatives, one incident edge per fibration label:

| Symbol | Edge index | Neighbor of u |
|---:|---:|---:|
| 0 | 630 | 78 |
| 1 | 619 | 77 |
| 2 | 608 | 76 |
| 3 | 598 | 75 |
| 4 | 647 | 80 |
| 5 | 639 | 79 |

Each branch starts with c=e_u and z=m=w=0. The symbol chooses which cut A-E_e operates. The port shape and kinetics are

\[
F=\tfrac23 I_0+\tfrac1{12}I_1B_1^T,
\quad g_i=(1-b_i/C)_+,\quad C=1/50,
\]

\[
c'=(A-E_e)c+FGz,\quad
z'=-GF^Tc-z,\quad
m_i'=z_i^2-\tfrac15m_i,\quad
w_i'=\tfrac15m_i.
\]

All required stars are available. The high guard is max b_i=27/1850, the write deadline 49/100 and the fixed additional actuation delay 1/100. Let T denote actual restoration time. After restoration replace A-E_e by A; PF=0 then protects Pc exactly.

The conserved normalized resource is

\[
\mathcal E=\tfrac12\|c\|^2+\tfrac12\|z\|^2+
\sum_i(m_i+w_i)=1/2.
\]

All conclusions below are for these declared uniform coefficients and calibrated real amplitudes. The symbol/address and prepared carrier are charged inputs.

## 3. Exact symmetry gives a common response

The replay constructs six quaternion conjugations fixing u and sending the reference neighbor to the chosen neighbor. Their signed simplicial actions T_h and ordinary vertex permutations V_h satisfy exactly

\[
T_hA=AT_h,\quad T_hF=FV_h,\quad
T_hE_{e_0}=E_{e_h}T_h.
\]

Uniform capacities, rates, componentwise z_i^2 and max-buffer guards are invariant under V_h. Uniqueness of the locally Lipschitz flow therefore makes the six branch states conjugate. Their guard times, timeout times and restoration times coincide. These identities are verified on the full finite chain, rather than inferred from matching numerical times.

Let g_h be the outward signed edge unit vector and w_h=P_cyc g_h. Define the common scalar drive

\[
a(s)=c_{0,u}(s)-c_{0,v_h}(s).
\]

It is the same function for all six branches. Projecting the cut equation gives

\[
\boxed{Y_h(T):=Pc_h(T)
=K_Tw_h,\qquad
K_T=\int_0^T a(s)e^{A(T-s)}ds.}
\]

The safe recovery port affects a through the unprotected working dynamics, but has no direct protected output. This representation is exact for the declared nonlinear writer.

## 4. A certified restoration-time window

The shape column norm is ||f_i||^2=19/36. Capacity gives |z_i|<=sqrt(2b_i), and normalized storage gives ||c||<=1. Therefore

\[
b_i'\le\|f_i\|\sqrt{2b_i}(1-b_i/C),
\qquad
\boxed{b_i(s)\le C\tanh^2(ks),\quad k^2=475/36.}
\]

The comparison follows by setting v=sqrt(b/C), or by a regularized square-root comparison at b=0, and integrating v'<=k(1-v^2).

At s=1/3, k/3<11/9. The exact exponential bound exp(22/9)<12 gives tanh(k/3)<11/13. Hence

\[
b_i(1/3)<C\frac{121}{169}
<C\frac{27}{37}=\frac{27}{1850}.
\]

The comparison envelope is increasing, so no buffer can have reached the high guard earlier. The deadline is later than 1/3. On the other side, the deadline plus delay is 49/100+1/100=1/2. Consequently

\[
\boxed{1/3\le T\le1/2.}
\]

The exponential inequality is certified by a rational Taylor sum with a bounded positive tail. This timing envelope is an analytic result for the refined controller; it does not rely on the numerical guard time being accurate enough to locate a root.

## 5. Bounding the actual drive without assuming its sign

Write K_e=A-E_e and let the unforced reference be c_ref(s)=exp(K_e s)e_u, with a_0(s)=c_ref,u-c_ref,v. The incidence certificates give ||A||<4 and ||E_e||=sqrt(2), hence ||K_e||<6.

For completeness, the A bound follows from boundary nilpotence and orthogonality of the Hodge blocks. The vertex Laplacian's certified nonzero polynomial roots are 10 plus/minus 2sqrt(5), 9 plus/minus 3sqrt(5), 9,12,14,15, all below 16. For B2 and B3, absolute column/row-sum products bound squared norms by 15 and 8. The exact rational pseudoinverse identity certifies the vertex polynomial annihilation. Thus no floating-point largest eigenvalue is needed.

The port norm satisfies ||F||^2<=4/9+24/144=11/18<1. Since 0<=G<=I and z'=-GF^Tc-z,

\[
\|z(s)\|\le\|F\|s,\qquad
\|c(s)-c_{\rm ref}(s)\|\le\tfrac12s^2,
\]

so

\[
\boxed{|a(s)-a_0(s)|\le\tfrac34s^2.}
\]

The replay computes the reference Taylor coefficients delta^T K_e^j e_u/j! exactly through degree 15. Odd coefficients vanish. Taylor's integral remainder, ||delta||=sqrt(2)<3/2 and ||K_e||<6 give a uniform remainder at s<=1/2 bounded by

\[
R_{16}=\frac32\frac{3^{16}}{16!}.
\]

Rational Bernstein coefficients on the relevant intervals certify

\[
a_0(s)\ge-1/16\quad(0\le s\le1/2),
\qquad
\int_0^T a_0(s)ds\ge1/4
\quad(1/3\le T\le1/2).
\]

All coefficients and the stronger rational computed bounds are exported. Integrating the perturbation bound gives at most T^3/4<=1/32. Thus, for

\[
J=\int_0^T a(s)ds,\qquad
N=\int_0^T(-a(s))_+ds,
\]

we obtain

\[
\boxed{J\ge7/32,\qquad N\le1/16.}
\]

The argument deliberately allows a negative drive near the end of a write. Positivity of the entire waveform is not required.

## 6. Exact retained separation and decoder radius

Center the orthogonal response:

\[
\widetilde K_T=e^{-AT/2}K_T
=\int_0^T a(s)e^{A(T/2-s)}ds.
\]

Because ||A||<4 and |T/2-s|<=1/4, the symmetric part of each exponential lies between (1/2)I and I; cos(1)>=1/2 suffices. Split positive and negative a. Then

\[
\operatorname{sym}\widetilde K_T
\succeq\tfrac12(J-N)I
\succeq\frac5{64}I.
\]

For every v, v^T K_tilde v>=5||v||^2/64, so Cauchy-Schwarz gives ||K_tilde v||>=5||v||/64. Orthogonal centering does not change singular values:

\[
\boxed{\sigma_{\min}(K_T)\ge5/64.}
\]

The independently reconstructed six leading words have exact minimum squared distance 136907/75600>(5/4)^2. Therefore

\[
\boxed{\min_{h\ne j}\|Y_h-Y_j\|
\ge\frac5{64}\frac54=\frac{25}{256}.}
\]

Restored orthogonal evolution preserves this separation. Nearest-template decoding is guaranteed whenever the total error in protected signed amplitude is

\[
\boxed{e_{\rm total}<25/512.}
\]

The template must be at the actual calibrated recovery phase, or the readout must use a known co-rotating frame. Access to signed amplitudes, the frame, stored templates and a norm-bounded measurement error are declared readout assumptions. They are not supplied by the carrier equation.

An unprotected residual does not change ideal full-amplitude nearest-template decisions: all templates lie in W, so the squared norm of the observed U component adds the same term to every distance. This does not remove the need to measure the relevant amplitudes or bound their protected noise.

## 7. A finite contact-error and clock budget

After restoration only, let a reciprocal port fault change F to F+epsilon H, with H=I1 e_edge e_u^T, while retaining the same matched forward/reverse coupling and positive load/export laws. The protected norm of this single-edge port is rho^2=601/720, verified from the exact Gram reconstruction.

The actual trajectory still obeys signed storage dissipation integral ||z||^2 ds<=1/2 because D=I. Projecting and applying Duhamel plus Cauchy-Schwarz gives

\[
\|Pc_\epsilon(s)-e^{As}Y_h\|
\le|\epsilon|\rho\sqrt{s/2}
<16|\epsilon|\qquad(0\le s\le600).
\]

Local capacity remains invariant for this reciprocal fault because the contact still closes at b=C; no unmodified writing-guard bound is transferred to a faulty writer. The bound concerns a fault introduced after the codeword was prepared.

If nu is protected readout noise, e_T a certified template/preparation error and delta s the recovery-phase error, the unit carrier bound and ||A||<4 yield the sufficient budget

\[
\boxed{\nu+e_T+4|\delta s|+16|\epsilon|<25/512.}
\]

The actual storage age must be <=600. A phase error means the frame used for that readout is offset; it does not extend the age range silently. For example, nu<=1/100, e_T=0, |delta s|<=1/1000 and |epsilon|<=1/1000 give total bound 3/100<25/512. These are conservative dimensionless tolerances, not hardware specifications or a proven physical lifetime.

Writing imperfections that destroy the exact branch symmetry need their own preparation-error receipt e_T. They are not covered by the post-restoration contact-fault bound.

## 8. Six-branch replay and resource ledger

The new replay performs all six nonlinear writes and their full response delays. It stores the protected words, restoration states and pair distances in `CODEBOOK.npz`. Numerical branch times and stocks agree, corroborating the exact symmetry argument.

| Quantity | Result |
|---|---:|
| Guard time, all branches | approximately 0.4635449456 |
| Restoration time | approximately 0.4735449456 |
| Analytic minimum output distance | 25/256 |
| Numerical minimum output distance | approximately 0.3915309059 |
| Analytic decoder error radius | 25/512 |
| Retained protected squared norm | approximately 0.07025819823 |
| Retained normalized chain energy | approximately 0.03512909911 |
| Ultimate normalized export | approximately 0.46487090089 |

The six quadratic scores also select their supplied labels in this replay, but no exact score-gap certificate for this longer writer is claimed. The analytic result is for the nearest-template decoder. Six bounded-noise tests point toward a competing word with error norm 0.04 and recover the correct template; these examples corroborate rather than prove the universal radius.

The resource accounting is:

| Resource | Declared quantity / limitation |
|---|---|
| Carrier | 2640 real coordinates; the protected sector has dimension 2401 |
| Transport, local load, export receipts | 120 coordinates each; 3000 total with the carrier, excluding controller/readout |
| Local buffer provision | 120 x 1/50 = 12/5 aggregate normalized capacity; not extra initialized storage |
| Initial normalized storage | 1/2 |
| Finite collector provision | Capacity 2; retained energy plus ultimate export equals 1/2 |
| Reuse | Accumulated export consumes collector capacity; resetting local loads does not renew the collector |
| Classical input | One of six supplied addresses; a uniform label carries log2(6) mathematical bits |
| Readout | Calibrated signed amplitudes, recovery phase and six templates; implementation cost open |
| Control | Guard detection, coordinated stopping, timer and matched contacts; physical costs open |

The code transports a supplied distinction; it does not create log2(6) bits from an unlabeled source. An exact six-label bounded-noise channel can retain those labels under the stated readout contract, but this is not a thermodynamic entropy normalization.

There is still no information-per-physical-area result. The 600-cell boundary is a closed three-dimensional complex with no free external triangular faces. Its 1200 triangles are internal interfaces between tetrahedra, not a supplied two-dimensional horizon area. A chosen control boundary and physical metric/area map would be separate required inputs. Dividing by the face count would not supply them.

## 9. Verification and next closure

The package records 53 exact checks and 17 numerical corroborations, plus a clean-directory replay. The exact checks include full signed automorphisms, port/writer covariance, rational timing inequalities, Taylor/Bernstein bounds, leading Gram geometry, retained-distance and error-budget arithmetic. Universal consequences are proved above; numerical ODE solutions are corroborations rather than validated interval integration.

During construction, fixed-width NumPy integer coefficients contaminated Fraction arithmetic and caused an overflow before the bound checks. Explicit Python-integer conversion repaired the constructor. No bound was weakened or numerical result relabeled as exact. This implementation correction is recorded in `VALIDATION_NOTE.json`.

The next useful target is a measurement and reuse model: derive a permitted readout that distinguishes the six signed patterns, carry its noise and storage cost, and give the finite collector a sourced renewal protocol. Native source/address selection, stock normalization and physical units remain open. This report is a separate manuscript-development addendum; it does not overwrite a frozen manuscript or promote the candidate mechanism.
