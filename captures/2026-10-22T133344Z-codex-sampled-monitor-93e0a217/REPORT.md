# Sampled complex-monitor leakage witness v0.1

22October2026 America/Chicago. PASS_EXACT_CONDITIONAL_SAMPLED_MONITOR. Constructor checked; independent review pending. Development —no registry entry; physical promotion0; EXIT-03 HOLD.

## Result

The leakage theorem now applies directly to a sampled complex monitor, rather than requiring a continuous-time RMS reconstruction. Exact sample-Gram bounds cover the declared timing/frequency family, and stored binary64 sample RMS is checked with exact rational arithmetic. All physical source/monitor premises remain proposed and unmeasured.

| Proposed monitor design | Bound/result |
|---|---:|
| Nominal complex samples |1024;1s cyclic grid span |
| Nominal finite modes |100–199Hz |
| Per-mode frequency uncertainty |±5mHz |
| Affine clock error / per-sample residual |10ppb /10ns |
| Sampled Gram eigenvalue lower bound |>0.9096 |
| Digital RMS ceiling / total sample error |55µV /20µV |
| Independent outside-model spectral TV |<=10µV |
| Conditional tail TV |<=0.00090675V |
| Propagated full-state error / phase |<0.008367V /<0.016903rad |

These independent-monitor timing and calibration requirements are distinct from the original acquisition's0.2ns timing and1/4000V input budget. No instrument capability is asserted, and no existing gate is silently relaxed.

## Direct contamination accounting

THEOREM.md proves

    T_tail<=sqrt(K/lambda_d)*(r_d+epsilon_d+T_out)+T_out.

The outside-model component is charged explicitly inside the raw total-tail sample norm and again in the full reference. The previous200µV outside-model allowance would give a3.10125mV sufficient bound for this direct route, so the new design tightens it to10µV. This is an additional prospective requirement, not evidence discovered in the published dataset. Prior isolated-monitor and coefficient-error theorems remain scoped to their own premises.

The conditional monitor error split is10µV acquisition/quantization,5µV quadrature calibration,3µV baseline and2µV numerical error. A matrix operator-norm uncertainty1/1000000 at vector magnitude<=5V supplies the quadrature share. Frequency response, loading, reference uncertainty and nonlinearity need applicable independent bounds; these values are not filled calibration receipts.

## What is checked

The source-family proof uses exact rational row sums and elementary sine inequalities, not a floating frequency grid. The certificate evaluates the stored contract, the sampled Gram bound and inherited fixed-kernel error budget. A1024-point synthetic fixture is serialized as canonical binary64 hex words, read back and checked by exact rational mean-squared complex norm. Numerical waveform generation is diagnostic only; it does not formally certify a physical finite-tone preparation.

The exact digital fixture check passes. Five corruptions return HOLD: one large sample, wrong sample count, nonfinite value, malformed encoding and a non-fixture designation. The reader is deliberately a software-control interface, not an empirical-admission service. Other controls reject the64-sample rank/alias case, excessive100µs time residual and the previous200µV direct-route outside budget.

A distinct-source alias counterexample is exact: modes100 and1124 have the same1024-point sample vectors. Opposite coefficients yield zero sampled signal with2V spectral TV. This demonstrates why a sampled witness still needs independently justified source completeness/outside bounds. It does not invalidate the declared100..199 non-aliasing family.

## Reproduce and limitations

Run `python3 certify.py` with standard Python. It regenerates SYNTHETIC_SAMPLES.json and CERTIFICATE.json, parses the fixture's exact words, checks digital norm and negative controls, and propagates the design tail ceiling through the previous leakage certificate. No downloaded archive code or experimental data executes. The reader's fixture-only guard prevents a software test result being presented as empirical admission.

The first-to-last nominal sample span is1023/1024s;1s is the cyclic design span used in the Fourier grid. Arbitrary epoch and common frequency shifts leave Gram eigenvalues invariant but do not certify absolute phase or physical band membership. Time-varying modes and nonlinear time warp are excluded unless separately covered by a justified new model/error bound.

The outside-TV cap, source stationarity/completeness, clock/time limits, independent complex reference, I/Q/path calibration and pre-RMS numerical error remain external evidence gates. Digital exactness alone closes none of them. The prior twelve-role evidence schema, circuit HOLD,2/6 and0/891 outcomes remain intact. The attached v0.39 ledger is historical and CRL-2 subdivision remains a proposal. Gap2_FINAL_Finite_Genesis.png is unavailable and unused.

## Next

Prepare a reference-monitor receipt contract that binds actual sample indices/timestamps, I/Q transfer calibration, source preparation, outside-model evidence and computation hashes. Integrate the sampled certificate as a derived tail bound in the evidence-admission graph, with explicit dependencies and no self-certification from the candidate estimator. Prioritize feasibility of the tightened10µV outside-model requirement. No further filter refinement can replace independent evidence for it.

A. CURRENT MISSION TRAJECTORY — Connect leakage assumptions to verifiable sampled-monitor records.

B. WHAT WAS DONE — Sampled-Gram theorem, direct outside contamination budget, quadrature allocation and exact digital-RMS fixture checks.

C. FINDING — Conditional sampled witness passes; aliasing and unverified outside-model content remain decisive limitations.

D. UD GAP IMPACT — Measurement computation is specified; independent physical calibration and source evidence remain open. Physical promotion0.
