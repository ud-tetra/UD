# Gauge-aligned conditioning, saved floating least squares and fixed-basis lag obstruction

Development — no registry entry. Physical Promotion=0; external promotion review PENDING. This is a mathematical/posterior continuation of PR254/256/258/260, using the two already saved PR256 outputs. Zero new estimator calls, raw records or retained-factor copies; no full Hankel allocation. Every earlier campaign status and gate remains immutable.

## Main results

The exact saved-dyadic normal equations validate the actual floating least-squares step for both saved outputs. For A=U[:-2], B=U[2:], Gamma=A^T A and N=A^T(AT-B), the verified positive Gram floor gives ||T-A†B||2 <= ||N||2/lambda_lower. Full integer Gram/normal witnesses are retained rather than merely asserting solver accuracy.

| Saved case | Normal operator upper (via Frobenius) | LS-step operator-distance upper |
|---|---:|---:|
| Top1 alternating | 2.888633811516826e-14 | 2.9957398491767956e-14 |
| Top2 alternating | 2.882566856634085e-14 | 2.989447941066855e-14 |

The Gram eigenvalue floor exceeds0.96424721669693 in both cases. The result is finite and posterior; it proves no all-input rounding guarantee, exact spectrum(T), zero model residual or physical accuracy.

A separate explicitly postknown Pythagoras corollary, frozen and reviewed before its new lower-bound evaluation, proves

 min_X ||AX-B||F² >= max(0, ||AT-B||F²-||N||F²/lambda_lower).

Top2's minimum Frobenius lag exceeds6.157845732673311e-11 > 2^-34 =5.820766091346741e-11. Thus no T-only repair can pass that old gate at the fixed saved U. Top1 lower5.567150207488287e-11 does not establish such an obstruction. This is neither an operator-norm failure nor a phase failure: PR258's separate operator certificate and PR256's finite saved phase results stand. It is also distinct from the older rank209 full-reconstruction-cap NO-GO.

## Conditional input theorem

The new bound uses projectors and a coherent Procrustes alignment, avoiding an unqualified raw SVD gauge. For R=(U^TU)^(1/2), Q=UR^-1 and alignment O, the shift is O^T R T R^-1 O. The polar similarity is essential. THEOREMS.md derives projector, Procrustes, aligned-shift, exact least-squares-map and rank-cutoff bounds.

All82 frozen rows are retained:57 certify conditionally (including zero);25 HOLD. Largest positive qualifying grid point is extra sketch operator radius zeta=2^-45, with:

| Quantity | Bound |
|---|---:|
| Projector distance upper | 1.5140651100670966e-9 |
| Two-step target phase upper | 3.6341241257342406e-7 rad |
| Matching margin lower | 8.587620959342127e-10 |
| Unpolarized deleted-basis sigma lower | 0.9744380641723569 |
| Exact aligned LS-map change upper | 3.148325200939988e-9 |
| Required computed singular-value error (strictly below) | 5.960073836888403e-8 |

These bounds require FUTURE q209 outputs to actually satisfy the original PR254 retained-equation/Gram/lag/eigenpair/inverse/argument/encoding caps and a positive source-scale proposed singular floor. Otherwise HOLD. The singular-value error budget is a requirement, not a proved uniform backend error. Source H/full-factor/frame/target proofs are inherited and hash-pinned. The theorem does not transfer raw factors into PR260's fixed-gauge2^-49 box.

Projection-conditionally zeta/C is about4.759869900267585e-17 extra per-vector raw radius, below the2^-48 encoding quantum. The additional encoded ball about a fixed record contains only zero. The total radius retains exactly the earlier zero/one/two-coordinate pattern set. No new nonzero encoded-input tolerance is advertised; zeta2^-44 HOLD is failure of this sufficient phase envelope, not a counterexample or exact stability boundary.

## Verification and scope

Core packages and controls were frozen, separately reviewed and root-released before their new evaluations. Controls:18 conditioning constructor checks,13 LS constructor checks,16 independent mathematical checks. The corollary adds4 pure root and8 independent controls. Independent review matched all82 rows and all174,724 Gram/normal entries; root replay reproduced certificate and witness bytes exactly. Review is same-team mathematical review, not external promotion authority or blinded experimental replication. The original sealed review is preserved, with append-only v0.2 corollary extension.

The public-source AST audit binds the actual estimator implementation. Exact integer projection has explicit range checks. Floating SVD, least-squares, eigenvalues, eigenvectors, inversion and argument values are proposals requiring separate posterior checks. Undocumented default drivers, binary builds, uniform numerical success and uniform rounding bounds remain unproved. No solver defaults were inferred.

Primary saved-normal verification took20.80217570399691s with process peak RSS580268KiB. Unique gzip witness bytes total4,091,335; resource timing is a verifier measurement, not an estimator or full-pipeline benchmark. Replays retain identical witnesses for audit; Git stores identical blobs once. No287-GiB Hankel matrix was allocated.

The bounded evidence review retains its original PR261/issue check and any separately hashed incremental PR262 addendum. No attributable actual R01–R14 return was found within those stated checks; this is not global absence. All128 paths unresolved; request UNSENT. No outreach, physical acquisition, site deployment or Project-board update is claimed. Genesis PNG unavailable/unused.

## Record and next dependencies

MANIFEST.json inventories all new files with SHA256/size/provenance; a unique event and contributor PR provide append-only publication. Frozen source hashes remain immutable even after relocation into this capture; execution receipts record pre-capture locations. Existing source packages are read, not copied or modified. Same numerical values never identify different typed objects; protocol tolerances remain controls under ledger v0.39 and CRL2 anti-erosion rules.

Next1: build a frozen proposal-plus-exact-verifier admission path for genuinely fresh eligible encoded records, recording failures as HOLD; do not claim universal backend success. Any T-only repair of Top2's old fixed-U Frobenius gate is now ruled out.
Next2: actual independently supported source-specific calibration/acquisition/model/fresh-lineage returns and non-constructor review/custodian ruling. No new template or constructor simulation can substitute for those returns.
