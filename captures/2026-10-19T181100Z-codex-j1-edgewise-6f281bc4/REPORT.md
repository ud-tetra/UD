# J1 h-reducing edgewise mesh family and refined RT1 certificates

**DERIVED / EXACT CONDITIONAL**; four audited numerical witnesses. Development — no registry entry. Constructor verification only; physical promotion **0**. Refs #218 #136. Extends PR223/225/226/228 append-only. PR228 passed CI and merged at `a36864dc84a518ed71a0cc1a38012dde965d9550` before this return.

## Result

An explicit conforming, uniformly shape-regular tetrahedron family now satisfies the mesh assumptions of the fixed-port continuum-convergence theorem. Its first implemented level has55 vertices and128 tetrahedra. Exact family geometry gives

$$h_\ell^2\le\frac54\,4^{-\ell},\qquad \ell\ge0.$$

Here level0 is the14-node/16-cell starting mesh, a=1. The first level's actual maximum diameter squared is5/16, compared with3/4 at level0. This is a new ordered edgewise rule; it is not repeated use of the previous barycenter rule or an assertion about arbitrary tetrahedron refinement.

The static continuum bracket improves to **[1.123043,1.206865]**. At omega4.5 the certified corrected-output radius falls from901.394 on the barycenter enrichment to77.9723 here. At omega4 the radius increases. Resonance accuracy remains **OPEN**.

## Exact refinement construction and family proof

For an ordered physical tetrahedron(p0,p1,p2,p3), define its increment frame

$$G=[p_1-p_0,\ p_2-p_1,\ p_3-p_2].$$

It maps the reference ordered Kuhn tetrahedron0<=z<=y<=x<=1 to the physical tetrahedron by p0+G(x,y,z). Partition the half-grid cubes into their permutation path tetrahedra, retaining those entirely in the order region. Exactly eight paths remain. A path's four half-grid vertices map to old vertices or shared edge midpoints; no new face or cell-center node is required. Each path is ordered in its coordinate-step order.

For each child,

$$G_{\mathrm{child}}=\tfrac12 GP_\sigma,$$

where P_sigma is a3-column permutation. The reference barycentric coefficient identities are checked exactly for all24 child steps, independently of coordinates.128 additional identities check the16 physical parents and their eight children. At every subsequent level,

$$G_{\ell,T}=2^{-\ell}G_{0,T_0}P,\qquad P\in S_3.$$

Thus each of16 initial tetrahedra produces at most six normalized ordered shapes: at most96 total. Every initial frame is nonsingular. There is no accumulating shear or uncontrolled choice of central diagonal.

Each parent triangle is partitioned into exactly its three corner triangles and central midpoint triangle. Four exact reference-face set equalities verify this rule independently of local vertex order. Adjacent cells share midpoint IDs and this unique face partition; conformity follows inductively. Reference cube permutation paths have disjoint interiors. Their eight determinant volumes exhaust the parent tetrahedron. The implemented physical child volumes are independently checked as1/64 in normalized measure, summing to2 over128 cells.

The physical metric in(x,y,t=sqrt2*z) coordinates is diag(1,1,1/2). For the16 initial increment frames, exact Gram calculations give

$$\lambda_{\min}(G^TgG)\ge\frac1{72},\qquad
\lambda_{\max}(G^TgG)\le\frac32.$$

The lower estimate uses lambda_min>=4det(Gram)/trace(Gram)^2; the upper uses lambda_max<=trace. Column permutations preserve these eigenvalues; level scaling multiplies both by4^-ell. The squared increment-frame condition number is therefore at most108 uniformly. A fixed transformation from the Kuhn reference cell to the usual reference simplex then gives uniform tetrahedron shape regularity.108 is the increment-frame bound, not an independently computed inradius/aspect ratio.

Every edge is a scaled sum of a nonempty subset of the three parent increments. Exact enumeration of these subset sums gives the global constant C²=5/4 and the displayed h bound. These are dimensionless lengths; for physical edge scale a the bound multiplies by a². `MESH_FAMILY.json` stores the exact certificate. The proof relies on the specified child ordering; arbitrary reordering between levels is outside its scope.

## Continuum-convergence consequence and its limits

Keep the same declared scalar-wave model: meanfree V=H1(Omega), gradient norm, normalized measure mu(Omega)=2, source/readout F=10(x+y), z=-omega²+2i gamma omega. The convex Poincare lower bound lambda1>=pi²/2>4 remains the continuum anchor. No finite-mesh eigenvalue is substituted for it. Damping gamma remains externally declared, with time tau=ct/a.

Uniform shape regularity and h->0 give density of the conforming P1 spaces: first interpolate smooth functions on the uniformly controlled reference shapes, then use H1 density; subtract the mean to remain in V. The fixed distributed port embeds exactly at every level, since F is globally affine. The coefficient space is not a point-forcing substitute.

The earlier damped Galerkin theorem therefore applies to this concrete family. On |omega|<=6 and gamma in[1/10,1], beta_*²=1/901 and B_*=13. Compactness of the parameterized continuum solution set, the finite-net/density argument and the uniform Galerkin estimate imply

$$\sup_{|\omega|\le6,\,1/10\le\gamma\le1}|H-H_\ell|\longrightarrow0.$$

This statement concerns the exact Galerkin family under the declared model. It does not assert that the four stored floating outputs cover the band, that their algebraic budget will hold automatically at later levels, or that the particular hierarchical flux estimator converges to zero. No numerical regularity/interpolation constant or h-to-output tolerance is claimed. A posteriori stopping test based on the computed certificate is valid, but termination at a requested tolerance is still unproved.

## General local flux projection and reconstruction

The parent16-cell RT1 field now uses the cellwise L2 projection of the computed fine P1 state onto affine parent fields. This generalizes the special barycenter-hat projection in PR228. For parent volume V=1/8 and parent barycentric basis, the local mass matrix is V(I+11^T)/20. Its exact inverse gives projected nodal coefficients

$$c_i=160\left(b_i-\tfrac15\sum_jb_j\right),\quad b_i=\int_Tv\lambda_i\,d\mu.$$

The fine local consistent mass matrix evaluates these moments exactly. All four projection normal equations are checked on every cell for each state component. The parent flux has divergence z Pi_1 v-F; mean preservation gives global compatibility.

Each eight-child patch adds a flux of divergence z(v-Pi_1v) with zero normal trace on the parent boundary. It has120 RT1 coefficients,104 constraints of rank103, and17 proposal variables. After choosing floating free coefficients, exact reconstruction enforces the constraints. The parent field has240 coefficients,196 constraints of rank195 and45 proposal variables. Local minimization is separate per patch; no exact or global optimality is asserted.

Finally, the assembled1920-coefficient flux is checked directly against1424 global trace/divergence equations in real and imaginary parts at four samples: **11392 scalar exact flux checks**. These ensure zero exterior normal trace, internal normal continuity and divergence z v-F. No remainder residual is omitted.

## Posterior outputs

For any conforming v, J(v)=2ell(v)-b_z(v,v), H-J(v)=b_z(u-v,u-v). Use the spectral factor derived in PR228,

$$|H-J(v)|\le\kappa\eta^2,\quad
\kappa=\sup_{\lambda\ge4}\frac{\lambda}{|\lambda-\omega^2+2i\gamma\omega|},\quad
\eta=\|\tau-\nabla v\|_{L^2}.$$

The exact bound and recorded corrected-output evaluation error are stored separately. Raw outputs additionally include the inexact algebraic correction and raw evaluation error. The continuum gap, fixed port and complex-bilinear convention are unchanged.

The following are display approximations at gamma=1/10. Exact rational upper bounds in RESULTS.json govern acceptance.

|omega|corrected output real|corrected output imaginary|eta²|continuum radius|
|---|---:|---:|---:|---:|
|0|1.123044|0|0.083821|0.083821|
|4|9.885631|-4.957263|8.436314|168.937052|
|4.5|-6.663391|-2.259573|3.462016|77.972266|
|5|-2.614305|-0.353475|0.495166|12.389042|

At omega4, eta² increases from5.684336 on the previous barycenter enrichment to8.436314 here. The two fine spaces are different and this flux construction is not a monotone optimized estimator. No monotonic resonance response or resonance-location theorem follows from these samples.

At zero frequency the real energy identity gives the outward bracket

$$\boxed{1.123043\le H(0)\le1.206865}.$$

The worst certified end-to-end **algebraic** raw-output error is9.504732e-12, below the declared1e-10 budget. This does not reduce the continuum discretization radii to that scale.

## Verification, replay and governance

The solver audit passes11421 exact checks, including11392 assembled flux constraints. Three expected rejection controls cover an under-solved zero state, nonfinite coefficient and truncated free-flux proposal. Family checks include24 generic frame identities, four reference-face equalities,128 physical frame identities, and exact Gram/determinant bounds. Stored numerical proposals and reported outputs are decoded from binary64 hex, then audited using Fraction arithmetic and outward square roots. This is a finite-witness posterior certificate, not an all-input IEEE theorem.

```sh
python3 red_mesh.py
python3 red_flux.py .
python3 red_controls.py WITNESS.json red_flux.py
```

Replay is read-only when RESULTS.json exists. Imports disable bytecode. `--generate` is only for new unpublished output directories, never frozen captures. `fine_flux_core.py` and `patch_flux.py` are byte-identical reuse from the prior own verified capture; source hashes are in CONTRACT.json. Their old command entry points are not invoked by the new runner.

The attached ledger's Q169-Q179 concerns incidence/support operators and does not derive this benchmark's metric action or damping. The attached CRL2 amendment explicitly labels itself a governance proposal; it is not treated as enacted authority. Neither source is overwritten. Missing image `Gap2_FINAL_Finite_Genesis.png` was not used; reupload was requested. All work remains development, with no scientific registry entry or independent review.

Native Project1 issue218 remains In review / Scientific OPEN / Constructor checked / Development. Next gate was saved and verified after reload: independent review of the edgewise family; tighter resonance certificates using refined/dual solves; a quantitative stopping rule and native UD action bridge. See PROJECT_RECEIPT.json and screenshot.

Remaining work: obtain tight posterior output intervals near resonance, improve scalable flux/dual reconstruction, quantify an actual accuracy stopping/termination guarantee, and separately select a native UD source/action/units correspondence. The explicit mesh-family assumption is now constructor-checked; native physical identification remains open. Physical promotion0.
