# Boundary treatment and omitted-band benchmark v0.1

21 October 2026. NUMERICAL SYNTHETIC / DERIVED CONDITIONAL. Development — no registry entry. Constructor checks only; independent review pending. Physical promotion = 0. EXIT-03 HOLD.

## Result

No tested boundary treatment recovers every injected signal. Of six cases, periodic projection passes 2, zero padding 4, reflection padding 4 and Hann taper/division 4. All four fail the narrow-pulse and omitted-sideband full-state diagnostics. There is no empirical rerun, replacement gate, selected winner or action estimate in this milestone. The previous signed-reconstruction contract's **0/891** composite result remains intact.

The benchmark separates two failure mechanisms in known synthetic controls: nonperiodic boundary mismatch and genuine content outside the retained carrier band. It does **not** determine their relative contributions in the experimental traces. The four treatments are candidate signal-processing choices, not physical continuations.

## Frozen setup

CONTRACT.json and benchmark.py were written before execution. The six explicit generators, four methods and metrics are fixed in those files, with no search or post-result adjustment. This is constructor-frozen analysis, not independently reviewed preregistration. The supplied v0.39 ledger is historical context; it does not replace the previously recovered v0.85 source. The supplied CRL-2 subdivision document remains a governance proposal. Nothing is promoted by citation.

Use N=16184 samples, fs=1953125 Hz, trigger-relative t_j=j/fs, carrier fc=257 fs/N=31015.39328966881 Hz and retained half-bandwidth 5000 Hz. Noninteger cases use fc+(37/100)fs/N. All generators have initial phase 73/100 rad. Interior evaluation discards 1024 samples at each end. A synthetic diagnostic passes if complex relative RMS error <=1/100 and maximum phase error <=1/50 rad at points whose true amplitude is at least 1/5 V. These ground-truth-based thresholds differ from v0.1's empirical residual gate; their pass rates must not be compared as if they were the same test.

All methods first subtract the original voltage-record mean, then double retained positive-frequency DFT bins and discard all other bins. Periodic uses the original record. Zero and reflection padding append one original record length on both sides; reflection excludes endpoint replication. Hann uses the original symmetric taper and divides the complex output by its taper only at nonzero-weight points; metrics use the fixed interior, not the endpoints. No carrier fitting, decimation or empirical calibration occurs.

Let P(a,f,p)=a exp(i(2 pi f t+0.73+p)). Synthetic real observations are the real part of the following explicit complex phasors:

| Case | Full injected reference |
|---|---|
| exact_bin | P(1,fc,0) |
| off_bin | P(1,f_off,0) |
| smooth_AM_PM | P(1+0.2 cos(2 pi 600 t), f_off, 0.15 sin(2 pi 200 t)) |
| smooth_turnon | P(0.1+0.45[1+tanh((t-0.001)/0.0002)], f_off,0) |
| narrow_pulse | P(0.05+exp(-((t-0.004)/0.00012)^2),f_off,0) |
| omitted_sideband | P(1,f_off,0)+P(0.3,f_off+12000,0) |

For smooth transients these phasors are declared generative references, not a claim that finite-record or infinite-line analytic transforms equal them exactly. The sideband case separately reports error to its fundamental-only target. Removing a sideband can improve fundamental extraction while failing full-state recovery; those are distinct objectives.

## Results: complex relative RMS error on fixed interior

| Case | Periodic | Zero pad | Reflect pad | Hann/divide |
|---|---:|---:|---:|---:|
| Exact bin | 5.83e-14 | 0.003822 | 0.004897 | 3.00e-7 |
| Off bin | 0.009294 | 0.005652 | 0.004530 | 2.99e-5 |
| Smooth AM/PM | 0.010865 | 0.006702 | 0.005559 | 3.53e-5 |
| Smooth turn-on | 0.005640 | 0.003784 | 0.001692 | 2.18e-5 |
| Narrow pulse | 0.011585 | 0.011194 | 0.011291 | 0.022994 |
| Omitted sideband, full truth | 0.287532 | 0.287424 | 0.287431 | 0.287377 |
| Omitted sideband, fundamental only | 0.009303 | 0.005685 | 0.004521 | 2.97e-5 |

Phase also matters: periodic turn-on fails its phase threshold (0.05813 rad) even though its RMS error is below 1/100. Complete amplitude/phase metrics and eligible counts are retained in METRICS.csv and RESULTS.json. Hann strongly improves these smooth-signal cases but roughly doubles the pulse RMS error compared with the other methods. No uniform dominance follows from this finite bank.

## Explicit boundary uncertainty bound

This is a standard finite-dimensional linear-filter statement, recorded with its exact scope, not a new UD physical theorem. For a fixed padded length L, retained positive bin set B and inverse-DFT convention 1/L, define

    k_r = (2/L) sum_{b in B} exp(2 pi i b r/L).

The reconstructed complex signal on input x is (k*x)_j. For two extensions x and x+e that agree on the measured segment and satisfy |e_l|<=epsilon_l outside it,

    |Delta z_j| <= sum_{l outside} |k_{j-l}| epsilon_l.

If epsilon_l<=epsilon uniformly, the bound is epsilon times the outside-row absolute sum. Cauchy–Schwarz and DFT orthogonality also give

    |Delta z_j| <= 2 sqrt(|B|/L) ||e||_2.

Proof: expand the convolution difference and apply the triangle inequality; orthogonality gives sum_r|k_r|²=4|B|/L, then Cauchy–Schwarz. Both are exact conditional statements in real arithmetic; evaluated constants below are numerical, not outward-rounded interval enclosures.

For L=48552 and the frozen band, |B|=249 and row l2 norm is approximately 0.1432274. The outside-row absolute sum over the fixed interior ranges approximately 1.06749–1.64220. A unit voltage-sample impulse just outside the measured segment produces maximum interior complex effect approximately 0.00059509 V, despite the 1024-sample guard. The FFT convolution equals the explicitly shifted kernel to 3.88e-18 maximum error. A nonzero coefficient supplies a direct counterexample to “the guard removes all boundary influence”; scaling that impulse precludes a finite uniform continuation-error bound without some amplitude, norm or source restriction.

These bounds apply to extension differences at the same length/filter. The Hann method changes the operator and requires its own error analysis, including division amplification. They are not a bound on unknown infinite-time dynamics or an experimental gain/skew certificate.

Given a separately justified total complex error budget d_j against a specified reference and estimate zhat_j with |zhat_j|>d_j, elementary disk geometry yields phase error <=asin(d_j/|zhat_j|). The reverse triangle inequality yields amplitude error <=d_j and squared-amplitude error <=d_j(2|zhat_j|+d_j). A physical use must include continuation, omitted-band/model, noise, gain, timing and numerical contributions without double-counting. This milestone bounds none of those unknown physical inputs merely by choosing padding.

## Verification and next gate

Run `python3 benchmark.py` with Python 3 and NumPy. Assertions cover exact-bin recovery, preservation of the injected omitted-band full-state failure, the explicit kernel identity, an l2 impulse bound and nonzero guarded boundary influence. There are 24 method/case evaluations. The primary waveforms are generated locally; no imported scripts or notebooks execute. No experimental data are analyzed anew and no independent review is claimed.

Next construct a finite-support quadrature estimator with a fixed demodulation kernel and explicit transfer response. A valid interior estimate should depend only on measured samples, while source assumptions and omitted-band uncertainty remain visible. Freeze its filter, delay, evaluation window and synthetic calibration bank before any experimental rerun. This can remove assumed padded samples from the estimator, but cannot make a finite record identify unrestricted external physics. Gain/skew, total energy/baseline, absolute native support and EXIT-03 remain open.

A. CURRENT MISSION TRAJECTORY — Certify signed reconstruction before using phase or action observables.

B. WHAT WAS DONE — Frozen six-case/four-method synthetic bank; full-state versus fundamental diagnostics; explicit finite-filter boundary bounds.

C. FINDING — Padding can reduce smooth-signal error, but cannot recover excluded content or eliminate continuation uncertainty by guard alone.

D. UD GAP IMPACT — Constructor-checked development only. No new action anchor, native clock, independent review or physical promotion.
