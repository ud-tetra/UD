# Globally coupled affine-curl tightening of the enriched J1 certificate

DERIVED / EXACT CONDITIONAL. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion = 0. Refs #218 and #136; extends the frozen enriched-state certificate in PR247 without modifying it.

## Problem and fixed data

The center-enriched scalar-wave state has 2,809 nodes and 12,288 P1 tetrahedra at dimensionless omega=9/2 and gamma=1/10. Its own hierarchical RT1 certificate in PR247 had eta squared approximately 0.1972381069 and a shifted phase-circle output radius approximately 2.221119156. The present construction keeps that exact decoded state and the same continuum problem. It changes the admissible flux through a globally coupled correction.

Normalized measure has mass 2. Coordinates are (x,y,t=sqrt(2) z_phys), with gradient metric diag(1,1,2). The flux coordinates j=(tau_x,tau_y,sqrt(2) tau_z) have metric diag(1,1,1/2), so coordinate divergence is physical divergence. Every exact integral and the floating least-squares objective include the actual unequal measures: four children of measure 1/4096 and eight of measure 1/8192 per original parent. Frequency/time units remain the benchmark's dimensionless ct/a convention; no material sound speed or physical frequency is inferred.

## Global correction space

Reconstruct the immutable PR247 flux exactly from its saved free-coordinate words and the 8/8/12-child hierarchy. Add an affine divergence-free correction s from quadratic edge/face vector potentials. Write lambda_i for a local barycentric function and g_i for its coordinate gradient. For each sorted interior edge i<j use the two curls

    s_ij,i = 3 lambda_i (g_i cross g_j),
    s_ij,j = 3 lambda_j (g_i cross g_j).

They are curls of lambda_i or lambda_j times the Whitney edge potential lambda_i g_j-lambda_j g_i. For each sorted interior face (a,b,c), use two cyclic choices of

    s_abc = lambda_b(g_a cross g_c)
            -lambda_c(g_a cross g_b)
            +2 lambda_a(g_b cross g_c).

This is curl[lambda_a(lambda_b g_c-lambda_c g_b)]. Boundary edge and face potentials are excluded. Canonical global vertex order fixes all orientations. The same coefficient is shared by every incident cell, allowing nonzero normal transport across the old 1,024 parent patches.

The implementation does not assume a numerical rank or that this potential parameterization yields an exact global optimizer. It constructs an admissible correction and checks its realized reduction. Every local basis has zero divergence algebraically. Every actual assembled correction has zero affine divergence, continuous face normal traces at all three vertices, and zero exterior normal trace. Consequently the corrected RT1 flux still satisfies

    div(tau+s) = z v-F,
    R=F-zv+div(tau+s)=0.

These identities are also checked directly on the final corrected flux, separately from the correction-only checks.

## Floating proposal and exact posterior audit

The L2 affine projection of the old flux is computed exactly on every cell. A sparse least-squares system minimizes its norm after the global affine correction. The cell block is the Cholesky factor of the P1 mass matrix, multiplied by the square root of the actual cell measure and the physical flux metric. Positive diagonal column scaling is used before LSMR. Solver status, iterations and residual diagnostics are saved as numerical proposal metadata. They are not premises of the certificate or claims of exact optimality.

The actual coefficient words are stored component-major as little-endian IEEE754 binary64 in CURL_COEFFICIENTS.bin.gz. CURL_WITNESS.json binds their hash, dimensions and canonical edge/face topology digest. Replay decompresses, checks byte count and finiteness, and converts each saved word to an exact Fraction. No Krylov solve is rerun in replay.

The exact audit checks gradient orthogonality integral(s dot grad v)=0 for each real component and the norm-change identity

    ||tau+s||^2-||tau||^2 = 2(tau,s)+||s||^2 <=0.

The mixed moments use the exact affine projection of tau and the exact cell mass; no sampled quadrature enters. The final full RT1 norm and real/imaginary covariance are recomputed independently through degree four and compared with the old frozen norms plus these exact changes. This comparison catches unequal-volume, projection or assembly inconsistencies.

Controls reject truncated and nonfinite coefficient payloads and a corrupted exterior affine trace. The inherited hierarchy controls additionally reject incompatible zero-normal divergence, a corrupted final boundary trace, truncated hierarchy free coordinates and nonfinite hierarchy words. Constructor checks do not constitute independent review.

## Continuum output enclosure

For the exact continuum solution u, let H=ell(u), J(v)=2 ell(v)-b_z(v,v), D=tau+s-grad v, eta squared=integral |D| squared, and q=integral D dot D (bilinear, without conjugation). Exact symmetry gives H-J(v)=b_z(u-v,u-v), even for the inexact saved state. Exact integration by parts gives residual r(w)=integral D dot grad w, hence ||r||_{V'} <= eta.

The inherited spectral-circle proof applies unchanged. At this fixed parameter pair,

    c=1/2-45i/4,  delta squared=2029/16,
    |H-[J(v)+c q]| <= delta eta squared,
    |H-J(v)| <= 2 delta eta squared.

The full norm budget includes solenoidal components; they cannot be dropped from the circle estimate. The reported shifted proxy is rounded to two actual binary64 words and its outward evaluation error is added. The J-centered radius includes the saved J evaluation bound. UPPER precision conclusions are determined by exact rational comparison with 1/10; display decimals are approximations only.

An additional correction-family diagnostic is the exact within-cell quadratic remainder

    floor = ||tau|| squared-||Pi_P1 tau|| squared.

It is invariant under every affine correction and lower-bounds the flux defect norm squared for this frozen initial quadratic part. It is not a lower bound on the actual transfer error or on every possible flux/dual certificate.

## Scope and provenance

Only the frozen point omega=4.5,gamma=0.1 is certified here. No uniform-band accuracy, continuum rate constant, finite termination rule, exact least-squares optimality or all-input floating-point guarantee follows. Earlier frozen-state no-go results retain their original state/family scopes. The shifted proxy is a derived certified estimate, not another FEM solve.

This is the externally declared scalar-wave benchmark on the J1 domain. The coefficient ledger Q169-Q179 concerns incidence/support dynamics and does not derive the benchmark scalar-wave action or damping. The uploaded CRL2 subdivision document remains a governance proposal, not enacted by citation. The missing Gap2_FINAL_Finite_Genesis.png was not read or used. No native UD constitutive, horn/material, GR/QFT or empirical claim is promoted.

## Reproduction

Run `python3 captures/2026-10-19T213658Z-codex-j1-coupled-curl-86434624/replay.py` from the repository. It hashes all immutable source dependencies, reconstructs both frozen hierarchy and global correction using exact rational arithmetic, checks all constraints and compares both frozen result JSON files. NumPy and SciPy are used only for proposal generation. The exact replay uses standard-library arithmetic. REPLAY.log records completion; the repository integrity verifier separately checks hashes and append-only inventory/events.

## Captured result

Exact posterior checks PASS. The saved floating proposal used 302 LSMR iterations for each component; numerical stopping diagnostics do not prove exact optimality. The mesh has 13,560 interior edges and 23,808 interior faces, giving 74,736 potential coefficients per real component. All 7,424 old parent interfaces carry nonzero corrections at their vertices.

| Quantity | Prior hierarchical flux | Globally coupled flux |
|---|---:|---:|
| eta squared | 0.19723810689739968 | 0.12395170889381193 |
| Radius about reported corrected J | 4.442238311890338 | 2.791666573634287 |
| Radius about own derived shifted proxy | 2.2211191559451198 | 1.3958332868170942 |

The new shifted proxy is approximately -4.215921931027678-2.380933884989171 i. Display decimals are approximations; UPPER_RESULTS fractions from PR247 and this capture's COUPLED_RESULTS.json carry the authoritative outward radii and actual reported center words. The radius decreased by approximately 37.16% for the same frozen state and residual. This is a certificate tightening, not a change in the actual state or its continuum error. The exact 1/10 precision comparison fails for both new disks; a failed upper certificate does not prove actual output error exceeds 1/10.

Validation includes 230,016 local basis-divergence identities, 24,576 actual correction-divergence checks, 152,064 correction face-vertex/component normal checks, two exact global gradient-orthogonality identities and two exact norm decreases. The inherited 98,304 direct final divergence checks and 152,064 final trace checks are repeated on the complete corrected RT1 flux. Full degree-four norms match the old norms plus the independently integrated changes exactly; defect covariance is positive semidefinite.

The exact affine-invariant quadratic remainder floor is approximately 0.000035735864034601356. This particular local floor is below the 1/10 circle obstruction threshold and gives no new no-go conclusion. The strongest prior tested residual dual-norm squared lower bound remains approximately 0.0029313793985937704, while this own upper bound is approximately 0.12395170889381193. Neither sparse-solver stopping nor the residual bound gap is converted into an optimality or physical claim.

Next gate: construct a conforming enriched dual/Riesz test lower certificate to measure the residual bound gap and decide whether further flux work or state enrichment is warranted. A goal-oriented adjoint certificate is an alternative for tightening the output directly. Independent review, full-band accuracy, finite stopping and the native UD bridge remain open.
