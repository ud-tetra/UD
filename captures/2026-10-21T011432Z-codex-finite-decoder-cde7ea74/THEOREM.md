# A finite matrix-free decoder with the correct observable projection

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

## 1. Fixed object and what is closed

Keep the PR307 weighted4096 half-step observation map F, its Euclidean metric, readout and weights unchanged. Inherited pinned results give

\[
\operatorname{rank}F=1999,\quad\dim\ker F=641,\quad
\|F\|\le1,\quad\sigma_{\min,+}(F)>s=61/27648.
\]

Let V=(kerF)-perpendicular and let P be its orthogonal projection. PR309 required a decoder with a full-state bound on BF−P, rather than only a forward fit or a trial-frame inverse. This construction supplies such a finite linear decoder in exact operator arithmetic. It also bounds its implementation error under explicit absolute action-oracle and whole-update arithmetic contracts. The executable reference verifies those contracts on small rational control operators; the actual600-cell action implementation remains HOLD.

## 2. Polynomial construction

Set A=F^T F, a=s², c=(1+a)/2, d=(1−a)/2 and sigma=c/d. The positive spectrum of A lies in[a,1], and its kernel is kerF. Define

\[
p_N(\lambda)=\frac{T_N((c-\lambda)/d)}{T_N(\sigma)},\qquad
h_{N-1}(\lambda)=\frac{1-p_N(\lambda)}{\lambda},\qquad
B_N=h_{N-1}(A)F^T.
\]

Because p_N(0)=1, the apparent quotient is a polynomial. Its value at zero is generally nonzero:

\[
h_{N-1}(0)=\frac{N U_{N-1}(\sigma)}{d T_N(\sigma)}.
\]

The exact seed F^T y lies in V; therefore B_N has range in V. The construction does not need an explicit P or a numerically approximate observable frame. In particular, B_NF vanishes on every hidden state.

For q=(1−s)/(1+s)=27587/27709,

\[
\|B_NF-P\|\le2q^N=:\alpha_N,\qquad
\|B_N\|\le(1+\alpha_N)/s.
\]

This follows from |T_N(z)|<=1 on[-1,1], T_N(sigma)>=q^-N/2, and the singular decomposition of F. It is a whole2640-state operator bound, including the hidden directions, not a check on selected preparations.

Freeze N=8192 as an algorithmic control. An exact integer-power comparison proves

\[
2\,27587^{8192}2^{51}<27709^{8192},
\quad\alpha_N<2^{-51},\quad\|B_N\|<512.
\]

These constants are protocol bounds, not native clock periods or physical coefficients.

## 3. Matrix-free recurrence and exact zero start

Put g=F^T y. Start x0=0 exactly and x1=g/c. With rho0=d/c, use

\[
\rho_k=(2\sigma-\rho_{k-1})^{-1},
\]
\[
x_{k+1}=x_k+\rho_k\rho_{k-1}(x_k-x_{k-1})
+\frac{2\rho_k}{d}(g-Ax_k),\qquad k=1,\ldots,N-1.
\]

Chebyshev recurrence shows x_N=B_N y. This requires one adjoint action and8191 normal actions. If each normal action is composed as F^T(Fv), it needs16383 total forward/adjoint observation actions. Three iterate vectors, the fixed adjoint seed g, and current action results suffice, in addition to supplied input/oracle storage; no matrix F, A, P or full Hankel is stored by this recurrence. Its actual600-cell runtime has not been benchmarked.

The exact zero initialization is necessary. A preexisting hidden component has no observation residual that could remove it. The API deliberately supplies no arbitrary initial-state argument.

## 4. Full-space propagation of arithmetic errors

Let epsilon_j denote the aggregate additive defect introduced into update x_j, including initialization. It is one whole-vector update defect, not a bound on each primitive operation. Let Z=(cI−A)/d. The exact error propagation coefficient from update j to output N is

\[
\frac{T_j(\sigma)}{T_N(\sigma)}U_{N-j}(Z),\qquad 1\le j\le N.
\]

The full spectrum of Z is in[-1,sigma], including sigma>1 on the hidden space. Write sigma=cosh(theta). Since |U_l(z)|<=U_l(sigma) on this interval,

\[
\left\|\frac{T_j(\sigma)}{T_N(\sigma)}U_{N-j}(Z)\right\|
\le\frac{e^\theta}{\sinh\theta}
=G=\frac{(1+s)^2}{2s}=\frac{767788681}{3373056}<256.
\]

Consequently

\[
\|\widehat x_N-B_Ny\|\le G\sum_{j=1}^N\|\epsilon_j\|.
\]

This covers coherent errors and hidden-direction injections. It would be incorrect to use only the[-1,1] visible interval or to assume that every computed action/error stays in V. The nonzero value h(0) explains why an erroneous hidden component in the adjoint seed can be amplified.

## 5. Concrete absolute oracle and arithmetic obligations

Suppose ||y||<=2. For each actual call require:

| Obligation | Bound | Domain |
|---|---:|---|
| Adjoint seed delivery, g_tilde−F^T y | <=2^-67 | Normalized data ball2 |
| Normal action delivery, A_tilde(v)−Av | <=2^-67 | Every actual iterate in state ball2048 |
| Entire recurrence update arithmetic/coefficient defect | <=2^-67 | Current delivered dyadics and exact recurrence coefficients |

The action bounds are absolute, not relative and not unit-vector-only. They must describe the true fixed F, not PR307's approximate trial trajectories. Mathematical truth of an opaque callback is a caller obligation; the generic reference module cannot infer it from returned values.

The coefficients obey 1/c<2, 0<rho_k<1 and2rho_k/d<5. Initialization error is at most3u and each later local defect is at most11u for u=2^-67. With N=8192,

\[
\|\widehat x_N-B_Ny\|<N\,256\,11\,2^{-67}
=11\,2^{-46}<2^{-42}.
\]

Coefficient generation, multiplication, cancellation and final rounding must all be included in the single whole-update arithmetic defect.

The domain is self-consistent. For every ideal intermediate iterate, |p_k|<=1 gives ||B_k||<=2/s. Thus ||x_k||<=4/s for ||y||<=2, and

\[
4/s+2^{-42}<2048.
\]

Induction using the accumulated error bound keeps every computed iterate inside the action-oracle domain.

A sufficient factored oracle contract is forward error<=2^-68 on the state ball2048 and adjoint error<=2^-68 on the data ball2049. Since ||F||<=1, the computed forward output has norm<2049, and the composed normal-action error is at most2^-68+2^-68=2^-67. This requirement is not established for actual600-cell code in this capture.

## 6. Executable reference arithmetic

The reference represents delivered data and state vectors as exact integers times2^-96. Arb192 balls enclose the exact recurrence coefficients. Each coordinate evaluates the entire update expression using the current exact dyadics and enclosing coefficient balls, then certifies its rounded value differs from that expression by less than2^-80. For n<=2640,

\[
n\,2^{-160}<2^{-134},
\]

so the whole-vector arithmetic/coefficient defect is below2^-67. A wide or undecidable ball causes rejection. This validates the aggregate update; it does not assume one rounding-error bound per primitive.

The full decode(data,adjoint,normal) wrapper checks a normalized dyadic data norm<=2, invokes the adjoint once, and enforces the iterate-domain checks. The source of the callbacks and their truth/error contracts remain explicit obligations.

Three full8192-step controls use a four-state rotated rational observation operator with singular values{s,1/2,1,0}. The controls include weak-mode input, a rotated hidden direction with inconsistent observation data, and coherent oracle perturbations with hidden components. An exact Fraction audit checks each proxy action; the computed output is compared with the known minimum-norm target for the actual encoded input. Bad oracle delivery is rejected by that independent proxy audit, while the module itself rejects a wide arithmetic ball. The weak-mode control has minimum-norm state amplitude about453; it tests the generic data-ball2 decoder, not the separate illustrative state-X<=1 profile below. These are small controls, not a run of the actual2640-state600-cell decoder.

The standard-library certificate checker also verifies30 scalar recurrence/zero-mode identities at small degrees and the exact8192-degree power inequality. Separate review supplies additional independent recurrence/Green controls and its own full-step proxy execution.

## 7. Relation to the earlier conditional error profile

For the PR309 error envelope D and state cap X, the new algorithm gives

\[
\|\widehat x_N-Px\|
\le\alpha_NX+\|B_N\|D+\epsilon_{\rm impl}.
\]

Under the new action/update contracts, alpha_N<2^-51, ||B_N||<512 and epsilon_impl<11*2^-46. Substituting the earlier declared X<=1 and D<2^-50 gives

\[
\|\widehat x_N-Px\|<2^{-51}+512D+11\,2^{-46}<2^{-40}.
\]

Thus alpha and beta are derived for a specific decoder rather than postulated. Implementation accuracy still requires the source-bound action/update contracts, and every physical/input premise of the old profile remains UNSUPPLIED/HOLD. The target is observable-chain Euclidean error, not the older six-ratio q or Hankel-family estimator target. The641 hidden state components are not reconstructed.

## 8. Status and next implementation gap

Closed here: a finite matrix-free linear decoder with the correct nominal orthogonal projection, explicit gain and convergence bounds, full-space arithmetic-error propagation, and an executable reference with validated proxy arithmetic. Open: actual weighted600-cell F/F^T action implementation, absolute action-error certificates on the specified domains, full problem execution/performance, input/source evidence and physical acquisition. No full Hankel is allocated, and no actual600-cell floating decoder or physical experiment is claimed.

The earlier arbitrary-Q right-inverse counterexample remains valid. This decoder avoids it through the exact F^T seed and polynomial functional calculus; it does not declare the old trial frame an exact observable basis.

Ledger v0.39 / CRL-2; Development — no registry entry. O03 controls are not theory constants. External promotion review PENDING; Physical Promotion=0. Full-session retraction ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable and unused; please re-upload it if required. Notes/ASTER available but unused.
