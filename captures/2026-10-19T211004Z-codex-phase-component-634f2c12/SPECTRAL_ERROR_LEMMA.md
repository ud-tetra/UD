# Conditional deterministic spectral summaries

Development — no registry entry; Physical Promotion=0. This lemma supplies error propagation **if** a justified waveform-error bound is supplied. It does not supply that bound or identify the waveform with a UD state.

Let vhat,v in R^N be an acquired voltage vector and its intended true voltage vector in the SAME coordinates and time grid. Assume ||vhat-v||2<=epsilon, with epsilon in volts in this finite-vector norm. The epsilon here is unrelated to the native600-cell encoded quantum, instrument ceilings or shape statistic.

Let P=I-11^T/N, let W be a diagonal window with ||W||2<=1, let F be the unitary complex N-point discrete Fourier matrix, and let R select the declared positive-frequency rows. Put z=RFWPv and zhat=RFWPvhat. These factors are contractions, hence

||zhat-z||2<=epsilon, and ||zhat_j|-|z_j||<=epsilon for every selected bin.

The proof is submultiplicativity and reverse triangle inequality. This statement uses FFT/N^0.5 and no doubled one-sided weights. A different published amplitude/PSD convention must include its actual scaling factor in the operator norm. No data-dependent normalization by a small signal norm is silently allowed.

The acquired DC mean mhat and demeaned RMS rhat satisfy

|mhat-m|<=epsilon/sqrt(N),
|rhat-r|<=epsilon/sqrt(N), where r=||Pv||2/sqrt(N).

Cauchy-Schwarz proves the first bound; the reverse triangle inequality and ||P||<=1 prove the second. The same RMS bound holds specifically for ||WPv||2/sqrt(N). A taper-energy-normalized RMS with denominator sqrt(sumw2) requires its own factor ||W||/sqrt(sumw2). It does not include errors in sample times, gains, offsets or analog filtering unless a justified upstream epsilon already covers them in the declared common grid.

If the observed largest amplitude has strict margin

|zhat_k|-max(j!=k)|zhat_j|>2epsilon,

then k is the unique largest true amplitude among exactly those selected bins. Each competitor can gain at mostepsilon and the selected amplitude can lose at mostepsilon. Otherwise the certificate returns HOLD: failure of this sufficient inequality is not proof that the physical spectral maximum is wrong. The conclusion is a discrete-bin identity, not a sub-bin frequency estimate or continuum frequency confidence bound.

For a conditional spectral-centroid interval, define

p_j^- = max(0,|zhat_j|-epsilon)^2,
p_j^+ = (|zhat_j|+epsilon)^2.

Suppose nonnegative bin coordinates have justified intervals f_j^-<=f_j<=f_j^+. If S^- = sum p_j^->0, then

(sum f_j^- p_j^-)/(sum p_j^+) <= centroid <= (sum f_j^+ p_j^+)/(sum p_j^-).

This follows from nonnegativity and interval bounds on numerator and positive denominator; common-rate correlations do not invalidate the enclosure. Intersect with the overall frequency range when helpful. If S^-=0, this formula supplies no denominator certificate and returns HOLD. Nominal bin coordinates alone support a descriptive nominal-grid centroid, not independently calibrated hertz. A sample-rate interval supplies f_j intervals via f_j=j*f_s/N only when the common-grid model is justified.

No independence, Gaussian noise, bootstrap, asymptotic or simultaneous-coverage assumption was used. A single simultaneous deterministic vector boundepsilon covers every displayed selected bin, DC and RMS at once. Without a real calibrated epsilon and time-grid premise, all physical uncertainty claims remain HOLD; descriptive numerical summaries may still be reported with their scope.

The proof is algebraic and does not depend on the outcomes of the published waveform or synthetic tests. It does not establish circuit Gauss-law conservation, source-family membership, a native62-channel observer, SI-to-UD correspondence, or a physical promotion.

## Mapping to the frozen one-sided power convention

The component protocol uses power

P_j=d_j |FFT(w*(vhat-mean(vhat)))_j|^2/(N*sum_n w_n^2),

with d_j=2 at the interior positive bins and d_j=1 at DC/Nyquist. Its positive-bin power is |z_j|^2 for

T=D R F W P, D_jj=sqrt(d_j/sum_n w_n^2).

If sumw2>0, then ||T||2<=L, where L=sqrt(2/sumw2)*||w||infinity is a safe common bound. Substitute alpha=L*epsilon_vector for epsilon in the selected-bin amplitude/margin/power/centroid statements above. The DC and unwindowed demeaned RMS still use epsilon_vector/sqrtN. If a justified uniform per-sample error epsilon_sample is supplied, epsilon_vector<=sqrtN*epsilon_sample, so those DC/RMS errors are at mostepsilon_sample. This conversion does not assume independence.

Finite floating FFT/window/normalization computation is another error source. If an independently validated implementation bound ||zhat_computed-T*vhat||infinity<=eta_computation is available for the same declared operator, use

alpha_total=L*epsilon_vector+eta_computation.

Deterministic contributions add. Analytic versus finite stored windows and the normalization denominator must be included in that declared operator or in the validated implementation debit. An ordinary floating FFT result supplies no such validated debit by itself. No numerical calibration epsilon, sample-rate interval or validated computation debit is supplied by this turn; hence these are conditional formulas, not an experimental interval certificate. The reference checker's actual waveform features remain descriptive.
