# Bounded excitation family and prospective apparatus contract

Development — no registry entry. Physical Promotion=0. Same-team reviews are not external non-constructor review.

## Exact objects and inherited premises

Let Y0 be the pinned synthetic raw baseline, unfolded as8191×2294 with column37c+a, raw quantum h=2^-48. There are n=18,790,154 scalar entries and v=303,067 preparation/time62-vectors. Its independently recomputed exact norm is F0²=552546211865498532528442731269961/2^96. The baseline hash is25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59. The source and saved-anchor receipts are inherited premises, not apparatus facts or independently re-run estimator outputs in this capture.

The pinned source waveform uses52 frequencies with two shared parity clock families: t_a,k=(a-18)/36+(1+p_a 2^-20)k+p_a(-1)^k/16, p_a=+1 for even a and-1 otherwise. Within each parity/frequency, preparation origins enter coefficients of two common cosine/sine time functions. Consequently the exact unsketched source Y* has rank at most1+2*2*52=209, despite alternating jitter. The validated generator scalar error is d0=278304534082539066/2^120+2^-49. Arbitrary preparation-specific clocks are not covered.

The frozen sketch S=Aint/128 has2294 rows and321 columns. Its first/last160 columns are twice seeded signs; its middle padded null column has squared norm16228. Thus ||S||op<=||S||F=kA, kA²=(320*4*2294+16228)/128²=738137/4096. The exact projection Z=YS has8191×321 entries. No native1893-dimensional Hankel claim is made.

The SIX anchors are reverse_stationary, shuffle_cycle, shuffle_block1024, offset_rotation_period2, double_rotation_period4 and transpose_directed, all from PR231. Each Tj is exactly orthogonal, same-parity, and rational; its saved record is round_h(Y0 B_Tj)+Ej with each62-vector of Ej bounded by h. Its certified sigma209 lower gj comes from that same saved record, not an unrounded surrogate. Code checks the integer matrix orthogonality/parity and hashes tying these inputs together. g=min_j gj>0.0026729647180951.

## Uniform cutoff theorem

For a real exactly orthogonal, same-parity37×37 T define B_T to repeat the preparation map over62 channels. Require min_j||T-Tj||op<=rho, and let

R(T,E)=round_h(Y0 B_T)+E,

with coordinatewise nearest rounding error<=h/2, E in hZ^n, and every62-vector of E having Euclidean norm<=delta. This is a ball about EACH NEW rounded nominal, not the old original-baseline ball. The smaller condition ||T-Tj||F<=rho suffices. Only aggregate pre-rounding preparation energy is preserved, not each preparation's norm.

Orthogonality, the rank209 source, and Eckart–Young give

sigma210(RS)<=B(delta)=kA[(d0+h/2)sqrt(n)+delta sqrt(v)].

This bound is independent of rho. Anchor subtraction, the two rounding errors and the different anchor/family noise bounds give

||RS-Zj||op<=D(rho,delta)=kA[F0 rho+h sqrt(n)+(delta+h)sqrt(v)].

There is no extra sqrt62 factor in F0 rho. Weyl then yields sigma209(RS)>=g-D. Strictly g-D>c and B<c imply exactly209 singular values ABOVE c=2^-24. This is a cutoff count; the exact discarded singular values need not vanish.

Freeze delta=1127*2^-48 and rho=2^-20. Directed512-bit Arb arithmetic verifies B(delta)<c/2, B(delta+h)>=c/2, and rho<rho_crit<=2rho where rho_crit=(g-c-kA[h sqrt(n)+(delta+h)sqrt(v)])/(2kA F0). Therefore1127 is the maximum integer for THIS sufficient half-tail contour, and2^-20 is the largest power-of-two radius satisfying THIS half-gap reserve. These conservative contours are engineering choices, not sharp failure thresholds or physical constants.

At the CLOSED selected radii, sigma209>0.0016037985060919 and sigma210<2.979654257366e-8<2^-25. Exact rational outward endpoints, not displayed decimals, decide the comparisons. Future floating SVD/normal/frame/phase outputs still require their own unchanged certificates. No universal library success, future emitted phase bound, exact algebraic rank209, or fixed int64 implementation claim follows merely from this theorem.

## Why unrestricted orthogonal remixes do not suffice

A rank-one source along e1 and sketch S=e1 is observed before an orthogonal quarter-turn, but is annihilated when rotated to e2. This can occur within a same-parity preparation block and preserves source rank/norm. It is a generic counterexample to an unrestricted excitation inference, not a demonstrated failure for the fixed600-cell-derived source. Anchored lower margins supply the missing premise.

## Calibration budget and model mismatch

For z=g_true*y+b_true+n, correction yhat=(z-bhat)/ghat and independently justified ghat>=gmin>0, an admissible scalar bound is (dg*A+db+deltaADC)/gmin+processing+Lt*dt. All terms must be deterministic, valid over the frozen run domain and model-coordinate units. Channel/vector/Frobenius budgets follow Euclidean aggregation within a displayed decomposition; disjoint deterministic error components add by the triangle inequality. No independence or root-sum-square cancellation is presumed.

Timestamp uncertainty can be bounded by do_a+k*de_a+jitter_a over the finite horizon, using a separately calibrated seconds-to-model-time conversion and source derivative envelope. Preparation error can be bounded by Fanchor*||T-That||op. Terms tested as mismatch cannot also be subtracted as acquisition uncertainty. A uniform vector acquisition bound delta_v gives projected Frobenius error alpha<=kA sqrt(v) delta_v. Neither raw quantization nor this source-family excitation delta is evidence of actual instrument precision.

Freeze model, preprocessing, cap, horizon, initialization rule and preparation lineage before scored validation. For measured residual enclosure[rlo,rhi], valid acquisition error alpha and predata mismatch cap tau in the SAME space/units, true mismatch lies in[max(0,rlo-alpha),rhi+alpha]. Upper<=tau gives conditional consistency; lower>tau contradicts the frozen collection of assumptions; overlap/inconclusive inputs give HOLD. Contradiction does not uniquely identify hiddenbulk dynamics or falsify all UD constructions. Hashes establish bytes, not calibration truth or reviewer identity.

The packet verifier in this capture tests synthetic intake and arithmetic only. Any apparatus_submission remains HOLD_UNQUALIFIED and explicitly reports actual numerical evidence verification unimplemented. The unfilled actual packet is not a certified experiment. Two-step exp(2i omega) only determines omega modulo pi; calibrated time alone does not resolve aliases. Unaliased/SI claims need an independently frozen injective frequency band and filter/clock evidence.

## Typed lane separation

The current209-clock sample index step is1. The separate six-ratio12-reading protocol uses1/32 and ratio l2 gate2^-39. The old native1893 history contract uses normalized step1/2, candidate raw step16/33 and vector error2^-20. Its62 history channels differ from189 diagnostic outputs. Shape gate2^-38 retains its source-defined statistic. The rejected2^-49 residual gate is not reinstated. The nominal747-dimensional unobservable space is unchanged; no leakage or hidden-state recovery is inferred.
