# P2 projected-source RT1 continuum certificate and local frequency bounds

DERIVED / EXACT CONDITIONAL. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion=0. Refs #218, #136. Extends the P2 state captured in PR251. Older frozen-state results remain unchanged. Concurrent PR252 evidence is preserved.

## Result

The saved 18,673-DOF conforming P2 state at omega=9/2, gamma=1/10 now has an actual flux-plus-volume-residual continuum upper certificate. Its reported corrected output remains approximately

    J = -4.781059743930876 - 1.1058532364256974 i.

The new J-centered radius is 0.0127860733196308. Recentring the new shifted disk gives the slightly smaller selected radius 0.0127825195404181 about the same actual reported J. Both certify the declared pointwise 1/10 continuum target. This replaces the previously selected bound 2.7905416462650745 for this state by a tighter bound; it does not alter that earlier evidence.

The new shifted output proxy is approximately

    C = -4.778231920858928 - 1.1110713541364545 i,

with certified radius 0.00684742596325596, including the actual center evaluation budget. C and J are different estimators; their radii must not be exchanged without recentering. All decimals displayed here are approximations; UPPER_RESULTS.json contains exact rational upper bounds and binary64 center hex words.

The pointwise target also passes using the simpler global Poincare residual inequality, without a local residual lift: its J-radius is approximately 0.0276827044692568. The local lift tightens it further.

A uniform exact-model corrected-estimator family on [4.495,4.505] at fixed gamma=0.1 has radius at most 0.053668. This is a bound for an exact symbolic frequency-dependent estimator. It is not a uniform floating-evaluation or solver guarantee, and it does not close the full [0,6] x [0.1,1] band audit.

## Constructed flux and actual coefficients

The mesh is unchanged: 2,809 vertices, 15,864 edge midpoint state nodes and 12,288 tetrahedra, with all Neumann boundary state nodes included. Normalized measure is 2; cell measures are 1/4096 and 1/8192. Coordinates are (x,y,t=sqrt(2) z_phys). The physical gradient metric is diag(1,1,2), flux norm metric diag(1,1,1/2). Source F=10(x+y) remains externally declared and meanfree. Frequency is dimensionless under ct/a; no physical hertz value is inferred.

Let v be the exact decoded two-word P2 state from PR251, with its exact weighted mean removed. Let Pi v be its broken cellwise affine L2 projection. Construct tau in H_0(div) with

    div tau = z Pi v - F,   z=-81/4+9i/10.

Three exact L2 projection levels permit the existing RT1 hierarchy: 16 root cells, then 128 and 1,024 local patches, ending in the same 12,288 cells. Root and patch free coordinates are proposed by binary64 linear algebra and saved in UPPER_WITNESS.json.gz. Exact rational constraint reconstruction enforces compatibility and face traces, independently of the numerical minimizer's convergence.

Global quadratic edge/face potentials add an affine divergence-free curl. There are 13,560 interior edges and 23,808 interior faces, hence 74,736 coefficients per real component. Unequal cell measures and the physical flux metric enter the least-squares objective. The numerical proposals converge in 302 LSMR iterations per component and are saved as actual binary64 words in CURL_COEFFICIENTS.bin.gz. Exact arithmetic, rather than the stopping criterion, establishes validity and flux-norm decrease. No global optimality or all-input IEEE claim follows.

Direct final audits check 98,304 affine divergence values and 152,064 face-vertex-component normal traces. The curl audit checks 24,576 actual affine divergences, the same 152,064 correction traces, and two exact global orthogonality identities against the full P2 gradient. Corrections cross all 7,424 old parent interfaces. The squared norm changes are approximately -0.06703531174173212 and -0.003199615298947478.

## Volume residual and local lift

The RT1 flux is equilibrated with the projected source, not with the full P2 source. Its nonzero residual is

    R=F-zv+div tau=z(Pi v-v).

R has zero mean on every tetrahedron. The exact projection reproduces PR251's budgets:

    ||R|| squared = 0.000585120770412596,
    nu squared = sum_K diam(K)^2/9 * ||R||_K^2 = 7.43652891543635e-07.

Payne-Weinberger on each convex tetrahedron, with pi>3, gives a weak zero-normal local lift psi_K satisfying -div psi_K=R_K and ||psi_K||<=diam(K)/3 ||R_K||. Joining these lifts gives psi in H_0(div), ||psi||<=nu, and tau+psi exactly equilibrated with the full source. The lifts are supplied by existence and a rigorous norm bound; no explicit polynomial full-source lift is claimed.

For D=tau-grad v and d=||D||, the actual degree-four norm audit gives

    d squared = 0.000527359173396899,
    ||r||_(dual V) <= d+nu,
    ||r||_(dual V)^2 <= 0.000567709501189457.

The global alternative is ||r||<=d+(1/2)||R||. Both apply to the actual saved state without assuming exact Galerkin arithmetic.

## Correct projected-mass cross-terms

The scalar norm and bilinear covariance use the projected state mass:

    ||D||^2=||tau||^2+||grad v||^2-2 Re ell(v)-2*(81/4)||Pi v||^2,
    integral D dot D=integral tau dot tau+integral grad v dot grad v
                    -2 ell(v)+2z integral (Pi v)^2.

The corrected state output J=2ell(v)-b_z(v,v) still uses the full P2 state mass. Replacing projected mass by full mass in the defect cross-term would understate the defect norm. The saved replay independently integrates the full affine P2 gradient against the quadratic flux through degree three and checks each real norm, imaginary norm and covariance against these integration-by-parts identities. It also reproduces J and the earlier exact projected-source residual budget.

For kappa=sqrt(2029)/2, the corrected output identity gives

    |H-J(v)| <= kappa (d+nu)^2.

For c=1/2-45i/4, delta=|c|=sqrt(2029)/4 and q_D=integral D dot D, the phase proxy is J+c q_D. Apply the existing spectral-circle theorem to D+psi and bound the unknown center shift by delta*(2d nu+nu^2). This yields

    |H-(J+c q_D)| <= delta*(d^2+4d nu+2nu^2).

Actual center evaluation bounds are added outward. UPPER_RESULTS records both actual reported estimators and their distinct radii.

## Exact symbolic local frequency band

Keep the same state v and gamma=1/10. Define z(w)=-w^2+2i gamma w. The exact frequency-dependent corrected estimator is

    J_w(v)=J_w0(v)-(z(w)-z(w0))*integral v^2,  w0=9/2.

The residual identity and global Poincare bound give

    ||r_z|| <= d+nu + (1/2)|z-z0| ||v||_L2.

On [w0-rho,w0+rho],

    |z-z0|^2 <= [rho(2w0+rho)]^2+(2gamma rho)^2,
    kappa(w,gamma) <= sqrt(1+[(w0+rho)/(2gamma)]^2).

Multiplying this kappa upper by the squared residual upper gives a uniform exact-model output radius. LOCAL_BAND_RESULTS.json records rational outward square roots, the fixed state's full L2 mass and the exact symbolic estimator. No frequency sample interpolation is used.

| Frequency interval, gamma=0.1 | Uniform exact-model radius | 0.1 target |
| --- | ---: | --- |
| 4.499–4.501 | 0.0187065074 | PASS |
| 4.498–4.502 | 0.0257533360 | PASS |
| 4.495–4.505 | 0.0536671450 | PASS |
| 4.49–4.51 | 0.1228577732 | OPEN: bound exceeds target |
| 4.48–4.52 | 0.3469183643 | OPEN: bound exceeds target |
| 4.46–4.54 | 1.1430406733 | OPEN: bound exceeds target |

An upper bound exceeding 0.1 is an uncertified interval, not proof of actual error exceeding 0.1. These local bounds do not establish a full-band floating implementation, a convergence rate constant, finite stopping or native UD dynamics.

## Verification and controls

The frozen-source hashes are checked before replay. Saved-coefficient replay reconstructs the full flux, verifies source projection, constraints, final traces, exact P2-gradient orthogonality, direct norm/covariance integration and both pointwise/local-band output bounds. Controls reject incompatible divergence, corrupted exterior normal trace, truncated/nonfinite hierarchy coefficients, truncated/nonfinite global curl payloads, and an incorrect full-mass defect cross-term. Constructor checks are not non-constructor review.

Run `python3 captures/2026-10-19T225423Z-codex-j1-p2-projected-flux-8a5ce1f3/replay.py` from the repository root. The captured REPLAY.log must finish with matching UPPER_RESULTS and matching LOCAL_BAND_RESULTS. NumPy/SciPy are needed only for numerical proposal generation; saved-coefficient replay uses standard-library exact rational arithmetic. The repository verifier separately checks SHA-256 inventory and append-only event coverage.

## Governance and next gate

The supplied coefficient ledger does not derive this benchmark's scalar-wave action, source, damping or metric from native UD support dynamics. The CRL2 subdivision document remains a proposal, not an enacted rule by citation. Gap2_FINAL_Finite_Genesis.png was unavailable and was not used.

Scientific status remains OPEN for the wider program. Independent review, actual floating frequency-band certification, full-band precision, finite termination and the native UD action/observable bridge remain open. Development — no registry entry; physical promotion=0. No horn/material, GR/QFT or empirical identification is claimed.
