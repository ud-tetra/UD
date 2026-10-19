# Conditional timing-to-waveform enclosure

Status: DERIVED conditional lemma; development — no registry entry. No numerical apparatus tolerance is asserted.

The pinned author utility header declares a nominal 125 MHz base and 16384 samples. The selected-style drive1 executable sets decimation 64. Conditional on that code and nominal clock being the applicable recipe,
f0=125000000/64=1953125 Hz and dt0=64/125000000=0.000000512s.
A buffer's N/fs duration convention is 0.008388608s; first-to-last sample span is 16383/fs=0.008388096s. After dropping 200 samples, N=16184, N/fs=0.008286208s and first-to-last span 16183/fs=0.008285696s. These are nominal bookkeeping identities, not calibrated time intervals. GPIO header /8 conflicts with its executable /64 setting; another drive2 program actually uses /8. Request program/binary/device/acquisition bindings.

Let nominal cropped timestamps be t_n=t0+n/f0, n=0,...,N-1. Suppose independently justified acquisition evidence proves
t_actual,c,n=t0+delta_origin+delta_skew,c+n/[f0(1+e_c)]+j_c,n,
|delta_origin|<=o, |delta_skew,c|<=s, |j_c,n|<=j and |e_c|<=rho<1.
Here origin refers to the cropped start. If instead bounds refer to acquisition trigger, use the actual offset index (e.g. 200+n) or debit it in origin.
Then, for every channel/sample,
|t_actual,c,n-t_n| <= tau_N = o+s+j+(N-1)rho/[f0(1-rho)].
Proof: |1/(1+e)-1|=|e|/|1+e|<=rho/(1-rho), then triangle inequality.

If, on the entire enlarged time domain, a channel voltage has independently justified derivative bound |dv_c/dt|<=L_c, the mean value theorem gives
||v_c(t_actual)-v_c(t_nominal)||_2 <= sqrt(N)L_c tau_N.
For a known finite multitone with amplitudes bounded by A_k and frequencies by F_k, one possible derivative bound is L_c<=2pi sum_k A_k F_k. No spectral band or derivative bound is inferred from metadata, finite time FFT peaks, nominal oscillator frequencies or trigger comments.

If a vector budget allocates eta_c>0V to timing alone and L_c>0V/s, it suffices to establish tau_N<=eta_c/[sqrt(N)L_c]. With independently bounded a=o+s+j and b=eta_c/[sqrt(N)L_c]-a>0, a sufficient rate condition is
rho <= b f0 / [(N-1)+b f0].
All other amplitude, aliasing, numerical and model discrepancy debits remain separate; do not double count. This directly supplies the mathematical role requested by calibration.timebase.warp_to_waveform_vector_error_V and band_or_derivative_domain_proof. Unknown o,s,j,rho,L_c,eta_c remain unknown.

Shared external trigger does not prove a shared ADC clock. The source comment's 0.2–0.3us generated CH2 trigger latency is not a measured inter-device jitter, skew, or clock rate bound. Decimal %f serialization is a source setting, not ADC precision or calibration. A half-last-decimal bound would additionally need verified rounding, runtime, locale and conformance and binary-to-voltage error coverage; no such bound is filled into the request here.

