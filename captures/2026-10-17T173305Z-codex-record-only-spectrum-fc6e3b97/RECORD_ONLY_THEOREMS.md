# Record-only Hankel extraction: verified development result

Lane: **development — no registry entry**. Physical promotion: **0**. Independent review: **pending**. This is a benchmark on previously seen, constructed nominal data. It is not a blinded apparatus run or a CRL promotion.

## Inputs and distinction from the previous benchmark

The previous nominal benchmark used the known 600-cell frequencies and modal blocks. The present learner and verifier receive **only** the complete encoded record, frozen contract, and an untrusted proposal learned from that record. They do not load the cell operator, preparation vectors, annihilator, spectral roots, prior modal blocks or character projectors.

The proposal family is a stationary term plus real oscillatory pairs. This is a modeling choice for the numerical optimizer; the final proof does **not** assume the record was produced by that family. It checks the approximation against every reading. A failed proposal returns HOLD or produces no acceptance certificate.

Discovery cutoffs, sketch width and seed are protocol controls under ledger O03, not UD coefficients. They are fixed in this version's code; the frozen target count, selection threshold and condition cap are unchanged. This new implementation does not retrospectively satisfy the original contract's requirement for an independently reviewed, pre-data analysis freeze.

## Theorem 1: full-record residual bound

Let `Y[a,k,c]` be the integer record, with quantum `2^-48`, and

\[
H_{(i,c),(j,a)}=\frac{Y[a,i+j,c]}{M2^{48}},\quad M=4096.
\]

A proposed real temporal model has dyadic coefficients `C_l,c,a` and phases `theta_j`. The verifier evaluates every phase directly with 512-bit interval arithmetic. If `P_kl` are its dyadic phase numerators, scale `2^-60`, and coefficient numerators have the same scale, define

\[
D_{k,c,a}=2^{72}Y[a,k,c]-\sum_l P_{kl}C_{l,c,a},
\quad w_k=\min(k+1,2M-1-k,M).
\]

The dyadic model's Hankel residual is exactly

\[
\epsilon_D^2=\frac{\sum_{k,c,a} w_kD_{k,c,a}^{2}}{M^2 2^{240}}.
\]

If every nonconstant phase has error less than `2^-60`, the difference between this dyadic model and the exact trigonometric model is at most

\[
\epsilon_P\leq\sqrt{62\cdot37}\,2^{-120}
\sum_{l>0}\max_{c,a}|C_{l,c,a}|.
\]

Thus `||H-H_model||F <= epsilon_D+epsilon_P`. This is a finite numeric-record statement; it does not use a continuous generator, excitation assumption or nominal spectral decomposition.

## Theorem 2: retained spectrum and complete projection tail

Factor each fitted complex observation block as `L_j R_j*`, allowing an enclosed truncation residual. Let `epsilon_B` be the Frobenius norm of the block-diagonal residual over all signed modes. If the temporal Gram has norm at most `b`, the resulting rank-r factorization satisfies

\[
\|H-\widetilde H\|_F\leq\delta
=\epsilon_D+\epsilon_P+b\epsilon_B.
\]

Construct both actual r-by-r factor Grams from dyadic inner products and enclosed geometric sums. Certified Cholesky residuals normalize the factors to near-isometries. Exact small-core SVD residuals and polar corrections enclose its singular values; frame distortions enclose those of `H_tilde`. Weyl then expands the retained intervals by `±delta` and gives

\[
\sigma_{r+1}(H)\leq\delta,\qquad
\|H(I-P_{\mathrm{range}(F_R)})\|_F\leq\delta.
\]

If the certified rth lower bound exceeds the frozen threshold, `delta` lies below that threshold, and the certified ratio of largest to smallest retained singular values is below 2029, the numeric record has exactly **1893 singular values above the frozen threshold**. This does not assert that its exact algebraic rank equals 1893: integer quantization or small perturbations may add nonzero singular values below the threshold.

The bounds apply only to the frozen finite sample window; future prediction is not certified. The proof needs no dense Hankel array. It also does not require a small floating-point energy difference to resolve the tail. Exact full-record energy is retained as a separate check.

## Theorem 3: complete full-size perturbation controls

Changing the central reading `[a=0,k=M-1,c=0]` by amplitude `u` adds an M-by-M anti-diagonal block inside the full Hankel operator. Its M nonzero singular values are all `|u|/M` and its Frobenius norm is `|u|/sqrt(M)`.

For `u=2^-20`, this norm is exactly **2^-26**. Applying Weyl to the verified base bounds certifies the same frozen numeric signature. This is a single-vector perturbation control, not a calibration receipt.

For `u=1`, rank-r perturbation inequalities imply that at least `M-r=2203` singular values exceed `1/M-delta` when `r=1893`. This exceeds the frozen threshold and proves an actual rank-signature breach, rather than just an inconclusive tail estimate. Both complete modified records are scanned to verify the one-entry difference. The learner is not rerun for these perturbation certificates.

## Theorem 4: a conditional stability radius from the actual certificate

Write `l,u,tau` for the certified rth lower bound, largest upper bound and tail bound, `T` for the exact frozen threshold and `K=2029`. The numeric signature is preserved for every perturbation `E` satisfying

\[
\|E\|_2<\rho=\min\left(T-\tau,\ l-T,\frac{Kl-u}{K+1}\right).
\]

The source ceiling `B=9093197064441289377/1208925819614629174706176` lies strictly inside this radius. Conditional on `||E||2<=B`, the actual record certificate gives **condition <754.162**, with 1893 values above the frozen threshold. This is a perturbation theorem, not verification that an apparatus satisfies B.

Separately, if each complete 62-vector changes by at most `delta=2^-20` in Euclidean norm, the triangular Hankel weights sum to `M²` per preparation, giving `||E||F<=sqrt(37)·delta`. The retained condition bound then stays below **742.718**, and the Frobenius projection-tail bound follows as well. An operator-norm bound alone does not provide this Frobenius-tail claim.

## No-go: samples do not uniquely identify the continuous generator

On a real rotation plane, sampled evolutions with angular frequencies `omega` and `omega+2*pi*n/h` coincide at every integer multiple of sampling interval `h`. A record-only spectral certificate therefore cannot choose a unique continuous skew generator without an independently justified frequency range or other source information. Nor can it infer a global 747-dimensional unobservable subspace from one collection of sampled preparations. The earlier kernel theorem remains confined to the specified nominal operator and observer.

## Lossless replay input

The package stores a learned codec dictionary plus **every integer residual** needed to restore the original 150,321,232-byte record. These residuals are not omitted, smoothed or thresholded. The restored payload must match the original SHA-256 before processing. The learner then receives only the restored raw record and contract; the codec dictionary is not passed to the learner or verifier as a spectral hypothesis.

## Review and limitations

All verification here is by the constructor. The attached CRL-2 amendment is a governance proposal; its non-constructor review requirement has not been satisfied by these checks. No registry entry or physical promotion is claimed.

The numerical proposer has a finite resource envelope: at most 160 sketched temporal columns, stationary-plus-oscillatory frames, and conservative rank/range checks. It may HOLD on valid but noisier or more complicated records. Successful certification of this benchmark does not guarantee successful proposal generation for every admissible acquisition. The generic dense-candidate method remains available as a separate, unbenchmarked alternative.

The 62 history outputs remain distinct from 189 diagnostic outputs and additional six-ratio ports. This work does not re-certify six-ratio calibration, the source-defined shape statistic, apparatus error receipts or physical clock units.
