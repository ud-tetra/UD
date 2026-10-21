# Leakage-tolerant full-state quadrature and joint instrument budget

Theorem manuscript v0.1 —21 October2026. DERIVED / EXACT CONDITIONAL. Constructor checked, independent review pending. Development —no registry entry. Physical promotion0. Standard linear-filter bounds, not physical UD identification or a novelty claim.

## Theorem

Use the unchanged finite complex kernel h and full measured-window estimator zhat=sum h_k V_{j+k} from local-quadrature v0.1. Let H>=sum|h_k|, C0>=|sum h_k|, and let R bound |A(f)-1|+|B(f)| throughout the declared in-band envelope support. Write the complex envelope u=u_in+u_tail, where the in-band spectral measure has total variation<=M and the tail spectral measure has total variation<=T. The tail may occupy arbitrary frequencies for the estimator-error theorem; in particular no unproved anti-alias suppression is assumed. Assume constant baseline magnitude<=beta, input sample errors<=epsilon and implementation evaluation error<=E_fp.

Then the error against the **full** phasor Z_j=u(t_j)exp(2pi i fc t_j) obeys

    d_full <= M R+(H+1) T+H epsilon+beta C0+E_fp.

Against the **in-band-only** reference, instead,

    d_in <= M R+H T+H epsilon+beta C0+E_fp.

These are different targets. At full-reference amplitude>=a_min>d_full, geometric phase error<=asin(d_full/a_min). For d_full/a_min<=1/10, the rational upper bound100 d_full/(99 a_min) suffices.

## Proof

The existing continuous-band theorem bounds the in-band error by M R. At any time, total variation bounds |u_tail|<=T, hence the tail's real voltage has magnitude<=T. The finite kernel's response to that voltage is at most H T. Comparing the output against the full reference also subtracts the tail phasor itself, whose magnitude is<=T, producing (H+1)T. Comparing only with the in-band reference does not subtract that phasor, producing H T. Baseline, sample and evaluation terms follow by triangle inequalities. Apply disk geometry and the previously proved rational inverse-sine bound for phase. QED.

The full-state tail coefficient is a conservative sufficient bound, not asserted optimal for a particular frequency distribution. It cannot be replaced by the in-band formula while retaining the full reference: even an ideal rejection of a tail leaves that tail absent from the recovered full state. Frequency-specific response bounds can sharpen the coefficient only under additional spectral information.

## Exact sufficient frontier

With M=1, beta=3, a_min=1/2, absolute target1/100 V and phase target1/50 rad, the rational phase certificate imposes d<=99/10000 V, which also satisfies the absolute target. Put C=R+3C0+E_fp. The sufficient feasible set is

    (H+1)T+H epsilon <= 99/10000-C,    T>=0, epsilon>=0.

At fixed epsilon, the largest admitted T under this certificate is (99/10000-C-H epsilon)/(H+1), provided the numerator is nonnegative. At fixed T, the admitted epsilon is (99/10000-C-(H+1)T)/H for H>0. Frontier equality is included. This is the feasible set of this sufficient certificate, not the physically optimal frontier across all kernels or uncertainty models.

## Instrument allocation

Suppose measured-input uncertainty is bounded by

    epsilon <= epsilon_noise+g_max V_max+tau_max D_max+epsilon_baseline,

where additive noise includes quantization, gain error is relative to a signal of magnitude<=V_max, timing error is<=tau_max and the clean voltage derivative is bounded by D_max throughout every displaced sampling interval. Any baseline variation beyond the locally constant component is included in epsilon_baseline. This sufficient allocation uses worst-case addition, with no assumed statistical independence or cancellation.

The declared split is noise/quantization1/10000 V plus gain, timing and baseline1/20000 V each, totaling1/4000 V. Relative gain<=1/100000 with V_max=5 V supplies the gain share. tau_max=1/5000000000 s (0.2 ns) and D_max=250000 V/s supply the timing share. Under an additional physical tail-frequency cutoff|fc+f|<=200000 Hz,

    |V_clean'| <= 2pi[(fc+50) M+200000 T] <196526 V/s

for the frozen fc and T=1/1000 V, excluding baseline variation handled separately. Using pi<22/7 makes this a rational sufficient derivative bound. The cutoff is not needed for the generic leakage theorem, but is needed for this illustrative timing justification. No observed hardware capability or cross-channel skew calibration is claimed.

## Limits of finite-record tail certification

A finite set of voltage samples does not itself bound unrestricted out-of-band spectral-measure total variation. For N real sample constraints, choose N+1 distinct real sinusoidal basis functions with frequencies in an allowed tail interval. The N-by-(N+1) evaluation matrix has a nonzero real null vector; linear independence of distinct sinusoidal functions implies that combination is not identically zero as a function. It vanishes at all measured sample times and can be scaled to arbitrarily large finite spectral variation. Thus the same finite samples can coexist with arbitrarily large unobserved tails unless an independent source, norm or model restriction excludes them. This is an identifiability obstruction under unrestricted amplitudes, not a no-go against calibrated source controls or source-class assumptions.

Therefore an FFT of the same finite record, even after filtering, is not by itself an independent tail-TV certificate. Source restrictions, calibrated monitor bounds, justified transfer/anti-alias models or other independent evidence must close that premise. Prior2/6 synthetic and0/891 empirical outcomes, native-action identifiability and EXIT-03 remain unchanged.
