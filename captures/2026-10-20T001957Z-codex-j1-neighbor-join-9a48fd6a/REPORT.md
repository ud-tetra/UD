# Neighboring P2 state and joined certified J1 frequency intervals

DERIVED / EXACT CONDITIONAL. Native floating claims assume the declared IEEE binary64 round-to-nearest, ties-to-even operation model. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion=0. Refs #218 and #136. Extends PR255; all earlier captures remain unchanged.

## Result

Constructed a new P2 wave state at

    omega_1 = 289/64 = 4.515625,  gamma=1/10.

Its corrected output is approximately

    J_1 = -4.6286042307053075 - 1.0368334288713472 i.

The actual sparse-evaluation algebraic output budget is below 2.087e-13, passing the 1e-10 finite-Galerkin target. Its newly constructed continuum certificate has selected reported-J radius below 0.011995. The separate shifted proxy has radius below 0.006429. The continuum certificate is derived at the new frequency; no old-frequency output disk is inherited.

The new actual compact floating evaluator passes the absolute continuum target 1/10 uniformly on [4.507125,4.524125], fixed gamma=0.1, with combined continuum-plus-evaluation radius below 0.093372. Its floating-evaluation contribution is at most 6.520e-16.

Join it to PR255's interval using the exact midpoint of the overlap:

    switch = 577/128 = 4.5078125.

| Certificate | Frequency interval | Uniform total radius |
| --- | --- | ---: |
| Original state / PR255 evaluator | [4.4915, 4.5085] | <0.099117 |
| New neighboring state / evaluator | [4.507125, 4.524125] | <0.093372 |
| Joined exact selector | [4.4915, 4.524125] | <0.099117 |

The overlap is [36057/8000,9017/2000]=[4.507125,4.5085], of width 11/8000=0.001375. The joined width is 261/8000=0.032625, a factor 261/136 of the previous width: approximately 91.91% wider. These are absolute scalar-wave output bounds for represented binary64 inputs, conditional on the declared IEEE semantics. Decimal table values are outward-readable summaries; the JSON results contain exact rational bounds and actual output hex words.

## Neighboring state and finite-Galerkin audit

The domain, normalized measure, source and finite-element space are unchanged: 12,288 tetrahedra, 2,809 vertices and 15,864 edge midpoints, giving 18,673 P2 state degrees of freedom with Neumann boundary nodes included. The ordered topology hash equals PR251's. Both states use the same frozen rational mesh routine and affine source-load expression; the latter is checked by AST equality, in addition to the exact source squared L2 norm 20. The source is F=10(x+y), with zero mean, and mu(Omega)=2.

Coordinates remain (x,y,t=sqrt(2) z_phys), with physical gradient metric diag(1,1,2) and flux norm metric diag(1,1,1/2). Frequency is dimensionless under ct/a; no Hertz calibration is inferred.

A new complex sparse solve and one exact-residual refinement propose four binary64 arrays: high real, high imaginary, low real, low imaginary. The state is decoded as exact rationals and its exact weighted mean is removed. P2_STATE.bin.gz and P2_WITNESS.json identify the actual saved state; no solver-tolerance assumption substitutes for the posterior residual audit.

The positive reference mass bound M_ref >= (1/1000) I is checked by exact LDL pivots. Positive incident-cell weights are used for the residual bound; signed P2 vertex basis means are not used as positive norm weights. The continuum Poincare constant 1/2 remains unchanged. At the neighboring frequency,

    beta^2=4096/2092121,  kappa^2=2092121/4096.

The finite-Galerkin output error and actual sparse output evaluation error are recorded separately from the continuum error. Passing the algebraic target does not itself certify the continuum target. Truncated/nonfinite state payloads are rejected.

## New continuum flux certificate

For the new exact decoded state v_1, let Pi v_1 be its broken affine cell L2 projection. Construct a new RT1 flux tau in H_0(div) with

    div tau=z_1 Pi v_1-F,
    z_1=-(289/64)^2+i*(289/320).

A three-level hierarchical construction and a global affine-curl correction provide actual saved free-coordinate witnesses. The global correction has 74,736 coefficients per real component and includes the unequal cell measures. Floating proposals are reconstructed and checked in exact rational arithmetic; no exact optimality is claimed.

The full P2 source residual is nonzero:

    R=z_1(Pi v_1-v_1),
    nu^2=sum_K diam(K)^2/9 * ||R||_K^2 = 7.050922969026365e-07.

It is cellwise meanfree. Convex-cell Poincare yields zero-normal local lifts psi with -div psi=R and ||psi||<=nu; the full-source equilibrated flux tau+psi is supplied by this existence/norm argument. No explicit polynomial full-source lift is asserted.

For D=tau-grad v_1, the actual direct flux audit gives

    ||D||^2 = 0.0004928953625313005,
    ||r||_(dual V)^2 <= (||D||+nu)^2 = 0.0005308851285320108.

The projected state mass, not the full P2 mass, enters the flux/gradient cross identity. Full P2 mass still enters J=2ell(v)-b_z(v,v). Independent degree-three integration of the complete affine P2 gradient against the quadratic flux reproduces the real defect norm, imaginary defect norm and covariance exactly. Final divergence, normal traces, global full-P2-gradient curl orthogonality, flux-norm decrease and corruption controls pass.

The direct reported-J radius is approximately 0.01199814165854499. The slightly smaller selected radius after recentering the new phase disk is approximately 0.01199476850797179. The shifted proxy is approximately -4.626021378949311 - 1.0417643293183172 i, with radius approximately 0.006428360113748804. These centers are different outputs and their radii are not interchanged without recentering.

## Neighboring frequency evaluator

Freeze a new compact scalar evaluator for the same neighboring state:

    J_w(v_1)=J_w1(v_1)-(z(w)-z(w_1))*integral v_1^2.

It uses six actual constant words and twelve explicit scalar operations, with a factored difference (w-w_1)(w+w_1). It is distinct from the sparse-matrix output evaluation. Its actual center shift from that pipeline is recorded in FLOATING_BAND_RESULTS.json. Constant quantization and all per-operation rounding enter its error bound.

Uniform ideal-interval/error propagation uses

    |RN(x)-x| <= 2^-53 |x|+2^-1075.

Exact propagated magnitudes exclude overflow; the underflow term is retained. Rational error bookkeeping bounds are rounded upward on a 2^-120 grid. The AST matches the declared operation DAG. An integer-only rational rounding oracle matches all 19,956 intermediate words on 1,663 native traces, with separate tie/subnormal/sign/boundary/nonfinite/type/corruption and constant-quantization controls. These samples are supplemental runtime controls; the analytic propagation covers every accepted frequency word.

For the fixed state, residual perturbation gives

    ||r_z|| <= ||D||+nu+(1/2)|z-z_1| ||v_1||_L2.

On |w-w_1|<=rho, with gamma=1/10,

    |z-z_1|^2 <= [rho(2w_1+rho)]^2+(2gamma rho)^2,
    kappa <= sqrt(1+[(w_1+rho)/(2gamma)]^2).

The corrected output radius is this kappa times the squared residual upper plus the uniform actual evaluator error. For rho=17/2000, the combined bound is approximately 0.09337110005158449; the evaluator contribution is approximately 6.51958244540628e-16. Actual input frequency means its exact represented binary64 value; decimal conversion, measurement uncertainty and physical frequency calibration are excluded.

## Exact join and seam checks

The joined evaluator performs no blending. It chooses

    original evaluator,  if exact represented w <= 577/128;
    neighboring evaluator, otherwise.

The exact switch lies strictly inside both the real overlap and its binary64 word interval. Thus the selected leaf is certified for every accepted input. Exact rational guard/selection adds no numerical output error. The uniform joined radius is the maximum of the two leaf radii, not their sum. Both leaf bounds target the same externally declared source/domain/gamma continuum transfer H(w), as checked by common topology, source expression, measure/mesh and IEEE-model bindings.

There are exactly

    original inputs: 19,140,298,416,325
    neighboring inputs: 19,140,298,416,325
    overlap inputs: 1,548,112,371,909
    joined inputs: 36,732,484,460,741

in the accepted binary64 intervals. Inclusion-exclusion is checked exactly. The selected original word interval ends at the switch word; the selected neighbor interval begins at its immediate successor, proving no uncovered binary64 input. Outside-union, nonfinite and non-float inputs are rejected. Moving the switch beyond overlap is rejected as a route to an uncertified leaf. 521 selector controls compare actual returned output bits with the selected frozen leaf, including the switch and its adjacent words.

At the same seam input, the two native leaf output centers differ by at most approximately 9.557659217149739e-05. This is below the sum of their radii, as required for consistency with common H. JOINED_RESULTS.json records this and the adjacent-input output jump as diagnostics. The piecewise output is not claimed continuous or differentiable. No smoothing, spectral derivative or interpolation accuracy claim follows from the join.

## Reproduction and governance

Run `python3 captures/2026-10-20T001957Z-codex-j1-neighbor-join-9a48fd6a/replay.py` from the repository. The hash-gated replay reconstructs the neighboring P2 state, its complete saved flux, exact full-gradient moments, native floating interval proof and selector/union checks, then compares all four result records. Saved-state/flux replay uses standard-library exact arithmetic; NumPy/SciPy are needed for proposal generation only. The prior original-state bound is a hash-bound dependency with its own completed replay record. REPLAY.log records the new complete read-only replay; repository integrity separately checks SHA-256 inventories and append-only event coverage.

The supplied coefficient ledger does not derive the externally declared scalar-wave action, source, damping or metric from native UD support dynamics. The CRL2 subdivision document remains a governance proposal. Gap2_FINAL_Finite_Genesis.png was unavailable and was not used. No horn/material, GR/QFT or empirical identification follows.

Independent review, every-platform formal IEEE verification, the full [0,6] x [0.1,1] parameter audit, finite mesh termination and the native UD action/observable bridge remain OPEN. Next: extend the certified state bank or derive a validated frequency-dependent trial state for wider coverage. Development — no registry entry; physical promotion=0.
