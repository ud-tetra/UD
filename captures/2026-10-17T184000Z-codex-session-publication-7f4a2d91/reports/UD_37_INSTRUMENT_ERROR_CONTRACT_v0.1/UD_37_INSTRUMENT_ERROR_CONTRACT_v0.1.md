# UD thirty seven preparation instrument error contract

**RESULT — Separate preparation, readout, clock and generator bounds jointly preserve the 1893-direction Hankel signal gap.** A common candidate allocation passes all three finite schedules, with retained-signal condition bounds 16657, 3156 and 1755. The bounds are sufficient and conservative; they are not measurements or necessary hardware specifications.

Physical promotion remains **0**. This is development work with no registry entry and independent review pending. All tolerances are protocol controls under coefficient-ledger O03. No SI time conversion or physical-clock identification is supplied.

## Declared plant and measurement quantities

Keep the frozen nominal generator A, the original 62-channel coordinate observer R and the explicit 37 preparation vectors from the parent certificate. Each nominal preparation has norm `a=sqrt(165/169)`.

The candidate actual generator is

\[
K=H^{-1}(A(w)+J),\qquad H=H^T>0,
\]

where the three native incidence rates obey `|w_k-1|<=r`, the metric obeys `||H-I||<=eta<1`, and an additional generator discrepancy obeys `J^T=-J`, `||J||<=sigma`. All matrix norms are Euclidean operator norms. The constant plant is H-skew, giving

\[
\|e^{tK}\|\le g=\sqrt{\frac{1+\eta}{1-\eta}}
\quad\text{for every real }t.
\]

Native incidence blocks have pairwise zero products by boundary nilpotency. With the independently established nominal bound `||A||<4`, this gives `||A(w)-A||<=4r` and

\[
\|K-A\|\le e=
\frac{4r+\sigma+4\eta}{1-\eta}.
\]

The actual preparation is `x_a+d_a`, with `||d_a||<=p`. At nominal time t, the actual time is `(1+theta)t+b+zeta`, with `|theta|<=chi`, `|b|<=b 0` and `|zeta|<=j`. The readout is `R+E`, `||E||<=rho`, with an additional output-vector error of norm at most nu. Readout errors may vary with preparation and time within their bounds; no independence or zero-mean assumption is used.

The metric, rate and clock bounds refer to distinct quantities. Equal numerical allocations do not identify these objects or determine a physical time unit.

## Joint response error theorem

Set `tau=b 0+j` and

\[
e_{\rm eff}=e+(4+e)\chi.
\]

Duhamel's formula and H-skew norm control imply, for nominal t at least zero,

\[
\|y_{\rm actual}(t)-R e^{tA}x_a\|
\le u+vt,
\]

where

\[
u=g\left[(1+\rho)p+\rho a+a(4+e)\tau\right]+\nu,
\qquad v=g a e_{\rm eff}.
\]

Preparation, instantaneous readout and absolute timing errors enter u. Generator error and relative clock drift enter the accumulating term vt. This separation prevents a fixed jitter budget from silently absorbing clock drift over a long record.

The formula includes simultaneous errors and their cross terms. It does not sum separately optimized one-error-at-a-time limits. It assumes the declared constant H-skew plant; unrestricted nonnormal or time-varying generators need a different propagator bound.

## Finite Hankel error theorem

Use the parent normalized response matrix, with M samples on each Hankel axis and time `(i+j)/2` at block(i,j). The mean and mean-square times under the actual Hankel duplication weights are

\[
\overline t=\frac{M-1}{2},\qquad
\overline{t^2}=\frac{7M^2-12M+5}{24}.
\]

These are not the uniform moments of the 4095 or 8191 raw time samples. The matrix repeats raw vectors with triangular weights. Direct counting gives

\[
\boxed{\|\Delta H_M\|\le\beta_M=
\sqrt{37}\sqrt{u^2+2uv\overline t+v^2\overline{t^2}}.}
\]

The certificate verifies both time-moment formulas by exact weighted integer sums. No large Hankel matrix is materialized. The simpler uniform raw-vector bound is `u+v(M-1)`; both bounds are checked against the parent error contract.

If s is the parent lower bound on the smallest nonzero singular value, and B its upper bound on the largest, then `beta_M<s/4` guarantees:

\[
\widetilde\sigma_{1893}>3s/4,\qquad
\widetilde\sigma_{1894}<s/4,
\qquad
\kappa_{\rm retained}\le\frac{B+\beta_M}{s-\beta_M}.
\]

Thresholding at s/2 returns 1893 signal directions. The perturbed data matrix may have higher algebraic rank, and a perturbed generator may make additional bulk modes weakly observable. This contract does not assert that the perturbed system retains the nominal 747-dimensional kernel.

## One common sufficient allocation

| Quantity | Bound | Declared units |
|---|---:|---|
| Preparation error p, each of 37 states | 2^-25 | Euclidean state norm |
| Readout operator error rho | 2^-25 | Operator gain in the declared coordinates |
| Additional output-vector error nu | 2^-26 | Norm of the complete 62-component vector |
| Time-origin error b 0 | 2^-29 | Normalized model time |
| Per-sample timing jitter j | 2^-29 | Normalized model time |
| Relative clock-scale error chi | 2^-38 | Relative scale |
| Each native rate error r | 2^-38 | Relative to nominal unit rate |
| Metric error eta | 2^-38 | Euclidean operator norm |
| Extra skew generator discrepancy sigma | 2^-38 | Generator operator norm in model units |

This allocation gives `e=9/(2^38-1)`. Its small generator and drift limits reflect a conservative bound on accumulated response mismatch against the frozen nominal A. They are not proved necessary for finite Hankel conditioning; a certificate around a calibrated generator can permit larger nominal offsets.

| Hankel axis M | Last model time | Worst raw-vector error upper | beta_M/s upper | Retained-signal condition bound |
|---:|---:|---:|---:|---:|
| 2048 | 2047 | 1.846e-7 | 0.078 | 16657 |
| 4096 | 4095 | 2.803e-7 | 0.027 | 3156 |
| 8192 | 8191 | 4.717e-7 | 0.028 | 1755 |

Decimals in this table are outward-rounded summaries of the Arb enclosures in `INSTRUMENT_CONTRACT.json`. The defining bounds are the exact fractions and interval inequalities in the certificate. Each raw-vector error stays below the parent's respective ceilings 2^-22,2^-20 and 2^-19. Every beta_M/s is strictly below 1/4. Do not extrapolate these tolerances to arbitrarily long records.

## What independent calibration must establish

The output-error theorem is sufficient regardless of how its component bounds are established. For numerical signal-rank validation alone, a justified end-to-end raw-response bound is enough. Identifying the separate physical components requires additional evidence; a successful Hankel SVD cannot provide it automatically.

| Required receipt | Acceptance statement | Evidence limit |
|---|---|---|
| Preparation | Every actual input lies within 2^-25 of its declared 2640-coordinate target | The shell cannot test errors entirely in its hidden subspace. Independent input metrology or a justified preparation model is needed. |
| Readout | Operator discrepancy from R is at most 2^-25 on the claimed domain | The 37 preparation trajectories do not span the whole bulk. A full-domain test or a separately validated structural family is needed for this global norm. |
| Additive output error | Each complete 62-component error vector has norm at most 2^-26 | A finite set of small blank readings alone does not prove an unconditional bound on future errors. State the run scope or statistical contract separately. |
| Clock | Relative scale within 2^-38; origin and jitter within 2^-29 each | Relative clock scale and generator scale cannot be identified separately from response times alone. Supply an independent scale anchor. |
| Native rates | Each rate differs from its declared nominal value by at most 2^-38 | Use the stated constitutive family and independent clock/metric anchors. |
| Metric | SPD and global `||H-I||<=2^-38` | Dynamic data do not identify metric variations on generator-null directions. |
| Extra generator terms | Skew discrepancy norm at most 2^-38 | Hidden generator blocks require independent structural evidence or a more informative observer. |

`CALIBRATION_REQUIREMENTS.json` freezes these requirements and fields for recording future evidence. No receipt is marked executed.

## Exact calibration obstructions

The following are separate witnesses, not additive counts.

**Unexcited inputs.** The 37 preparations generate a free-evolution state span of dimension at most 2430. This follows by summing `min(37,d_lambda)` across the nominal full-carrier eigenvalue multiplicities. At least 210 real bulk directions are unexcited. Arbitrary readout perturbations annihilating the excited span have at least 210 free parameters per row, or **13020** across 62 rows, and leave every 37-input response unchanged. No full readout-operator bound follows from this experiment alone.

**Hidden generator blocks.** The nominal shell has an A-invariant hidden subspace N of dimension 747. Since A is skew, its orthogonal complement is invariant too. Any skew J supported entirely in N changes only hidden dynamics and leaves all shell responses unchanged for every possible initial preparation. Such J form a space of dimension

\[
747\cdot 746/2=278631.
\]

This obstruction applies to the declared broad family allowing arbitrary extra skew J. A narrower native-incidence model has different identification requirements. Adding inputs alone cannot eliminate this shell-observer obstruction.

**Clock scale.** For any positive c, the pair `(alpha,K)` and `(c alpha,K/c)` gives the same effective evolution `exp(alpha t K)`. Response data identify the effective generator, not the independent clock/rate factors.

**Metric shadow.** If a unit vector u lies in `ker A`, then `H=I+h u u^T` gives `H^-1 A=A` for any h greater than minus one. Even perfect full-state dynamics cannot identify that metric perturbation without another measurement.

Small exact matrix instances of these mechanisms are replayed by `validate_instrument.py`. They demonstrate why separate global calibration statements cannot be inferred from a passing signal test.

## Existing calibration gap and next action

The previous grade-calibration packet bounds its accepted metric and rate deviations by 3/10^9, while the present conservative allocation uses 1/2^38. Its stated metric estimation uncertainty 5/10^10 also exceeds this new allocation. The previous packet concerns a grade-scalar family and a 189-channel protocol; it therefore does not certify the present broader global contract. This is a gap between sufficient certificates, not a measured failure of an instrument or proof that the 37-preparation design is unusable.

The next useful derivation is a certificate around a separately calibrated fitted generator, so known nominal offsets are not charged as accumulating unknown response noise. Its calibration family and observer must be explicit. The existing 189-channel full-state observer can help test hidden dynamics if its own instrument contract is met; the original 62-channel shell cannot do that job by itself.

Constructor verification, exact replay and a machine-readable contract are complete. Independent calibration, non-constructor review and a physical time/action correspondence remain open.
