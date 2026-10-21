Date: 1 October 2026, America Chicago. Development audit v0.1. Physical promotion 0. Constructor evidence, no independent review or novelty claim. Frozen papers and coefficient values receive no changes.

The six-tetrahedron carrier supports a consistent spatial assembly, but its unweighted scalar propagation is anisotropic in the supplied orthogonal cube embedding. Requiring an isotropic leading propagation term fixes a different Gram shape, up to scale: a body centered cubic primitive lattice cell with basis angle cosine minus one third. This is an exact conditional result under an added isotropy criterion. The admitted UD source does not yet select that criterion or embedding.

## Source scope and added premises

The source rule inspected in the current boundary content audit is the finite reversible support generator A = B transpose minus B. This development extends its incidence construction to the declared macrocell and a translation invariant infinite mesh, using a unit Euclidean pairing on chain coordinates. Carrier admission and geometric embedding remain candidate interfaces. No reciprocal support burden cross operator, geometric stock allocation, action, physical clock, physical length unit, or irreversible selector is added.

Sources inspected during this session:

- UD_BOUNDARY_CONTENT_VOLUME_LIVING_AUDIT.md, saved version 5, including step 6 on recurrent finite skew flow. Its most recent modification at inspection was 1 October 2026.

- UD_BIDIRECTIONAL_SUPPORT_BURDEN_CURRENT_RUNTIME_RESULT_v0.1, dated 18 September 2026. It reports the absent reciprocal cross operator in the inspected runtime package.

- The user's numbered cube and hub and spoke sketches, and the later two colored face sketch. The colored faces are interpreted as opposite faces of one parallelepiped; the photo supplies no measured coordinates or confirmed Gram matrix.

No earlier reported protected regression or empirical experiment is claimed to have been replayed by this package.

## Carrier construction and finite assembly

Use the standard cube with endpoints 000 and 111 on the common body diagonal. Its six tetrahedra are indexed by permutations of the three coordinate steps. Reflecting y and translating gives the original drawing's diagonal 3 to 6. The reference tetrahedra have squared edge signatures 1, 1, 1, 2, 2, 3 and each has unit reference volume divided by six. They are congruent and nonregular.

| Carrier | Vertices | Edges | Triangles | Tetrahedra | Chain coordinates | Internal faces | Boundary faces |
|---|---:|---:|---:|---:|---:|---:|---:|
| One cube | 8 | 19 | 18 | 6 | 51 | 6 | 12 |
| Two cubes along x | 12 | 33 | 34 | 12 | 91 | 14 | 20 |
| Two by two by two cubes | 27 | 98 | 120 | 48 | 293 | 72 | 48 |

The matrices have exact boundary nilpotency, consistent exterior faces and coherently oriented occupancy cancellation. Their rationally computed homology dimensions are 1, 0, 0, 0. The one cube boundary ranks are 7, 12, 6. Six separate tetrahedra contain 90 local coordinate occurrences, which reduce to 51 distinct simplex coordinates after gluing. These are chain basis counts, not physical degree of freedom counts.

The finite assembled generator is skew and obeys:

```text
A = B^T - B
A^2 = -(B B^T + B^T B)
```

The shared-face dual graph of one cube is a six-cycle, with incidence rank five and one independent divergence-free circulation. In the two-cube and eight-cube blocks the dual cycle dimensions are three and twenty-five. These graph circulations are not spatial holes in the contractible filled blocks.

## Metric nonidentifiability survives fixed volume

Connectivity and unit incidence leave the embedding unspecified. Even preserving the twelve selected diagonal symmetries and the macrocell volume does not choose a metric.

Let J be the three by three all-ones matrix. A reference identity embedding and the following rational stretch have the same carrier and unit volume:

```text
E0 = I
E1 = I/2 + 7J/6
det(E1) = 1
G0 = I
G1 = E1^T E1 = I/4 + 21J/4
```

E1 has longitudinal stretch four and transverse stretch one half. The twelve signed permutations preserving the selected diagonal also preserve G1. This provides a metric failure witness under stronger conditions than arbitrary shear. Fixing volume alone does not fix shape; no fitted density identity repairs this ambiguity.

## Periodic scalar propagation

Translation orbits contain one vertex type, seven edge types, twelve triangle types and six tetrahedron types, for twenty-six chain coordinates per primitive cell. Periodic boundary entries are exact Laurent polynomials. Both boundary compositions vanish coefficient by coefficient, so a small aliased torus is not used as a substitute for the infinite periodic carrier.

For the scalar degree-zero component, the squared generator gives the vertex graph Laplacian. With wavevector q in declared reference lattice coordinates and D the seven nonzero binary displacement vectors:

```text
omega(q)^2 = 2 sum[d in D] (1 - cos(q dot d))
S = sum[d in D] d d^T = 2I + 2J
omega(q)^2 = q^T S q + terms of fourth and higher order
```

S has eigenvalue eight along 111 and two in the perpendicular plane. Therefore the leading scalar speed ratio is two. These are dimensionless native generator and lattice units, not measured physical speeds.

This is a degree-zero second-order branch of the assembled chain system. It does not establish that a general scalar-only initial datum stays in degree zero under the first-order generator. The closed second-order scalar equation follows from A squared. Vector, higher-form, gauge and gravitational interpretations are not computed here.

## Conditional isotropic embedding theorem

Supply an invertible embedding E with positive unit determinant. If physical coordinates are x = E n, then q = E transpose k, and the leading scalar symbol in those coordinates is E S E transpose.

Require isotropic leading propagation as an added criterion:

```text
E S E^T = kappa I
det(E) = 1
```

Since S is positive definite, all solutions have E = sqrt(kappa) R S to the power minus one half, with R a proper orthogonal matrix. Thus G = E transpose E = kappa S inverse is unique up to overall scale when volume is not fixed, and unique as a Gram matrix after unit volume normalization. Taking determinants gives kappa cubed = det S = 32.

```text
kappa = 2^(5/3)
G = 2^(2/3) (I - J/4)
Gii = 3 * 2^(2/3) / 4
Gij = -2^(2/3) / 4, for i != j
cos(basis angle) = Gij / sqrt(Gii Gjj) = -1/3
basis angle = approximately 109.4712206 degrees
```

This fixes a ratio under a supplied isotropy criterion. It does not demonstrate that the original UD evolution dynamically selects G. Unit volume is a reference normalization and supplies no physical absolute scale.

## Body centered cubic representation and symmetry

One explicit positive determinant embedding is:

```text
t = 4^(-1/3)
E = t (J - 2I)
a = t (-1,  1,  1)
b = t ( 1, -1,  1)
c = t ( 1,  1, -1)
```

The generated integer coordinates have all three Cartesian components of the same parity. Conversely every such integer triple has an integer preimage, because the inverse of J minus 2I is (J minus I) divided by two. The lattice is therefore the union of 2t times the integer cubic lattice and its translate by t times 111: precisely a body centered cubic lattice.

The six tetrahedra remain congruent, with squared edge signature 3, 3, 3, 3, 4, 4 before multiplication by t squared. Each has four edges of length sqrt(3) t and two opposite edges of length 2t. They are nonregular disphenoids, with long to short edge ratio 2 divided by sqrt(3). Each cell volume is one sixth in the normalized primitive parallelepiped.

One selected block has twenty-four abstract tetrahedral automorphisms and twelve cube-metric symmetries. Under the BCC embedding, all forty-eight signed Cartesian permutations preserve the entire periodic lattice and the simplex orbits in every degree. This is a symmetry of the repeated complex, not forty-eight symmetries of one selected primitive block. It is also a finite cubic symmetry, not continuous rotational or Lorentz symmetry.

## Residual finite wavelength anisotropy

The fourteen physical graph neighbors are eight vectors t times the sign triples and six vectors along the coordinate axes with length 2t. Consequently the scalar dispersion has the exact form:

```text
omega(k)^2 = 14
             - 8 cos(t kx) cos(t ky) cos(t kz)
             - 2 [cos(2t kx) + cos(2t ky) + cos(2t kz)]
```

Its quadratic term is isotropic, but its quartic term is:

```text
-t^4 [(5/3)(kx^4 + ky^4 + kz^4)
      + 2(kx^2 ky^2 + kx^2 kz^2 + ky^2 kz^2)]
```

At fixed wavevector magnitude r, the quartic correction is minus 5t to the fourth r to the fourth divided by three along a Cartesian axis, and minus 11t to the fourth r to the fourth divided by nine along the Cartesian body diagonal. The difference prevents an exact all-wavelength isotropy claim. Refinement or a source-selected correction remains a separate task.

## Evidence and replay

The verifier uses only the Python standard library. It records 457 exact constructor checks and three numerical evaluations of equivalent dispersion formulas. Exact checks cover integer and rational incidence, rational ranks, face cancellation, Laurent-polynomial nilpotency, fixed-volume metric ambiguity, conditional Gram identities, congruent edge signatures and all forty-eight BCC point symmetries. The numerical checks are supplemental formula smoke checks; they are not time integration, physical simulation, experiment or independent review.

```text
python verify_ud_cubic_macrocell_v0_1.py --output-dir replay
```

UD_CUBIC_MACROCELL_CARRIER_v0.1.json contains the finite simplex and sparse incidence data and the periodic Laurent boundary entries. UD_CUBIC_MACROCELL_RESULTS_v0.1.json records the checks and exact expressions. The manifest locks the included report, verifier and JSON bytes. Archive transport does not confer canonical promotion.

## Correspondence packet and retained risks

Internal object: declared six-simplex macrocell, assembled incidence generator and degree-zero scalar branch. Internal carrier: finite affine tetrahedral complexes and their translation invariant periodic extension. Internal claim bin: exact constructor and conditional metric mathematics; candidate UD carrier and metric selection interface. Proposed external object: a spatial lattice with isotropic leading scalar propagation. Shared structure: simplicial gluing, conservative reversible evolution, positive quadratic wave symbol and finite cubic symmetries. Candidate map: use the declared physical embedding E to identify lattice positions and wavevector components. Correspondence status: FORMAL_CORRESPONDENCE. Physical promotion: 0.

Added premises: the periodic extension, unit chain pairing, nonsingular spatial embedding, isotropic leading scalar criterion and reference unit covolume. Open quantities and laws: source admission of the carrier, selection of E, absolute length and time scale, reciprocal support burden coupling, stock geometry coupling, identification of other branches, continuum behavior and empirical discriminators.

| Retained failed route | Failure mode | Mitigation and replay condition |
|---|---|---|
| Seven visible positions imply seven solids | Projection merges two diagonal endpoints | Reconstruct four distinct spatial vertices per cell and compare total volume |
| Six regular tetrahedra fill the reference cube | Reference edge signatures are unequal | Replay every squared-edge signature |
| Equal symmetry counts identify symmetry groups | Abstract assembly and a single tetrahedron have different group structure | Preserve the objects acted upon and metric labels |
| A cubic block automatically gives isotropic propagation | Reference scalar symbol has eigenvalues eight and two | Replay the exact periodic stencil and quadratic symbol |
| Isotropy compatibility derives the native metric selector | Isotropy was supplied as a criterion | Require an admitted source selector for the conditional Gram shape |
| Leading isotropy establishes all-wavelength isotropy | Quartic axis and diagonal coefficients differ | Replay the exact cosine symbol and directional expansions |
| A larger finite reversible carrier explains irreversible relaxation | Finite autonomous skew recurrence survives enlargement | Keep the existing recurrence obstruction and declare any changed source premise |

## Next development gate

Test whether the inspected UD source admits and selects this Gram shape without fitting a desired propagation speed or angle. A symmetry argument alone must distinguish the full periodic cubic symmetry from the smaller symmetry of one primitive block. If an isotropy condition is supplied externally, retain this result as a conditional correspondence constructor.

The next executable comparison should compute the remaining chain branches and the leading corrections for compatible alternate carriers or refinements. It should keep the unit pairing baseline fixed before introducing any geometric weighting. A proposed metric or current amendment must also preserve the existing support burden separation, stock conservation scope and recurrence limitation.

## Replay artifacts

[Replay archive](library-file:libfile_3e5d4d9db7208191847f62799c00a0a1)

[Exact results](library-file:libfile_53ab9ce5428081919a513c97ce74e288)
