# UD grade-metric and individual-gain calibration v0.1

**RESULT / STATUS — DERIVED CONDITIONAL; development — no registry entry.**
A specified three-preparation protocol identifies 189 individual gains, four
grade metric weights, three rates and one clock scale: **197 parameters**.
It uses 195 sensor scalars and two independent scale references. The normalized
six-ratio finite response map is globally one-to-one on the stated box, with
Jacobian condition number <3/2. This is an extension within an explicitly
chosen finite model. Physical promotion = 0. Constructor verification passed;
independent review pending. No apparatus data were supplied.

## 1. Candidate family and source assumptions

Retain the real 2640-coordinate 600-cell chain carrier, oriented incidence
maps, generator channels A1,A2,A3, and 189-coordinate readout R. The chain
grade dimensions are (120,720,1200,600). Write

\[
H=\operatorname{diag}(h_0 I_{120},h_1 I_{720},
                      h_2 I_{1200},h_3 I_{600}),\quad
A_w=\sum_{k=1}^3 w_k A_k,\quad K=H^{-1}A_w,
\]
\[
y(u)=D_g R e^{\alpha u K}p,\qquad
D_g=\operatorname{diag}(g_1,\ldots,g_{189}).
\]

All h, w, g and alpha are positive and fixed during calibration and subsequent
acquisition. u is logger time and t=alpha u is time in a chosen reference
unit after setting the preparation event to zero. This is an affine clock
with known origin; offsets, nonlinear drift and jitter are separately scoped.

**CANDIDATE choices:** H is scalar on each chain grade, the evolution rule is
K=H^(-1)A_w, readout errors are diagonal gains, offsets are zero, and known
chain-coordinate preparations are available. These choices are not derived
as native physical laws. H is a chain-space metric, not a spacetime metric.
The reference-time convention does not derive physical seconds from UD.

The exact identities Ai Aj=0 for i!=j follow from consecutive boundary maps
multiplying to zero. Their active subspaces are mutually orthogonal. On the
kth active subspace K has off-diagonal blocks -dk Bk and uk Bk^T, where

\[
d_k=\frac{w_k}{h_{k-1}},\qquad
u_k=\frac{w_k}{h_k},\qquad
q=(d_1,u_1,d_2,u_2,d_3,u_3).
\]

Consequently ||K(q)|| <=4 max_i qi, using the parent ||A||<4 bound and the
orthogonal active-subspace split. This norm bound is valid although K is
generally not skew in the Euclidean metric. It is H-skew. Replacing a dense
H by grade scalars is a substantive restriction, not a change of notation.

## 2. Two scale ambiguities and their references

Even exact knowledge of all directed slopes leaves these transformations:

1. (alpha,w)->(c alpha,w/c), leaving the generator in logger time unchanged.
2. (H,w)->(cH,cw), leaving K unchanged.

In logarithmic coordinates the six logger-time slope magnitudes are
log alpha+log wk-log htarget. Their 6 by 8 parameter matrix has rank 6.
The two independent null directions are

\[
(\delta\log\alpha,\delta\log h,\delta\log w)
=(1,0,-\mathbf1_3),\quad (0,\mathbf1_4,\mathbf1_3).
\]

An independent **clock-scale observation alpha** and an independent
**metric-scale observation h0** remove these two ambiguities. Appending their
logarithms gives an integer 8 by 8 matrix of determinant -1. The reference
for h0 may be replaced by another independent scale constraint transverse to
the same null direction, such as an independently known rate. A convention
h0=1 selects a mathematical representative; it is not a measured physical
metric receipt. This protocol requires the declared h0 uncertainty if its
numerical metric-error guarantee is to be used.

Given alpha, the six reference-time ratios q and h0 determine every weight:

\[
\boxed{h_k=h_0\prod_{i=1}^k\frac{d_i}{u_i},\qquad
w_k=h_0d_k\prod_{i=1}^{k-1}\frac{d_i}{u_i}.}
\]

The transformation between (h0,h1,h2,h3,w1,w2,w3) and (h0,q) is a smooth
bijection on positive parameters. These are identifiability equations for
the chosen family, not physical estimates from existing data.

## 3. Three known preparations and the actual sensor coordinates

Let e_j denote the chain coordinate vector with coefficient 1 at coordinate j.
The fixed observed coordinates used dynamically are:

| Coordinate | Grade | Oriented simplex |
|---:|---:|---|
| 1 | 0 | (1) |
| 133 | 1 | (1,11) |
| 486 | 1 | (33,34) |
| 878 | 2 | (1,11,87) |
| 1680 | 2 | (33,34,41) |
| 2040 | 3 | (0,33,34,41) |

All are in the existing 189-coordinate readout. Use these independent runs:

**Gain preparation:** pG=R^T 1_189. At the known preparation event u=0,
read all 189 outputs. The ideal vector is exactly g, independent of H and w.
The initial gain map has identity Jacobian. pG has 189 unit coefficients and
norm sqrt(189). Realizing and verifying this input is an external requirement:
one run here contains **189 known coordinate amplitudes**, not one unverified
scalar amplitude assumption. Unknown individual preparation amplitudes would
be confounded with the individual gains.

**Dynamic preparations:** pA=e1+e1680 and pB=e133+e2040. Their norms are
sqrt(2); the combined norm of pA direct-sum pB is 2. Choose logger h=1/32.
After independently preparing each, read the following at u=h, divide by its
calibrated individual sensor gain, and apply the indicated sign:

| Ratio feature | Preparation | Output coordinate | Sign |
|---|---|---:|---:|
| d1 | B | 1 | +1 |
| u1 | A | 133 | -1 |
| d2 | A | 486 | -1 |
| u2 | B | 878 | +1 |
| d3 | B | 1680 | -1 |
| u3 | A | 2040 | +1 |

Every named dynamic output has zero prepared coefficient. The six signed
initial slopes, divided by alpha, are exactly q. The full-carrier integer
jet matrix is I6. The preparations were chosen to avoid first-order mixing
of the directed channels in these six outputs. Higher-order mixing is retained
in the finite exponential map; it is not discarded.

The sensor count is 189 initial gain values plus six finite response values,
total 195. The clock and metric scale references add two scalars, total 197.
These counts assume the specified known preparations and model. They do not
establish globally minimal experimental effort or count the effort needed
to verify 189 preparation amplitudes. Optional initial/off-channel readings
would be additional model checks, not part of the rank count.

## 4. Finite-map theorem: no derivative oracle

Let L extract the six signed coordinates from the direct-sum states for runs
A and B. For known alpha define

\[
\Psi_\alpha(q)=\frac{1}{h\alpha}\mathcal L
 \left(e^{h\alpha K(q)}p_A\oplus
       e^{h\alpha K(q)}p_B\right).
\]

Each preparation is supported on one grade parity, while its extracted outputs
have the opposite parity. Since K flips parity, every even Taylor power
vanishes in these outputs. Thus Psi=q plus odd-power terms starting at order 3.
Let gains, alpha and q_i lie in [15/16,17/16]; let h0 and its estimate also
lie in that interval. This box is in **directed ratios**, not independently
in all h and w. Reconstructed h and w can span a wider range before acceptance.

For a directed generator derivative Ti, ||Ti||<4. The derivative of K^n is
the sum of n products K^r Ti K^(n-1-r), so its norm is <=4n||K||^(n-1).
The combined preparation has norm 2. Summing the odd powers n>=3 gives
each Jacobian error column norm <=8[cosh(z)-1], with
z=4h alpha max qi. A Frobenius bound over six columns yields

\[
\|D\Psi_\alpha-I_6\|
\le8\sqrt6[\cosh(289/2048)-1]
<\frac15.
\]

The interval-enclosed expression is approximately 0.195430324. Integrating
the Jacobian along segments in the convex ratio box proves the **global**
inequalities

\[
\boxed{\frac45\|q-q'\|\le
\|\Psi_\alpha(q)-\Psi_\alpha(q')\|
\le\frac65\|q-q'\|.}
\]

Hence Psi is one-to-one and the normalized six-ratio Jacobian has condition
number <3/2 throughout the box. Its determinant magnitude is >(4/5)^6.
This does not give a condition number <3/2 for raw sensor voltages, the log
metric reconstruction, or the entire 197-parameter problem. Dividing by
sensor gain and h alpha amplifies raw errors, and scale references contribute
their own uncertainty.

With all gain readings, the two scale references and the six finite responses,
the full parameter map is globally identifiable on this domain and has
Jacobian rank **197**. The proof is block triangular: 189 gain coordinates,
the two scale observations, and the invertible six-ratio map, followed by the
smooth metric/rate reconstruction. At the jet level the ranks are 195 without
scale anchors, 196 with clock anchor only, and 197 with both anchors.

## 5. Constructive inverse and uncertainty propagation

For normalized finite data z, use

\[
q_{n+1}=\Pi_\Omega[q_n+z-\Psi_{\widehat\alpha}(q_n)],
\quad \Omega=[15/16,17/16]^6.
\]

This is a contraction with factor <1/5. It is defined even when noisy z is
outside the model image. If its certified fixed-point residual is <=rs and
||z-Psi_alphahat(q)||<=B, then

\[
\|\widehat q-q\|\le\epsilon_q:=\frac54(B+r_s).
\]

The same nonexpansive-projection argument as in the preceding calibration
applies. From any starting point in the box, 17 iterations suffice for a
residual below 10^(-12) in exact arithmetic, using the box diameter sqrt(6)/8.
Actual arithmetic/evaluation error must be enclosed in a certified residual.

Let epsilon0 bound the error in log h0, and let epsilon_log=epsilon_q/(15/16).
The mean-value theorem for log gives componentwise log-ratio errors at most
epsilon_log. Reconstruction then gives

\[
|\Delta\log h_k|\le\epsilon_0+2k\epsilon_{\log},\quad
|\Delta\log w_k|\le\epsilon_0+(2k-1)\epsilon_{\log}.
\]

The exact 7 by 7 log reconstruction matrix is integer, with Frobenius norm
squared 28. Its rows explicitly accumulate the ratio uncertainties; no
claim that reconstruction is perfectly conditioned is made.

If h0 and h0hat are in the declared box, both true and estimated weights obey
hmax=83521/54000 and wmax=83521/57600. Uniform absolute ceilings are therefore

\[
\epsilon_H=h_{\max}[e^{\epsilon_0+6\epsilon_{\log}}-1],\quad
\epsilon_w=w_{\max}[e^{\epsilon_0+5\epsilon_{\log}}-1].
\]

## 6. Candidate precision contract

These are sufficient proposed requirements, not measured apparatus performance
or theory constants. Let l=15/16, u=17/16, OmegaK=4u, h=1/32.

| Quantity | Exact ceiling | Norm/type |
|---|---:|---|
| Gain preparation error at its readout | 1/10^13 | Infinity norm of observed prepared coefficients |
| Initial gain-read noise | 1/10^13 | Infinity norm, 189 outputs |
| Dynamic preparation error | 1/10^13 | Combined two-run Euclidean state norm |
| Dynamic sensor noise | 1/10^13 | Euclidean norm of six scalars |
| Clock-scale estimate error | 1/10^12 | Absolute alpha error |
| Dynamic calibration interval jitter | 1/10^15 | Absolute reference-time interval error |
| Metric-scale reference error | 1/10^11 | Absolute error in log h0 |
| Certified projected solver residual | 1/10^12 | Normalized ratio-feature norm |

Clip gain and clock estimates to their known box. The individual gain error
is <=epsilon_g=u xiG+nuG=33/(16 times 10^13). No independent-noise assumption
or stochastic averaging is used. Constant gains and stable clock/rates/metric
are required across the different runs and later acquisition.

For dynamic combined preparation error xi, raw six-value noise nu, clock error
epsilon_alpha and calibration jitter jcal, set
E=exp[OmegaK(uh+jcal)]. A valid feature-error ceiling is

\[
B=\frac{E(\nu+2\epsilon_g+u\xi)/l
       +2\Omega_K E(h\epsilon_\alpha+j_{\rm cal})}{hl}.
\]

The factor 2 is the combined nominal preparation norm. The exponential factor
is retained because K is not Euclidean-skew. The gain error is diagonal, so
its operator norm is the maximum relative gain error; a factor sqrt(189) is
not required for this particular operator bound.

256-bit interval arithmetic gives these conservative ceilings:

| Recovered quantity | Exact declared error ceiling | Enclosed bound, display only |
|---|---:|---:|
| Four metric weights, maximum absolute error | 5/10^10 | 4.821588 times 10^(-10) |
| Three rates, maximum absolute error | 4/10^10 | 3.791033 times 10^(-10) |
| Six-ratio vector error | Exact expression above | 4.714638 times 10^(-11) |

They are deterministic conditional bounds, not confidence intervals. The
very small input ceilings and reference requirements are experimental design
burdens; satisfying the mathematical inequalities does not demonstrate their
feasibility in a particular device.

**Acceptance rule:** require each estimated metric weight and each estimated
rate to be within 2/10^9 of 1. The error ceilings then imply
||H-I||<3/10^9 and max|wk-1|<3/10^9. Merely estimating parameters accurately
does not show that these parameters are near nominal values; measurements
must pass this gate. No feedback or physical parameter adjustment is assumed.

After dividing future sensor readings by their individual gain estimates,
the residual readout error is <=epsilon_g/l, below 1/100000. This conclusion
uses diagonal gains. It does not control an arbitrary matrix of cross-talk.

Schedule logger times at tj/alphahat for tj=j/2. For the 8192-snapshot profile,
clock-scale error contributes at most 4.368534 times 10^(-9) reference-time
units. Separately certifying acquisition jitter <=1/10^6 keeps total error
below the parent 3/10^6 ceiling for all three profiles. A short clock reference
does not itself certify long-term clock stability.

Under these accepted checks and the declared family, the parent full-state
conditions apply to gain-normalized data: rank 2640, kernel 0, condition
numbers <748,<375,<306 for M=2048,4096,8192. Additive-noise receipts must also
be normalized by the individual estimated gains. The combined noiseless
calibration-plus-unknown-state inverse has Jacobian rank 197+2640=2837,
conditional on these parent observation bounds and a stable plant.

## 7. What this result leaves open

**General metric NO-GO remains.** The previously constructed harmonic metric
family H=I+eta u0u0^T/120 leaves H^(-1)A=A at unit rates. That family is
excluded by the grade-scalar restriction. This extension therefore does not
invalidate the general-metric obstruction. It identifies a declared finite
family using a new independent metric-scale reference.

**Readout-family validation remains.** The initial gain vector can absorb an
unknown contribution E pG if actual readout is Dg R+E. These 195 sensor values
do not establish that E=0, nor that offsets, drift and nonlinearities vanish.
Off-diagonal metric terms may also violate the finite family. Held-out probes
with explicit detectable alternatives and thresholds are required to test
model discrepancy before applying this calibration as an experimental claim.

**Preparation and scale references remain external.** Known vector amplitude,
relative coefficients and addresses are not supplied by topology. An h0
normalization convention is not an empirical metric identification. No
native law selecting these apparatus quantities is derived here.

## 8. Verification, source status and governance

`python certify_grade_calibration.py` reproduces the exact observed simplex
selection, full-carrier cross-channel identities, gain map and directed jet,
symbolic two-scale ranks, the parity-based finite bound, precision propagation,
three rational forward evaluations and one synthetic inverse round trip.
Integer weighted incidence powers produce exact rational Taylor sums. Degree
32 and the general exponential remainder give feature-vector error <10^(-50)
throughout the box. The finite rank theorem is analytical and uniform; three
point checks alone would not prove it. Clean replay uses a fresh directory
with identical frozen inputs. Constructor checks are not independent review.

A pre-release interval residual evaluation needed repair near exact zero;
CORRECTIONS.json records it. It did not change an earlier capture or the
analytic rank/uncertainty theorems. All source versions and prior captures
remain immutable.

The attached coefficient ledger's O03 controls, Q139 clock gap, Q165 support
carrier and Q169 generator remain scoped. No ledger entry is edited. The
attached CRL-2 amendment labels itself a proposal; this work remains in its
development distinction and makes no registry promotion. Attachments were
read for provenance and are not redistributed. The unavailable Genesis image
was not used. Repository main and the parent local captures are source-bound
in PROVENANCE.json. Local capture is separate from public publication.

**Next gate:** specify held-out tests for off-diagonal metric terms, sensor
cross-talk and temporal drift, prove what those probes can detect, and attach
explicit rejection thresholds. An independent reviewer and an apparatus
implementation are still required before experimental qualification.
