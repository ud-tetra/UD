# A complementary finite observation for the fixed temporal sketch

Development lane; constructor proofs and executions. Physical promotion 0.
This is an engineering change to temporal discovery, not a new physical channel
or an independently reviewed bridge. Thresholds and sketch choices are O03
protocol controls; they are not derived physical constants.

## 1. Exact targeted kernel reduction

Use time-by-coordinate record `D[k,37c+a]`, with 8191 times and 2294 coordinates.
The existing sketch is `S=W/64`, where the pinned 2294-by-160 sign matrix has
rank160. The pinned null witness stores320 integer coordinates followed by1974
implicit zeros. Its exact identities are

\[
 v^T W=0,\qquad v^T v=16228.
\]

Add the computed column `g=v/128`, forming `S_+=[W/64 | v/128]`.
The first160 columns are unchanged. Because `g` is nonzero and orthogonal to
their span, `rank S_+=161` and

\[
 \ker S_+^T=\ker W^T\cap v^\perp,\quad
 \dim\ker W^T=2134,\quad \dim\ker S_+^T=2133.
\]

Thus this one-column augmentation removes exactly one sketch null direction.
It does not reduce the nominal dynamical observer's747-dimensional unobservable
subspace. It recombines existing readings and requires no additional physical
measurements.

For every old blind-family perturbation `E=(s/2^48) f v^T`,

\[
 ES_+=(s/2^{48})[0\mid (4057/32) f].
\]

Every nonzero member (`s!=0`, `f!=0`) is exposed algebraically. Exposure does not
mean its amplitude is above a detection threshold. In particular the bounded
impulse and alternating cases should remain below the discovery error floor.
The new kernel still supports other blind families. Any fixed sketch with
fewer than2294 columns has a nonzero nullspace, so this cannot be a universal
adversarial blindness repair.

## 2. Noise transfer and finite conditioning

The complement has squared norm `4057/4096`, so

\[
 \|S_+\|_F^2=371097/4096.
\]

If every one of303067 preparation/time62-vectors has Euclidean error at most
`delta=2^-20`, then the reshaped error matrix obeys

\[
 \|E\|_F\le\sqrt{37\cdot8191}\,\delta,\qquad
 \|ES_+\|_2\le\|E\|_F\|S_+\|_F\le N,
 \quad N^2=112467254499/4503599627370496.
\]

The frozen discovery cutoff is the outward100-bit dyadic upper bound on `2N`
written in SKETCH_RULE.json. No value is retuned after the controls run.
This is the temporal discovery cutoff, distinct from the full Hankel selection
threshold and from the source-defined shape gate.

Let the new exact-Gram certificate for the baseline give lower bound `L0` on
sigma105, upper bound `U0` on sigma1 and upper bound `T0` on sigma106.
Weyl's inequality gives, throughout the stated vector-error ball,

\[
 \sigma_{105}((D_0+E)S_+)\ge L_0-N,\quad
 \sigma_{106}((D_0+E)S_+)\le T_0+N,\quad
 \kappa_{105}\le(U_0+N)/(L_0-N).
\]

The exact interval comparisons verify `L0-N>cutoff>T0+N`. Therefore exactly105
singular values of this finite temporal sketch exceed the cutoff for every
perturbation in that ball, with the stored uniform condition bound.
This does not prove convergence of phase estimation, coefficient fitting,
continuous-generator uniqueness, exact algebraic rank105 or full acquisition
qualification. The declared vector-error ball is not the complete acquisition
contract.

## 3. Validated small-Gram spectral arithmetic

No dense Hankel is used. Set integer `A=[2W|v]`, integer raw data `X=2^48D` and
`Z=XA`. Every partial sum is bounded below signed-int64 overflow before the
integer multiplication. The exact sketch Gram is `G=Z^T Z/2^110` (161-by-161).
The stored Gram entries use decimal strings, not lossy binary64 integers.

Floating eigensolvers supply untrusted, dyadically quantized `Q,Lambda`.
The checker computes exact residual norms with outward interval arithmetic:
`eta>=||Q^TQ-I||_2`, `r>=||GQ-Q Lambda||_2`, `g>=||G||_2`.
If `eta<1`, put

\[
 s=\sqrt{1+\eta},\quad d=\eta/(1+\sqrt{1-\eta}),\quad
 \rho=g\eta+rs+\|\Lambda\|_2d(s+1).
\]

For the orthogonal polar factor `U` of `Q`, `||Q-U||_2<=d` and
`||G-U Lambda U^T||_2<=rho`. The latter follows by splitting
`G-Q Lambda Q^T=G(I-QQ^T)+(GQ-Q Lambda)Q^T` and bounding the polar replacement.
Every true ordered Gram eigenvalue is therefore within `rho` of its proposed
ordered value. Strict squared-cutoff comparisons classify all161 eigenvalues;
square roots yield the retained singular-value and condition bounds.
The portable replay checker rechecks the stored exact Grams and untrusted
factors; it does not silently trust a floating SVD.

## 4. Oversized alternating control

The intentionally out-of-budget alternating perturbation is a Nyquist term
`(-1)^k`. Adding the complement can expose this extra real temporal component.
A certified count106 is legitimate temporal behavior; it is incompatible with
this particular proposer's frozen model of one stationary mode plus conjugate
non-Nyquist pairs. Its resulting HOLD is model/order refusal, not evidence of a
physical fracture or a proof that the full record signature fails.

## 5. Resource and governance scope

The extra float64 trajectory column costs65528 bytes, with2568 extra bytes for
one161-by-161 versus160-by-160 float64 Gram (integer proof storage differs).
The column count rises by1/160=0.625%; the Frobenius noise envelope rises by less
than0.552%. All controls are existing known constructed records. Code and rules
were frozen before the new executions, but this is not independent or blinded
preregistration. The full spectral verifier, target1893 and cap2029 stay fixed;
a new full positive certificate tests one generated proposal separately.
Independent review and experimental/metrology obligations remain open.
