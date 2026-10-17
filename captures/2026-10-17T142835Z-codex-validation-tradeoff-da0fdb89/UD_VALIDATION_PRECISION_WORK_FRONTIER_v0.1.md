# UD validation precision–work frontier v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; constructor checks PASS.**
Two improved protocols are available with the same restricted physical model
and deterministic error convention as the parent certificate:

| Protocol | Scalar readings | Total response error ceiling | Guarantee retained |
|---|---:|---:|---|
| Parent |591948|2^-64|Parent readout, metric, calibration and history bounds|
| Strict-target variant |394632|2^-64|Same parent bounds|
| Recommended history-target corner |493290|2^-58|Same1893-signal history guarantee; previous extra safety margins relaxed|

The recommended corner permits **64 times more total response error** and
reduces readings by1/6. The strict-target variant reduces readings by1/3
without changing precision. Neither is a measured instrument capability.
Physical promotion0; development lane; no registry entry. Independent review
pending.

## 1. Fixed scope and what may change

Keep the source2640-dimensional600-cell operator,189-channel diagnostic readout,
260 parity-separated preparation code, two epochs and one blank per epoch.
Keep the parent's fault family: positive constant native rates; grade-scalar
background metric plus same-grade matching defects on the2574 listed pairs;
readout errors restricted to listed local stencils; no additional generator J.
The original62-channel history readout is a subset of the189 outputs.

Every coded preparation has norm at most1. At each time, its blank-corrected
189-output error vector has norm at most epsilon. Errors may be correlated
across outputs, inputs, times and epochs. No averaging gain or probabilistic
independence is assumed.

The exact source geometry and code remain fixed. We improve the statistic,
error analysis, central derivative order and time step. The recommended
variant allows larger intermediate readout and metric bounds, while checking
the final history budgets explicitly. The strict variant preserves the old
intermediate bounds as well. Neither test proves membership of an unrestricted
unknown plant in the assumed family.

## 2. Tighter spatial statistic

For each listed oriented pair(r,t) whose first endpoint is observed, define
J_rt=N_t minus N_r from the native incidence row supports. There are3171 such
filters; every J_rt has at least three entries. Local color injectivity lets
each generator coefficient in that set be decoded separately.

Use the signed score

\[
 z_{rt}=\frac1{|J_{rt}|}\sum_{j\in J_{rt}}A_{tj}\widehat K_{rj}.
\]

For the actual matching partner, the parent inverse-metric identity gives
K_rj=−s w_channel A_tj/(h_grade^2−s^2). Therefore all signed terms have the
same sign, and

\[
 |z_{rt}^{true}|\ge c|s|,\qquad
 c=(15/16)/(17/16)^2=240/289.
\]

This is an algebraic matching/positivity result. It is not statistical noise
cancellation. Define the decoder amplification
qbar_rt=mean_(j inJ_rt) q_color(j). Its exact maximum is14/3. Applying a bound
to the selected score avoids paying the parent's whole-forbidden-row
Frobenius factor sqrt(991) at every pair.

The global static error remains bounded by sqrt(2073) epsilon. In addition to
the global decoded residual gate46 epsilon, impose a row-local static gate

\[
 T_r=[\lceil\sqrt{M_r}\rceil+1/16]\epsilon,
 \qquad M_r=\sum_{j\in JC_r}q_{color(j)}^2.
\]

It strictly exceeds the row decoding error sqrt(M_r) epsilon, including when
M_r is a perfect square. Passage gives ||E_r|| below L_r epsilon, where
L_r=2 ceil(sqrt(M_r))+1/16. The global readout operator satisfies
||E||<92 epsilon. The unused-static-cell gate17 epsilon is retained. No new
readings are needed for these additional row gates.

## 3. Stable temporal error bound

The parent's coarse family already supplies
H eigenvalues in[7/8,9/8], HK=A_w skew, and ||K||<5. Thus

\[
 \|e^{tK}\|\le\sqrt{9/7}<G=8/7
\]

at every signed time. This is an existing consequence of the declared model,
not an additional regularity assumption.

For m positive time points, use centered derivative weights

\[
 a_k=\frac{2(-1)^{k+1}}k\frac{(m!)^2}{(m-k)!(m+k)!},\quad1\le k\le m,
 \qquad a_0=-\sum_{k=1}^m a_k.
\]

Only times0,h,...,mh are measured. Opposite-parity native outputs are odd in
time, so they supply the negative-time part mathematically. Readout leakage
need not have that parity; it is bounded separately and the a0 term removes
its constant contribution.

Hermite interpolation at0,±h,...,±mh gives the scalar derivative remainder
bound (m!)^2 h^(2m) sup|f^(2m+1)|/(2m+1)!. To see the coefficient directly,
subtract the interpolating polynomial and a multiple of
W(t)=t product_(k=1..m)(t^2−k^2h^2), choosing the multiple to cancel the
derivative error at0. Generalized Rolle's theorem gives the derivative
remainder, since W'(0)=(-1)^m(m!)^2 h^(2m).

Apply this to each sine frequency of the H-skew generator and transfer back
through H^(1/2). For unit-norm preparations, the native finite derivative error
is bounded by

\[
 B_m(h)=C_mh^{2m},\qquad
 C_m=G\frac{(m!)^2}{(2m+1)!}5^{2m+1}.
\]

The stable propagator also gives

\[
 F_m=5G\sum|a_k|k,
 \qquad N_m=|\sum a_k|+\sum|a_k|.
\]

The readout term uses ||e^(khK)−I||≤5Gkh rather than an exponentially growing
envelope. A decoded pair score has error at most

\[
 qbar_{rt}[C_mh^{2m}+(L_rF_m+N_m/h)\epsilon].
\]

Use that exact rational expression as its strict acceptance gate. If all gates
pass, the full matching metric defect satisfies

\[
 S_{pass}(m,h,\epsilon)=
 \max_{rt}\frac{2qbar_{rt}}c
 [C_mh^{2m}+(L_rF_m+N_m/h)\epsilon].
\]

Matching makes ||S|| the maximum active-pair amplitude. The factor2 includes
both an accepted residual and its possible error. All3171 geometric filters
and all107 distinct(qbar,L) bound pairs are checked exactly.

## 4. Optimization domain and precision ceiling

The searched temporal family is the standard maximally accurate, equispaced
centered interpolation derivative, exact through degree2m, for every m≥1.
Nonuniform nodes, nonmaximal-order weights, unequal static/dynamic precision,
pair-specific steps, alternative spatial codes and correction schemes are
outside this optimization. The same epsilon and step apply across each profile.

Keep the parent's re-derived calibration function Q(S,E): the explicit
six-ratio error bound after bounded metric/readout model discrepancy, including
unchanged metrology, solver and full gain-preparation receipts. It is strictly
increasing in both nonnegative arguments. Require

\[
 Q(S_{pass},92\epsilon)<2^{-39}.
\]

This retains the original requested ratio accuracy. Together with the measured
relative-rate shape gate2^-38, the final metric, rate, readout and constant
common-scale requirements of the history theorem are checked again.

For fixed m and epsilon, every pair bound is an increasing affine function
of the same quantity C_mh^(2m)+N_m epsilon/h. Consequently the exact continuous
minimizer is shared by every pair and their maximum:

\[
 \boxed{h_*=(N_m\epsilon/(2mC_m))^{1/(2m+1)}.}
\]

At h*, that quantity equals(2m+1) C_m h_*^(2m). Monotonicity then reduces the
precision ceiling to a single increasing scalar equation in epsilon. Each
root is bracketed by80 bisections in512-bit interval arithmetic. Endpoint
classifications use interval comparisons, never floating-point decisions.

Orders m=1,...,12 are solved explicitly. Their continuous Pareto frontier is:

| Positive time points m | Readings | Supremum total error, approximate | Minimum binary precision exponent |
|---:|---:|---:|---:|
|1|197316|2.41686e-23|76|
|2|295974|1.25942e-19|63|
|3|394632|1.71875e-18|60|
|4|493290|3.86058e-18|58|
|5|591948|4.59291e-18|58|
|6|690606|4.66226e-18|58|

The root is a strict admissibility boundary, not a recommended error allowance.
The package also supplies a certified rational step/error pair just inside
the best continuous ceiling. Orders7–12 have smaller ceilings and more readings
than m6. For m≥13, the static readout-contamination floor already exceeds the
ratio gate at an error level certified for m6. F_m increases strictly with m:
each existing factorial weight magnitude increases and an additional positive
term appears. This proves higher orders cannot improve the ceiling within
this bound family, without an arbitrary order cutoff.

There is also a global **binary precision floor58** for this certificate
family. At epsilon=2^-57, the monotone readout floor rules out every m≥4;
the exact continuous-step optima rule out m=1,2,3. A feasible m4 protocol
exists at2^-58. This is a limitation of the specified deterministic error
envelope and code/stencil family. It is not an information-theoretic or physical
noise floor, and does not rule out other codes, corrections or noise models.

## 5. Recommended exact dyadic corner

Choose m4, h=1/256, epsilon=2^-58. This is the least reading count at the
minimum binary precision exponent. Its continuous optimal step is about
0.00420419; the simpler dyadic step has a fully certified margin and avoids
an unnecessary algebraic time specification.

The derivative estimator is

\[
 D_hY=\frac{672Y(h)-168Y(2h)+32Y(3h)-3Y(4h)-533Y(0)}{420h}.
\]

Two epochs,260 coded preparations plus a blank per epoch, five time nodes and
189 outputs give493290 readings. The latest diagnostic time is1/64. One
separate six-ratio calibration adds12 readings. The relevant passage bounds are:

| Quantity | Certified bound, decimal rounded outward |
|---|---:|
| Global readout error |92/2^58, approximately3.192e-16|
| Matching metric defect |6.698e-14|
| Six-ratio error |1.713e-12 <2^-39|
| Final-frame metric error including S |1.175e-11 <2^-35|
| Native-rate shape error |1.724e-11 <2^-35|
| Final-frame readout error |4.647e-16 <2^-25|
| Constant common-scale error |1.941e-12 <1/1024|

The earlier intermediate promises E≤2^-57,S≤2^-47 and ratio error≤2^-40
are not retained by this corner. They were stronger than the history theorem
requires. This is an explicit target relaxation, not a silent claim that all
old numerical bounds improved.

Conditional on the measured shape gate and the parent's separate history
preparation, noise, timing and stability receipts, the retained1893-signal
condition bounds remain19410,3385,1930 for axis sizes2048,4096,8192. Acquisition
uses the same inferred coframe and chat-normalized sampling rule. Keep the
validated global gain correction; changing it requires renewed readout validation.
No actual kernel-dimension invariance is asserted.

A sufficient component contract for each code/sample is preparation error
2^-62, logger-time error2^-65, corrected additive output error2^-60 and
computation error2^-60. With ||C||≤2, ||U||≤G and ||K||≤5 these contributions
sum below2^-58. Their realization remains external. The two epochs do not
establish arbitrary future parameter stability.

## 6. Strict-target alternative

If the previous intermediate bounds are required, choose m3, h=1/2048 and
epsilon=2^-64. Four nodes and the unchanged code/readout give394632 readings,
one-third fewer than the parent protocol. The certified metric defect is below
4.292e-15 and ratio error below6.984e-13, retaining the old S2^-47 and ratio2^-40
bounds. The same global readout2^-57 bound also holds.

At this fixed binary precision, the continuous optimum rules out m1 and m2
for the strict metric target, while m3 has a certified rational realization.
Thus this is the smallest reading-count strict-target member of this stencil
family at the inherited precision. Much tighter precision can reduce count
further, as the full frontier illustrates.

## 7. Verification and interpretation

`optimized_gate.py` implements both profiles with exact rational squared
static gates and signed pair scores. Float inputs and wrong dimensions are
rejected. The six tests include a case where the global static gate passes but
the new row-local gate correctly fails, demonstrating why the row receipt
cannot be omitted from the dynamic bound.

Full-carrier rational Taylor controls at pair(0,4) check no metric defect and
both signs of a2^-42 defect. Transposed integer powers generate all necessary
coded-input responses for the matched filter. The finite propagator remainder
is enclosed independently; both nonzero alternatives reject with the proposed
noise budget. These are constructed controls, not independently collected
validation data. An isolated replay reproduces geometry, roots, bounds and
control outputs.

The procedure optimizes the actual declared deterministic envelope. It does
not prove a globally best experiment or establish practical metrology. No
stochastic averaging, unrestricted fault coverage, future-drift guarantee,
physical clock or spacetime identification is added. O03 values remain protocol
controls; Q139's physical time gap remains open. The CRL2 attachment remains
a proposal. Constructor verification is separate from independent review.
Physical promotion stays0; no public push, PR or merge is performed.

Recommended next step: derive a noise-versus-retained-dimension curve to guide
experimental scope when the full1893-signal contract is too demanding.
