# Timing-source evaluation and actual-output phase validation

Development — no registry entry. Physical promotion 0; independent review pending.

## 1. Declared source and clocks

The pinned learned coefficient matrix B has shape 105-by-2294, stored as integer
numerators at scale 2^-60. Preparation a selects columns c*37+a. Its exact model
waveform is p(t)B_a, where p(t)=[1,cos(theta_j t),sin(theta_j t),...]. The pinned
52 positive theta_j are dyadics at scale 2^-60. This interpolation is declared;
it is not a consequence of integer samples alone or a physical source law.

For a=0,...,36 and k=0,...,8190, the frozen times are

\[
 t_{ak}=o_a+(1+(-1)^a\mu)k+(-1)^{a+k}j.
\]

There is one clock across all 62 channels within each preparation. Cross-
preparation errors are fully dependent, with explicitly fixed signs. Four
records use zero clocks, alternating quarter-sample origins, ramp origins with
small clocks, and the same ramp with larger clocks. Rational controls are in
CAMPAIGN_FREEZE.json. Their units are nominal sample-index units; O03 controls
remain protocol controls, not theory constants or SI specifications.

## 2. Certified fixed-point evaluation

Set Q=2^96. Validated Arb512 enclosures choose complex start, step and alternating
jitter factors whose real and imaginary component errors are each <=1/Q. The
complex norm of any anchor error is therefore less than e=2^-95. Multiplication
uses exact Python integers followed by ties-to-even rounding of each component
to Q; the complex rounding error is less than e.

Let z_k be the true unit phase at origin plus affine time and zhat_k the
recurrence. Its error E_k obeys

\[
 E_0<e,\qquad E_{k+1}<(1+e)E_k+2e,\qquad
 E_k<(2k+1)e(1+e)^k.
\]

For k<=8191, (1+e)^k<2: the binomial expansion is bounded by the geometric
series sum_m(ke)^m, and ke<1/2. Hence E_k<2(2k+1)e<2^-79. Multiplication by
one jitter factor, with one further exact rounded product, adds less than
(2+E_k)e. Rounding the resulting phase components to scale 2^-60 adds at most
2^-61. The total error in each sine/cosine component is strictly below 2^-60.
This is a finite recurrence bound. Tests include a full 8191-step endpoint.

The phase/coeff contraction uses exact integer matrix multiplication. Only the
resulting coordinate is rounded once to raw scale 2^-48. If
L=max_c sum_{r>0}|B_integer[r,c]|, then every encoded scalar has waveform error

\[
 |y_{akc}^{encoded}-[p(t_{ak})B_a]_c|
 \le L\,2^{-120}+2^{-49}=:d_{eval}.
\]

Thus each 62-vector has squared error <=62*d_eval^2. The integer L and rational
bounds are recorded in DATA_FREEZE.json. All raw layouts, ranges, byte counts
and SHA256 hashes are checked before fitting. A separate direct Arb512 audit
checks five frozen times per preparation and channel; it is a spot audit, while
the uniform bound follows from the recurrence proof. No old clean-fit residual
or future instrument-noise allowance is inherited. These are newly generated
modal-source records, not old raw samples at newly measured times.

## 3. What the unchanged output certificate proves

Preparation-specific constant origins rotate coefficient blocks and retain the
original temporal frame P(k), if excitation survives. Differential rates and
jitter generally leave that exact frame and can introduce additional modes.
The unchanged floating proposer learns its own temporal order from each raw
record. Orders outside 105 are retained with an explicit applicability HOLD;
no forced truncation or threshold adjustment is permitted.

For each applicable run, the uninstrumented and instrumented original proposals
must be byte-identical. The saved basis U, actual shift T, returned eigenvalues,
eigenvectors, inverse, angle outputs and emitted dyadic phases are retained.
An untrusted new reduction D is computed only to verify ||P-U D||. No reference
phases are supplied to the floating proposer. Reference phases are used by the
verifier to state and prove the comparison target.

PARENT_FRAME_THEOREMS.md gives the complete PR189 amplitude-independent proof.
The mathematical helper modules retain their published bytes. Exact binary64
encodings, integer residual Grams, validated frame constants, inverse/eigenpair
residuals, argument enclosures and ties-to-even emission checks enclose the
actual output, without assuming SVD/LS/eigensolver/atan2 accuracy.
A pass certifies bounded discrepancy of actual emitted phases from the original
fitted reference. It does not certify exact recovery of the clock-distorted
native components or general estimator convergence.

Every discovery/order, adapter or phase-proof HOLD is retained. A HOLD refuses
this sufficient proof attempt; it does not establish a failed physical model,
a true full-Hankel signature failure or a general failure of the estimator.

## 4. Scope

These are synthetic same-constructor executions, not blinded independent data,
independent review, SI calibration or a physical bridge. Phase certificates do
not prove full-Hankel retained count 1893, exact spatial rank, future acquisition
admission, continuous-generator uniqueness or hidden-state recovery. No dense
Hankel matrix is allocated. The nominal 747-dimensional observer kernel is not
altered. Independent replay/review and physical source/metric mapping remain
separate requirements. Physical promotion stays 0.
