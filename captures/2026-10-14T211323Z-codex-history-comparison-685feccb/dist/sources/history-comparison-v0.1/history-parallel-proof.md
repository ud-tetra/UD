# Star versus barycentric refinement: exact parallel check

Status: exact conditional construction, constructor-team check. Physical promotion 0. Native adoption and independent human review remain open.

## Carriers and calibration

The center-star is the cone on the boundary of the oriented tetrahedron, with center vertex 4. Its f-vector is (5,10,10,4), total dimension 29. The subdivision map is the identity on old vertices, edges and faces, and sends 0123 to 0124 − 0134 + 0234 − 1234. The affine retraction sends center 4 to the average of the four original vertices and extends by exterior powers. Exact checks give BS=SB, RB=BR, RS=I.

For either history the conditional metric is H=RᵀR+QᵀQ, Q=I−SR. It makes coarse and residual sectors orthogonal, retaining the old unit metric on the coarse code and the Euclidean metric on ker R. This is a selected mathematical calibration premise, not a recovered native physical metric law.

The star has 14 detail directions, in degrees (1,4,6,3). Its detail boundary ranks are (1,3,3). Each detail Laplacian satisfies L²=5L, and its restriction to detail is 5I. Therefore its full skew generator has characteristic polynomial λ(λ²+4)^7(λ²+5)^7. The coarse harmonic direction is retained.

## Spectral capacity does not settle covariance

The barycentric history has 134 detail directions. Its exact squared-frequency-5 eigenspaces have graded dimensions (2,7,8,3): ten positive/negative √5 pairs. Thus frequency capacity allows a full 29-to-149 generator isometry, without symmetry constraints. It also allows a graded chain isometry: the √5 singular-pair counts across boundaries are (2,5,3), versus the star's (1,3,3). These existence statements use nonunique singular-vector choices; they do not select a local geometric comparison map.

The group check averages all 24 signed S4 actions to form the exact trivial-representation projector P₁ in each degree. The common kernel of L−5I and I−P₁ has dimensions:

| History | Degree 0 | Degree 1 | Degree 2 | Degree 3 |
|---|---:|---:|---:|---:|
| Star | 1 | 1 | 0 | 0 |
| Barycentric | 0 | 0 | 0 | 0 |

The star therefore has a trivial-representation √5 skew pair absent from barycentric detail. Barycentric coarse frequencies are only 0 and 2, so the missing pair cannot occur in its coarse code either. An S4-equivariant generator-intertwining isometry must preserve both the trivial representation and squared frequency 5, and cannot annihilate a nonzero source vector. Such a full isometry is impossible. The check does not forbid non-equivariant isometries or a differently calibrated target metric.

## Full-state and coarse comparisons differ

No terminal bijection exists between all 149 barycentric and all 29 star directions. The source-canonical coarse comparison C=S_star R_bary is exact on the common old code, but annihilates every one of the 134 barycentric details. It is not a full-state isometry, history-equivalence theorem or detail-preserving readout.

## No autonomous detail seed under exact inheritance

Let A be H-skew and let AS=S A₀ with SᵀHS=G. For a detail vector z H-orthogonal to im S, and any coarse c,

⟨Az,Sc⟩H=−⟨z,ASc⟩H=−⟨z,S A₀c⟩H=0.

Thus the detail complement is invariant, as is the coarse code: the decomposition reduces A. Starting from Sc with zero detail, autonomous evolution remains S exp(tA₀)c, with identically zero detail. A source law exciting detail must therefore supply a nonzero detail initial state, an external/open forcing or an explicitly modified generator that relaxes exact inheritance. Merely adding detail directions or their metric does not provide this law.

## Replay

The fresh checker constructs signed maps from simplex lists, imports the current generated barycentric map constructor (not archived executable source), verifies exact rational identities and obtains ranks through exact DomainMatrix elimination. Numerical eigenvalue samples are diagnostic only; exact nullities and group-projector intersections establish the stated frequency and covariance results.
