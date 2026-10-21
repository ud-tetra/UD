# Measured-window quadrature estimator v0.1

21 October 2026. DERIVED CONDITIONAL / NUMERICAL SYNTHETIC. Development — no registry entry; independent review pending. Physical promotion 0; EXIT-03 HOLD.

## Result

A fixed local weighted least-squares estimator uses only measured voltage samples and rejects a constant local baseline. It has no padding or whole-record demeaning dependency. The frozen estimator passes **2/6** known synthetic recovery gates; it is not a generally successful replacement for the prior reconstruction. No experimental rerun occurs and the **0/891** empirical gate result remains unchanged.

The specific theorem and proof are in THEOREM.md. For local envelope Lipschitz bound L and sample error epsilon, the exact-real-arithmetic complex error is bounded by

    d = H1*L + H0*epsilon.

For the numerical frozen kernel, H0≈2.000000000043 and H1≈0.000311801908507 s. These are computed constants, not certified interval upper bounds; a deployed certificate must enclose numerical error and justify L/epsilon independently.

## Frozen apparatus-to-estimator contract

The sample rate fs=1953125 Hz and length N=16184 mirror the previously inspected circuit record format. They are design inputs here, not a new hardware calibration. Use a 2049-sample symmetric Hann window and the fixed carrier fc=257 fs/N≈31015.393289669 Hz. Weighted design columns are cos(omega k/fs), -sin(omega k/fs), and 1; the complex output combines the first two fitted coefficients. The third coefficient absorbs a constant baseline. KERNEL.csv preserves the numerical complex weights.

Valid center indices are 1024–15159 inclusive (14136 outputs). Every output uses exactly its full measured window. Real-time availability is delayed 1024/fs=0.000524288 s (524.288 microseconds); timestamps refer to window centers. There is no resampling, endpoint extrapolation, carrier refit or taper division. Carrier phase demodulation uses the same trigger-relative time convention.

CONTRACT.json and verify.py were written before execution. The six source generators reproduce the prior boundary-bank formulas explicitly, with no imported code execution. Synthetic acceptance is complex relative RMS <=1/100 AND maximum phase error <=1/50 rad where true amplitude>=1/5 V. This is a known-truth diagnostic, not the prior empirical residual gate, an independent preregistration or a hardware specification.

## Results

| Case | Complex relative RMS | Maximum eligible phase error (rad) | Gate |
|---|---:|---:|---|
| Exact carrier bin | 5.84e-14 | 1.99e-13 | PASS |
| Carrier offset 44.6525 Hz | 0.001413 | 1.66e-7 | PASS |
| Smooth amplitude/phase modulation | 0.033564 | 0.012016 | FAIL |
| Smooth turn-on | 0.025600 | 0.035221 | FAIL |
| Narrow pulse | 0.549315 | 0.034588 | FAIL |
| Omitted sideband, full truth | 0.287422 | 0.304735 | FAIL |

The omitted-sideband case's fundamental-only relative RMS is 0.001414; this does not recover the full injected state. The narrow pulse is strongly smoothed. The same window that removes exterior assumptions still imposes an amplitude/phase transfer response; locality does not imply broadband recovery.

For a pure tone offset from the carrier, the computed main response A and conjugate-image response B give relative error <=|A-1|+|B|:

| Offset (Hz) | Main response Re(A) | Image magnitude | Relative error bound |
|---|---:|---:|---:|
| 0 | 1 | 1.70e-16 | 1.06e-15 |
| 200 | 0.971956 | 6.65e-7 | 0.028045 |
| 600 | 0.769422 | 8.39e-7 | 0.230578 |
| 1000 | 0.463726 | 3.90e-7 | 0.536275 |
| 5000 | 0.001584 | 7.19e-7 | 0.998417 |
| 12000 | -0.000155 | 6.27e-7 | 1.000156 |

This is a discrete offset table, not a certified continuous passband. Even at 200 Hz, this window does not guarantee 1% amplitude recovery. No transfer correction or post-result window tuning is applied.

## Verification and limitations

Run `python3 verify.py` with Python 3 and NumPy. The design Gram matrix has numerical condition number≈2.000000319; moment residual is 4.44e-16. The exact finite-transfer formula agrees with direct convolution within 2.00e-13. A 2.7 V constant offset and four initial phases reconstruct within 2.23e-13 V. Injected bounded 0.005 V noise satisfies the conservative H0 epsilon≈0.01 V bound. All six declared analytic envelope-derivative bounds dominate observed complex errors within the explicitly used 1e-11 floating tolerance. The exact-carrier bound is zero in real arithmetic; its nonzero observed residual is numerical and is not hidden by claiming a rigorous floating certificate.

The Lipschitz bounds are known from synthetic generators only. For example, amplitude/phase modulation uses L<=0.2*2pi*600+1.2*(2pi*44.6525+0.15*2pi*200); narrow pulse uses sqrt(2/e)/0.00012+1.05*2pi*44.6525. These conservative bounds can be loose. No experimental estimate of L or epsilon is inferred from the estimator's own output.

Source context: the attached 235-object v0.39 ledger remains historical; it does not replace the recovered v0.85 ledger. The CRL-2 subdivision document remains a proposal; constructor work is not independent promotion. The unavailable Gap2_FINAL_Finite_Genesis.png is unused. The concurrent J1 scalar-wave track is retained without importing its calibration claims.

## Next gate

Prospectively specify a source-class-aware filter design problem: declared envelope bandwidth/regularity, noise and gain/skew bounds, allowed delay, passband distortion and image rejection. Audit whether one fixed measured-window kernel can meet that joint budget, using an analytic or certified continuous-frequency response rather than a few offsets alone. Preserve this estimator and its 2/6 result. No empirical rerun should be treated as a physical phase certificate until source and input bounds are independently supported. Full energy/baseline, native support, action anchor and EXIT-03 remain open.

A. CURRENT MISSION TRAJECTORY — Bound signed local reconstruction before phase/action inference.

B. WHAT WAS DONE — Frozen measured-window estimator, theorem manuscript, kernel, transfer identity and synthetic tests.

C. FINDING — Exterior-sample dependency is removed, but the chosen window smooths dynamic envelopes and passes only2/6 cases.

D. UD GAP IMPACT — A conditional error-budget interface is explicit; physical input bounds and independent review remain open. Physical promotion0.
