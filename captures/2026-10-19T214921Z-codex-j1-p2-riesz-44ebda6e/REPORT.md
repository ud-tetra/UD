# Conforming P2 dual lower certificate and scoped phase-circle obstruction

DERIVED / EXACT CONDITIONAL. SCOPED NO-GO for the declared phase-circle certificate family on the frozen enriched state. Constructor checked; independent review OPEN. Development — no registry entry. Physical promotion = 0. Refs #218 and #136; extends PR248 without changing any older state, bound or record.

## Result and decision

The continuum residual dual norm squared is enclosed by the exact rational lower and upper certificates whose decimal approximations are

    0.12339873860344404 <= ||r||_{V'} squared <= 0.12395170889381193.

Decimals in this report are display approximations. RIESZ_RESULTS.json contains the authoritative exact fractions. A simple outward decimal enclosure is

    0.12339873 <= ||r||_{V'} squared <= 0.12395171.

The new lower is 99.55388248% of the previously verified flux upper. Their squared effectivity ratio U/L is approximately 1.0044811665. Consequently even an arbitrarily improved equilibrated flux can reduce the current eta squared by at most 0.44611753% relative to its present value. This measures the remaining possible improvement of the norm estimator for the same residual, not a change in the actual state or output error.

For every exactly equilibrated flux on this frozen state, the delta*eta_squared phase-circle radius is at least approximately 1.3896062299672551. The outward rational lower in the result JSON is rigorous; in particular the radius is >=1.38960>0.1. Thus further flux-only optimization cannot reach 0.1 using this declared formula on this state. This is a certificate-family obstruction, not an actual transfer-error lower bound and not a no-go for an adjoint, deflation, spectral-intersection or other output certificate.

Next useful action: solve a conforming quadratic P2 wave state at the same parameter pair and repeat the primal/dual audit, or use a different goal-oriented output certificate. Further optimization of the old flux alone cannot meet the existing phase-circle target.

## Frozen problem and independent lower-bound construction

The state is the exact decoded two-word, meanfree P1 state of PR245, used unchanged by PR247 and PR248. There are 2,809 P1 vertices and 12,288 tetrahedra, at dimensionless omega=9/2 and gamma=1/10. The benchmark has F=10(x+y), homogeneous Neumann boundary data and normalized measure mu(Omega)=2. Coordinates are (x,y,t=sqrt(2) z_phys), with physical gradient metric diag(1,1,2). Cell measures are 1/4096 or 1/8192; all are used exactly.

Write z=-a+i b, a=81/4, b=9/10, and v=v_R+i v_I. For real w the residual components are

    r_R(w)=integral [(F+a v_R+b v_I)w-grad v_R dot grad w],
    r_I(w)=integral [(a v_I-b v_R)w-grad v_I dot grad w].

The lower construction uses these expressions directly from the source and state, without a flux witness or a fitted spectral constant. Only after computing its lower is it compared with the already verified PR248 upper result, whose state and parameter hashes are checked. The normalized V norm is the physical gradient seminorm on meanfree H1. The real/imaginary Riesz decomposition gives ||r|| squared=||r_R|| squared+||r_I|| squared.

## Conforming quadratic test space and exact assembly

Use continuous nodal P2 tetrahedral functions on the same mesh: all 2,809 vertices and all 15,864 edge midpoints, totaling 18,673 degrees of freedom. Boundary degrees of freedom are included; this is the Neumann test problem. Shared global vertex and edge-midpoint coefficients determine the same six-node quadratic trace on every common triangular face, so the assembled tests are conforming H1 functions. The two actual saved tests are centered by subtracting their exact normalized integrals divided by 2. Constants have zero gradient and both residuals annihilate constants, so this projection changes neither energy nor residual pairings.

On a cell with barycentric coordinates lambda_i, the basis is

    N_i=lambda_i(2 lambda_i-1),
    N_ij=4 lambda_i lambda_j.

Gradient values are affine and integrated exactly through degree two. With local measure m, the load moments for an affine source f with vertex values f_i and sum S are

    integral f N_i = m(f_i-S)/60,
    integral f N_ij = m(S+f_i+f_j)/30.

Basis means are -m/20 at vertices and m/5 at edges. These signed basis means are integration weights, not an energy norm. Local partition of unity, gradient sum zero, affine mass/load moments, constant annihilation and the identity P_transpose K_P2 P=K_P1 are verified exactly. Globally, the entire P2 residual is restricted through the nodal P1 prolongation and agrees exactly with both components of the frozen P1 algebraic residual at all 2,809 vertices. This binds the enriched tests to the same source, state and residual.

## Numerical test proposals, exact lower proof

A floating conjugate-gradient solve of the P2 Poisson matrix plus the Euclidean constant-mode projector 11_transpose/n proposes two Riesz tests, one for each residual component. A positive diagonal preconditioner is used. The saved proposal needed 400 and 401 iterations respectively, with numerical stop code 0. This is proposal metadata, not a premise that an exact linear system or continuum Riesz problem was solved.

RIESZ_TESTS.bin.gz stores the actual component-major little-endian binary64 coefficient words. The witness JSON binds its hash, dimensions, frequency/damping, source state and canonical mesh topology. Replay converts every finite saved word to an exact Fraction. It subtracts the exact weighted mean, evaluates the exact 2x2 test energy Gram G and the exact pairings C_{r,j}=r_r(phi_j).

G is verified positive definite. Projection onto the complex span of these two real meanfree test functions gives the lower

    L = C_R G^{-1} C_R_transpose + C_I G^{-1} C_I_transpose
      <= ||r||_{V'} squared.

This is a conforming variational lower certificate for the continuum norm. Exact Poisson/Galerkin optimality, a solver-tolerance theorem and a continuum approximation rate are unnecessary. The result also checks that L dominates both the separate-test Rayleigh lower and the unscaled variational lower 2*r_R(phi_R)+2*r_I(phi_I)-||phi_R|| squared-||phi_I|| squared. The prior quartic-bubble lower is weaker and remains valid in its original scope; overlapping bounds are not added.

Structural controls reject truncated and nonfinite test payloads, zero test energy and an indefinite test Gram. Exact geometry, local nesting and global P1 residual restriction provide checks independent of the floating proposal. Constructor verification does not constitute independent review.

## Scoped no-go proof and its limits

For any admissible exactly equilibrated flux tau on this same state,

    div tau=zv-F,  tau dot n=0,
    D=tau-grad v,
    r(w)=integral D dot grad w,
    ||r||_{V'} squared <= eta squared=integral |D| squared.

The existing phase-circle theorem uses radius delta*eta_squared, with delta squared=2029/16 at this point. Therefore every such radius obeys

    radius squared >= (2029/16) L squared > 1/100.

The strict last inequality is tested with exact rational arithmetic. A directed lower square root is saved, with its lower/next-gridpoint inequalities checked. Center evaluation adds a nonnegative budget and cannot remove this obstruction. The J-centered 2*delta estimator is likewise blocked for 0.1. This conclusion concerns the size of these guaranteed envelopes, not the value of |H-J| or an arbitrary optimal output enclosure.

The earlier absence of a quartic-bubble obstruction on the enriched state was correctly limited to that tested family. These new conforming quadratic tests reveal the stronger obstruction without changing the state. No prior record is retracted or overwritten.

## Governance and reproduction

The scalar-wave action, damping, physical metric and source are externally declared benchmark data. The coefficient ledger Q169-Q179 does not derive this wave model from native UD incidence/support dynamics. The CRL2 subdivision file remains a governance proposal; citing it enacts no new registry rule. The missing Gap2_FINAL_Finite_Genesis.png was not read or used.

Scientific status remains OPEN. There is no native UD constitutive, horn/material, GR/QFT or empirical identification, no uniform-band accuracy, no explicit convergence-rate constant, no finite stopping rule and no all-input floating-point theorem. No independent review or physical promotion occurs.

Run `python3 captures/2026-10-19T214921Z-codex-j1-p2-riesz-44ebda6e/replay.py` from the repository. It verifies immutable dependency hashes, rebuilds the direct residual and P2 test energy, and compares the saved exact result. NumPy/SciPy are used only to propose the saved test words. The actual replay arithmetic uses the standard library. REPLAY.log records completion; the repository integrity verifier separately checks capture hashes and append-only event coverage.
