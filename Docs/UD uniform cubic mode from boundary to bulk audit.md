2026-10-02, America/Chicago. Development lane. Constructor: Codex. Independent review: pending. Internal claim bin: CANDIDATE_DEVELOPMENT_MATHEMATICS. Correspondence status: NOT_PROPOSED. Physical promotion: 0.

The isolated cube's uniform oscillating cell mode does not survive unchanged when that cube subdivision is extended. On an open block of several cubes, the uniform vector is not an eigenvector. On the periodic carrier tested here, it is a zero-frequency top cycle and cannot supply a nontrivial uniform crossing clock.

The earlier full-support single-frequency compatibility result remains valid for an admitted mode on its supplied carrier. The present audit narrows a proposed uniform-mode interpretation: the isolated cube's squared frequency2 is set by its boundary-face pattern, rather than establishing a size-independent uniform bulk oscillator.

## Sources and declared family

The [single-frequency audit](https://chatgpt.com/space/page_0006b51b8d2081918648f9daa490de3e) supplied compatible eigenvectors on the six-tetrahedron cube and showed that native evolution preserves supplied modal preparation without dynamically selecting it. Its result snapshot is retained with its original identity.

The already inspected collective-closure note supplies u'=j, j'=-G u, G=B3^T B3 and j=B3^T f on finite unit-metric 3-complexes. Its note explicitly says top kernel modes are static and distinguishes core amplitudes from event counts. The complete note is retained from the October2 gap-inventory release.

The new carriers are n by n by n arrays of unit cubes, each subdivided by the same six coordinate-order tetrahedra and oriented coherently. We separately test open boundary and periodic boundary carriers. Periodic coordinates identify opposite sides; n>=3 avoids small-quotient degeneracies in this construction. These are separate fixed source flows. No state jump, topology-changing dynamics or physical lattice selection is claimed.

Geometric cubes define incidence only. The source still uses unit simplex norms, not Euclidean length/volume weights. n is a declared carrier size, not a fitted dynamics coefficient. The periodic carrier is an artificial boundary test, not an asserted topology of physical space.

## Exact Gram decomposition

Every interior triangular face belongs to two cells with opposite oriented coefficients; every exterior triangle belongs to one. Let A be the face-sharing adjacency, d_c its degree and b_c=4-d_c the number of exterior triangular faces of cell c. Then:

```text
G = 4I - A = L_face + diag(b)
G 1 = b
x^T G x = sum_internal_faces (x_c-x_d)^2
          + sum_cells b_c x_c^2.
```

L_face is the ordinary degree-minus-adjacency graph Laplacian. The decomposition follows directly from the coherent incidence rows. It separates internal differences from boundary penalties. It does not define a physical propagation speed or identify graph distance with a spacetime metric.

## Open cube blocks

One isolated cube has six cells with two exterior faces each. Thus G1=2·1 and the uniform cell frequency is sqrt2. For n>1, interior and boundary tetrahedra have different b_c. Equal initial amplitudes do not remain one uniform oscillator: with j(0)=0, their initial accelerations are u_c''(0)=-b_c u_c(0).

The exact carrier tests give:

| Cubes per axis | Tetrahedra | Cells with b=0 | Cells with b=1 | Cells with b=2 | Uniform vector is an eigenvector |
|---|---|---|---|---|---|
| 1 | 6 | 0 | 0 | 6 | Yes, eigenvalue2 |
| 2 | 48 | 12 | 24 | 12 | No |
| 3 | 162 | 72 | 72 | 18 | No |
| 4 | 384 | 216 | 144 | 24 | No |

The general counts are 6n(n-1)^2, 12n(n-1) and6n respectively. Each coordinate-order tetrahedron has two possible cube-exterior faces, on distinct axes. Counting origins at neither, exactly one or both outer boundaries gives those formulas. Their sum is6n^3; the boundary-face total is12n^2.

The uniform vector's Rayleigh quotient and best scalar residual are:

```text
(1^T G 1)/(1^T 1) = 2/n
||G1-(2/n)1||^2 / ||1||^2 = 2(n-1)/n^2.
```

For n>1, the first expression is not an eigenvalue or an exact uniform frequency. It is an energy quotient. It does provide the bound lambda_min(G)<=2/n. Thus this open carrier family has no positive lower spectral bound independent of size. No exact continuum law or physical dispersion relation is inferred.

The face-sharing graph is connected. The quadratic decomposition proves the open Gram matrix has no kernel: zero internal differences force a constant vector, and a nonempty boundary then forces that constant to zero. All open blocks still have positive oscillating modes; the uniform vector simply mixes them when n>1.

## Periodic boundary test

The n=3 periodic carrier has27 vertices,189 edges,324 faces and162 tetrahedra, with no boundary triangles. Its face-sharing graph is connected and four-regular. Every oriented face row cancels in B3·1, so G1=0.

The top kernel is one-dimensional: the quadratic form contains only internal differences, and connectedness forces any zero-energy top vector to be constant. Crucially, the native rate is constrained to j=B3^T f. Therefore:

```text
1^T j = (B3 1)^T f = 0.
```

A uniform top preparation cannot be assigned a nonzero uniform rate within that native interface. A pure uniform preparation u=a·1 with no other active sector stays static. It yields no nontrivial transverse crossings. The constant top component is a harmonic cycle, not a common oscillating clock.

This is stronger than merely setting lambda=0 in an unconstrained second-order equation and allowing u to drift linearly. Such a uniform drift would require a rate outside im(B3^T) and is not admitted by the inspected native source. Other positive, nonuniform periodic modes remain possible and are not classified by this audit.

## Interpretation for the cubic hypothesis

The cube remains a useful supplied geometric and computational carrier. Its isolated uniform oscillator, however, cannot be treated as a universal uniform bulk clock on the basis of that example alone. Boundary conditions and the admitted cell mode matter independently of local tetrahedral closure.

The earlier discrete event-order lift did not require a uniform mode specifically. A full-support nonuniform single-frequency mode could still provide compatible counts, provided it is admitted on the extended carrier. Native modal conservation still does not explain why such a preparation is selected. A source-defined preparation, event selector or new coupling remains open.

This result does not reject every cubic, periodic or BCC interpretation. It examines one declared cube subdivision with unit simplex norms. It does not transfer a single-cube state into a bulk state or identify all of its positive modes with physical waves.

## Verification and next bounded target

6917 exact constructor assertions pass on open blocks with n=1,2,3,4 and the periodic n=3 carrier. They verify distinct tetrahedra, coherent face pairing, boundary-of-boundary identities, connectivity, Euler counts, Gram row sums, the boundary histograms, rational residuals, and quadratic-form identities. Kernel conclusions follow from the connected-graph proof, not a floating-point rank estimate.

The next useful positive test is a nonuniform periodic mode: derive it from exact incidence, check that every cell is active and its crossing cadence admits the discrete event lift. That can establish a compatible bulk branch. It cannot by itself establish source selection; a separately admitted law must still choose the preparation or events.

Earlier artifacts and canonical sources remain unchanged. Physical promotion remains0. Page content is verified by readback; visual layout is unverified.
