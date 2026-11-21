# Spin transition across the shared face of \(K_-^{(A)}\)

**Disposition:** Exact for the declared finite transport model. A native spin connection or frame-history law remains open. **Physical Promotion = 0.**

Let \(L=[0123]\), \(R=[0124]\), and \(F=[012]\), all written with increasing vertex labels. Use \(L-R\) as the coherently oriented top chain. The signed coefficient of \(F\) is \(-1\) from \(L\) and \(+1\) from \(-R\). Use the same orientation of each simplex of \(F\) when restricting either cell. These conventions separate incidence signs from the spin transition.

## Transition and matching

Use a complex spin doublet \(S=\mathbb C^2\) in each cell. For the two congruent regular tetrahedra choose a common ambient oriented frame. The geometric face identification fixes \(0,1,2\). With the common frame its rotational transition is the identity, with lifts \(U_{RL}=\pm I_2\). In separate right-handed cell frames the coordinate rotation is \(R_R^{-1}R_L\), where \(R_c\) maps the coordinates of cell \(c\) into the common frame. Choosing spin frames \(s_c\) above \(R_c\) gives an explicit lift and its reciprocal,
\[
U_{RL}=s_R^{-1}s_L,\qquad U_{LR}=U_{RL}^{-1}.
\]
The other lift is obtained by negating one spin frame. Arbitrary oriented coordinate frames use \(\mathrm{Spin}(3)\); the discrete frame history within each cell may use the declared \(2T\) embedded in it.

In degree \(p\), let \(r_L,r_R\) restrict cochains to \(F\). For compatible traces,
\[
r_R\Psi_R=(I_{C^p(F)}\otimes U_{RL})\,r_L\Psi_L .
\]
This condition is empty in degree three. Constant \(U_{RL}\) commutes with the coboundary on \(F\). Transporting the right trace into the left frame makes the signed internal-face sum \(-r_L\Psi_L+(I\otimes U_{LR})r_R\Psi_R=0\) on the degree-two face. The same convention gives the covariant difference of edge traces; with spin-scalar Whitney metric its squared norm is invariant under a frame change.

For a coordinate change \(\Psi_c'=h_c\Psi_c\), the transition becomes \(U_{RL}'=h_R U_{RL}h_L^{-1}\). Taking \(h_R=U_{RL}^{-1}\), \(h_L=I_2\) removes the sole transition. In particular, components on opposite sides can differ by a minus sign in one convention while describing the same trace. An outward-normal reversal in the oriented boundary contributes an incidence convention independently of this frame choice.

## Closed transport and an internal readout

The cell adjacency graph has two nodes and one reciprocal edge. Every closed walk crosses the seam an even number of times and each backtrack cancels as \(U_{LR}U_{RL}=I_2\). More generally both cells and their common face contract to vertex \(0\) with a compatible straight-line homotopy, so the filled two-cell space is contractible. Flat transport on the filled base has trivial closed-path holonomy, including on exterior loops. A boundary twist, removed defect, or nonflat connection changes those premises.

Suppose a separately prescribed local frame history \(w\) returns the geometric face labels to themselves and lifts to \(-I_2\) in \(L\). Comparing paths from the same nonzero trace \(v\), the direct crossing gives \(U_{RL}v\), while the crossing after \(w\) gives \(U_{RL}(-I_2)v=-U_{RL}v\). Traversing the same history in the transported frame gives the same result since
\[
U_{RL}(-I_2)U_{RL}^{-1}=-I_2 .
\]
Thus a relative central sign already carried by a frame history can be read on the internal face with matched coherent paths and a common reference. It is preserved across the face and requires no exterior boundary. An isolated endpoint has sign-invariant norm and density operator. A single reciprocal crossing cannot create this relative sign.

| Model | Loop sign from the seam | Internal comparison |
| --- | --- | --- |
| Flat gluing on the filled two-cell base | \(+I_2\) on every closed base path | Sole transition can be made identity |
| Prescribed frame history ending at the central \(-I_2\) | History contributes \(-I_2\) | Direct and history-bearing arrivals differ by a relative minus sign |

The second row concerns a loop in frame space with specified lift, as in the length-12 word construction. The ordinary tetrahedral cochains see its identity projection. A base-space realization would need an explicit independent transport law and loop, beyond the two-cell adjacency data. No physical fermion statistics follow.

## Replay and related reference

The adjacent standard-library replay checks incidence cancellation, frame covariance, reciprocal crossings and central sign preservation using all 24 binary tetrahedral elements. It also replays the exact unsigned and signed projector fixtures in the companion reference.

- [Local systems and monodromy, Chapter 8](https://webhome.auburn.edu/~hks0015/cxarr.pdf)
