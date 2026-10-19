# J1 nonconstant curls and the frozen-state residual obstruction

**DERIVED / EXACT CONDITIONAL**, with audited floating proposals. Development — no registry entry. Constructor verification only; independent review outstanding; physical promotion **0**. Refs #218 #136. PR239 passed CI and merged at `ab20d188d577cdec752c4f387e041ef9b85400c3`. Concurrent boundary-intake main487f69 was preserved; fresh merged-tree verification passed150 captures/3107 inventoried files/154 events, tree `a31556abf8f77dab60094aa9a1b85ee010941f30`.

## Outcome and decision

Nonconstant affine curl corrections reduce the guaranteed output disks, but only modestly. A separate residual lower bound now shows that flux optimization alone cannot close the phase-circle1/10 gate at omega4 or4.5 while the state is frozen. The next task is state enrichment/refinement at these frequencies or another output certificate, rather than repeated flux-only optimization.

|omega, gamma=1/10|previous selected radius|new selected radius|new eta²|1/10 gate|
|---|---:|---:|---:|---|
|0|0.0141893157|0.0137316152|0.0274632303|PASS|
|4|23.4767331|23.4767331|6.6573676646|FAIL|
|4.5|7.5238449|7.2252057|0.6416071273|FAIL|
|5|1.6234309|1.5535496|0.1241846539|FAIL|

The phase radii at0/4.5/5 refer to newly derived, actually recorded proxy centers. At4 the inherited moment-based disk remains selected. The original corrected FEM outputs have direct new norm-based radii14.45042 at4.5 and3.10710 at5; they are different reporting centers. Exact fractions and binary64 hex words govern; table decimals are explanatory. A failed certificate gate does not establish actual error above the target.

The static bracket tightens to

$$[587861/500000,601593/500000]=[1.175722,1.203186].$$

Its new midpoint594727/500000=1.189454 certifies uniform1/10 accuracy for |omega|<=142313/1000000=0.142313 and gamma in[1/10,1], via the inherited static spectral-variation theorem and recorded proxy evaluation error. The next10^-6 grid point fails this sufficient test only. No physical cutoff or full-band precision is asserted.

## Model and provenance

The benchmark remains normalized J1, measure2, F=10(x+y), meanfree Neumann Laplacian with continuum gap floor4, z=-omega²+2i gamma omega, externally declared damping and time ct/a. The fixed285-node/1024-cell two-word P1 state, original hierarchical RT1 flux and previous constant-curl witness are reused byte-identically. No PDE solve, state refinement or physical calibration occurs in this capture.

Coordinate flux is j=(tau_x,tau_y,sqrt2 tau_z) on(x,y,t=sqrt2 z_physical), with metric g=diag(1,1,1/2). Coordinate div j is physical divergence. The physical gradient norm of a scalar uses the inverse metric diag(1,1,2). The exact audits keep these roles distinct.

## Quadratic potentials and affine divergencefree curls

Let phi_i denote fine P1 nodal hats. For each interior edge i<j, use two potentials

$$\phi_i(\phi_i\nabla\phi_j-\phi_j\nabla\phi_i),\quad
\phi_j(\phi_i\nabla\phi_j-\phi_j\nabla\phi_i).$$

Their curls are respectively3 phi_i grad(phi_i) cross grad(phi_j) and3 phi_j grad(phi_i) cross grad(phi_j).

For each globally ordered interior face(i,j,k), use two cyclic potentials of the form

$$\phi_i(\phi_j\nabla\phi_k-\phi_k\nabla\phi_j),$$

whose curl is

$$\phi_j\nabla\phi_i\times\nabla\phi_k
-\phi_k\nabla\phi_i\times\nabla\phi_j
+2\phi_i\nabla\phi_j\times\nabla\phi_k.$$

Global edge/face ordering fixes orientation. These piecewise quadratic potentials have continuous tangential traces; boundary edge potentials are excluded, and interior face potentials have zero tangential trace on all other faces. Their curls are affine, divergencefree and have continuous normal trace with zero exterior trace. They can change within-cell variance, unlike the prior constant correction.

The mesh supplies924 interior edges and1856 interior faces, giving5560 potential coefficients per real component. SciPy1.17.0 `sparse.linalg.lsmr` proposes eight real coefficient vectors for the four complex fixtures, with recorded stop codes and208–210 iterations for nonzero components. The static imaginary component is zero. No exact rank, complete-span or global optimality theorem is used.

The12288-by5560 sparse least-squares system uses the consistent affine mass matrix(I+11^T)/20 and metric g. Its target is the exact cellwise affine L2 projection of the existing quadratic RT1 flux. For linear functions u,v expressed at four vertices,

$$E[\lambda_a uv]=[U V+\sum_bu_bv_b+u_aV+v_aU+2u_av_a]/120,$$

where U=sum u_b and V=sum v_b. This supplies the projection moments without floating quadrature. Because the correction is affine, the omitted orthogonal quadratic remainder adds a constant to the objective. The common cell volume1/512 does not change its minimizer.

The stored coefficients are decoded exactly. The posterior audit checks16832 local basis divergence identities,8192 actual affine divergence values and53760 face/vertex/component normal traces.7168 cell-components have nonconstant corrections. It also checks eight exact global gradient-orthogonality identities and eight flux-norm nonincrease inequalities. The new eta² equals the old eta² plus the exact constant- and affine-curl norm changes. The prior86528 direct final assembled divergence/trace conditions pass again on the resulting RT1 field. These checks establish validity/decrease without trusting solver convergence or claiming exact optimality.

## Output enclosure

The inherited complex-symmetric identity and phase-circle theorem remain

$$|H-[J(v)+c_zq]|\le\delta_z\eta^2,\quad
q=\int(\tau-\nabla v)\cdot(\tau-\nabla v),$$

$$c_z=1/2-i\omega/(4\gamma),\qquad
\delta_z=\tfrac12\sqrt{1+\omega^2/(4\gamma^2)}.$$

At zero frequency take c=delta=1/2. New exact mixed moments determine q, covariance positivity is checked, and the actual rounded proxy evaluation error is added once. Prior valid disks and rational outer-polygon candidates remain separately recorded. All dynamic selected radii remain above1/10. Source state/output identities, conjugacy, outward square roots and malformed-payload/trace controls are retained. No exact Galerkin projection or all-input IEEE guarantee is assumed.

## Flux-independent lower bound from cell bubbles

This diagnostic uses only the frozen state, source and geometry. On each tetrahedron K set b_K=product_a lambda_a, extend it by zero, and subtract its global mean to obtain an admissible meanfree test. Subtracting the mean changes no gradient; the residual on constants is zero because both F and v have zero mean.

The bubble gradients have disjoint cell supports, hence are orthogonal in the V energy inner product. Their normalized barycentric moments are

$$\int_Kb_K\,d\mu=\mu(K)/840,\qquad
\int_K\lambda_ab_K\,d\mu=\mu(K)/3360.$$

Since v is affine on each cell and b_K vanishes on its boundary, integral grad(v) dot grad(b_K)=0. Thus the complex residual value is

$$R_K=r(b_K)=\frac{\mu(K)}{3360}\sum_{a=0}^3(F_a-zv_a).$$

Writing g_a=grad_coordinate(lambda_a), its energy is

$$E_K=\|b_K\|_V^2
=\frac{\mu(K)}{15120}\sum_a(g_{a,x}^2+g_{a,y}^2+2g_{a,t}^2).$$

The formula follows by integrating all16 gradient-product monomials: diagonal barycentric moments are1/7560 and off-diagonal ones1/15120, with sum g_a=0. The code independently compares the full factorial-moment expansion against this energy formula on all1024 cells; five bubble/moment identities are also checked.

Optimizing the residual quotient over the orthogonal complex span of these mean-subtracted bubbles yields

$$\boxed{\|r\|_{V'}^2\ge L_{\rm bubble}:=\sum_K|R_K|^2/E_K.}$$

Every equilibrated flux estimator for the same state satisfies ||r||V'<=eta, so eta²>=L_bubble regardless of flux degree, mesh or optimization. The recorded flux eta² is checked to exceed this lower bound. This is a lower bound on residual norm, **not actual transfer error**.

|omega|L_bubble, approximate|delta L_bubble, approximate|flux-only circle1/10 obstruction|
|---|---:|---:|---|
|0|0.000862833|0.000431417|Not proved|
|4|0.198436057|1.986839470|YES|
|4.5|0.018844903|0.212214442|YES|
|5|0.003588026|0.044886186|Not proved|

The acceptance obstruction uses the exact rational squared test delta² L_bubble² > (1/10)². Therefore **no admissible flux for this frozen state can meet1/10 through the delta*eta² circle certificate at4 or4.5**. This remains true after improving flux spaces or solver tolerances. It does not exclude another output certificate, a changed state, a different approximation or a physical response. At5 this particular test is inconclusive; failure to prove an obstruction is not a precision pass.

This strengthens the earlier constant-only variance result: at4/4.5 the current state itself blocks this certificate, independently of the flux-correction space. State enrichment/refinement or another certificate is now the scientific gate.

## Replay and governance

```sh
python3 linear_flux.py .
python3 linear_circle.py .
python3 linear_summary.py .
python3 bubble_floor.py .
```

Captured stored-results replay is read-only and disables bytecode. Proposal generation requires a new unpublished directory without a linear witness. Backend diagnostics are numerical data; exact posterior checks establish the declared conclusions. Files and event are append-only, with source hashes in CONTRACT.json. Constructor verification is not independent review.

Native Project218 remains In review / Scientific OPEN / Constructor checked / Development. Its saved/reloaded next gate requests independent review, state enrichment/refinement at4/4.5 or another output certificate, full-band precision, termination and the native UD bridge. Screenshot and receipt accompany the capture.

Estimator convergence, quantitative stopping termination, resonance/full-band1/10 precision, native UD action/source/units and calibration remain open. The uploaded support ledger does not source this scalar-wave action/damping. The uploaded CRL2 amendment remains a governance proposal; no uploaded files or registry entries are changed. Gap2_FINAL_Finite_Genesis.png remains unavailable and was not used; reupload requested. Physical promotion remains **0**.
