# Leakage and instrument allocation v0.1

21 October2026. PASS_EXACT_CONDITIONAL_LEAKAGE_BUDGET. Constructor checked; independent review pending. Development —no registry entry. Physical promotion0; EXIT-03 HOLD.

## Result

The full-state quadrature theorem now admits bounded spectral tails. With in-band envelope TV<=1 V within±50 Hz, tail spectral-measure TV<=1/1000 V and total input error<=1/4000 V, the unchanged kernel satisfies:

| Quantity | Outward bound / exact value |
|---|---:|
| Full complex error | <0.008698 V |
| Phase error at true full-envelope amplitude>=1/2 V | <0.017571 rad |
| Unallocated output-error margin to the joint sufficient cap | >0.001202 V |
| Availability delay | 1024/1953125 s =524.288 microseconds |

The joint sufficient cap is99/10000 V (phase certificate), slightly tighter than the absolute1/100 V target. Phase target remains1/50 rad; delay cap remains3/5000 s. These are conditional mathematical requirements, not experimental measurements. No raw dataset is reanalyzed; prior2/6 and0/891 outcomes stay intact.

## New theorem and exact frontier

For kernel norm bound H, certified in-band transfer error R, constant-baseline leakage C0 and evaluation allowance E_fp,

    d_full <= R+(H+1)T+H epsilon+3 C0+E_fp.

The tail coefficient H+1 accounts for the filtered tail response and the missing tail in the full reference. Using H alone would change the target to the in-band component. THEOREM.md states and proves both contracts separately.

The inherited rational transfer upper bounds are rounded upward to denominator10^12 before exact calculations. H≈2.546477684438, R≈0.004514533315, and E_fp=2^-30 V. This certificate reuses the unchanged dyadic kernel and inherited continuous-band proof; it is not an independent reconstruction of that proof. Certificate hashes bind the dependency.

At frozen epsilon=1/4000 V, the sufficient tail ceiling is approximately0.001339031781 V. At frozen T=1/1000 V, the sufficient input ceiling is approximately0.000722169323 V. These one-coordinate ceilings cannot both be increased simultaneously: they are points on the same linear budget frontier. Exact fractions in CERTIFICATE.json carry the authoritative thresholds. Frontier equality and points just beyond it are checked exactly.

## Instrument-facing allocation

| Input contribution | Required ceiling | Sufficient supporting requirement |
|---|---:|---|
| Additive noise and quantization | 1/10000 V | Independent acquisition/error bound |
| Gain contribution | 1/20000 V | Relative gain error<=1/100000 at magnitude<=5 V |
| Timing contribution | 1/20000 V | Time error<=1/5000000000 s with clean slope<=250000 V/s |
| Nonconstant baseline | 1/20000 V | Independent residual-baseline bound |
| Total | 1/4000 V | Worst-case sum; no cancellation assumed |

The timing number is0.2 ns. It is an illustrative demanding design requirement, not a statement about the circuit acquisition's actual skew. An additional physical tail-frequency limit200000 Hz and the declared tail-TV cap imply a clean-signal slope below196526 V/s for this allocation. Time errors must be bounded over the displaced sampling interval; sample-index metadata alone does not establish that.

The full clean signal plus constant baseline and allowed errors has magnitude below5 V, matching the inherited serial binary64 evaluation premise. The floating allowance remains algorithm-specific; no new all-platform or numerical atan2/demodulation receipt is claimed.

## Negative controls and independent evidence

Tail TV1/500 V fails the sufficient joint budget at the frozen input error. Input error1/1000 V also fails it at the frozen tail allowance. Neither failure proves every corresponding waveform or error realization fails. The prior600 Hz unit-tone lower failure bound remains a separate, stronger specified-signal result.

A finite-record identifiability argument shows why the tail cap cannot be certified from the same samples without independent restrictions: sufficiently many distinct tail tones admit a nonzero combination vanishing at all finite sample times, with arbitrarily scalable spectral variation. Filtering or taking an output FFT does not close this gap.

## Reproduce and proceed

Run `python3 certify.py` with standard Python in the repository. It reads and hashes the immutable prior certificate/kernel, performs upward rational rounding, checks the full-state budget, allocation sum, gain/time products, conditional source slope, voltage envelope, exact frontier and negative controls. No imported scripts execute and no experimental data are used. The supplied v0.39 ledger remains historical context; the CRL-2 subdivision document remains a proposal. Gap2_FINAL_Finite_Genesis.png is unavailable and unused.

Next prepare an independent-evidence checklist and a fail-closed admission schema for source leakage, gain, noise, timing and baseline certificates. Missing, circular, mismatched-unit or same-output-derived bounds must return HOLD. This will turn the theorem assumptions into reviewable experiment prerequisites without pretending that metadata alone closes them. Full energy, absolute native support, primitive clock, action anchor and EXIT-03 remain open.

A. CURRENT MISSION TRAJECTORY — Make signed reconstruction assumptions instrument-facing and auditable.

B. WHAT WAS DONE — Leakage-tolerant full-state theorem, exact joint frontier and rational instrument-error allocation.

C. FINDING — The declared tail/input budget passes conditionally; independent tail and acquisition evidence remains necessary.

D. UD GAP IMPACT — Measurement requirements sharpened, no empirical admission or physical promotion.
