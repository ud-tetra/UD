# Joined J₁ frequency/damping certificate

The new two-input evaluator passes the declared complex absolute error target 0.1 on the full rectangle

\[
\omega\in[4.4915,4.524125],\qquad\gamma\in[0.1,0.1005].
\]

Under the declared IEEE binary64 round-to-nearest, ties-to-even operation model, its uniform continuum-plus-evaluation error is **less than 0.099503**. This extends the previous fixed-damping result into a two-parameter region, with no reduction of frequency coverage. It reuses both saved P2 states and their flux/local-lift certificates. There is no new mesh solve or flux fit in this capture.

## Exact residual extension

The frozen centers are \((\omega_c,\gamma_c)=(9/2,1/10)\) and \((289/64,1/10)\). Both states are in the same meanfree conforming P2 space on 12,288 tetrahedra, with 18,673 degrees of freedom. The domain, normalized measure, source \(F=10(x+y)\), gradient metric and homogeneous Neumann condition are unchanged. The source and damping are externally declared benchmark data.

Write \(z=-\omega^2+2i\gamma\omega\), \(z_c=-\omega_c^2+2i\gamma_c\omega_c\). For either frozen exact trial state \(v_c\), the corrected family is

\[
J_z(v_c)=J_{z_c}(v_c)-(z-z_c)\int_\Omega v_c^2\,d\mu.
\]

The mass here is **bilinear**. The residual perturbation uses the separate Hermitian mass \(\|v_c\|_{L^2}^2\). With the existing exact flux defect \(d_c^2\), local volume-lift budget \(\nu_c^2\), and continuum Poincaré bound \(C_P\le1/2\),

\[
\|r_z\|_{V'}\le R_c+\tfrac12|z-z_c|\|v_c\|_{L^2},\qquad R_c=\sqrt{d_c^2}+\sqrt{\nu_c^2}.
\]

The corrected-output identity applies to arbitrary frozen meanfree trials, so it requires no exact Galerkin solve assumption. The inherited rotated-coercivity/residual bound gives

\[
|H_z-J_z(v_c)|\le\kappa(\omega,\gamma)\|r_z\|_{V'}^2,
\quad \kappa(\omega,\gamma)=\sqrt{1+\left(\frac{\omega}{2\gamma}\right)^2}.
\]

Each leaf has \(\rho=17/2000\), \(\omega\in[\omega_c-\rho,\omega_c+\rho]\), and the common damping interval. Let \(g_+=201/2000\). Positivity and \(g_+\ge\gamma_c\) yield

\[
|\omega^2-\omega_c^2|\le\rho(2\omega_c+\rho),\qquad
2|\gamma\omega-\gamma_c\omega_c|\le2\big[g_+(\omega_c+\rho)-\gamma_c\omega_c\big].
\]

The absolute maxima of both components occur together at the upper corner. Their squared sum bounds \(|z-z_c|^2\) on the entire continuous rectangle. Also \(\kappa\le\sqrt{1+[(\omega_c+\rho)/(2\gamma_c)]^2}\). All quantities are exact rationals with square roots rounded upward by verified integer arithmetic. The evaluator error is added afterward.

| Frozen leaf | Frequency interval | Damping interval | Combined radius, outward rounded | Uniform evaluator contribution, outward rounded |
| --- | --- | --- | --- | --- |
| Original | [4.4915, 4.5085] | [0.1, 0.1005] | <0.099503 | <7.808×10⁻¹⁶ |
| Neighbor | [4.507125, 4.524125] | [0.1, 0.1005] | <0.093735 | <6.957×10⁻¹⁶ |

`RECTANGLE_RESULTS.json` retains exact rational budgets, not only these displayed decimals. Increasing the damping upper endpoint to 0.101 makes the original leaf's same sufficient envelope exceed 0.1 (about 0.100327). That is a failure of this conservative certificate, not a lower bound on actual error or a physical NO-GO.

## Actual two-input floating evaluator

`evaluator.py` accepts two finite native floats. Each represents its exact binary64 value. Exact rational guards reject values outside the certified domain, and reject integers, booleans, strings, NaNs and infinities.

For each leaf, the frozen seven coefficient words are nearest binary64 representations of exact rational constants. In particular, the stored `GAMMA0` is not exactly 1/10. Its quantization error is included. Passing `float(0.1)` means its represented value, slightly greater than rational 1/10; it is not asserted to be the old exact fixed damping parameter. The previous one-input fixed-damping evaluator and its evidence remain unchanged.

Sixteen explicit scalar operations evaluate the identity. The damping shift is factored as

\[
2(\gamma\omega-\gamma_c\omega_c)
=2\{\gamma(\omega-\omega_c)+\omega_c(\gamma-\gamma_c)\}.
\]

The exact-rational interval/error recurrence propagates constant quantization and each primitive rounding. It uses \(|\mathrm{RN}(x)-x|\le2^{-53}|x|+2^{-1075}\), includes subnormal underflow, rounds bounds upward on a rational grid, and excludes overflow by propagated magnitudes less than 16. The source AST is checked against all sixteen nodes, the complex output extraction and the exact selector. This is conditional on the stated primitive IEEE semantics and no FMA/contraction, not a formal verification of every Python/platform implementation.

The uniform proof covers **1,323,427,226,638,286,793,890,492,324 accepted binary64 input pairs**. The frequency count is 36,732,484,460,741 and the damping count is 36,028,797,018,964. These pairs were not brute-force enumerated. Word endpoints, binade spacings and the Cartesian-product count are proved exactly.

Supplemental constructor checks cover 4,488 input-pair traces and 71,808 intermediate native/software-oracle comparisons, all passing. Every sampled ideal trace also matches the independently expanded closed corrected estimator. Integer-only RN controls exercise ties and subnormals. Domain, wrong-leaf, quantization, output-corruption, wider-box and selector-containment controls pass. The saved read-only replay reproduces the exact JSON.

## Join over the full damping interval

The original leaf is selected iff the exact represented frequency is at most \(577/128=4.5078125\); otherwise the neighbor is selected. Both accept the unchanged damping input. The switch lies inside the overlap \([4.507125,4.5085]\), of width \(11/8000\), for every damping in the common interval.

The exact consecutive word partition covers the joined frequency range without a gap. Taking its Cartesian product with the common damping domain covers every accepted pair. The selector adds no numerical output arithmetic. Thus the joined error bound is the maximum leaf radius. The selected approximate output is piecewise; continuity or differentiability across the switch is not claimed, and no blending is performed.

## Evidence and review boundary

Generated: new frozen two-input evaluator, coefficient witness, rectangle proof/audit, results, contract and report. Checked: dependency SHA/size pins, exact parameter perturbation, all-input rounding recurrence, native trace/identity controls, domain census, selector coverage and saved read-only replay. Captured: unique append-only directory with manifest/event plus persisted Project gate receipt and screenshot. GitHub PR/CI/merge receipts are posted separately after publication; this report does not predeclare a merge.

The prior saved state/flux results are reused by hashed dependency; they were not regenerated here. Source contracts and previous read-only replay receipts remain in their original captures. The audit command is `PYTHONDONTWRITEBYTECODE=1 python3 audit.py` from this directory. It verifies frozen dependencies and compares with saved results without rewriting them.

Project remains **In review / Scientific OPEN / Constructor checked / Development**. The next gate is an independently reviewed certificate and a damping-shifted state to widen the region. Full [0,6]×[0.1,1] precision, quantitative mesh termination and the native UD action/source/damping/metric bridge remain open. No physical Hertz calibration, input parsing/measurement uncertainty guarantee, native constitutive law, material/horn identification or GR/QFT equivalence follows.

The coefficient provenance ledger v0.39 is not a derivation of the declared benchmark dynamics. CRL2 subdivision v1.0 remains a governance proposal, not enacted by citation. `Gap2_FINAL_Finite_Genesis.png` is unavailable and was not read. This is a Development artifact with no authoritative registry entry; independent review is absent and **physical promotion=0**.

**A. CURRENT MISSION TRAJECTORY —** Extend certified J₁ continuum output coverage in frequency and damping.

**B. WHAT WAS DONE —** Reused two frozen states/flux budgets; built and replayed the two-input evaluator and exact rectangle join; updated the Project gate.

**C. FINDING —** The full rectangle [4.4915,4.524125]×[0.1,0.1005] passes with combined radius <0.099503 under declared IEEE binary64 RN semantics.

**D. UD GAP IMPACT —** Benchmark certification advances. Independent review, full-band closure, finite mesh termination and the native UD bridge remain OPEN. Physical promotion=0.

**NEXT —** Construct a damping-shifted certified state and join its rectangle; obtain non-constructor review.
