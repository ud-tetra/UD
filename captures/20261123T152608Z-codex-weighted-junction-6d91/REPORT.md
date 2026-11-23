# Weighted junction transfer and lossless memory

**EXACT_INTERNAL / PASS_SCOPED_CONTROL / OPEN_CONSTITUTIVE_SOURCE. Physical Promotion = 0.**

Dependencies are [UD #610 at a208971](https://github.com/ud-tetra/UD/tree/a208971023cad92a30dd2f2f6e3a805a91970708), [UD #609](https://github.com/ud-tetra/UD/pull/609), [UD-Physics #458 at e548441](https://github.com/ud-tetra/UD-Physics/tree/e548441f33087407159babf6e2b1e3dadc766f82), and [UD-Physics #457](https://github.com/ud-tetra/UD-Physics/pull/457). This is follow-on constructor evidence. The earlier repository and review evidence refers to those earlier revisions.

## Conditional 3D transfer

Use the antipodal regular tetrahedra, with shared vertices introduced by six prescribed midpoint identifications. Split edges, cone each subdivided face boundary from a private face center, then cone each subdivided tetrahedron boundary from a private interior vertex. The column counts are (1,2,6,24) in degrees 0 through 3. The cone identity and boundary-square-zero give B' Phi = Phi B. Set the target diagonal weights to the reciprocal column count on each child and to 1 on unused rows. Column supports are disjoint in each grade, so Phi^T W Phi = I. This metric is a chosen contract. No source-derived metric or event is implied.

The full target has simplex counts (24,100,120,48), 292 total coordinates and Betti numbers (1,5,0,0). The graph-only Betti number from the earlier audit refers to a different complex. With one shared midpoint, the two filled, contractible packets meet at one point and have b1=0.

## TEST-PRE-AUTH-01

Fix the same six exact midpoint contacts in every run. For the benchmark only, maximize the score c_A(e)^2 c_B(opposite(e))^2. A unique positive winner identifies that pair. Zero throughput in the benchmark or a tied maximum gives HOLD. Lists below give the only nonzero edge coefficients.

| A | B | Outcome |
| --- | --- | --- |
| 01:1 | 23:1 | 01 ↔ 23 |
| 02:1 | 13:-1 | 02 ↔ 13 |
| 01:1, 02:1 | 23:1, 13:1 | HOLD |
| 01:1 | 02:1 | HOLD |

The two positive preparations both have quadratic stock 2. This is an exact selector control with constructed outcomes, not an independently observed or blinded junction event.

## Resolvent and back-reaction

Use A = B' - W^(-1) B'^T W on the full target, L = Phi^T W, P = Phi L and Q = I - P. The ordinary-transpose generator fails weighted skew-adjointness on an old vertex/half-edge with weights 1 and 1/2. A is W-skew-adjoint. In retained coordinates and the W-orthogonal complement define H = L A Phi, G = Q A Phi, D = Q A Q restricted to im Q. The exact blocks are [H, -G^T W; G, D]. The chain identity and weighted isometry give H = B - B^T. D is W-skew-adjoint, so its 262 eigenvalues lie on the imaginary axis, including any zero modes, and its spectral abscissa is zero.

For Re(z)>0, the retained resolvent is [z I-H+G^T W (z I-D)^(-1) G]^(-1). With prepared transverse data zero, the time-domain memory term is convolution with M(s) = -G^T W exp(sD) G. For arbitrary transverse initialization, add -G^T W exp(sD) q(0). The rational replay gives M(0)_{0,0}=-7 for the first old vertex in the explicitly chosen metric. This proves genuine transverse coupling and a nonzero return term. The corresponding scalar entry is a nonzero finite sum of pure oscillations (constant terms allowed) and cannot decay to zero. The matrix kernel consequently has at least one visible imaginary-axis pole. No damping or fitted coefficient was inserted. Individual pole locations and residues are not tabulated.

## Source-facing candidate

Let E(x) contain pre-event transverse interior contacts with an eligible C06 route and Q_T,e = 0. If the pinned source supplies a comparable nonnegative through-stock observable for those contacts, use its unique strictly positive maximum as a candidate for event selection, with HOLD on ties or no positive value. Q_T,e = 0 is a closure filter. The candidate depends on a declared pre-event route-use map and a separate source axiom that licenses writing new incidence. Existing support coefficients are not substituted for authenticated C06 throughput. Thus the fixture cannot close native authorization. Require a prospective matched-geometry test using authenticated route/closure data and independently recorded outcomes before advancing the claim.

## Replay and handoff

Run python3 replay.py with SymPy and compare stdout to replay-results.txt. Exact rational checks cover the fixture, chain and Gram identities, Betti numbers, skew-adjointness and the first-return witness. Next, bind the selector to authenticated pre-event route/closure receipts or document the source obstruction if none supply the required observables. Resolve the current PRs under their own review and merge holds.
