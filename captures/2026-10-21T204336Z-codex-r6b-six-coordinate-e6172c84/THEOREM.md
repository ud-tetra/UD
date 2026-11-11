# R6b: six-coordinate ground sector and certified channel weights

**EXACT CONDITIONAL. Development — no registry entry.** Constructor: Codex. Reviewers: none. Physical promotion: 0. Applies to the rational clean L=4 R6b source equations and identity site metric; physical species, action units, and target-blind registration remain open. No recovered script was executed.

## Source and depth orbits

Source: `docs/hmulti_r6b.py` at base `4c264504f1ec8ce8965b097356d7193103c9382a`. Preserve eta=185/192, delta=7/192, a=eta^4, b=eta^6, and

\[
v_h=\delta(1-\eta^h),\quad
c_h=\eta^2\delta(1-\eta^h)(\eta^h-\eta^{2h}),\quad
r_h=4\eta^2+v_h.
\]

The unresolved 64-site module has first address digit zero. Its 16 sibling groups of four sites fall into three depth orbits, in order (h=4,h=3,h=2), with multiplicities n=(1,3,12). Write y_h for a Theta amplitude constant on every sibling group of depth h, and x_h for the corresponding rho amplitude multiplied by the source site parity. Fix the same coordinate scale in both channels.

The invariant six-coordinate matrix is

\[
K_6=\begin{pmatrix}R&C\\C&A\end{pmatrix},\quad
R=\operatorname{diag}(r_4,r_3,r_2),\quad
C=\operatorname{diag}(c_4,c_3,c_2),
\]

\[
A=\begin{pmatrix}
12a+48b&-12a&-48b\\
-4a&4a+48b&-48b\\
-4b&-12b&16b
\end{pmatrix}.
\]

This matrix uses unnormalized orbit amplitudes. Its inherited coordinate metric is proportional to

\[
G=\operatorname{diag}(1,3,12,1,3,12),\qquad GK_6=K_6^T G.
\]

The original 128-coordinate site metric remains the identity. The coordinate metric G is induced by the embedding, not an additional source choice. In orthonormal coordinates the matrix is G^(1/2) K6 G^(-1/2), which is symmetric. Treating K6 as symmetric in the ordinary six-coordinate Euclidean metric would give incorrect weights.

The verifier independently builds the source module H from exact rational edge contributions. With B the integer 128-by-6 embedding (rho entries source parity, Theta entries 1 on their depth orbit), it checks every entry of HB=BK6 and B^T B=4G. This establishes exact invariance, not merely agreement of a compressed Rayleigh matrix.

## Why this sector contains the unique negative eigenvalue

First retain separate amplitudes on all 16 sibling groups. The resulting 32-coordinate sector is invariant: rho group vectors are parity weighted and Theta group vectors are constant. Its rho block is diag(r_h), its coupling is diag(c_h), and its Theta block L has diagonal 12a+48b and off-diagonal -4a within a common 16-site block, -4b otherwise.

For group averaging projectors E4 and E16,

\[
L=64b(E_4-E_{16})+(16a+48b)(I-E_4).
\]

Its constant vector is the unique zero mode, and its positive gap is gamma=64b. Define M=max_h c_h^2/r_h. The verifier checks gamma>M>0. The zero-energy Schur complement L-C R^(-1)C is positive on the codimension-one subspace perpendicular to the constant vector, and negative on the constant vector itself. Interlacing gives exactly one negative eigenvalue and no zero eigenvalues in that sector.

On the orthogonal 96-coordinate complement, Theta has zero mean in each sibling group, giving stiffness g0=12a+48b; rho is bounded below by v_min. Its energy is at least

\[
\frac{v_{\min}}2\|x\|^2+
\left(g_0-\frac{2c_{\max}^2}{v_{\min}}\right)\|y\|^2.
\]

The verifier checks the second coefficient exceeds v_min/2>0. Thus the full module has exactly one negative eigenvalue. The six-coordinate sector has a negative Rayleigh vector by taking y constant and x=-R^(-1)Cy. Since it is invariant, it contains that unique negative eigenvalue and its full eigenvector. No assumption of spontaneous symmetry selection is needed.

These analytical implications require review. The constructor's exact arithmetic checks do not constitute non-constructor adversarial review or CRL-2b.

## Certified scalar root

For lambda<0, eliminate rho:

\[
x_h=-\frac{c_h}{r_h-\lambda}y_h,\qquad
S(\lambda)=A-\lambda I-
\operatorname{diag}\left(\frac{c_h^2}{r_h-\lambda}\right).
\]

The ground root satisfies det S(lambda)=0. There are no poles for lambda<0. The full-module uniqueness just proved and the invariant embedding imply exactly one negative root. The initial interval is [-M,0], verified with det S(-M)>0 and det S(0)<0. Exact rational bisection for 160 steps keeps those signs and produces a root interval narrower than 10^(-55). No solver tolerance or floating matrix enters the certificate.

A convenient broader exact enclosure is

\[
-0.000000016145247540177632
<\lambda<
-0.000000016145247540177631.
\]

The unrounded rational interval is in CERTIFICATE.json; its decimal display begins -1.61452475401776316314526313396009751832809430657e-8.

## Certified amplitudes, channel weights, and nonuniformity

Set y4=1. Solve the last two rows of S(lambda)y=0 for y3,y2 using their two-by-two determinant. Rational interval arithmetic over the certified lambda interval bounds that determinant strictly above zero and gives positive intervals for all three amplitudes. At the root the remaining row follows from det S=0 and that invertibility.

Readable amplitude approximations are

| Depth | Multiplicity | Theta amplitude relative to y4 |
|---|---:|---:|
| 4 | 1 | 1 |
| 3 | 3 | 0.9999999989912707175276463 |
| 2 | 12 | 0.9999999985275668269742396 |

Define T=sum_h n_h y_h^2 and Rho=sum_h n_h x_h^2. The normalized channel weights are

\[
W_\rho=\frac{\mathrm{Rho}}{\mathrm{Rho}+T},\qquad
W_\Theta=\frac{T}{\mathrm{Rho}+T}.
\]

A common embedding factor cancels in these ratios. The exact intervals imply

\[
4.3430663967222016\times10^{-9}<W_\rho<4.3430663967222018\times10^{-9},
\]

\[
0.99999999565693360<W_\Theta<0.99999999565693361.
\]

Their exact sum is 1 by definition. Separate enclosing intervals need not sum pointwise to exactly 1.

The within-module Theta diagnostic is F_Theta=16 sum_h n_h y_h^4/T^2. For stable certification use the identity

\[
F_\Theta-1=
\frac{\sum_{i<j}n_i n_j(y_i^2-y_j^2)^2}{T^2}.
\]

It avoids subtracting nearly equal quantities and proves the sharper positive enclosure

\[
5.7515757103508979\times10^{-19}
<F_\Theta-1<
5.7515757103508980\times10^{-19}.
\]

The verifier checks these broader printed enclosures against its exact intervals. The earlier upper bound approximately 2.21121963410e-18 from PR355 is respected. The floating replay's display of 1 was therefore consistent with a positive source-model departure below its resolving precision. This result does not certify the replay's IEEE matrix or conflate assembly error with eigensolver error.

## Receipt and remaining gates

`verify_certificate.py` is fresh standard-library code. Every numerical decision uses Fraction; outward rational quantization to a grid of 10^(-65) keeps certificate endpoints compact. Decimal strings are displays only. Run it directly to regenerate CERTIFICATE.json. The proof, source/governance hashes, event, and inventory are captured append-only.

This work re-derives directly from the lower-depth source equations; it does not promote a claim by citing PR354 or PR355. Per the attached CRL-2 amendment it stays in the development lane, with no registry entry. A non-constructor review remains necessary for any subsequent promotion.

Next useful audit: close the source-to-floating error budget for all four low modes using these exact reduced anchors, then assemble a single review packet. Particle operators and action-unit maps remain separate open dependencies. `Gap2_FINAL_Finite_Genesis.png` remains unavailable and was not used.
