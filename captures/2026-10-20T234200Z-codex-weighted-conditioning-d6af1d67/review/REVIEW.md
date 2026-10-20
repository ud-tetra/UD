# Independent review of C27 finite-map conditioning

PASS for a fresh conditioning bound on the fixed PR305 mathematical map:

\[
\sigma_{\min,+}(F)>61/27648>1/512,
\qquad \kappa_+(F)<27648/61<512.
\]

Here F is the normalized4096-sample, half-step observation map for the unchanged epsilon=1/2 ten-tetrahedron C10-orbit weighting, the same62-coordinate observer, and unit Euclidean chain coordinates. Rank1999/kernel641 are inherited and hash-pinned. The full2640-domain condition is still infinite. This does not certify the numerical screen's estimate near180. It is a new bound for this object, not a transfer of the separate nominal Hankel2029 certificate or any preparation, estimator, calibration, shape or noise gate.

## Proof review

The arbitrary-frame route is sound. For Q of shape2640-by1999 and skew J, the exact residual E=KQ-QJ gives ||FQ-Y||<=T_rms||E|| by Duhamel, because both propagators are orthogonal. The finite-grid second moment is exactly11180715/8. Exact membership of Q in the observable subspace is unnecessary for this lower singular bound. The inherited rank premise is necessary: sigma_1999(F) equals the smallest positive singular value only because rank(F)=1999. The singular-product inequality and division by ||Q|| correctly transfer the lower bound from FQ to F.

The complete Y Gram retains all cross-channel terms. Its eigenproposal is square and full rank, as certified by its orthogonality defect. For G0, the left-eigenvector residual argument gives lambda_min(G0)>=min(d)-||G0V-Vd||/sqrt(1-etaV). Weyl then accounts for the true-Gram midpoint error. Exact conservative constants close as follows:

- etaQ,etaV<1/16;
- equation residual norm<2^-24 and T_rms<2048;
- Gram eigenproposal residual norm<2^-22, min(d)>9*2^-20;
- true-Gram midpoint error<2^-44;
- lambda_min(G)>2^-17, hence sigma_min(Y)>1/384;
- ||Q||<9/8, yielding (1/384-1/8192)/(9/8)=61/27648>1/512.

The exact margin over1/512 is7/27648. The original weak-response obstruction route was not needed; a small response would require an observable trial vector, unlike the lower-bound route used here. Separate frozen proof notes distinguish these two inferences.

## Independent finite verification

No producer checker, archived program or eigensolver was executed by this reviewer. The following were independently recomputed from the frozen inputs:

| Check | Coverage | Result |
|---|---:|---|
| Intended signed weighted source action | All grades | Exact equation residual matches |
| Q-transpose Q defect | Complete1999-by1999 product | Exact squared norm matches |
| Temporal kernel enclosures | 57,600 values | All enclosed by a separate192-bit complex geometric-series formula |
| Full Gram midpoint | 3,996,001 entries | Every exact integer matches, both triangles included |
| Saved eigenproposal orthogonality | Complete1999-by1999 product | Exact squared norm matches |
| Saved Gram eigen-residual | 3,996,001 entries | Every-entry exact product yields the recorded squared norm |
| Saved diagonal minimum | 1999 entries | Exact minimum matches |
| Conservative scalar chain | Rational comparisons | PASS |

The source K was rebuilt grade by grade with upper−B/lower+B-transpose. The temporal audit used (1-z^4096)/(4096(1-z)) with z=exp(i*delta/2^41), special-casing zero, rather than the producer's sine quotient. Gram reconstruction used literal cosine/sine coefficient vectors for every state column rather than the producer's three block cases. Both constructions give the same complete dyadic midpoint. The four coefficient magnitudes are each at most2; every kernel error is below2^-59; final dyadic rounding adds below2^-60. Thus the17*2^-60 entry envelope and the full Frobenius/operator error bound are justified.

The saved V,d witness is replayed directly without generating a replacement proposal. Its orthogonality squared numerator is459837442908301902389808122680 over2^160. Its Gram eigen-residual squared numerator is674952829151325818357725459461793805948 over2^200. The minimum diagonal numerator is10187499820548 over2^60. The independent fixed-frame audit separately matches the recorded Q-defect, equation-residual and maximum coefficient integers.

Exact adversarial controls show why the proof requires the Q norm divisor, the rank premise, a square complete Gram frame, and the full cross terms: isolated one-column conditions can both be1 while their joint map has condition at least20000. These are mathematical countermodels, not bugs alleged in the actual implementation.

## Final bindings, version history and limits

FINAL_BINDING.json pins the final source and theorem, both dyadic proposals, source archive and inherited rank receipts. All six final scientific files, including the complete Gram midpoint and compressed witnesses, are byte-identical between the producer run and its frozen-witness replay. The replay invokes no eigensolver. The independent review's finite receipts are separately source-frozen before their execution, and no witness arrays are copied into this review package.

The first source version checked an internally generated eigenproposal without retaining it. Version2 adds persistence and frozen-witness replay, inherited-result bindings and robust integer-range checks; the model, mathematical inequalities and budgets are unchanged. This addresses auditability, not a mathematical retraction. The initial numerical screen used the opposite global generator sign. Global time reversal preserves the full equally spaced sample singular spectrum; the final exact source instead uses the intended sign and negated upper-grade trial partners, verified through E. Signed predictions are not silently identified.

This is a finite same-team mathematical review after disclosed numerical witness search, not blinded validation or external promotion authority. Correct exact-integer and Arb primitives, stable intended input bytes, and the explicit inherited rank/model premises remain assumptions; no universal software, all-input, backend-completeness or concurrent-mutation guarantee is claimed. No independent acquisition, physical weight selection, instrument timing or constitutive correspondence is supplied. No sampled trajectory/Hankel array or estimator fit was allocated or run by this review. Physical/preparation/estimator gates remain HOLD.

Development — no registry entry. External review PENDING. New finite-map positive conditioning certified; physical and estimator gates HOLD. Physical Promotion=0.
