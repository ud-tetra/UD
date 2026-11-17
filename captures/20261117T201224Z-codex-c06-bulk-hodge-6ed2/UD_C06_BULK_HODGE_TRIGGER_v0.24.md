# C06 bulk incidence and Hodge trigger v0.24

**EXACT / CONDITIONAL** for rank, signed incidence, and complementary projector identities. **CANDIDATE** for use of the projector in a shared event. **Physical Promotion = 0.**

## The single bulk cell

Use the v0.23 unsigned face-sum readout \(H:X\to\mathbb R^4\) on the mean-zero ordinary-edge carrier \(X\). Its odd image is \(\mathbf1^\perp\), and \(H^\mathsf TH=2P_-\) on \(X\). Take the regular unit-cell convention and equal Euclidean face weights used for this projector. In coherently outward-oriented boundary face coordinates the signed map \(\partial_3\) of the single oriented 3-cell is the column \(\mathbf1\). In increasing simplex coordinates it is the alternating sign column, which gives the same rank after changing face orientation. Signed boundary operators obey \(\partial_2\partial_3=0\).

A reciprocal linear correction routed solely through one scalar bulk state factors through a one-dimensional space. Its rank is at most one, including a static elimination with scalar invertible response. It cannot supply the rank-three v0.23 change. In the specific common-face channel the result is stronger. With \(Q=\mathbf1\mathbf1^\mathsf T/4\), \(QH=0\) on \(X\) and thus \(H^\mathsf TQH=0\) there.

The complementary map \(I_4-Q\) is rank three and
\[
P_-=\tfrac12 H^\mathsf T(I_4-Q)H .
\]
The bulk incidence identifies the direction to remove in face coordinates. The identity term retains the three independent boundary directions. Computing this projector therefore has a face-channel realization, but it cannot be implemented as a correction passing only through the single bulk scalar. The argument does not bound a cell that carries additional independent internal variables or acts directly on its incident faces.

## Boundary Hodge star

For a two-dimensional boundary, the discrete star sends primal face cochains to dual vertex cochains. It uses a metric and identification with the dual cells. In the equal-weight regular-cell comparison, representing the star by a common nonzero weight times the primal-to-dual relabeling gives a scalar Gram after identifying the dual coordinates. The map does not select the face common-mode complement on its own. Combining the face metric with removal of the bulk direction gives the preceding projection, and its incidence pullback supplies the exact v0.23 cut \(G(I_X-P_-)\). The unsigned sum \(H\) here is the declared face observable. The signed differential \(\partial_2\) computes a different operator. The earlier Whitney Hodge energy audit in UD-Physics #405 also distinguishes the static energy from a constitutive port update.

The incidence and fixed star data are identical before and after first balance for an unchanged tetrahedron. The v0.21 record-only branch and the candidate commit-and-cut branch both satisfy these same data and stock conservation. This is a scoped trigger underdetermination, leaving open a native state-dependent rule or additional cell dynamics. No native authority, timing, or Stage 2 rule is inferred.

## Replay

Run python3 replay_c06_bulk_hodge.py. Checks use exact signed simplex boundaries, unsigned face Gram, a rational complement, and mean-zero edge witnesses. The inverse-free static rank argument is analytic.
