# UD held-out sampled validation v0.1

**RESULT / STATUS — REPAIRED PROPOSAL; DERIVED CONDITIONAL certificate.**
The supplied script cannot validate the fitted UD generator. It does not
parse as written, substitutes random dense matrices for the frozen model,
and constructs its purported truth directly from its prediction. Its residual
therefore measures the injected noise. Its thresholds also omit the certified
parameter uncertainty. The replacement package provides three frozen rational
probes, the actual 600-cell incidence generator, a finite propagator with
certified numerical error, exact residual decisions and synthetic fault controls.

The correct sampled threshold is

\[
 \boxed{\tau(t)=\frac{11}{2^{49}}+\frac5{2^{39}}t,\qquad
 t=j/32,\quad j=0,\ldots,24.}
\]

This is a sufficient null envelope under the stated model and metrology
receipts. A pass means consistency at the selected samples. No experimental
pass, unrestricted model identification, asymptotic stability or physical
promotion is claimed. Constructor verification passed; independent review
pending. Development lane; no registry entry.

## 1. Repairs to the synthesis and script

The previous six-ratio certificate proves a nonzero parameter-error bound by
exact arithmetic and interval inequalities. It does not make estimated
parameters exact. Three preparations and twelve readings were sufficient;
global minimality was not proved. The twelve readings consist of six initial
gain values and six outputs after one positive interval h=1/32. They are not
twelve time steps. The four auxiliary ports provide additional readout access,
not an invariant separation of shell and bulk. Inversion defect in normalized
ratio coordinates and raw measurement noise have different scaling.

The proposed code contains an invalid decimal literal `822d407`. Interpreting
the commit prefix as hexadecimal would fix syntax but would not make a random
matrix the certified UD operator. The real source is a sparse 2640-dimensional
incidence generator with 14880 signed entries and a fixed coordinate selector
R of norm 1. A generic fitted grade-scalar generator is skew with respect to
its fitted positive metric; it need not be Euclidean-skew.

The sign preparations already have squared norm 2640/52^2=165/169; floating
square-root rescaling is unnecessary. Gaussian draws do not obey a deterministic
hard noise bound. The draft evaluates the spectral norm but specifies a
Frobenius gate; it then compares the peak against 2^-39 instead of 2^-49.
The copied value 2^-55 bounds logger-interval error in the calibration contract,
not integrated residual energy. No transfer between these typed quantities was
proved.

Euler stepping is not exponential propagation: for real skew A,

\[
 \|(I+hA)x\|^2=\|x\|^2+h^2\|Ax\|^2.
\]

It increases the Euclidean stock on every active input. Finally,
`range(24)` reports states at times0,...,23/32. Twenty-four intervals through
24/32 require **25 snapshots**. This is a short finite horizon, rather than
a test of long-term recurrence or asymptotic stability. `AUDIT.json` records
18 scoped findings. The supplied script was statically inspected, not executed.

## 2. Frozen probes and acquisition plan

The new preparations X=[x38,x39,x40] have exactly 2640 coefficients each,
all ±1/52. Signs come from SHAKE256 using the domain recorded in DESIGN.json,
little-bit order and a2640x3 row-major layout. The numbering is a label;
freshness comes from the separate design and its frozen hash, not the numbers.
There is no assertion of statistical independence merely from different labels.

Each input has squared norm165/169; the combined squared Frobenius norm is
495/169. An exact modulo1009 Gram check proves that the three new inputs,
the previous37 history inputs and the three calibration inputs are jointly
linearly independent: rank43. This does not prove full dynamical excitation.

Use the original62-coordinate shell readout, at t_j=j/32 for j=0,...,24.
This requires **25x62x3=4650 scalar readings**. The first13 snapshots cover
0 through12/32; all25 cover0 through24/32=3/4. Those horizons are new protocol
choices. They do not inherit a twelve-step calibration horizon.

Freeze the actual six fitted effective ratios, probes, time grid, source hashes
and thresholds before examining validation outputs. Validation outputs must not
be used for parameter selection. The prediction file binds the fitted ratios,
source operator, design, engine and certificate through hashes. Hardware data
must be independently supplied. Synthetic controls are always labelled as such.

Only two of these62 channels were among the six diagnostic ports calibrated
previously. All62 gain corrections therefore require uncertainty receipts;
the twelve-value calibration alone does not supply them. Blank/offset correction
is included in the required noise receipt. No blank run is included in4650.

## 3. Null model and uniform propagator bound

Let K=K(q) and Khat=K(qhat) use the frozen incidence signs, with positive
effective ratios D1,U1,D2,U2,D3,U3 in Omega=[15/16,17/16]^6. These are
logger-time ratios, with the constant clock scale absorbed. Use the previous
uniform vector error delta=2^-40, conservatively above its tighter interval
bound. On the orthogonal incidence channel spaces,

\[
 \|K-Khat\|\le4\|q-qhat\|_\infty\le4\delta=:e=2^{-38},
 \qquad\|K\|,\|Khat\|\le\omega=17/4.
\]

Recover representative grade metrics h0=1 and
h_k=product_(j<=k)(D_j/U_j). The logarithmic metric spread across at most
three grade steps is bounded by3 log(17/15). Both propagators are thus bounded,
uniformly at every signed time, by

\[
 \|e^{tK}\|,\|e^{tKhat}\|
 \le g=(17/15)^{3/2}<1.206526.
\]

This uses metric skewness, avoiding an unnecessary exponentially growing
error estimate. Duhamel's identity gives

\[
 \|e^{tK}-e^{tKhat}\|\le g^2 e t\quad(t\ge0).
\]

It is a bound for the declared positive grade-scalar family; it cannot be
assumed for arbitrary extra generators or arbitrary time-varying systems.

## 4. Predictive thresholds from the complete error budget

Let b=||X||F=sqrt(495)/13. Under the joint null, gain-normalized readout is
C=R+E with ||E||≤rho. In the diagonal readout family, the external individual
gain uncertainties yield this modeled operator bound. Cross-talk beyond the
null is an alternative being tested, not something that three probes certify
absent. The remaining required ceilings are:

| Quantity | Exact ceiling | Scope |
|---|---:|---|
| Modeled62-channel gain/readout uncertainty rho | 2^-47 | Operator norm under the readout null |
| Preparation error xi | 2^-49 | Frobenius norm, all three runs combined |
| Corrected output noise nu | 2^-49 | Frobenius norm of62x3 matrix, at each sample |
| Timing error j | 2^-55 | Each validation run, logger units |
| Prediction numerical error eps | 2^-70 | Frobenius norm at each sample |

The parameters, gain corrections and model family must remain valid throughout
all calibration and validation runs. Receipt identifiers are external evidence
references; the module checks their presence and does not claim to verify their
truth. Missing receipts leave the result incomplete.

Separating generator, gain, preparation, timing, noise and numerical errors
gives, at each selected node,

\[
 \|R e^{tKhat}X-Y(t)\|_F\le a_0+a_1t,
\]
\[
 a_0=g[(1+\rho)\xi+\rho b+(1+\rho)b\omega j]+\nu+\epsilon,
 \qquad a_1=b g^2 e.
\]

The timing term allows different interval errors in the three runs; their
combined Frobenius contribution uses b. Uniform256-bit interval arithmetic
verifies

\[
 a_0<11/2^{49},\qquad a_1<5/2^{39}.
\]

Hence the boxed affine threshold strictly covers the null envelope. It includes
calibration uncertainty, rather than demanding raw noise-level prediction from
an uncertain fitted generator.

| Logger time | Exact gate | Approximate gate, display only |
|---:|---:|---:|
| 0 | 11/2^49 | 1.953993e-14 |
| 1/32 | 171/2^49 | 3.037570e-13 |
| 12/32 | 1931/2^49 | 3.430145e-12 |
| 24/32 | 3851/2^49 | 6.840751e-12 |

The module compares exact rational squared Frobenius norms with exact squared
thresholds. A node at or above threshold rejects the joint contract. This
does not assign a cause: preparation, timing, readout, generator, drift or
other model discrepancies can produce the same rejection.

## 5. Finite numerical implementation and controls

`validation_engine.py` uses the actual sparse incidence data. It forms integer
weighted powers, evaluates a degree80 Taylor series in256-bit Arb arithmetic,
and rounds predictions to exact dyadic rationals. At T=3/4, the uniform vector
Taylor remainder is bounded by

\[
 b e^{\omega T}(\omega T)^{81}/81!<2^{-100}.
\]

For every entry, an interval check certifies error from series evaluation and
dyadic rounding <2^-79. Combining186 entries and the vector remainder keeps
prediction error below2^-70. Alternative controls also pass an explicit
generator-norm certificate. No Euler stepping or random dense replacement is
used. The ordinary real norm and exponential remain separate from mod13 field
arithmetic; p=13 in the draft did not define its real propagator.

Ten gate tests pass, including these substantive controls:

| Control | Result and scope |
|---|---|
| Nominal fitted model | Consistent at every sample |
| True D1=1+2^-45, fitted D1=1; others1 | Realizable within the calibration noise budget; passes corrected gate but fails proposed2^-49 gate at12/32 |
| Readout C=R+2^-30 e_output0 e_input0^T | Rejected at t=0; twelve calibration readings unchanged because this output is uncalibrated |
| Generator A+2^-20(e33 e0^T−e0 e33^T) | Rejected at t=1/32; positive control of the response gate, with no claim it passes calibration first |

The allowed-ratio control has residual about3.16e-15 at12/32, exceeding the
proposed2^-49 gate despite being a legitimate calibrated null member. This is
a concrete counterexample, not merely an oversized conservative bound. The
six raw response changes can be canceled by calibration noise with combined
norm below2^-49, leaving observed data equal to the unit-ratio finite response.
The parent finite-map polynomial and its remainder certify this realization.

The cross-talk control has exact t0 signal norm2^-30 sqrt(3)/52, approximately
3.1021e-11, well above the t0 threshold and its bounded measurement uncertainty.
For the restricted single-coefficient fault family, its static singular value
is sqrt(3)/52. Conditional passage bounds that one coefficient below2^-39;
the interval-enclosed bound is1.153e-12. This does not bound arbitrary cross-talk.

The engine additionally rejects mismatched locks, modified predictions, malformed
dimensions and float-valued decision inputs. Synthetic controls never generate
an empirical validity claim. A source-hash check and isolated fresh-directory
replay reproduce the certificate, probe arrays, audit and control results.

## 6. Sampled energy and continuous-time limit

Report the explicitly sampled diagnostic

\[
 E_{grid}=\sum_{j=0}^{24}w_j\|r(t_j)\|_F^2,
 \quad w_0=w_{24}=1/64,\quad w_j=1/32\ (1\le j\le23).
\]

Its threshold is the exact rational sum of w_j tau(t_j)^2, approximately
1.174258e-23. It is redundant when all node gates pass, and is not an
independently measured continuous integral or a conserved stock.

Finite sampled passage does not control the continuum. For any unit output
matrix V, the smooth discrepancy

\[
 r(t)=2^{-20}\sin(32\pi t)V
\]

vanishes at every grid node, yet its squared Frobenius integral on[0,3/4]
is3/2^43, which exceeds2^-55. Independent regularity or quadrature control is
required to infer a continuous energy inequality. Under the null and only
if the same error receipts hold at every intermediate time, integrating the
affine envelope gives a separate conditional upper bound1.165e-23. The finite
test does not establish those all-time receipts.

## 7. What three probes cannot certify

At the frozen nominal A, its degree105 minimal polynomial bounds the cyclic
span of three validation inputs by315. At least2325 input directions per
arbitrary readout row can therefore remain blind, even with every possible
time sample on these inputs. Adding the three calibration inputs gives a
span upper bound630 and at least2010 blind directions per row. These counts
use nominal A; the same polynomial is not asserted for generic unequal rates.

The original62-channel observer also has its inherited747-dimensional nominal
dynamical kernel. A skew generator perturbation supported entirely in that
invariant kernel remains invisible to this readout for all preparations.
Distinct preparations and many samples do not remove that obstruction.

Consequently, this package tests specified predictive alternatives. It does
not establish full-domain readout or generator bounds required by the history
instrument certificate. To derive those bounds, restrict the fault family and
prove an observation lower bound for that family, or enlarge the independent
input/readout design. A short finite grid also leaves unsampled drift and
arbitrary nonlinear alternatives unresolved.

## 8. Governance and next action

The previous commit822d407 remains an immutable source. This audit corrects
the newly supplied proposal and supersedes none of that commit's certified
calibration inequalities. Exact construction, conditional derivation, proposed
metrology and empirical execution remain separate. The source coefficient
ledgerO03 keeps all thresholds as protocol controls; Q139's physical time gap
remains open; Q165/Q169 retain the scoped support/generator interpretation.
The CRL2 amendment is a proposal, and no registry promotion is made. Independent
review is pending. Physical promotion stays0. No public push, PR or merge occurs.

Recommended next step: freeze a restricted readout/generator fault family and
derive a detection lower bound that turns held-out passage into the specific
operator-error bounds needed for the subsequent history acquisition.
