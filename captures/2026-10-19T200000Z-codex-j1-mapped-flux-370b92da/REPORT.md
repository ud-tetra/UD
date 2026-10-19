# J1 mapped hierarchical RT1 flux on1024 cells

**DERIVED / EXACT CONDITIONAL**, with audited floating free-coefficient proposals. Development — no registry entry. Constructor verification only; physical promotion **0**. Refs #218 #136; append-only extension of PR223/225/226/228/229/230/232/234. PR234 passed CI and merged at `8b6f8114ea4be5ae75b9c5597caa5f36c04d5c35` after fresh integration verification against concurrent main513d6b4. The merged tree matched verified local tree8d73c9ba9f7af8585effab2e83025dda6e52c1e9; concurrent work is preserved.

## Outcome

The1024-cell state now has its own exactly equilibrated RT1 flux certificate. The construction uses one root solve and144 mapped eight-cell patch solves, with a single reusable reference constraint elimination. Final assembled divergence and normal-trace conditions pass **86528 exact scalar checks**, separate from the119808 mapped-patch constraints and1568 root constraints.

The new fine-flux output radius is about16.3574 at omega4.5 and3.55629 at omega5, improving the inherited21.6445 and12.5729 bounds. At omega4 the new flux radius149.699 is worse than the inherited23.4767, which is retained. None of the dynamic samples meets the declared1/10 absolute output target.

The static continuum bracket tightens slightly to

$$\boxed{1.175722\le H(0)\le1.206011}.$$

With the updated midpoint proxy1.1908665, the uniform1/10 low-frequency strip extends to |omega|<=0.139694 for gamma in[1/10,1], including the recorded binary64 proxy-evaluation error. The proxy center changes with the bracket; no larger interval is silently assigned to the previous midpoint.

## Model and input provenance

The model, fixed distributed port and units are unchanged: normalized J1, coordinates(x,y,t=sqrt2*z), normalized measure mu(Omega)=2, meanfree Neumann scalar wave, F=10(x+y), z=-omega²+2i gamma omega and time tau=ct/a. Damping is externally declared. The continuum Poincare gap floor4 is retained; no finite-mesh eigenvalue replaces it.

STATE_WITNESS.json, SOLVE_RESULTS.json and INHERITED_CONTINUUM.json are byte-identical copies of the merged PR234 evidence. They contain the two-word numerical state expansions and actual reported floating outputs at omega0,4,4.5,5 with gamma1/10. This return does not run a new PDE solve. It generates new flux free-variable proposals, decodes them exactly, reconstructs the constraints and rechecks the source/output linkage against the actual stored state.

The physical flux tau is represented in the coordinate system by

$$j=(\tau_x,\tau_y,\sqrt2\tau_z),\qquad g=\operatorname{diag}(1,1,1/2).$$

Then physical divergence is coordinate div j, and physical flux norm squared is j^Tg j. Consistent stiffness/mass forms and source integration are inherited from the exact mesh construction.

## Two-level projected divergence hierarchy

The16-root-cell mesh is refined to128 parent cells and then1024 fine cells. Let v be the fixed fine conforming state, Pi1 its cellwise L2 projection onto broken affine fields on128 parents, and Pi0 its projection onto broken affine fields on16 roots. The broken polynomial spaces are nested, so Pi0 Pi1 v=Pi0 v.

The code computes these projections by exact consistent-mass moments. For each parent volume V, the affine mass matrix is V(I+11^T)/20, with inverse20(I-11^T/5)/V. All four projection normal equations are checked for every real/imaginary state component. Mean preservation gives the compatibility needed for zero-normal patch corrections.

The flux is built as:

1. Root RT1 field with divergence z Pi0v-F, zero exterior normal trace and continuous root-interface normal trace.
2. Sixteen root-patch corrections, each with divergence z(Pi1v-Pi0v), zero normal trace on its root boundary and continuous internal normal trace.
3.128 parent-patch corrections, each with divergence z(v-Pi1v), zero normal trace on its parent boundary and continuous internal normal trace.

The sum has divergence z v-F and zero exterior normal trace. The root solve has240 coefficients,196 equations of rank195 and45 free proposal coefficients per real component. Each eight-cell patch has120 coefficients,104 equations of rank103 and17 free proposal coefficients.

## One reference operator and affine flux mapping

Use the ordered Kuhn reference tetrahedron0<=xi3<=xi2<=xi1<=1 and the same eight-child edgewise pattern. Exact row reduction constructs a right-inverse action, nullspace and one compatibility condition for its RT1 trace/divergence equations. The operator is reused for all144 geometrical patches and all eight real/imaginary right-hand sides.

For a parent map x=o+G xi, use

$$j(x)=G\widehat j(\xi),\qquad\xi=G^{-1}(x-o).$$

The usual constant Piola determinant factor is absorbed into the coefficient convention. With this convention, div_x j=div_xi j_hat; the scalar divergence RHS is not additionally divided by a determinant. Zero outer normal traces and continuous internal normal traces are preserved. Physical norm integration still includes the parent volume and the metric G^TgG. These factors are not dropped.

A reference RT1 field has form a+A xi+xi(b dot xi). Under the map it remains in the global RT1 basis P1³+x times homogeneous P1. The implementation transforms its15 coefficients exactly.1152 vector roundtrips check mapped actual patch polynomials. More importantly, final global-coordinate trace and divergence checks audit the assembled field directly, without relying solely on those map roundtrips.

Floating minimization proposes the17 nullspace coefficients for each patch after accounting for the existing parent flux. Exact reconstruction imposes all104 constraints regardless of proposal roundoff. This is separate local minimum-norm proposal work, not a global15360-variable exact optimizer. Optimality is not used as a validity premise.

## Exact norm and residual certificate

All flux norms use rational polynomial moments through degree4. On the unit reference Kuhn tetrahedron with normalized measure,

$$\int\xi_1^i\xi_2^j\xi_3^k\,d\widehat\mu
=\frac6{(k+1)(j+k+2)(i+j+k+3)}.$$

Child moments are evaluated by exact barycentric expansion. The affine-map metric and normalized cell volumes are included explicitly. There is no floating quadrature-error assumption. An additional checker verifies all35 reference monomial partition identities through degree4 against the analytic ordered-tetrahedron formula, plus three mapped constant-flux norms on a translated nonorthogonal cell.

The final flux is piecewise RT1 on1024 cells, with15360 coefficients per real component. The audit performs:

- 1568 scalar root constraints;
- 119808 scalar mapped-patch constraints;
- 1152 vector map roundtrips;
- 32768 direct final divergence equalities;
- 53760 direct final boundary/interface normal-trace equalities.

RT1 normal traces are affine on each face, so checking its three vertices establishes the entire face polynomial. Divergence is affine on each cell, so its four vertices establish the entire cell polynomial. Therefore the final residual remainder is identically zero, not merely small at sampled points.

For the inexact conforming state v, set

$$\eta^2=\|\tau-\nabla v\|_{L^2}^2.$$

Integration by parts gives the exact cross-term identity used for efficient evaluation,

$$\eta^2=\|\tau\|^2+\|v\|_V^2
-2\operatorname{Re}\ell(v)-2\omega^2\|v\|_{L^2}^2.$$

The source and exact raw/corrected output identities are recomputed from the stored state and checked against SOLVE_RESULTS.json. The actual reported corrected-output evaluation bound is also recomputed from the recorded output hex. Source hashes in FLUX_RESULTS.json and SUMMARY_RESULTS.json preserve this linkage.

Because div tau=zv-F and exterior normal trace is zero, the continuum residual satisfies ||r||V'<=eta. For J(v)=2ell(v)-b_z(v,v), the previously derived complex-symmetric identity and continuum spectral factor give

$$|H-J(v)|\le\kappa\eta^2,\qquad
\kappa=\sup_{\lambda\ge4}\frac{\lambda}{|\lambda-\omega^2+2i\gamma\omega|}.$$

Add reported-output evaluation error once. The bound does not require exact Galerkin orthogonality. Raw-output bounds also include the raw/corrected offset and its own evaluation error.

## Measured certificate results

Display approximations follow; exact rational upper bounds govern acceptance. gamma=1/10 throughout. Inherited bounds and new bounds refer to the same stored state and reported output.

|omega|new eta²|new flux output radius|inherited output radius|selected radius|
|---|---:|---:|---:|---:|
|0|0.030288522|0.030288522|0.031142535|0.030288522|
|4|7.475610708|149.698988|23.476733|23.476733|
|4.5|0.726276516|16.357353|21.644546|16.357353|
|5|0.142138125|3.556295|12.572893|3.556295|

Selecting the smaller of two valid bounds is valid; it does not erase the weaker bound or claim monotonicity under refinement. All dynamic selected radii remain above1/10. Neither a precise resonance frequency nor a native UD response law follows from these samples.

## Static and continuous low-frequency consequence

The real static state is checked directly. At zero frequency,

$$H(0)-J(v)=\|u-v\|_V^2\le\eta^2.$$

Combining the new fine-flux upper with the inherited static upper and rounding outward gives [1.175722,1.206011]. The lower bound is preserved from the refined static energy value; the new work reduces the upper bound.

For bracket midpoint c, half-width r, upper Sbar and |omega|<=d<2, gamma<=1, the prior spectral-variation theorem gives

$$|H-c|\le r+\frac{\overline S\,d\sqrt{d^2+4}}{4-d^2}.$$

Including the exact binary64 center-evaluation error, rational bisection certifies d=69847/500000=0.139694 about c=2381733/2000000=1.1908665. The next10^-6 grid point fails this sufficient test only; no physical cutoff or actual failure beyond it is asserted. The complete continuous precision map is not regenerated here, and full-band1/10 accuracy remains open.

## Controls, replay and remaining gaps

Two malformed-proposal controls reject a nonfinite root free word and truncated patch free word. Two structural adversarial controls detect an incompatible zero-normal divergence RHS and a deliberately perturbed boundary flux. None is an independent review or physical experiment.

```sh
python3 flux2_moment_check.py
python3 flux2.py .
python3 flux2_summary.py .
python3 flux2_controls.py . flux2.py
```

Stored-witness replay is read-only when result files exist; imports disable bytecode. `--generate` is only for a new unpublished output directory. The numerical state and prior solver certificates are reused byte-identically. Flux proposals are new numerical data; exact posterior checks establish their validity without assuming an all-input IEEE theorem. The audit does not require NumPy; generation does. Source/helper hashes and measured backend scope are in CONTRACT.json and the witness files.

Patch corrections have zero normal trace on their parent boundaries. Consequently this hierarchy does not optimize every fine interface degree of freedom across the original macrocell boundaries. No proof is claimed that eta must tend to zero under further refinement, or that the chosen stopping rule terminates. Improving coarse-interface flux coupling or constructing an output-specific dual certificate is the next accuracy task.

The attached coefficient ledger remains an incidence/support source and does not select this scalar-wave action/damping. The CRL2 subdivision amendment remains a governance proposal. No uploaded-source bytes or scientific registry entry are changed. Missing image Gap2_FINAL_Finite_Genesis.png was not read or used; reupload was requested.

Native Project218 remains In review / Scientific OPEN / Constructor checked / Development. Its saved/reloaded next gate requests independent review, coarse-interface flux or dual improvements toward resonance1/10 accuracy, full-band precision, stopping termination and the native UD action bridge. Screenshot and receipt accompany this capture. Physical promotion remains0.
