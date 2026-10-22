# Leakage witness with uncertain frequencies and monitor duration

Theorem manuscript v0.1. 21 October2026 America/Chicago. DERIVED / EXACT CONDITIONAL. Constructor checked; independent review pending. Development —no registry entry; physical promotion0. Standard Gram/coercivity inequalities applied to measurement requirements, not a physical UD identification or novelty claim.

## General Gram witness

On the actual monitor interval I of duration T, use normalized inner product (1/T)integral_I conjugate(v)w dt. Let p(t)=sum_{l=1}^K a_l exp(2pi i f_l t) with distinct constant frequencies. Let G be their Hermitian Gram matrix. If G>=lambda_* I with lambda_*>0, a calibrated estimate phat satisfies ||p-phat||_{L2(I)/sqrt(T)}<=epsilon_mon, and r_meas bounds ||phat||_{L2(I)/sqrt(T)}, then

    T_tail <= sqrt(K/lambda_*) (r_meas+epsilon_mon)+T_out,

provided an independent outside-model spectral-measure TV bound<=T_out holds.

Proof: ||p||²=a*Ga>=lambda_*||a||². Cauchy–Schwarz gives sum|a_l|<=sqrt(K)||a||, and the L2 triangle inequality gives ||p||<=r_meas+epsilon_mon. Add the outside-model measure by the TV triangle inequality. QED.

The monitor error here is a **waveform L2 error**, including frequency/clock normalization, gain, reference error, numerical integration/reconstruction and outside-model contamination/isolation error. It differs from a directly certified coefficient-vector error in the preceding orthogonal theorem. If such a coefficient-error certificate already exists, its direct l1/l2 bound remains valid without this Gram route; do not substitute one error type for the other.

## Robust lower bound from nominal integer modes

Let T0>0, distinct integers n_l and f_l=f_common+n_l/T0+e_l with |e_l|<=eta. Assume the actual interval satisfies |T/T0-1|<=rho, rho>=0. For d_lm=|n_l-n_m|, define

    q_lm=d_lm rho+2 eta T0(1+rho).

If q_lm<d_lm for every pair, then

    |G_lm| <= q_lm/(d_lm-q_lm), l!=m,
    lambda_min(G) >= 1-max_l sum_{m!=l} q_lm/(d_lm-q_lm).

Proof: the frequency difference obeys |(f_l-f_m)T-(n_l-n_m)|<=q_lm. The normalized exponential inner product has magnitude |sinc((f_l-f_m)T)|, with sinc(x)=sin(pi x)/(pi x). Since the nominal difference is a nonzero integer, |sin(pi(integer+v))|<=pi|v| and |integer+v|>=d_lm-q_lm. This gives the pair bound. G has diagonal1 and is Hermitian, so its smallest eigenvalue is bounded below by1 minus the largest off-diagonal absolute row sum. Equivalently bound the off-diagonal quadratic form by its maximal row sum. QED.

An arbitrary common frequency shift cancels from pair differences and changes Gram entries only by an interval-location phase convention. This invariance does not certify that the shifted modes remain in a physical tail-frequency band; that premise remains separate. A time-varying frequency or nonlinear clock warp is not covered by the constant-frequency/duration model and needs its own error bound.

## Exact instantiated design

Freeze K=100 nominal modes n=100,...,199, T0=1s, eta=1/200Hz and rho=1/100000000. Exact rational row sums give lambda_min(G)>=lambda_G, where the authoritative fraction appears in CERTIFICATE.json and lambda_G is approximately0.9098874884. In particular lambda_G>9/10.

Choose C=211/20. Since C²*(9/10)>=100, C>=sqrt(100/lambda_G). With r_meas<=11/200000V=55microvolts, epsilon_mon<=1/50000V=20microvolts and T_out<=1/5000V=200microvolts,

    T_tail <=(211/20)(15/200000)+1/5000
           =793/800000 V=0.00099125V <1/1000V.

The supplied error/TV premises are proposed requirements, not measurements. Outside-mode projection contamination cannot be assumed zero, particularly when T_out exceeds epsilon_mon. Independent isolation/transfer or contamination evidence remains essential.

The previous60microvolt RMS share would yield0.001044V with this sufficient factor, exceeding the selected1millivolt target. The new55microvolt requirement is a prospective design restriction for this witness, not a reanalysis or silent replacement of the old orthogonal packet. A failed sufficient bound is not proof that every corresponding physical signal fails.

## Near-collision counterexample

On a centered one-second interval, take distinct frequencies f1=201/2-1/2000000Hz and f2=201/2+1/2000000Hz with coefficients+1V and-1V. Their spectral measure has TV2V. Their separation is delta=1/1000000Hz, and pointwise

    |exp(2pi i f1 t)-exp(2pi i f2 t)| <=2pi delta |t| <=pi delta.

Thus normalized complex RMS is at most22/(7*1000000)V, below10microvolts, despite2V tail variation. The modes are distinct; no cancellation of identical-frequency atoms is used. This is an actual source counterexample to an orthogonal-style RMS-to-TV inference without a separation/coercivity premise.

At uncertainty eta=1/2Hz, adjacent nominal modes can collide, so the uniform family cannot retain the same positive lower Gram certificate. Coincident atoms must be coalesced and the model rebuilt; they are not two identifiable independent coefficients. Larger-frequency-error and larger-outside-tail cases in the verifier return HOLD under the chosen sufficient gates, without claiming a no-go for other designs.

## Relation to the full-state error certificate

Insert the new tail bound into the prior unchanged-kernel inequality

    d_full<=R+(H+1)T_tail+H epsilon_input+3C0+E_fp.

At epsilon_input=1/4000V, the inherited exact constants give d_full<0.008667V and phase error<0.017509rad at true full-envelope magnitude>=1/2V. The original delay524.288microseconds is unchanged. No source evidence, native support, energy functional, primitive state clock, action normalization or empirical admission is inferred. Independent review and EXIT-03 remain OPEN/HOLD.
