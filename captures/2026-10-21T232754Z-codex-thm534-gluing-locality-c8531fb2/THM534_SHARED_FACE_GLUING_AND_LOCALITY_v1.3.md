# THM-534 shared-face gluing and locality audit, v1.3

October 21, 2026. EXACT CONDITIONAL mathematics; scoped locality obstruction. Development, no registry entry. Physical promotion 0; outside peer review pending. Labels G1–G5 are local, not new global theorem allocations.

## Result and source scope

The single-tetrahedron maximal-permission policy of PR371 cannot be applied independently to cells sharing a face. Its global extension exists, but it makes every edge–face column in a face-connected component switch off when the component's vertex–edge mask is mixed. This is a precise locality limitation, not a failure of the earlier norm-conservation or conditional recovery proofs.

Sources: the preserved PR371 permission theorem at GitHub commit `1d461876655cfc75521c0cc4b7a9c0c2ca47100e`; attached coefficient ledger Q169–Q173 for unique global simplices and control-volume flux, and Q177–Q179 for equal-top-star ownership; THM research branch checked at `b8701df319db7391a1065aa56c4f957f221844a5`. The permission theorem is copied here byte-for-byte as source data. The verifier is new standard-library code and executes no source archive or previous verifier.

Effective-chain nilpotency and maximal contact count are still additional hypotheses. Neither is promoted to a native UD constitutive law by this audit. The underlying topological chain identities and the identities of transport-masked operators remain distinct.

## Carrier and permissions

Let K be a finite pure tetrahedral simplicial complex, with one coordinate per unique simplex. Two cells are face adjacent if they share a triangular face. Work on each connected component of that cell adjacency graph and all its contained faces and edges. Global signed boundaries satisfy B1 B2=B2 B3=0.

Use binary edge mask h and binary face masks a,t:

\[
D_1=B_1\operatorname{diag}(h),\qquad
D_2=B_2\operatorname{diag}(a),\qquad
D_3=\operatorname{diag}(t)B_3.
\]

Both contacts incident to a shared face use its same global a_f and t_f. Incidence-specific per-cell face permissions are a different family and are not covered by the following classification. Transport permissions do not remove geometric simplices.

## G1 — Live face–cell contacts force component-wide face uniformity

Assume every face–cell contact is live, t_f=1. Then D2 D3=0 holds exactly when a is constant on the faces of every face-adjacency component.

**Proof.** Examine one cell column of B2 diag(a)B3. It is the boundary of that tetrahedron's weighted oriented boundary. On the six edges of this cell, the local face-boundary map has one-dimensional kernel spanned by its oriented tetrahedral boundary. Therefore its four face weights must agree. The embedding of these six local edges into global edge coordinates is injective, so cancellation cannot be supplied by another cell column. Shared faces propagate equality to face-adjacent cells. Conversely a constant multiplier on each component makes each cell column a scalar multiple of B2 B3=0. QED.

This argument uses the local tetrahedron kernel; it does not assume that the global B2 has a one-dimensional kernel. In larger complexes that global statement would generally be false.

## G2 — Global maximal completion and its exact counts

With t=1 and both chain identities imposed, a component has only these possibilities:

- a=0 on all its faces: any h on its edges is allowed.
- a=1 on all its faces: h must be constant on all its edges.

**Proof.** G1 gives the two a choices. If a=1, each triangular face boundary must have three equal h values to make D1 D2=0. Within a tetrahedron these equalities connect all six edges, and shared faces propagate equality between tetrahedra. If a=0, both products vanish. QED.

For a face-connected carrier with E edges, the count of compatible (h,a) pairs is therefore

\[
2^E+2.
\]

The unique maximal-contact completion is a=1 on a component exactly when its h restriction is uniform; otherwise a=0 throughout that component. Uniqueness remains conditional on maximizing the number of live a columns.

The exact verifier accounts for all h,a pairs by first evaluating the second product for every a and then the first-product columns for every h. Eliminating an a whose second product is nonzero eliminates all its h partners exactly; no numerical sampling is used.

| Carrier | f-vector | Chain dimension | Binary pairs accounted for | Compatible pairs |
|---|---|---:|---:|---:|
| One tetrahedron | (4,6,4,1) | 15 | 1,024 | 66 |
| Two cells sharing face 012 | (5,9,7,2) | 23 | 65,536 | 514 |
| Three face-connected cells | (5,10,9,3) | 27 | 524,288 | 1,026 |
| Boundary of the 4-simplex | (5,10,10,5) | 30 | 1,048,576 | 1,026 |
| Two disjoint tetrahedra | (8,12,8,2) | 30 | 1,048,576 | 4,356 |

The disconnected control gives 66 squared, since its coordinates are disjoint. For general components that share lower-dimensional simplices, no unrestricted product formula for the h counts is asserted.

## G3 — Concrete shared-face conflict; neither AND nor OR repairs it

Take cells 0123 and 0124 sharing the single global face 012. Let h_03=1 and every other h bit be zero. The first cell's edge mask is mixed; the second cell's is uniformly zero.

Independent single-cell maximal completions assign **a_012=0** from cell 0123 and **a_012=1** from cell 0124. Both cannot be a permission of the one shared face. Duplicating that face coordinate would change the carrier from the frozen global unique-simplex construction.

Merging the two prescriptions with AND leaves the first cell's faces off and the second cell's three private faces on. The second cell then has an incomplete weighted boundary, and

\[
\|D_2D_3\|_F^2=3.
\]

Merging with OR instead enables the shared face and leaves the first cell's three private faces off; now the first cell column has the same squared defect, 3. These are exact matrix counterexamples. A full triangle boundary has three unit-magnitude entries, explaining that value; it is not an inferred physical curvature.

The global chain-compatible maximal completion sets all seven face columns to zero, including the three private faces of the otherwise uniform second cell. Thus the candidate imposes a component-wide edge–face transport response to a local mixed edge pattern. It does not close every grade: face–cell support dynamics may continue.

## G4 — Support conservation and shared ownership survive; they do not select flatness

The AND control in G3 has a nonzero effective chain defect. Nevertheless the block generator with D1,D2,D3 in its upper off-diagonal blocks and their negative transposes in the lower blocks is real skew. Its Cayley update preserves the full 23-coordinate support norm exactly.

For each cell tau, retain the Q177–Q179 ownership convention

\[
w_{\sigma,\tau}=
\frac{\mathbf1[\sigma\subseteq\tau]}{n_3(\sigma)},
\qquad
S_\tau=\sum_\sigma w_{\sigma,\tau}z_\sigma^2.
\]

Here n3 counts containing top-dimensional tetrahedra. Purity ensures that denominator is positive, and

\[
\sum_\tau w_{\sigma,\tau}=1,
\qquad \sum_\tau S_\tau=\|z\|^2.
\]

The shared face has weights 1/2 in both cells, not two copies of its entire support. For the chosen skew-current convention and a Cayley event of size epsilon, its exact midpoint receipt is

\[
\Delta S_\tau=
2\epsilon\sum_{i<j}
(w_{i,\tau}-w_{j,\tau})A_{ij}\bar z_i\bar z_j,
\quad \bar z=(z+z')/2.
\]

**Proof.** Use z'-z=epsilon A bar-z and the squared-amplitude midpoint identity. Group the two contributions for each skew pair i,j. Summing over cells gives zero because the ownership weights at each coordinate sum to one. The sign of the displayed current is positive into the lower-index coordinate; a different source current orientation must be transformed consistently. QED.

A rational 23-coordinate control verifies the full norm, the shared-face half weights, both cell receipts, and cancellation of their total change, despite the chain defect. This shows directly that support conservation and correct ownership accounting alone cannot require the effective masked chain identities. No physical energy interpretation is used.

## G5 — A locality and local-transition barrier

**Memoryless locality obstruction.** There is no uniformly bounded face-adjacent-cell-radius, memoryless rule that computes the exact global maximal completion of G2 on every finite face-connected tetrahedral carrier.

**Proof.** Consider stacked cells (i,i+1,i+2,i+3), i=0 through m−1. Their face-adjacency graph is a path. Start with every h bit zero: maximal completion assigns a=1 everywhere. Change only edge 01, which belongs to the first cell alone. The component's h is now mixed, so G2 requires a=0 at a private face of the last cell. For m larger than any proposed radius, the input in that last cell's radius neighborhood did not change but its required output did. This contradicts such a rule. QED.

An eight-cell rational/combinatorial control checks the endpoint geometry and changed edge. The proof is for arbitrary m; the finite control does not substitute for it. Locality here is a stated combinatorial neighborhood condition, not a claim about physical distances, light cones or time units.

**Stronger contact-transition barrier.** Even if the common face–cell mask t may change, D2 D3=0 requires

\[
c_f:=a_ft_f
\]

to be constant throughout each face-adjacency component, by the same local-column proof as G1. In any effective-chain-compatible state with c=1, changing to c=0 requires changing at least one of a_f,t_f at **every face** in that component during the transition. An update confined to a proper subset of those faces cannot accomplish it while keeping both endpoint states chain compatible. Changing h alone cannot create a mixed h while c=1, since a=1 then and the first identity forces uniform h.

Consequently the all-on contact configuration has no chain-compatible one-bit neighbor within this family. The checker confirms that barrier on the shared-face pair and the eight-cell stack. This is a statement about mask transitions, not about amplitudes becoming frozen or support disappearing; fixed-mask amplitudes may continue to evolve.

## Disposition and next source requirement

The mathematics of PR371's single-cell completion remains valid. Its promotion as a **native local repair law** is held: independent cellwise application conflicts at shared faces, and exact global completion requires component-wide information and transitions in the stated family.

No native requirement for effective-chain flatness has been recovered. It must not be imposed merely because the unmasked topological boundaries compose to zero. The next model choice must be source justified: permit and account for transport defects; supply a genuinely different incidence-permission/transition family; or provide explicit nonlocal/atomic coordination semantics. Adding a shared-face protocol, extra memory or new degrees of freedom is a new construction requiring its own receipts and tests, not a consequence of this theorem.

The isolated higher-grade support branch remains a conditional example; this result neither makes its sign/AND readout canonical nor produces persistent passive burden circulation, physical action units or particle correspondence. No held-out experiment was conducted. Physical promotion remains 0.
