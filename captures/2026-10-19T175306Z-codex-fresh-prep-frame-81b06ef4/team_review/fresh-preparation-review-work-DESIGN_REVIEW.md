# Fresh synthetic preparation protocol — same-team design review

Status: design acceptable with the domain and proof restrictions below. This review uses the proposed recipes and the published source-frame policy, before viewing any new record or estimator outcome. No new records, transforms, estimator runs, or numerical outcomes were produced by this review.

## Preparation map and signal scope

The proposed 37-by-37 maps are block diagonal on the even-index group of size19 and odd-index group of size18. A signed cycle and signed shuffle are exact integer orthogonal maps. A rational plane block can be fixed as `(u,v) -> ((3u-4v)/5,(4u+3v)/5)`; its exact numerator matrix has transpose-product25I. Pair adjacent indices in each parity list and leave the last even index unchanged. Explicit input/output indexing and signs must be frozen, as must shuffle RNG algorithm, seed219137, call order and exact sign pattern.

Before rounding, an invertible preparation map preserves the temporal column span of the full unsketched observation matrix and cannot create new dynamical clock frequencies. The family is a synthetic linear remix of the original recorded preparations. It does not constitute independent physical acquisition or an independent generator validation. Parity preservation keeps the two preparation classes separate. Orthogonality preserves total energy within each parity group; preservation of each individual preparation energy additionally requires the corresponding within-parity preparation Gram matrix to be a scalar multiple of identity.

The fixed sketch does not generally commute with preparation mixing. Its singular values and numerical order may change. Neither temporal-span preservation before the sketch nor exact orthogonality proves that the new sketched data will have learned order209 above2^-24. Preserve any learned-order refusal; never force209 or select another sketch based on outcomes.

## Exact rounding and separate input domains

Signed permutations act exactly on the existing integer raw baseline and need no rounding. For a rational plane block, form its two integer numerators from the original pair, then round each numerator divided by5 exactly once. Do not update one member of a pair in place before forming the other, and do not implement rational rounding through float64. Use arbitrary-precision integers or prove the intermediate multiply/add range fits int64 before generation. Check the final raw integer range and the exact integer-projection overflow/cast premises for each new family.

Because5 is odd, an integer numerator divided by5 never has a half-integer tie. Exact nearest rounding has coordinate error at most2/5 raw quantum, sharper than the generic1/2 bound. The predicate `5*rounded - numerator in {-2,-1,0,1,2}` is a complete exact rounding check. A generic nearest-even helper can still be used; its tie rule is irrelevant for these particular denominator5 values.

Each new family has its own nominal integer record: the exact signed transform, or the once-rounded rational transform, of the pinned clean raw baseline. One independently generated onehot±1 integer perturbation in each62-vector has squared integer norm exactly1 relative to that new nominal, hence encoded norm exactly2^-48. Verify this difference directly and retain every scalar mismatch/count. Noise seeds219201,219202,219203 and the complete channel/sign draw ordering must be frozen before generation. These are deterministic pseudorandom fixtures, not empirical independent-noise measurements.

The original baseline-centered raw ball is not the new eligibility domain. For the rational family, the pre-noise rounding discrepancy relative to its exact rational nominal has62-vector norm at most `(2/5)*sqrt(62)*2^-48`. After additive onehot noise, the conservative bound is `[1+(2/5)*sqrt(62)]*2^-48`. Neither this estimate nor new-nominal one-quantum eligibility establishes membership in the old original-baseline one-quantum ball. Do not silently reuse old whole-ball certificates for these new inputs. Pin the clean baseline hash and distinguish it from the prior CYCLIC anchor before generation.

## Fixed source-frame policy

The published direct source-frame proof applies to an actual retained basis U1 through its measured dyadic residual `R=U1-U0X`, with an arbitrary untrusted dyadic alignment X. Its algebraic implication is not restricted to the old baseline raw ball. Therefore it can be used on the proposed new synthetic families if the same reference U0, source constants, strict raw-frame residual budget, Gram cap and normal-residual cap remain frozen.

In particular retain the PR224 raw-frame budget about2.4895818841068944e-10, retained Gram cap2^-43, and the exact previously frozen normal cap (maximum verified upper over the three old named outputs, about3.078514e-14). The exact dyadic values are authoritative; the decimal descriptions are not new thresholds. Do not replace the normal cap with the maximum new residual, or choose alignment/budget thresholds after looking at new outcomes. Auxiliary alignment proposals may be fitted after each actual U1 is returned: their acceptance depends on exact residual verification, with no inverse or optimality premise.

The result is a source-frame/actual-returned-shift validation. Without the corresponding fresh fullfactor, eigensystem, angle and all-eight-gate checks, it is not a new complete spectral/phase/all-eight-gate certificate. Actual retained Gram and exact normal residual must be computed for the same returned U1/T. Learned order must be209 for this fixed209 reference route. A failed sufficient budget or changed learned order is HOLD, not proof of an actual phase error or universal algorithm failure.

## Controls and retention

Before records or estimator execution, freeze the exact transform matrices/tables, source baseline hash, seeds and RNG call order, integer rounding rule, projection source/sketch, estimator code/cutoff, and the exact inherited policy numbers. Hash all new raw records before any fits. Retain all three families and all PASS/HOLD outcomes without outcome-dependent replacement.

Useful exact controls are: wrong parity mapping rejected; a repeated/missing permutation index rejected; rational block transpose-product25I; a rounding value outside the exact residue predicate rejected; onehot norm/count verified against the correct new nominal; byte/hash mutation rejected; cap equality handled by the already frozen strictness convention; zero alignment fails the principal-angle guard; a learned order other than209 does not enter this209-dimensional source-frame certificate. An independently written raw regeneration should reproduce full records and the exact projection before saved-factor replay.

Review scope: same-team mathematical design only. No new input records or estimator runs, no new external review, no physical promotion. External review remains pending; Physical Promotion=0.
