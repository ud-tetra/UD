# Deterministic errors and decoder conformance for the weighted observer

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

## 1. Fixed map and typed constants

Use exactly PR307's map
\[
F=4096^{-1/2}\operatorname{stack}_{j=0}^{4095}R e^{t_jK},\qquad t_j=j/2.
\]
The unit Euclidean chain coordinates, epsilon=1/2 selected C10-orbit weights and62-coordinate readout are unchanged. The source is a real skew generator. The inherited, hash-pinned certificate gives rank1999, kernel dimension641, ||F||<=1 and
\[
s=61/27648<\sigma_{\min,+}(F),\qquad \|F^\dagger\|<C=27648/61.
\]
Let N=kerF, V=N-perpendicular and P=F-dagger F, the Euclidean orthogonal projection onto V. C is a bound derived from the numerical certificate, not a new theory constant. Time is internal model time, not calibrated SI time. All input norms and output norms below are Euclidean; time-stacked observations include the1/64 normalization.

## 2. A per-record deterministic envelope

For one fixed preparation x, suppose the actual records have the form
\[
\widetilde y_j=(R+E_j)e^{(t_j+\theta_j)(K+\Delta K)}(x+p_0)+n_j+c_j.
\]
Assume K+DeltaK is real skew, ||DeltaK||<=xi, ||E_j||<=rho_j, |theta_j|<=eta_j, ||x||<=X and ||p_0||<=p. The preparation error p_0 is fixed across this trajectory. The normalized noise and encoding errors satisfy
\[
\nu^2\ge M^{-1}\sum_j\|n_j\|^2,\qquad
\epsilon_{\rm enc}^2\ge M^{-1}\sum_j\|c_j\|^2.
\]
These are supplied deterministic bounds. No statistical independence, zero mean or source receipt is assumed merely from the notation.

Because ||K||<5 and both propagators are orthogonal,
\[
\|e^{(t_j+\theta_j)(K+\Delta K)}-e^{t_jK}\|
\le\min\{2,\ t_j\xi+(5+\xi)\eta_j\}.
\]
The first term follows by comparing K+DeltaK to K at t_j and then shifting along K+DeltaK by theta_j. It includes xi*eta_j. The cap2 follows from unitary/orthogonal norms.

Set
\[
b_j=\rho_j+\min\{2,t_j\xi+(5+\xi)\eta_j\},\quad
b=\sqrt{M^{-1}\sum_jb_j^2}.
\]
A convenient conservative bound is
\[
b\le\rho_{\rm rms}+T_{\rm rms}\xi+(5+\xi)\eta_{\rm rms}.
\]
With the same1/64 stacking convention, the actual data obey
\[
\boxed{\|\widetilde y-Fx\|\le D:=p+(X+p)b+\nu+\epsilon_{\rm enc}.}
\]
Indeed, split the difference into nominal propagation of p_0 and the actual/nominal map difference acting on x+p_0, then add noise and encoding. This retains the p*b term. Without a finite X, multiplicative map errors have no finite uniform absolute-data bound.

For time-varying preparation errors p_j, replace the preparation contribution by p_rms and the amplitude multiplier by X+p_max, with independently supplied p_rms and p_max. An RMS preparation bound alone does not justify replacing p_max in the product. Multiple preparations can be bounded separately; their Frobenius error is at most the square root of the sum of the squared deterministic envelopes. This is algebraic norm aggregation, not independent-error RSS cancellation.

## 3. Clock offset, scale and jitter

The exact finite moments are
\[
\mu=4095/4,\quad T_{\rm rms}^2=11180715/8<2048^2,
\quad v=(4096^2-1)/48.
\]
For theta_j=b0+a*t_j+zeta_j,
\[
\eta_{\rm rms}\le\sqrt{(b0+a\mu)^2+a^2v}+\zeta_{\rm rms}
\le |b0|+T_{\rm rms}|a|+\zeta_{\rm rms}.
\]
The first expression applies when signed offset and scale errors are specified; uncertainty in them requires its own interval/envelope. A dimensionless rate error a is amplified by the sample horizon. These bounds are not instrument timing receipts and do not convert model time to physical time.

## 4. Reconstruction and actual decoder conformance

The ideal nominal minimum-norm reconstruction x_star=F-dagger y_tilde satisfies
\[
\|x_\star-Px\|\le C D.
\]
The non-strict inequality includes D=0. It controls the observable component. Because x_star belongs to V,
\[
\|x_\star-x\|^2=\|x_\star-Px\|^2+\|(I-P)x\|^2.
\]
The641 hidden directions are not reconstructed. States x+h and x−h with h in N give identical nominal records; no deterministic decoder can uniformly recover both without an additional prior/source restriction.

For an actual linear decoder B, suppose independently verified certificates establish
\[
\|B\|\le\beta,\quad \|BF-P\|\le\alpha
\]
over the full2640-dimensional input space, and its numerical implementation returns x_hat=B*y_tilde+e_alg with ||e_alg||<=epsilon_alg on the declared input domain. Then
\[
\boxed{\|\widehat x-Px\|\le\alpha X+\beta D+\epsilon_{\rm alg}.}
\]
The input domain can be enclosed by ||y_tilde||<=X+D. This is a conformance requirement, not a consequence of conditioning. Checking only the prepared states, a forward fit, FB≈identity or BFQ≈Q does not establish BF≈P. An approximate decoder need not output V; the preceding full-state orthogonality identity applies to it only if its range is independently shown to lie in V.

A specific exact counterexample is F=[1,0], Q=(3/5,4/5)^T, K=J=0. Q has unit norm, E=0 and its trial Gram is9/25. The trial-coordinate right inverse B=Q/(FQ)=(1,4/3)^T satisfies FB=1 and BFQ=Q, but ||BF−P||=4/3. It adds a hidden component to a noiseless observable state. PR307's arbitrary-Q singular lower-bound proof remains valid; this example prevents silently upgrading it to an orthogonal decoder.

## 5. What small model error preserves

If the actual clocks, readout errors and generator define a fixed linear map F_tilde across input states, then ||F_tilde−F||<=b. For b<s,
\[
\sigma_{\min}(\widetilde F|_V)>s-b,\qquad
\kappa(\widetilde F|_V)\le(1+b)/(s-b).
\]
Also sigma_1999(F_tilde)>s−b, while any additional singular values are at most b. They may be positive. Thus small errors do not prove preservation of rank1999, the641-dimensional actual kernel, or full-positive-quotient conditioning. State-dependent error rules can still obey the per-record envelope, but are not automatically a fixed linear map with an SVD.

The exact control uses a three-time sampled planar rotation with a stationary third coordinate and readout R_epsilon=[1,0,epsilon]. Its normalized map is
\[
\frac1{\sqrt3}\begin{pmatrix}1&0&\epsilon\\0&1&\epsilon\\-1&0&\epsilon\end{pmatrix}.
\]
The nominal rank is2; any nonzero epsilon gives rank3, map perturbation norm|epsilon| and positive condition number greater than1/|epsilon|. At epsilon=2^-12 the perturbation is smaller than s, yet the full-positive condition exceeds4096. Nominal-subspace stability and full-kernel preservation are different claims. This is a logical control, not an asserted600-cell perturbation measurement.

## 6. Source gain for boundary-weight calibration

For weight errors supported only on the ten selected tetrahedra J, write DeltaD=diag(delta d_j) on J. The source incidence calculation checks
\[
B_J^T B_J=4I_{10}.
\]
Therefore the changed skew boundary-coupling block has the exact norm
\[
\|\Delta K\|=\|B_J\Delta D_J\|=2\max_{j\in J}|\delta d_j|.
\]
The checker reconstructs all100 selected Gram entries from the pinned oriented600-cell JSON. If weight errors instead affect all600 tetrahedra with max error u, the boundary row/column sums give ||B3||<=sqrt8 and hence ||DeltaK||<=sqrt8*u<=3u. Neither statement covers other simultaneous coupling errors unless separately included. Arbitrary per-tetrahedron errors need not preserve C10 symmetry.

Here delta d_j denotes an absolute change of a diagonal weight, not a relative error. For the nominal selected weight3/2, a relative error cap r first gives an absolute cap3r/2 and therefore xi<=3r. These are exact conditional calibration gains. No physical weight law or measured weight uncertainty is supplied. In the illustrative profile below, xi<=2^-66 could be implied by selected-weight error at most2^-67, but that premise itself remains unsupported.

## 7. An exact conditional precision example

For illustration only, declare X<=1 and the following upper bounds:

| Quantity | Declared bound | Evidence status |
|---|---:|---|
| Fixed preparation p | 2^-52 | UNSUPPLIED — HOLD |
| Generator error xi | 2^-66 | UNSUPPLIED — HOLD |
| Readout operator RMS rho | 2^-53 | UNSUPPLIED — HOLD |
| Clock RMS eta | 2^-56 in model time | UNSUPPLIED — HOLD |
| Normalized noise norm nu | 2^-53 | UNSUPPLIED — HOLD |
| Normalized encoding norm | 2^-53 | UNSUPPLIED — HOLD |
| Actual decoder defect alpha | 2^-42 | UNSUPPLIED — HOLD |
| Actual decoder gain beta | 512 | UNSUPPLIED — HOLD |
| Implementation error | 2^-42 | UNSUPPLIED — HOLD |

An optional clock envelope |b0|<=2^-58, |a|<=2^-70 and jitter_RMS<=2^-58 gives eta<=5*2^-59<2^-56. Fraction arithmetic verifies D<2^-50 and
\[
\alpha X+\beta D+\epsilon_{\rm alg}<2^{-40}<2^{-39}.
\]
This is a mathematical implication. It is not a measured accuracy certificate, an admitted acquisition or validation of an actual floating estimator. The target here is a declared observable-chain Euclidean error; it is not the earlier six-ratio q target, port-residual gate, shape gate or Hankel-family certificate.

For the ideal nominal inverse alone, a fresh combined data requirement for a declared target tau is D<=s*tau. At tau=2^-39 this is61/(27*2^49) in the normalized total-data norm. It is not a per-port threshold. Deterministic scalar errors bounded by u on each of62 coordinates give nu<=sqrt62*u<=8u, with no1/sqrt4096 improvement for coherent errors. An unnormalized stacked error must be divided by64 before using these formulas.

## 8. Checks, limits and next work

The standard-library checker reads pinned PR307 result/theorem files and one source-complex JSON member as data. It computes exact finite time moments, checks the source calibration gain and conditional budget, and records eight exact logical countermodels. A second run must produce four byte-identical scientific JSON files. No acquisition, noise campaign, decoder construction, floating-estimator call or new Hankel allocation occurs. Separate same-team review independently derives the bounds and arithmetic; it is not external promotion review.

The concrete remaining implementation task is to construct and verify a decoder against the orthogonal observable projection P, including full-domain BF−P and arithmetic error. Every illustrative input bound also needs independent source evidence before an actual run can be admitted. A condition number alone closes neither requirement.

Ledger v0.39 / CRL-2; Development — no registry entry. O03 controls are not theory constants. External promotion review PENDING; Physical Promotion=0. Full-session retraction ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused; please re-upload if needed. Notes/ASTER available but unused.
