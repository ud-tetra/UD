# Refined J1 RT1 flux and actual complex128 output audit v0.1

Development — no registry entry. **NUMERICAL witness generation / EXACT a posteriori rational checks / CONDITIONAL continuum envelope.** Constructor only, independent review absent, physical promotion0. Refs #218,#136. Extends merged PR223/225, preserving all prior bytes and scope.

## 1. Implemented return

Implemented the fixed volume port F=10(x+y) on the existing14-node,16-tetrahedron conforming J1 refinement. Exact target K,M,load g,geometry and the mean-free basis are rebuilt with Fraction arithmetic. Material gamma=1/10 is an external declared control. Tested omega=0,4,9/2,5; these four fixtures do not constitute a continuous-frequency accuracy certificate.

For each fixture, NumPy2.3.5 `numpy.linalg.solve` generates a complex128 solution of the13-dimensional mean-free reduced system. The14-dimensional mean-free reference field is the EXACT rational lift Z of the stored reduced binary64 coefficients. The actual floating lift, raw dot-product output and bilinear corrected output are also run and their complex binary64 results stored. Every stored scalar is decoded by exact float hex into a rational value for the certificate.

Official NumPy2.3 documentation identifies its solve interface and LAPACK `_gesv` implementation: https://numpy.org/doc/2.3/reference/generated/numpy.linalg.solve.html . The certificate does not assume a generic library error bound: it checks these returned witnesses against the exact intended matrices. Regeneration on another backend may return different bits; stored-witness exact replay is the reproducibility target.

## 2. Refined equilibrated flux

Use the same RT1 polynomial basis and transformed coordinate t=sqrt2 z as PR223. There are15 local coefficients on each of16 tetrahedra,240 total. Exterior normal trace is zero; interior normal trace is continuous; cell divergence equals z*v-F, where v is the exact mean-free reference field. Affine normal traces and divergences are constrained at the required face/cell vertices, proving whole-face/cell identities.

The real geometry constraint matrix has196 equations, rank195 and45 free coefficients. Elimination is performed exactly, carrying all complex source right-hand sides as separate rational real/imaginary columns. One dependent equation expresses global mean/divergence compatibility. A floating solve proposes low-norm values for the45 free coefficients. Those values are decoded exactly, then the remaining coefficients are imposed by the exact eliminated constraints. Thus all trace/divergence constraints hold exactly even if the floating minimization is imperfect. No claim of exact flux optimality is made.

This is a global constrained RT1 reconstruction on one refined mesh. It is not yet a scalable local-patch or adaptive mesh implementation. The reconstruction uses the actual computed field; R=F-z*v+div(tau)=0 identically. Its exact flux misfit norm eta²=||tau-grad v||² is evaluated by rational polynomial volume integration, using weights(1,1,1/2) for transformed contravariant fluxes. The cross term is independently determined by the verified integration-by-parts identity.

## 3. Certified algebraic stopping and reported output

With K_V the exact positive definite reduced gradient Gram and rho=g_V-A_V x_returned,

    epsilon_alg²=rho* K_V^(-1)rho,
    algebraic raw output error <= sqrt5 epsilon_alg/beta.

The check uses the exact target A_V and decoded binary64 coefficients, so matrix-conversion and solve-rounding effects are included for the represented mean-free field. A separate exact difference bounds the actual floating reported raw output against ell(v); this includes floating lift/dot-product evaluation. Adding the two bounds must meet the declared absolute output budget10^-10. Every fixture passes. The worst total bound is below1.35e-12. The budget is an audit choice, not a theory constant or universal solver tolerance.

For the actual reported corrected output, the exact reference is

    Jcorr(v)=2g^T v-v^T(K+zM)v,

using ordinary transpose, not conjugate transpose. The difference between its actual reported binary64 value and this rational reference is also bounded exactly. Its continuum certificate is

    |H-Jcorr_reported| <= B eta²/beta² + evaluation_error.

The raw reported output additionally includes |ell(v)-b_z(v,v)| as required by PR225. No exact Galerkin orthogonality is assumed for the returned numerical vector. The certificate is a finite set of a posteriori audited outputs, not a universal all-input IEEE error theorem, a certified library implementation or a physical measurement.

## 4. Results and limitations

The outward-rounded STATIC continuum bracket is

    1022727/1000000 <= H(0) <= 1216053/1000000.

This uses the real static corrected functional as a guaranteed lower bound and the exact flux misfit as the error upper bound. It improves the earlier coarse bracket[1,215/168]. The lower and upper endpoints are rounded outward and verified exactly.

Approximate diagnostics below are rounded for readability; full rational values are in RESULTS.json:

| omega | Refined eta² | Earlier coarse eta² | Refined quadratic continuum error bound |
|---|---:|---:|---:|
|0|0.193326|0.279762|0.193326|
|4|5.73471|6.72505|11958.1|
|9/2|51.7636|128.258|165091.3|
|5|2.31367|4.30403|10862.7|

The estimator improves at all FOUR tested frequencies. The response certificates near resonance remain extremely wide because the coercivity/output bounds amplify the flux misfit at low damping. The algebraic solve passed; meaningful continuum resonance accuracy has NOT passed. These large bounds are not observed gains, resonance intervals or useful precision claims. The existing global gain bound can give a smaller, but still broad, response enclosure. Additional refinement, sharper dual/resolvent estimates or both are required.

## 5. Verification and replay

1591 exact checks pass, including1568 individual real/imaginary flux constraints, exact mean removal, flux norms, the raw algebraic budget, reported-output evaluation budget, static outward rounding and sampled estimator improvements. Two negative controls reject a zero/under-solved vector and a nonfinite coefficient. NEGATIVE_CONTROLS.json records the outcomes. These are constructor audits, not independent review.

Read-only replay on the captured witness:

    python3 fine_flux_run.py <path-to-this-capture>

When RESULTS.json already exists, audit mode compares the computed result and does not overwrite it. NumPy is optional in audit mode; exact checking uses the standard library. Generation requires NumPy and must run in a NEW output directory:

    python3 fine_flux_run.py <new-output-directory> --generate

Generation writes new WITNESS.json and RESULTS.json. Never regenerate inside the immutable capture. Source helpers are reused from our prior exact mesh implementation, not executed from an untrusted archive. Target reports/checker hashes, environment declaration and scope are recorded in CONTRACT.json.

Next: independent review; adaptive/local equilibration or another refined hierarchy; sharper verified continuum response intervals near4<=omega<=5. Mesh-family certification and native UD action/state/units selection remain open. PR225 passed remote CI and is merged; that integration does not establish independent scientific review. Physical promotion0.
