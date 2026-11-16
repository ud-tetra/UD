# Revised Manuscript Reproducibility Supplement — AW5 chapter

**EXACT_INTERNAL.** All replays use ascending simplex orientation and unit simplex inner products. The child orientations in the local proof can be chosen coherently by diagonal sign changes. Constructor verification. Independent review open. **Physical Promotion = 0.**

## Carriers and shared probe faces

Start from hub 0123 and its four leaves 1234, 0235, 0136, 0127. The filled carrier uses all five cells. The hollow carrier deletes just the hub volume, retaining its four triangular faces. The external probe mask P selects the same twelve outer triangles throughout. The hollow complex has four additional boundary triangles on the cavity.

## Heat trace and its control

With signed boundary maps B₂ and B₃, the degree-2 Laplacian is L₂ = B₂ᵀB₂ + B₃B₃ᵀ. Filled and hollow carriers have the same B₂, so their common im B₂ᵀ trace contribution cancels. On ker B₂ their spectra are (2,4,4,4,6) and (0,4,4,4,4). Therefore the hollow-minus-filled heat trace is

$$
(1-e^{-2t})(1+e^{-4t})=4t-12t^2+O(t^3).
$$

Its limiting value is 1. For the filled control, replace 0123 and 1234 by 0124, 0134 and 0234. This bistellar move preserves the boundary and the local ball. Face count changes from 16 to 18 and Tr L₂ changes from 68 to 78. The flipped-minus-filled per-face trace starts at zero with slope −1/12. Both raw long-time face traces are zero. The raw limiting heat trace measures b₂; finite-time traces depend on the operator and metric.

## Boundary-fixed stellar refinement of hollow AW5

For every selected leaf, insert a fresh interior vertex and replace that tetrahedron by the four cones over its boundary faces. This subdivides a ball relative to its full boundary. All four cavity faces and twelve exterior probe faces persist. The refined complex has b₂=1. At m refined leaves its face count is 16+6m.

Write z for the oriented cavity shell and D for the top boundary of the carrier under test. Its harmonic representative is h=z−D(DᵀD)⁻¹Dᵀz. Distinct leaves do not share faces, so DᵀD separates into leaf blocks. In an original leaf, the Gram is [4]. After subdivision, coherently oriented children have Gram 5I₄−J₄, with inverse (I₄+J₄)/5, where J₄ is the all-ones matrix. The shell meets only the child based on the cavity face, with unit signed incidence. The harmonic cavity coefficient magnitude is therefore 3/4 in an original leaf and 3/5 in a refined leaf. The three exterior coefficients in each leaf keep their signs and have magnitude 1/4 or 1/5 respectively. Since h is the orthogonal projection of z, ||h||² = zᵀh = 3−3m/20.

For a unit exterior drive/readout q, the collocated zero-frequency residue is R(q)=(qᵀPh)²/||h||². Let q₀ be the unit exterior pattern aligned with the unrefined mode. Keep this drive fixed across the series. The alternative matched pattern may be recomputed for each refinement. Exact formulas are

$$
R(q_0)=\frac{20-m}{80},\qquad
\max_{\|q\|=1,\,Pq=q}R(q)=\frac{100-9m}{20(20-m)}.
$$

| Refined leaves | b₂ | Original exterior drive | Best aligned exterior drive |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 1/4 | 1/4 |
| 1 | 1 | 19/80 | 91/380 |
| 2 | 1 | 9/40 | 41/180 |
| 3 | 1 | 17/80 | 73/340 |
| 4 | 1 | 1/5 | 1/5 |

For a single refinement, the maximum residue attainable by an exterior unit pattern orthogonal to q₀ is 3/1520. This is the squared exterior overlap left after projecting away from q₀, divided by ||h||². It permits leakage into some old orthogonal controls. Each specific control requires its own projection calculation. The first-order exterior damping slope of the simple face-accessible pole is minus the best aligned residue because the damping projector is P.

The Betti count is preserved in this test. The exterior residue changes under the declared choice to use unit simplex weights on every refined carrier. This does not settle whether another metric and a readout transfer can make the residue stable under refinement.

## Reproduce

Run `python3 refine_aw5.py` with SymPy 1.14. The script loads the neighboring heat-trace capture to replay the original and flipped face spectra, then checks the exact boundaries, harmonic rank, and exterior residues for the five refinement configurations. See `replay.txt`.
