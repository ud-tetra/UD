# Own flux upper certificate for the center-enriched J1 state

DERIVED / EXACT CONDITIONAL; constructor checked; independent review OPEN; physical promotion = 0. Development artifact, no authoritative registry entry. Refs #218 and #136; extends PR245 without changing any older frozen state or certificate.

## Problem and supplied state

At dimensionless omega = 9/2 and gamma = 1/10, take the exact meanfree P1 state v obtained by decoding and summing the two binary64 words per nodal component in the center-enriched capture. It has 2,809 nodes and 12,288 tetrahedra. The scalar-wave equation, source F=10(x+y), homogeneous Neumann condition, damping and normalization are externally declared benchmark data. They are not native UD action or constitutive derivations.

The normalized measure has total mass 2. Coordinates are (x,y,t=sqrt(2) z_phys), gradient metric diag(1,1,2). The flux coordinates j=(tau_x,tau_y,sqrt(2) tau_z) use metric diag(1,1,1/2); coordinate divergence equals physical divergence. Cell measures are 1/4096 (4 per parent) and 1/8192 (8 per parent). Center insertion preserves the exterior mesh and maximum diameter squared 5/256.

## Construction and exact checks

Project the final state in L2, separately for both real components, onto broken affine polynomials on the 1,024-, 128-, and 16-cell parent levels. Every projection uses exact local consistent mass and unequal child measures; it preserves the parent affine moments and averages. On a parent with measure V, the mass matrix is V(I+11^T)/20 and inverse 20(I-11^T/5)/V.

Construct a continuous-normal RT1 root flux on the 16-cell mesh with divergence z Pi_0 v-F and zero exterior normal trace. On each subsequent parent patch, add an RT1 correction with zero patch-boundary normal trace and divergence z(Pi_{l+1}v-Pi_l v). The average-preserving projections ensure compatibility. The eight-child reference system has rank 103 and 17 free coefficients; the twelve-child system has rank 143 and 37 free coefficients. There are 16+128+1024 patches. Binary64 minimum-norm proposals select free coordinates only. Exact rational elimination and reconstruction enforce every constraint, so floating optimization accuracy is not a premise of flux admissibility or validity.

Each affine coordinate map x=o+G xi sends j_ref to G j_ref; its constant determinant is absorbed in the coefficient convention. Exact map roundtrips are checked. The final flux is checked again directly on the actual 12,288 cells: divergence at all four vertices, normal traces at all three vertices of each face, and zero exterior traces. RT1 divergence and normal traces are affine, so these tests establish the full polynomial identities. Thus tau belongs to H_0(div) and

    div tau = z v-F,   R=F-zv+div tau=0.

Flux norms and real/imaginary covariance are integrated exactly through polynomial degree four. Actual unequal cell measures and the physical metric are included. The resulting covariance is positive semidefinite. Structural controls reject incompatible zero-normal divergence on both reference patches, a corrupted exterior trace, truncated free-coordinate words and nonfinite words. The parent reference moment formulas and final defect norm identity provide additional independent consistency checks within the constructor audit.

## Output certificates and proof

Let z=-omega^2+2 i gamma omega, ell(w)=integral F w, b(w,w)=integral(grad w dot grad w+z w^2), and define the algebraically corrected output J(v)=2 ell(v)-b(v,v). These are complex bilinear expressions. For the exact continuum solution u and e=u-v, symmetry gives the identity H-J(v)=b(e,e), with no exact-Galerkin assumption on the saved state.

Set D=tau-grad v, eta^2=integral |D|^2, and q=integral D dot D. Integration by parts gives the exact residual r(w)=integral D dot grad w. Hence ||r||_{V'} <= eta. At this point the rotated coercivity factor obeys beta^{-2}=2029/4. The origin-centered certificate is

    |H-J(v)| <= sqrt(2029/4) eta^2.

The reported J radius adds its exact outward evaluation bound from the saved state audit.

A sharper shifted output enclosure follows from the continuum spectral representation. In each normalized gradient eigenmode the coefficient of the bilinear error is f(lambda)=lambda/(lambda-omega^2+2 i gamma omega). For real lambda, f lies on the circle with center c=1/2-i omega/(4 gamma) and radius delta=|c|. The solenoidal coefficient 0 lies on this same circle, so the norm budget must include the solenoidal part of D. Therefore

    |H-[J(v)+c q]| <= delta eta^2,
    c=1/2-45 i/4,   delta^2=2029/16.

The exact rational center is rounded to two reported binary64 words; the radius includes an outward rational square-root bound for this center evaluation. The resulting proxy is a derived certified output estimate, not another FEM state solve. Full exact fractions and the actual reported hex words are in UPPER_RESULTS.json.

## Scope and remaining gates

This is an own pointwise continuum upper certificate for the enriched state, independent of the older disk inherited by recentering. It is not an assertion that the chosen hierarchical flux is globally optimal, that the upper bound equals the actual error, or that the accuracy target is met. A failure of this particular upper bound to reach 0.1 is inconclusive about true error. Existing lower-bound no-go results remain confined to the frozen states and diagnostic families for which they were derived.

The spectral/functional-analytic premises are those already declared in PR223 and the phase-circle contract of PR238: the meanfree Neumann continuum problem on the convex J1 polyhedron, positive damping and conforming state. No discrete spectral gap is substituted for a continuum gap. No uniform frequency-band accuracy, convergence rate, finite stopping rule, all-input IEEE guarantee, independent review, empirical material/horn claim, GR/QFT counterpart, native incidence/support-ledger action or physical promotion follows.

The uploaded coefficient-provenance ledger remains a source ledger; it does not derive this benchmark wave action/damping. The CRL2 subdivision document remains a governance proposal. The missing Gap2_FINAL_Finite_Genesis.png was unavailable and was not read or used. Independent review and the native UD bridge remain OPEN.

## Reproduction

Run `python3 captures/2026-10-19T212549Z-codex-j1-center-upper-96b9aca0/replay.py` from this repository, substituting this capture directory. It verifies immutable source dependencies, reconstructs the saved flux with standard-library exact rational arithmetic and compares the result with the frozen result JSON. NumPy was used only to propose saved free coordinates and is optional for replay. REPLAY.log records the read-only result. The repository integrity verifier checks capture hashes and append-only event coverage.

## Measured certificate result

The exact rational squared defect is approximately 0.19723810689739968. The outward radius about the saved corrected FEM output J is approximately 4.442238311890338, versus the older inherited radius 14.433979577949017 about that same output. The own phase-circle proxy is approximately -3.830940227108530 - 3.110463301523840 i, with outward radius approximately 2.2211191559451198. All decimals here are display approximations; authoritative outward rational values and actual proxy hex words are in UPPER_RESULTS.json. Neither own certificate passes the 1/10 target.

The strongest previously tested residual squared lower bound was approximately 0.0029313793985937704; together these yield a conditional enclosure of the full residual dual norm squared between that lower bound and this own upper bound. The previous fixed coarse-bubble lower bound remains approximately 0.0014051048226027911. The tested-family reductions were not an upper estimate of the full residual.

The frozen flux free-coordinate witness is stored as deterministic gzip-compressed JSON (UPPER_WITNESS.json.gz). Compression changes only storage; replay decodes the actual hexadecimal words and performs exact rational reconstruction.

Next: reduce the gap between the residual lower and upper bounds using coupled global divergence-free corrections on this enriched mesh, or construct an enriched adjoint certificate. Independent review and full-band/termination/native-source gates remain open.
