# Calibration preparation and receipt packet v0.1

21 October2026 America/Chicago. PROPOSED / UNEXECUTED. Constructor checks only; independent review pending. Development —no registry entry. Physical promotion0; EXIT-03 HOLD.

## Delivered

PROTOCOL.md specifies a reference-chain preparation, timing and spectral-tail feasibility gates, voltage acquisition calibration, binding and independent review handoff. BOUND_TEMPLATES.json provides twelve blank bound records with requirements separate from measured values. REVIEW_TEMPLATE.json and METHOD_WITNESS_TEMPLATE.json are deliberately incomplete and marked pending. None is a calibration result or approved receipt.

THEOREM.md supplies a conditional finite-mode leakage witness: K orthogonal tail modes, coefficient-error bound epsilon and outside-model TV bound T_out imply T_tail<=sqrt(K)(r_meas+epsilon)+T_out. Its frozen illustrative100-mode allocation needs60microvolt finite-mode complex RMS,20microvolt total coefficient error and200microvolt independently bounded outside-model TV to reach1millivolt tail TV. Projected outside-model contamination belongs in coefficient error; because the outside-model TV share exceeds the error share, isolation or a sharper projection argument is essential. The theorem does not manufacture that evidence.

## Quantified feasibility

| Item | Exact condition / result |
|---|---|
| Timing budget | Four50ps shares sum to0.2ns |
| Drift model over16183/1953125s | Fractional error<=1953125/(20000000000*16183), about6.03ppb |
| Reference envelope | Carrier±25Hz and center, magnitudes1/16,3/4,1/16V |
| Reference in-band TV | 7/8V |
| Full-reference amplitude floor with1/1000V tail | 78/125V=0.624V |
| Generic mathematical timing frontier with other shares fixed | Approximately2.08868ns |
|1ns timing alternative | Total error≈0.00920693V; within joint sufficient cap, but fails current0.2ns per-role admission |

The timing alternative is explanatory engineering feasibility under the same slope and other-share assumptions. It does not replace the frozen contract or relax an evidence gate after measurement. The prepared reference is a proposed calibration signal; source command settings alone are insufficient. A calibrated reference chain cannot establish that a nonlinear simulator output remains in this source class.

## Checks and disposition

Run `PYTHONDONTWRITEBYTECODE=1 python3 build_and_verify.py`. It regenerates the blank templates, verifies exact timing sums, drift, source TV/amplitude floor, finite-mode bound and alternative timing arithmetic. It also inserts a null bound into each corresponding otherwise complete synthetic packet and confirms all twelve return HOLD. These are constructor arithmetic/software controls, not physical measurements or independent review.

The admission checker and circuit candidate remain unchanged. The previous unresolved apparatus profile and twelve missing reviewed calibration/source roles still prevent readiness. Same-output FFTs, sample-rate metadata, typical jitter or RMS noise values alone cannot supply the required deterministic certificates. A real preparation needs a new resolved apparatus/run profile and independent applicable evidence.

No raw data were reacquired, no hardware/software was operated on instruments, no equipment was recommended/purchased and no author was contacted. Previous2/6 and0/891 results are preserved. The attached v0.39 ledger remains historical context and the CRL-2 document a proposal; Gap2_FINAL_Finite_Genesis.png remains unavailable and unused.

## Next

The immediate review question is feasibility of independently bounding the source residual and clock/path errors. Next derive a frequency-offset/Gram-matrix extension of the finite-mode witness so monitor clock error and off-grid modes have explicit tolerances instead of assuming exact orthogonality. Keep the original witness as a scoped special case. Full energy, native support, primitive state clock, action anchor and EXIT-03 stay open.

A. CURRENT MISSION TRAJECTORY — Complete reviewable prerequisites up to physical experimentation.

B. WHAT WAS DONE — Calibration/preparation protocol, twelve blank bounds, review/witness templates and conditional finite-mode theorem.

C. FINDING — Timing and source-model completeness remain practical evidence bottlenecks; arithmetic alone does not admit a run.

D. UD GAP IMPACT — Experiment requirements are concrete, unexecuted and independently reviewable. Physical promotion0.
