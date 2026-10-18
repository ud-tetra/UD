# Preparation excitation and common-clock phase bounds

Development — no registry entry. Physical promotion 0. Exact conditional
finite-matrix results plus constructor interval calculations. Two parallel
same-team mathematical reviews informed the derivation; independent review is
pending. No SI timing or physical preparation identification is established.

## 1. Source-bound temporal excitation

Let P(k)=[1,cos(k theta1),sin(k theta1),...] be the fixed real temporal frame,
n=8191,q=105. The theta values are the pinned learned positive dyadic phases.
Let S=[W/64|v/128] be the unchanged2294-by-161 sketch. The exact learned real
sketch coefficient matrix is C=(coeff [2W|v])/2^67, of size105-by-161.
No nominal operator or nominal source frequencies are loaded.

For any untrusted right-inverse witness H, validated bounds
rho>=||CH-I||2<1 and h>=||H||2 imply

\[
 \sigma_{105}(C)\ge\gamma:=(1-\rho)/h>0.
\]

Indeed CH is invertible, R=H(CH)^-1 is a right inverse of C, and
||R||<=h/(1-rho). The minimum-norm right inverse cannot have greater norm.
All float entries of H are encoded exactly as dyadic integers. Residual and
norm bounds use exact small integer Grams and validated outward arithmetic.

If a preparation-induced coefficient perturbation satisfies ||E||2<=p<gamma,
then sigma105(C+E)>=gamma-p. If aI<=F*F/n<=bI for the complex exponential frame,
the real/complex column transform has minimum singular value1/sqrt(2), so

\[
 \sigma_{105}(P(C+E))\ge L:=\sqrt{na/2}(\gamma-p).
\]

This is temporal excitation of a learned sketched model, not spatial rank1893,
state controllability, a result from the number37 alone, or a physical preparation
error limit. A source map from laboratory/preparation errors to E is still
required. If raw modal coefficient error is DeltaB, a sufficient conversion is
||E||<=||DeltaB|| ||S||; a physical state-to-modal map needs its own justified norm.

## 2. Declared interpolation and common-clock perturbations

Adopt explicitly P(t)=[1,cos(theta_j t),sin(theta_j t),...] with the pinned
unwrapped representatives theta_j in(0,pi), and t in nominal sample-index units.
This interpolation is a model assumption; integer samples alone do not select it.
Put Omega^2=sum_j theta_j^2 over the52 positive phases. Every derivative row of
P(t) has exactly squared Euclidean norm Omega^2. Integration therefore gives

\[
 \|P_v-P\|_2\le\|P_v-P\|_F
 \le\Omega\|v\|_2.
\]

This is a global derivative bound, not a truncated
Taylor approximation; no unaccounted quadratic remainder is discarded.

For a common clock tau_k=o+(1+epsilon)k+u_k with |epsilon|<=mu and |u_k|<=j,
a common constant origin o rotates every real coefficient pair by the same
block-orthogonal matrix. It preserves coefficient singular values, coefficient
norm and temporal span exactly. It may be absorbed without an error charge.
The remaining timing vector satisfies

\[
 \|v\|_2\le
 \mu\sqrt{n(n-1)(2n-1)/6}+\sqrt n\,j.
\]

If Z=P_v(C+E)+N with ||N||2<=nu, after any common-origin rotation,

\[
 \|Z-P(C+E)\|_2\le
 e:=\Omega\|v\|_2(\|C\|_2+p)+\nu.
\]

For raw62-vector errors bounded by delta over37 preparations and n times,
||raw_error S||2<=sqrt(37 n 371097/4096) delta. The numeric grid uses
nu=nu_model+this bound, with the pinned clean fitted-reference residual as the
DECLARED nu_model floor. This is a conditional model-family example; a past fit
residual is not a guaranteed noise/model floor of a future instrument or a
changed preparation. Future acquisition must independently justify its own nu.

## 3. Transport to the exact SVD/least-squares estimator

For the exact top105-SVD basis of Z and its exact least-squares shift, define

\[
 t=e/(L-e),\quad d=\sqrt{2-2\sqrt{1-t^2}},\quad
 K=\sqrt{b/a},\quad\beta=\sqrt{1-q/(na)},\quad
 R=K d(1+K)/(\beta-d).
\]

If L>2e, the leading model subspace is separated. Projection of its singular
vector equation gives principal sine<=t. Unitarily aligning orthonormal bases
gives distance<=d. The reference frame's deleted-row singular value is>=beta;
its shift J has norm and diagonalizer condition<=K. Least-squares residual
transport gives ||T-J||<=d(1+K)/(beta-d). The diagonal resolvent bound and a
reference-to-perturbed-matrix homotopy then place one eigenvalue in each reference
disk when d<beta,R<1 and2R<s, where s is the minimum unit-circle chord separation.
The circular phase error is<=asin(R). Frame constants and s are recomputed
from fixed phase integers, not accepted on citation alone.

This is an a priori theorem for the EXACT estimator. It does not prove the
behavior or convergence of every floating SVD/LS implementation. Actual
floating outputs still require the orthogonality, span/shift, eigenpair,
inverse and emitted-argument checks of PR189. No new actual-floating run or
full-Hankel signature execution is claimed in this return.

The74 grid rows and the separate joint example are conditional sufficient
bounds. The largest passing dyadic budget on a frozen grid is not optimal or
necessary, and isolated maximum budgets cannot be combined without adding their
error contributions. ONE_SIDED/HOLD outcomes are proof limitations, not measured
failures. The full raw vector budget2^-20 remains without unique matching here.

## 4. Preparation-specific offsets and clocks

Constant offsets for different preparations can each be absorbed into their own
coefficient-column pair rotations, leaving the declared reference temporal
space available. They do not necessarily preserve its excitation. Different
column rotations are not one common left-orthogonal transform. The finite
control with C=I3 and one sine preparation shifted by minus one quarter-turn
has adjusted C=[[1,0,0],[0,1,-1],[0,0,0]], rank2. A fresh coefficient-rank
margin or a justified coefficient-error bound is necessary.

Preparation-dependent time-varying clocks likewise cannot use P_v C with a
single common P_v. For raw preparation a, a sufficient vector Lipschitz constant
is L_a=sum_j |theta_j| sqrt(||A_ja||2^2+||B_ja||2^2). A separately bounded
raw error delta_ak<=p_a+noise_ak+L_a(k mu_a+j_a) yields
||raw_error S||<=||S|| sqrt(sum_ak delta_ak^2). Adjusted comparison amplitudes
must retain a separately certified excitation margin. This extension is derived
but is not instantiated by the common-clock numeric grid in this package.

## 5. Two exact identifiability obstructions

ALIAS/JITTER NO-GO. Modes theta and theta+2pi m agree at every integer k. At
u=1/(2m), their relative phase is exp(i2pi m u)=-1, so their unit-complex sample
discrepancy is exactly2 although u tends to0. Thus sampled phases alone imply
no finite uniform jitter Lipschitz bound. An unwrapped interpolation, bandwidth
restriction or independently bounded source generator is essential. Choosing
the principal representative internally does not establish a physical band.

CLOCK-SCALE NO-GO. A source theta sampled with clock1+epsilon is identical at
every k to a source theta'=(1+epsilon)theta sampled with clock1, within any
suitable interior band. Even infinitely many noiseless samples cannot separate
source scale from clock rate without an external clock convention/calibration.
Finite controls validate instances; the algebra proves the general obstruction.

Loss of an entire mode pair or a preparation in the sketch kernel also leaves
that phase unexcited. No amount of observer history recovers an absent mode
without an excitation/source assumption. None of these results changes the
nominal747-dimensional dynamical observer kernel or implies hidden-state leaks.

## 6. Experimental obligations and governance

Before applying these model-unit bounds, supply a source/band justification,
calibrated clock-rate/jitter bounds, preparation-to-coefficient map and error
bound, excitation margin, acquisition/model-noise floor and their dependence
assumptions. Convert sample-index quantities to SI only through a separately
calibrated sample interval. Then validate actual floating outputs and apply
full record/Hankel/acquisition criteria separately. Temporal order, phase
matching, exact algebraic rank and the retained1893-value spectral signature
are distinct.62 history channels and189 diagnostic outputs remain distinct.

Two parallel assistants provided same-team mathematical review, not an
independent non-constructor attestation. Review HOLD177 and independent replay130
remain open. O03 tolerances remain protocol controls, never theory constants.
Physical promotion0; development — no registry entry.
