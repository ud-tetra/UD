# UD observer robustness v0.1

**RESULT / STATUS — DERIVED, CONDITIONAL, CONSTRUCTOR VERIFIED.** The retained
189-coordinate observer remains injective under the joint operator tolerances
below, for each of the three previously certified finite sampling protocols.
This adds a model-mismatch theorem to the known-model observer. It does not
measure an apparatus or establish a native metric-dependent physical law.
Physical promotion = 0. Independent review pending. Local append-only capture;
public publication pending. Parent local commit:
`0c0158fef1cb6b75ad4c7d057c0b72abdbcce3c0`.

## 1. Frozen carrier and nominal inputs

The carrier is the real simplicial chain space of the regular 600-cell boundary
S3, with grade dimensions (120,720,1200,600), total 2640. Ordered oriented
simplices carry the identity metric. The real generator A has upper adjacent
blocks -Bk and lower blocks Bk^T. Thus A^T = -A. Write A = A1+A2+A3 for the
three adjacent-grade channels. B1 B2 = B2 B3 = 0 implies
Ai Aj = 0 for i != j. The parent exact annihilator and spectral certificate give
||A|| < 4. All norms in this note are Euclidean operator/vector norms unless
an H subscript is present.

R selects 189 distinct chain coordinates: three vertex links centred at vertices
0,45,66, retained tetrahedral coordinate 2040, and coordinates 928 (face),
152 (edge), and 4 (vertex). There are 36 vertex, 91 edge, 61 face and one
tetrahedral channels. Consequently ||R|| = 1. A snapshot still has nullity 2451;
the full finite history is injective. This note does not change the observer
or its historical selection.

At times tj = j/2, j = 0,...,M-1, define

\[
F_M=M^{-1/2}\operatorname{stack}_j R e^{t_j A}.
\]

The frozen parent certificate supplies sigma_min(F_M) >= sM and
sigma_max(F_M) <= 1:

| M | Last nominal time | Exact sM | Parent condition bound |
|---:|---:|---:|---:|
| 2048 | 2047/2 | 1/(512 sqrt(2)) | <725 |
| 4096 | 4095/2 | 1/(256 sqrt(2)) | <363 |
| 8192 | 8191/2 | sqrt(3)/512 | <296 |

These are lower bounds, not measured singular values. The 105 distinct temporal
frequencies and common spatial certificate are inherited; this addendum checks
their hashes and spectral band input without recomputing the parent proof.

## 2. General perturbation theorem

**DERIVED.** In common fixed state coordinates let the actual constant generator
be K, the actual sample times tj+dj with |dj| <= tau, and the actual readouts
Cj = R+Ej with ||Ej|| <= rho. No statistical independence is assumed. Let
||K-A|| <= epsilon. The normalized actual map is

\[
\widetilde F_M=M^{-1/2}\operatorname{stack}_j
 (R+E_j)e^{(t_j+d_j)K}.
\]

First suppose one fixed SPD H satisfies ||H-I|| <= eta < 1 and
K^T H + H K = 0. Put

\[
g=\sqrt{\frac{1+\eta}{1-\eta}},\quad
\overline t=\frac{M-1}{4},\quad
T_{\rm rms}^2=\frac{(M-1)(2M-1)}{24},\quad
b=\rho+(4+\epsilon)\tau.
\]

Then a sufficient mismatch bound is

\[
\boxed{\|\widetilde F_M-F_M\|\le
\beta_H:=g\sqrt{b^2+2b\epsilon\overline t+
\epsilon^2 T_{\rm rms}^2}
\le g(b+\epsilon T_{\rm rms}).}
\]

Proof: H^(1/2) K H^(-1/2) is skew, so ||exp(tK)|| <= g for
every real t. Duhamel gives ||exp(tK)-exp(tA)|| <= g epsilon t for t>=0.
The integral of the time derivative gives
||exp((t+d)K)-exp(tK)|| <= g(4+epsilon)|d|, even when the first
jittered time is negative. The readout-error term is <= rho g. The jth block
error is therefore <= g[b+epsilon tj]. Squaring, averaging and using the
triangle bound for a stacked operator yields the displayed RMS expression.
These bounds do not assume that H commutes with A or K.

If an H-skew structure is unavailable, the same epsilon still yields the
unstructured bound, with T=(M-1)/2:

\[
\boxed{\beta_U=e^{\epsilon(T+\tau)}
 [\rho+\epsilon T_{\rm rms}+(4+\epsilon)\tau].}
\]

Indeed A is skew and K=A+Delta has two-sided propagator bound
||exp(tK)|| <= exp(epsilon |t|). Duhamel and the jitter integral then bound
each block by exp(epsilon(T+tau))[rho+epsilon tj+(4+epsilon)tau].
The exponential factor cannot in general be dropped: Delta=epsilon I gives
exp(tK)=exp(epsilon t)exp(tA).

For either valid bound beta < sM, singular-value perturbation gives

\[
\sigma_{\min}(\widetilde F_M)\ge s_M-\beta>0,\qquad
\sigma_{\max}(\widetilde F_M)\le1+\beta,\qquad
\kappa_2(\widetilde F_M)\le\frac{1+\beta}{s_M-\beta}.
\]

Thus every plant within the stated bounds has rank 2640 and kernel zero.
This is a uniform rank certificate. It does not identify an unknown K or Cj.

## 3. Rates and metric: three distinct meanings

**DERIVED — rate perturbation.** Let
A_w=a A1+b A2+c A3, with each of |a-1|,|b-1|,|c-1| <= r.
The mutually orthogonal active subspaces ran(Ai) follow from Ai Aj=0
and skew symmetry. On ran(Ai), A acts as Ai; on the common kernel it vanishes.
Hence ||A_w-A|| <= r||A|| <= 4r. The exact sparse identities were checked
on all 2640 coordinates; this bound does not pay an unnecessary factor of three.
In the H=I rate-only branch K=A_w, one can take epsilon=4r.

**DERIVED — metric as reporting norm.** If the state evolution and readout are
unchanged, merely reporting ||x||H does not alter rank or create a generator
error. The norm relations are

\[
\sqrt{1-\eta}\|x\|\le\|x\|_H\le\sqrt{1+\eta}\|x\|.
\]

For Euclidean observation norm and H state norm, the lower singular bound
is divided by sqrt(1+eta), the upper by sqrt(1-eta), and the condition
bound is multiplied by at most g.

**CANDIDATE constitutive rule — metric affects evolution.** For the declared
rule K=H^(-1) A_w, H-skewness follows exactly from HK=A_w. Moreover

\[
\|K-A\|\le
\|H^{-1}\|\|A_w-A\|+\|H^{-1}-I\|\|A\|
\le\boxed{\frac{4(r+\eta)}{1-\eta}}.
\]

This rule is a branch chosen for the calculation. No result here proves that
UD or any apparatus selects it. For a different metric-to-generator rule,
one must supply its own epsilon; a metric discrepancy alone is insufficient.

## 4. Certified joint envelope

The following exact rational ceilings may hold **simultaneously**, using the
candidate constitutive branch. Rates and metric are fixed over acquisition;
readout and jitter may vary by sample.

| Quantity | Joint ceiling | Meaning |
|---|---:|---|
| r | 3/10^9 | Each of three rates relative to nominal 1 |
| eta | 3/10^9 | ||H-I|| in the fixed state coordinates |
| rho | 1/100000 | ||Ej||, absolute operator error relative to ||R||=1 |
| tau | 3/10^6 | Absolute jitter in internal model time |

Use epsilon=4(r+eta)/(1-eta)=24/999999997. With Arb at 256 bits,
the constructor verifies beta_H < (3/100)sM for all three protocols.
The unstructured bound beta_U also passes the same 3% margin for the same
direct epsilon, rho and tau ceilings, without invoking H-skewness.

| M | beta_H/sM, display approximation | Actual condition bound | Actual kernel |
|---:|---:|---:|---:|
| 2048 | 0.0253487801 | <748 | 0 |
| 4096 | 0.0176253407 | <375 | 0 |
| 8192 | 0.0226422504 | <306 | 0 |

The displayed ratios are approximations, not inequality thresholds. The JSON
contains interval enclosures; the exact common threshold is 3/100.
In particular sigma_min(actual)^2 >= (97/100)^2 sM^2.
This is a sufficient envelope; it is not a necessary limit or an optimized
hardware specification. The very small rate/metric budget reflects a
conservative long-horizon phase-error bound. More samples improve the nominal
noise bound but increase accumulated generator mismatch; the 4096 profile
has the smallest certified mismatch ratio for this selected envelope.

For comparison, isolated 5% budgets with H=I and all other errors zero are:

\[
\epsilon\le\frac{s_M}{20T_{\rm rms}},\quad
r\le\frac{s_M}{80T_{\rm rms}},\quad
\rho\le\frac{s_M}{20},\quad
\tau\le\frac{s_M}{80}.
\]

These isolated maxima cannot be combined as a joint budget. Their interval
values are retained in ROBUSTNESS_CERTIFICATE.json.

## 5. Reconstruction error and the meaning of 8%

**DERIVED.** Let measured normalized data be y=Ftilde x+e, with
delta=||e||=(M^(-1) sum_j ||e_j||^2)^(1/2), i.e. vector RMS noise across
snapshots. The nominal least-squares decoder has error

\[
\boxed{\|F_M^\dagger y-x\|\le
 \frac{\beta\|x\|+\delta}{s_M}.}
\]

The systematic mismatch term is present even at zero measurement noise. A
decoder calibrated to the actual map instead has noise error
delta/(sM-beta). Full observability alone does not justify replacing the
nominal decoder with an unknown actual decoder.

For a declared state bound ||x|| <= X, the joint 3% envelope and
delta <= sM X/20 imply an **absolute** error ceiling

\[
\|\widehat x-x\|\le\frac{2}{25}X.
\]

This is 8% of the supplied state bound X. It is not a uniform 8% relative
error guarantee for arbitrarily small states. If the stronger signal-specific
noise hypothesis delta <= sM||x||/20 holds, then the relative bound follows.
A per-scalar deterministic noise ceiling nu only implies delta <= sqrt(189)nu;
no averaging improvement from independent noise is assumed here.

## 6. Exact calibration obstructions

**NO-GO for joint gain/state identification.** For any c>0, the models
(C=R,x0,K=A) and (C'=cR,x0'=x0/c,K'=A) give exactly the same history
at every time. For c arbitrarily close to 1, both satisfy arbitrarily small
nonzero readout neighborhoods. Therefore rank 2640 for each known readout
does not establish joint unknown-gain and state-amplitude identification.
An amplitude reference or other gain constraint is needed.

**NO-GO for separating common metric/rate scale in the candidate branch.**
The change (H,w) -> (cH,cw) leaves K=H^(-1)A_w exactly unchanged.
Dynamics alone cannot separate the two scales without a further anchor.

**NO-GO for separating common clock/rate scale from unconstrained data.**
The change (K,t) -> (cK,t/c) leaves exp(tK) unchanged. An external time
reference or fixed rate scale is required to attach physical time units.

These are changed unknown-parameter inverse problems, not new kernels of the
known-parameter linear observer. None authorizes calling missing modes gauge
redundancy, reconstructs topology from a scalar coincidence, or promotes physics.

## 7. Reproduction, provenance and remaining work

Install the pinned requirements and run `python certify_robustness.py` from any
directory. It checks exact skew symmetry, distinct coordinates, six vanishing
cross-channel products, the parent band enclosures, three joint interval
budgets, unstructured budgets and condition bounds. JSON decimal display fields
are explanatory; exact fractions and Arb comparisons carry the inequalities.
The script checks the actual full carrier identities without building a dense
million-row finite history. The analytic theorem handles arbitrary admissible
perturbations, so a random simulation is not the certificate.

Sources are frozen copies and hashes of the preceding observer outputs, with
its source register and annihilator retained. Source register names upstream
PR heads and issues #136 and #144; this addendum does not update or close them.
The report and proof are new; no supplied private attachment is copied.

**OPEN:** choose a source-supported constitutive rule, independently validate
the mathematical certificates, supply gain/time/metric anchors, and compare
measured operator errors and noise with the budget. An apparatus specification
and measurements are absent. The present result makes an experimental contract
possible, but does not qualify an experiment.
