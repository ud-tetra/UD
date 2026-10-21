# Signed-voltage reconstruction contract v0.1

21 October 2026. Development — no registry entry. Constructor verification only; independent review pending. Physical promotion = 0. EXIT-03 HOLD.

## Result and disposition

The signed finite-DFT analytic representation round-trips all 891 evaluated channel-records to a maximum absolute error of 1.5543122344752192e-15 V. The frozen narrow-band reconstruction passes **0/891** composite diagnostic gates. No interior point in any evaluated record passes the conservative uniform phase floor. This is a failure of the specified reconstruction/phase-certification gate, not evidence against the simulator or UD dynamics. No native clock, action ratio, physical correspondence or quantum normalization is estimated.

Carrier selection used each live channel's record 0, which was already explored in the preceding content audit. The extension evaluates records 1–99 of channels 1–9, totaling 891; these have varying drive-frequency metadata and are not identical repeated trials. CONTRACT.json was written before running this extension; this is a constructor freeze, not a blinded preregistration or independent review.

## Frozen apparatus-to-signal map

Input: Riechert et al., Heidelberg data DOI https://doi.org/10.11588/DATA/6MEKHI, file ID 6385, v1.0. Source SHA-256: 7966700a6208e2bd2b5829a32b38cce7016f0c3460ace2708c85bac8577c282c. The release filename identifies CH1/3/5/7/9 as sites 1–5 and CH2/4/6/8 as links 1–4; CH10 is labeled empty, not a certified noise witness. No new physical channel calibration is asserted. Imported scripts/notebooks are not executed.

Six metadata columns precede 16384 voltage samples. Retain samples 200–16383, N=16184, fs=1953125 Hz; define t_j=j/fs relative to the documented trigger sample. Demean each retained trace. Let Z=DFT(V) and H double strictly positive-frequency bins, retain DC and Nyquist once, and zero negative-frequency bins. The complex analytic signal is z=IDFT(HZ); Re(z)=V in exact arithmetic. DC removal is preprocessing and does not recover the circuit's physical baseline.

Select fixed fc per channel from its record-0 demeaned Hann-window power maximum in 10–200 kHz. On each subsequent record, form z_f by rectangular projection of z onto strictly positive DFT bins within 5000 Hz of that fc. No per-record retuning, resampling or decimation occurs. The rotating-frame envelope is u(t)=z_f(t) exp(-2 pi i fc t), and signed reconstruction is Re(u(t) exp(2 pi i fc t)). Complex u retains phase that |u| and |u|² discard. Carrier choice is a coordinate convention and does not establish a native primitive period.

The entire post-trigger record supplies RMS residual and delta=max_j|z_j-z_f,j|. Interior diagnostics discard 1024 samples at each end. Accept phase at an interior point only when |u|>10 delta. Accept a record only if relative signed RMS residual <= 0.05 and accepted interior phase fraction >=0.95. These are design thresholds, not statistical confidence levels or UD acceptance criteria.

## Explicit finite-record error statements

For this finite-DFT reference, the residual gives |z-z_f|<=delta by definition. The reverse triangle inequality yields ||z|-|z_f||<=delta. Consequently

    ||z|²-|z_f|²| <= delta (2 |z_f| + delta).

If |z_f|>delta, the disk of radius delta around z_f excludes the origin. Its tangent angle gives

    |arg(z/z_f)| <= asin(delta/|z_f|).

Thus an accepted point has phase error < asin(1/10) = 0.1001674211615598 radians relative to the full finite-DFT analytic reference. Demodulation preserves this bound because its multiplier has unit modulus. A physical error certificate must add instrument, gain, timing and nonperiodic-boundary errors; they are not bounded by this numerical residual.

If an independently known capacitor C applies to the same voltage, the nominal envelope proxy E_env=C|u|²/2 has truncation error <= C delta(2|u|+delta)/2. This is a conditional voltage-derived proxy. The source notebook uses nominal C=20 nF for an envelope routine; that does not certify total LC/coupler energy, baseline, physical Hamiltonian or native energy unit. No new energy number is promoted here.

## Numerical results

| Channel | Fixed fc (Hz) | Median signed RMS residual | Phase fraction (all records) | Composite passes |
|---|---:|---:|---:|---:|
| 1 | 31015.393290 | 0.098608 | 0 | 0/99 |
| 2 | 55634.615979 | 0.090683 | 0 | 0/99 |
| 3 | 84960.454770 | 0.046812 | 0 | 0/99 |
| 4 | 56238.028300 | 0.057923 | 0 | 0/99 |
| 5 | 30774.028361 | 0.071944 | 0 | 0/99 |
| 6 | 58048.265262 | 0.067882 | 0 | 0/99 |
| 7 | 87012.056661 | 0.052373 | 0 | 0/99 |
| 8 | 57444.852941 | 0.081110 | 0 | 0/99 |
| 9 | 32101.535467 | 0.042596 | 0 | 0/99 |

The global maximum residual makes the phase gate conservative: excluding endpoint samples from the evaluation region does not remove their contribution to delta. Periodic-extension artifacts can affect this maximum. The present run does not establish whether endpoints, omitted bands, instrument response or other effects dominate. A guard interval alone supplies no certified edge-error bound. The failed threshold is preserved rather than relaxed after seeing the result.

Five synthetic controls check signed round-trip (6.66e-16 maximum), complex modulated-envelope recovery (2.93e-13 maximum), exact opposite-sign ambiguity under squaring, rejection of zero-signal phase, and rejection of an omitted 0.3-amplitude harmonic (relative RMS 0.28735). All 891 records satisfy the amplitude and squared-envelope inequalities numerically. Accepted-point empirical phase checks have zero eligible points and are vacuous; only the synthetic nonzero case tests successful envelope recovery. NumPy floating-point assertions are constructor checks, not formal interval arithmetic or independent metrology.

## Reproduce and proceed

Use Python 3 and NumPy; download source file 6385 from https://heidata.uni-heidelberg.de/api/access/datafile/6385, retaining the original gzip bytes. Run `python3 reconstruct.py /path/to/riechert_waveform.gz`. The script verifies the source hash and contract, then regenerates RECORDS.csv and RESULTS.json. No downloaded executable code is used.

Next freeze a boundary-treatment comparison using synthetic transients and nonperiodic carriers, with known injected amplitude/phase error. Distinguish edge effects from genuine omitted-band content before revising a reconstruction contract. Any revision must keep v0.1's failed result and use a new version. Independently audit acquisition gain/skew and full circuit energy before any cross-channel phase or native-support claim. The absolute apparatus-to-native map, EXIT-03 specification and action anchor remain OPEN/HOLD.
