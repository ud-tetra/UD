# Same-carrier energy, clock and support theorem v0.1

EXACT CONDITIONAL. Development — no registry entry. Physical promotion 0.

## Declared carrier and apparatus hypotheses

On the nonzero active sector of the filled tetrahedron, let A=2J, J^T=-J, J^2=-I and x'=Ax in native update parameter s. Define a=||x||^2>0. The source ledger Q283 gives H_Hodge=a, Q284 gives phase rate 2/tau0 under t=tau0*s, and Q285 uses native dimensional energy E=(A0/tau0)*a. Physical equality to a measured apparatus energy is a separate hypothesis, not a consequence of matching spectra.

Let z=Mx with M injective on the active sector; physical time t=tau0*s, tau0>0; calibrated quadratic energy E(z)=(1/2)z^T G z, with its baseline removed and all included degrees specified. The simultaneous map conditions are KM=MA/tau0 and M^T G M=(2A0/tau0)I, where z_dot=Kz on the invariant image. These are proposed correspondence conditions. A physical device has not satisfied them here. An instantaneous energy/period measurement alone does not verify them.

## Theorem 1: observable product and normalization ambiguity

Under these hypotheses, E=(A0/tau0)*a and the primitive full-state recurrence is T_state=pi*tau0. Hence A0*a=E*T_state/pi. For any c>0 the replacements x_new=c*x, M_new=M/c, a_new=c^2*a, A0_new=A0/c^2 leave z, K, G, tau0 and all physical observations constructed from z unchanged, and preserve both map equations. Therefore measured E and T_state do not identify A0 without an independent constraint on a or the absolute amplitude map M. They identify A0*a. This is a no-go only within a model class admitting this rescaling; additional independently justified amplitude/quantization laws can remove it.

Proof: exp(sA)=cos(2s)I+sin(2s)J, so nonzero real x returns first at s=pi. The quadratic pullback yields E=(A0/tau0)||x||^2. Multiplying by T_state proves the product identity. Direct substitution verifies both rescaled map equations, while M_new*x_new=M*x and A0_new*a_new=A0*a. Thus all observations depending only on unchanged physical trajectories and energy remain the same. A0 changes continuously with c, proving nonidentifiability.

The previous anchor-identifiability theorem is retained: E0 and tau0 identify A0=E0*tau0 when E0 is independently known. Here the measured total energy is E=E0*a, so it is not that anchor when a is unknown. In log variables (A0,tau0,a), energy and primitive period constrain rows (1,-1,1) and (0,1,0); (1,0,0) is outside their row span. The ambiguity witness is (-1,0,1). Adding an independent norm anchor (0,0,1) closes the rank condition.

Constructive calibration corollary: given an independently calibrated absolute M and left inverse L (LM=I), define C=LKM and B=M^T G M. The map holds if KM=MC (no leakage), C=gamma*A with gamma>0, and B=lambda*I with lambda>0. Then tau0=1/gamma and A0=lambda/(2*gamma). Substitution proves the equivalence with the two map equations. This target-blind extraction rule still requires the independently fixed absolute scale of M; energy or spectrum alone does not establish these matrix conditions.

## Theorem 2: readout period is part of the map

The half-period state is -x. Every even readout f(-x)=f(x) is therefore periodic with period at most T_state/2 (or is constant). A nonconstant homogeneous quadratic readout along the orbit has primitive period exactly T_state/2. A nonzero signed linear readout with nonzero orbit projection has primitive period T_state. For example, on one active plane x=(cos(2s),sin(2s)), x_1 has period pi, x_1^2 has period pi/2, and energy is constant. Thus an energy trace cannot supply the required clock, and an unqualified quadratic recurrence can cause a factor-two action error. A projective/sign-blind observable also cannot certify the signed state period without an appropriate reference. No physical spinor or quantum phase identification is implied.

Proof: exp((pi/2)A)=-I. A quadratic form evaluated on cos(2s)x+sin(2s)Jx has only a constant and fourth-harmonic sine/cosine terms. If nonconstant, the primitive period is pi/2. A nonzero linear orbit projection contains a second-harmonic sinusoid and has primitive period pi. More general even readouts can have shorter periods; no universal primitive period is asserted for them.

## Corollary: independent support calibration and finite intervals

Let rho=T_read/T_state be independently certified for the actual readout. Then A0=E*T_read/(pi*rho*a). Suppose a joint deterministic certificate gives positive E_-<=E<=E_+, T_-<=T_read<=T_+, rho_-<=rho<=rho_+, and 0<a_-<=a<=a_+. Then

E_- T_-/(pi rho_+ a_+) <= A0 <= E_+ T_+/(pi rho_- a_-).

This interval remains valid with correlated errors, provided their joint coverage is certified. Statistical coverage is not supplied by algebra. If a_->0 cannot be established, this argument supplies no finite upper action bound.

If an independently calibrated absolute map reconstructs xhat with ||x-xhat||<=delta, then a lies between max(0,||xhat||-delta)^2 and (||xhat||+delta)^2. Derivation: triangle and reverse triangle inequalities. Map uncertainty, unobserved-mode leakage and readout error belong inside delta. Choosing ||x||=1 as a mathematical ray convention is not independent physical support calibration.

## Experimental entry contract and source boundary

Require the exact active sector and same carrier; signed phase/readout law and primitive-period certificate; an independently calibrated energy functional G and zero-energy baseline; the intertwiner/time map; an absolute amplitude map or independent support law; joint uncertainty certificates; and a frozen estimator/comparison rule before QPB1 scoring. Identify all calibration dependencies on the target. Circuit action Phi0*Q0 and Hodge A0 remain distinct until their map is demonstrated. No physical apparatus, dataset, independent norm anchor or empirical score is admitted here. The measurement contract is proposed, not preregistered.

Source: recovered v0.85 ledger SHA-256 8845ca23e178e043ef0c7bac01be3afba9cabbefd866c366921387a8ca843aec, especially Q282–Q288 and O54–O55. The native-action identifiability theorem in capture 2026-10-21T160300Z-codex-action-identifiability-32b8a1d4 supplies the rank test. Its known-coefficient premise remains intact; this theorem shows why total energy is not automatically a known native energy-unit anchor. Q287/Q288 remain quarantined. EXIT-03 remains HOLD. Constructor: Codex root; non-constructor review pending. Physical promotion 0.
