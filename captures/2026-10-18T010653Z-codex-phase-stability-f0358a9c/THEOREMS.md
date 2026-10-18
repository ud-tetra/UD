# Finite-window phase stability around a pinned fitted reference

Development lane; physical promotion 0. Exact conditional matrix analysis plus
constructor computations. Independent review is pending. The reference phases
are learned from a numeric record; they are not nominal source modes, measured
physical truth, or a uniquely identified continuous generator.

## 1. Source model and validated constants

Let `n=8191`, `q=105` and `S=[W/64 | v/128]` be the pinned complementary sketch.
Let `Z0=D0 S` be the pinned clean record's sketch. The previous exact161-by-161
Gram certificate gives `sigma105(Z0)>=L0`. Let

\[
 M_{k,:}=\sum_{j=1}^{q}e^{ik\theta_j}C_{j,:},\quad
 \theta_j\in\{0,\pm\widehat\theta_1,\ldots,\pm\widehat\theta_{52}\}
\]

be the real modal model obtained from the pinned clean learned proposal after
applying the same sketch. The coefficient convention is the original stationary,
cosine and sine convention. The full complex representation is only a change
of basis. Every raw reading contributes to the exact integer sketch; no nominal
600-cell operator or nominal frequencies enter this calculation.

`certify_phase.py` computes an exact unweighted squared residual `F` between
the integer sketch and dyadic approximations to the modal phases. If `CA` is
the integer product of the proposed coefficients with `[2W|v]`, its entries
represent coefficients at scale2^-67. Every sine/cosine dyadic error is less
than2^-60. With `Cmax` the sum of the largest absolute `CA` coefficient in
each nonstationary row,

\[
 \|Z_0-M\|_2\le\|Z_0-M\|_F
 \le\varepsilon_0:=\sqrt F+
 \sqrt{8191\cdot161}\,C_{\max}/2^{127}.
\]

The resulting bound is about2.639e-11. It is a newly computed fit bound, not an
assumption that the quantized record has exact temporal rank105. Since `M` has
rank at most105, Weyl's inequality and
`alpha=L0-epsilon0>0` prove it has rank exactly105 and
`sigma105(M)>=alpha`.

Normalize the Vandermonde frame by `V[k,j]=exp(ik theta_j)/sqrt(n)` and set
`G=V* V`. Off-diagonal entries use the finite geometric sum. Exact interval
bounds and Gershgorin give `a I <= G <= b I`, with `a>0`.
For every pair of distinct reference eigenvalues, the chord separation obeys

\[
 |e^{i\theta_j}-e^{i\theta_l}|\ge s_{\min}>0.
\]

All constants are outward dyadic bounds in PHASE_STABILITY_CERTIFICATE.json.
The minimum reference chord separation is approximately0.00214408.

## 2. Conditional phase-matching theorem

Suppose a new record is `D0+E`, with each62-vector error at most `delta` across
37 preparations and8191 times. Its sketch is `Z=M+R`, where

\[
 \|R\|_2\le e:=\varepsilon_0+
 \sqrt{37\cdot8191\cdot371097/4096}\,\delta.
\]

Consider the **exact-arithmetic** estimator: take an orthonormal basis `U` of
the leading105 left singular vectors of `Z`, delete its last/first row to form
`U_-`, `U_+`, and calculate `T=U_-^dagger U_+` by exact least squares.
This theorem concerns that estimator. It is not an implementation-error proof
for the floating SVD/least-squares routine used in the proposer.

Define

\[
 K=\sqrt{b/a},\quad \beta=\sqrt{1-q/(na)},\quad
 t=e/(\alpha-e),\quad d=\sqrt{2-2\sqrt{1-t^2}},\quad
 r=\frac{K d(1+K)}{\beta-d}.
\]

If `alpha>2e` and `beta>d`, every eigenvalue of `T` lies within distance `r`
of some reference `exp(i theta_j)`. If also `2r<s_min`, these disks are
pairwise disjoint and there is exactly one eigenvalue in each disk, counting
multiplicity. When `r<1`, the corresponding circular phase error is at most
`arcsin(r)` radians per sample.

**Proof.** Put `Q=V G^-1/2`. Then `Q*Q=I` and
`Q_+=Q_- J`, where `J=G^1/2 diag(exp(i theta_j)) G^-1/2` has diagonalizer
condition at most `K` and norm at most `K`. Each row of `Q` has squared norm
at most `q/(na)`. Consequently `sigma_min(Q_-)>=beta`.

Projecting the leading left singular-vector equation for `Z=M+R` off the
column space of `M` gives
`||(I-QQ*)U||_2 <= e/sigma105(Z) <= e/(alpha-e)=t`.
The leading subspace is separated because `alpha>2e`. A unitary alignment of
`U` with `Q` has basis distance at most `d`. After that alignment,

\[
 \|U_+-U_-J\|_2\le d(1+K),\qquad
 \sigma_{\min}(U_-)\ge\beta-d.
\]

Least squares therefore bounds `||T-J||_2<=d(1+K)/(beta-d)`.
Diagonalizing `J` bounds every perturbed eigenvalue within the stated radius
(Bauer-Fike, directly by the diagonal resolvent/Neumann series). Along the
homotopy `J+x(T-J)`, `0<=x<=1`, the eigenvalues stay inside these disks.
If the full disks are disjoint, multiplicity cannot move between them, giving
one-to-one matching. A disk of radius `r<1` about a unit-circle point subtends
at most `arcsin(r)` from the origin. QED.

## 3. Certified grid boundary, not an algorithm-failure boundary

The dyadic grid was frozen as `delta=2^-k`, `k=20,...,40`, before execution.
The largest radius on this grid satisfying unique matching is `2^-27`.
There `r<0.000646029` and phase error `<0.000646029` radians per sample.
At the full `2^-20` vector budget the theorem gives only a one-sided enclosure:
`r<0.088763` and angular error to some reference phase `<0.088880`; the disks
overlap, so unique matching is not certified. This is a limitation of this
sufficient bound, not evidence that actual phase recovery fails there. It does
not establish that2^-27 is an optimal or necessary threshold.

The previous temporal-order theorem remains valid at2^-20. Stable component
count, retained conditioning, individual phase matching and convergence of a
particular numerical fitter are distinct claims.

## 4. Two fitting controls

Two new deterministic coherent phase-shift controls have declared vector-error
budgets2^-28 and2^-20. They shift the lower member of the closest positive
reference pair, using a source-bound coefficient L1 Lipschitz scale. A floating
constructor rounds the additive perturbations to encoded integers; exact
integer checks verify the actual vector/scalar error gates. Both remain known
constructor records, not independent apparatus or blinded data.

Returned phase numerators are compared exactly with the intended constructor
phase numerators. These differences are empirical parameter discrepancies;
the generated quantized record is not asserted to be exactly that modal model.
Passing a control does not close a general numerical-implementation or optimizer
convergence guarantee. One new full-record Hankel certificate separately tests
the higher-budget record against the unchanged selection criteria.

## 5. Two identifiability limits

**EXACT sampled aliasing.** For sampling interval `h=1/2` in normalized model
units, every continuous frequency `omega+4*pi*m` has the same sampled complex
phase as `omega`, for integer `m`. Even perfect sampled phase recovery cannot
select a unique continuous generator without an alias restriction.

**EXACT positive-noise obstruction.** For a nonzero one-mode amplitude vector
`a`, `||a cos((theta+eta)k)-a cos(theta k)||<=||a|| k |eta|`.
For any positive finite error budget there are distinct nearby phase models
whose finite records differ by less than twice that budget at every sample;
their error balls overlap. Thus exact real-valued phase identification is not
uniformly possible under positive bounded error. Approximate/local bounds such
as the theorem above remain meaningful.

No result here identifies unobservable bulk dynamics, promotes an experimental
bridge, supplies SI units, or changes the full-Hankel threshold/count/condition
cap. O03 tolerances remain protocol controls, not theory constants.
