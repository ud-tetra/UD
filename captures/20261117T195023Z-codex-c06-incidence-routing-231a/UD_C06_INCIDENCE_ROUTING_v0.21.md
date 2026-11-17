# C06 incidence routing and commit scope v0.21

**EXACT / CONDITIONAL** for the incidence readout and actuator independence. **CANDIDATE** for synchronous cell-level commit. **Physical Promotion = 0.**

## Incidence supplies the opposite-edge difference

Let \(H\) be the unsigned face-by-edge incidence of a tetrahedron, \(O\) the opposite-edge involution and \(J\) the all-ones matrix on six edges. Two distinct adjacent edges share one face, opposite edges share none, and each edge has two faces. Consequently
\[
H^\mathsf T H=I+J-O,\qquad P_-=(I-O)/2.
\]
For mean-zero ordinary-edge data \(z\), \(Jz=0\). The two raw face sums incident to \(e\), when added at \(e\), give \((H^\mathsf THz)_e=z_e-z_{O(e)}\). This is an edge-to-face-to-edge calculation. A direct link between opposite edges is unnecessary for the algebraic readout. One face alone is insufficient on the entire mean-zero space: keep all three face-edge values fixed, change the opposite edge, and compensate on another unseen edge. Without the mean-zero constraint the two-face sum includes the total edge sum, which must be subtracted.

The v0.20 copy map \(S\) is the forward map in flag coordinates. The closed port evolves \(\dot y=Sx\), so empty initial flags stay in \(S(\mathbf1^\perp)\). The metric \(M\) enters the adjoint and the source Gram \(S^\mathsf TMS\). If flags are expressed as dual coordinates \(My\), their velocity is \(MSx\) and the raw two-flag rule still refers to the primal coordinates. On copied records \(y=Sz\), the normalized odd coordinate is \(\omega_-(z_e-z_{O(e)})/\sqrt2\) with \(\omega_-^2=106/9\) in the declared unit-cell model. The unsigned face sums can be formed directly from cooriented primal flags on each face. This derivation preserves the v0.20 off-range limitation. The flag shortcut need not fail on every off-range vector, but fails as a universal readout there.

## Shared actuation remains a transition law

The 3-cell contains the six edges and all four faces. It gives a common support for a candidate transition. Incidence does not fix the rate or execution semantics of that transition. Compare two extensions with the same incidence, copied range, incoming exchange and first directed crossing. One records the crossing and continues the same skew exchange. The other atomically records and selects \(GP_+\) as in v0.20. Both are compatible with the incidence identities and stock conservation. Their held odd stocks differ at any sufficiently small positive time after the event. Thus those structural constraints alone do not entail the cut.

For synchronous aggregation and a shared atomic Ready state, the face reduction can feed one commit as a candidate cell-level rule. The original ordered receipt tests only establish deduplication under a shared atomic arbiter. If a real aggregation delay \(\delta>0\) leaves the odd oscillator active after balance, the latched fraction is \(1/2+\sin(2\omega_-\delta)/2\) by the v0.17 flow calculation. This changes the fraction whenever \(2\omega_-\delta\notin\pi\mathbb Z\). Geometry supplies a finite stencil while a native timing and actuation law remains open. No coframe evolution or Stage 2 rule is assumed here.

## Replay

Run python3 replay_c06_incidence.py. Checks use exact integer face sums for arbitrary mean-zero edge inputs and nonzero-mean controls, single-face ambiguity and the copy-versus-dual witness. No timing or hardware claim is based on the finite replay.
