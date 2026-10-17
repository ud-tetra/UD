# UD noise versus retained-signal frontier v0.1

RESULT / STATUS: DERIVED, conditional, constructor checked. Development — no registry entry. Physical promotion **0**; independent review pending. No experimental data were evaluated.

The original 62-channel vertex-link observer and the frozen 37 preparations yield a conservative, reproducible noise-versus-signal-count staircase. It separates noise in the long observation record from the much tighter error budget of the proposed calibration/diagnostic experiment. It does not reduce the original 747-dimensional dynamical unobservable space.

## Decision table

The following are **guaranteed minimum counts**, including the model-error bounds conditional on a pass of the recommended restricted-family validator, its shape gate and continued validity during acquisition. The additive error δ bounds the Euclidean norm of each complete 62-vector, for every preparation and timestamp. It is not a per-scalar RMS, a stochastic standard deviation or a calibration-ratio error.

| Axis samples M | Raw vectors per preparation | Scalar readings | δ = 2^-20 | δ = 2^-18 | δ = 2^-16 | δ = 2^-14 | δ = 2^-12 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2,048 | 4,095 | 9,393,930 | 1,833 | 1,519 | 519 | 75 | 0 |
| 4,096 | 8,191 | 18,790,154 | 1,893 | 1,833 | 1,519 | 589 | 111 |
| 8,192 | 16,383 | 37,582,602 | 1,893 | 1,833 | 1,579 | 965 | 163 |

Zero here means this bound certifies no retained signal, not that the true matrix vanishes. A count below 1,893 is a sufficient guarantee, not an exact truncation rank or a proof that other signals were erased.

The full-1,893 sufficient noise ceilings are shown below. The JSON preserves 512-bit interval enclosures; these decimals are display summaries. Operate below an outward-lowered boundary rather than using a rounded-up decimal as a gate.

| M | Output error only | Parent model budget | Restricted-pass model budget |
|---:|---:|---:|---:|
| 2,048 | 6.1609086 × 10^-7 | 2.6750613 × 10^-7 | 4.5239854 × 10^-7 |
| 4,096 | 2.7651891 × 10^-6 | 2.1525576 × 10^-6 | 2.4843578 × 10^-6 |
| 8,192 | 3.8397382 × 10^-6 | 2.6808191 × 10^-6 | 3.3210952 × 10^-6 |

A simple dyadic operating point is **M = 4,096, δ ≤ 2^-20**. It certifies exactly 1,893 singular values above the declared noise threshold, with a retained condition-number upper bound below **2,029**. The looser δ ≤ 2^-19 also retains 1,893, with condition bound below **2,246**. `ACQUISITION_CHOICES.json` records these and three smaller-count options with exact gates. A sufficient deterministic scalar-output error ceiling is δ/8, since sqrt(62) < 8; the first option can therefore use 2^-23 per scalar. These are proposed operating contracts, not apparatus receipts. Choosing either does not establish that the model-family or preparation assumptions hold.

## Frozen observation and inherited facts

Use the real 2,640-dimensional unique-simplex chain carrier, its skew Hodge–Dirac generator A, the original coordinate selector R with 62 channels, and X with 37 columns. The columns of X are the frozen ±1/52 preparation vectors, each with norm squared 165/169. The sampled normalized Hankel matrix is

\[
H_M[(i,c),(j,a)]=\frac1M [R e^{q(i+j)A/2}X_a]_c,
\quad i,j=0,\ldots,M-1.
\]

Thus H has 62M rows, 37M columns and uses 2M−1 distinct time vectors per preparation. Its normalized time horizon is M−1. The constant common scale q belongs to [1023/1024,1025/1024]; fitted raw times and coordinates require the previously specified transfer. The time indices here are sample indices, not finite-field Frobenius iterations.

The parent certificate supplies 53 nonnegative squared-frequency blocks: one stationary block and 52 positive-frequency blocks. Each positive block represents a conjugate pair. Their 105 signed temporal frequencies excite rank 1,893. For each block b, the parent supplies rank r_b and bounds

\[
0<\ell_b\le\sigma_j(B_b)^2\le u_b,
\qquad B_\lambda=R E_\lambda X,
\]

for every nonzero block singular value. These are block extrema; individual singular values were not stored. This turn does not rerun those modal diagonalizations. It copies the source certificate, records its hash, rounds every lower bound down and upper bound up to exact dyadics with denominator 2^160, and checks the new conclusions against those inputs. Source-bound constructor checks are not independent verification of the inherited modal proof.

## The finite-sample retention theorem

Let C = 1828864/1021 < 1792 be the inherited reciprocal-sine bound valid uniformly for the constant common-rate family. For M > C, the temporal Gram eigenvalues lie between 1−C/M and 1+C/M. This uses the parent Gershgorin argument with the explicit C/M value, sharpening its coarser three-window allowances.

Set a_M = 1−C/M and b_M = 1+C/M. The exact factorization is

\[
H_M=(V_M\otimes I_{62})D(V_M^T\otimes I_{37}),
\qquad D=\operatorname{diag}_\lambda B_\lambda.
\]

The transpose on the right is intentional. It has the same singular values as V_M. Both outer factors have singular values in [sqrt(a_M),sqrt(b_M)] on their full column/row spaces. Consequently, for every ordered nonzero singular value,

\[
a_M\sigma_j(D)\le\sigma_j(H_M)\le b_M\sigma_j(D).
\]

Proof: the upper bound is the singular-value product inequality. Apply the same inequality to D = L^+ H_M Q^+, where L and Q are the full-column and full-row outer factors, to obtain the lower bound. Their inverse norms are at most a_M^-1/2. The complex factorization certifies the real H_M singular values; conjugate blocks count twice in real dimension.

Suppose the full observation/model perturbation obeys ||ΔH|| ≤ β. Define

\[
d_M(\beta)=\sum_{b:\ a_M^2\ell_b\ge16\beta^2}m_b r_b,
\qquad m_0=1,\quad m_b=2\ (b>0).
\]

Weyl's inequality gives at least d_M observed singular values at least 3β, hence strictly above the threshold 2β for β > 0. Singular values arising from the nominal zero tail are at most β. Weak genuine signals can also exceed 2β, so d_M is normally a lower bound, not an exact observed rank. The certificate also records the rigorous upper bound

\[
\#\{\sigma_j(H_M+\Delta H)>2\beta\}
\le\sum_{b:\ b_M^2u_b>\beta^2}m_b r_b.
\]

If d_M = 1,893, these bounds agree and the threshold selects exactly 1,893 signals. For d_M > 0, let s_d be the smallest admitted a_M sqrt(ell_b). Then

\[
\kappa_{d_M}(H_M+\Delta H)
\le\frac{b_M\sqrt{\max_b u_b}+\beta}{s_d-\beta}.
\]

This bounds the conditioning of the leading retained singular spectrum; it does not identify individual eigenmodes, resolve C10 character sectors or certify subspace angles. Blocks here are temporal-frequency blocks, not the ten character sectors.

## Adversarial output error and model drift

With error norm ≤ δ in every raw 62-vector, every preparation and timestamp, the Hankel Frobenius bound yields ||ΔH|| ≤ sqrt(37) δ. Increasing M gives no generic averaging gain: constant, aligned errors at all timestamps attain this bound. The six checks include that coherent example.

For the fitted-model contract, write G = Htilde^-1(qA+ΔA+J), with metric error η, native-rate error r and extra skew error σ. The inherited operator estimate is

\[
e=\frac{4r+\sigma+4q_+\eta}{1-\eta},\qquad
g=\sqrt{\frac{1+\eta}{1-\eta}},\quad q_+=1025/1024.
\]

Let α = sqrt(165/169), preparation error p, readout error ρ, and combined origin/jitter allowance τ. A uniform vector-error envelope is u_0+δ+vt, where

\[
u_0=g[(1+\rho)p+\rho\alpha+\alpha(4q_++e)\tau],
\qquad v=g\alpha e.
\]

The exact Hankel time moments, accounting for antidiagonal duplication, are

\[
\mu_1=(M-1)/2,\qquad
\mu_2=(7M^2-12M+5)/24.
\]

Therefore

\[
\beta_M^2\le37[(u_0+\delta)^2+2(u_0+\delta)v\mu_1+v^2\mu_2].
\]

The three reported scenarios are:

- Output error only: u_0 = v = 0.
- Parent model: p = ρ = 2^-25, τ = 2^-28, η = r = σ = 2^-35. δ replaces the parent's additive-output budget; at δ = 2^-26 the new calculation reproduces all three parent Hankel error bounds.
- Restricted-pass model: p = 2^-25 and τ = 2^-28 remain separate acquisition requirements; η, r and ρ use outward-rounded tighter bounds in the latest precision/work certificate. J = 0 is a restriction of that fault family, not something inferred for arbitrary generators. These bounds require the proposed diagnostic pass, the measured shape gate, family membership, corrected coordinates and stability throughout acquisition. No such empirical pass is asserted here.

For a block minimum ell, solving the sufficient inequality β_M ≤ a_M sqrt(ell)/4 gives the scalar boundary

\[
\delta_*=
\sqrt{\frac{a_M^2\ell}{592}-\frac{v^2(M^2-1)}{24}}
-u_0-\frac{v(M-1)}2,
\]

when the radicand and result are positive. The smallest block ell gives the full-1,893 ceiling. The JSON stores all per-block boundaries, and the CSV stores 207 exact dyadic grid evaluations across three windows and three budgets. The figure uses display-only floating conversions. Stair steps between grid points are conservative, not exact physical transition locations.

Longer windows improve temporal separation but accumulate model drift. The certificate compares only the stated three M values; it claims neither global sample optimality nor monotone improvement for arbitrarily long acquisition.

## What this changes

The new result quantifies an experimental scope tradeoff: a larger allowed observation error can still certify a smaller signal count. The nominal dynamical unobservable space remains 747-dimensional. No alignment map reconstructs it in this calculation. Finite-field arithmetic, Frobenius order, irrational-frequency physical clocks and modular orthogonality are outside this real observation certificate.

The recommended validator's per-coded-response ceiling 2^-58 and its six-ratio target 2^-39 remain separate. Allowing δ near 10^-6 for the later history acquisition does not relax either calibration requirement. Relaxing those requirements for a smaller retained count would need a new propagation proof.

These tolerance values are protocol controls under O03. There are no measured noise receipts, independent review or physical promotion. Failure of a gate rejects its declared contract; it does not diagnose microscopic phase leakage.

## Verification and next step

Run `python certify_noise.py`, `python -m unittest -v test_noise.py`, and `python validate_noise.py`. Plot with `python plot_noise.py`. The fresh-directory replay reproduces the certificate and CSV byte for byte, verifies source hashes and passes six checks: coherent worst-case noise, duplicated time moments, complex-transpose singular bounds, non-exact partial threshold count, parent budget reproduction, and staircase monotonicity/accounting. No enormous Hankel matrix is allocated. Inherited modal diagonalization is not rerun.

Recommended next step — priority **97/100**: freeze a rank-adaptive acquisition contract that declares a window, per-vector error receipt and target retained count before independent validation. The immediate concrete candidate is M = 4,096 and δ ≤ 2^-20 for 1,893 signals. Apparatus execution and non-constructor review remain open.
