# Global edge-curl correction of the J1 fixed-port flux

**DERIVED / EXACT CONDITIONAL**, with audited floating proposals. Development — no registry entry; constructor verification only; independent review outstanding; physical promotion **0**. Refs #218 #136. PR238 passed CI and merged at `e8ec3cfe3c68a17450542fdfc6980c46823bed54`; public/local verified tree `df71f305ae6c2e167ebba93b6e1f9f70542f8cf5` matched. Old evidence is preserved.

## Outcome

A globally coupled correction now crosses the original macrocell interfaces. Its924 interior-edge potential coefficients per real component generate piecewise constant divergencefree flux corrections. The exact audit verifies17920 correction face/component traces, eight gradient-orthogonality identities and eight nonincrease inequalities.2240 trace components on original macrocell interfaces change. The prior86528 direct final scalar divergence/trace checks pass on the corrected assembled RT1 field.

The gain is modest, and the remaining limitation is now explicit:

|omega, gamma=1/10|old selected phase radius|new selected phase radius|new eta²|1/10 gate|
|---|---:|---:|---:|---|
|0|0.0151442611|0.0141893157|0.0283786314|PASS|
|4|23.4767331|23.4767331|6.9151662311|FAIL|
|4.5|8.1786766|7.5238449|0.6681266645|FAIL|
|5|1.7781474|1.6234309|0.1297706986|FAIL|

The phase radii at0/4.5/5 refer to newly computed proxy centers, not automatically to the previous outputs. At4 the inherited moment-based disk remains the best selected candidate. Around the same original corrected FEM outputs, the new direct norm-based bounds improve to15.04769 at4.5 and3.24686 at5; the old-center polygon and phase candidates remain separately recorded. All displayed decimals are explanatory; exact fractions/hex words govern.

The static bracket improves to

$$[587861/500000,602051/500000]=[1.175722,1.204102].$$

With its new midpoint148739/125000=1.189912, the inherited spectral-variation theorem certifies uniform1/10 accuracy on |omega|<=70731/500000=0.141462 for gamma in[1/10,1], including the recorded proxy evaluation error. The next10^-6 grid point fails this sufficient test only, not a physical cutoff. This low-frequency consequence does not establish resonance/full-band accuracy.

## Frozen model and coordinate convention

The scalar-wave benchmark is unchanged: normalized J1, mu(Omega)=2, F=10(x+y), meanfree Neumann Laplacian, continuum gap floor4, z=-omega²+2i gamma omega, externally declared gamma and dimensionless time ct/a. The fixed285-node/1024-cell state and original hierarchical RT1 flux are reused byte-identically. No PDE solve, mesh refinement, physical calibration or native UD constitutive derivation occurs here.

Use coordinates(x,y,t=sqrt2 z_physical), contravariant flux j=(tau_x,tau_y,sqrt2 tau_z) and metric g=diag(1,1,1/2). Physical divergence equals coordinate div j; flux norm is integral j^Tg j. For a P1 state, physical flux-gradient pairing with a coordinate correction k is integral grad_coordinate(v) dot k. These conventions are checked by exact global gradient orthogonality.

## Global curl construction

Let phi_i be continuous P1 nodal hats on the fine mesh. For each globally oriented edge i<j, define the coordinate edge potential

$$W_{ij}=\phi_i\nabla\phi_j-\phi_j\nabla\phi_i,$$

whose cellwise curl is

$$k_{ij}=2\nabla\phi_i\times\nabla\phi_j.$$

This is piecewise constant, so cellwise divergence vanishes. Tangential potential traces agree across faces; hence the curl's normal trace agrees. Exclude every edge on an exterior triangular face. The remaining potential has zero exterior tangential trace, yielding zero exterior normal curl trace. Global edge orientation is fixed by vertex index, rather than local tetrahedron order.

There are1500 total edges:576 boundary edges excluded and924 interior edges retained. The field is represented by7392 recorded binary64 words across the eight real components of four complex fixtures. NumPy2.3.5 `linalg.lstsq` proposes the coefficients in a3072-by924 weighted cell-vector system. Its numerical rank is833. This is a numerical diagnostic; no exact rank or global RT1 optimality claim depends on it. The redundant potential gauge does not affect validity of the represented curl.

The objective uses each cell's exact mean original flux, metric weights and equal normalized volume1/512. Since the correction is constant per cell, minimizing the mean-flux objective also minimizes the full flux norm within this proposal space, up to a constant. Floating minimization is not a proof of optimality.

For every stored component, the posterior audit computes exactly

$$\Delta=\sum_K\mu(K)[2\overline j_K^Tg k_K+k_K^Tg k_K]\le0,$$

and verifies integral grad(v) dot k=0. Therefore adding k does not increase eta²=||tau-grad v||². The new estimator also equals the old estimator plus the exact real/imaginary norm changes, an identity checked against the frozen prior result.

The correction changes2240 component traces across320 original macrocell-interface faces. This directly resolves the earlier zero-normal-parent restriction for the tested correction space. It does not optimize every RT1 interface degree of freedom.

## Continuum output certificate and actual proxies

The unchanged phase-aware theorem gives

$$|H-[J(v)+c_zq]|\le\delta_z\eta^2,\quad
q=\int(\tau-\nabla v)\cdot(\tau-\nabla v),$$

$$c_z=1/2-i\omega/(4\gamma),\qquad
\delta_z=\tfrac12\sqrt{1+\omega^2/(4\gamma^2)}.$$

At zero frequency use c=delta=1/2. New exact mixed flux moments yield q; covariance positivity, source/output identities, conjugacy, outward rational square roots and actual binary64 proxy evaluation errors are audited. A phase disk, inherited disks and rational outer-polygon intersections remain distinct candidates; the minimum valid reported radius is selected. No exact Galerkin orthogonality or all-input IEEE theorem is assumed.

## Constant-correction variance obstruction

For any piecewise constant correction k, on each cell K decompose d=tau-grad v into its mean and fluctuation. Because grad v is constant on a P1 cell,

$$\int_K|d+k|^2
=\int_K|\tau-\overline\tau_K|^2
+\mu(K)|\overline d_K+k_K|^2.$$

Consequently every such correction, even one unconstrained by divergence or normal continuity, satisfies

$$\eta_{\rm corrected}^2\ge L_{\rm const}
:=\sum_K[\|\tau\|_{L^2(K)}^2-\mu(K)|\overline\tau_K|^2].$$

The exact cell means and original flux norms determine this invariant floor. The audit uses the rational squared test delta² L_const² > (1/10)², avoiding any inward-root ambiguity.

|omega|eta² floor|phase-circle radius floor, approximate|constant-only circle1/10 obstruction|
|---|---:|---:|---|
|0|0.010058971|0.005029485|No obstruction proved|
|4|2.375164703|23.781318057|YES|
|4.5|0.227070579|2.557065771|YES|
|5|0.043510630|0.544317811|YES|

**Scoped NO-GO:** no piecewise constant correction to this frozen flux can meet the1/10 target using the delta*eta² phase-circle certificate alone at the three dynamic fixtures. This is not a lower bound on actual transfer error. It does not rule out another certificate, extra spectral information, nonconstant divergencefree corrections, a changed state/flux or refinement. In particular the inherited moment disk can be smaller than this circle-family floor without contradiction.

This obstruction makes further constant-only optimization insufficient for the declared circle target, regardless of the numerical solver tolerance. The next substantive space should contain nonconstant curls or globally coupled RT1 corrections; repeated tuning inside the same constant space cannot close this gate.

## Validation and replay

`curl_flux.py` extends the prior phase audit, preserving all root/mapped-patch reconstruction and final divergence/trace checks. `curl_interface.py` decodes the stored proposal, computes cell means/curls exactly, verifies continuity/orthogonality/decrease and records the variance floor. `curl_circle.py` and `curl_summary.py` update output and static/low-frequency consequences. `floor_check.py` verifies floor/source linkage and exact squared obstruction tests.

Malformed nonfinite and truncated coefficient payloads are rejected; a corrupted exterior trace is detected. The inherited spectral sign, solenoidal, covariance, damping and outward-rounding controls are retained. Constructor verification is not independent review.

```sh
python3 curl_flux.py .
python3 curl_circle.py .
python3 curl_summary.py .
python3 floor_check.py .
```

Stored-results replay is read-only and disables bytecode. `--propose-curl` is restricted to a new unpublished directory without a curl witness; it does not regenerate the prior state or hierarchical flux. Exact posterior checking needs no least-squares solve. Witnesses, receipts and source hashes are captured; old published bytes remain unchanged.

## Remaining gates

Dynamic/full-band1/10 precision, estimator convergence and stopping termination remain open. Native Project218 remains In review / Scientific OPEN / Constructor checked / Development, with its next gate updated to nonconstant curl/global RT1 corrections or spectral information, independent review, full-band precision, termination and the native UD bridge. A saved/reloaded screenshot receipt is attached.

The uploaded support/incidence ledger does not select this scalar-wave action or damping. The uploaded CRL2 subdivision document remains a governance proposal. No source/registry changes or physical identification are made. Gap2_FINAL_Finite_Genesis.png remains unavailable and was not used; reupload requested. Physical promotion remains0.
