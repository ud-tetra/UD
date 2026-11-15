# AW5 filled and hollow star — offline intake and exact audit

Status: EXACT within the stated simplicial model. Constructor replay. Independent review OPEN. Physical Promotion = 0.

## Source and construction

Intake source is the user-supplied offline LLM report on the 5-Cell Regional Complex Survey, Central-Cell Star / Core-Star, and its hollow variant. Offline citation keys 83, 86, 91, 98, 103, 121, 122, 714, 736, 739–743, 842 and 848 have no bibliography or source files in the submission. The numeric keys remain unresolved. The archived [UD Theory Narrative Manuscript v0.15](https://github.com/ud-tetra/UD/blob/634d1ef6dd173bb73adb8d106fb995a19cc08858/docs/UD_Theory_Narrative_Manuscript_v0.15.pdf), §7.4 and Theorem 6.5, independently identify the filled benchmark and clarify the source memory claim. The audit below replays the mathematics directly. The linear face-sharing chain and central-edge pentagonal bipyramid (PB5) are comparison leads from the intake and were outside this replay.

Let the hub be (0,1,2,3). Attach a tetrahedron to each hub face opposite i, using distinct apex 4+i. Take downward simplicial closure. The hollow variant deletes only the hub 3-simplex. The four hub faces remain as faces of leaves. Leaf pairs intersect in one hub edge with its endpoints. The six edges form the K4 graph and remain part of the complex's triangular faces.

Use ascending vertex orientation, unit simplex inner products, signed incidence maps D_k and A = B^T − B with B the graded boundary. The comparison uses native dimensionless flow parameter s in U(s) = exp(sA).

| Quantity | Filled | Hollow |
| --- | --- | --- |
| f-vector | (8,18,16,5) | (8,18,16,4) |
| Graded chain dimension | 47 | 46 |
| Boundary ranks D1,D2,D3 | (7,11,5) | (7,11,4) |
| Betti vector | (1,0,0,0) | (1,0,1,0) |
| Eigenvalues of D3^T D3 | 2, 4 (triple), 6 | 4 (quadruple) |

## Cavity and harmonic projection

Each attached leaf retracts onto its base face, fixing that face and hence the leaf intersections. The filled complex retracts to the hub, and the hollow complex retracts to the hub boundary S². The signed cavity shell z = D3_filled e_hub is therefore a closed representative of the new H2 class.

For hollow D3, the four columns are orthogonal with squared norms 4, and D3^T z has entries ±1. Thus z fails co-closure. The harmonic representative in the same class is h = z − D3 D3^T z/4. Its hub-face coefficients have magnitudes 3/4 and its outer-face coefficients have magnitudes 1/4. It has nonzero support on all 16 triangles. Its squared norm is 3. The conserved coefficient under the undamped linear skew flow is a mathematical observable once a readout is defined.

## Spectra and recurrence

Both characteristic polynomials include Q = (λ⁴+9λ²+16)³(λ⁴+10λ²+20)³. The filled polynomial is λ(λ²+2)(λ²+3)²(λ²+4)³(λ²+5)³(λ²+6)² Q. The hollow polynomial is λ²(λ²+3)²(λ²+4)⁴(λ²+5)³(λ²+6)Q. By boundary nilpotency, the nonzero squared frequencies are the union of nonzero spectra of D_k^T D_k. The single tetrahedron has polynomial λ(λ²+4)⁷ and global recurrence π. Both stars contain frequencies √3 and √5, so neither has a finite positive full-state identity recurrence. Individual frequency sectors still recur. The calculation does not settle clock mechanisms or all glued complexes.

The filled top Gram has a three-dimensional leaf-difference subspace at eigenvalue 4 and two symmetric hub/leaf modes at 2 and 6. The hollow top Gram is 4I₄, giving four independent leaf modes including the symmetric combination. Its invariant volume/face sector decouples across leaves. The full graded generator includes shared lower-dimensional coordinates, so top Gram diagonality alone cannot establish an exclusive exchange law for arbitrary initial states or with added interactions.

## Boundary readout and copied-register observability

On the filled real A² = −qI sectors for q=3,5, the outer-face projection compressed to the sector has eigenvalues 0 and 1 with equal multiplicities (2+2 and 3+3 respectively). Peak face-side coordinates lie entirely on exterior triangles. The complementary edge-side quadrature has zero instantaneous face projection but rotates into the face side under A. For damping −γP_face with γ>0, no nonzero trajectory confined to either sector stays dark for an entire cycle. The split does not establish protected core trajectories or physical radiation.

Five independent copied tetrahedron registers total 75 coordinates. With the signed, consistently oriented simplex-sum map P onto the 47 unique coordinates, rank P = 47 and dim ker P = 28. The first-jet matrix [P; PA_copy] has rank 75, so this readout plus its exact first derivative already reconstructs the copied state. The archived Theorem 6.5 uses a normalized signed sum, which differs from P by invertible row scaling. The ranks therefore agree. Its 28-coordinate bound is for an autonomous linear realization that retains the 47 snapshot coordinates, with arbitrary copied initial states and linear initial encoding. The full trajectory has observation rank 75, so such a realization needs 75 total states, or 28 additional states. When the initial derivative is supplied, the pair already determines those states. The offline wording conflated the realization dimension and the information supplied by the first jet.

Replay: python3 aw5.py (SymPy 1.14). See replay.txt for constructor output.
