# AW5 metric and readout transfer under refinement

**EXACT_INTERNAL / CONDITIONAL.** Signed chains, stated metric and matched readout. Constructor verification. Independent review open. **Physical Promotion = 0.**

## Exact transfer metric, including repeated refinements

Let s be the signed subdivision chain map. It fixes each old simplex that remains and sends a subdivided tetrahedron to its oriented child sum. Let r be the simplicial chain map that sends each newly inserted vertex to a selected old vertex of the parent tetrahedron and fixes old vertices. Degenerate images map to zero. Then rs=I. For repeated refinements compose the respective maps. Write Q=I−sr. All three maps are defined grade by grade and commute with boundary in their respective domains. Every fine chain decomposes uniquely as sx+y with y in ker r.

Given the original positive definite metric M_c, choose a positive definite complement weight W and form

$$M_f=r^T M_c r+Q^T WQ.$$

The two fine subcomplexes are orthogonal for M_f, which is positive definite because rx and Qx jointly determine x. This makes s an isometry and its metric adjoint r. Because both summands are boundary-invariant, both are invariant under the metric boundary adjoint and the resulting skew Hodge–Dirac generator. In particular A_f s=sA_c. The coarse drive q transfers as sq, with readout covector M_f sq=rᵀ M_c q. Thus every collocated response is identical on the lifted coarse subspace, including the zero-frequency residue 1/4 and the same norm convention. The argument applies at any finite depth of the indicated refinement family. It also gives a transfer of the damped response if damping is transferred on the same invariant subspace. Reusing a fine coordinate-mask damping operator requires a separate check.

The construction is a family indexed by collapse and complement metric choices. It provides existence of exact transfer without fitting the residue. It does not select a unique native physical metric. The lift fixes the drive coordinates on exterior faces. Its metric-dual readout can include interior coordinates. For the first-leaf collapse to vertex 1 and W=I, replay gives 1/4 for the transferred readout and 3/13 for the raw exterior covector renormalized in the fine dual norm. If the raw covector instead keeps its original gain, it agrees on the lifted coarse subspace; a collocated raw drive can also excite fine complement modes.

A simpler finite diagonal repair fails under a common internal-face weight. With unit weights on old faces and weight w>0 on all six new interior faces of a split leaf, the oriented child Gram is (1+4w)I−wJ. The new exterior coefficient magnitude is w/(1+4w), smaller than 1/4 for every finite w. The shell coefficient is three times that value. With at least one such split, the frozen-drive residue is (sum over leaves of their exterior coefficient magnitude)/4, strictly below 1/4. This obstruction applies to the stated diagonal family.

## Euclidean Whitney-style check

Use cochains and the exact degree-2 Whitney L² mass matrix of an explicit rational Euclidean embedding. The hub vertices are the origin and the three coordinate unit vectors. The four leaf apexes are (1,1,1), (−1,0,0), (0,−1,0), (0,0,−1). Subdivide the first leaf at its barycenter. Use the same signed exterior load covector given by the original unit-simplex harmonic exterior coefficients, with no extra rescaling. The exact mass assembly and kernel equations B₃ᵀh=0 and B₂ M₂ h=0 yield

| Euclidean Whitney metric | Fixed exterior load residue | Unit-dual normalized residue |
| --- | ---: | ---: |
| Before refinement | 27/64 | 1/6 |
| One leaf refined | 27/64 | 43/273 |

The fixed-load residue uses (lᵀh)²/(hᵀM₂h). Unit-dual normalization divides this by lᵀM₂⁻¹l. Neither normalized value equals the unit-simplex 1/4 benchmark.

For these interior-only refinements, the fixed-load equality has an explanation that extends to nested refinements with all original faces intact. The vector proxy of a closed Whitney 2-form on an affine tetrahedron is a constant vector: the local lowest-order space has the form a+b x with scalar b, and closure forces b=0. The coarse closed field therefore extends into the refined space with unchanged energy. The flux of any closed fine field on each original face is constant there, since the original face remains a single triangle. On each coarse tetrahedron its volume mean is determined by those four normal fluxes via integration by parts against linear coordinate functions. For a fine exact cochain the original face flux restriction is coarse exact, by the subdivision chain map. The coarse harmonic field is orthogonal to that coarse exact cochain, and hence to the fine exact field by the volume-mean identity. Its lift is harmonic and keeps the original face loads. The load's dual norm can still change as the fine test space expands. A transferred unit readout requires a declared transfer and normalization.

## Relation to the acquisition threshold

The unweighted 1/5 floor concerns the undamped harmonic residue for the five declared one-split-per-leaf cases. It is neither a finite-time contrast guarantee nor a bound for arbitrary parasitic subdivisions. The frozen AW5 scorer compares two signed finite-window means with 3/64, and the signed-pair bench intake tests the two-state circuit calibration. Neither has a refinement mode. Even assuming the old positive-frequency, damping and acquisition allowances transfer, substituting 1/5 into that conservative budget gives 1/5−1/8−1/64−1/32−1/32=−1/320. Certifying a refined carrier requires its identified model and a renewed contrast bound. No alteration to either gate is justified by the DC floor alone.

Replay: `python3 metric_transfer_aw5.py` with SymPy 1.14. The two sibling captures supply the signed incidence and the unweighted refinement controls.
