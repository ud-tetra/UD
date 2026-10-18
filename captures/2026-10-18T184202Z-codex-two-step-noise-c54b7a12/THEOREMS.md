# Two-step noise tolerance: certified scopes

Development — no registry entry. Physical promotion = 0. These are conditional finite numerical and exact algebraic results for the pinned synthetic PR195 stress record and the PR197 source-precision rule. Same-team review is not independent review.

## 1. Arbitrary per-vector order ball (DERIVED)

Let Y have 8191 time rows and 62×37 columns ordered c×37+a. Let S=A/128 be the unchanged width321 sketch, with ||S||F²=738137/4096. Assume each of the37×8191 additive62-vectors has Euclidean norm at most δ. Then

||ES||2 ≤ ||E||F ||S||F ≤ Cδ,  C=√(37×8191×738137/4096).

This permits correlated, adversarial and time-dependent errors. It does not assume the frozen random pattern. The parent receipt gives σ209(YS)≥s0 and σ210(YS)≤ε0. Weyl implies exactly209 singular values exceed τ=2^-24 whenever

Cδ < min(s0−τ, τ−ε0).

UNIFORM_CERTIFICATE.json encloses this strict radius between adjacent2^-100 dyadics. In particular δ≤2^-37 passes; δ=2^-36 is not certified by this sufficient bound. The bounds concern singular-value order, not floating solver convergence or phase accuracy. Error is relative to the already encoded PR195 stress record; generation error is already included in its parent receipt and is not charged twice.

## 2. Exact frozen-family order bounds (DERIVED + NUMERICAL)

For unit sign noise U, form N=UA as exact signed integers and G=NᵀN with FLINT integer arithmetic. With integer amplitude a and raw quantum2^-48,

||ES||2 ≤ a·√min(tr G, max_i Σ_j|Gij|)/2^55 = b.

The exact Gram, raw hashes and all18,790,154 integer differences per case are checked. Thus σ209≥s0−b. For dense noise σ210≤ε0+b. Coherent DC noise is time-constant and lies exactly in the stationary column of the source frame. It can be absorbed in the comparison coefficients, so its σ210 bound remains ε0 while excitation is still checked using s0−b. These are sufficient bounds, with HOLD denoting an inconclusive bound.

For every frozen case each62-vector has squared added error62a²/2^96. At a=2^25 this equals(31/32)·2^-40 and satisfies the per-vector2^-20 gate. It also meets the scalar2^-23 sufficient gate exactly. These gates do not imply phase acceptance. Amplitude families sharing one frozen sign tensor are not independent random replicates.

## 3. Conditional ideal-subspace lag-two phase bound (DERIVED)

Write the ideal source sketch as PC, with P full column rank209 and exact orthogonal lag-two source shift J. Let U be an orthonormal basis for its column span. Parent validated source reduction D, inverse proposal K, basis defectη, span defectζ, inverse residualρ and norms h=||K||,d=||D|| give

m=√(1−η)(1−ρ)/h−ζ ≤ σmin(P),
M=√(1+η)d+ζ ≥ ||P||, κ≤M/m.

Polar correction of the actual parent basis and exact saved last two rows give βU≥√(1−||Uactual,last||F²/(1−η)). Aligning to the source span loses at most d0=√(2−2√(1−(ζ/m)²)), so σmin(Uminus)≥β=βU−d0>0.

For total source perturbation e=ε0+Cδ and source σ209 lowerα=s0−ε0, the ideal top209 subspace sine is at most t=e/(α−e), provided α>2e. Its aligned basis distance is at most d1=√(2−2√(1−t²)). If β>d1 then the exact lag-two least-squares matrix T for that ideal orthonormal subspace satisfies

||TD−DJ||·||D^-1|| ≤ R = 2κt / ((β−d1)√(1−t²)).

Indeed write P=Uhat D+Espan with ||Espan||≤Mt. Lag-two restriction gives TD−DJ=Uhat_minus†(Espan_minus J−Espan_plus), with ||J||=1. Also σmin(D)≥m√(1−t²). Normal-model eigenvalue disks and homotopy counting yield unique matching if2R is below the209-target minimum chord. Circular phase error is at most asin(R) when R<1; its uniqueness check is also imposed. This is an exact ideal-subspace sufficient bound, not a floating backward-error certificate. It returns HOLD for every frozen uniform row, includingδ=0. No positive uniform phase tolerance follows from this bound; no failure or zero actual tolerance follows from HOLD.

## 4. Actual floating-output phase certificate (NUMERICAL, validated)

The unchanged PR197 record-only proposer learns its own order atτ and fits the lag-two least-squares matrix before instrumentation. Original and instrumented emitted phase archives must be byte-identical. For order209 only, exact binary witnesses are validated using integer Grams and512-bit Arb bounds.

Let actual T,D,K and actual eigensystem V,Λ,H have validatedρD=||DK−I||<1 andρV=||VH−I||<1. Set hD=||K||/(1−ρD), δλ=||TV−VΛ||·||H||/(1−ρV). For the exact normal source shift J,

R=hD (||TD−DJ|| + ||D||δλ).

The J rotation enclosure is included. Strict disk separation and phase/quantization bounds certify unique matching of the actual emitted2^-60 circular angles to all209 source targets. Source order must also be certified. A source-order HOLD or similarity-phase HOLD is preserved, with no forced truncation or threshold change. Phase units are radians per TWO-STEP sample. Dividing by2 leaves the original frequency moduloπ; source lifts remain conditional.

## 5. Supplemental source-target comparison (NUMERICAL, validated)

A floating Hungarian assignment is only an untrusted matching proposal. Each assigned actual emitted angle is compared with its exact source target using validated arguments and the minimum of three valid circular-distance upper bounds. Twice the maximum error below the target separation certifies a unique disjoint assignment. Otherwise only that proposed assignment's error bound is asserted. This sharper source-aware diagnostic does not replace a HOLD in the frozen primary similarity certificate.

The initial supplemental diagnostic encountered an unresolved outward rounding at exactzero. Its failed attempt is retained. direct_error_v2.py first takes the validated upper endpoint, then outward dyadic rounding. Recipes, estimator, primary certificate and gates were unchanged. DIAGNOSTIC_CORRECTION.json identifies this postexecution correction.

## 6. Scope and blindness (NO-GO / OPEN)

No finite list of tested amplitudes proves all intermediate amplitudes or all noise patterns pass the actual floating estimator. The 2294×321 sketch has a right-observation kernel of dimension at least1973: ES=0 leaves its outputs unchanged. Raw-noise admission must therefore be checked independently. This sketch blindness is distinct from the nominal747-dimensional dynamical unobservable subspace. Neither is repaired by this campaign. No SI, apparatus, full-Hankel, independent-review or physical-promotion claim is made. The original noise-cutoff204/205 HOLD remains unchanged.
