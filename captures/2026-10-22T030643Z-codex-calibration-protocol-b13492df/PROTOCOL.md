# Calibration and source-preparation protocol v0.1

PROPOSED / UNEXECUTED. 21 October2026 America/Chicago. Development —no registry entry. Independent review pending; physical promotion0. This packet specifies work for a future laboratory preparation. It does not record measurements, purchases or author contact.

## Objective and binding

Establish whether the twelve prerequisites in evidence-admission v0.1 can be supported for a real, named acquisition chain. Begin with an independent reference-chain calibration. Transfer to a simulator/DUT only after its output source class and all uncertainty records are separately supported. A programmed input spectrum does not certify the output of nonlinear dynamics.

Record apparatus serial identifiers, acquisition firmware/settings, analog range, probes/cables, channel assignment and loading, clock/trigger topology, operating conditions, preparation state and UTC acquisition interval. Hash raw reference captures, calibration files and analysis configuration. Freeze an apparatus/run profile with the actual channel set, sample-clock interpretation, carrier, kernel and every displaced sample interval. A new preparation cannot reuse the unresolved historical Riechert profile as though it were the same run.

## Gate1 — timing feasibility before long acquisition

Required total absolute sample-time error is<=1/5000000000 s=0.2ns relative to the declared reference epoch. A proposed worst-case split assigns50ps each to epoch uncertainty, fixed path skew, within-run variation and clock drift. Each share must include calibration-reference uncertainty; statistical independence is not assumed.

1. Feed the same independently characterized reference waveform to every intended acquisition channel through characterized paths. Use an independent time/phase reference with an uncertainty budget adequate for the share being tested. Do not use the candidate quadrature output as its own reference.
2. Bound path-delay corrections across channel, voltage/frequency range and stated operating conditions. Preserve applied corrections and residual uncertainty. Recheck before and after the run; justify any interpolation or stability bound between checks.
3. Establish sample-clock drift and time-varying jitter across the entire active acquisition span and any displaced sample intervals. The50ps drift share over16183/1953125 seconds requires fractional clock-error bound<=1953125/(20000000000*16183), approximately6.03parts per billion if linear drift is the declared model. Epoch resets, nonlinear drift and trigger latency need their own shares.
4. A repeated standard deviation is diagnostic only. To claim a deterministic uniform bound, supply bounded-source/hardware/monitor arguments covering unobserved intervals; otherwise mark HOLD or derive a separate probabilistic contract with explicit failure probability. That would be a new contract, not automatic satisfaction of this one.

The exact joint error frontier also permits other allocations. A1ns timing alternative with the same250000V/s slope and other input shares would fit the mathematical total budget, but would fail the existing evidence checker’s0.2ns per-role requirement. It remains a design alternative requiring a separately versioned profile/requirements review; this protocol does not silently substitute it.

## Gate2 — prepared reference signal

Use a source model with carrier fc=501953125/16184 Hz and envelope lines at-25,0,+25Hz. Declare coefficient magnitudes1/16,3/4,1/16V. Before tail/error allowances, spectral TV is7/8V and the triangle-inequality amplitude floor is5/8V. A total tail TV<=1/1000V leaves full-reference amplitude>=78/125V=0.624V, above the1/2V phase threshold.

Calibrate the actual line coefficients and frequencies against the independent reference chain; command values alone do not establish them. Include source drift, phase noise, harmonics/intermodulation, switching transients and residual source error in an independently justified source model. Finite gating and preparation transients cannot be discarded while assuming exact compact support. Source bounds must apply throughout the target run; monitor the DUT output independently if nonlinear coupling changes its spectrum.

## Gate3 — spectral-tail feasibility

A1second complex-envelope monitor interval is proposed for a declared finite100-mode tail bank. Freeze frequencies, mode count, reference normalization, window/epoch and any isolation filter before inspecting results. Distinct integer-Hz envelope frequencies are orthogonal on exactly1second under the stated clock model; deviations require a new Gram bound. The nominal1Hz Fourier spacing does not itself certify spectral variation or suppress unresolved content.

The finite-mode witness theorem requires measured finite-mode complex RMS<=60microvolts, total coefficient-estimation error<=20microvolts and independently bounded outside-model spectral TV<=200microvolts. These combine to the1millivolt tail-TV ceiling. Coefficient error must include monitor uncertainty, frequency/clock error and outside-mode contamination. Because the outside-model TV ceiling is larger than the coefficient-error share, isolation or a sharper projection bound is essential; passing an electronics-noise check alone is insufficient.

Preserve complex monitor data and the calibrated projection/transfer model. Document where the outside-model bound comes from independently: a validated source restriction and calibrated full-path transfer bound, or another sufficiently justified measurement/model argument. A same-output FFT, a fitted residual alone, or an unqualified spectrum-analyzer noise floor is not this certificate. If finite-mode completeness, stationarity, monitor error or the outside-model bound is unsupported, return HOLD. The theorem is conditional and supplies no missing empirical evidence by itself.

## Gate4 — voltage acquisition budget

| Contribution | Required bound | Measurement/preparation action |
|---|---:|---|
| Noise and quantization | <=1/10000V | Independently characterize range, ADC resolution/nonlinearity, noise model and worst-case acquisition error; include reference uncertainty |
| Relative gain | <=1/100000 | Compare calibrated input levels/frequencies across the operating range, before/after acquisition; bound interpolation/drift and loading |
| Timing contribution | <=1/20000V | Combine timing witness with clean slope<=250000V/s over displaced sample intervals |
| Nonconstant baseline | <=1/20000V | Calibrate drift beyond each local constant baseline; include temperature/time dependence and reference uncertainty |
| Constant baseline | <=3V | Record offset/range and verify no clipping/saturation |
| Input magnitude | <=5V | Bound full clean waveform plus baseline/error and document acquisition range |

The four input contributions sum to1/4000V. Uniform noise bounds are not inferred from RMS statistics without a declared additional model. Any spectrum used to derive slope must also justify the physical tail-frequency cutoff200000Hz or provide an independent derivative bound. A nominal20nF energy formula does not establish a full energy functional.

## Gate5 — receipt and review handoff

For every role, complete the blank bound record and method/witness attachment. Record value/unit/direction, validity interval, profile hash, calibration corrections, raw witness hashes, analysis hashes, uncertainty model, dependencies and limitations. Derived slope or amplitude bounds must reference independently supported source records. Keep any unresolved values null and statusPENDING; templates are intentionally non-admissible.

An independent reviewer inspects the method, source restrictions and witness bytes, then writes a scoped review receipt. Only the external review authority may add its hash to the trusted catalog. Different reviewer labels and hashes alone do not authenticate independent science. Run the structure checker after that review; its success still means ready for review/decision, not physical promotion. Missing bounds, invalid transfer assumptions, stale calibration or incompatible channel/run coverage returns HOLD.

## Release conditions and current disposition

Release a measurement-readiness packet only with all twelve actual reviewed bounds and a resolved apparatus/run profile. This protocol is not executed; every blank template and the historical circuit candidate remains HOLD. A future reference-chain calibration cannot retroactively supply missing provenance for a historical run without justified transfer/stability evidence.

A subsequent native-action experiment would additionally need a same-carrier apparatus-to-native map, absolute support, complete calibrated energy/baseline and a signed primitive clock. Neither this protocol nor a successful reference-tone calibration supplies those gates. EXIT-03 remains HOLD; no eta_A or hbar fit is authorized by calibration readiness.
