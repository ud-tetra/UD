# Preparation-specific origins, excitation and clocks

Development — no registry entry. Physical promotion0; independent review pending.
All bounds use the learned real modal model and an explicit unwrapped principal
frequency-band interpolation. They do not identify a physical clock, preparation
source, native metric or SI units. Same-team review is not independent review.

## 1. Raw modal blocks and origin rotations

Write the raw time-by-coordinate model as D[k,:]=p(k)B, with
p(t)=[1,cos(theta_j t),sin(theta_j t),...] and B of size105-by2294. Preparation a
selects the62 columns c*37+a, c=0,...,61. Its block is B_a. The learned theta and
integer B numerators are the pinned reference proposal, at scale2^-60.
The sketch is S=[W/64|v/128], size2294-by161; C=B S.

For a constant origin o_a,

\[
 p(k+o_a)B_a=p(k)R(o_a)B_a,\quad
 R_j(o)=\begin{pmatrix}\cos(\theta_j o)&\sin(\theta_j o)\\
 -\sin(\theta_j o)&\cos(\theta_j o)\end{pmatrix}.
\]

The stationary block is1. The forward sine signs are checked by an exact
quarter-turn waveform control and a production-layout interleaving test.
A common origin multiplies all B by ONE orthogonal left matrix, preserving
singular values of C exactly. Different origins act on different column blocks;
there is no single common left matrix. Let B_o collect those adjusted blocks,
and C_o=B_o S.

A simple exact counterexample uses stationary/cosine/sine preparations C=I3.
Moving only the sine preparation by a negative quarter-turn gives
C_o=[[1,0,0],[0,1,-1],[0,0,0]], rank2. Independent origins need not preserve
excitation. Likewise raw perturbation columns e_cos,e_sin, each norm1, become
e_cos,e_cos after rotating only the second column. The global operator norm
grows from1 to sqrt2. Per-column/block orthogonality is not global norm invariance.

## 2. Unknown origin box

Because ||R_j(o)-I||<=|theta_j o|, for any known origin vector

\[
 \|C_o-C\|_2\le\|S\|_F
 \sqrt{\sum_{a,j}\theta_j^2 o_a^2
 (\|A_{ja}\|_2^2+\|B_{ja}\|_2^2)}.
\]

For |o_a|<=xi this is <=K_o xi, with
K_o=||S||F sqrt(sum_aj theta_j^2(||A_ja||²+||B_ja||²)). This multiplier is computed
from exact learned integer coefficients and fixed phase numerators. A common
origin can be removed first; xi may bound remaining deviations from that origin.
If gamma<=sigma105(C), then gamma-K_o xi is a sufficient excitation margin.
A negative bound is inconclusive, not evidence of actual rank loss.

The current source gives K_o<16.771765. The frozen unknown-origin box2^-14 sample
units proves margin>0.00018941124, with no other preparation perturbation.
Box2^-13 is inconclusive by this proof. These are model-unit bounds, not SI clock
specifications or a necessary boundary.

## 3. Stronger certificates for declared offset patterns

For four frozen origin vectors, sine/cosine rotations are validated at512-bit
precision and rounded to60-bit dyadics, entry error<2^-60. There is no intermediate
coefficient rounding: exact multiplication by B produces approximate B_o at
scale2^-120, then approximate C_o at scale2^-127. Every rotation block error has
operator norm<=2^(1-60), so

\[
 \|C_o-\widetilde C_o\|_2\le
 \epsilon_{rot}:=2^{1-60}\|B_{osc}\|_F\|S\|_F.
\]

This is<2.152e-17 for the pinned source. For the exactly zero origin the error
is exactly0. Stored rotation integers are recomputed and checked against the
same rational origins during replay; no object-pickle matrix is trusted.

An untrusted binary64 H_o is encoded exactly. Small integer Grams validate
rho_o>=||tilde C_o H_o-I||<1 and h_o>=||H_o||. Then

\[
 \sigma_{105}(C_o)\ge\gamma_o:=(1-\rho_o)/h_o-\epsilon_{rot}>0.
\]

Both right-inverse accuracy and transcendental rotation error are accounted for.
The specific profile must be the declared comparison profile; unknown deviations
need their own origin-box or timing-residual budget. Stored known-profile cases
use origin-box0, not an additional uncharged offset uncertainty.

Common-origin singular values are invariant, but the row-sum upper bounds used
for H_o are basis-dependent. Different conservative LOWER bounds for zero and
common origins do not imply a physical or true conditioning change. Larger
lower bounds alone do not order the true condition numbers of two profiles.

## 4. Preparation errors require block bounds

Let E_a be an uncertain raw modal block for preparation a, ||E_a||2<=p_a. The
same-preparation origin rotation preserves this block operator norm. With
arbitrary dependence between preparations,

\[
 \|E_o\|_2\le\sqrt{\sum_a p_a^2},\quad
 \|E_o S\|_2\le\|S\|_F\sqrt{\sum_a p_a^2}=:p_C.
\]

For unknown origins a sufficient remaining coefficient margin is
gamma-K_o xi-p_C. For a declared directly certified profile it is gamma_o-p_C.
It must be strictly positive. The numeric grid chooses uniform p_a so that
p_C<=r gamma (or r gamma_o for the specific profile), with r frozen in advance.
The exact reported dyadic p_a bound is rounded down; the computed r gamma loss
therefore safely upper-bounds the actual loss.

This per-preparation raw modal bound is not a physical state-preparation error
or a state-to-coefficient map. A prior global ||E||2 bound cannot simply be kept
unchanged after differential origins. The sqrt(sum p_a²) rule, rather than an
unsupported global invariance assumption, is used in every numeric budget here.

## 5. Preparation-specific rate and jitter

Assume times tau_ak=o_a+(1+epsilon_a)k+u_ak, common across the62 channels of a
preparation but not necessarily common across preparations. Declare
|epsilon_a|<=mu_a and |u_ak|<=j_a. With

\[
 L_a=\sum_j |\theta_j|
 \sqrt{\|A_{ja}\|_2^2+\|B_{ja}\|_2^2},\qquad
 \Omega^2=\sum_j\theta_j^2,
\]

the nominal raw output derivative norm is<=L_a. Pair rotations preserve each
pair energy, so nominal L_a is unchanged by constant o_a. Preparation uncertainty
adds at most Omega p_a, because the real derivative row has norm Omega and
||p'(t)E_a||<=Omega||E_a||. There is no assumption that the coefficientwise sum
of perturbation pair norms is itself <=Omega p_a.

Define w_a=mu_a sqrt(sum k²)+sqrt(n)j_a, where sum k²=n(n-1)(2n-1)/6 exactly.
Then the sketched timing residual obeys the global, non-linearization bound

\[
 e_t\le\|S\|_F
 \sqrt{\sum_a(L_a+\Omega p_a)^2 w_a^2}.
\]

No statistical independence of clocks, jitters, preparations or channels is
required. The numeric grid uses common UPPER BOUNDS mu,j,p_a across preparations;
the actual errors can differ arbitrarily within them. With uniform upper bounds,
e_t<=||S||F sqrt(sum_a(L_a+Omega p_a)²)(mu sqrt(sum k²)+sqrt(n)j).

Add raw62-vector acquisition error delta and a separately justified model floor:
e=e_t+sqrt(37 n)||S||F delta+nu_model. The grid uses the inherited clean-fit
residual as a DECLARED nu_model example. It is not a future-instrument or
changed-preparation guarantee. Constant deviations from a declared origin profile
may be charged as part of u_ak; they are not silently free.

## 6. Ideal-estimator phase transport

Let g be the remaining positive coefficient margin. Then
L=sqrt(na/2)g lower-bounds sigma105 of the comparison model P C_adjusted.
For exact top105 SVD and exact least-squares shift, use

\[
 t=e/(L-e),\quad d=\sqrt{2-2\sqrt{1-t^2}},\quad
 K=\sqrt{b/a},\quad\beta=\sqrt{1-q/(na)},\quad
 R=K d(1+K)/(\beta-d).
\]

Require L>2e,d<beta,R<1,2R<s. The singular-subspace projection, orthonormal
alignment, deleted-row bound, diagonal resolvent and homotopy proof then yield
unique reference-phase matching and phase error<=asin(R). The complete parent
argument is reproduced in PARENT_CLOCK_THEOREMS.md. Reference frame constants
and s are recomputed here. Actual data need not have exact rank105; this is
leading-subspace separation around a rank105 comparison model.

This is an exact-estimator theorem, not general floating convergence or a new
actual floating-output run. Future outputs still need PR189's basis/shift,
eigenpair/inverse and emitted-argument residual checks. There is no new
full-Hankel1893-value certificate, acquisition admission or raw-record generation.

## 7. Scope and metrology obligations

The unwrapped principal-band interpolation is declared. Integer-sampled aliases
alone do not bound jitter sensitivity; source-frequency scale remains confounded
with clock rate without calibration. Preparation-specific clocks are covered
only with the stated maps, source bandwidth/interpolation, modal-block errors,
positive excitation margin and noise bounds. Physical preparation/readout/metric
sources, SI sample interval, instrument clock bounds, covariance and dependence
models, cost/disturbance and actual acquisition validation remain open.

Grid maxima are sufficient budgets on frozen dyadic grids, not optimal boundaries.
Individually varied maxima cannot be combined without summing their errors.
Known-pattern certificates and worst-case boxes have different scopes; large
specific offsets may certify when the worst-case box proof is inconclusive.
All HOLD/one-sided cases are preserved as proof limitations, not measured failure.
Two parallel same-team reviews do not close independent review/replay obligations.
The nominal747-dimensional hidden space,62 history channels and separate189
diagnostic outputs remain unchanged. O03 parameters are protocol controls,
never theory constants. Physical promotion0; development — no registry entry.
