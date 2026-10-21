# A bounded native-integer implementation of the weighted600-cell actions

Development — no registry entry. DERIVED algorithm/error/overflow certificate with executed source-bound comparisons. External promotion review PENDING; Physical Promotion=0.

## 1. The mathematical map stays fixed

Use the PR316 source operator and the PR313 decoder without changing the model. F has2640 state coordinates,62 ordered observer coordinates and4096 normalized half-step samples; H=2K has14880 entries±2 or±3, with Q=H/4=K/2. The source identity, weighted chain annihilations and squared boundary norm caps24,15,15 imply ||Q||<5/2. The ordered source bytes retain SHA256 cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950. The source file's128 field is retained metadata of the previous reference protocol; the new arithmetic grid104 is declared separately. This does not change F, R, K, rank1999/kernel641 or the Euclidean metric.

The optimization replaces arbitrary-precision propagation with signed128-bit integer operations. GMP remains only for the exact external-domain squared-norm checks. Inputs and delivered outputs remain exact integers times2^-96. The source/build-bound adapter from PR316 still verifies expected operator and executable hashes before every call. Correct trusted build/compiler/GMP execution and stable intended files remain explicit premises.

## 2. Native recurrence, signed division and source identity

Internally use integers times2^-104. For either sign, form Taylor terms through degree40 by

\[
t_0=v,\qquad t_k=\operatorname{trunc}_{104}(\pm Ht_{k-1}/(4k)),
\qquad \widetilde E_\pm v=\sum_{k=0}^{40}t_k.
\]

All multiplication/addition before division is exact if it stays within signed128 range, as proved below. Division truncates toward zero. The weighted sparse row is evaluated by collecting one signed copy of every incident value into z, collecting one additional signed copy only for entries of magnitude3 into extra, then taking2z+extra. Thus it equals Ht exactly for all weighted/unweighted entries. Template specialization fixes each divisor4k at compile time; it changes no algebraic expression.

External96→internal104 multiplication uses2^8. Forward normalization/delivery divides by2^14, accounting for64 and the8 grid bits. Adjoint injections multiply by2^2 exactly, since104−96−6=2; final adjoint delivery divides by2^8. No signed left shift of a negative value is used. The decimal conversion handles the signed minimum safely; admitted values are much smaller. The parser bounds scalar input magnitude before any native scale multiplication, and exact GMP Euclidean-domain checks precede the grid conversion.

## 3. A complete overflow argument

Let C=4096 and u=52*2^-104. The comparison with exact Taylor terms, as in PR316, gives per-term vector rounding error below3u and whole-step error r=120u=6240*2^-104. The exact Taylor term norm multiplier max_(0<=k<=40)(5/2)^k/k! is less than4. Thus every computed term has norm less than4C+3u. Every partial sparse-row sum has absolute value bounded by the row absolute sum24 times that term bound. In integer coordinates,

\[
24(4C+3u)2^{104}<2^{123}<2^{127}.
\]

This is a bound on every partial accumulation, not merely its final value. A rational Taylor/geometric-tail comparison proves exp(5/2)<13. Consequently every partial output sum has norm less than13C+r, so each corresponding integer magnitude is below2^121. Negation, coefficient handling, positive power-of-two multiplication and division remain in range as well.

The code additionally guards every supplied term and every divided next term by absolute integer magnitude<2^119. With the accepted row absolute sum<=24, every intermediate sparse sum is then below2^124, and a sum of at most41 guarded terms is below2^125. These guards provide a conservative fallback against oversized runtime terms. The source-bound proof establishes that no admitted computation reaches them. Nine specific invalid-input rejections are tested; neither those probes nor this certificate claim universal hostile-file or compiler/runtime verification.

## 4. Uniform action error is preserved

The unchanged degree40 truncation bound is

\[
\tau=\frac{(5/2)^{41}}{41!}\frac1{1-5/84}<2^{-109}.
\]

For every internal state v with ||v||<=4096 in the admitted source-bound execution,

\[
\|\widetilde E_\pm v-e^{\pm K/2}v\|\le\tau\|v\|+6240\,2^{-104}.
\]

Set

\[
E=4096(4096\tau+6240\,2^{-104}).
\]

The exact forward states have norm<=2048. Exact normalized adjoint partial sums have norm<=2049 by Cauchy-Schwarz and the1/64 factor. Comparison at each computed input with the exact isometric exponential accumulates at most E error. Exact rational checks give E<1 and2049+E<4096, closing the internal cap C. This avoids exponentiating a loose norm growth bound over4096 steps.

Final delivered-coordinate rounding gives

\[
\|\widetilde Fv-Fv\|\le E+504\,2^{-96}
\approx1.27755\,10^{-24}<2^{-68},\qquad\|v\|\le2048,
\]
\[
\|\widetilde F^Ty-F^Ty\|\le E+52\,2^{-96}
\approx1.27185\,10^{-24}<2^{-68},\qquad\|y\|\le2049.
\]

The exact fractions and overflow comparisons are retained in NATIVE_CONSTANTS.json. Both upper bounds are actually below2^-79; the retained contract remains the unchanged2^-68. Computed forward outputs stay inside the data ball2049, so the composed normal action remains within2^-67. Hidden-direction errors are included; the method does not require computed actions to stay exactly in the observable subspace.

## 5. Conformance and finite execution evidence

The104-grid output generally differs from the previous128-grid reference. The correct conformance test compares their difference with the sum of their two independently proved true-map error bounds. Exact full-vector squared differences pass for all253952 forward coordinates and2640 adjoint coordinates. Full-size duality satisfies the same absolute-budget logic. No exact linearity or transpose identity is asserted for the rounded delivered maps.

Within the new104-grid method, full forward/adjoint replays are byte-identical, including across a parser-only source correction. Separate review evaluates its own eight compiled halfstep probes and checks all21120 delivered outputs against a Python-bigint104-grid recurrence. That reference evaluates844800 term-coordinate divisions; compiled intermediate terms are not exported or claimed compared. Zero, dense signed and positive/negative norm2048 boundary states are exercised for both signs. Nine additional rejection cases pass, including a truncated operator at the incidence count. The source/readout and analytic constants are separately checked.

A source/build-bound actual sixteen-step run connects the native actions to the unchanged PR313 Arb/dyadic decoder. It uses15 forward and16 adjoint actions, with42240 whole-update coordinate checks at state dimension2640. This is a finite extension from the earlier two-step run. It does not inherit the8192-step projection defect bound or establish any final accuracy gate. Full8192 execution and performance remain OPEN.

## 6. Timing evidence and interpretation

The final paired benchmark runs the earlier GMP propagation and new native propagation sequentially for each fixed full-size input/mode. Its timing helper obtains resource usage from os.wait4 for the specific action child. Thus a previous compiler or other child cannot contaminate that child's peak RSS. The first preliminary native timing used cumulative RUSAGE_CHILDREN and its memory value is not final action-memory evidence; it is preserved as a corrected construction diagnostic.

BENCHMARK.json reports the observed walltime ratio and individual child RSS for each pair. These are measurements in this environment, not a universal speed guarantee, independent laboratory replication or worst-case bound. They exclude total Python-wrapper/pipeline memory. No full F,F^TF or287-GiB Hankel array is allocated. The8192-step decoder still requires16383 actions, so the standalone improvement is not a completed full extraction benchmark.

## 7. Scope and next bottleneck

Closed here: a new source-bound native backend, finite overflow proof, unchanged absolute oracle error contract, actual full-vector reference conformance, observed paired standalone timing and a sixteen-step full-state decoder extension. A different optimized/floating backend requires fresh source/arithmetic conformance; the result is not transferable by name or timing similarity.

Open: full8192-step extraction, practical full-pipeline performance, and every physical preparation/timing/readout/generator/noise/encoding premise inherited from the prior conditional profile. The641 nominal hidden components remain unrecovered. No six-ratio calibration, old Hankel-family condition bound or physical identification is promoted. Further acceleration or a certified reusable compression is the practical next task before the full run.

Ledger v0.39/CRL-2; Development—no registry entry. Taylor degree, native precision, guards and all O03 tolerances are controls, not theory constants. External promotion review PENDING; Physical Promotion=0. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER unused.
