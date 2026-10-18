# A posteriori validation of the actual floating phase estimator

Development lane; physical promotion 0. Constructor calculations with exact
integer/rational residuals and outward512-bit interval arithmetic. This certifies
captured outputs on pinned records about a pinned fitted reference, not physical
frequencies, global optimizer convergence or all possible error patterns.

## 1. What is captured and what remains untrusted

The instrumented proposer executes the original SVD, least-squares shift solve,
eigvals, angle calculation, phase rounding and coefficient fit without changing
those arithmetic expressions. After that calculation, it saves the actual
binary64 basis U (8191-by-105), shift T, returned complex eigenvalues lambda,
angles and auxiliary untrusted eigenvector/inverse/reduction proposals V, H, B.
Every generated PROPOSAL.npz must be byte-identical to its pinned parent.

All finite floating entries are converted with as_integer_ratio to exact dyadic
integers at a common power-of-two scale. There is no extra quantization of U or T.
The exact record sketch Z=X[2W|v]/2^55 is recomputed from all18,790,154 readings,
with signed-integer partial sums checked against overflow. Thus BLAS errors in
the proposer's floating sketch are included in the residual check below.
Both the floating witness and exact record sketch are retained for portable
verification without the full raw record or dense Hankel.

## 2. A computed subspace certificate without trusting SVD

Let M be the pinned fitted-reference sketch, and retain the previous certified
constants alpha<=sigma105(M), aI<=G<=bI for its normalized Vandermonde Gram,
K=sqrt(b/a), beta=sqrt(1-105/(8191a)), and minimum eigenvalue chord separation s.
The new verifier bounds e>=||Z-M||_2 by a newly computed exact Frobenius residual
plus its enclosed phase-rounding term. This is a measured finite-matrix fit
bound for the actual record, not a worst-case assumption about the whole error
ball.

Compute validated bounds

\[
 \eta\ge\|U^*U-I\|_2,\qquad
 p\ge\|Z-UB\|_2,\qquad b_B\ge\|B\|_2.
\]

Frobenius norms supply these operator-norm upper bounds. If eta<1, the polar
factor Q=U(U*U)^-1/2 is orthonormal and

\[
 d_U=\eta/(1+\sqrt{1-\eta})\ge\|U-Q\|_2,\quad
 \tau=p+d_Ub_B\ge\|(I-QQ^*)Z\|_2.
\]

Let Q0 be the reference model's orthonormal frame. Since M has rank105 with
sigma105(M)>=alpha,

\[
 t=(e+\tau)/\alpha\ge\|(I-QQ^*)Q_0\|_2.
\]

For t<1 there is a unitary basis alignment with

\[
 \|U O-Q_0\|_2\le d:=d_U+\sqrt{2-2\sqrt{1-t^2}}.
\]

No correctness or optimality of the floating SVD is assumed: its returned basis
must satisfy these data-bound residuals. Additionally alpha-e>cutoff>e certifies
exactly105 sketch values above the discovery cutoff on each tested record.

## 3. Validate the returned floating shift

The reference frame satisfies Q0_+=Q0_- J, with ||J||_2<=K and a diagonalizer
condition at most K. Its deleted-row singular value is at least beta.
Compute r_T>=||U_+-U_- T||_2 exactly from the captured floating matrices.
After unitary alignment, put x=||T'-J||_2. Then

\[
 \beta x\le r_T+d(1+\|T'\|_2)\le r_T+d(1+K+x).
\]

If d<beta, this gives

\[
 x\le\Delta_T:=\frac{r_T+d(1+K)}{\beta-d}.
\]

This step validates the actual floating shift matrix using its residual, rather
than replacing it by an ideal least-squares answer.

## 4. Validate the returned floating eigenvalues

The actual lambda values from eigvals are retained. Separate untrusted calls
supply paired right vectors V and an inverse witness H. Compute exact bounds

\[
 \rho\ge\|VH-I\|_2<1,\quad h\ge\|H\|_2,\quad
 r_\lambda\ge\|TV-V\operatorname{diag}(\lambda)\|_2.
\]

The first inequality proves V invertible and
`||V^-1||_2<=h/(1-rho)`. Therefore the exact matrix
A=V diag(lambda) V^-1 has exactly the captured lambda values as its eigenvalues,
and

\[
 \|A-T\|_2\le\Delta_\lambda:=r_\lambda h/(1-\rho).
\]

After the same unitary alignment, every eigenvalue of A lies within
`R=K(Delta_T+Delta_lambda)` of a reference exp(i theta_j). If 2R<s, the disks are
disjoint and each contains one captured eigenvalue, counting multiplicity. This
follows by the diagonal resolvent bound and the homotopy from J to A, as in the
previous conditional theorem. Inverse/eigenpair residuals close the floating
eigensolver step; its numerical eigenvalues are not accepted on trust.

## 5. Validate the actual emitted phases

For each selected positive angle, exact integer arithmetic checks that the
emitted theta numerator is the ties-to-even rounding of the captured angle times
2^60. Validated complex argument intervals then directly bound

\[
 \epsilon_{arg}\ge\max_j|
 \arg(\lambda_j)-\widehat\theta_j|.
\]

This accounts for the actual angle routine and emitted-grid error without
assuming an atan2 accuracy specification. When R<1, the output phase bound is

\[
 |\widehat\theta_j-\theta_{ref,j}|_{circle}
 \le\arcsin(R)+\epsilon_{arg}.
\]

The checker also requires twice this bound to be less than the reference chord
separation (a conservative sufficient condition for angular matching).
Only52 positive phases are emitted; their negatives and stationary0 form the105-mode model.
The reference phases are fitted parameters, not a source rule for a physical
generator. A small residual does not remove sampled-frequency aliasing.

## 6. Scope of the completed validation

The frozen campaign covers the clean record and both prior coherent controls.
For every accepted case, the actual regenerated proposal matches its parent
bytes, the exact record sketch and floating arrays are retained, and all residual
and matching gates pass. This supplies a posteriori validation of those floating
outputs. It does not certify convergence or acceptance on every future input,
unique matching throughout the entire2^-20 error ball, independent review,
physical measurements, full acquisition admission or hidden-state recovery.
The original full-Hankel criteria and nominal747-dimensional observer kernel are
unchanged. O03 tolerances remain protocol controls, not theory constants.
