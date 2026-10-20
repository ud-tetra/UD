# Frozen two-case actual floating estimator protocol

Development research only; Physical Promotion = 0. Epoch: UTC 2026-10-20; Chicago 2026-10-19. The head at intake is 9c1795d5e815d65c20ef0965fb8a79747175d8aa (merged PR254). Governance versions 20/21 apply. No registry entry or universal floating backend success claim is made.

## Outcomes and custody

The PR254 `null_top1_alternating` and `null_top2_alternating` original-nominal recipes already have known strict rank-209 reconstruction-cap NO-GO proofs. Those old outcomes remain unchanged. Actual floating estimator outputs are UNKNOWN at this protocol freeze. The existing cyclic-one-quantum receipt is inherited evidence only; no control estimator call is authorized here.

The exact fixed sequence is top1 then top2, two records only. All raw hashes, exact noise norms, all scalar overflow checks, and exact integer/projection hashes for BOTH recipes must be written to DATA_FREEZE.json BEFORE the first fit. Projected numerator hashes must match the independent reviewer receipt. Raw records are regenerated deterministically into one temporary 150,321,232-byte file at a time, verified, and removed; they are never retained as duplicate archive files. Regeneration, hash checking, and matrix arithmetic are not fits.

## Execution

`estimator.py` is byte-identical to PR250 source SHA256 5fa15ca0f3830f168fe9e1483db7f21cb6e462780209b4d8b4e8ad43d64cfe86. Only its imported custody/environment module is isolated. Its seeded sketch, rank gate, LAPACK/SciPy SVD, lag least squares, eigenpairs, inversion, angle calculation, and ties-even emissions are unchanged. No rank forcing, cap tuning, sketch change, alternative estimator, retry or replacement is permitted. A pre-fit reviewer and root release must be obtained before `driver.py fit --execute-once`.

The driver freezes an exclusive per-case START intent, calls `estimate` once, preserves returned HOLD/error and saved numerical witnesses, and continues to the fixed remaining case. Any exception is a retained HOLD. No recovery execution is permitted. All saved factors are retained losslessly once. Numeric environment and witness hashes are in unchanged RUN.json. The final report distinguishes invocation intent from completed output.

## Exact output certification

At fixed 512-bit FLINT/Arb precision, finite binary64 factors are decoded into exact dyadics. Integer FLINT row chunks (512 rows) evaluate retained singular equation `Z V - U Sigma` exactly, with Z=N/2^55. The exact rational squared Frobenius norm is retained. Its outward 180-bit dyadic square-root upper bounds the operator norm xi. The reconstruction tail is neither added to nor erased from xi. Both U and V Gram defects and raw two-step lag residual `U[2:] - U[:-2] T` are likewise exact dyadic squared Frobenius norms, used conservatively as operator upper bounds.

For each completed q=209 output, all PR254 caps are checked independently: etaU,etaV <=2^-43; xi<=2^-41; raw lag<=2^-34; inverse residual<=2^-40; inverse norm<=128; eigenpair residual<=2^-42; emitted argument/encoding error<=2^-50. The measured proposed s209 must independently satisfy `s209 >= s0 - C*(3/2)*2^-48 - 2^-41 > 0`. The radius is the frozen common 3/2 quantum ball and is not reduced for either outcome. The pinned PR254 equation theorem then propagates the measured quantities and unchanged source frame to finite source-target phase matching. No full SVD reconstruction, exact-spectrum(T) forward error, universal solver, unaliased primitive-frequency, six-ratio or physical claim follows.

The copied PR250 phase qualifier uses its exact saved complex inverse/eigenpair residuals, inverse-norm bound, Arb argument bounds and exact ties-even fixed-point encoding. It directly checks a bijection of all 209 emitted two-step phases to the pinned source targets modulo 2pi, within the fixed source half-chord. Finite list accuracy and conditional equation theorem are both required, alongside all numerical caps.

## Review and controls

Before fits: static source review; both-data hash/norm/overflow/projection audit; immutable protocol/source hash binding; synthetic exact dyadic Gram/equation/lag controls; invalid output ancestor/descendant and symlink guard checks; unchanged inherited theorem negative controls, with no fit. After fits: an independent saved-witness replay with zero estimator calls and separate reviewer inspection. Every gate and HOLD is recorded, without changes of precision, targets or caps in response to outcomes. Output paths are checked lexically and after resolution against the package and all MANIFEST-bearing ancestors, including invalid ancestor destinations. Writes are exclusive.
