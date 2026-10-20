# Two-residual retained-spectrum theorem: independent proof

Development — no registry entry. Physical Promotion = 0. External promotion review PENDING. This proof is frozen before the new adjoint residual values are supplied.

Let Z be real m by n, m >= n, 1 <= q < n. Let saved factors U and V have shapes m by q and n by q, and S=diag(s1,...,sq) with descending positive entries. Assume actual operator-norm enclosures

\[
\|U^TU-I\|\le a<1,\quad \|V^TV-I\|\le b<1,
\quad \|ZV-US\|\le f,\quad\|Z^TU-VS\|\le g,
\]

where a,b,f,g are nonnegative. Also assume a separately established actual tail enclosure sigma_(q+1)(Z)<=t, with t>=0. Gram and residual upper bounds may be certified using Frobenius bounds. Byte hashes alone do not prove these norm statements.

Define the exact rational enclosures

\[
p=s_1\left(\frac{a}{2-a}+\frac{b}{2-b}\right),\quad
c=\frac{p+f}{1-b},\quad
e=\max\left(\frac{f}{1-b},\frac{g}{1-a}\right),\quad
\epsilon=c+e.
\]

If the strict matching condition

\[
s_q-c>t+e
\]

holds, then for each j=1,...,q,

\[
|\sigma_j(Z)-s_j|\le\epsilon.
\]

In addition sigma_q(Z)>=sq-epsilon>0 and the **ambient leading-spectrum** condition number satisfies

\[
\frac{\sigma_1(Z)}{\sigma_q(Z)}
\le\frac{s_1+\epsilon}{s_q-\epsilon}.
\]

This is an ambient bound, unlike the preceding partial-factor restriction bound. It does not assert conditioning of the entire matrix, an exact rank-q factorization, or absence of smaller nonzero singular values.

## Proof

Set A=U^TU, B=V^TV and QL=UA^(-1/2), QR=VB^(-1/2). The Gram assumptions make A,B positive definite, so QL and QR have orthonormal columns. Their column spaces are the same as those of the saved factors. Let C=QL^T Z QR.

For 0<=x<1, spectral calculus gives

\[
\|A^{1/2}-I\|\le\frac{a}{2-a},\quad
\|B^{-1/2}\|\le\frac1{1-b},\quad
\|B^{-1/2}-I\|\le\frac{b}{(1-b)(2-b)}.
\]

Indeed the largest square-root deviation is at most 1-sqrt(1-a)=a/(1+sqrt(1-a))<=a/(2-a). The largest inverse-square-root deviation is at most b/[sqrt(1-b)(1+sqrt(1-b))], with denominator at least (1-b)(2-b). These statements hold for Gram eigenvalues on either side of1; no commutation of S with A or B is assumed.

Writing E=ZV-US gives

\[
C=A^{1/2}S B^{-1/2}+Q_L^T E B^{-1/2}.
\]

Expand the difference from S as (A^(1/2)-I) S B^(-1/2)+S(B^(-1/2)-I)+QL^T E B^(-1/2). The triangle inequality and ||S||=s1 imply ||C-S||<=c. Therefore sigma_q(C)>=sq-c and |sigma_j(C)-sj|<=c, by singular-value perturbation.

Complete QL and QR to orthogonal bases. In these bases Z has the block form

\[
\widetilde Z=\begin{pmatrix}C&X\\Y&D\end{pmatrix}.
\]

The forward equation implies ||Y||<=f/sqrt(1-b)<=f/(1-b), because the orthogonal projection perpendicular to QL annihilates U. Applying the same argument to Z^TU-VS gives ||X||<=g/sqrt(1-a)<=g/(1-a). Thus

\[
\left\|\begin{pmatrix}0&X\\Y&0\end{pmatrix}\right\|
=\max(\|X\|,\|Y\|)\le e.
\]

The equality follows by squaring the norm: the adjoint product is block diagonal with blocks Y^TY and X^TX. It remains valid for rectangular off-diagonal blocks. Let Z0=diag(C,D); its singular values are the union of those of C and D. Orthogonal changes of coordinates do not change singular values. Weyl's inequality gives

\[
\sigma_{q+1}(Z_0)\le\sigma_{q+1}(Z)+e\le t+e.
\]

Every one of C's q singular values is strictly above t+e by the matching condition. If ||D|| were above t+e, Z0 would have at least q+1 singular values above that threshold, a contradiction. Hence ||D||<=t+e<sigma_q(C). The q leading singular values of Z0 are consequently exactly those of C, with descending order preserved. A second application of Weyl, followed by ||C-S||<=c, yields |sigma_j(Z)-sj|<=e+c for all j<=q. The matching condition also implies sq-epsilon>t>=0, justifying the condition-number division.

## Remaining ordered proposals and cutoff

Suppose the complete saved singular list has n descending nonnegative entries and next proposal s_(q+1). For j>q, both 0<=sigma_j(Z)<=t and 0<=sj<=s_(q+1). Consequently

\[
|\sigma_j(Z)-s_j|\le\max(t,s_{q+1}),\qquad
\max_{1\le j\le n}|\sigma_j(Z)-s_j|
\le\max(\epsilon,t,s_{q+1}).
\]

The maximum, not the sum, suffices because both compared scalars are nonnegative. Thus retained accuracy at2^-41 does not imply full-list accuracy at2^-41 when the inherited actual-tail bound is larger. No tighter original noise radius may be substituted to make this conclusion pass.

If the original source cutoff tau satisfies t<tau<sq-epsilon, exactly q actual singular values exceed tau, with no equality. This is a cutoff count, not algebraic rank. A retained error <=2^-41 also yields sq>=sigma_q(Z)-2^-41, hence the original proposed-floor consequence from any inherited actual sigma_q lower. It does not certify every other numerical gate or all-history backend conformance.

## Necessary qualifications and countermodels

1. The adjoint residual cannot be discarded. For Z=[[1,3/4],[0,0]], U=V=e1, S=[1], both Grams and forward residual are exact, and the actual tail is zero. The adjoint residual is3/4, while actual sigma1=5/4. A zero forward residual alone does not establish zero ordered error.
2. The tail/matching step cannot be discarded. Z=diag(1,2), U=V=e1, S=[1] has both residuals and both Gram defects zero, but actual leading singular value2. Its actual sigma2 is1, so sq-c=t+e and strict matching correctly fails. Without an upper-tail premise or index-match condition, the retained factor may represent a lower singular subspace.
3. Retained accuracy does not imply tail accuracy. Z=diag(1,2^-30), U=V=e1, S=[1] has exact retained factors and residuals. A saved next proposal zero differs from the actual tail by2^-30>2^-41, despite exact retained accuracy and correct cutoff count at2^-24.

These are exact logical examples, not actual saved records or an actual backend bug. All finite numerical consequences remain conditional on the norm/source premises actually being established for the particular saved tuple. The theorem does not close global backend obligations or authorize physical promotion.
