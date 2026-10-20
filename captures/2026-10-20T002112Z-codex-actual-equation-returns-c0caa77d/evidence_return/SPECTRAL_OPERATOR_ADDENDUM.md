# Explicit spectral normalization for the return profile

Development — no registry entry. Physical Promotion = 0. This append-only clarification supplies the exact operator behind the spectral-amplitude paragraph of RETURN_REVIEW_GUIDE.md. It preserves the frozen guide rather than changing its bytes. It responds to a same-team review question after the first structural inventory execution; it is not an independent metrology finding or a change in the acquisition budget.

The pinned source is `captures/2026-10-19T211004Z-codex-phase-component-634f2c12/SPECTRAL_ERROR_LEMMA.md`, especially “Mapping to the frozen one-sided power convention.” The source convention uses an **unnormalized FFT** in the power formula

\[
 p_j=\frac{d_j\left|\operatorname{FFT}(WPv)_j\right|^2}
 {N\sum_n w_n^2},
\]

where \(P=I-\mathbf1\mathbf1^T/N\), \(W=\operatorname{diag}(w)\), and \(d_j=2\) at interior positive bins and \(d_j=1\) at DC/Nyquist when included. Let \(F=\operatorname{FFT}/\sqrt N\) be the unitary Fourier matrix, \(R\) select exactly the declared bins, and \(D_{jj}=\sqrt{d_j/\sum_n w_n^2}\). Then the spectral-amplitude vector is \(|Tv|\), with

\[
 T=DRFWP,\qquad
 \|T\|_2\le\sqrt{\frac{2}{\sum_n w_n^2}}\max_n|w_n|=L_w,
 \quad \sum_nw_n^2>0.
\]

This follows from \(\|P\|_2\le1\), \(\|F\|_2=1\), \(\|R\|_2\le1\), \(\|W\|_2=\max|w_n|\), and \(\|D\|_2\le\sqrt{2/\sum_n w_n^2}\). Thus a justified same-grid waveform bound \(\|\widehat v-v\|_2\le\epsilon\) and an independently validated computational debit for this exact operator give amplitude error at most \(L_w\epsilon+\eta_{\rm computation}\).

The factor \(1/N\) in the power definition already accounts for the unitary FFT scaling. Applying the displayed \(L_w\) to an unnormalized FFT amplitude without its \(1/\sqrt N\) factor would be incorrect. A different normalization, weighting, window, bin selection, denominator or amplitude/PSD convention needs its actual operator norm and validated computation debit. Nothing here supplies any missing physical calibration, positive centroid denominator or numerical rounding bound. Source-specific finite stored windows and normalization rounding still require R07 content review.
