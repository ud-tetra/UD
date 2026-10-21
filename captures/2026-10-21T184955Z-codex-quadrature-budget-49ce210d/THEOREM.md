# A continuous-band quadrature error budget for a saved finite kernel

Theorem manuscript v0.1. 21 October 2026. DERIVED / EXACT CONDITIONAL. Constructor checked; independent review pending. Development — no registry entry. Physical promotion 0. This is a finite-filter measurement theorem, not a physical UD identification or novelty claim.

## Source and estimator

Let fs>0, offsets k=-m,...,m, s_k=k/fs and a fixed complex kernel h_k. Define zhat_j=sum h_k V_{j+k} on centers with a complete measured window. Define its tone responses at carrier fc by

    A(f)=(1/2)sum h_k exp(2pi i(fc+f)s_k),
    B(f)=(1/2)sum h_k exp(-2pi i(fc+f)s_k).

Assume the complex envelope u(t)=integral[-W,W]exp(2pi i f t)dmu(f) for a finite complex measure mu with total variation <=M. Measured samples satisfy

    V_{j+k}=Re(u(t_j+s_k)exp(2pi i fc(t_j+s_k)))+b+e_{j+k},

where |b|<=beta is constant on the window and |e_{j+k}|<=epsilon. This source assumption constrains a global generative signal; its satisfaction cannot be inferred merely from filtering one finite record.

Let D0>=|A(0)-1|+|B(0)| and D1>=|A'(0)|+|B'(0)|. Choose upper bounds H0>=sum|h_k|, H2>=sum|h_k|s_k² and C0>=|sum h_k|. Put

    R(W)=D0+W D1+2pi² H2 W²,
    d=M R(W)+beta C0+epsilon H0+E_fp.

## Theorem

In real arithmetic, estimator error relative to Z_j=u(t_j)exp(2pi i fc t_j) is <=M R(W)+beta C0+epsilon H0. If a declared implementation has complex evaluation error <=E_fp, total output error is <=d. At centers with |Z_j|>=a_min>d, phase error is <=asin(d/a_min). Amplitude error is <=d and squared-amplitude error <=d(2|zhat_j|+d).

A complete measured window introduces no external-sample continuation assumption. A centered window becomes available only at delay m/fs; no phase statement is made where the amplitude premise fails.

## Proof

Taylor's integral remainder gives |A(f)-1|+|B(f)|<=D0+|f|D1+(f²/2)sup_q(|A''(q)|+|B''(q)|). Each derivative contributes at most (1/2)(2pi)² sum|h_k|s_k²; together the supremum is <=4pi²H2. Thus the response bound R(W) holds for every real f in [-W,W], without interpolation from a frequency grid.

For each spectral tone the real input contains positive and conjugate exponentials. Its response is A(f) times the positive phasor plus B(f) times the conjugate phasor. Subtract the positive reference, integrate and use the total-variation inequality to obtain M R(W). A constant baseline contributes at most beta C0; bounded sample error contributes epsilon H0. Add implementation error by the triangle inequality. The disk of radius d about the true phasor has tangent angle asin(d/|Z_j|), proving the stated phase bound. Reverse triangle and the difference of squares prove the remaining statements. QED.

## Instantiated certificate

Use the unchanged 2049-sample kernel from local-quadrature v0.1, interpreting each saved parsed binary64 coefficient as an exact dyadic rational; fs=1953125 Hz and fc=257fs/16184. Real/imaginary absolute-value sums bound complex magnitudes conservatively. Coefficients are not reoptimized or re-solved. The certificate checks W=50 Hz, M=1 V, a_min=1/2 V, epsilon=1/2000 V, beta=3 V, delay cap3/5000 s and E_fp=2^-30 V against targets1/100 V and1/50 rad.

All comparison fields in CERTIFICATE.json contain exact rational fractions. Decimal approximations are explanatory only. D0/D1 use 160-bit fixed-point interval arithmetic with exact integer floor/ceiling, an alternating-series Machin pi enclosure, bounded-remainder sine/cosine Taylor evaluation at a small angle, and binary interval powers. H0,H2,C0 are rational sums of exact dyadic coefficients. No floating grid is used for the continuous-band guarantee.

For the declared serial real/imaginary binary64 dot products, with round-to-nearest, no overflow, |V|<=5 V, n=4098, machine unit u=2^-53 and subnormal absolute allowance eta=2^-1074, a conservative bound is

    E_eval <= [n u/(1-n u)] 5 H0 + 2 n eta/(1-n u) < 2^-30 V.

This follows by propagating each primitive relative/absolute rounding bound through the finite sums. It bounds that declared evaluation, not arbitrary BLAS/convolution libraries, demodulation, atan2 calls or every platform. The certificate is not a new native runtime-validation receipt. The stored coefficient quantization is already included in A,B and their derivatives.

The phase ratio r=d/a_min is below1/10. Instead of computing inverse sine numerically, use asin(r)<=r/sqrt(1-r²)<=100r/99 for 0<=r<=1/10. The resulting rational phase bound passes1/50 rad. The numerical delay1024/1953125 s passes3/5000 s.

## Negative controls and scope

The exact interval response at+600 Hz gives the lower error bound |A-1|-|B|>0.2305 for every phase of a unit tone; this is a concrete failure of1% recovery for the unchanged kernel outside the admitted source class. It is not a no-go against other kernels. Raising input epsilon to1/100 V fails this sufficient budget, not a proof that every noise realization must fail. Tightening the delay cap to1/2000 s fails the unchanged window's exact delay.

Independent source bandwidth, instrument gain/skew and input-error evidence remain OPEN. Cross-channel timing, full energy, absolute native support, primitive recurrence, eta_A and EXIT-03 are not closed. Previous2/6 synthetic and0/891 empirical results remain valid in their original, different scopes.
