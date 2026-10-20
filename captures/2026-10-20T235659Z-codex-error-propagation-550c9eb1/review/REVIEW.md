# Independent review of C28 deterministic error propagation

PASS for the conditional mathematics and exact finite checks. The actual error-input evidence and floating-estimator conformance remain HOLD. No acquisition, noise-tolerance measurement or actual estimator has been certified by this work.

The fixed object is PR307's normalized4096-sample half-step map in unit Euclidean chain coordinates, with inherited rank1999/kernel641 and inverse norm strictly below C=27648/61. The observable state target2^-39 is a declared target in these coordinates, distinct from the earlier six-ratio parameter target and other error gates.

## Observation bound and mixed terms

The root theorem correctly derives

\[
\|\widetilde y-Fx\|\le D=p+(X+p)b+\nu+\epsilon_{\rm enc},
\quad b\le\rho_{\rm rms}+T_{\rm rms}\xi+(5+\xi)\eta_{\rm rms}.
\]

The tighter per-sample RMS envelope includes rho_j plus min(2,t_j*xi+(5+xi)*eta_j). This follows from skew-generator isometries and Duhamel. The preparation contribution is separated through nominal propagation; the mismatch acts on x+p, so both state amplitude and the preparation/mismatch mixed term are necessary. Clock displacement acts under the actual generator, requiring the xi*eta term. The argument allows negative time offsets. Non-skew generator errors require a different growth estimate.

All stacked norms use the1/64 normalization. Coherent errors receive no automatic1/sqrt4096 reduction; arbitrary distinct sources are combined by triangle/Minkowski, not an independence-based RSS assumption. The scalar-to-vector noise conversion nu<=sqrt62*u<=8u is valid also at zero. The time-varying preparation extension using p_rms for the first term and p_max for the mismatch amplitude is sound. Multiple-preparation Frobenius aggregation is an exact block-norm identity, not an assertion of statistical independence.

The exact time moments independently agree: mean4095/4, second moment11180715/8, variance5592405/16. The centered affine-clock formula and its offset/relative-drift/jitter envelope are correct. Relative drift is scaled by the finite time horizon; jitter need not be orthogonal to that drift.

## Reconstruction is a separate conformance question

For the ideal nominal inverse the bound is ||F-dagger y-Px||<=C*D. The non-strict form correctly includes zero error. Its range is the nominal observable space V, so the full-state orthogonal error decomposition is valid for this ideal inverse. It is not valid for an arbitrary decoder unless its output range is separately certified in V.

For a specified implementation the full-state operator requirements ||B||<=beta and ||BF-P||<=alpha, plus a valid arithmetic bound on its input domain, give

\[
\|\widehat x-Px\|\le\alpha X+\beta D+\epsilon_{\rm alg}.
\]

These requirements do not follow from the map's condition number, a right-inverse identity, a forward fit or a finite preparation test. The exact F=[1,0], Q=(3/5,4/5), B=(1,4/3) control is verified: FB=1 and BFQ=Q, yet ||BF-P||=4/3. This preserves the validity of PR307's arbitrary-Q singular lower proof while blocking its misuse as an orthogonal-decoder certificate. Hidden-state ambiguity remains.

For a fixed linear perturbed map and b<s, the restriction to nominal V retains lower singular bound greater than s-b and condition at most(1+b)/(s-b). The complete perturbed kernel need not remain641-dimensional: added singular values can be positive but at most b. State-dependent bounded errors may satisfy the per-record envelope without defining a fixed linear map eligible for this SVD argument. The three-time exact map countermodel verifies rank2-to3 under arbitrarily small map error and a full-positive condition above4096 at epsilon2^-12. This is a logical control, not a claimed physical600-cell measurement.

## Source calibration gain and the conditional example

The reviewer rebuilt oriented boundary columns directly from the pinned source JSON. All100 entries of the selected Gram equal4I10. Thus absolute top-weight errors supported on J give exactly ||DeltaK||=2*max|delta d_j|. All600-column row/column sums also verify the conservative all-support gain at most sqrt8, hence at most3. Arbitrary individual weight errors need not preserve C10. For the selected nominal weight3/2, a relative cap r yields absolute cap3r/2 and generator cap3r. Other error classes require separate budgets. None of these identities supplies a measured weight uncertainty or physical law.

The independently checked root profile is entirely conditional:

| Derived quantity | Exact-comparison result | Display value |
|---|---|---:|
| Normalized observation error D | below2^-50 | 6.522560269672795e-16 |
| Ideal observable reconstruction bound C*D | below2^-40 | 2.956323710424811e-13 |
| Implemented-decoder bound under its stated alpha,beta,eps assumptions | below2^-40, hence below2^-39 | 7.887024366937112e-13 |
| Optional clock envelope | exactly5*2^-59, below2^-56 | 8.673617379884035e-18 |

ROOT_PROFILE_CHECKS.json retains the exact rational fractions. Every profile input and the actual B-conformance evidence remains explicitly UNSUPPLIED/HOLD. A selected absolute weight cap2^-67 would imply xi<=2^-66, but that cap has not been established. The fresh ideal total-data requirement D<=s*tau, with tau2^-39, is61/(27*2^49); it is a normalized aggregate norm, not a per-port threshold.

## Verification and binding

The independent reviewer executed only its own frozen standard-library checks, not the producer or an archived executable. The source weight calculation is a fresh data-only reconstruction. All eight root countermodels are independently verified, alongside separate reviewer controls. Four exact root-profile pairs agree with the independently derived fractions. All four final scientific JSON files are byte-identical to the producer replay. FINAL_BINDING.json pins the final checker, theorem, inherited PR307 receipt and source archive.

One minor prefinal endpoint wording was corrected: strict sqrt62*u<8u was made non-strict for u=0. The positive illustrative profile and all substantive arithmetic were unaffected; no mathematical retraction is required. The initial calculation was extended with the source calibration gain before final binding; the profile and model were unchanged.

This is same-team development review after disclosed conditional profile selection. It supplies no external promotion authority, actual input evidence, implementation-wide/all-backend guarantee or physical identification. Physical units, clock calibration and all actual error limits require their own evidence. The next implementation obligation is an actual decoder with full-domain BF-P, gain and arithmetic certificates.

Development — no registry entry. Conditional mathematics PASS; actual error evidence and estimator conformance HOLD. External review PENDING. Physical Promotion=0.
