# A sampled complex-monitor leakage witness with timing and calibration error

Theorem manuscript v0.1 —22October2026 America/Chicago. DERIVED / EXACT CONDITIONAL. Constructor checked; independent review pending. Development —no registry entry; physical promotion0. Standard finite-dimensional norm bounds applied to an explicit measurement contract; no physical UD identification or novelty claim.

## Direct sampled witness

Let the finite-mode component be

$$p(t)=\sum_{\ell=1}^{K}a_\ell e^{2\pi i f_\ell t},$$

and the full source tail be p+r_out, with outside-model complex spectral-measure total variation at most T_out. For actual sample times t_j, j=0,...,N-1, define the sample norm ||v||_d²=N^{-1}sum_j|v_j|². Let the complex-monitor outputs satisfy

$$y_j=p(t_j)+r_{\rm out}(t_j)+e_j,\qquad \|e\|_d\le\epsilon_d.$$

The monitor must be independent and applicable to this source; e includes I/Q/path calibration, acquisition, quantization, baseline, reference and numerical errors. Put Phi_{j,l}=exp(2pi i f_l t_j) and G_d=Phi*Phi/N. If G_d>=lambda_d I with lambda_d>0 and r_d>=||y||_d, then

$$T_{\rm tail}\le\sqrt{K/\lambda_d}\,(r_d+\epsilon_d+T_{\rm out})+T_{\rm out}.$$

Proof: ||p(t_j)||_d²=a*G_d a>=lambda_d||a||_2². Also |r_out(t)|<=T_out, so ||p(t_j)||_d<=||y||_d+epsilon_d+T_out. Apply ||a||_1<=sqrt(K)||a||_2 and add the outside-model measure. QED.

This bound explicitly charges outside-mode contamination inside the sample norm as well as its contribution to the full spectral tail. It does not assume a perfect isolation filter or infer a continuous-time RMS by interpolating the samples. The finite-mode source model must hold on the claimed source scope; finite samples alone cannot establish it.

## Timing-robust sampled Gram bound

Assume T0>0, distinct integer nominal modes n_l and fixed frequencies f_l=f_common+n_l/T0+e_l, |e_l|<=eta. Actual sample times obey

$$t_j=t_{\rm epoch}+(1+\alpha)jT_0/N+\xi_j,\quad |\alpha|\le\rho,\quad |\xi_j|\le\tau.$$

Epoch is arbitrary. A common frequency or epoch shift contributes only unit-modulus row/column factors and leaves Gram eigenvalues unchanged. It does not certify absolute phase or physical band membership. For d_lm=|n_l-n_m|, set

$$q_{\ell m}=d_{\ell m}\rho+2\eta T_0(1+\rho),\qquad s_{\ell m}=1-\frac{1}{6}\left[\frac{\pi(d_{\ell m}+q_{\ell m})}{N}\right]^2.$$

Suppose all nominal modes are distinct modulo N and every pair satisfies q<d, d+q<N/2 and s>0. Then

$$|(G_d)_{\ell m}|\le b_{\ell m}:=\frac{q_{\ell m}}{(d_{\ell m}-q_{\ell m})s_{\ell m}}+2\pi\left(\frac{d_{\ell m}}{T_0}+2\eta\right)\tau,$$

and

$$\lambda_{\min}(G_d)\ge 1-\max_\ell\sum_{m\ne\ell}b_{\ell m}.$$

Proof: first set xi_j=0. Write u=(f_l-f_m)(1+alpha)T0. Its distance from the signed nominal integer gap is at most q. The geometric-series magnitude is |sin(pi u)|/[N|sin(pi u/N)|]. The numerator is <=pi q. With |u| between d-q and d+q, sin(x)>=x-x³/6 on this guarded interval gives denominator>=pi(d-q)s. Now restore xi_j. The change of each pair-phase factor has magnitude<=2pi|f_l-f_m||xi_j|, and |f_l-f_m|<=d/T0+2eta. Average these perturbations and apply the maximal absolute-row-sum lower bound for a Hermitian matrix with diagonal1. QED.

In the rational certificate, pi is conservatively replaced by22/7 in upper terms and in the denominator factor's subtracted upper term. No floating trigonometry or eigenvalue is used for acceptance. These are sufficient guards; a failed row bound does not imply that a particular Gram matrix is singular.

## Instantiated sampled design

Freeze N=1024, T0=1s, n_l=100,...,199, eta=1/200Hz, rho=1/100000000 and tau=1/100000000s=10ns. T0 is the nominal cyclic grid span; the first-to-last nominal sample separation is1023/1024s. This is an independent complex-envelope monitor design, not the original acquisition clock or its0.2ns requirement.

Exact rational row sums yield lambda_d>0.9096. Therefore lambda_d>=9/10 is certified, and C=211/20 satisfies C²*(9/10)>=100. Choose r_d<=55microvolts, epsilon_d<=20microvolts and T_out<=10microvolts. Then

$$T_{\rm tail}\le\frac{211}{20}(55+20+10)\,\mu{\rm V}+10\,\mu{\rm V}=906.75\,\mu{\rm V}<1\,{\rm mV}.$$

The new outside-model ceiling is prospectively stricter than the previous200microvolt proposal. With that previous ceiling and the same direct-monitor formula, the sufficient bound is3.10125mV, which misses the1mV target. The earlier isolated-waveform/coefficient-error routes remain valid under their own assumptions; this is not a retraction of those theorems or evidence that every source with the larger ceiling fails.

## Quadrature and digital arithmetic

One sufficient independent-monitor error split is10microvolts calibrated acquisition/quantization,5microvolts quadrature-matrix error,3microvolts residual baseline and2microvolts numerical error. These sum to20microvolts. For a calibrated real two-component input vector of norm<=5V, operator-norm matrix uncertainty<=1/1000000 gives a5microvolt output contribution. Applicable full-path frequency response, reference uncertainty, nonlinearity and any conditioning/amplification must be included; a static matrix label alone does not establish them.

For exact serialized binary64 complex values y_j, compute E=N^{-1}sum[(Re y_j)²+(Im y_j)²] as a rational number. E<=r_max² certifies the digital RMS ceiling without a floating square root. An explanatory rational RMS upper bound can be obtained with an integer ceiling square root. This certifies arithmetic on the stored values, not that they equal physical source samples or that calibration errors satisfy epsilon_d. The previous steps producing those values retain their own numerical/error obligations.

## Aliasing and evidence limits

On the nominal1024-point grid, integer modes100 and1124 are identical at every sample. Their opposite1V coefficients produce zero sampled signal while distinct source atoms have TV2V. A continuous-time Gram theorem alone cannot exclude this sampled alias. The declared100..199 bank, non-alias guard and independent outside-model bound are essential. With only64 samples the proposed100-mode bank also has a rank obstruction.

No time-varying coefficients, unrestricted off-bank modes, clock warping or arbitrary transfer errors are admitted by the fixed-mode contract. The source completeness and10microvolt outside-model TV bound cannot be inferred solely from the same finite samples. No physical gain, skew, I/Q accuracy, independent reference identity, native support, full energy, primitive clock, eta_A or EXIT-03 closure is supplied here. No experiment is executed.
