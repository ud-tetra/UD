# UD transport reconstruction under stock and readout uncertainty — v0.1

5 October 2026. Development addendum. Constructor: Codex for Benjamin Walker Mayes. Independent review pending; physical promotion 0. No registry or physical bridge level advances.

## 1. Source contract and scope

Sources: **UD_CONSTITUTIVE_CURRENT_IDENTIFIABILITY_v0.1**, sections 2–5; **UD_HASSE_CURRENT_CURL_AUDIT_v0.1**, sections 2–4 and its exact `MATRICES.json`; attached **UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md**, Q169–Q172; **UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md**, sections 5–6. Source copies and hashes accompany this release. The historical ledger is not substituted for later portal state. Repository version 176 was checked before extending its transport addendum.

Domain: one filled tetrahedron, its 15 real amplitude addresses and 28 incidence currents, known unit-incidence real skew generator A, one instant, and positive normalized stocks. The sign ray x is unknown; nominal magnitudes a_i and normalization Q define c_i*=x_i a_i/sqrt(Q), rho_i*=a_i²/Q. The nominal stock derivative is d_i*=2 c_i*(A c*)_i. Time units are the declared mathematical generator parameter, with no physical calibration.

This is design optimization and exact inference analysis. It is not a sensor benchmark, a native preparation law, a complex-phase reconstruction theorem, or global profile optimization. Papers I–IV and the controller WBS are unchanged.

## 2. EXACT: four magnitude classes suffice

Number the original tetrahedron vertices 0,1,2,3. Assign a simplex sigma the color chi(sigma)=XOR of its vertex labels, including label 0 as the ordinary integer zero. The four colors are 0,1,2,3. Neighbors of any Hasse address are obtained by toggling one original vertex i; their colors are chi(sigma) XOR i. Thus all neighbors of a given address have distinct colors. No claim that adjacent addresses must have different colors is made.

The 15 nonempty simplices have color multiplicities (3,4,4,4). Assign magnitudes

\[
(a_{\chi=0},a_{\chi=1},a_{\chi=2},a_{\chi=3})=(8,4,5,6),\qquad Q=500.
\]

The stocks are respectively 64/500,16/500,25/500,36/500, with total one. Their maximum/minimum ratio is exactly 4. The subset sums of (4,5,6,8) are distinct, with minimum gap 1.

For distinct sign rays, at least one changed edge product occurs. At an endpoint i, a derivative difference equals 4 a_i/Q times a nonzero signed sum of neighbor magnitudes with coefficients 0 or ±1. Distinct subset sums prevent cancellation. With minimum amplitude 4 and subset gap 1,

\[
\Delta=\min_{[x]\ne[y]}\|d_x^*-d_y^*\|_\infty\ \ge\ \frac{16}{500}=\frac4{125}.
\]

This supplies a direct positive margin without the previous powers-of-two stock range 4^14. It does not claim that the mathematical profile can be prepared natively.

## 3. EXACT: finite-family optimization and full separation

The declared search family consists of four distinct positive integer magnitudes from 1 through 32 with largest/smallest ratio at most 2. The objective is the **local lower bound** 4 m delta_sub/Q, where m is the smallest magnitude and delta_sub is the minimum subset-sum gap. Repeated subset sums exclude a profile from this certificate family. This exclusion does not prove global derivative non-identifiability.

For each unordered weight set, placing its largest magnitude on color 0 minimizes Q, because color 0 occurs three times and the other colors four times. Other permutations cannot improve this lower-bound objective. The replay tests 4,200 sets, of which 3,640 have distinct subset sums. The maximum bound is 4/125, attained by (4,5,6,8) and its integer multiples up to the search limit. These multiples give the same normalized stock profile. This is a finite-family optimum of a sufficient bound, not an optimum of actual separation, all real profiles, or all encodings.

An independent exhaustive integer comparison of every pair of 16,384 global-sign-fixed rays gives

\[
\boxed{\Delta=\frac{40}{500}=\frac2{25}}.
\]

The receipt preserves a closest pair, the two sign rays and their nominal derivative vectors. Diagonal pairs are excluded. Each unordered pair is covered (the implementation also checks the reverse order). It uses signed 64-bit integer operations at values far below overflow, not floating-point nearest-neighbor estimates. The local subset proof independently supplies the weaker lower bound, and the explicit closest pair supplies the sharp upper bound.

## 4. EXACT: stock and derivative uncertainty contract

Let true normalized stocks satisfy

\[
|\rho_i-\rho_i^*|\le u\rho_i^*,\qquad 0\le u<1,
\]

and true amplitudes be real with sign ray x. Then each true positive magnitude differs from its nominal value by at most relative u: sqrt(1−u)≥1−u and sqrt(1+u)≤1+u. Products differ by at most relative 2u+u². For the exact supplied generator,

\[
\|d_x(\rho)-d_x^*(\rho^*)\|_\infty
\le K(2u+u^2),\qquad
K=\max_i\frac{2a_i\sum_{j\sim i}a_j}{Q}=\frac{92}{125}.
\]

If a measured derivative vector y has error at most epsilon in infinity norm relative to the true derivative, nearest nominal sign-ray decoding is unique whenever

\[
\boxed{\epsilon+\frac{92}{125}(2u+u^2)<\frac1{25}}.
\]

Proof: y is within epsilon+K(2u+u²) of the correct nominal signature. Every incorrect signature is at least Delta minus that radius away. A radius strictly below Delta/2 separates them. At equality no uniqueness guarantee follows. This proves recovery of the sign ray. Actual current magnitudes remain uncertain; nominal currents have edgewise product-error bound (2u+u²)|j_e*|.

For u=1/100 and epsilon=1/50, the total error bound is

\[
\frac{10873}{312500}<\frac1{25},\qquad
\text{slack}=\frac{1627}{312500}.
\]

Thus a 1% relative stock allocation and 1/50 absolute derivative allocation satisfy the declared mathematical decoding test. Percent refers only to the relative stock interval. Derivative error has generator-time units; it is not a 2% sensor claim. The first conservative allocation u=1/1000, epsilon=1/100 also passes the local lower-bound test with half-margin 2/125.

All inequalities concern worst-case admitted errors, not Gaussian error models. They presuppose the exact generator, all address derivatives, known address correspondence, real amplitudes, and the retained instantaneous law. Unknown generator coefficients, derivative-estimation bias beyond epsilon, missing addresses, uncertain units, and complex phases require separate error contracts. No physical readout accuracy is asserted.

## 5. EXACT: compare derivative-only and tree-current observation routes

With signed current probes, all positive equal stocks rho=1/15 yield tree edge magnitude 2/15. Any spanning tree then reconstructs the real sign ray if its additive current error is strictly less than (1−u)2/15 under the same relative stock interval. This sign recovery does not require exact magnitudes; numerical current recovery does.

For the selected derivative profile, a maximum-bottleneck spanning tree has nominal minimum current 12/125. Descending Kruskal constructs the tree. A cut witness shows that the graph with only edges strictly above this value is disconnected, proving optimality for this fixed profile. Its sign tolerance is correspondingly (1−u)12/125.

| Observation route | Profile | Certified nominal discrimination | Limitation |
|---|---|---|---|
| All 15 stock derivatives | Equal stocks | Zero global sign-ray separation | Explicit collisions remain |
| All 15 stock derivatives | Four-class 4:1 profile | Exact pair separation 2/25 | Generator and real-state law supplied |
| 14 signed tree currents | Equal stocks | Sign threshold 2/15 | Current-sensitive probes must exist |
| 14 signed tree currents | Four-class 4:1 profile | Optimal tree sign threshold 12/125 | Weaker tree tolerance than equal stocks |

The current thresholds and derivative signature separation refer to different observables; they are not interchangeable tolerances. Equal stocks favor tree-current sign sensing, while the four-class profile removes the derivative-only degeneracy. Probe realizability decides which design matters.

## 6. Reproduction, dispositions and next action

Run `python3 replay.py` from the unpacked release directory with NumPy available. The replay performs 15 grouped exact checks: XOR labeling, multiplicities, finite optimum, complete signature uniqueness, all-pair integer separation, independent local bound, two uncertainty budgets, optimal tree/cut witnesses, and equal-stock negative control. No physical dataset is used. The finite search is exploratory design work; all 16,384 rays are exhaustively tested, with no held-out empirical validation claim.

**Closed within scope:** a useful bounded-range real-stock profile, a sharp finite separation certificate, and a combined stock/readout error inequality. **Narrowed:** robust transport inference under a supplied generator. **Open:** physical stock/readout channels, native preparation, generator defects, complex receipt recovery, and independent review. Physical promotion remains 0.

Recommended next action: extend the frozen inference contract to a source-bound non-unit generator perturbation and partial observations, using rank/counterexample tests before proposing apparatus. Priority judgment 91/100. This removes the exact-generator and complete-observation dependencies without inventing measurement capability.

`Gap2_FINAL_Finite_Genesis.png` remains unavailable and excluded; please retry its upload if needed.
