# Conditional finite-mode leakage witness bound

Theorem manuscript v0.1. 21 October2026 America/Chicago. DERIVED / EXACT CONDITIONAL. Constructor checked; independent review pending. Development —no registry entry. Physical promotion0. This is a standard orthogonality/Cauchy–Schwarz measurement bound, not a physical UD identification or novelty claim.

Let the source tail on a declared stationary monitor interval have complex envelope

    r(t)=sum_{l=1}^K a_l exp(2pi i f_l t)+r_out(t).

Assume the K distinct frequencies are orthonormal for the normalized inner product on that interval, and the outside-model complex spectral-measure total variation is at most T_out. Let p(t)=sum a_l exp(2pi i f_l t). An independently calibrated complex monitor provides a coefficient-vector estimate ahat with Euclidean error ||ahat-a||_2<=epsilon_mon. If the measured normalized complex RMS of its finite-mode reconstruction is r_meas=||ahat||_2, then total tail spectral variation obeys

    T_tail <= sqrt(K)(r_meas+epsilon_mon)+T_out.

For K=0 the finite-mode contribution is zero. For K>=1 the proof is

    sum|a_l| <= sqrt(K)||a||_2
             <= sqrt(K)(||ahat||_2+||a-ahat||_2),

followed by the triangle inequality for the outside-model measure. Orthonormality identifies the normalized complex RMS with the coefficient norm. QED.

A sufficient way to obtain the coefficient error is an L2 monitor error bound on the finite-mode signal: orthogonal projection is a contraction. If the monitor observes p+r_out, the coefficient error must also include projected contamination by r_out, in addition to instrument error. Alternatively an independently justified filtered/isolated finite-mode channel may supply the coefficient-error bound directly. The outside-model contribution cannot be assumed removed merely by fitting the same data.

For a1second interval, distinct integer-Hz envelope frequencies are orthogonal in exact arithmetic. Actual frequency offsets, finite clock uncertainty or nonstationarity can destroy that premise and require a Gram-matrix bound instead. These conditions are proposed source/monitor restrictions, not established by an FFT peak. The theorem applies to an independently defined complex envelope monitor; conversion from a real-voltage RMS needs its own carrier/quadrature and normalization analysis.

The illustrative frozen witness has K=100, r_meas<=3/50000 V, epsilon_mon<=1/50000 V and T_out<=1/5000 V. Thus

    T_tail <=10*(4/50000)+1/5000 =1/1000 V.

Here epsilon_mon is the **total coefficient-error budget**, including any outside-model projection contamination; it is not automatically a20microvolt electronics-noise specification. T_out=200microvolts is larger than epsilon_mon; a protocol must show isolation or explicitly bound the contamination. The planned witness can remain HOLD if this cannot be supported. These inequalities provide a target requirement, not a completed calibration or guaranteed feasible apparatus.

Without a justified finite mode count/orthogonality or a separate outside-model bound, complex RMS alone does not give this tail-TV ceiling. The previous finite-sample nullspace obstruction still applies. Increasing the mode count raises the worst-case l1/l2 factor and cannot be hidden by reporting an averaged PSD. No uniform deterministic bound follows from a sample standard deviation alone.

Together with the prior leakage theorem, a valid independent witness supplies T for

    d_full <= R+(H+1)T+H epsilon+3 C0+E_fp.

It does not supply noise, gain, timing, native support, full energy or action calibration. The theorem requires independent review and physically valid premises before empirical use.
