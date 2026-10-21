# Continuous-band quadrature requirements and certificate v0.1

21 October 2026. DERIVED / EXACT CONDITIONAL, constructor checked. Independent review pending. Development — no registry entry. Physical promotion0; EXIT-03 HOLD.

## Outcome

The unchanged saved local-quadrature kernel satisfies an explicit **conditional narrow-band measurement budget**. Exact rational comparisons, directed interval trigonometric enclosures and an analytic Taylor remainder cover every envelope frequency within±50 Hz. No sampled-grid extrapolation is used. No experimental data are reanalyzed and no source or instrument premise is claimed measured.

| Proposed requirement | Value / disposition |
|---|---|
| Envelope spectral support relative to fixed carrier | [-50,50] Hz |
| Complex spectral-measure total variation | <=1 V |
| True envelope magnitude at phase-reported centers | >=1/2 V |
| Total input error: noise+gain+timing+baseline variation | <=1/2000 V; uncalibrated requirement |
| Constant baseline magnitude | <=3 V |
| Availability-delay cap | 3/5000 s |
| Absolute complex error target | 1/100 V |
| Phase error target | 1/50 rad |

The source class is a design choice frozen before certificate execution; it is not inferred from the previous simulator file. It can exclude the faster synthetic modulation and pulse cases. A compact spectral support with a total-variation cap is stronger than merely seeing a spectral peak or asserting an envelope RMS bandwidth.

## Certified conditional bounds

| Quantity | Outward explanatory bound |
|---|---:|
| Continuous-band transfer error, unit total variation | <0.004515 V |
| Input-error output contribution | <0.001274 V |
| Total complex error including baseline leakage and numerical allowance | <0.005788 V |
| Phase bound at admitted amplitudes | <0.011693 rad |
| Exact availability delay | 1024/1953125 s =524.288 microseconds |

CERTIFICATE.json supplies authoritative exact fractions; printed approximations are not interval endpoints. The theorem uses H0≈2.546478 and H2≈9.147976e-8 s², obtained with conservative |Re h|+|Im h| magnitude bounds. H0 therefore differs from the tighter floating Euclidean-magnitude sum≈2 in the preceding manuscript; these are different bounds on the same unchanged kernel, not a correction or re-fit.

The conditional serial-evaluation rounding bound is compared against2^-30 V. It assumes round-to-nearest binary64, no overflow and input magnitudes<=5 V. This algorithm-specific budget is not an actual all-platform audit of NumPy or an instrument runtime. Geometric phase error is certified; floating atan2/demodulation evaluation is not included as a separately executed implementation.

## Adversarial controls

The interval response at600 Hz yields a unit-tone complex error lower bound above0.2305, establishing failure of the unchanged kernel's1% target there. This is an actual specified-tone lower bound, not just failure of a sufficient upper certificate.

An input-error allowance of1/100 V fails the sufficient budget; this does not say every such noise realization fails. An exact delay cap1/2000 s rejects the unchanged kernel's1024/fs delay. No design parameter or coefficient is changed after these results.

## Reproduce and provenance

Run `python3 certify.py` from this capture in the repository; standard Python only. The script reads the prior immutable KERNEL.csv, hashes it and the frozen CONTRACT.json, then interprets stored coefficient values as exact binary64 dyadics. It recomputes Machin pi intervals, sine/cosine remainder bounds, interval phase powers, moments, derivative bounds, serial floating allowance and positive/negative gates. No source archive code is executed.

Kernel SHA-256:5beebe40fa2bfe744a0a64ee57401e77334b925bf0a23c0d2f24cafcd60ff254. THEOREM.md supplies the assumptions, formulas and proof. Scope is a saved finite kernel and declared source class. Constructor verification is not independent review or CRL promotion.

The previously supplied v0.39 ledger remains historical context; the recovered v0.85 ledger is not replaced. CRL-2 subdivision remains a proposal. Gap2_FINAL_Finite_Genesis.png is unavailable and unused. No previous capture is superseded:2/6 synthetic outcomes and0/891 empirical gate result remain intact.

## Experiment-facing next gate

Acquire evidence for the declared source class and combined1/2000 V input-error ceiling before applying this certificate physically. Required budget records should separately expose additive noise, relative gain times voltage scale, timing skew times a voltage-derivative bound, nonconstant baseline and out-of-class spectral leakage. If the compact-band premise cannot be supported, extend the theorem with an independently bounded out-of-band total variation rather than deleting the tails through filtering.

Next derive a leakage-tolerant source contract and allocate the remaining error margin between spectral tails and instrument uncertainty. A finite trace cannot by itself establish unrestricted global compact spectral support. No action or native support number follows from the present filter certificate; full energy/baseline, absolute apparatus-to-native map, signed primitive clock and EXIT-03 remain OPEN/HOLD.

A. CURRENT MISSION TRAJECTORY — Turn signed reconstruction into reviewable measurement requirements.

B. WHAT WAS DONE — Frozen source/uncertainty/delay contract; continuous-band theorem; exact rational interval certificate and negative controls.

C. FINDING — The unchanged kernel meets the proposed±50 Hz budget conditionally; it demonstrably fails unit-tone1% recovery at600 Hz.

D. UD GAP IMPACT — Mathematical measurement interface sharpened. Empirical input/source gates and independent review remain open; physical promotion0.
