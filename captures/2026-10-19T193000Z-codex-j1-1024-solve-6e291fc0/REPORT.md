# J1 1024-cell solver audit and refined static certificate

**DERIVED / EXACT CONDITIONAL**, with four actual numerical solve/output witnesses. Development — no registry entry. Constructor verification only; physical promotion **0**. Refs #218 #136; extends PR223/225/226/228/229/230/232 append-only. PR232 passed CI and merged at `714835475115611e476ec5580b2122b617844ea1` before this return.

## Result and limits

The next certified edgewise mesh has285 nodes and1024 tetrahedra. Four actual solves at omega0,4,4.5,5 and gamma1/10 are now audited using two-word coefficient expansions and an inverse-free residual bound. The worst end-to-end algebraic raw-output bound is **2.692e-15**, below the existing1e-10 budget. This is an algebraic witness certificate, not a continuum-error or physical certificate.

The real static energy lower bound improves the continuum bracket to

$$\boxed{1.175722\le H(0)\le1.206865}.$$

The upper bound is inherited from the earlier flux certificate, not recomputed on1024 cells. The corresponding midpoint proxy1.1912935 is certified to absolute error1/10 throughout

$$\boxed{|\omega|\le0.138904,\qquad\gamma\in[1/10,1],}$$

including its recorded binary64 evaluation error. The prior uniform strip ended at0.095932 around a different midpoint. The proxy center changed; the old center is not silently granted the larger interval.

Near omega4 the refined numerical response changes substantially. Recentered inherited dynamic continuum radii remain roughly12–24, so the dynamic1/10 target remains **OPEN**. A new1024-cell flux or dual certificate has not been constructed in this return.

## Mesh and fixed port

Apply the ordered edgewise rule from PR229 twice to the14-node/16-cell starting mesh. The first level has55 nodes/128 cells; this level has285 nodes/1024 cells. The certified finite-frame shape argument and h->0 family remain unchanged. Actual maximum diameter squared falls from5/16 to5/64.

The checker independently verifies every child determinant volume1/512 in normalized measure, the actual maximum diameter, the consistent mass/stiffness pullback identities and the fixed affine volume source. Normalized volume is2. The domain coordinates are(x,y,t=sqrt2*z) with metric diag(1,1,1/2), and F=10(x+y). No point-port substitution or change of units is made. Meanfree mass weights w=M1 are positive; the meanfree basis uses the largest weight as pivot, limiting the pivot ratios to at most1.

This remains an externally declared scalar-wave benchmark. Ledger incidence/support operators do not select this metric action, source or damping. Physical time normalization tau=ct/a has no calibrated c or native material identification here.

## Scalable inverse-free algebraic residual bound

For a tetrahedron of normalized volume V, the consistent local P1 mass matrix is

$$M_T=\frac V{20}(I+11^T),\qquad
M_{T,\mathrm{lump}}=\frac V4I.$$

Thus M_T>=M_T,lump/5 as Hermitian quadratic forms. Assembly gives M>=diag(w)/5. For a nodal residual vector rho and meanfree conforming v_h,

$$|\rho^Tv_h|\le
\left(\sum_i\frac{|\rho_i|^2}{w_i}\right)^{1/2}
\left(\sum_iw_i|v_i|^2\right)^{1/2}
\le\frac{\sqrt5}{2}
\left(\sum_i\frac{|\rho_i|^2}{w_i}\right)^{1/2}\|v_h\|_V.$$

The last step uses the same continuum Poincare constant1/2; no discrete gap is substituted. Therefore

$$\epsilon_h^2:=\|\rho\|_{V_h'}^2
\le\frac54\sum_i\frac{|\rho_i|^2}{w_i}.$$

The stored value is an **upper bound**, not an exact dual norm. It avoids an exact dense stiffness inverse. Sparse matrix-vector operations and sparse prolongation pullbacks also avoid dense cubic exact algebra for those steps.

Rotated coercivity gives the raw algebraic output bound sqrt5 epsilon_h/beta, plus the separately checked floating evaluation error. For the corrected collocated output, the discrete spectral lower bound lambda_h>=4 follows from conformity and the continuum gap, yielding kappa epsilon_h² plus evaluation error. These bounds compare the computed field/output with the exact finite-element Galerkin solution. Continuum discretization error is a separate obligation.

## Actual numerical pipeline and posterior audit

For each frequency, NumPy solves the284-dimensional meanfree complex system in complex128. Decode its coefficients exactly from binary64 hex. Compute its full residual in rational arithmetic, project that residual into the reduced basis and perform one additional complex128 correction solve. Store the initial and correction words separately.

The audited reference coefficient is the **exact sum of those two decoded words**. It is not a single binary64 coefficient or an assertion of IEEE quadruple precision. The reference field is lifted to the full mesh with an exact meanfree constraint. The reported floating outputs are generated from the actual rounded sum/lift/dot operations, then their distance from the rational reference raw/corrected output is bounded exactly.

The pipeline therefore includes exact residual construction; it is not described as a pure IEEE-only algorithm. Proposal quality is assessed a posteriori. No universal input-dependent rounding theorem or automatic budget guarantee at later levels is claimed. NumPy/Python versions are measured in WITNESS.json; the exact audit does not require NumPy, while generation does.

The static state is explicitly checked to be real. This is necessary for the energy lower-bound argument; a merely real corrected scalar from a complex field would not suffice. All fields have exactly zero mean and the full residual has exactly zero constant component. Three rejection controls cover a zero/under-solved state, nonfinite word and truncated correction word.

## Refined outputs and continuum provenance

Values below are display approximations. SOLVE_RESULTS.json and CONTINUUM_RESULTS.json contain exact fractions and outward bounds. gamma=1/10 throughout.

|omega|1024-cell corrected real|corrected imaginary|raw algebraic error bound|continuum radius around reported corrected output|
|---|---:|---:|---:|---:|
|0|1.175722465|0|1.89e-16|0.031143|
|4|12.284942625|-12.862627136|2.692e-15|23.476734|
|4.5|-5.287938463|-1.365899776|4.91e-16|21.644546|
|5|-2.351079826|-0.285843210|5.92e-16|12.572893|

The table's last column is not a new fine-mesh flux bound. For positive frequencies, retain the old certified continuum polygon P and old anchor disk centered at J_old. About the new exact corrected output J_new, use

$$R_{\rm new}\le\min\left\{
R_{\rm old}+|J_{\rm new}-J_{\rm old}|,
\max_{p\in\mathrm{vertices}(P)}|p-J_{\rm new}|
\right\}.$$

This is valid triangle/convexity recentering of **inherited continuum information**. Add the new reported-output evaluation error once. Raw-output radii also add the exact raw/corrected offset and its evaluation bound. No new dynamic continuum information is inferred just because the finite solve is more accurate algebraically.

For example, at omega4 the128-cell corrected output was about9.885631-4.957263i, while the new value is12.284943-12.862627i. This significant shift motivates stronger continuum certification. Its magnitude is not itself an upper bound on continuum error or a proof of a resonance location. At omega4.5 and5, the recentered radii are slightly worse than their earlier counterparts; no monotone accuracy claim is made.

## Static energy improvement and continuous low-frequency strip

For any real conforming meanfree v at zero frequency,

$$J(v)=2\ell(v)-\|v\|_V^2,\qquad
H(0)-J(v)=\|u(0)-v\|_V^2\ge0.$$

The exact refined J(v) is about1.1757224650772649. Rounding it downward to a10^-6 grid gives the new lower bound1.175722. Retain the prior rigorous upper1.206865; this yields the boxed static bracket without assuming exact Galerkin orthogonality.

Let c and r be that bracket's midpoint and half-width. The earlier spectral-variation argument gives, for |omega|<=d<2 and gamma<=1,

$$|H-c|\le r+
\frac{\overline S\,d\sqrt{d^2+4}}{4-d^2}.$$

Add the exact binary64 center-evaluation error and require this bound<=1/10. Exact rational bisection gives d=17363/125000=0.138904. The next10^-6-grid value fails this sufficient test. This is not a physical cutoff or proof that actual accuracy fails beyond it. No new complete221-cell map is claimed; the prior map is preserved, and the new uniform strip is an additional certified region with its declared new proxy center.

## Replay and governance

```sh
python3 level2_check.py .
python3 level2_continuum.py .
python3 level2_controls.py WITNESS.json level2_check.py
```

Captured stored-witness replay compares results without writing. Imports disable bytecode. Generation with `--generate` is only for a new unpublished output directory. Exact helper files are byte-identical reuse from the prior own verified mesh capture; old source certificates are copied byte-identically and hash-linked. WITNESS.json contains the actual proposal words and reported floating outputs. Constructor auditing is not independent review.

A duplicate full checkout initially hit scratch-space limits. Reversible sparse checkout omitted tracked ZIP working copies in three older clean worktrees, retaining Git objects and committed evidence. The active checkout is fully materialized for repository verification. No scientific evidence was retracted or overwritten.

The attached CRL2 subdivision file remains a governance proposal; the coefficient ledger's native support claims remain distinct from the scalar-wave benchmark. No source or scientific registry entry is modified. Missing image Gap2_FINAL_Finite_Genesis.png was not read or used; reupload was requested.

Native Project218 remains In review / Scientific OPEN / Constructor checked / Development. The next gate now explicitly requests independent review and a flux/dual certificate for the1024-cell solution, followed by resonance1/10 accuracy, full-band accuracy, stopping termination and a native UD action bridge. Screenshot and saved/reloaded receipt accompany this capture. Physical promotion remains0.
