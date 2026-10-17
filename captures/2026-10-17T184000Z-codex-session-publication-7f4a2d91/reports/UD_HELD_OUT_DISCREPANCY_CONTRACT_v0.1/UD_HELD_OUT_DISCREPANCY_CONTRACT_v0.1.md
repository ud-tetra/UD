# UD held-out discrepancy contract v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; development — no registry entry.**
This contract separates a compact fault screen from a complete-basis coverage
benchmark. It gives explicit rejection thresholds for cross-talk, departures
from the fitted dynamics and observable drift. Under a repeatable linear
time-invariant plant, passing the complete-basis frame test would certify the
actual finite observer's rank 2640, kernel 0 and condition number <748. This
does not require the actual metric to be grade scalar or actual readout to be
diagonal. No experiment has been run. Physical promotion = 0; constructor
checks passed; independent review pending.

## 1. Freeze the predictor before taking held-out data

Retain the prior 197-parameter calibration and the 189-coordinate observer.
Freeze fitted gains ghat, clock scale alphahat, metric Hhat and generator
Khat=Hhat^(-1) A_what before acquiring the probes below. Do not refit these
parameters on held-out measurements. A rejection may motivate a new version
and a new held-out dataset; reusing the same data after refitting is not an
independent validation test.

Use reference-time coordinates t=alphahat u and gain-normalized outputs.
The fitted predictor is R exp(t Khat)p. Under the declared null family, the
true normalized readout C differs from R by at most gamma, and the true
effective generator in these reference-time coordinates differs from Khat
by at most epsilon. From the preceding candidate precision contract, take

\[
\eta=3/10^9,\quad r_{\rm fit}=2/10^9,\quad
\Delta_H=5/10^{10},\quad\Delta_w=4/10^{10},\quad l=15/16,
\]
\[
\epsilon_g=33/(16\cdot10^{13}),\quad
\gamma=\epsilon_g/l,\quad
\Gamma=\sqrt{(1+\eta)/(1-\eta)},\quad
K_{\max}=4(1+\eta)/(1-\eta),
\]
\[
\epsilon=\frac{4\Delta_w}{1-\eta}
 +\frac{4(1+r_{\rm fit})\Delta_H}{(1-\eta)^2}
 +K_{\max}\frac{1/10^{12}}{l}.
\]

The final term accounts for constant clock-scale uncertainty. Both null
propagators have norm <=Gamma for all real time. Their Duhamel difference
is <=Gamma^2 epsilon t for t>=0. The frozen model itself has a certified
2048-snapshot normalized minimum singular-value lower bound

\[
s_{\rm fit}=\frac{97}{100}\frac1{512\sqrt2}.
\]

These are conditional mathematical inputs. If the calibration model is false,
they need not describe the actual plant. Their role is to bound discrepancies
under the null and to certify the frozen predictor, not to assume the actual
plant belongs to the null while testing it.

## 2. Instrument contract and decision rule

The candidate validation error ceiling is

\[
e_{\rm col}=1/10^{13}.
\]

It bounds the Euclidean error in each complete 189-output, gain-normalized,
blank-corrected response vector for a specified unit preparation at a
specified reference time. It includes sensor noise, preparation contamination,
timing error, normalization arithmetic and blank correction. This is a
**total response error requirement**, not a claim that a preparation error of
the same size remains bounded under an arbitrary unstable plant. An apparatus
must independently justify this ceiling. No independent-noise assumption or
statistical averaging is used.

The zero-preparation blank is also bounded by ecol in response norm under the
zero-offset null. A blank response tests additive offsets; subtracting it
does not make an offset-free model empirically true. The total corrected
response error must include uncertainty in that subtraction.

For every statistic use a verified interval enclosure. Reject when its lower
bound is above the threshold, pass when its upper bound is at or below the
threshold, and refine or report inconclusive when the interval straddles it.
Numerical prediction error must be enclosed. The thresholds are deterministic
error budgets, not significance levels or estimated false-positive rates.

## 3. Compact targeted screen

Prepare the blank p=0 and six separate unit coordinate states

\[
p\in\{e_0,e_4,e_{120},e_{152},e_{928},e_{2040}\}.
\]

These are held out from the three mixed calibration preparations. Coordinates
0 and 120 are outside the readout; coordinate 120 is edge (0,33). The other
roles include all four chain degrees. Read all 189 outputs at reference times
0,1/32,1/16,1/2. Repeat the seven-preparation block at an early and a late
wall-clock epoch using the same preparation and relative-time schedule.
Cost: 2 times 7 times 4 times 189 = **10584 scalar outputs**.

For unit inputs let z(t,p) be corrected normalized data. Reject the frozen
prediction when

\[
\|z(t,p)-R e^{t\widehat K}p\|>
T(t):=\gamma\Gamma+\Gamma^2\epsilon t+e_{\rm col}+e_{\rm eval},
\quad e_{\rm eval}=1/10^{20}.
\]

| Reference time | Null residual threshold, display approximation |
|---:|---:|
| 0 | 3.200001 times 10^(-13) |
| 1/32 | 1.129534 times 10^(-10) |
| 1/16 | 2.255867 times 10^(-10) |
| 1/2 | 1.802454 times 10^(-9) |

The exact expressions and interval enclosures, not rounded values, define the
thresholds. A true response discrepancy above the null allowance plus twice
the instrument/evaluation error is guaranteed to reject. At time zero, for an
input outside the readout, the null response is exactly zero for every metric,
rate and diagonal gain; use the sharper ecol threshold for cross-talk leakage.
For the blank use threshold ecol and guaranteed offset detection above 2ecol.

**Observable drift:** compare the two blocks directly, with no model refit:

\[
D(t,p)=\|z_{\rm late}(t,p)-z_{\rm early}(t,p)\|.
\]

Reject stationarity if D>2ecol. A true response change >4ecol is guaranteed
to reject. Calibration uncertainty cancels because the same frozen predictor
and normalization are used in both blocks. The statistic does not identify
whether gain, generator, clock, offsets or preparation changed. It detects
response drift at the tested epochs and inputs, not every parameter drift.

## 4. Two actual-carrier synthetic fault demonstrations

These are mathematical fault injections, not empirical results.

**Cross-talk missed by the calibration.** Add
E=epsilon times output_row4 times input_column0^T to the readout, with
epsilon=1/10^9. The original gain preparation has zero coefficient at input0,
and none of its six dynamic calibration outputs was row4. Thus all 197
original calibration scalars are exactly unchanged. The new input e0 at time
zero produces leakage epsilon in observed coordinate4, far above the 2ecol
guaranteed-detection threshold.

**Excluded metric accepted by the calibration.** At unit rates and clock take

\[
H_\rho=I+\rho(e_0e_4^T+e_4e_0^T),\qquad \rho=1/10^6.
\]

This is SPD with eigenvalues 1+rho,1-rho and 1 elsewhere, and
||Hrho-I||=rho. It is not grade scalar. For K=Hrho^(-1)A,

\[
K[4,120]=-\frac{\rho}{1-\rho^2},
\]

where every grade-scalar candidate has zero direct incidence entry there.
Exact rational Taylor evaluation of the six original finite calibration
responses, followed by the prescribed projected fit, gives fitted q,h,w all
equal to 1 at the stored rational precision. The certified feature residual
is <10^(-12) (enclosed expression approximately 5.54 times 10^(-19)), so the
original estimated-parameter acceptance gates pass. The independent metric
reference at a diagonal unit coefficient also agrees with 1 in this example.

The held-out edge input e120, output4, at t=1/32 instead has a certified
prediction-residual magnitude **>3/10^8**, exceeding twice the screen threshold.
The signal lower bound is approximately 3.112296433 times 10^(-8).
This certifies detection of this alternative; it is not a universal lower
bound on the observability of every metric perturbation of that norm.

## 5. Complete-basis coverage benchmark

The compact screen cannot validate arbitrary readout columns or arbitrary
generator directions. For a complete benchmark, prepare every e_l,
l=0,...,2639, on the same repeatable linear time-invariant plant. Collect all
189 outputs at both schedules

\[
t_j=j/2,\quad t_j+\delta,\qquad j=0,\ldots,2047,
\quad\delta=1/32.
\]

Include a zero-input run for blank correction. Gain normalization is fixed
from the preceding calibration. The last reference time is 2047/2+1/32.
Each relative-time response block is an empirical 189 by 2640 unit-response
matrix. Form the normalized operators

\[
F=2048^{-1/2}\operatorname{stack}_j C e^{t_jK},\qquad
G=2048^{-1/2}\operatorname{stack}_j C e^{(t_j+\delta)K}.
\]

K here denotes the actual effective generator in the frozen reference-time
coordinates, with no grade-metric or diagonal-readout assumption. Let Fm,Gm
be their measured estimates. The response-error contract implies

\[
\|F_m-F\|,\|G_m-G\|\le
\varepsilon_V:=\sqrt{2640}\,e_{\rm col}.
\]

Proof: the normalized stacked error in each input column is <=ecol; sum
squared column bounds to obtain a Frobenius bound, hence an operator bound.
The normalized sample count does not introduce another sqrt(2048) factor.

**Cost:** 2640 times 4096 times 189 = **2043740160 sensor scalars**, or
2044514304 including one blank run. This is a complete-coverage benchmark,
not a practical sensor-minimal design. No such dataset was allocated or
generated. A streamed/sharded implementation can accumulate Gram statistics;
verified operator-norm bounds are required. Substituting a Frobenius residual
into the same null threshold without changing its uncertainty bound is invalid.

### 5.1 Arbitrary static cross-talk

At t=0, the full unit-response matrix is C. Mask out, in each output row, its
single allowed coordinate from R. Let Lm be the Frobenius norm of all remaining
measured entries. Under diagonal readout the true masked matrix is zero.
Reject if

\[
L_m>\varepsilon_V.
\]

Passing implies masked cross-talk Frobenius norm <=2epsilonV, hence operator
norm <=2epsilonV. The enclosed bound is <1.028 times 10^(-11). Cross-talk
operator norm >2/10^11 is therefore guaranteed to reject. These units refer
to gain-normalized readout. Unknown diagonal gain changes are not called
cross-talk by this statistic; they are tested by the frozen-frame comparison.

### 5.2 Direct validation of the finite observer

Let Fhat be the exact frozen-model history operator. Test

\[
\|F_m-\widehat F\|\le T_A:=1/400000.
\]

Under the null, the residual is bounded by

\[
\gamma\Gamma+\Gamma^2\epsilon T_{\rm rms}+\varepsilon_V<T_A,
\quad T_{\rm rms}^2=2047\cdot4095/24.
\]

If the test passes, irrespective of whether the actual H and C belong to the
calibration family,

\[
\sigma_{\min}(F)\ge s_*:=s_{\rm fit}-T_A-\varepsilon_V>0,
\quad\sigma_{\max}(F)\le\Gamma+T_A+\varepsilon_V.
\]

The interval calculation gives s_*>0.0013371358889 and
(Gamma+TA+epsilonV)/s_*<748. Thus the actual finite observer has **rank2640,
kernel0 and condition<748**, conditional on linearity, repeatability and the
response-error contract. A simulated or proposed pass is not an empirical pass.

### 5.3 Short-step dynamical consistency

Let Qhat=exp(delta Khat). Test the held-out shift residual

\[
\|G_m-F_m\widehat Q\|\le T_B:=1/(8\cdot10^9).
\]

Using measured Fm here cancels the long-duration prediction error. Under a
constant null plant, G=FQ with Q=exp(delta K), and

\[
\|G_m-F_m\widehat Q\|
\le(1+\gamma)\Gamma^3\epsilon\delta
    +\varepsilon_V(1+\Gamma)<T_B.
\]

The enclosed expression is approximately 1.229095211 times 10^(-10).
If both frame and shift tests pass, then

\[
\boxed{\|Q-\widehat Q\|\le
\frac{T_B+\varepsilon_V(1+\Gamma)}{s_*}}
\]

with enclosed upper-bound expression approximately 1.011686151 times 10^(-7).
This bound permits arbitrary constant actual C and K. It follows from
F(Q-Qhat)=G-F Qhat and the independently established lower singular bound.
Comparing Gm only with the frozen Ghat would retain a long-horizon parameter
uncertainty and give a much weaker result.

### 5.4 Continuous generator: an extra bandwidth assumption

To infer a continuous generator, additionally require ||K||<=5 in the fixed
coordinates. The fitted generator also satisfies this ceiling. Then
||exp(delta K)-I||<=r=exp(5/32)-1<1. The convergent logarithm series gives

\[
\|K-\widehat K\|\le
\frac{32}{2-e^{5/32}}\|Q-\widehat Q\|,
\quad \frac{32}{2-e^{5/32}}<40.
\]

Proof: for ||X||,||Y||<=r<1, expand log(I+X)-log(I+Y); each nth difference
is bounded by n r^(n-1)||X-Y||, canceling the factor1/n and summing to
1/(1-r). The same convergent series satisfies log(exp(delta K))=delta K
on this norm ball, for example by differentiating along sK where the series
converges and all terms commute. The combined interval ceiling is

\[
\boxed{\|K-\widehat K\|<1/250000.}
\]

Thus a constant bounded generator discrepancy above this ceiling cannot pass
both tests under the instrument contract. This is an operator validation
bound, not a direct metric-norm bound. It is looser than the original
generator calibration budget. The direct frame test certifies finite
observability without needing to turn this generator bound into a long-time
perturbation estimate.

## 6. Exact blind spots and scope limits

**Metric shadow:** u0 is uniform on the 120 vertex coordinates and zero
elsewhere. Au0=0 exactly. H=I+eta u0u0^T/120 is SPD for eta>-1 and satisfies
H^(-1)A=A. Every dynamical probe, including a complete basis sweep, gives the
same histories. A metric norm/energy measurement is needed to distinguish
this family; it must not be dismissed as gauge without an independent rule.

**Few-input blind directions:** under the nominal skew generator there are
105 distinct temporal frequencies. Each prepared vector spans at most105
dimensions under all powers of A. The original three preparations therefore
span at most315 dimensions over all time. At least2325 input directions per
readout row can support an added E annihilating all those trajectories. This
is a lower bound on blindness, not a computed exact dimension. A handful of
successful probe histories cannot validate arbitrary cross-talk.

**Sampling alias:** on the active space define the real complex structure
J=A(-A^2)^(-1/2), and J=0 on ker A. It commutes with A and J^2=-I on the
active space. The real skew generator Kprime=A+64 pi J has exactly the same
propagators as A at every multiple of1/32, since its extra exponential is
exp(2 pi n J)=I. All specified rational-grid probes miss this high-frequency
alternative. The generator norm ceiling above is essential; a finite-grid
pass alone cannot establish it.

**Drift between epochs:** finite tests cannot exclude unsampled bursts. For an
externally justified response Lipschitz constant L in wall-clock time and
maximum sampling gap Delta, passing sampled paired-drift tests implies a
continuous response bound <=4ecol+L Delta/2 inside the bracketed interval.
Without L, only sampled-epoch claims follow. Common time-dependent metric/rate
rescaling can also leave K unchanged, so independent scale references must
be monitored if parameter stability itself is claimed.

**Linearity and repeatability:** basis response matrices identify an LTI
operator only when the same linear plant is used across runs. Finite probes
cannot establish unrestricted linearity, exclude arbitrary nonlinearities
vanishing on the tested trajectories, or certify a time-varying plant by
silently assembling different runs into one matrix. Amplitude/superposition
checks and stability receipts are additional requirements with their own
detectable alternative classes.

## 7. Reproduction and remaining gate

Run `python certify_discrepancy.py` with the pinned requirements. It certifies
the null thresholds, conditional frame rank/conditioning, generator bound,
actual-carrier cross-talk blindness and harmonic witness, and exact rational
finite responses for the excluded-metric fault followed by calibration refit
and held-out rejection. Taylor remainders are enclosed; no decimal fit is
treated as proof. The complete-basis acquisition is a compact schedule, not a
generated or executed dataset. Constructor verification is not independent
adversarial review.

Ledger entries O03, Q139, Q165 and Q169 remain scoped; no coefficient ledger
entry is modified. The attached CRL-2 amendment labels itself a proposal.
This work stays in the development distinction and makes no registry claim.
Attachments are not redistributed; the unavailable Genesis image was unused.
Source hashes, clean replay, parent captures and publication status accompany
the contract. Public publication is separate from local capture.

**Next gate:** reduce the complete-basis cost for an explicitly restricted
discrepancy family, while retaining certified coverage and detection limits;
then map preparations, error receipts and scale references to a concrete
apparatus and obtain independent review. A smaller probe set is defensible
only after its remaining blind directions are quantified.
