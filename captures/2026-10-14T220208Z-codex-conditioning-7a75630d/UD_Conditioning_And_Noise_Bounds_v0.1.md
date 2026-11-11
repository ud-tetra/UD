---
title: "Unified Dynamics: conditioning and noise bounds"
subtitle: "From exact gluing observability to finite-precision reconstruction"
author: "Benjamin Walker Mayes"
date: "14 October 2026 - Development derivation 0.1"
---

Development lane; no registry entry. Constructor derivation; independent review pending. Physical promotion: 0.

# 1. Declared readout and its conditioning

Use the copied-state generator $A^T=-A$ and normalized gluing observation $Q$, with $QQ^T=I_m$, from the stacked-family theorem. The copied state has $n$ real coordinates. Declare an observation scale $\tau>0$ and

\[
y=M_\tau x+e,\qquad M_\tau=\begin{pmatrix}Q\\\tau QA\end{pmatrix},
\quad e=\begin{pmatrix}e_0\\\tau e_1\end{pmatrix}.
\]

Here $e_1$ is raw derivative error; its acquisition is not assumed free. The scale makes the two blocks commensurate in the chosen model units. It is not a new dynamical coefficient or a physical clock calibration. Assume full column rank when reconstructing the complete state.

Define

\[
H_\tau=M_\tau^TM_\tau=P+\tau^2A^TPA,
\quad P=Q^TQ,
\quad\gamma_\tau=\sqrt{\lambda_{\min}(H_\tau)}>0.
\]

The absolute noise gain is $1/\gamma_\tau$. The relative matrix condition number is $\kappa_2(M_\tau)=\sigma_{\max}(M_\tau)/\gamma_\tau$. These are different quantities.

**Theorem C1 (sharp deterministic error).** The least-squares reconstruction $\widehat x=M_\tau^\dagger y$ satisfies

\[
\boxed{\|\widehat x-x\|\le
\frac{\sqrt{\epsilon_0^2+\tau^2\epsilon_1^2}}{\gamma_\tau}}
\quad\text{if }\|e_0\|\le\epsilon_0,\ \|e_1\|\le\epsilon_1.
\]

As a bound in the combined error norm $\|e\|$, the factor $1/\gamma_\tau$ is attained by error along a least singular left vector. Separate block budgets need not attain this combined bound simultaneously.

**Proof.** Full rank gives $M_\tau^\dagger M_\tau=I$. Hence $\widehat x-x=M_\tau^\dagger e$, and the pseudoinverse norm is $1/\gamma_\tau$. A singular-vector error attains the norm. This is standard SVD-based least-squares conditioning, specialized to the declared observation.

If $M_\tau$ is rank deficient, no finite bound recovers arbitrary full states even at zero noise. The pseudoinverse recovers only the projection onto its row space. That space need not equal the full time-observable subspace when higher derivatives are required.

# 2. Generator uncertainty and usable certificates

Let $\bar A$ be the reconstruction model, $\|A-\bar A\|\le\delta$, with the same exact $Q$. Set $\bar M_\tau=(Q;\tau Q\bar A)$ and $\bar\gamma_\tau=\sigma_{\min}(\bar M_\tau)$. For $\|x\|\le R$,

\[
\boxed{\|\bar M_\tau^\dagger y-x\|\le
\frac{\sqrt{\epsilon_0^2+\tau^2\epsilon_1^2}+\tau\delta R}
{\bar\gamma_\tau}.}
\]

This assumes $\bar\gamma_\tau>0$. It owns model mismatch separately from measurement noise. Since $\|M_\tau-\bar M_\tau\|\le\tau\delta$, minimization over unit vectors gives

\[
|\gamma_\tau-\bar\gamma_\tau|\le\tau\delta.
\]

Thus a certified true lower bound $\gamma_\tau\ge\Gamma$ guarantees reconstruction-model injectivity when $\tau\delta<\Gamma$, with denominator at least $\Gamma-\tau\delta$.

**Proof.** Write $y=\bar M_\tau x+e+(M_\tau-\bar M_\tau)x$ and apply C1. The singular-value inequality follows from $\|\bar Mv\|\ge\|Mv\|-\|(\bar M-M)v\|$ for unit $v$, and then interchange the matrices. No small-error expansion is used.

For exact rational $H_\tau$, a rational LDL factorization of $H_\tau-qI$ with positive pivots certifies $\gamma_\tau>\sqrt q$. Floating eigenvalues may suggest $q$ but do not certify it. A general, usually conservative, bound is

\[
\gamma_\tau\ge
\frac{\sqrt{\det H_\tau}}{(1+\tau^2\|A\|^2)^{(n-1)/2}},
\]

because every Gram eigenvalue is at most $1+\tau^2\|A\|^2$. Positivity of the determinant is available only after full rank is established. Unknown errors in $Q$ require an additional observation-model term and are not included in $\delta$.

# 3. Gaussian noise, correlations and representation invariance

Assume the complete error $e$ is zero-mean Gaussian with known positive-definite covariance $\Sigma$, independent of the unknown fixed state. The generalized least-squares estimate and information matrix are

\[
\widehat x=I_\Sigma^{-1}M_\tau^T\Sigma^{-1}y,
\qquad I_\Sigma=M_\tau^T\Sigma^{-1}M_\tau.
\]

**Theorem C2 (exact covariance and confidence region).** Under full column rank and the exact measurement model,

\[
\operatorname{Cov}(\widehat x-x)=I_\Sigma^{-1},\qquad
\mathbb E\|\widehat x-x\|^2=\operatorname{tr}(I_\Sigma^{-1}),
\]

\[
\Pr\!\left[(\widehat x-x)^TI_\Sigma(\widehat x-x)
\le\chi^2_{n,1-\alpha}\right]=1-\alpha.
\]

In particular, a Euclidean confidence radius is

\[
\|\widehat x-x\|\le
\sqrt{\chi^2_{n,1-\alpha}/\lambda_{\min}(I_\Sigma)}.
\]

**Proof.** The estimator error is the displayed linear map applied to $e$. Multiplying its covariance gives $I_\Sigma^{-1}$. Whiten this $n$-dimensional Gaussian error to obtain the chi-square statement. The radius follows from the smallest information eigenvalue. Gaussianity is needed for this exact coverage, not for the covariance identity. Bias, covariance estimation and non-Gaussian tails need separate bounds.

For equal-prior alternatives separated by $\Delta x$ under the same covariance, the exact optimal decision error is

\[
P_e=\Phi\!\left(-\tfrac12\sqrt{\Delta x^TI_\Sigma\Delta x}\right)
\le\Phi\!\left(-\tfrac12\sqrt{\lambda_{\min}(I_\Sigma)}\|\Delta x\|\right).
\]

This follows by the likelihood-ratio projection onto $\Sigma^{-1}M_\tau\Delta x$. It is distinguishability of the readout distributions, not information already written into a retained physical memory.

For an invertible output rescaling $S$, transport all three objects:

\[
y\mapsto Sy,\quad M\mapsto SM,\quad
\Sigma\mapsto S\Sigma S^T.
\]

Then $I_\Sigma$ is unchanged. Increasing $\tau$ on paper cannot improve statistical information while leaving the raw noise physics fixed. An unweighted singular value can change under this rescaling; a consistent whitened calculation cannot. Correlated observations require the full covariance, including cross-block terms.

# 4. Derivative acquisition from three snapshots

Observe $y_-,y_0,y_+$ at $s_0-h,s_0,s_0+h$, with $h>0$ and $s_0\ge h$. Prepare the state and retain its history under the same constant generator throughout. Define

\[
D_h=\frac{y_+-y_-}{2h}.
\]

If each endpoint has norm error at most $\epsilon$, $\|A\|\le L$ and $\|x(s_0)\|\le R$, then

\[
\boxed{\|D_h-QAx(s_0)\|
\le\frac\epsilon h+\frac{L^3Rh^2}{6}.}
\]

**Proof.** Endpoint errors contribute at most $2\epsilon/(2h)$. The third derivative of $Qx$ is $QA^3x$, whose norm is at most $L^3R$ by skew-flow norm preservation. The centered Taylor remainder gives the second term. No noiseless derivative is assumed.

Finite precision and timing fit the same budget. Suppose each $m$-coordinate snapshot has additional detector error at most $\epsilon_{\rm det}$, componentwise rounding to nearest with step $q$ and no saturation, and timestamp error at most $j$. Its total deterministic error is at most

\[
\epsilon_{\rm eff}=\epsilon_{\rm det}+\frac{\sqrt m\,q}{2}+LRj.
\]

The rounding vector has at most $q/2$ in each component, and integrating $\|Qx'\|\le LR$ over the timing offset gives the last term. Use the appropriate effective budget for each center/endpoint in C1 and the difference formula. Correlated or stochastic timing errors are not thereby independent Gaussian noise.

Substitute this derivative error into C1. For this conservative derivative-approximation bound alone, the unconstrained minimizing step is

\[
h_*=(3\epsilon/(L^3R))^{1/3},
\]

when $L,R,\epsilon>0$. Actual latency or admissible-time restrictions may exclude it. This is a minimum of the bound, not a universal sampling optimum.

For independent endpoint Gaussian errors with covariance $\sigma^2I_m$, derivative-noise covariance is $\sigma^2I_m/(2h^2)$. With an independent center snapshot of the same noise, the cross covariance with $y_0$ is zero. The derivative mean-square error obeys

\[
\mathbb E\|D_h-QAx\|^2\le
\frac{m\sigma^2}{2h^2}+\frac{L^6R^2h^4}{36}.
\]

Its unconstrained bound-minimizing step satisfies $h_*^6=9m\sigma^2/(L^6R^2)$. Shared temporal noise changes these formulas. A three-snapshot acquisition uses $3m$ scalar readout channels over a span $2h$, plus clock alignment, bandwidth and storage resources; this is not a complete energy cost.

# 5. Exact canonical sampling avoids truncation bias

For the canonical independent-copy generator, $A^3=-4A$. Consequently

\[
\frac{e^{hA}-e^{-hA}}{2h}
=f(h)A,\qquad f(h)=\frac{\sin(2h)}{2h}.
\]

This can be used as the exact measurement matrix rather than approximating the derivative. The retained statistic $(y_0,D_h)$ has

\[
M_h=\begin{pmatrix}Q\\f(h)QA\end{pmatrix},\qquad
\Sigma_h=\sigma^2\operatorname{diag}(I_m,I_m/(2h^2))
\]

under the independent equal-noise three-snapshot contract. Its information matrix is exactly

\[
\boxed{I_h=\sigma^{-2}
\left[P+\frac{\sin^2(2h)}2A^TPA\right].}
\]

Thus $h=\pi/4$ maximizes this information matrix in Loewner order over $0<h<\pi/2$. It is a model-unit optimum for this retained statistic under fixed snapshot noise; it is not an optimum over every sensor, time budget or the full three-snapshot record. The symmetric endpoint sum has been discarded. At $h=k\pi/2$, $k\ne0$, the derivative statistic loses its active signal, so this two-block readout is rank deficient for a nontrivial stack.

**Proof.** On harmonic modes both sides of the first identity vanish; on every active mode $A$ has frequency 2, giving the sine factor. The covariance inverse contributes $2h^2/\sigma^2$, which cancels the factor $1/(4h^2)$ in $f(h)^2$. The remaining coefficient is maximized when $\sin^2(2h)=1$. At its zeros, only the snapshot remains. Calibrating the exact matrix removes Taylor bias, not noise amplification or acquisition cost.

# 6. Exact two-cell and five-cell conditioning

The following values concern independent copied dynamics and the normalized union observation, with $\tau=1/2$ and canonical weights. They are not the native union-generator frequencies. All copied generators have norm 2.

| Configuration | $n$ | $m$ | Minimum Gram eigenvalue | Absolute error gain $1/\gamma$ |
|:--|--:|--:|:--|:--|
| Two cells, shared face | 30 | 23 | $1-\sqrt3/2$ | $1+\sqrt3\approx2.73205$ |
| Five-cell core-star | 75 | 47 | $1-\sqrt{15}/4$ | $\sqrt2(\sqrt5+\sqrt3)\approx5.61177$ |
| Five-cell chain | 75 | 47 | Smallest root of $64z^4-256z^3+280z^2-48z+1$ | Approximately 6.43292 |

For the chain, exact LDL and Sturm checks place the minimum Gram eigenvalue in $(241/10000,243/10000)$. Hence an entirely rational certificate gives error gain below $100/\sqrt{241}$. The decimal estimate is more precise but is not itself the certificate. All three maximum Gram eigenvalues are 2, so their relative condition numbers are $\sqrt2$ times the listed absolute gains.

**Proof for two cells.** The exact Gram polynomial factors as

\[
\frac{(z-2)^{14}(z-1)(4z-7)(4z^2-8z+1)^7}{2^{16}}.
\]

Its smallest root is $1-\sqrt3/2=((\sqrt3-1)/2)^2$. Inverting its square root gives $1+\sqrt3$. The star's exact factorization, stored in the certificate, has its smallest root in $16z^2-32z+1$. All its other factor roots are at least this value. For the chain, the full characteristic polynomial's square-free part has exactly one root in the certified interval and none between zero and its lower endpoint; that root belongs to the displayed quartic. These statements are checked in exact arithmetic.

For the same combined output error budget 0.01, worst-case state errors are at most approximately 0.02732, 0.05612 and 0.06433 respectively. These are worst-direction readout comparisons. They do not establish universal architecture superiority or equal physical expenditure.

# 7. Exact recoverability has no uniform robustness guarantee

Even keeping the copied-generator norm equal to 2 does not give a positive uniform $\gamma$ over all nonzero weights. In the two-cell example set $a=b=1$, $c=\varepsilon>0$ in each cell. Let $v$ be the unit difference of their shared-face coordinates. Then

\[
Qv=0,\qquad\|QAv\|=\varepsilon,
\qquad\gamma_\tau\le\tau\varepsilon.
\]

Therefore the snapshot/derivative noise gain is at least $1/(\tau\varepsilon)$ and diverges as $\varepsilon\downarrow0$, although exact rank remains full for every positive $\varepsilon$. The other channels keep $\|A\|=2$. At $c=0$ a higher derivative can restore time observability, so this is specifically a failure of uniform robustness of the declared two-block readout, not a theorem that all possible observation histories fail.

For full-state reconstruction on the closed five-cell boundary, the two-block matrix has a 20-dimensional kernel even before noise. Restricting to its certified observable subspace permits positive singular-value bounds there; adding a finite noise budget cannot identify the discarded directions.

# 8. Scope, verification and references

The pseudoinverse, whitening and Gaussian arguments are standard statistical linear algebra. The specialized results here are their application to the declared gluing observation, its exact spectra, the fixed-norm degenerating family and the exact canonical sampling contract. Constructor replay supplies exact characteristic-polynomial/LDL/Sturm certificates plus separately labelled floating fixtures. It does not estimate a physical noise covariance, establish independent review, certify measured bandwidth or prove a physical entropy-area relation.

Primary background: LAPACK *Users' Guide*, [Linear Least Squares Problems](https://www.netlib.org/lapack/lug/node27.html), and [How to Measure Errors](https://www.netlib.org/lapack/lug/node75.html). General perturbation literature includes G. W. Stewart, [On the Perturbation of Pseudo-Inverses, Projections and Linear Least Squares Problems](https://doi.org/10.1137/1019104); only its abstract/metadata were inspected, so no specific theorem from its paywalled text is invoked here. The displayed bounds have self-contained proofs.

Next requirements for operational use are calibrated joint covariance, acquisition and clock-error models, admissible sampling windows, generator uncertainty and a complete resource ledger. The derivation closes a mathematical conditioning gap while leaving those physical inputs explicit.
