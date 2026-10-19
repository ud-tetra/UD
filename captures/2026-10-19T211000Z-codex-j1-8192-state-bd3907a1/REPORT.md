# J1:8192-cell state and paired residual audit at omega9/2

**EXACT POSTERIOR AUDIT of NUMERICAL REFINEMENT**, conditional on the declared scalar-wave benchmark. Development — no registry entry; constructor verification only; independent review outstanding; physical promotion **0**. Refs #218 #136. PR242 passed CI and merged at `10bc8010ec538ebf0afbf82fc144680d61698f64`. Integrated local/public tree `b045330a15158ab602d88b04916a43770feccd15` matched; repository verification passed151 captures/3140 inventoried files/155 events.

## Outcome

At omega9/2=4.5 and gamma1/10, the next conforming P1 mesh has1785 nodes and8192 tetrahedra, with maximum diameter squared5/256. A sparse complex128 solve plus one exact-residual correction supplies a new two-word state. Its raw algebraic output-error bound is5.08e-16; the corrected-output algebraic bound is2.0922e-14, both below the1e-10 numerical-solve budget.

The corrected reported output is approximately

$$-4.922152448056788-1.174806575991213i.$$

Its difference from the prior1024-cell corrected output is about0.412694. This is a numerical refinement diagnostic, **not a continuum error estimate**.

The residual lower bound on the **same1024 coarse-cell bubbles** drops from0.0188449028870 to0.0144389683765, ratio0.7662002008. This is about23.4% lower for the tested residual component. It still forces the phase-circle radius above0.1: the new floor is about0.162599. Flux optimization alone therefore remains insufficient for that certificate on this newly frozen state.

The separate8192 fine-cell bubble test gives a smaller lower bound0.0039406328113. That test is inconclusive at0.1; it does not override the stronger coarse-test obstruction. Comparing only the old coarse test to a new fine test would mix state change with test-family change. Both families are retained separately, and their overlapping lower bounds are not added.

No own8192-cell flux or dual upper certificate is built in this return. The prior valid continuum disk, recentered to the new reported corrected output, gives a conservative radius about14.43497. Continuum1/10 accuracy remains **OPEN**.

## Fixed model and mesh

The normalized J1 domain, volume measure2, source F=10(x+y), meanfree Neumann space, gap floor4, z=-omega²+2i gamma omega and declared damping are unchanged. Dimensionless time remains ct/a. No native UD action/units selection or physical calibration is implied.

The1024-cell mesh is refined once by the existing ordered edgewise subdivision. Every parent has eight children. Exact determinants give normalized child volume1/4096, and the exact maximum physical diameter squared is5/256, one quarter of the previous5/64. Exact sparse prolongation checks reproduce both parent stiffness and consistent mass matrices. The geometry/source are not fitted to a target response.

The sparse stiffness has22089 nonzeros; the consistent mass has23273. Cell gradients use the physical scalar-gradient metric diag(1,1,2) in coordinates(x,y,t=sqrt2 z_physical). This is distinct from the contravariant flux metric diag(1,1,1/2). Zero stiffness row sums, source zero mean and total measure2 are checked exactly.

## Sparse proposal and exact meanfree state

SciPy1.17.0 SuperLU solves the full sparse matrix K+zM at nonzero z. NumPy2.3.5 supplies array/output operations. The solver first proposes high words, the code computes their exact rational residual after mean removal, and the same sparse factorization solves that residual to propose low words.

Every complex nodal coefficient is an exact sum of two decoded binary64 words per real/imaginary component. The exact weighted mean is then removed:

$$v_i=x_i-\frac{\sum_jw_jx_j}{2},\qquad w=M1.$$

Consequently integral v=0 exactly, independent of floating projection error. Reported raw and corrected outputs are separately recorded as actual binary64 hex words and compared with exact output functionals of this state. Solver/backend diagnostics do not replace the posterior proof, and no all-input IEEE guarantee is claimed.

## Inverse-free algebraic audit

Let rho=g-(K+zM)v. The exact full residual sums to zero. For P1 tetrahedral mass matrices, M>=D/5 with D=diag(w), because each local consistent mass is vol(I+11^T)/20 and its lumped diagonal is vol I/4. Combined with the continuum Poincare floor4 on the conforming meanfree space,

$$\|\rho\|_{V_h'}^2\le\epsilon^2
:=\frac54\sum_i\frac{|\rho_i|^2}{w_i}.$$

The damping rotation gives beta²=4gamma²/(omega²+4gamma²). With ||ell||V'<=sqrt5, the raw algebraic output error is bounded by sqrt(5epsilon²/beta²), plus the actual reported-output evaluation discrepancy. The complex-symmetric corrected functional

$$J(v)=2\ell(v)-b_z(v,v)$$

has algebraic output error at most kappa epsilon² plus its own evaluation discrepancy, with kappa=sqrt((omega²+4gamma²)/(4gamma²)) at this sample. These are errors relative to the exact discrete Galerkin response on the8192-cell space, not the continuum response.

The exact posterior bounds are5.08e-16 raw and2.0922e-14 corrected. Actual finite-precision evaluation dominates these tiny algebraic bounds. The declared1e-10 algebraic gate passes.

## Paired coarse-bubble test

The previous residual obstruction used coarse bubbles b_K=product of the four original barycentric coordinates on each1024-cell parent, each globally mean-subtracted. Their gradients are disjoint and energy-orthogonal; the residual on constants is zero. Their fixed energies are

$$E_K=\frac{\mu(K)}{15120}\sum_a(g_{a,x}^2+g_{a,y}^2+2g_{a,t}^2).$$

The new state is affine on the eight child cells, so its gradient cannot be treated as one parent-cell constant. `fine_diagnostics.py` expands the original coarse bubble into each child's barycentric coordinates and integrates exactly:

$$r_v(b_K)=\sum_{T\subset K}\int_T[(F-zv)b_K-\nabla v\cdot\nabla b_K]d\mu.$$

Degree5 mass/source products and degree3 gradient terms use exact factorial barycentric moments. Reference weights are reused for the eight-child pattern. Nine partition moment identities are checked.

As a source/implementation control, the old state is prolonged to the new mesh and evaluated with the same childwise formulas. Its resulting lower bound exactly reproduces the prior0.018844902887005677 source fraction. The new state is then evaluated on precisely the same tests. This isolates state change from changes to the test family.

|fixed coarse test family|residual dual squared lower bound, approximate|phase-circle radius floor, approximate|1/10 obstruction|
|---|---:|---:|---|
|old1024-cell state|0.018844902887|0.212214442|YES|
|new8192-cell state|0.014438968377|0.162598749|YES|

The lower bound is L=sum_K|r_v(b_K)|²/E_K. Any equilibrated flux for this state has eta²>=L. At omega4.5,gamma0.1 the phase-circle factor has delta²=2029/16, so the obstruction is the exact rational inequality delta² L²>1/100. Rounded table values are explanatory; exact fractions govern.

A decreased tested lower bound does not prove that the full residual norm decreased by the same factor, or even supply an upper bound on it. The continued obstruction applies only to certification through the delta eta² circle radius with this fixed state. It is not a lower bound on actual transfer error and does not exclude another output certificate.

## Separate fine-bubble test and next state space

The8192 new-cell bubbles give a second valid residual dual squared lower bound0.0039406328113. They form another orthogonal family internally, but overlap the coarse family; the available combined lower bound is their maximum, not their sum. The exact circle obstruction is inconclusive from the fine family alone, while the coarse family still proves it.

This uniform edge refinement adds only old vertices and edge midpoints to each old tetrahedron. The old quartic bubble vanishes at all such local nodes. Thus its P1 nodal interpolant is still zero on this refinement. This geometric observation motivates introducing interior-cell trial degrees of freedom, such as a conforming center subdivision or a controlled interior enrichment. It does not prove an optimal refinement policy or a convergence rate.

The next accuracy task should test interior-cell state enrichment at omega4.5 and repeat the same coarse-bubble audit, together with an own fine flux/dual upper certificate when feasible. More flux-only optimization cannot close the current circle gate.

## Stored replay, controls and governance

```sh
python3 fine_diagnostics.py .
python3 fine_controls.py .
```

The diagnostic runner first replays the full sparse-state geometry/residual/output audit, then the paired and fine bubble tests. Stored-results replay is read-only and disables bytecode. Generation requires a new unpublished directory without a fine witness. Controls reject a nonfinite state word, truncated low words and a wrong frequency target.

Old state/solver/bubble/continuum inputs are reused byte-identically; source hashes and verification scope are listed in CONTRACT.json. Files and event are append-only. Constructor verification is not independent review.

Native Project218 remains In review / Scientific OPEN / Constructor checked / Development. Its next gate was saved/reloaded for interior-cell state enrichment at4.5, an own fine flux/dual upper certificate, independent review, full-band precision, termination and the native UD bridge. Screenshot and receipt accompany the capture.

Continuum1/10 accuracy, full-band coverage, stopping termination, independent review and native UD action/source/units/calibration remain open. The uploaded support ledger does not source this scalar-wave action/damping. The uploaded CRL2 amendment remains a governance proposal, with no source or registry edits. Gap2_FINAL_Finite_Genesis.png remains unavailable and was not used; reupload requested. Physical promotion remains **0**.
