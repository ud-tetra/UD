# UD restricted-fault to history certificate v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; constructor verification PASS.**
The inherited local probe design can certify operator bounds sufficient for
the history instrument, within a declared fault family. Two changes are needed:
test generator coefficients forbidden by every grade-scalar background, and
replace the earlier low-order derivative estimator by a tenth-order finite
stencil. Conditional passage gives

\[
\boxed{\|C-R\|\le2^{-57},\qquad\|S\|\le2^{-47}.}
\]

Including these defects in a fresh calibration error derivation gives
\(\|\widehat q-q\|_2<7.401\times10^{-13}<2^{-40}\).
Thus the diagonal-model calibration is not assumed valid in order to validate
the diagonal-model hypothesis. The permitted family is essential; passage
does not establish that an arbitrary plant belongs to it.

The proposed diagnostic requires591948 scalar readings and a total response
error ceiling2^-64 per coded189-output vector. No apparatus implementation or
independent review is claimed. Development lane; no registry entry. Physical
promotion remains0.

## 1. Frozen source and declared family

All statements apply in a selected, fixed normalized chain coordinate frame.
The real2640-dimensional600-cell incidence generator A has14880 signed entries
and grade dimensions(120,720,1200,600). The189-coordinate diagnostic readout
contains the original62-channel history readout. The source260-code design,
operator matrices and parent certificates are included with hashes.

Assume throughout diagnosis, calibration and the later history batch:

\[
 H=H_0+S,\quad H_0=\operatorname{diag}(h_k I_{f_k}),\quad
 K=(H_0+S)^{-1}A_w,\quad A_w=\sum_{k=1}^3w_kA_k.
\]

The coarse positive h_k and w_k lie in[15/16,17/16]. The background ratios
w_k/h_(k-1),w_k/h_k also lie in that interval. Logger scale is absorbed in w.
S is a symmetric same-grade off-diagonal defect supported on the2574 listed
pairs. Its nonzero pairs form a matching: no coordinate belongs to two active
pairs. Each pair has at least one observed endpoint. Initially ||S||≤1/16.

The allowed pairs are the inherited same-grade, Hasse-distance-two rule, plus
the explicitly named pair(0,4). That additional pair remains a candidate
extension; it is not implied by the distance rule. Diagonal metric heterogeneity,
cross-grade defects, interacting nonmatching pairs and extra generator terms
are excluded. In particular J=0 is a family restriction, not an experimental
inference from these tests.

The corrected readout C is189x2640. C−R has support only in the inherited
local row stencils, including their diagonal entries. A coarse ||C||≤2 receipt
is sufficient for the component error contract below. Nothing in the local
probe tests proves absence of off-stencil readout terms. Parameters are fixed
through all runs; finite repeated epochs do not establish arbitrary future
stability or global linearity.

The incidence channels have orthogonal active spaces, Ai Aj=0 for i≠j, and
the inherited norm bound is ||A||<4. Consequently

\[
 \|K\|\le\frac{4(17/16)}{15/16-1/16}=34/7<5.
\]

The new replay checks channel annihilation, source identity, signs and grade
parity. The full spectral norm result is inherited from the frozen frequency
certificate, with largest squared frequency9+3sqrt(5)<16.

## 2. Local code and static readout bound

Keep the260 parity-separated color classes from the earlier deterministic
design. Preparation p_c has coefficient1/q_c on every coordinate of color c,
zero elsewhere, where q_c is an integer from1 through5. Each preparation has
Euclidean norm at most1. Within any allowed readout row stencil, all input
coordinates have distinct colors. Thus every one of the16175 allowed readout
coefficients has its own observed(row,color) data cell. The restricted code
has smallest singular value at least1/5.

At time0, decode that cell by multiplying by q_c and subtracting the known
identity entry of R. If each blank-corrected output vector has total error at
most epsilon=2^-64, the decoded global Frobenius error is at most

\[
 \tau_C=\sqrt{\sum_cq_c^2}\,\epsilon
       =\sqrt{2073}\,2^{-64}.
\]

Require the decoded residual Frobenius norm to be strictly below
T_C=23/2^63. Then

\[
 \|C-R\|\le\|C-R\|_F<T_C+\tau_C<2^{-57}.
\]

Unused static data cells have gate17 epsilon, above sqrt(260) epsilon.
They provide an additional discrepancy screen using the same data, but do not
remove all off-stencil aliases. Both static gates are required at each epoch.

## 3. Fit-independent metric visibility

For observed coordinate r, let N_r be the native nonzero columns of A's row r.
Decode only generator columns outside N_r. Those coefficients vanish for
every admissible diagonal H0 and native w, irrespective of their fitted values.
No uncertain fitted-generator subtraction is used in this test.

If matching pair(r,t) carries defect s, the inverse metric block has
off-diagonal entry−s/(h_grade^2−s^2). On the forbidden columns N_t minus N_r,
the own native row contributes zero. Therefore

\[
 K_{r,N_t\setminus N_r}
 =\frac{-s}{h_{grade}^2-s^2}(A_w)_{t,N_t\setminus N_r}.
\]

An exact exhaustive incidence check finds at least three exclusive native
neighbors for every listed pair's observed endpoint. A minimum witness is
(1680,840). Since every native weight is at least15/16,

\[
 \|K_{r,\mathrm{forbidden}}\|_2\ge c_S|s|,
 \qquad c_S=\sqrt3\frac{15/16}{(17/16)^2}.
\]

This proof works for arbitrary unknown matching subsets. The matching
restriction gives ||S||=max|s|, so row-wise passage controls the full metric
defect operator. Without that restriction, different partners can interfere
and this lower bound is not asserted.

## 4. Finite stencil and decoded-error theorem

Use h=1/128 and time samples0,h,2h,3h,4h,5h. Define

\[
 D_hY=\frac{2100Y(h)-600Y(2h)+150Y(3h)-25Y(4h)
                 +2Y(5h)-1627Y(0)}{1260h}.
\]

For a preparation of opposite parity to an output row, the ideal native
trajectory contains only odd Taylor powers. The weights a_k are
(5/3,−10/21,5/42,−5/252,1/630). They reproduce the derivative and cancel
orders3,5,7,9. Their exact moment-generating identity is

\[
 \sum_{r\ge0}M_rt^r
 =\sum_{k=1}^5\frac{a_kk}{1-k^2t}
 =1+\frac{14400t^5}{\prod_{k=1}^5(1-k^2t)}.
\]

All remaining coefficients are nonnegative. Thus with Omega=5, the ideal
derivative remainder is bounded uniformly by

\[
 B_h=\frac{\sum_{k=1}^5a_k\sinh(k\Omega h)-\Omega h}{h}
 <1.493\times10^{-17}.
\]

Readout cross-talk can introduce even powers, so its error is bounded using
the full exponential rather than invoking native parity. Define

\[
 F_h=\Omega\sum_{k=1}^5|a_k|k e^{k\Omega h},\qquad
 N_h=(|\sum a_k|+\sum|a_k|)\epsilon/h.
\]

Subtracting the zero-time term cancels constant readout contamination. After
local decoding, every forbidden row estimate has error at most

\[
 \tau_K=\sqrt{991}\,[B_h+(T_C+\tau_C)F_h+N_h]
 <3.803\times10^{-15}.
\]

Require every decoded forbidden row norm to be strictly below
T_D=9/2^51, approximately3.997e-15. Then

\[
 \|S\|\le(T_D+\tau_K)/c_S
 <5.423\times10^{-15}<2^{-47}.
\]

This is the required detection lower bound turning restricted-family passage
into a global metric error bound. It is not a proof of the fault family's
membership from finite data. `restricted_gate.py` implements the static,
unused-cell and forbidden-row tests using exact rational squared norms.

## 5. Measurements and precision burden

At each of two epochs, use260 coded preparations plus one blank, six times and
189 outputs:2x261x6x189=591948 scalar readings. A subsequent separate six-ratio
calibration adds12 readings, total591960. The constant-parameter assumption
must connect these epochs to later acquisition; two epochs alone do not prove it.

The total blank-corrected response error receipt epsilon=2^-64 is required
for each coded output vector and time. A sufficient component contract is:

| Quantity | Exact ceiling | Scope |
|---|---:|---|
| Full preparation state error | 2^-68 | Per unit-norm coded preparation |
| Logger interval error | 2^-71 | Per sample |
| Blank-corrected additive noise | 2^-66 |189-output Euclidean vector |
| Computation/readout representation error | 2^-66 | Same vector norm |

Using ||C||≤2, ||K||≤5, maximum time5/128 and the exponential envelope<5/4,
these four contributions sum below2^-64. Other component allocations are
allowed if the same total-response inequality is certified.

This response requirement is about1.84 million times tighter than the earlier
1e-13 local-validation contract. It is a mathematical sufficient requirement,
not evidence that a physical instrument can realize it. Precision values are
protocol controls under ledgerO03, never theory constants. Blank correction
error is included in the total receipt; it is not assumed free.

## 6. Re-derive calibration with the now-bounded defects

The original six-ratio proof assumes a diagonal grade metric and diagonal
readout. Its conclusion cannot be used unchanged while those assumptions are
the faults being tested. After the fit-independent code passes, use
Sstar=2^-47 and Estar=2^-57 as conservative bounds.

Retain the parent h_cal=1/32, gain/preparation/noise receipts2^-49, timing
2^-55, solver defect2^-44 and normalized computation error2^-60. Add a full-state
gain-preparation error receipt≤sqrt(6) times2^-49; controlling only its six
observed coefficients would not bound leakage through an off-diagonal readout.

Let l=15/16,u=17/16,

\[
 g_0=\sqrt{u/l},\quad g_S=\sqrt{(u+Sstar)/(l-Sstar)},\quad
 e_S=\frac{4uSstar}{l(l-Sstar)}.
\]

The metric model discrepancy in normalized finite calibration features is
at most B_S=2g0 gS eS/l. Gain-run readout contamination contributes an extra
gain error≤Estar sqrt(6)(1+2^-49). The dynamic and gain-normalization readout
terms give

\[
 B_E=\frac{Estar\,g_S(2+\mu)+2g_S Estar\sqrt6(1+\mu)}{h_{cal}l},
 \quad\mu=2^{-49}.
\]

Re-evaluate the parent metrology bound B0 with generator envelope5 rather
than17/4. The same projected inverse remains a contraction for the diagonal
background forward map. Its final error is bounded by

\[
 \frac54[B_0+B_S+B_E+2^{-44}]
 <7.401\times10^{-13}<2^{-40}.
\]

The proof now allows the bounded S and readout leakage; it does not depend
on first declaring them zero. The exact definitions and interval enclosures
are in RESTRICTED_FAULT_CERTIFICATE.json.

## 7. Transfer to the history operator limits

From the six fitted ratios, construct qhat_frame0=1,
qhat_framek^2=product_(j<=k)(Dhat_j/Uhat_j), shat_k=sqrt(Dhat_k Uhat_k),
and chat=(shat1 shat2 shat3)^(1/3). Require the measured rate-shape gate
|shat_k/chat−1|≤2^-38. The existing parent shape theorem, conservatively
using ratio uncertainty2^-39, bounds diagonal metric error by1.165e-11 and
native-rate shape error by1.724e-11.

The new off-diagonal S and readout must also be transformed, not compared in
different frames. Safe amplification factors are

\[
 F_S=(u/l)^3/l,\qquad F_C=(u/l)^3.
\]

Thus after the inferred coframe, overall metric normalization and chat time
normalization,

\[
 \|H_{final}-I\|<1.166\times10^{-11}<2^{-35},\qquad
 \max|\Delta w_k|<1.724\times10^{-11}<2^{-35},
\]
\[
 \|C_{final}-R\|<2^{-56}<2^{-25},\qquad J=0\text{ within the chosen family}.
\]

Overall metric scale cancels from the effective generator; this does not
identify a physical metric scale. With fixed clock/rates through the batch,
the log-error bound from the stronger2^-40 ratio result also gives
|c_true/chat−1|<2^-39, well inside the parent's allowed constant common-scale
interval1±1/1024. This uses logger-time calibration and does not derive physical
seconds.

These limits satisfy the parent history hypotheses. Conditional on its separate
37-preparation realization, transformed readout, acquisition noise and timing
receipts, its retained1893-signal bounds remain:

| Hankel axis samples | Retained-signal condition upper bound |
|---:|---:|
|2048|19410|
|4096|3385|
|8192|1930|

Sample at logger step1/(2chat), with the inferred coframe input/output corrections.
Retain the globally validated readout correction for history. The six residual
gain estimates above normalize calibration features only; replacing the history
correction requires renewed readout validation.
The remaining history receipts are preparation error2^-25, additive noise2^-26,
origin error2^-29 and jitter2^-29 in the final normalized coordinates. Passing
diagnosis does not itself establish those separate receipts. The count is a
retained numerical signal guarantee; weak modes can be lifted by perturbations,
so no claim that the actual kernel remains exactly747 is made.

## 8. Verification and limits

Exact checks cover all16175 coefficient assignments, all listed observed
metric endpoints, minimum exclusive-neighbor count3, native channel identities,
unit-norm code preparations and the stencil moment identity. Full-carrier
rational Taylor calculations test no defect and both signs of a2^-44 metric
defect at pair(0,4). The nonzero cases reject with the noise budget, while
the native control lies inside the null gate. A local static readout control
is exactly decoded and rejected. Five decoder tests and an isolated replay
check the implementation. All observations are constructed controls.

Arbitrary readout operators remain unidentifiable: the static code has at
least2380 blind input directions per row; six fixed times give a general lower
bound1080 per row. A two-entry off-stencil same-color alias is retained as a
counterexample. Extra generator terms can cancel a metric signature, and
nonmatching metric faults can interfere. Rejection identifies a violated joint
contract, not a physical cause. There is no new physical law, gauge group,
continuum limit or asymptotic experiment claim.

The source packages were restored from their saved copies after the transient
checkout was lost. The new repository capture starts from current origin/main;
earlier local commit identifiers remain source records, not reconstructed Git
ancestors. Original package hashes and source manifests are retained. No old
capture or attachment is rewritten. The CRL2 amendment remains a proposal;
constructor verification is not non-constructor review. Physical promotion0;
no public push, PR or merge.

Recommended next action: determine the best achievable precision/work tradeoff
for the restricted validator, including rigorous uncertainty floors and
whether a practical measurement design can satisfy the derived contract.
