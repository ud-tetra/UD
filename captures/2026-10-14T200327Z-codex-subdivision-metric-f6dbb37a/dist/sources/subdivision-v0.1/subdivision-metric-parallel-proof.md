# Exact conditional metric completion for tetrahedral barycentric subdivision

Status: constructor-team exact verification. Conditional construction; native
metric selection OPEN; physical promotion 0. This is not an independent human
review receipt.

The checker was freshly written using only the Python standard library and exact
`Fraction` arithmetic. It does not execute imported or archived scientific code.

## Carrier and maps

Let K be the filled tetrahedron on vertices 0,1,2,3 with increasing orientations.
Let sd K have a vertex for each nonempty face F of K and a k-simplex for every
strict inclusion flag F0 < ... < Fk, oriented in inclusion order. Its face vector
is (15,50,60,24), so the real nonaugmented chain dimension is 149, compared with
15 for K.

For a k-simplex sigma, the ordinary signed subdivision map S_k sums its (k+1)!
maximal prefix flags over permutations of the vertices, with permutation signs.
Define the affine barycenter vector u_F = (1/|F|) sum_(v in F) e_v. The map R_k
sends a flag to u_F0 wedge ... wedge u_Fk. Its matrix coefficients are determinants
in the original increasing simplex basis.

The contraction of each u_F with the all-ones covector is 1. Exterior functoriality
therefore proves that R is a chain map. Ordinary signed subdivision is also a
chain map. The exact checker additionally verifies both identities on every
matrix coefficient and verifies R_k S_k = I for all four degrees. Equivalently,
the signed barycentric pieces reconstitute the original oriented simplex.

All 24 original vertex permutations commute with R and S, using their induced
signed action on the original oriented simplices and their inclusion-ordered
permutation action on barycentric flags.

## Conditional metric

For each degree define Q_k = I - S_k R_k and

    H_k = R_k^T R_k + Q_k^T Q_k.

This metric is not selected by the historical source law. It is a declared exact
completion of the three required compatibility conditions.

For every fine chain u,

    u^T H_k u = ||R_k u||² + ||Q_k u||²,
    u = S_k R_k u + Q_k u.

Consequently H_k is symmetric positive definite. Since R_k S_k=I and Q_k S_k=0,

    H_k S_k = R_k^T,
    S_k^T H_k S_k = I.

This gives exact norm preservation for the embedded coarse states. The metric
also remains invariant under the full signed S4 action; this was checked for all
24 permutations in every degree.

## Generator compatibility

Let B_k and B'_k be the coarse and fine boundary matrices. The fine metric adjoint
is B'_k† = H_k^(-1) B'_k^T H_(k-1). Since R is a chain map,

    H_k S_k B_k^T
      = R_k^T B_k^T
      = B'_k^T R_(k-1)^T
      = B'_k^T H_(k-1) S_(k-1).

Multiplication by H_k^(-1) proves B'_k† S_(k-1) = S_k B_k^T.
Together with B'_k S_k = S_(k-1) B_k, this proves

    A'_H S = S A

for A = boundary-adjoint minus boundary (or the opposite consistently chosen
sign). It also proves preservation of the corresponding constant-generator
evolution on the embedded image, without a time rescaling.

The proof does not assert equivalence of the full 149-dimensional fine generator
with the 15-dimensional coarse generator. The fine complement is present. The
embedded coarse norm and generator are exact; extra fine modes are not removed.

## Why factorial normalization is insufficient

The Euclidean Gram matrix of ordinary subdivision is

    S_k^T S_k = (k+1)! I.

Thus the naive degree metric H_k^naive=I/(k+1)! makes S isometric and leaves its
chain identity intact. But its weighted adjoint equals (k+1) B'_k^T, and the defect

    (k+1) B'_k^T S_(k-1) - S_k B_k^T

is nonzero in every positive degree:

| k | Defect rank | Nonzero entries | Largest absolute entry |
|---|---:|---:|---:|
| 1 | 4 | 40 | 2 |
| 2 | 6 | 84 | 3 |
| 3 | 3 | 96 | 3 |

Degreewise factors are 1, 1/2, 1/6 and 1/24, rather than a universal sqrt(2)
factor. Isometry and topological compatibility alone do not ensure dynamical
compatibility.

## Scope and costs

The completed H is rational and generally dense within a degree. It is not a
diagonal simplex-volume metric or an assertion of strictly local incidence
couplings. The largest denominators in degrees 0,1,2,3 are 9,48,576,576.

This remedy demonstrates mathematical feasibility after declaring a different
metric. It does not select that metric physically, prove a kinetic/potential
interpretation, establish a saturation threshold, or supply a clock/reset law.
Its 134 additional coordinates and possible nonlocal weighted adjoints remain
part of the finite-carrier accounting.

The verification passed 332 exact checks, including the negative controls above.
