# Validated conditioning of the frozen weighted observation map

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

## 1. Fixed object and result

Keep the PR305 model unchanged: epsilon=1/2 on the specified ten-tetrahedron C10 orbit; B3D with D=I+P_J/2; unit Euclidean chain coordinates; unchanged62-coordinate vertex-link restriction R. The signed generator K has upper adjacent blocks −B_k (−B3D at the top) and lower blocks their positive transposes. It is real skew. Define

\[
F=M^{-1/2}\begin{bmatrix}R\\Re^{hK}\\\vdots\\Re^{(M-1)hK}\end{bmatrix},
\qquad M=4096,\quad h=1/2.
\]

The exact PR305 rank1999/kernel641 is inherited and pinned by result/theorem hashes. No rank or model is changed. This note supplies a fresh conditioning certificate for this particular map and metric:

\[
\sigma_{\min,+}(F)>\frac{61}{27648}>\frac1{512},
\qquad
\kappa_+(F)<\frac{27648}{61}<512.
\]

The subscript+ restricts to the orthogonal complement of the641-dimensional kernel. The full2640-domain condition remains infinite. This improves the previous extremely loose analytic enclosure; it does not certify the numerical screen's estimate near180. The new bound does not transfer the distinct nominal Hankel2029 certificate, physical calibration, estimator, shape or noise gates.

## 2. Arbitrary trial columns and the exact dynamics residual

Let r=1999. The saved integer trial matrix Q_I has shape2640×r, with Q=2^-40 Q_I. Its columns need not lie exactly in the observable subspace. A real skew trial matrix J consists of one zero block and999 oscillator pairs,

\[
J_i=\begin{pmatrix}0&\omega_i\\-\omega_i&0\end{pmatrix},
\]

where the frequencies are saved dyadic rationals with denominator2^40. Repeated numerical frequencies were grouped only to construct this trial J. The actual K is unchanged, and every frequency or vector approximation enters the exact residual

\[
E=KQ-QJ.
\]

The proposed Q and frequency list were frozen before the validated run. Exact integer arithmetic verifies

\[
\|Q^TQ-I\|_F<1/16,\qquad \|E\|_F<2^{-24}.
\]

Consequently \(\|Q\|_2<9/8\). With the declared ordering, QJ is obtained by column swaps and frequency multiplication. Since2K is integer, E has common denominator2^80. The checker calculates its squared Frobenius norm as an integer over2^160. The sparse integer product (2K)Q_I is also exact in signed64-bit arithmetic: every absolute row sum of2K is at most24, each entry of Q_I is between−2^40 and2^40, so every partial sum is bounded by24·2^40, below signed64 capacity. Larger residual/Gram products use arbitrary-precision integers.

Put Y_j=RQ exp(jhJ) and Y=M^-1/2 stack(Y_j). Both exponentials are orthogonal. Variation of constants gives

\[
\|FQ-Y\|_2\le T_{\rm rms}\|E\|_2,
\quad T_{\rm rms}^2=\frac{(M-1)(2M-1)}{24}<2048^2.
\]

Thus \(\|FQ-Y\|_2<1/8192\). No sampled trajectory array is needed for this bound.

## 3. Full cross-channel Gram matrix

For one trial pair write a_i=R u_i and b_i=R v_i. Its output columns are

\[
a_i\cos(\omega_i t)-b_i\sin(\omega_i t),\qquad
a_i\sin(\omega_i t)+b_i\cos(\omega_i t).
\]

The zero block supplies only a_0; its dummy b_0 is zero. All inner products use the complete62-coordinate readout vectors. For any two frequencies define C_cc, C_ss, C_cs, C_sc as the normalized sums of cos-cos, sin-sin, cos-sin and sin-cos products over the4096 times. Let A_ij=a_i^T a_j, B_ij=a_i^T b_j and D_ij=b_i^T b_j. Every entry of G=Y^TY is included, including cross-channel terms:

\[
\begin{aligned}
G_{u_i u_j}&=A_{ij}C_{cc}-B_{ij}C_{cs}-B_{ji}C_{sc}+D_{ij}C_{ss},\\
G_{u_i v_j}&=A_{ij}C_{cs}+B_{ij}C_{cc}-B_{ji}C_{ss}-D_{ij}C_{sc},\\
G_{v_i v_j}&=A_{ij}C_{ss}+B_{ij}C_{sc}+B_{ji}C_{cs}+D_{ij}C_{cc}.
\end{aligned}
\]

The coefficients are exact dyadic dot products. Their common denominator is2^80, and each has absolute value at most2, as checked from the integers.

For a frequency difference or sum x, the complex normalized time sum is

\[
\Phi(x)=\frac1M\sum_{j=0}^{M-1}e^{ijx/2}
=e^{i(M-1)x/4}\frac{\sin(Mx/4)}{M\sin(x/4)}.
\]

At x=0 the checker uses the exact value1. All other needed arguments are evaluated with160-bit Arb balls. The four real kernels follow from product-to-sum identities. Each is enclosed by a dyadic midpoint of denominator2^60 with error strictly below2^-59. The saved120 distinct trial frequencies require14400 ordered kernel quadruples; their midpoint bytes and hashes are retained.

For each Gram entry, four coefficient/kernel products contribute error below4·2·2^-59. Rounding the resulting exact dyadic midpoint to denominator2^60 adds less than2^-60. Hence a symmetric integer midpoint G0 satisfies

\[
|(G-G_0)_{ij}|<17\,2^{-60},\qquad
\|G-G_0\|_2\le\|G-G_0\|_F<1999\cdot17\,2^{-60}<2^{-44}.
\]

No isolated-channel condition bound replaces this full matrix.

## 4. Saved eigenproposal and exact positive-definiteness certificate

A floating eigensolver proposes a square matrix V and a diagonal d for G0. Both are quantized and saved as exact integers: V=2^-40 V_I and d=2^-60 d_I. The floating eigenvalues and solver success are not acceptance evidence. Exact integer products must verify

\[
\|V^TV-I\|_F<1/16,\quad
\|G_0V-Vd\|_F<2^{-22},\quad
\min_i d_i>9\,2^{-20}.
\]

The verifier can read the frozen eigenproposal and perform all checks without invoking an eigensolver. Its eigen-residual has denominator2^100, so its squared norm is checked as an integer over2^200. V orthogonality uses an integer over2^160. The source equations, all midpoint entries and exact residual tests are replayed; no supplied PASS flag is trusted.

For completeness, if a symmetric G0, square V and diagonal d obey eta=||V^TV−I||<1 and beta=||G0V−Vd||, then

\[
\lambda_{\min}(G_0)\ge\min d-\frac{\beta}{\sqrt{1-\eta}}.
\]

Indeed, for a unit left eigenvector w of G0, \(w^T(G_0V-Vd)=w^TV(\lambda I-d)\), and \(\|w^TV\|\ge\sqrt{1-\eta}\). A Gram eigenvalue below min d is therefore at most beta/sqrt(1−eta) below it. Square invertibility is essential.

The certified bounds imply beta/sqrt(1−eta)<2^-21. Weyl's inequality then gives

\[
\lambda_{\min}(G)>9\,2^{-20}-2^{-21}-2^{-44}>2^{-17},
\qquad \sigma_{\min}(Y)>1/384.
\]

## 5. Full observable quotient, not only trial coordinates

The rank premise is essential. For rank(F)=r and an arbitrary2640×r trial matrix Q, the singular-product inequality gives

\[
\sigma_r(FQ)\le\|Q\|_2\sigma_r(F).
\]

Combine this with the validated Gram bound and the dynamics residual:

\[
\sigma_{\min,+}(F)
\ge\frac{\sigma_{\min}(Y)-\|FQ-Y\|_2}{\|Q\|_2}
>\frac{1/384-1/8192}{9/8}
=\frac{61}{27648}>1/512.
\]

Because R is a coordinate restriction and exp(tK) is orthogonal, ||F||<=1. The stated positive-quotient condition bound follows. Exact membership of Q in the observable subspace is not needed for this lower bound; it would be needed to turn a small-response trial vector into an upper bound for the smallest positive singular value. The proof does not infer any property of the641 hidden directions beyond the inherited rank/kernel result.

## 6. Verification, storage and epistemic scope

The main checker reconstructs the source signed K and readout R from pinned JSON data, verifies the inherited rank bindings, and reads the frozen dyadic Q and frequencies. Its optional proposer mode generates V,d; frozen-witness replay requires no eigensolver. All acceptance inequalities use integer matrix multiplication, exact rational comparisons and validated Arb time functions. Numerical screen results are identified as proposals only. The initial screen used the opposite global generator sign; the final trial upper-grade vectors were negated and the exact residual uses the intended source sign. This is recorded; global reversal preserves the complete-grid singular spectrum but is not silently treated as source equality.

The implementation reconstructs the1999×1999 Gram midpoint. It stores small matrices and compressed witnesses, and never allocates the253952-row sampled trajectory or the287-GiB Hankel matrix. The exact rank1999/kernel641 and model weights are unchanged. Fresh standalone conditioning is now certified for this map; PR305's practical-conditioning HOLD is extended only for this mathematical object. The distinct Hankel/preparation/321-column estimator, raw source/calibration and physical error gates remain HOLD.

No experimental data, instrument timing, physical weight law, or constitutive correspondence is supplied. The numerical trial search is disclosed and is not a blinded run. Separate same-team review is not external promotion authority. Ledger v0.39 and CRL-2 governance apply; O03 choices are controls, not theory constants. External promotion review PENDING; Physical Promotion=0. The session-wide retraction ratio is NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable and unused; please re-upload if needed. Notes/ASTER available but unused.
