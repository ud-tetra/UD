# Unified Dynamics: source-admitted quadratic support observer and the O09 phase-reference gate

**Artifact:** `UD_NATIVE_QUADRATIC_OBSERVER_GATE_v0.1`  
**Date:** 2026-11-01  
**Status:** **EXACT / SCOPED** (native grade-stock/flow observer, its double-frequency response, signed-
\(S_4\) covariance, and observation non-injectivity); **DERIVED / CONDITIONAL** (normalized complex stock-flow packaging); **NO-GO / SCOPED** (cardioid and absolute-phase extraction from even quadratic readouts alone); **OPEN_GATED** (O09 source selection of absolute/relative reference and physical readout).  
**Physical promotion:** **0**. Non-constructor review pending.

## 1. Result and original question

The preceding rolling-circle analysis showed that a *chosen* complex observer \(2u-u^2\) converts one filled-tetrahedron Hodge oscillator into a cardioid. The unproved step was why UD would select that observer. This audit determines whether the currently recovered UD source contracts themselves contain a nonlinear observation mechanism, without choosing an output because it draws a familiar curve.

**Answer:** Yes, a **quadratic stock observer and its signed current** are already in the current mathematical source ledger (Q165/Q166/Q169/Q170). Their exact readout can be combined into a phase-doubled circle with a normalization fixed by the finite operator and the conserved stock. **No**, the sources do not select the complex *cardioid* or an optical detector. O09 itself contains phase **increments**, not a fixed absolute phase reference or a nonlinear apparatus coupling.

All frequency statements below concern an internal evolution parameter \(s\), not seconds or optical hertz. All support stocks are squared real simplex coordinates in the declared unit metric, not material energy or probability distributions.

## 2. Precise source register and types

| Source, version | Typed object / source statement | Use in this audit | Boundary |
|---|---|---|---|
| UD public Paper I, §4.3 | Filled oriented \(\Delta^3\), \(A=B^\mathsf T-B\), \(A^2=-4(I-P_0)\) | Exact closed finite evolution | No physical clock |
| Coefficient ledger `library_LEDGER_v0.85.json`, recovered 2026-10-21, inherited scientific revision `v0.43`, Q165 | \(S_\mu^\mathrm{rev}=\|c_0\|^2+\|c_1\|^2+\|c_2\|^2+\|c_3\|^2\) | Native quadratic carrier/grade stocks | Real simplex-coordinate metric |
| Same, Q166 | \(J_{01},J_{12},J_{23}\) = signed incidence bilinear support currents | Native signed readout of stock exchange | No physical current units |
| Same, Q169/Q170 | Full unique-simplex skew Hodge generator and region \(S(R)=\sum_{\sigma\in R}c_\sigma^2\) | Region = *all six edges* is a lawful fixed region | Different choice of region changes response |
| Same, Q76–Q79/Q84 | Conditional chain/seam coherence \(\cos\Delta\phi\), magnitude \(|\cos\Delta\phi|\), burden \(-\ln|\cos\Delta\phi|\) | Independent nonlinear phase-readout comparison | Branch-to-physical phase map OPEN |
| Same, O09 | \(\mathcal I_\mathrm{lift}=\frac12\sum_{\omega>0}a_\omega\Delta\widetilde\phi_\omega\) | History/action provenance | Does **not** prescribe a detector or absolute reference |
| Same, G05 | Former universal loop-action scalar retired | No scalar reused | Cannot infer physical coupling |

The v0.85 **filename version** and inherited v0.43 **scientific revision** are distinct provenance fields; archived v0.39 (2026-08-22) is not silently made current. Current program portal: https://unified-dynamics-public.ben-w-mayes.chatgpt.site/mathematics/ and https://unified-dynamics-public.ben-w-mayes.chatgpt.site/evidence/ledger-recovery/.

## 3. Theorem 1 (native quadratic stock produces exact frequency doubling)

**Carrier:** \(\mathcal C=\bigoplus_{k=0}^{3}C_k(\Delta^3;\mathbb R)\), with \(\dim\mathcal C=(4,6,4,1)\), total 15.  
**Boundary:** signed incidence \(B:\mathcal C\to\mathcal C\) satisfying \(B^2=0\).  
**Generator:** \(A=B^\mathsf T-B:\mathcal C\to\mathcal C\), skew under the native unit metric.  
**Initial condition:** any \(x\in C_1\setminus\{0\}\), all other grades zero. \(q=\|x\|^2>0\).  
**Evolution:** \(X(s)=e^{sA}x\).  
**Observable:** \(S_k(X)=\|P_k X\|^2\), \(P_k\) the complete grade-\(k\) coordinate projector. This is source-defined Q165/Q170 for a specified region.

Since \(x\in C_1\) is orthogonal to the only harmonic mode (the constant vertex direction), \(A^2x=-4x\). Also \(Ax=-B_1x+B_2^\mathsf T x\) lies in \(C_0\oplus C_2\). Hence

\[
X(s)=\cos(2s)x+\tfrac12\sin(2s)Ax,
\qquad S_1(s)=q\cos^2(2s)=\frac q2\bigl(1+\cos4s\bigr).
\]

Define \(\alpha_x=\|B_1x\|^2/(4q)\), \(\beta_x=\|B_2^\mathsf T x\|^2/(4q)\). The exact edge Laplacian identity

\[
B_1^\mathsf T B_1+B_2 B_2^\mathsf T=4I_{C_1}
\]

shows \(\alpha_x+\beta_x=1\). Thus the other stocks are

\[
S_0(s)=q\alpha_x\sin^2(2s),\qquad
S_2(s)=q\beta_x\sin^2(2s),\qquad
S_3(s)=0.
\]

For **any single unit oriented edge**, the two incident vertices and two incident triangular faces give \(\alpha_x=\beta_x=1/2\). Therefore \((S_0,S_1,S_2,S_3)=(\tfrac12\sin^2 2s,\cos^2 2s,\tfrac12\sin^2 2s,0)\).

**EXACT CONCLUSION:** The accepted finite dynamics has oscillatory frequency 2 but its declared quadratic *edge-degree stock* has period \(\pi/2\) and nonconstant Fourier frequency 4. The \(1/2\) Fourier coefficient is the exact consequence of squaring, **not a physical fit or added frequency source**.

## 4. Theorem 2 (native stock and signed flow give a phase-doubled circle)

Use the source-current orientation (the sign can be changed only together with the incidence convention)

\[
J_{01}=2c_1^\mathsf T B_1^\mathsf T c_0,\qquad
J_{12}=2c_2^\mathsf T B_2^\mathsf T c_1.
\]

Under \(\dot X=AX\), the micro support continuity identities are

\[
\dot S_0=-J_{01},\quad \dot S_1=J_{01}-J_{12},\quad
\dot S_2=J_{12}-J_{23},\quad \dot S_3=J_{23}.
\]

On the pure-edge initial-state orbit,

\[
J_{01}=-2q\alpha_x\sin4s,\qquad
J_{12}=+2q\beta_x\sin4s,\qquad
J_{12}-J_{01}=2q\sin4s.
\]

Consequently the **declared diagnostic packaging** of two accepted source observables,

\[
\boxed{W(X)=\left(\frac{2S_1(X)}{q}-1\right)
+i\frac{J_{12}(X)-J_{01}(X)}{2q}=e^{4is},}
\]

has a perfectly circular trace and \(|W|=1\) on this restricted initial-state orbit. The numerical normalization is fixed by \(q\) and the known Hodge frequency, with **no fitted dimensionless coefficient**. Packaging two real channels as a complex number is a declared convention, not a demonstrated unique physical detector.

Both \(S_1\) and \(J_{12}-J_{01}\) are invariant under a *simultaneous* signed permutation of all vertex labels: the signed \(S_4\) action commutes with \(A\), respects grade projectors, and carries the incidence bilinear to itself. The full 24-element check passes.

## 5. Theorem 3 (observer two-to-one quotient and cardioid no-go)

The *native* state has \(X(s+\pi/2)=-X(s)\) and period \(\pi\). All Q165/Q170 quadratic stocks and Q166 bilinear currents satisfy \(F(-X)=F(X)\). Hence

\[
W(s+\pi/2)=W(s),\quad X(s+\pi/2)=-X(s).
\]

Thus the source-admitted even readout cannot distinguish \(+X\) and \(-X\); it is a genuine mathematically non-injective observation, **not** measured quantum decoherence or physical loss.

The earlier cardioid candidate takes a **sign-sensitive modal phase** \(u=e^{2is}\) and reports \(Z=2u-u^2\). Under \(X\mapsto-X\), \(u\mapsto-u\), giving \(Z(-u)=-2u-u^2\ne Z(u)\) when \(u\ne0\). Therefore the cardioid's first harmonic **cannot** be reconstructed by any function of the even stock-and-current observables alone. An odd/sign-sensitive native phase reference, a marked edge/observer, or an additional measured channel is necessary. None is selected by Q165/Q166/O09.

## 6. Theorem 4 (O09 alone cannot select absolute phase)

O09 is stated as a sum of positive-frequency **phase increments** and modal weights. Increments \(\Delta\phi=\phi_\mathrm{final}-\phi_\mathrm{initial}\) do not change when both phases receive a common constant offset \(\theta\), **holding the modal actions \(a_\omega\) fixed**. The absolute complex phase \(u=e^{i\phi}\) and cardioid \(2u-u^2\) **do** change under this offset. Two phase histories can thus have identical O09 data but different cardioid readouts.

**NO-GO under O09-only information:** no unique absolute-phase nonlinear observer follows from the recorded O09 increment functional. A phase reference/section and a selection rule for the actual observable are independent required inputs.

## 7. Independent phase-coherence readout comparison

The accepted *conditional* Q76/Q77/Q78 chain-phase observables already include nonlinearities:

\[
K_\mathrm{chain}=\cos\Delta\phi,\quad
\Gamma_\mathrm{chain}=|\cos\Delta\phi|,\quad
D_\mathrm{chain}=-\ln|\cos\Delta\phi|.
\]

If (as an **added identification**) \(\Delta\phi(s)=2s\), then \(K_\mathrm{chain}\) has the native first harmonic, \(\Gamma_\mathrm{chain}\) has period \(\pi/2\) and all even harmonics, and \(D_\mathrm{chain}\) diverges at \(\cos(2s)=0\) while \(X(s)\) remains regular. The exact Fourier series is

\[
|\cos\phi|=\frac2\pi+\frac4\pi\sum_{n=1}^\infty
\frac{(-1)^{n-1}}{4n^2-1}\cos(2n\phi).
\]

Likewise \(K_\mathrm{chain}^2=\tfrac12(1+\cos2\Delta\phi)\), but **squaring that kernel as a measured probability** is new postprocessing unless a physical readout rule is independently admitted. Q78's small-phase series \(D=\phi^2/2+\phi^4/12+O(\phi^6)\) agrees with Q79. Q76's branch-to-phase source and Q84's apparatus forcing remain open.

A single reference-free U(1) modal phase \(u\) of unit modulus has no nonconstant *phase-invariant* quadratic scalar: all such real quadratic invariants have form \(c|u|^2=c\). The nonconstant grade-stock observer is invariant under **S4 vertex relabeling**, not under arbitrary phase rotations within its selected dynamical orbit; these symmetries must not be conflated.

## 8. Reproducibility and strongest counterexamples

`exact_source_observer.py` independently constructs the filled 15D signed boundary, verifies the operator, all six single-edge preparations, the general six-parameter edge initial state, the source currents, 24 signed S4 permutations and nonlinear two-channel identity. 

`independent_numeric.py` independently constructs the incidence matrices and uses eight random normalized edge preparations, 4096 samples, Fourier coefficients and a sign-quotient test. The maximum discrepancy is \(8.882\times10^{-16}\). The normalized stock Fourier components on \(s\in[0,\pi)\) are DC \(1/2\) and coefficient \(1/4\) at ±2 cycles (internal oscillatory source ±1 cycle). 

`coherence_kernel_audit.py` separately verifies Q76/Q77/Q78 identities, Q79 expansion, the first four exact Fourier coefficients of \(|\cos\phi|\), and the U(1) reference-free quadratic invariant obstruction. All three scripts pass. Exact and numerical JSON receipts are included.

Adversarial checks: non-pure-edge initial states need not give \(|W|=1\); a linear grade observable would not satisfy the quadratic doubling statement; the branch-to-physical phase mapping is open; a calibrated detector need not measure these canonical mathematical stocks; a nonzero frequency in *a measured stock* is not a new eigenfrequency of \(A\). None of these mathematical observations promotes an optical, lepton, cosmological or instrument-error claim.

## 9. Decision and next source gate

**AUTO_LOCK (scoped mathematical):** the selected source stock \(S_1\) and Q166 signed flows have a parameter-free doubled-frequency response on the filled K4 pure-edge initial-state orbit, with an \(S_4\)-covariant two-channel circular packaging.

**AUTO_FREEZE (unsupported promotion):** the assertion that O09 uniquely selects the cardioid coefficients, an absolute phase reference, a physical detector gain, or a laboratory correction factor.

**OPEN_GATED:** recover a source-approved orientation/phase-reference channel and physically qualified readout/detector. Freeze its functional, domain, normalization, variance and source units before comparing to a known target. Keep the distinction between **internal source harmonics**, **quadratic observation harmonics**, and **physical spectra**.

**Physical promotion remains 0.** This record is constructor-checked exact mathematics, not independent scientific review or publication of a new measured law.
