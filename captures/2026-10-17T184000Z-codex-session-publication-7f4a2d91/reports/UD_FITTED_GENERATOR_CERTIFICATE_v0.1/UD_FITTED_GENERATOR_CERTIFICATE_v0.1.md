# UD fitted generator and common scale certificate

**RESULT — Known fitted offsets can be absorbed exactly into the coordinates, preparations, readout and sampling interval. An unknown common effective scale within 1±1/1024 preserves the parent temporal frame bounds. Residual shape limits can be relaxed eightfold to 2^-35 while retaining 1893 signal directions.** The resulting condition bounds are 19410, 3385 and 1930 for the three schedules.

This is a conditional certificate for an explicitly declared matched grade-metric family. The concrete centre below is an exact candidate example, not an empirical fit. Equal effective incidence rates are a model restriction used for this transfer theorem, not a derived physical unification law. Physical promotion is **0**, development lane, no registry entry; independent review is pending.

## General fitted-coordinate principle

For a known fitted H-skew generator Khat and SPD fitted metric Hhat, let `Q=Hhat^(1/2)`. The transformed generator `Q Khat Q^-1` is skew in Euclidean coordinates. Preparation and readout must be transformed consistently, and calibration uncertainty must be expressed around the fitted values.

A general fitted centre still needs its own modal rank and finite-frame certificate. The exactly transferable family is

\[
\widehat K=cQ^{-1}AQ,\qquad
\widehat H=Q^2,
\]

where A is the frozen unit-metric generator. For grade-scalar `Q=diag(q0 I120,q1 I720,q2 I1200,q3 I600)`, this is a native weighted-incidence model

\[
\widehat K=\widehat H^{-1}A(\widehat w),
\qquad \widehat w_k=cq_{k-1}q_k.
\]

The proof uses exact diagonal similarity; it does not approximate a large known offset by a small perturbation. A fitted generator outside this matched family requires a fresh modal or clustered-frequency calculation before numerical bounds can transfer.

## Explicit exact centre and preparation conversion

Choose the candidate centre

\[
(q_0,q_1,q_2,q_3)=
\left(1,\frac{65}{64},\frac{33}{32},\frac{67}{64}\right),
\qquad c=\frac{33}{32}.
\]

Then

\[
\widehat H_k=
\left(1,\frac{4225}{4096},\frac{1089}{1024},\frac{4489}{4096}\right),
\]

\[
(\widehat w_1,\widehat w_2,\widehat w_3)=
\left(\frac{2145}{2048},\frac{70785}{65536},\frac{72963}{65536}\right).
\]

All 14880 sparse generator entries pass exact rational similarity and H-skew checks. The six directed calibration ratios lie within `[15/16,17/16]`, the earlier local identification domain. This domain check is not an executed calibration receipt or the older nominal-unit acceptance gate.

Use the 37 parent sign preparations X, with entries±1/52, and set

\[
\widehat X=Q^{-1}X,\qquad
\widehat R=RQ,\qquad
\widehat\Delta=\frac 1{2c}=\frac{16}{33}.
\]

The complete rational input matrix is supplied in `FITTED_PREPARATIONS.npz`. Its entries preserve the parent sign pattern and are±1/52,±16/845,±8/429 or±16/871 according to grade. Each has exactly `xhat^T Hhat xhat=165/169`, and Euclidean squared norm no greater than 165/169.

For every integer j,

\[
\widehat R\exp(j\widehat\Delta\widehat K)\widehat X
=R\exp(jA/2)X.
\]

Thus the parent response Hankel matrix is reproduced exactly at the fitted centre. If raw sensors read R, multiply each observed output channel by its fitted grade factor to implement RQ in software. The maximum output factor is 33/32; the maximum state whitening factor is 67/64. Changing only the generator while keeping the old inputs, readout normalization and sampling interval does not satisfy this identity.

Sufficient conversions from raw-coordinate error ceilings to normalized fitted-coordinate ceilings are: multiply the normalized preparation ceiling by 64/67, the readout-operator and additive-output ceilings by 32/33, and the origin/jitter ceilings by 32/33. These factors follow from operator norms of the declared transformations. They do not establish hardware accuracy or an SI clock conversion.

## Common scale uncertainty without phase-error accumulation

In fitted coordinates and normalized time, allow a reference generator `q A`, with

\[
|q-1|\le d=\frac 1{1024}.
\]

The common q is constant throughout the acquisition batch; arbitrary time-varying scale drift is outside this allowance. Its spectral projectors and modal response blocks `R E_lambda X` are unchanged. Only the temporal frequencies scale. The reference family therefore contains the accumulated phase shift exactly; it is not charged as a growing unknown waveform mismatch against A.

The nominal frequencies satisfy `|omega|<4`, so every positive half-phase gap `x=|omega_i-omega_j|/4` is below 2. Since `sin x>=x/3` there, and sine is 1-Lipschitz,

\[
\sin(qx)\ge\sin x-dx
\ge(1-3d)\sin x>0.
\]

The parent's reciprocal-sine sum C is below 1786. Uniformly over this whole common-scale interval,

\[
C(q)\le\frac{C}{1-3d}
<\frac{1786\cdot 1024}{1021}<1792.
\]

This retains the previous temporal Gram allowances 7/8,1/2 and 1/4 for M2048,4096 and 8192. Consequently every reference-family Hankel matrix has rank 1893 and the same certified nonzero condition bounds 15360,3072 and 5120/3 as the unit-rate model.

The effective scale may combine common clock, native-rate and metric factors:

\[
q=\alpha\beta/\lambda.
\]

If each positive factor lies within 1±1/4096, exact interval multiplication and division place q inside 1±1/1024. Their separate identities remain unidentifiable from the response. The signal-rank certificate does not need to separate them. Physical clock and metric identifications still need independent evidence.

The effective common-scale allowance 1/1024 is 2^28 times the previous common clock bound 2^-38. The primitive common-factor allowance 1/4096 is 2^26 times the former rate/metric cap. These comparisons concern different sufficient protocol envelopes and declared normalized coordinates, not a universal hardware improvement or a new theory constant.

## Residual shape errors around the fitted family

The fitted centre and residual plant parameters are constant through the batch. Describe actual normalized dynamics by

\[
G=\widetilde H^{-1}(qA+\Delta A+J),
\]

with `||Htilde-I||<=eta`, `||Delta A||<=4r`, and skew J of norm at most sigma. Here r bounds absolute normalized coefficient errors in the native rate shape after the common scale has been removed. It is not a raw relative error on each unnormalized fitted rate.

Taking `qplus=1+1/1024`, the residual generator difference from its own common-scale reference satisfies

\[
e\le\frac{4r+\sigma+4q_{+}\eta}{1-\eta},
\qquad \|e^{tG}\|\le g=\sqrt{\frac{1+\eta}{1-\eta}}.
\]

Preparation, readout, additional-output, origin and jitter limits remain respectively 2^-25,2^-25,2^-26,2^-29 and 2^-29 in normalized fitted coordinates. Set the three residual shape limits to

\[
\boxed{r=\eta=\sigma=2^{-35},}
\]

eight times the previous sufficient limits. With `a=sqrt(165/169)` and `tau=2^-28`, use

\[
u=g[(1+\rho)p+\rho a+a(4q_++e)\tau]+\nu,
\qquad v=gae.
\]

The response difference is bounded by u+vt relative to the appropriate member of the common-scale family. For the normalized finite Hankel matrix,

\[
\beta_M\le\sqrt{37}
\sqrt{u^2+2uv\frac{M-1}{2}
+v^2\frac{7M^2-12M+5}{24}}.
\]

Interval arithmetic certifies:

| M on each Hankel axis | Raw vectors per preparation | beta_M/s upper | Retained-signal condition bound |
|---:|---:|---:|---:|
| 2048 | 4095 | 0.209 | 19410 |
| 4096 | 8191 | 0.093 | 3385 |
| 8192 | 16383 | 0.116 | 1930 |

Every beta_M/s is below 1/4. Thresholding at half the declared reference-family signal lower bound selects 1893 directions. The condition numbers are looser than the prior tighter-residual certificate because this envelope permits larger residual errors. The relaxed result uses the Hankel-weighted bound directly; it does not require the older uniform per-raw-vector error ceilings.

Small additional observable singular values may occur under residual perturbations. No claim is made that the perturbed matrix has algebraic rank 1893 or that its dynamical kernel remains 747-dimensional.

## Shape calibration without separate common-scale anchors

The six effective directed ratios satisfy

\[
D_k=\alpha w_k/h_{k-1},\qquad U_k=\alpha w_k/h_k.
\]

Common clock and metric factors cancel from the relative metric reconstruction and the relative effective rates:

\[
q_k^2/q_0^2=\prod_{j=1}^k(D_j/U_j),\qquad
s_k=\sqrt{D_kU_k},\qquad
\frac{s_i}{s_j}=\sqrt{\frac{D_iU_i}{D_jU_j}}.
\]

Let the six estimated ratios lie in the earlier positive local domain, with each absolute estimation error at most 2^-39. Construct the fitted q values from the estimated metric ratios and take chat as the geometric mean of the three estimated s values. Require each estimated s_k/chat to lie within 1±2^-38. The separate common acquisition-scale interval must also hold.

With `ell=delta/(15/16-delta)`, delta=2^-39, the exact log error bound implies

\[
\|\widetilde H-I\|\le e^{6\ell}-1,
\]

\[
\max_k|\Delta a_k|\le
(1+1/1024)\left[(1+2^{-38})e^{7\ell}-1\right].
\]

The seven log-error contributions account for effective-rate normalization and the two neighboring fitted metric factors. Interval certification gives metric-shape error below 1.165e-11 and normalized native rate-shape error below 1.724e-11, both smaller than 2^-35. `SHAPE_CALIBRATION_GATE.json` records the proof bounds and exact reconstruction check for the candidate centre.

This is a sufficient gate on already bounded ratio estimates. It does not supply measurements at that precision, a bound on extra skew J, full-domain readout calibration or a physical clock correspondence. Common run-to-run scale changes must stay within the separately declared common-scale band, and noncommon changes must remain in the residual shape budget. Preserving correlated common-mode uncertainty may permit less restrictive absolute-ratio requirements than this simple gate.

## Calibration and interpretation limits

The older grade-calibration uncertainty bounds do not establish the new anisotropic shape limits: its metric uncertainty 5/10^10 and rate uncertainty 4/10^10 exceed 2^-35. They also do not establish the required correlation that would make most uncertainty a harmless common scale. The centre is illustrative, and no actual fitted data or calibration receipts were supplied.

The matched-family condition is a restriction on the three effective incidence rates. It is not a derivation that electromagnetic, weak or strong couplings unify, nor a theorem that measured rate ratios satisfy it. Generic unequal effective fitted rates require another certificate. Separate physical interpretation, full readout calibration and the hidden-generator obstructions from the preceding contract remain open.

Invertible Q and output rescaling do not add information: at an exact matched reference, the hidden space is Q^-1 N and still has dimension 747. The 37-input excitation limitations also persist under the similarity. A common-scale-tolerant rank certificate resolves neither those blind directions nor the coefficient ledger's Q139 clock bridge.

The next calibration task is to certify a finite measurement protocol delivering the six-ratio accuracy above while treating common scale as a nuisance parameter. Apply the matched-family gates explicitly; if the fitted effective rates are unequal beyond the allowed shape band, compute fresh modal or frequency-cluster bounds rather than transferring this certificate.

`validate_fitted.py` replays the exact construction and shape gate, verifies all source hashes and checks a small rational instance of the complete input/readout/retiming identity. Constructor verification is not independent review. No physical promotion or publication is claimed.
