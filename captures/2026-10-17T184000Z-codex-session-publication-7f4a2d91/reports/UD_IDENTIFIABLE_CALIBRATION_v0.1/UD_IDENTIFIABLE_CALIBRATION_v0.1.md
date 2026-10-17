# UD identifiable calibration protocol v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; development — no registry entry.**
One known two-coordinate preparation, two sample instants and an independent
clock-scale observation identify a common gain and three rates in the declared
unit-metric model. The finite calibration map has parameter rank 5. Its
normalized three-rate Jacobian has condition number <47/33 throughout the
specified parameter box. Physical promotion = 0. Constructor checks passed;
independent review pending. No apparatus data were supplied.

This extends the prior robustness result. It does not infer an arbitrary
metric, calibrate arbitrary cross-talk, select a native preparation mechanism,
or identify UD internal time with seconds.

## 1. Source-bound model and references

Retain the 2640-coordinate real chain carrier and the 189-coordinate readout R
from the preceding 600-cell observer. Let A1,A2,A3 denote its adjacent-grade
skew channels. The exact identities Ai Aj=0 for i!=j imply mutually orthogonal
active subspaces and ||A_w|| <= 4 max_i |wi| for A_w=sum_i wi Ai.

For this protocol **H=I is known**. The candidate calibration model is

\[
y(u)=g R e^{\alpha u A_w}p,
\quad w=(a,b,c),\quad g>0,\quad\alpha>0.
\]

u is logger time; reference time is t=alpha u after resetting the preparation
event to zero. Rates are defined per chosen reference-time unit. An external
clock compares an interval of logger time with that chosen reference unit;
it supplies a measurement of alpha. This is a laboratory convention and
calibration assumption, not a derivation of a UD physical clock. An unknown
time offset, nonlinear clock drift and sample jitter require separate checks.

Two external anchors are indispensable here:

1. A known prepared chain vector, including its amplitude, coordinate address
   and relative signs. Its realization in an apparatus is OPEN.
2. A clock-scale reference independent of the generator rates. At least two
   clock events are needed to measure an interval.

The shape of R, common-gain form gR and unit metric must be selected or
independently established. These are model assumptions, not outputs of four
sensor values. Nominal sensor gain does not set the physical units of support.

## 2. Concrete preparation inside the existing readout

The sorted oriented simplices and global coordinate numbers are:

| Role | Simplex | Coordinate |
|---|---|---:|
| v | (33) | 33 |
| e | (33,34) | 486 |
| f | (33,34,41) | 1680 |
| tau | (0,33,34,41) | 2040 |

All four belong to the retained 189-coordinate observer. Prepare

\[
p=e_{486}+e_{1680},\qquad \|p\|=\sqrt2.
\]

Here e_j denotes a chain coordinate vector, not a geometric coframe. Let P
select coordinates (33,486,2040), and S=diag(1,-1,1). Exact integer checks on
the full carrier give

\[
SP[A_1p\ A_2p\ A_3p]=I_3,\qquad Pp=(0,1,0)^T.
\]

Thus the initial scalar readout at coordinate 486 gives g, and the signed
initial slopes give g alpha (a,b,c). The orientation signs used here are
A[33,486]=1, A[486,1680]=-1 and A[2040,1680]=1.

**Scoped minimality.** A single coordinate preparation lies in one chain
degree and excites at most two adjacent channels. Since different channels
annihilate each other, no later sample can recover a rate whose channel was
not excited. At least two nonzero coordinate components are therefore needed
to identify all three rates in one preparation of this form. The selected
two-component vector achieves this. This is not a sensor-minimality theorem
for every possible intervention architecture.

## 3. Exact jet rank and the necessary clock anchor

For theta=(g,alpha,a,b,c), the unanchored ideal jet is

\[
J_0(\theta)=(g,g\alpha a,g\alpha b,g\alpha c).
\]

Its Jacobian has rank 4 and null direction
(0,alpha,-a,-b,-c). The exact nonlinear ambiguity is
(alpha,w)->(q alpha,w/q), q>0. Arbitrarily many preparations or time samples
cannot separate alpha from w without a scale reference, because the entire
generator in logger time is alpha A_w.

With an independent alpha observation, arrange the outputs as
(g,alpha,g alpha a,g alpha b,g alpha c). The Jacobian determinant is
g^3 alpha^3, so its rank is 5. This is a structural check; the protocol below
does not assume that an exact derivative can be measured.

If the prepared amplitude were also unknown, the further change
(g,p)->(qg,p/q) would leave every sensor history unchanged. A preparation
address without an amplitude reference does not remove the gain ambiguity.

## 4. Finite two-instant protocol and uniform inverse theorem

Choose the rational logger interval h=1/256. Record only:

| Instant/source | Scalar value(s) |
|---|---|
| u=0 | y486(0) |
| u=h | y33(h), y486(h), y2040(h) |
| Independent interval reference | alpha |

There are four sensor scalars and one clock-scale scalar. No derivative
oracle is used. In the noiseless model g=y486(0). For known g and alpha define

\[
\Phi_\alpha(w)=\frac{SP(e^{h\alpha A_w}-I)p}{h\alpha}.
\]

The observed finite feature is S[Py(h)/g-Pp]/(h alpha), where Py(h) here
means the three named sensor channels. Its model value is Phi_alpha(w).
One must fit this finite exponential map; simply setting w equal to the
feature would retain a finite-step bias.

Let g,alpha,a,b,c lie in [15/16,17/16]. For each rate derivative the integral
formula for the exponential gives

\[
\left\|\frac{\partial\Phi_\alpha}{\partial w_i}
       -e_i\right\|
\le 4\sqrt2\,h\,\|\alpha A_w\|.
\]

For completeness, subtract h alpha Ai from the derivative of
exp(h alpha A_w), express the derivative as its integral, and bound the
two propagator differences by time times ||alpha A_w||. Both propagators
are orthogonal. Divide by h alpha, use ||Ai||<4 and ||p||=sqrt2.
Taking a Frobenius bound over three columns yields

\[
\|D\Phi_\alpha-I\|\le16\sqrt6\,\alpha\max_i w_i\,h
\le\frac{289\sqrt6}{4096}<\frac7{40}.
\]

The last inequality can also be checked by squaring positive rationals:
501126/16777216 < 49/1600. The box is convex, so integration of the Jacobian
along a line gives the **global** bound

\[
\boxed{\frac{33}{40}\|w-w'\|
\le\|\Phi_\alpha(w)-\Phi_\alpha(w')\|
\le\frac{47}{40}\|w-w'\|.}
\]

Consequently Phi is one-to-one on the box and every rate Jacobian has
sigma_min>33/40, sigma_max<47/40, hence condition number <47/33. The
five-feature raw parameter map has determinant magnitude bounded below by
(g h alpha)^3 (33/40)^3, so it has rank 5 at every point in the box. Since
g and alpha are separately read, the finite full map is globally identifiable
on this box as well.

The condition number <47/33 belongs to the **normalized rate map**, not to
raw voltages or the full five-parameter map. Normalization divides sensor
errors by g h alpha, approximately multiplying them by 256 near nominal
parameters. The raw determinant carries h^3. This precision cost remains.

## 5. A constructive inverse that also handles noisy data

Let Omega=[15/16,17/16]^3 and let q be the normalized measured feature.
The iteration

\[
w_{n+1}=\Pi_\Omega\bigl(w_n+q-\Phi_{\widehat\alpha}(w_n)\bigr)
\]

is a contraction with factor <7/40. It has one fixed point even if noisy
q lies outside the image of Phi. From any initial point in the box,
(7/40)^n sqrt(3)/8 bounds distance to that fixed point; n=14 suffices for
distance <10^(-11). This is an a priori iteration bound, not a physical
convergence claim for a UD dynamical process.

If ||q-Phi_alphahat(w)||<=B and a computed point has certified projected
fixed-point residual <=rsolve, then

\[
\boxed{\|\widehat w-w\|\le\frac{40}{33}(B+r_{\rm solve}).}
\]

Proof: projection is nonexpansive. Compare the noisy fixed-point equation
with the noiseless one, use the 7/40 Lipschitz bound for Phi-I, and absorb
that term. The same argument with a residual gives the displayed result.
No assumption that noisy data admit an exact exponential fit is needed.

For certified evaluations at rational candidate parameters, write A_w=G/d
with integer sparse G. Integer powers G^n p give exact rational Taylor sums.
The skew-exponential integral remainder after degree N is bounded by
sqrt(2)||h alpha A_w||^(N+1)/(N+1)!. Degree 20 makes the coordinate error
<10^(-50) throughout the parameter box. Remainders must be included in the
residual bound. The included synthetic round trip verifies this procedure
on the actual 2640-coordinate operator; it is not experimental data.

## 6. Candidate measurement contract and acceptance rule

This contract is a sufficient design example, **not measured instrument
performance**. Assume the actual calibration preparation is p+delta_p with
||delta_p||<=xi; common readout gain is constant g; initial scalar noise is
bounded by nu0 and later three-channel vector noise by nu. The later true
reference-time interval differs from alpha h by at most jcal. Clip the gain
and clock estimates to [15/16,17/16]; clipping preserves their error bounds
when the true parameters are in this box.

Let |ghat-g|<=epsilon_g, |alphahat-alpha|<=epsilon_alpha. The initial reading
supplies epsilon_g <= (17/16)xi+nu0. With l=15/16 and u=17/16, a rigorous
feature-error ceiling is

\[
B=\frac{\nu+\sqrt2\epsilon_g+u\xi}{l^2h}
 +\frac{4\sqrt2u}{l}
   \left(\epsilon_\alpha+\frac{j_{\rm cal}}h\right).
\]

The first term accounts for additive sensor noise, gain normalization and
preparation error. The second uses the orthogonal propagator's Lipschitz
bound for clock-scale and interval-jitter errors.

| Declared ceiling | Exact value |
|---|---:|
| nu0, nu, xi | 1/10^12 each |
| epsilon_g, derived | 33/(16 times 10^12) |
| epsilon_alpha | 1/10^11 |
| jcal, reference-time units | 1/10^14 |
| Certified projected solver residual | 1/10^11 |

256-bit interval arithmetic then proves

\[
\|\widehat w-w\|<\frac2{10^9}.
\]

The enclosed upper-bound expression is approximately 1.867702043 times
10^(-9), including the solver residual. This is a deterministic norm bound,
not a confidence interval. It is conditional on the stated precision ceilings.

**Rate acceptance rule.** Accept compatibility with the prior r=3/10^9
envelope only if max_i |what_i-1|<=1/10^9. Triangle inequality then certifies
max_i |wi-1|<3/10^9. Calibration precision alone cannot show that the actual
rates are near 1; data must pass this acceptance rule. No rate adjustment or
feedback actuator is assumed. A failed check requires a new baseline
certificate or a separately authorized physical adjustment.

For common gain, dividing future readings by ghat leaves a scalar operator
error at most epsilon_g/(15/16), below the prior rho=1/100000 ceiling. This
does not certify unknown relative gain or arbitrary cross-talk.

If later samples are scheduled at logger times tj/alphahat, clock-scale
uncertainty causes absolute timing error <= tj epsilon_alpha/(15/16).
For the longest M=8192 schedule this is <=4.368534 times 10^(-8) reference
time units. Separately bounded per-sample jitter <=1/10^6 leaves total error
below the prior tau=3/10^6 ceiling for all three schedules. This requires the
clock calibration to remain valid over acquisition; drift is not inferred
from a short interval.

Under these accepted checks, H=I, stable rates and common gain, the parent
robustness bounds apply to gain-normalized data: rank 2640 and conditions
<748,<375,<306 for M=2048,4096,8192 respectively. The parent's additive-noise
bound must be applied after gain normalization. The calibration and subsequent
unknown-state experiment are distinct runs on the same stable plant.

In the noiseless joint inverse problem the calibration block has rank 5 and
the subsequent state-history block has rank 2640. Their block-triangular
Jacobian therefore has rank 2645, provided the plant passes the parent
observability conditions. This statement does not add unknown metric or
arbitrary readout parameters to the model.

## 7. What the protocol cannot identify

**EXACT NO-GO — general metric.** Let u0 equal 1 on all 120 vertex coordinates
and 0 elsewhere. The exact incidence operator gives Au0=0 and ||u0||^2=120.
For every eta>-1 the SPD matrix

\[
H_\eta=I+\eta\,u_0u_0^T/120
\]

satisfies H_eta A=A, hence H_eta^(-1)A=A. Its distance from I is |eta|,
yet every coordinate history for every known preparation is unchanged at
the unit-rate plant. Thus even complete knowledge of K cannot bound a general
metric error using dynamics alone in the candidate rule K=H^(-1)A_w.
This is an exact counterexample, not a small-rank numerical observation.

There are additional common metric/rate scale ambiguities when H is unknown.
The present rank-5 theorem expressly assumes H=I. A selected metric family
with independently measured references is necessary before claiming broader
identification. A known norm convention and a measured physical metric remain
different types of objects.

**OPEN — relative readout.** Four sensor scalars cannot certify an arbitrary
189 by 2640 readout error matrix. Either the common-gain structure must be
validated independently or richer calibration preparations and sensors must
be specified. Time-dependent gain, timing drift and nonlinear generator
terms are also outside the rank-5 model and require explicit discrepancy
receipts.

## 8. Governance, reproducibility and provenance

Attached ledger v0.39 entries O03, Q139, Q165 and Q169 are relevant: tolerances
remain protocol controls, frequency does not acquire physical units from
geometry, and the chain generator/support carrier remain mathematically
typed. No ledger entry is modified. The attached CRL-2 amendment describes
itself as a governance proposal; its development-lane distinction and
non-constructor-review warning are respected without assuming formal adoption.
This output is not registered or promoted. The unavailable Genesis image was
not used. No private attachment is redistributed.

Run `python certify_calibration.py` with the pinned requirements. The code
verifies the actual observed flag, integer jet identities and metric
counterexample, symbolic parameter ranks, uniform finite-time inequalities,
precision budgets, three rational forward evaluations and a synthetic inverse
round trip. The rank-5 conclusion is supported by the analytic uniform proof;
point evaluations alone are not a uniform rank certificate. Source hashes
and a fresh-directory byte-identical replay accompany the result.

**Next gate:** formulate a richer readout and metric calibration model with
explicit admissible parameter families, then certify what additional reference
measurements make those parameters identifiable. Apparatus implementation and
independent review remain required before experimental qualification.
