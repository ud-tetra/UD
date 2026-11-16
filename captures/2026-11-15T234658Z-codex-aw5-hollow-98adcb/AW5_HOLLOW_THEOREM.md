# AW5 hollow star — topology and first-jet observability

**EXACT_INTERNAL.** Unit simplex inner products and consistently oriented bases. Constructor verification. Independent review open. **Physical Promotion = 0.**

## Native carrier

Take hub vertices 0,1,2,3 and one tetrahedral leaf per hub face, with a distinct apex on each leaf. The hollow complex is the downward closure of the four leaves. Its graded basis sizes are (8,18,16,4), totaling 46. Each leaf retracts onto its base face while fixing that face, so the hollow complex retracts to the hub boundary S². Its Betti vector is (1,0,1,0).

Let z be the oriented cavity shell and D the hollow top boundary map. The leaf columns have disjoint face support, DᵀD = 4I, and Dᵀz has entries ±1. The harmonic representative h = z − DDᵀz/4 is co-closed and closed. Its absolute coefficients are 3/4 on the four inner faces and 1/4 on the twelve exterior faces. Its squared norm is 3 and its exterior squared-norm fraction is 1/4. The coefficient of h is conserved under the native undamped skew flow. Exterior-face damping couples to h in the declared toy model. An identification with physical charge or flux remains open.

In the **filled** star, the real squared-frequency sectors q = 3 and 5 have dimensions 4 and 6. The compressed exterior-face projector has eigenvalues 0 and 1 of equal multiplicity in each sector. The edge quadrature has zero instantaneous face readout and evolves into the exterior face quadrature. This result concerns those two filled-star sectors and instantaneous overlap.

## Copied dynamics and exact recovery

Choose either four independent tetrahedral leaf registers (60 coordinates), or those same registers plus an independent copy of the 14-coordinate hub boundary (74 coordinates). The shell block is a modeling choice with its own truncated incidence generator. The native hollow generator acts on a separate 46-dimensional space. For copied dynamics let G be the block-diagonal sum of the local skew generators and P the oriented simplex-sum onto the unique hollow coordinates.

| Copied model | rank P | dim ker P | rank [P; PG] |
| --- | ---: | ---: | ---: |
| Four leaves | 46 | 14 | 60 |
| Four leaves and independent shell | 46 | 28 | 74 |

**Proof.** P is surjective because every simplex has a copy. Suppose Px = PGx = 0. Each leaf's apex-containing coordinates are private, so Px = 0 makes them zero. For each nonempty base simplex σ, its coned simplex σ ∪ {apex} is private. In the derivative of that private coordinate, all terms involving other private coordinates vanish, leaving a signed unit incidence coefficient multiplying the leaf's copy of σ. Hence PGx = 0 forces all its base coordinates to vanish. After all four leaf blocks vanish, any independent shell block is zero because its sum readout is injective. Thus the first-jet map is injective in both models.

The exact initial pair (y, ẏ) determines the entire copied initial state and therefore its trajectory under the declared generator. If an autonomous linear realization retains y as 46 visible state coordinates, has linear initialization, and reproduces the entire visible trajectory for arbitrary copied initial conditions, it needs at least as many states as the observation rank. The copied dynamics attain the bound in a basis extending P. Thus the minimum additional state is 14 for the leaves-only model and 28 for the explicit shell-copy model. The exact derivative already carries the missing information when supplied at initialization.

The archived UD Theory Narrative Manuscript v0.15, Theorem 6.5 and §7.4, supplies the filled stacked-family and spectral antecedents. The hollow-shell result here is proved separately. The offline numeric citation keys supplied with the intake lack a bibliography. Replay with Python and SymPy 1.14 by running `python3 hollow_jet.py`. The replay also prints the antecedent results from the sibling AW5 capture.
