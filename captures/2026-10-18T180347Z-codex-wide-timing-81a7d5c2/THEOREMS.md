# Wider timing sketch: finite counts and temporal closure

Development — no registry entry. Physical promotion 0; independent review pending.
This is a diagnostic of two already known synthetic PR195 records. It is not
independent discovery, a new acquisition, or an extension of the phase adapter.

## 1. Waveform span and shift closure are different

For preparation a, set s=(-1)^a and
t_ak=o_a+(1+s mu)k+s j0(-1)^k. Origins are preparation-specific constants.
For each of the 52 positive reference phases theta_j, let

\[
 \omega_{js}=(1+s\mu)\theta_j,\qquad
 g_{js}(k)=e^{i\omega_{js}k}e^{is\theta_jj_0(-1)^k}.
\]

The factor e^(i theta_j o_a) rotates that preparation's coefficients and does
not add a temporal function. With two rate classes, the real waveform family
has at most one stationary column and two real functions per pair per class:

\[
 \operatorname{rank}D_{\rm model}\le1+52\cdot2\cdot2=209.
\]

The sideband decomposition is

\[
 g_{js}(k)=\cos(\theta_jj_0)e^{i\omega_{js}k}
       +is\sin(\theta_jj_0)e^{i(\omega_{js}+\pi)k}.
\]

The two sideband amplitudes are tied. Counting them independently would wrongly
identify the observation-column bound as 417. One-step shifts can separate the
tied components, giving a shift-invariant closure bound of at most
1+52*2*4=417. Both are upper bounds: collisions, absent amplitudes or coefficient
dependence may lower them. No exact dimension 209 or 417 is asserted.

Two-step shifts instead preserve the original waveform family exactly:

\[
 g_{js}(k+2)=e^{2i\omega_{js}}g_{js}(k).
\]

This supplies a possible future stride-two adapter. It does not extend PR189
automatically: sampled collisions modulo pi, excitation, finite conditioning,
subspace truncation, actual solver residuals and phase emission all need checks.

## 2. Nested sketches and two threshold rules

The integer sketch matrix is A=[2W_old | v | 2W_new], with denominator 128.
W_old is regenerated in its ORIGINAL 2294-by-160 shape with seed172026.
W_new is a separately frozen 2294-by-160 sign matrix with seed184052.
Widths 161,257,321 select nested column prefixes. Generating a larger matrix
with the old seed and selecting its first160 columns would not preserve the
old sketch because its row stride changes RNG consumption.

For S_m=A_m/128, its exact squared Frobenius norm s_m^2 is recomputed.
Let tau be the exact positive dyadic cutoff from the parent SKETCH_RULE.json.
The two frozen diagnostic thresholds are

\[
 t_{m,\rm common}^2=\tau^2,\qquad
 t_{m,\rm scaled}^2=\tau^2s_m^2/s_{161}^2.
\]

Both squared thresholds are exact rationals. Their comparisons do not use
rounded displayed decimals. For a declared per-preparation62-vector error delta,
||E S_m||2 <=sqrt(37*8191)*delta*||S_m||F. The scaled rule preserves the parent's
threshold/noise-envelope ratio, using delta=2^-20 for that diagnostic comparison.
The stress record is NOT asserted to satisfy an additive-to-old-clean error
ball. Neither rule creates acquisition admission or a new theory constant.

Nested prefixes imply Z_next Z_next^T-Z_old Z_old^T is positive semidefinite.
Therefore counts above a COMMON threshold cannot decrease. Scaled-threshold
counts have no such monotonicity requirement.

## 3. Exact small Grams from every encoded reading

The raw little-endian int64 records have shape(37,8191,62), quantum2^-48.
Reshape to X of size8191-by2294 with coordinate index c*37+a. Before int64
matrix multiplication, verify max|X|*max_column_l1(A)<2^63, which bounds every
partial sum. Hence N=X A is exact, and the mathematical sketch is Z=N/2^55.

\[
 G=Z^TZ=N^TN/2^{110}.
\]

The integer numerator Gram is formed exactly with FLINT and stored losslessly
as decimal integers. Its dimension is321, with smaller widths using principal
prefixes. Hashes bind the complete raw record before/after projection. A second
complete raw projection reproduces every Gram integer. No8191-by8191 temporal
Gram or full Hankel array is stored.

This certifies the exact mathematical sketch of the encoded bytes. It does
not silently equate that sketch with a separately computed floating BLAS
product. Floating eigensystems below are untrusted certificate proposals.

## 4. Validated eigenvalue enclosure

Let Q be an untrusted square dyadic eigenvector proposal, Lambda a sorted real
dyadic diagonal proposal, and compute exact residual norms with validated roots:

\[
 \eta\ge\|Q^TQ-I\|_2<1,\quad
 r\ge\|GQ-Q\Lambda\|_2,\quad g\ge\|G\|_2.
\]

Frobenius norms bound each operator norm; all residual numerators and scales
are exact integers. Set qnorm=sqrt(1+eta) and
d=eta/(1+sqrt(1-eta)). The polar factor O of Q is orthogonal with ||Q-O||<=d.
The identities and triangle inequality give

\[
 \|G-Q\Lambda Q^T\|\le g\eta+r\,qnorm,
\]
\[
 \|Q\Lambda Q^T-O\Lambda O^T\|
 \le\|\Lambda\|d(qnorm+1).
\]

Thus each ordered eigenvalue of symmetric G lies within
R=g*eta+r*qnorm+||Lambda||*d*(qnorm+1) of the corresponding Lambda entry.
The checker uses512-bit interval arithmetic and outward rational rounding.
Strict lower>threshold_squared certifies above; strict upper<threshold_squared
certifies below. Any intersection is retained as HOLD. This proves counts for
the encoded mathematical sketch, rather than trusting floating eigenvalues.

Retained singular extrema, discarded-value bounds and retained condition bounds
follow by validated square roots. No full-Hankel spectrum follows.

## 5. Source-aware model tail, not exact encoded rank

PR195's validated generator gives each scalar waveform/encoding error at most
d_eval=L*2^-120+2^-49, with L=max_column sum_oscillatory |B_integer|.
L is recomputed from the pinned coefficient array. Hence

\[
 \|Z-Z_{\rm model}\|_2
 \le\sqrt{8191\cdot2294}\,d_{\rm eval}\|S_m\|_F=:\epsilon_m.
\]

Since rank(Z_model)<=209, Weyl gives sigma210(Z)<=epsilon_m. At width321,
epsilon_m<1.034e-10. Rounding can still give encoded Z a higher EXACT algebraic
rank; the theorem controls its tail, not that exact rank.

The certified205 values above the common cutoff at width321, together with
epsilon321 below that cutoff, prove rank(Z_model)>=205. Thus this return
places the comparison-model rank in[205,209], without proving its exact value.
The scaled rule instead certifies204 retained values for its larger cutoff.

## 6. Limits

These are source-aware finite constructor diagnostics. The PR195 stress
proposer's HOLD remains immutable; no new phase outputs are certified. The
nominal747-dimensional dynamical observer kernel is unchanged. Source/metric
selection, SI clocks, independent review and the full acquisition contract
remain open. O03 thresholds and seeds are protocol controls.
