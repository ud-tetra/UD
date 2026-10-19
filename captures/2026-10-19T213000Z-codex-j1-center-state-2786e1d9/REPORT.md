# J1 interior-center state at omega9/2 and repeated paired audit

**EXACT POSTERIOR AUDIT of NUMERICAL ENRICHMENT**, conditional on the declared scalar-wave benchmark. Development — no registry entry; constructor verification only; independent review outstanding; physical promotion **0**. Refs #218 #136. PR243 passed CI and merged at `cf9db531c490235f8f98ccc1ed127812364d480a`; integrated local/public tree `9747504bcdad886b71439d81b6785517dba92c0c` matched and repository verification passed152 captures/3161 inventoried files/156 events.

## Result

Added one interior state node per1024 coarse tetrahedra, enriching the8192-cell P1 space to **2809 nodes and12288 tetrahedra**. The exterior triangulation is unchanged. At omega4.5,gamma0.1 the new sparse two-word solve passes the algebraic1e-10 gate: raw output bound1.028e-15, corrected-output bound9.8978e-14.

On the **same1024 coarse-cell bubbles**, the squared residual lower bound falls from0.0144389683765 to0.00140510482260, ratio0.0973133804: about90.3% lower on this fixed test family. Both old source values are reproduced exactly before the new comparison.

|state|nodes|tetrahedra|same coarse-test squared lower bound, approximate|circle1/10 obstruction from this test|
|---|---:|---:|---:|---|
|original P1|285|1024|0.018844902887|YES|
|uniform-refined P1|1785|8192|0.014438968377|YES|
|interior-center P1|2809|12288|0.001405104823|Not established|

The new local-cell bubble lower bound is0.00293137939859. Added-center nodal tests give a squared lower bound about2.287e-56 on the new state, compared with0.0288266999368 when the previous uniform state is prolonged into the enriched space. These overlapping-family lower bounds are combined by maximum, not sum. The strongest available new lower bound is0.00293137939859; none of these tested bounds now establishes a circle1/10 obstruction.

**This is not a continuum accuracy pass.** Absence of a lower-bound obstruction does not provide an upper certificate. The inherited continuum disk recentered to the new reported corrected output still has radius about14.43398. An own center-mesh equilibrated-flux or output-specific dual upper certificate is the next gate. Earlier no-go conclusions remain valid for their original frozen states.

## State space and conforming interior split

The normalized J1 domain, measure2, F=10(x+y), meanfree Neumann space, continuum gap floor4, z=-omega²+2i gamma omega and external damping are unchanged. Dimensionless time remains ct/a. No physical/material promotion or native constitutive-law derivation occurs.

Within each1024-cell coarse parent, the previous eight-child subdivision contains four corner tetrahedra and four central tetrahedra sharing one interior octahedron diagonal. The midpoint of that diagonal is the coarse tetrahedron's barycenter. Add this point and bisect each of the four incident central children along the diagonal. The four corner children remain intact, giving12 cells per coarse parent.

The resulting cells have normalized volumes1/4096 or1/8192, summing to2 globally. Each new node has coarse barycentric coordinates(1/4,1/4,1/4,1/4), so is strictly interior to its parent. The reference pattern has one selected interior diagonal and12 children with total relative volume1. All12288 physical determinants/volumes are checked exactly. Every face has incidence1 or2, and the exterior face set equals the previous1536 triangles exactly.

The maximum physical diameter squared remains5/256. This is interior trial-space enrichment; a smaller global h or an error rate is not claimed. The old coarse quartic bubble previously vanished at all old vertices and edge midpoints. It now takes value1/256 at the added center, so its P1 nodal interpolant is nonzero. This supplies an interior trial direction targeted by the residual diagnosis without changing source or physical coefficients.

Prolongation from the8192-cell space uses identity at existing nodes and the average of the two old diagonal-endpoint values at each center. Exact sparse pullback reproduces both old stiffness and consistent mass matrices. The enriched stiffness has33461 nonzeros; mass has34537. Geometry, boundary agreement and nested forms establish the conforming-space relation used by the comparison.

## Sparse numerical proposal and exact algebraic audit

SciPy1.17.0 SuperLU solves K+zM atomega9/2,gamma1/10. NumPy2.3.5 supplies complex128 array/output operations. After the initial proposal, its decoded exact residual is solved once with the same sparse factorization to produce low words. Each real/imaginary nodal coefficient is the exact sum of two binary64 words; the exact weighted mean is then subtracted using w=M1 and sum w=2.

The posterior audit checks exact meanfree source, state and residual, zero stiffness row sums, and the inverse-free bound

$$\|\rho\|_{V_h'}^2\le\epsilon^2:=\frac54\sum_i|\rho_i|^2/w_i.$$

The constant5 follows from the tetrahedral consistent/lumped mass inequality, valid for these unequal positive cell volumes; the floor4 is the continuum Poincare bound on conforming meanfree states. Damping rotation and ||ell||V'<=sqrt5 bound raw algebraic output error. The complex-symmetric corrected functional J(v)=2ell(v)-b_z(v,v) uses its quadratic algebraic bound. Actual reported raw/corrected binary64 output discrepancies are added separately and once.

Both algebraic budgets pass:1.028e-15 raw and9.8978e-14 corrected, against1e-10. This is a posterior guarantee for the stored witness relative to the exact enriched Galerkin response, not an all-input IEEE theorem or continuum estimate.

The corrected output is approximately

$$-4.889359472687777-1.158629521219429i.$$

The change from the8192-cell corrected output is about0.0365661. This numerical refinement diagnostic does not bound continuum error.

## Three-state paired coarse-bubble audit

Use the original1024 coarse bubbles b_K=product of their four barycentric coordinates, each mean-subtracted globally. Their gradients have disjoint supports. Their energies remain fixed:

$$E_K=\frac{\mu(K)}{15120}\sum_a(g_{a,x}^2+g_{a,y}^2+2g_{a,t}^2).$$

For each state, integrate the identical residual tests over the12 children:

$$r_v(b_K)=\sum_{T\subset K}\int_T[(F-zv)b_K-\nabla v\cdot\nabla b_K]d\mu.$$

Degree5 mass/source products and degree3 gradient products are expanded exactly in child barycentric coordinates. Unequal child measures1/4096 and1/8192 are retained. Nine reference partition moment identities are checked.

The original1024-cell state and uniform8192-cell state are prolonged into the enriched geometry. Their two coarse-bubble lower bounds reproduce the earlier exact fractions,0.018844902887... and0.014438968377..., respectively. Only then is the new center state evaluated. This keeps the test family fixed and avoids attributing a changed test mesh to state improvement.

The lower-bound theorem is unchanged:

$$\|r_v\|_{V'}^2\ge L_{\rm coarse}:=\sum_K|r_v(b_K)|^2/E_K.$$

For any equilibrated flux estimator eta, eta²>=L_coarse. At this sample delta²=2029/16 for the phase-circle certificate |H-[J+cq]|<=delta eta². The old uniform state satisfies delta² L_coarse²>1/100, whereas the center state does not. Exact rational squared comparisons govern; displayed decimals do not establish acceptance.

A lower-bound reduction on this fixed test family does not prove the same reduction of the full residual norm, and it is not an upper error bound. The same qualifications apply to the added-node and new local-bubble test families.

## Additional residual tests

The12288 local-cell bubbles form an internally energy-orthogonal family and yield0.00293137939859. They overlap the coarse bubbles, so these lower bounds cannot be added.

The1024 added center nodal hats have disjoint coarse-parent supports and energies K_ii. Mean subtraction changes no gradient and the residual on constants vanishes. Thus sum_centers |rho_i|²/K_ii is another valid residual dual squared lower bound. It is about0.0288266999368 for the prolonged old uniform state and2.287e-56 for the new state. The latter is a numerical Galerkin-residual audit on the new trial directions, not a continuum accuracy certificate.

Taking the maximum of all tested center-state lower bounds gives0.00293137939859. These tests no longer prove a1/10 circle obstruction. Another test could reveal a larger residual, and an upper certificate is still required before accepting accuracy. Full-band coverage and stopping termination remain open.

## Replay, controls and governance

```sh
python3 center_diagnostics.py .
python3 center_controls.py .
```

The diagnostic runner first replays the complete center-state geometry/nesting/residual/output audit, then all three paired states and the additional lower tests. Stored replay is read-only and disables bytecode. Generation requires a new unpublished directory without a center witness. Controls reject nonfinite state words, truncated low words and a wrong frequency target. Old input evidence is byte-identical; source hashes are in CONTRACT.json. Files/event are append-only.

Native Project218 remains In review / Scientific OPEN / Constructor checked / Development. Its saved/reloaded next gate requests a center-mesh flux/dual upper certificate at4.5, independent review, full-band precision, termination and the native UD bridge. Screenshot and receipt accompany the capture. Constructor verification is not independent review.

The uploaded support/incidence ledger does not source this scalar-wave action or damping. The uploaded CRL2 amendment remains a governance proposal; no uploaded-source or registry edits occur. Gap2_FINAL_Finite_Genesis.png remains unavailable and was not used; reupload requested. Physical promotion remains **0**.
