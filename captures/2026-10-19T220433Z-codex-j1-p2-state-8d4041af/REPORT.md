# Conforming P2 J1 wave state and paired residual audits

DERIVED / EXACT CONDITIONAL. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion = 0. Refs #218 and #136. Extends PR249 on a new state; the old frozen-state no-go remains intact. Concurrent PR250 is preserved.

## Result and scope

Solved the conforming quadratic P2 wave system at omega=9/2, gamma=1/10, on the same 12,288 tetrahedra. The 2,809 vertices plus all 15,864 edge midpoints give 18,673 state degrees of freedom, including boundary nodes for the Neumann problem. The exact decoded two-word state is meanfree. Its corrected output is approximately

    J_P2 = -4.781059743930876 - 1.1058532364256974 i.

Actual floating output evaluation plus the finite-Galerkin algebraic solve budget is bounded by approximately 4.538e-15 for the raw output and 3.7605e-14 for the corrected output; both pass the declared 1e-10 algebraic target. These are algebraic budgets relative to the exact P2 Galerkin solution. They do not certify the continuum output to that precision.

The old P2 Riesz Gram and residual pairings and the old local quartic-bubble lower are reproduced exactly before comparison. On the new state, the same P2 Riesz-test squared lower is approximately 6.4897893975863e-55. Since these test functions now lie in the P2 trial space, this reflects the tiny Galerkin algebraic residual and does not bound the entire continuum residual from above. The local quartic-bubble squared lower drops from approximately 0.002931379398594 to 0.0000133488620642872, a ratio of about 0.00455378 on that same family.

Neither tested lower establishes the former phase-circle obstruction for this new state. This is not an accuracy pass, a full-residual reduction theorem or a universal absence of obstruction. The old PR249 no-go remains true for its own frozen P1 state.

A valid upper for the new state is derived by transporting the old equilibrated flux and bounding its now-nonzero volume residual. This upper is conservative: corrected-J radius approximately 3.877780258127. Recentring the older certified output disk gives the smaller radius approximately 2.790541646265 about the new reported J; it is selected as the current bound at that center. Neither reaches 0.1. All displayed decimals are approximations. P2_RESULTS.json contains exact fractions and P2_WITNESS.json contains the actual reported output hex words.

## Exact geometry, P2 forms and state proposal

The normalized measure is mu(Omega)=2; coordinates are (x,y,t=sqrt(2) z_phys), and the physical gradient metric is diag(1,1,2). The same actual measures 1/4096 and 1/8192 are used. Frequency and time remain dimensionless under ct/a; no physical sound speed or frequency is inferred.

Use nodal P2 barycentric basis N_i=lambda_i(2 lambda_i-1), N_ij=4 lambda_i lambda_j. Shared vertex/edge values determine identical quadratic traces on each common face, so the space is conforming H1. The stiffness matrix is assembled exactly using the affine basis gradients and physical metric. The normalized reference mass matrix is integrated through degree four by

    integral lambda^e / mu = 6 product(e_i!)/(3+sum e_i)!.

Local P1 energy and mass nesting are checked exactly. Global mass row sums equal the signed P2 basis integrals; total measure is 2. The affine source F=10(x+y) is represented exactly, has zero integral and squared L2 norm 20. The stiffness annihilates constants. Final sparse nonzero counts are 476,221 stiffness entries and 491,713 mass entries.

A complex sparse SuperLU solve proposes the high words. Its exact decoded, meanfree residual is evaluated and one residual correction solve proposes the low words. P2_STATE.bin.gz stores four arrays of actual little-endian binary64 coefficients: high real, high imaginary, low real, low imaginary. Replay sums each word pair as an exact rational and subtracts the exact weighted mean divided by 2. The reported raw and corrected outputs are actual floating evaluations from the proposal backend and are audited against the exact decoded state. No all-input IEEE guarantee is claimed.

## Positive algebraic residual bound for P2

P2 vertex basis means are negative. The positive P1 lumped-weight residual bound cannot be reused with them. Instead, the exact reference mass matrix obeys

    M_ref >= alpha I,  alpha=1/1000,

as proved by positive exact LDL pivots of M_ref-alpha I. For W_i=sum of incident cell measures, assembly gives M_P2>=alpha diag(W), with every W_i>0. This is an exact algebraic lower certificate, not an empirical spectral constant. The signed integration weights are used only for mean removal and integration.

The residual vector annihilates constants exactly. For its real/imaginary coefficients rho and a meanfree P2 test, the continuum Poincare constant 1/2 yields

    epsilon squared = (1/(4 alpha)) sum_i |rho_i| squared/W_i
                     >= ||rho||_(V_P2') squared.

At this point beta squared=4/2029 and kappa squared=2029/4. With ||ell||<=sqrt(5), the raw finite-Galerkin output budget is sqrt(5 epsilon_squared/beta_squared), and the bilinearly corrected budget is kappa epsilon_squared. Both add the actual outward output-evaluation error. The corrected identity J(v)=2 ell(v)-b_z(v,v) holds for the saved inexact state. The algebraic bounds and the continuum bounds are recorded separately.

Controls reject truncated and nonfinite state payloads. A structural guard confirms the signed P2 means cannot serve as a positive lumped residual norm. Constructor verification remains separate from independent review.

## Paired lower audits

The prior two Riesz tests are decoded from the immutable PR249 payload. Their energy Gram is recomputed using the new exact global P2 stiffness assembly and matches the previous cellwise energy Gram exactly. The old P1 state is embedded by edge averages; its residual pairings and dual lower reproduce the frozen PR249 values exactly. Only then are the new P2 state pairings evaluated with the same tests and Gram.

The independent local tests are the quartic cell bubbles B=lambda_0 lambda_1 lambda_2 lambda_3, which vanish on each cell boundary. Their supports are disjoint, so their squared dual lower contributions sum. Physical cell gradients g_i give energy

    integral |grad B| squared = mu sum_i |g_i|_physical squared/15120.

For a quadratic state, the source pairing includes its constant physical Laplacian. Exact bubble moments are integral(B)/mu=1/840, integral(N_i B)/mu=-1/10080 and integral(N_ij B)/mu=1/3780. Old P1 Laplacians vanish exactly and the old local-bubble result reproduces. The new P2 Laplacian is retained. Dropping it would give the wrong residual. Overlapping Riesz/bubble families are combined by max, not by summation.

## Valid transported continuum upper

Let v_1 be the old frozen state and tau_1 its verified equilibrated flux, with div tau_1=z v_1-F and zero exterior normal trace. Let d_v=v_2-v_1 and D_1=tau_1-grad v_1. Reusing tau_1 on v_2 gives

    D_2=D_1-grad d_v,
    R_2=F-z v_2+div tau_1=-z d_v.

Its exact defect norm is obtained without reconstructing or altering the old flux:

    ||D_2|| squared = eta_1 squared + ||grad d_v|| squared
                     -2 Re r_1(conjugate(d_v)).

The old residual pairings are assembled directly in P2. The volume residual norm is |z| squared times ||d_v||_L2 squared, integrated through degree four. Numerically these squared norms are approximately 0.018707448363244925 and 0.3095043413280397. Global Poincare gives

    ||r_2||_(V') <= ||D_2|| + (1/2)||R_2||,
    |H-J(v_2)| <= kappa ||r_2||_(V') squared.

The resulting upper and actual center-evaluation budget are valid, though loose. No new exactly equilibrated flux or new shifted phase proxy is claimed for v_2.

## Next upper certificate: projected-source RT1

An exact, implementable conditional route is recorded in PROJECTED_SOURCE_CONTRACT.json. Let Pi v_2 be the broken cell L2 affine projection. Construct an RT1 flux with

    div tau=z Pi(v_2)-F,  tau dot n=0.

This uses the same degree-one divergence space as the existing hierarchy. Its residual R=z(Pi v_2-v_2) has zero mean on each tetrahedron. Convex-cell Poincare gives a zero-normal local flux lift with global norm bounded by nu, where

    nu squared <= sum_K diam(K) squared/9 * ||R||_(L2(K)) squared.

Here diam/pi<diam/3 uses pi>3. The exact projection moments are checked; the captured volume-residual squared norm is approximately 0.0005851207704125963 and the local lift budget squared is approximately 7.436528915436351e-7. This is a budget for a future flux, not an evaluated new output certificate.

For an actual such flux, set D=tau-grad v_2, d=||D|| and q_D=integral D dot D. Then ||r||<=d+nu gives J-centered radius kappa(d+nu)^2. A shifted certificate is also available without computing the local lifts: with c=1/2-45i/4 and delta squared=2029/16, use center J+c q_D and radius

    delta*(d squared+4 d nu+2 nu squared),

plus its actual evaluation budget. To prove this, choose zero-normal local lifts psi with -div psi=R and ||psi||<=nu; tau+psi is exactly equilibrated. Apply the existing spectral-circle theorem to D+psi, and bound the center difference by |c|*(2 d nu+nu squared), with |c|=delta.

The norm/covariance audit must use projected mass: integration by parts gives

    d squared=||tau|| squared+||grad v_2|| squared
              -2 Re ell(v_2)-2*(81/4)||Pi(v_2)|| squared,
    q_D=integral tau dot tau+integral grad v_2 dot grad v_2
         -2 ell(v_2)+2 z integral (Pi(v_2)) squared.

Using the full P2 mass in place of projected mass would understate the defect norm. The future actual flux still needs direct divergence, face-trace, norm/covariance and output-evaluation checks before any precision conclusion.

## Governance and reproduction

The scalar-wave action, damping, source and physical metric remain externally declared benchmark data. The coefficient ledger Q169-Q179 does not derive them from native UD incidence/support dynamics. The CRL2 subdivision file remains a governance proposal. Gap2_FINAL_Finite_Genesis.png was unavailable and was not read or used.

Physical promotion remains 0; there is no authoritative registry entry. Independent review, native UD correspondence, full-band precision and finite termination remain open. No empirical, horn/material or GR/QFT identification follows from this solve.

Run `python3 captures/2026-10-19T220433Z-codex-j1-p2-state-8d4041af/replay.py` from the repository. It verifies source hashes, reconstructs exact forms and saved state, reproduces the two prior lower audits, and compares P2_RESULTS.json. NumPy/SciPy are needed only for proposal generation. Exact replay arithmetic uses the standard library. REPLAY.log records completion; the repository integrity verifier separately checks hashes and append-only capture/event coverage.
