# Finite-support quadrature with local source and input-error bounds

Theorem manuscript v0.1 — 21 October 2026. DERIVED / EXACT CONDITIONAL in real arithmetic. Standard weighted least-squares construction applied to the UD measurement protocol; no novelty or physical-identification claim. Constructor checked; independent review pending. Development — no registry entry. Physical promotion 0.

## Theorem

Let offsets k=-m,...,m have sample times s_k=k/fs, nonnegative weights w_k, and real design rows D_k=(cos(omega s_k),-sin(omega s_k),1). Assume G=D^T W D is invertible. Define Q=G^{-1}D^T W and h_k=Q_{0k}+i Q_{1k}. At a measured center j whose complete window is available, put

    zhat_j = sum_k h_k V_{j+k},
    uhat_j = exp(-i omega j/fs) zhat_j.

Then:

1. The three moments are sum h cos=1, sum h(-sin)=i, sum h=0. A signal V_{j+k}=Re(Z_j exp(i omega s_k))+b_j, with constant local phasor Z_j and real constant baseline b_j, is reconstructed exactly as zhat_j=Z_j.
2. Suppose V_{j+k}=Re(u_{j+k} exp(i omega(j+k)/fs))+b_j+e_{j+k}, with |u_{j+k}-u_j|<=L_j |k|/fs and |e_{j+k}|<=epsilon_j. Define H0=sum|h_k| and H1=sum|h_k||k|/fs. Then

       |zhat_j-u_j exp(i omega j/fs)| <= d_j := L_j H1+epsilon_j H0.

   The same bound holds for |uhat_j-u_j|. Time-varying baseline error must enter e; only a constant local baseline cancels.
3. For a constant-amplitude tone Z_j=Z exp(i(omega+delta)j/fs), its exact finite-filter transfer is

       zhat_j = A(delta) Z_j+B(delta) conjugate(Z_j),
       A(delta)=(1/2)sum h_k exp(i(omega+delta)s_k),
       B(delta)=(1/2)sum h_k exp(-i(omega+delta)s_k).

   Therefore |zhat_j-Z_j| <= (|A-1|+|B|)|Z_j|. At delta=0, A=1 and B=0.
4. If d_j<|zhat_j|, then the phase error relative to the specified true phasor is <=asin(d_j/|zhat_j|), amplitude error <=d_j, and squared-amplitude error <=d_j(2|zhat_j|+d_j). These are deterministic conditional bounds, not confidence intervals.

## Proof

Invertibility gives QD=I, hence the moments in (1). Expand Re(Z_j exp(i omega s_k))=Re(Z_j)cos(omega s_k)-Im(Z_j)sin(omega s_k) and apply those moments; the baseline term vanishes. For (2), subtract the exact local constant-phasor reconstruction. The residual at offset k has magnitude at most L_j|k|/fs+epsilon_j because |Re(a)|<=|a| and the oscillatory multiplier has modulus one. Multiply by |h_k|, sum, and use the triangle inequality. Demodulation has unit modulus. For (3), expand the real tone into its positive and negative complex exponentials and collect the two sums. For (4), apply the reverse triangle inequality, factor the difference of squared magnitudes, and use the tangent angle to the disk of radius d_j centered on zhat_j. QED.

## Applicability and limits

This theorem uses only the measured window. It does not use a periodic extension, unseen padding, a Hilbert-transform continuation or whole-record demeaning. With a centered window, the timestamp is j/fs but real-time availability is delayed by m/fs. Discarding the unavailable endpoint centers is essential.

Invertibility is a premise; arbitrary carrier/sample combinations can make the columns dependent. The numerical implementation checks conditioning and moments for its frozen design but does not supply formal outward-rounded enclosures. A deployed bound needs an additional certified numerical allowance.

Input uncertainty can be budgeted, conditionally, as epsilon<=epsilon_noise+g_max V_max+tau_max D_max+epsilon_baseline if independently justified bounds hold for additive noise, relative gain error, voltage magnitude, sampling-time error, voltage derivative and nonconstant baseline residual. This is a sufficient triangle-inequality budget, not a calibration supplied by this work. Fixed carrier error appears through the envelope variation L or the explicit transfer law; do not silently count or omit it twice. Cross-channel synchronization, absolute time units and the apparatus-to-native map need their own evidence.

If an independently calibrated energy proxy C|u|²/2 applies, its estimator contribution is bounded by C d_j(2|uhat_j|+d_j)/2. This does not establish a full Hamiltonian, native support, primitive state recurrence or action normalization.

The accompanying verifier checks the finite transfer identity, source-regularity inequalities and negative controls numerically. No claim advances beyond constructor-checked development.
