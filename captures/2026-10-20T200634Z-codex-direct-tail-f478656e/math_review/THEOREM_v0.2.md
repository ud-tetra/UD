# Right-tail minmax certificate and retained-proof reanchor: independent proof V2

Development — no registry entry. Physical Promotion = 0. External promotion review PENDING. This proof and its scalar implementation are frozen before the new tail norms are supplied.

Let Z be real m by n with m>=n, and fix 1<=k<=n. Put d=n-k+1. Let Vd be any real n by d matrix for which an actual operator bound

\[
\|V_d^TV_d-I_d\|_2\le\eta<1
\]

is certified, with eta>=0. Let W=ZVd and G=W^TW. Assume a nonnegative rational r is proved to satisfy

\[
r^4\ge\sum_{i,j=1}^{d}G_{ij}^{\,2}.
\]

Then

\[
\sigma_k(Z)\le\frac{\|ZV_d\|_2}{\sqrt{1-\eta}}
\le\frac{r}{\sqrt{1-\eta}}
\le\frac{r}{1-\eta}=t_{\rm new}.
\]

Here k=210, n=321, and d=112. The numerical square-root/fourth-root enclosures must round upward. Gram and W norms in this theorem refer to exact saved real dyadic matrices, not finite-field arithmetic.

## Proof and hypotheses

The Gram bound implies ||Vd c||>=sqrt(1-eta)||c|| for every coefficient vector c. Therefore Vd is injective and its range is a d-dimensional subspace of the right input space. On this subspace,

\[
\max_{x\in\operatorname{range}(V_d),\ x\ne0}
\frac{\|Zx\|_2}{\|x\|_2}
\le\frac{\|ZV_d\|_2}{\sqrt{1-\eta}}.
\]

The Courant–Fischer singular-value variational identity is

\[
\sigma_k(Z)=\min_{\dim L=n-k+1}\max_{x\in L\setminus\{0\}}
\frac{\|Zx\|_2}{\|x\|_2}.
\]

Choosing L=range(Vd) gives the **upper** bound. A poor choice of L can yield a loose upper bound; it does not turn this minimization into a lower bound. The dimension d and injectivity premise are essential.

Since G=W^TW is an exact positive semidefinite Gram matrix,

\[
\|W\|_2^4=\|G\|_2^2\le\|G\|_F^2=\sum_{ij}G_{ij}^2\le r^4.
\]

All terms are nonnegative, so ||W||<=r. Finally 0<1-eta<=1 implies sqrt(1-eta)>=1-eta; the stated rational relaxation follows. No orthogonality or other relation between Vd and the retained right columns is required. No assumption that range(Vd) is an exact singular subspace is required.

If the saved n proposals are descending and nonnegative, then for every j>=k both 0<=sigma_j(Z)<=tnew and 0<=sj<=sk. Hence

\[
|\sigma_j(Z)-s_j|\le\max(t_{\rm new},s_k).
\]

The maximum suffices because the two compared numbers are nonnegative. If a retained certificate bounds |sigma_j(Z)-sj|<=epsilon for j<k, the full n-list absolute-error bound is

\[
E_{\rm full}=\max(\epsilon,t_{\rm new},s_k).
\]

If this maximum is strictly below2^-41, the complete321 saved ordered proposal list meets that accuracy bound for the specific tuple. This is not all-input backend conformance. In combination with a retained actual sigma209 lower above the original cutoff and tnew below that cutoff, it certifies exactly209 actual singular values above the cutoff, with no cutoff equality. This remains a cutoff count rather than an algebraic rank claim. The original lower proposal-floor consequence remains inherited from the retained two-sided certificate and original source lower premise.

## Counterexamples and arithmetic traps

1. **A denominator cannot be omitted.** Z=diag(3,2), Vd=(0,1/2)^T has eta=3/4 and ||ZVd||=1, but sigma2(Z)=2. The exact denominator sqrt(1-eta)=1/2 restores the bound; r/(1-eta)=4 is conservative.
2. **The actual Gram bound is essential.** A zero column has W=0 but does not span a one-dimensional subspace. Its Gram defect is1, so eta<1 cannot legitimately hold. Supplying a falsely small eta cannot certify a tail.
3. **Dimension matters.** For Z=diag(3,1), a single column e2 yields maxgain1, but cannot certify sigma1=3: the sigma1 minmax requires dimension2. In the application the112-column shape and eta<1 together supply the required112-dimensional subspace.
4. **The minmax direction matters.** For Z=diag(3,1), Vd=e1 is an admissible one-dimensional subspace. It gives sigma2<=3, whereas sigma2>=3 would be false. Its overlap with a retained e1 is irrelevant to validity of the upper bound.
5. **Fourth-root powers matter.** For scalar W=1/2, G=1/4 and sum(Gij^2)=1/16. The correct fourth root is1/2. Taking just its square root gives1/4 and is an unsafe norm bound. A wrapper for eta requires a square test; a wrapper for ||W|| from the Gram-square sum requires a fourth-power test.

The exact norm calculations require the supplied G and Vd-Gram difference to be the stated matrix products. A distinct all-entry deterministic CRT audit is planned to establish those identities; checking a norm sum or hash alone does not establish them. Projection N is reused from the prior frozen computation and hash-matched to the original accepted projection. No fresh raw/projection reconstruction is independently claimed in this turn. The saved retained Gram/forward/adjoint norm premises remain inherited from PR286. In active V2 the retained matching proof is re-evaluated against the new direct tail, as follows; the old nominal/source tail is not needed for the current singular-accuracy or cutoff proof. No refit, independent physical acquisition, hardware calibration, exact spectrum of the saved shift operator, or physical six-ratio result follows.


## V2: reanchor retained ordering to the direct tail

Let inherited actual saved retained norm bounds be a,b,f,g, with a,b in [0,1) and f,g nonnegative. Recompute the separate-polar block quantities

\[
c=\frac{s_1[a/(2-a)+b/(2-b)]+f}{1-b},\quad
e=\max\left(\frac{f}{1-b},\frac{g}{1-a}\right),\quad
\epsilon=c+e.
\]

The existing proof establishes a compression C with ||C-S||<=c and off-diagonal block norm <=e. Reapply its index-match step with the newly proved tnew: if sq-c>tnew+e, Weyl gives sigma_(q+1)(diag(C,D))<=tnew+e. All q singular values of C exceed that threshold, so ||D||<=tnew+e<sigma_q(C). Thus the leading q block is C and the same retained bound |sigma_j(Z)-sj|<=epsilon follows. The ambient leading condition bound is (s1+epsilon)/(sq-epsilon), with positive denominator because the strict match implies sq-epsilon>tnew>=0.

Combining this retained proof with the new direct discarded proof yields the full321 bound max(epsilon,tnew,s210). Neither the previous nominal/source sigma210 upper nor the previous source sigma209 lower is a premise of this current full321 accuracy theorem or cutoff count. The actual cutoff count follows directly from tnew<tau<sq-epsilon. The recomputed c, e, epsilon and condition may match prior arithmetic exactly while the matching gap changes; identical numerical values do not mean identical proof dependencies.

If the original source lower L is supplied, saved sq can separately be compared to the fixed original protocol floor L-2^-41. L is a protocol-threshold provenance dependency for that comparison only. It is not needed for the current singular-accuracy or actual-cutoff proof. Earlier full-factor, frame, phase, target and physical-source claims are not prerequisites for this finite real singular-value argument. This reanchor does not rederive a,b,f,g and does not establish all-history backend completeness.

V1 proof/code/freezes are preserved; V2 is a dependency-strengthening extension, not a correction of a mathematical error.
